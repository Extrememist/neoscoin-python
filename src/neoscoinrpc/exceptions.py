# Copyright (c) 2010 Witchspace <witchspace81@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
Exception definitions.
"""


class neoscoinException(Exception):
    """
    Base class for exceptions received from neoscoin server.

    - *code* -- Error code from ``neoscoind``.
    """
    # Standard JSON-RPC 2.0 errors
    INVALID_REQUEST  = -32600,
    METHOD_NOT_FOUND = -32601,
    INVALID_PARAMS   = -32602,
    INTERNAL_ERROR   = -32603,
    PARSE_ERROR      = -32700,

    # General application defined errors
    MISC_ERROR                  = -1  # std::exception thrown in command handling
    FORBIDDEN_BY_SAFE_MODE      = -2  # Server is in safe mode, and command is not allowed in safe mode
    TYPE_ERROR                  = -3  # Unexpected type was passed as parameter
    INVALID_ADDRESS_OR_KEY      = -5  # Invalid address or key
    OUT_OF_MEMORY               = -7  # Ran out of memory during operation
    INVALID_PARAMETER           = -8  # Invalid, missing or duplicate parameter
    DATABASE_ERROR              = -20 # Database error
    DESERIALIZATION_ERROR       = -22 # Error parsing or validating structure in raw format

    # P2P client errors
    CLIENT_NOT_CONNECTED        = -9  # neoscoin is not connected
    CLIENT_IN_INITIAL_DOWNLOAD  = -10 # Still downloading initial blocks

    # Wallet errors
    WALLET_ERROR                = -4  # Unspecified problem with wallet (key not found etc.)
    WALLET_INSUFFICIENT_FUNDS   = -6  # Not enough funds in wallet or account
    WALLET_INVALID_ACCOUNT_NAME = -11 # Invalid account name
    WALLET_KEYPOOL_RAN_OUT      = -12 # Keypool ran out, call keypoolrefill first
    WALLET_UNLOCK_NEEDED        = -13 # Enter the wallet passphrase with walletpassphrase first
    WALLET_PASSPHRASE_INCORRECT = -14 # The wallet passphrase entered was incorrect
    WALLET_WRONG_ENC_STATE      = -15 # Command given in wrong wallet encryption state (encrypting an encrypted wallet etc.)
    WALLET_ENCRYPTION_FAILED    = -16 # Failed to encrypt the wallet
    WALLET_ALREADY_UNLOCKED     = -17 # Wallet is already unlocked

    def __init__(self, error):
        Exception.__init__(self, error['message'])
        self.code = error['code']


class TransportException(Exception):
    """
    Class to define transport-level failures.
    """
    def __init__(self, msg, code=None, protocol=None, raw_detail=None):
        self.msg = msg
        self.code = code
        self.protocol = protocol
        self.raw_detail = raw_detail
        self.s = """
        Transport-level failure: {msg}
        Code: {code}
        Protocol: {protocol}
        """.format(msg=msg, code=code, protocol=protocol)

    def __str__(self):
        return self.s


##### General application defined errors
class SafeMode(neoscoinException):
    """
    Operation denied in safe mode (run ``neoscoind`` with ``-disablesafemode``).
    """


class JSONTypeError(neoscoinException):
    """
    Unexpected type was passed as parameter
    """
InvalidAmount = JSONTypeError  # Backwards compatibility


class InvalidAddressOrKey(neoscoinException):
    """
    Invalid address or key.
    """
InvalidTransactionID = InvalidAddressOrKey  # Backwards compatibility


class OutOfMemory(neoscoinException):
    """
    Out of memory during operation.
    """


class InvalidParameter(neoscoinException):
    """
    Invalid parameter provided to RPC call.
    """


##### Client errors
class ClientException(neoscoinException):
    """
    P2P network error.
    This exception is never raised but functions as a superclass
    for other P2P client exceptions.
    """


class NotConnected(ClientException):
    """
    Not connected to any peers.
    """


class DownloadingBlocks(ClientException):
    """
    Client is still downloading blocks.
    """


##### Wallet errors
class WalletError(neoscoinException):
    """
    Unspecified problem with wallet (key not found etc.)
    """
SendError = WalletError  # Backwards compatibility


class InsufficientFunds(WalletError):
    """
    Insufficient funds to complete transaction in wallet or account
    """


class InvalidAccountName(WalletError):
    """
    Invalid account name
    """


class KeypoolRanOut(WalletError):
    """
    Keypool ran out, call keypoolrefill first
    """


class WalletUnlockNeeded(WalletError):
    """
    Enter the wallet passphrase with walletpassphrase first
    """


class WalletPassphraseIncorrect(WalletError):
    """
    The wallet passphrase entered was incorrect
    """


class WalletWrongEncState(WalletError):
    """
    Command given in wrong wallet encryption state (encrypting an encrypted wallet etc.)
    """


class WalletEncryptionFailed(WalletError):
    """
    Failed to encrypt the wallet
    """


class WalletAlreadyUnlocked(WalletError):
    """
    Wallet is already unlocked
    """


# For convenience, we define more specific exception classes
# for the more common errors.
_exception_map = {
    neoscoinException.FORBIDDEN_BY_SAFE_MODE: SafeMode,
    neoscoinException.TYPE_ERROR: JSONTypeError,
    neoscoinException.WALLET_ERROR: WalletError,
    neoscoinException.INVALID_ADDRESS_OR_KEY: InvalidAddressOrKey,
    neoscoinException.WALLET_INSUFFICIENT_FUNDS: InsufficientFunds,
    neoscoinException.OUT_OF_MEMORY: OutOfMemory,
    neoscoinException.INVALID_PARAMETER: InvalidParameter,
    neoscoinException.CLIENT_NOT_CONNECTED: NotConnected,
    neoscoinException.CLIENT_IN_INITIAL_DOWNLOAD: DownloadingBlocks,
    neoscoinException.WALLET_INSUFFICIENT_FUNDS: InsufficientFunds,
    neoscoinException.WALLET_INVALID_ACCOUNT_NAME: InvalidAccountName,
    neoscoinException.WALLET_KEYPOOL_RAN_OUT: KeypoolRanOut,
    neoscoinException.WALLET_UNLOCK_NEEDED: WalletUnlockNeeded,
    neoscoinException.WALLET_PASSPHRASE_INCORRECT: WalletPassphraseIncorrect,
    neoscoinException.WALLET_WRONG_ENC_STATE: WalletWrongEncState,
    neoscoinException.WALLET_ENCRYPTION_FAILED: WalletEncryptionFailed,
    neoscoinException.WALLET_ALREADY_UNLOCKED: WalletAlreadyUnlocked,
}


def wrap_exception(error):
    """
    Convert a JSON error object to a more specific neoscoin exception.
    """
    # work around to temporarily fix https://github.com/neoscoin/neoscoin/issues/3007
    if error['code'] == neoscoinException.WALLET_ERROR and error['message'] == u'Insufficient funds':
        error['code'] = neoscoinException.WALLET_INSUFFICIENT_FUNDS
    return _exception_map.get(error['code'], neoscoinException)(error)
