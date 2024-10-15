# SNMP MIB module (MRV-IN-REACH-CHARACTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IN-REACH-CHARACTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:35 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(AddressType,
 DateTime,
 mrvInReachProductDivision) = mibBuilder.importSymbols(
    "MRV-IN-REACH-PRODUCT-DIVISION-MIB",
    "AddressType",
    "DateTime",
    "mrvInReachProductDivision")

(charPortIndex,) = mibBuilder.importSymbols(
    "RFC1316-MIB",
    "charPortIndex")

(rs232InSigState,
 rs232OutSigState,
 rs232PortIndex) = mibBuilder.importSymbols(
    "RFC1317-MIB",
    "rs232InSigState",
    "rs232OutSigState",
    "rs232PortIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CharacterDep_ObjectIdentity = ObjectIdentity
characterDep = _CharacterDep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 2)
)
_XCharacter_ObjectIdentity = ObjectIdentity
xCharacter = _XCharacter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13)
)
_XBasic_ObjectIdentity = ObjectIdentity
xBasic = _XBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 1)
)


class _BasicBroadcast_Type(Integer32):
    """Custom type basicBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicBroadcast_Type.__name__ = "Integer32"
_BasicBroadcast_Object = MibScalar
basicBroadcast = _BasicBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 1),
    _BasicBroadcast_Type()
)
basicBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicBroadcast.setStatus("mandatory")


class _BasicErrorReport_Type(Integer32):
    """Custom type basicErrorReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicErrorReport_Type.__name__ = "Integer32"
_BasicErrorReport_Object = MibScalar
basicErrorReport = _BasicErrorReport_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 2),
    _BasicErrorReport_Type()
)
basicErrorReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicErrorReport.setStatus("mandatory")


class _BasicLock_Type(Integer32):
    """Custom type basicLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicLock_Type.__name__ = "Integer32"
_BasicLock_Object = MibScalar
basicLock = _BasicLock_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 3),
    _BasicLock_Type()
)
basicLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicLock.setStatus("mandatory")


class _BasicInactivityTimer_Type(Integer32):
    """Custom type basicInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 480),
    )


_BasicInactivityTimer_Type.__name__ = "Integer32"
_BasicInactivityTimer_Object = MibScalar
basicInactivityTimer = _BasicInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 4),
    _BasicInactivityTimer_Type()
)
basicInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicInactivityTimer.setStatus("mandatory")


class _BasicPasswordRetryLimit_Type(Integer32):
    """Custom type basicPasswordRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_BasicPasswordRetryLimit_Type.__name__ = "Integer32"
_BasicPasswordRetryLimit_Object = MibScalar
basicPasswordRetryLimit = _BasicPasswordRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 5),
    _BasicPasswordRetryLimit_Type()
)
basicPasswordRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPasswordRetryLimit.setStatus("mandatory")


class _BasicPrivilegedPassword_Type(DisplayString):
    """Custom type basicPrivilegedPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPrivilegedPassword_Type.__name__ = "DisplayString"
_BasicPrivilegedPassword_Object = MibScalar
basicPrivilegedPassword = _BasicPrivilegedPassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 6),
    _BasicPrivilegedPassword_Type()
)
basicPrivilegedPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPrivilegedPassword.setStatus("mandatory")


class _BasicLoginPassword_Type(DisplayString):
    """Custom type basicLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicLoginPassword_Type.__name__ = "DisplayString"
_BasicLoginPassword_Object = MibScalar
basicLoginPassword = _BasicLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 7),
    _BasicLoginPassword_Type()
)
basicLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicLoginPassword.setStatus("mandatory")


class _BasicLoginPrompt_Type(DisplayString):
    """Custom type basicLoginPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_BasicLoginPrompt_Type.__name__ = "DisplayString"
_BasicLoginPrompt_Object = MibScalar
basicLoginPrompt = _BasicLoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 8),
    _BasicLoginPrompt_Type()
)
basicLoginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicLoginPrompt.setStatus("mandatory")


class _BasicWelcome_Type(DisplayString):
    """Custom type basicWelcome based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BasicWelcome_Type.__name__ = "DisplayString"
_BasicWelcome_Object = MibScalar
basicWelcome = _BasicWelcome_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 9),
    _BasicWelcome_Type()
)
basicWelcome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicWelcome.setStatus("mandatory")
_BasicActivePorts_Type = Gauge32
_BasicActivePorts_Object = MibScalar
basicActivePorts = _BasicActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 10),
    _BasicActivePorts_Type()
)
basicActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicActivePorts.setStatus("mandatory")
_BasicActivePortsHigh_Type = Gauge32
_BasicActivePortsHigh_Object = MibScalar
basicActivePortsHigh = _BasicActivePortsHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 11),
    _BasicActivePortsHigh_Type()
)
basicActivePortsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicActivePortsHigh.setStatus("mandatory")
_BasicActiveUsers_Type = Gauge32
_BasicActiveUsers_Object = MibScalar
basicActiveUsers = _BasicActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 12),
    _BasicActiveUsers_Type()
)
basicActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicActiveUsers.setStatus("mandatory")
_BasicActiveUsersHigh_Type = Gauge32
_BasicActiveUsersHigh_Object = MibScalar
basicActiveUsersHigh = _BasicActiveUsersHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 13),
    _BasicActiveUsersHigh_Type()
)
basicActiveUsersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicActiveUsersHigh.setStatus("mandatory")
_BasicSessions_Type = Gauge32
_BasicSessions_Object = MibScalar
basicSessions = _BasicSessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 14),
    _BasicSessions_Type()
)
basicSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicSessions.setStatus("mandatory")
_BasicSessionsHigh_Type = Gauge32
_BasicSessionsHigh_Object = MibScalar
basicSessionsHigh = _BasicSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 15),
    _BasicSessionsHigh_Type()
)
basicSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicSessionsHigh.setStatus("mandatory")


class _BasicSessionsLimit_Type(Integer32):
    """Custom type basicSessionsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_BasicSessionsLimit_Type.__name__ = "Integer32"
_BasicSessionsLimit_Object = MibScalar
basicSessionsLimit = _BasicSessionsLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 16),
    _BasicSessionsLimit_Type()
)
basicSessionsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSessionsLimit.setStatus("mandatory")
_BasicPortTable_Object = MibTable
basicPortTable = _BasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17)
)
if mibBuilder.loadTexts:
    basicPortTable.setStatus("mandatory")
_BasicPortEntry_Object = MibTableRow
basicPortEntry = _BasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1)
)
basicPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicPortIndex"),
)
if mibBuilder.loadTexts:
    basicPortEntry.setStatus("mandatory")
_BasicPortIndex_Type = Integer32
_BasicPortIndex_Object = MibTableColumn
basicPortIndex = _BasicPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 1),
    _BasicPortIndex_Type()
)
basicPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortIndex.setStatus("mandatory")


class _BasicPortDefaultDestAction_Type(Integer32):
    """Custom type basicPortDefaultDestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 1),
          ("preferred", 2))
    )


_BasicPortDefaultDestAction_Type.__name__ = "Integer32"
_BasicPortDefaultDestAction_Object = MibTableColumn
basicPortDefaultDestAction = _BasicPortDefaultDestAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 2),
    _BasicPortDefaultDestAction_Type()
)
basicPortDefaultDestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestAction.setStatus("mandatory")


class _BasicPortDefaultDestProtocol_Type(Integer32):
    """Custom type basicPortDefaultDestProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("lat", 1),
          ("telnet", 2))
    )


_BasicPortDefaultDestProtocol_Type.__name__ = "Integer32"
_BasicPortDefaultDestProtocol_Object = MibTableColumn
basicPortDefaultDestProtocol = _BasicPortDefaultDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 3),
    _BasicPortDefaultDestProtocol_Type()
)
basicPortDefaultDestProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestProtocol.setStatus("mandatory")


class _BasicPortDefaultDestName_Type(DisplayString):
    """Custom type basicPortDefaultDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_BasicPortDefaultDestName_Type.__name__ = "DisplayString"
_BasicPortDefaultDestName_Object = MibTableColumn
basicPortDefaultDestName = _BasicPortDefaultDestName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 4),
    _BasicPortDefaultDestName_Type()
)
basicPortDefaultDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestName.setStatus("mandatory")


class _BasicPortDefaultDestLATNodeName_Type(DisplayString):
    """Custom type basicPortDefaultDestLATNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPortDefaultDestLATNodeName_Type.__name__ = "DisplayString"
_BasicPortDefaultDestLATNodeName_Object = MibTableColumn
basicPortDefaultDestLATNodeName = _BasicPortDefaultDestLATNodeName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 5),
    _BasicPortDefaultDestLATNodeName_Type()
)
basicPortDefaultDestLATNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestLATNodeName.setStatus("mandatory")


class _BasicPortDefaultDestLATPortName_Type(DisplayString):
    """Custom type basicPortDefaultDestLATPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPortDefaultDestLATPortName_Type.__name__ = "DisplayString"
_BasicPortDefaultDestLATPortName_Object = MibTableColumn
basicPortDefaultDestLATPortName = _BasicPortDefaultDestLATPortName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 6),
    _BasicPortDefaultDestLATPortName_Type()
)
basicPortDefaultDestLATPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestLATPortName.setStatus("mandatory")


class _BasicPortAutoConnect_Type(Integer32):
    """Custom type basicPortAutoConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortAutoConnect_Type.__name__ = "Integer32"
_BasicPortAutoConnect_Object = MibTableColumn
basicPortAutoConnect = _BasicPortAutoConnect_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 7),
    _BasicPortAutoConnect_Type()
)
basicPortAutoConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAutoConnect.setStatus("mandatory")


class _BasicPortAutoLogin_Type(Integer32):
    """Custom type basicPortAutoLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortAutoLogin_Type.__name__ = "Integer32"
_BasicPortAutoLogin_Object = MibTableColumn
basicPortAutoLogin = _BasicPortAutoLogin_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 8),
    _BasicPortAutoLogin_Type()
)
basicPortAutoLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAutoLogin.setStatus("mandatory")


class _BasicPortBroadcast_Type(Integer32):
    """Custom type basicPortBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortBroadcast_Type.__name__ = "Integer32"
_BasicPortBroadcast_Object = MibTableColumn
basicPortBroadcast = _BasicPortBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 9),
    _BasicPortBroadcast_Type()
)
basicPortBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortBroadcast.setStatus("mandatory")


class _BasicPortConnectResume_Type(Integer32):
    """Custom type basicPortConnectResume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortConnectResume_Type.__name__ = "Integer32"
_BasicPortConnectResume_Object = MibTableColumn
basicPortConnectResume = _BasicPortConnectResume_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 10),
    _BasicPortConnectResume_Type()
)
basicPortConnectResume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortConnectResume.setStatus("mandatory")


class _BasicPortDialup_Type(Integer32):
    """Custom type basicPortDialup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortDialup_Type.__name__ = "Integer32"
_BasicPortDialup_Object = MibTableColumn
basicPortDialup = _BasicPortDialup_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 11),
    _BasicPortDialup_Type()
)
basicPortDialup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDialup.setStatus("mandatory")


class _BasicPortIdleTimeout_Type(Integer32):
    """Custom type basicPortIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 480),
    )


_BasicPortIdleTimeout_Type.__name__ = "Integer32"
_BasicPortIdleTimeout_Object = MibTableColumn
basicPortIdleTimeout = _BasicPortIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 12),
    _BasicPortIdleTimeout_Type()
)
basicPortIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortIdleTimeout.setStatus("mandatory")


class _BasicPortInactivityLogout_Type(Integer32):
    """Custom type basicPortInactivityLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortInactivityLogout_Type.__name__ = "Integer32"
_BasicPortInactivityLogout_Object = MibTableColumn
basicPortInactivityLogout = _BasicPortInactivityLogout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 13),
    _BasicPortInactivityLogout_Type()
)
basicPortInactivityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortInactivityLogout.setStatus("mandatory")


class _BasicPortLossNotification_Type(Integer32):
    """Custom type basicPortLossNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortLossNotification_Type.__name__ = "Integer32"
_BasicPortLossNotification_Object = MibTableColumn
basicPortLossNotification = _BasicPortLossNotification_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 14),
    _BasicPortLossNotification_Type()
)
basicPortLossNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortLossNotification.setStatus("mandatory")


class _BasicPortMessageCodes_Type(Integer32):
    """Custom type basicPortMessageCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortMessageCodes_Type.__name__ = "Integer32"
_BasicPortMessageCodes_Object = MibTableColumn
basicPortMessageCodes = _BasicPortMessageCodes_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 15),
    _BasicPortMessageCodes_Type()
)
basicPortMessageCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortMessageCodes.setStatus("mandatory")


class _BasicPortMultisessions_Type(Integer32):
    """Custom type basicPortMultisessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortMultisessions_Type.__name__ = "Integer32"
_BasicPortMultisessions_Object = MibTableColumn
basicPortMultisessions = _BasicPortMultisessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 16),
    _BasicPortMultisessions_Type()
)
basicPortMultisessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortMultisessions.setStatus("mandatory")


class _BasicPortDefaultUserName_Type(DisplayString):
    """Custom type basicPortDefaultUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPortDefaultUserName_Type.__name__ = "DisplayString"
_BasicPortDefaultUserName_Object = MibTableColumn
basicPortDefaultUserName = _BasicPortDefaultUserName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 17),
    _BasicPortDefaultUserName_Type()
)
basicPortDefaultUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultUserName.setStatus("mandatory")


class _BasicPortVerification_Type(Integer32):
    """Custom type basicPortVerification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortVerification_Type.__name__ = "Integer32"
_BasicPortVerification_Object = MibTableColumn
basicPortVerification = _BasicPortVerification_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 18),
    _BasicPortVerification_Type()
)
basicPortVerification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortVerification.setStatus("mandatory")


class _BasicPortDefaultProtocol_Type(Integer32):
    """Custom type basicPortDefaultProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              13)
        )
    )
    namedValues = NamedValues(
        *(("anylat", 3),
          ("anytelnet", 13),
          ("lat", 1),
          ("telnet", 2))
    )


_BasicPortDefaultProtocol_Type.__name__ = "Integer32"
_BasicPortDefaultProtocol_Object = MibTableColumn
basicPortDefaultProtocol = _BasicPortDefaultProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 19),
    _BasicPortDefaultProtocol_Type()
)
basicPortDefaultProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultProtocol.setStatus("mandatory")
_BasicPortLogins_Type = Counter32
_BasicPortLogins_Object = MibTableColumn
basicPortLogins = _BasicPortLogins_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 20),
    _BasicPortLogins_Type()
)
basicPortLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortLogins.setStatus("mandatory")
_BasicPortRemoteSessions_Type = Counter32
_BasicPortRemoteSessions_Object = MibTableColumn
basicPortRemoteSessions = _BasicPortRemoteSessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 21),
    _BasicPortRemoteSessions_Type()
)
basicPortRemoteSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortRemoteSessions.setStatus("mandatory")
_BasicPortIdleTimeouts_Type = Counter32
_BasicPortIdleTimeouts_Object = MibTableColumn
basicPortIdleTimeouts = _BasicPortIdleTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 22),
    _BasicPortIdleTimeouts_Type()
)
basicPortIdleTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortIdleTimeouts.setStatus("mandatory")


class _BasicPortStatus_Type(Integer32):
    """Custom type basicPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61)
        )
    )
    namedValues = NamedValues(
        *(("apd", 61),
          ("arapConnecting", 55),
          ("arapDialDone", 52),
          ("arapDialback", 48),
          ("arapEnabling", 54),
          ("arapExit", 53),
          ("arapInit", 41),
          ("arapLoad", 50),
          ("arapRead", 51),
          ("arapSearch", 49),
          ("arapUser", 47),
          ("autobaud", 27),
          ("available", 28),
          ("cancelQueue", 26),
          ("cclAnswer", 42),
          ("cclDone", 60),
          ("cclExecute", 59),
          ("cclHangup", 44),
          ("cclLoadError", 57),
          ("cclLoadWaiting", 58),
          ("cclLoading", 56),
          ("cclOriginate", 43),
          ("checkConnect", 6),
          ("checkModem", 29),
          ("connectPassword", 23),
          ("connectWait", 16),
          ("connected", 8),
          ("connecting", 5),
          ("cslip", 40),
          ("dialback1", 35),
          ("dialback2", 36),
          ("dialback3", 37),
          ("disconnect", 10),
          ("disconnecting", 9),
          ("executingCommand", 4),
          ("idle", 1),
          ("kerberos", 45),
          ("local", 2),
          ("locked", 12),
          ("login", 18),
          ("loginWait", 14),
          ("logout", 17),
          ("permanent", 13),
          ("ppp", 39),
          ("reset", 20),
          ("retryConnect", 15),
          ("scriptLoad", 33),
          ("scriptRun", 34),
          ("scriptSearch", 32),
          ("securID", 46),
          ("signalWait", 31),
          ("slip", 30),
          ("suspended", 11),
          ("testServiceOut", 22),
          ("testServiceWait", 21),
          ("waitInput", 3),
          ("waitLogout", 24),
          ("waitOutput", 7),
          ("waitQueue", 25),
          ("waitSession", 19),
          ("xremote", 38))
    )


_BasicPortStatus_Type.__name__ = "Integer32"
_BasicPortStatus_Object = MibTableColumn
basicPortStatus = _BasicPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 23),
    _BasicPortStatus_Type()
)
basicPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortStatus.setStatus("mandatory")


class _BasicPortLastInCharacter_Type(Integer32):
    """Custom type basicPortLastInCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicPortLastInCharacter_Type.__name__ = "Integer32"
_BasicPortLastInCharacter_Object = MibTableColumn
basicPortLastInCharacter = _BasicPortLastInCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 24),
    _BasicPortLastInCharacter_Type()
)
basicPortLastInCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortLastInCharacter.setStatus("mandatory")


class _BasicPortLastOutCharacter_Type(Integer32):
    """Custom type basicPortLastOutCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicPortLastOutCharacter_Type.__name__ = "Integer32"
_BasicPortLastOutCharacter_Object = MibTableColumn
basicPortLastOutCharacter = _BasicPortLastOutCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 25),
    _BasicPortLastOutCharacter_Type()
)
basicPortLastOutCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortLastOutCharacter.setStatus("mandatory")


class _BasicPortActiveUserName_Type(DisplayString):
    """Custom type basicPortActiveUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPortActiveUserName_Type.__name__ = "DisplayString"
_BasicPortActiveUserName_Object = MibTableColumn
basicPortActiveUserName = _BasicPortActiveUserName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 26),
    _BasicPortActiveUserName_Type()
)
basicPortActiveUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortActiveUserName.setStatus("mandatory")


class _BasicPortDefaultSessionMode_Type(Integer32):
    """Custom type basicPortDefaultSessionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("binary", 2),
          ("binaryWithFlow", 3),
          ("interactive", 1),
          ("transparent", 4))
    )


_BasicPortDefaultSessionMode_Type.__name__ = "Integer32"
_BasicPortDefaultSessionMode_Object = MibTableColumn
basicPortDefaultSessionMode = _BasicPortDefaultSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 27),
    _BasicPortDefaultSessionMode_Type()
)
basicPortDefaultSessionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultSessionMode.setStatus("mandatory")


class _BasicPortZero_Type(Integer32):
    """Custom type basicPortZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_BasicPortZero_Type.__name__ = "Integer32"
_BasicPortZero_Object = MibTableColumn
basicPortZero = _BasicPortZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 28),
    _BasicPortZero_Type()
)
basicPortZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortZero.setStatus("mandatory")
_BasicPortZeroTime_Type = TimeTicks
_BasicPortZeroTime_Object = MibTableColumn
basicPortZeroTime = _BasicPortZeroTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 29),
    _BasicPortZeroTime_Type()
)
basicPortZeroTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortZeroTime.setStatus("mandatory")


class _BasicPortUnixCommands_Type(Integer32):
    """Custom type basicPortUnixCommands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("only", 4),
          ("primary", 3))
    )


_BasicPortUnixCommands_Type.__name__ = "Integer32"
_BasicPortUnixCommands_Object = MibTableColumn
basicPortUnixCommands = _BasicPortUnixCommands_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 30),
    _BasicPortUnixCommands_Type()
)
basicPortUnixCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortUnixCommands.setStatus("mandatory")


class _BasicPortSessionMode_Type(Integer32):
    """Custom type basicPortSessionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("binary", 2),
          ("binaryWithFlow", 3),
          ("interactive", 1),
          ("noActiveSessions", 5),
          ("transparent", 4))
    )


_BasicPortSessionMode_Type.__name__ = "Integer32"
_BasicPortSessionMode_Object = MibTableColumn
basicPortSessionMode = _BasicPortSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 31),
    _BasicPortSessionMode_Type()
)
basicPortSessionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortSessionMode.setStatus("mandatory")


class _BasicPortRemoteDisconnectNotify_Type(Integer32):
    """Custom type basicPortRemoteDisconnectNotify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortRemoteDisconnectNotify_Type.__name__ = "Integer32"
_BasicPortRemoteDisconnectNotify_Object = MibTableColumn
basicPortRemoteDisconnectNotify = _BasicPortRemoteDisconnectNotify_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 32),
    _BasicPortRemoteDisconnectNotify_Type()
)
basicPortRemoteDisconnectNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortRemoteDisconnectNotify.setStatus("mandatory")


class _BasicPortDefaultDestControlled_Type(Integer32):
    """Custom type basicPortDefaultDestControlled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortDefaultDestControlled_Type.__name__ = "Integer32"
_BasicPortDefaultDestControlled_Object = MibTableColumn
basicPortDefaultDestControlled = _BasicPortDefaultDestControlled_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 33),
    _BasicPortDefaultDestControlled_Type()
)
basicPortDefaultDestControlled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestControlled.setStatus("mandatory")


class _BasicPortControlledPortLogin_Type(OctetString):
    """Custom type basicPortControlledPortLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicPortControlledPortLogin_Type.__name__ = "OctetString"
_BasicPortControlledPortLogin_Object = MibTableColumn
basicPortControlledPortLogin = _BasicPortControlledPortLogin_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 34),
    _BasicPortControlledPortLogin_Type()
)
basicPortControlledPortLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortControlledPortLogin.setStatus("mandatory")


class _BasicPortControlledPortLogout_Type(OctetString):
    """Custom type basicPortControlledPortLogout based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicPortControlledPortLogout_Type.__name__ = "OctetString"
_BasicPortControlledPortLogout_Object = MibTableColumn
basicPortControlledPortLogout = _BasicPortControlledPortLogout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 35),
    _BasicPortControlledPortLogout_Type()
)
basicPortControlledPortLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortControlledPortLogout.setStatus("mandatory")


class _BasicPortControlledSessionInitialize_Type(OctetString):
    """Custom type basicPortControlledSessionInitialize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicPortControlledSessionInitialize_Type.__name__ = "OctetString"
_BasicPortControlledSessionInitialize_Object = MibTableColumn
basicPortControlledSessionInitialize = _BasicPortControlledSessionInitialize_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 36),
    _BasicPortControlledSessionInitialize_Type()
)
basicPortControlledSessionInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortControlledSessionInitialize.setStatus("mandatory")


class _BasicPortControlledSessionTerminate_Type(OctetString):
    """Custom type basicPortControlledSessionTerminate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicPortControlledSessionTerminate_Type.__name__ = "OctetString"
_BasicPortControlledSessionTerminate_Object = MibTableColumn
basicPortControlledSessionTerminate = _BasicPortControlledSessionTerminate_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 37),
    _BasicPortControlledSessionTerminate_Type()
)
basicPortControlledSessionTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortControlledSessionTerminate.setStatus("mandatory")


class _BasicPortRloginTransparentMode_Type(Integer32):
    """Custom type basicPortRloginTransparentMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortRloginTransparentMode_Type.__name__ = "Integer32"
_BasicPortRloginTransparentMode_Object = MibTableColumn
basicPortRloginTransparentMode = _BasicPortRloginTransparentMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 38),
    _BasicPortRloginTransparentMode_Type()
)
basicPortRloginTransparentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortRloginTransparentMode.setStatus("mandatory")


class _BasicPortLoginDuration_Type(Integer32):
    """Custom type basicPortLoginDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64800),
    )


_BasicPortLoginDuration_Type.__name__ = "Integer32"
_BasicPortLoginDuration_Object = MibTableColumn
basicPortLoginDuration = _BasicPortLoginDuration_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 39),
    _BasicPortLoginDuration_Type()
)
basicPortLoginDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortLoginDuration.setStatus("mandatory")


class _BasicPortOutboundSecurity_Type(Integer32):
    """Custom type basicPortOutboundSecurity based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortOutboundSecurity_Type.__name__ = "Integer32"
_BasicPortOutboundSecurity_Object = MibTableColumn
basicPortOutboundSecurity = _BasicPortOutboundSecurity_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 40),
    _BasicPortOutboundSecurity_Type()
)
basicPortOutboundSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortOutboundSecurity.setStatus("mandatory")


class _BasicPortXonTimer_Type(Integer32):
    """Custom type basicPortXonTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2550),
    )


_BasicPortXonTimer_Type.__name__ = "Integer32"
_BasicPortXonTimer_Object = MibTableColumn
basicPortXonTimer = _BasicPortXonTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 41),
    _BasicPortXonTimer_Type()
)
basicPortXonTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortXonTimer.setStatus("mandatory")


class _BasicPortDefaultDedicatedSessionType_Type(Integer32):
    """Custom type basicPortDefaultDedicatedSessionType based on Integer32"""
    defaultHexValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 168),
    )


_BasicPortDefaultDedicatedSessionType_Type.__name__ = "Integer32"
_BasicPortDefaultDedicatedSessionType_Object = MibTableColumn
basicPortDefaultDedicatedSessionType = _BasicPortDefaultDedicatedSessionType_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 42),
    _BasicPortDefaultDedicatedSessionType_Type()
)
basicPortDefaultDedicatedSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDedicatedSessionType.setStatus("mandatory")


class _BasicPortIdleTimeReceive_Type(Integer32):
    """Custom type basicPortIdleTimeReceive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortIdleTimeReceive_Type.__name__ = "Integer32"
_BasicPortIdleTimeReceive_Object = MibTableColumn
basicPortIdleTimeReceive = _BasicPortIdleTimeReceive_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 43),
    _BasicPortIdleTimeReceive_Type()
)
basicPortIdleTimeReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortIdleTimeReceive.setStatus("mandatory")


class _BasicPortIdleTimeTransmit_Type(Integer32):
    """Custom type basicPortIdleTimeTransmit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortIdleTimeTransmit_Type.__name__ = "Integer32"
_BasicPortIdleTimeTransmit_Object = MibTableColumn
basicPortIdleTimeTransmit = _BasicPortIdleTimeTransmit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 44),
    _BasicPortIdleTimeTransmit_Type()
)
basicPortIdleTimeTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortIdleTimeTransmit.setStatus("mandatory")


class _BasicPortZeroDisconnectSession_Type(Integer32):
    """Custom type basicPortZeroDisconnectSession based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortZeroDisconnectSession_Type.__name__ = "Integer32"
_BasicPortZeroDisconnectSession_Object = MibTableColumn
basicPortZeroDisconnectSession = _BasicPortZeroDisconnectSession_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 45),
    _BasicPortZeroDisconnectSession_Type()
)
basicPortZeroDisconnectSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortZeroDisconnectSession.setStatus("mandatory")


class _BasicPortConsolePort_Type(Integer32):
    """Custom type basicPortConsolePort based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortConsolePort_Type.__name__ = "Integer32"
_BasicPortConsolePort_Object = MibTableColumn
basicPortConsolePort = _BasicPortConsolePort_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 46),
    _BasicPortConsolePort_Type()
)
basicPortConsolePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortConsolePort.setStatus("mandatory")


class _BasicPortLoginPassword_Type(DisplayString):
    """Custom type basicPortLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPortLoginPassword_Type.__name__ = "DisplayString"
_BasicPortLoginPassword_Object = MibTableColumn
basicPortLoginPassword = _BasicPortLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 47),
    _BasicPortLoginPassword_Type()
)
basicPortLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortLoginPassword.setStatus("mandatory")


class _BasicPortSensor_Type(Integer32):
    """Custom type basicPortSensor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortSensor_Type.__name__ = "Integer32"
_BasicPortSensor_Object = MibTableColumn
basicPortSensor = _BasicPortSensor_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 48),
    _BasicPortSensor_Type()
)
basicPortSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortSensor.setStatus("mandatory")


class _BasicPortAlarmControl_Type(Integer32):
    """Custom type basicPortAlarmControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortAlarmControl_Type.__name__ = "Integer32"
_BasicPortAlarmControl_Object = MibTableColumn
basicPortAlarmControl = _BasicPortAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 49),
    _BasicPortAlarmControl_Type()
)
basicPortAlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmControl.setStatus("mandatory")


class _BasicPortCommandLogging_Type(Integer32):
    """Custom type basicPortCommandLogging based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortCommandLogging_Type.__name__ = "Integer32"
_BasicPortCommandLogging_Object = MibTableColumn
basicPortCommandLogging = _BasicPortCommandLogging_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 50),
    _BasicPortCommandLogging_Type()
)
basicPortCommandLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortCommandLogging.setStatus("mandatory")


class _BasicPortBreakSequence_Type(OctetString):
    """Custom type basicPortBreakSequence based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPortBreakSequence_Type.__name__ = "OctetString"
_BasicPortBreakSequence_Object = MibTableColumn
basicPortBreakSequence = _BasicPortBreakSequence_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 51),
    _BasicPortBreakSequence_Type()
)
basicPortBreakSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortBreakSequence.setStatus("mandatory")


class _BasicPortTl1Mode_Type(Integer32):
    """Custom type basicPortTl1Mode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("hml", 2),
          ("mml", 3),
          ("mmlNoEcho", 4))
    )


_BasicPortTl1Mode_Type.__name__ = "Integer32"
_BasicPortTl1Mode_Object = MibTableColumn
basicPortTl1Mode = _BasicPortTl1Mode_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 53),
    _BasicPortTl1Mode_Type()
)
basicPortTl1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortTl1Mode.setStatus("mandatory")


class _BasicPortTl1Console_Type(Integer32):
    """Custom type basicPortTl1Console based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortTl1Console_Type.__name__ = "Integer32"
_BasicPortTl1Console_Object = MibTableColumn
basicPortTl1Console = _BasicPortTl1Console_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 54),
    _BasicPortTl1Console_Type()
)
basicPortTl1Console.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortTl1Console.setStatus("mandatory")


class _BasicPortFallThrough_Type(Integer32):
    """Custom type basicPortFallThrough based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortFallThrough_Type.__name__ = "Integer32"
_BasicPortFallThrough_Object = MibTableColumn
basicPortFallThrough = _BasicPortFallThrough_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 55),
    _BasicPortFallThrough_Type()
)
basicPortFallThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortFallThrough.setStatus("mandatory")


class _BasicPortCommandLoggingSuppressControlCharacters_Type(Integer32):
    """Custom type basicPortCommandLoggingSuppressControlCharacters based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortCommandLoggingSuppressControlCharacters_Type.__name__ = "Integer32"
_BasicPortCommandLoggingSuppressControlCharacters_Object = MibTableColumn
basicPortCommandLoggingSuppressControlCharacters = _BasicPortCommandLoggingSuppressControlCharacters_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 56),
    _BasicPortCommandLoggingSuppressControlCharacters_Type()
)
basicPortCommandLoggingSuppressControlCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortCommandLoggingSuppressControlCharacters.setStatus("mandatory")


class _BasicPortDataLogging_Type(Integer32):
    """Custom type basicPortDataLogging based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortDataLogging_Type.__name__ = "Integer32"
_BasicPortDataLogging_Object = MibTableColumn
basicPortDataLogging = _BasicPortDataLogging_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 57),
    _BasicPortDataLogging_Type()
)
basicPortDataLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDataLogging.setStatus("mandatory")


class _BasicPortDataLoggingSuppressControlCharacters_Type(Integer32):
    """Custom type basicPortDataLoggingSuppressControlCharacters based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortDataLoggingSuppressControlCharacters_Type.__name__ = "Integer32"
_BasicPortDataLoggingSuppressControlCharacters_Object = MibTableColumn
basicPortDataLoggingSuppressControlCharacters = _BasicPortDataLoggingSuppressControlCharacters_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 58),
    _BasicPortDataLoggingSuppressControlCharacters_Type()
)
basicPortDataLoggingSuppressControlCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDataLoggingSuppressControlCharacters.setStatus("mandatory")


class _BasicPortOnboardSecurity_Type(Integer32):
    """Custom type basicPortOnboardSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortOnboardSecurity_Type.__name__ = "Integer32"
_BasicPortOnboardSecurity_Object = MibTableColumn
basicPortOnboardSecurity = _BasicPortOnboardSecurity_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 59),
    _BasicPortOnboardSecurity_Type()
)
basicPortOnboardSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortOnboardSecurity.setStatus("mandatory")


class _BasicPortFallBack_Type(Integer32):
    """Custom type basicPortFallBack based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortFallBack_Type.__name__ = "Integer32"
_BasicPortFallBack_Object = MibTableColumn
basicPortFallBack = _BasicPortFallBack_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 60),
    _BasicPortFallBack_Type()
)
basicPortFallBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortFallBack.setStatus("mandatory")


class _BasicPortAlarmMaster_Type(Integer32):
    """Custom type basicPortAlarmMaster based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortAlarmMaster_Type.__name__ = "Integer32"
_BasicPortAlarmMaster_Object = MibTableColumn
basicPortAlarmMaster = _BasicPortAlarmMaster_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 61),
    _BasicPortAlarmMaster_Type()
)
basicPortAlarmMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmMaster.setStatus("mandatory")


class _BasicPortAlarmMasterAccounting_Type(Integer32):
    """Custom type basicPortAlarmMasterAccounting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortAlarmMasterAccounting_Type.__name__ = "Integer32"
_BasicPortAlarmMasterAccounting_Object = MibTableColumn
basicPortAlarmMasterAccounting = _BasicPortAlarmMasterAccounting_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 62),
    _BasicPortAlarmMasterAccounting_Type()
)
basicPortAlarmMasterAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmMasterAccounting.setStatus("mandatory")


class _BasicPortAlarmMasterAudibleAlarm_Type(Integer32):
    """Custom type basicPortAlarmMasterAudibleAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortAlarmMasterAudibleAlarm_Type.__name__ = "Integer32"
_BasicPortAlarmMasterAudibleAlarm_Object = MibTableColumn
basicPortAlarmMasterAudibleAlarm = _BasicPortAlarmMasterAudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 63),
    _BasicPortAlarmMasterAudibleAlarm_Type()
)
basicPortAlarmMasterAudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmMasterAudibleAlarm.setStatus("mandatory")


class _BasicPortAlarmMasterFixTime_Type(Integer32):
    """Custom type basicPortAlarmMasterFixTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_BasicPortAlarmMasterFixTime_Type.__name__ = "Integer32"
_BasicPortAlarmMasterFixTime_Object = MibTableColumn
basicPortAlarmMasterFixTime = _BasicPortAlarmMasterFixTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 64),
    _BasicPortAlarmMasterFixTime_Type()
)
basicPortAlarmMasterFixTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmMasterFixTime.setStatus("mandatory")


class _BasicPortAlarmMasterLcdDisplayString_Type(DisplayString):
    """Custom type basicPortAlarmMasterLcdDisplayString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_BasicPortAlarmMasterLcdDisplayString_Type.__name__ = "DisplayString"
_BasicPortAlarmMasterLcdDisplayString_Object = MibTableColumn
basicPortAlarmMasterLcdDisplayString = _BasicPortAlarmMasterLcdDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 65),
    _BasicPortAlarmMasterLcdDisplayString_Type()
)
basicPortAlarmMasterLcdDisplayString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmMasterLcdDisplayString.setStatus("mandatory")


class _BasicPortAlarmMasterReboot_Type(Integer32):
    """Custom type basicPortAlarmMasterReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_BasicPortAlarmMasterReboot_Type.__name__ = "Integer32"
_BasicPortAlarmMasterReboot_Object = MibTableColumn
basicPortAlarmMasterReboot = _BasicPortAlarmMasterReboot_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 66),
    _BasicPortAlarmMasterReboot_Type()
)
basicPortAlarmMasterReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmMasterReboot.setStatus("mandatory")
_BasicPortAlarmMasterUpdateFirmwareHost_Type = IpAddress
_BasicPortAlarmMasterUpdateFirmwareHost_Object = MibTableColumn
basicPortAlarmMasterUpdateFirmwareHost = _BasicPortAlarmMasterUpdateFirmwareHost_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 67),
    _BasicPortAlarmMasterUpdateFirmwareHost_Type()
)
basicPortAlarmMasterUpdateFirmwareHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmMasterUpdateFirmwareHost.setStatus("mandatory")


class _BasicPortAlarmMasterUpdateFirmwareFileName_Type(DisplayString):
    """Custom type basicPortAlarmMasterUpdateFirmwareFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BasicPortAlarmMasterUpdateFirmwareFileName_Type.__name__ = "DisplayString"
_BasicPortAlarmMasterUpdateFirmwareFileName_Object = MibTableColumn
basicPortAlarmMasterUpdateFirmwareFileName = _BasicPortAlarmMasterUpdateFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 68),
    _BasicPortAlarmMasterUpdateFirmwareFileName_Type()
)
basicPortAlarmMasterUpdateFirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmMasterUpdateFirmwareFileName.setStatus("mandatory")


class _BasicPortAlarmMasterUpdateFirmware_Type(Integer32):
    """Custom type basicPortAlarmMasterUpdateFirmware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_BasicPortAlarmMasterUpdateFirmware_Type.__name__ = "Integer32"
_BasicPortAlarmMasterUpdateFirmware_Object = MibTableColumn
basicPortAlarmMasterUpdateFirmware = _BasicPortAlarmMasterUpdateFirmware_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 69),
    _BasicPortAlarmMasterUpdateFirmware_Type()
)
basicPortAlarmMasterUpdateFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmMasterUpdateFirmware.setStatus("mandatory")


class _BasicPortAlarmMasterStatus_Type(Integer32):
    """Custom type basicPortAlarmMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicPortAlarmMasterStatus_Type.__name__ = "Integer32"
_BasicPortAlarmMasterStatus_Object = MibTableColumn
basicPortAlarmMasterStatus = _BasicPortAlarmMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 70),
    _BasicPortAlarmMasterStatus_Type()
)
basicPortAlarmMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortAlarmMasterStatus.setStatus("mandatory")


class _BasicPortAlarmMasterFaultSeverity_Type(Integer32):
    """Custom type basicPortAlarmMasterFaultSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicPortAlarmMasterFaultSeverity_Type.__name__ = "Integer32"
_BasicPortAlarmMasterFaultSeverity_Object = MibTableColumn
basicPortAlarmMasterFaultSeverity = _BasicPortAlarmMasterFaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 71),
    _BasicPortAlarmMasterFaultSeverity_Type()
)
basicPortAlarmMasterFaultSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAlarmMasterFaultSeverity.setStatus("mandatory")


class _BasicPortPowerMaster_Type(Integer32):
    """Custom type basicPortPowerMaster based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortPowerMaster_Type.__name__ = "Integer32"
_BasicPortPowerMaster_Object = MibTableColumn
basicPortPowerMaster = _BasicPortPowerMaster_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 72),
    _BasicPortPowerMaster_Type()
)
basicPortPowerMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPowerMaster.setStatus("mandatory")


class _BasicPortPowerMasterTimeDelay_Type(Integer32):
    """Custom type basicPortPowerMasterTimeDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900)
        )
    )
    namedValues = NamedValues(
        *(("eightHundred", 800),
          ("fiveHundred", 500),
          ("fourHundred", 400),
          ("nineHundred", 900),
          ("none", 1),
          ("oneHundred", 100),
          ("sevenHundred", 700),
          ("sixHundred", 600),
          ("threeHundred", 300),
          ("twoHundred", 200))
    )


_BasicPortPowerMasterTimeDelay_Type.__name__ = "Integer32"
_BasicPortPowerMasterTimeDelay_Object = MibTableColumn
basicPortPowerMasterTimeDelay = _BasicPortPowerMasterTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 73),
    _BasicPortPowerMasterTimeDelay_Type()
)
basicPortPowerMasterTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPowerMasterTimeDelay.setStatus("mandatory")


class _BasicPortPowerMasterSwitch_Type(Integer32):
    """Custom type basicPortPowerMasterSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("ready", 1))
    )


_BasicPortPowerMasterSwitch_Type.__name__ = "Integer32"
_BasicPortPowerMasterSwitch_Object = MibTableColumn
basicPortPowerMasterSwitch = _BasicPortPowerMasterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 74),
    _BasicPortPowerMasterSwitch_Type()
)
basicPortPowerMasterSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPowerMasterSwitch.setStatus("mandatory")


class _BasicPortPowerMasterModel_Type(DisplayString):
    """Custom type basicPortPowerMasterModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BasicPortPowerMasterModel_Type.__name__ = "DisplayString"
_BasicPortPowerMasterModel_Object = MibTableColumn
basicPortPowerMasterModel = _BasicPortPowerMasterModel_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 75),
    _BasicPortPowerMasterModel_Type()
)
basicPortPowerMasterModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortPowerMasterModel.setStatus("mandatory")


class _BasicPortPowerMasterSerialNumber_Type(DisplayString):
    """Custom type basicPortPowerMasterSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_BasicPortPowerMasterSerialNumber_Type.__name__ = "DisplayString"
_BasicPortPowerMasterSerialNumber_Object = MibTableColumn
basicPortPowerMasterSerialNumber = _BasicPortPowerMasterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 76),
    _BasicPortPowerMasterSerialNumber_Type()
)
basicPortPowerMasterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortPowerMasterSerialNumber.setStatus("mandatory")


class _BasicPortPowerMasterFirmware_Type(DisplayString):
    """Custom type basicPortPowerMasterFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_BasicPortPowerMasterFirmware_Type.__name__ = "DisplayString"
_BasicPortPowerMasterFirmware_Object = MibTableColumn
basicPortPowerMasterFirmware = _BasicPortPowerMasterFirmware_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 77),
    _BasicPortPowerMasterFirmware_Type()
)
basicPortPowerMasterFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortPowerMasterFirmware.setStatus("mandatory")


class _BasicPortLockout_Type(Integer32):
    """Custom type basicPortLockout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortLockout_Type.__name__ = "Integer32"
_BasicPortLockout_Object = MibTableColumn
basicPortLockout = _BasicPortLockout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 78),
    _BasicPortLockout_Type()
)
basicPortLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortLockout.setStatus("mandatory")


class _BasicPortAsciiToTrapTranslation_Type(Integer32):
    """Custom type basicPortAsciiToTrapTranslation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortAsciiToTrapTranslation_Type.__name__ = "Integer32"
_BasicPortAsciiToTrapTranslation_Object = MibTableColumn
basicPortAsciiToTrapTranslation = _BasicPortAsciiToTrapTranslation_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 79),
    _BasicPortAsciiToTrapTranslation_Type()
)
basicPortAsciiToTrapTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAsciiToTrapTranslation.setStatus("mandatory")


class _BasicPortAsciiToTrapTranslationTrapSeverity_Type(Integer32):
    """Custom type basicPortAsciiToTrapTranslationTrapSeverity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicPortAsciiToTrapTranslationTrapSeverity_Type.__name__ = "Integer32"
_BasicPortAsciiToTrapTranslationTrapSeverity_Object = MibTableColumn
basicPortAsciiToTrapTranslationTrapSeverity = _BasicPortAsciiToTrapTranslationTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 80),
    _BasicPortAsciiToTrapTranslationTrapSeverity_Type()
)
basicPortAsciiToTrapTranslationTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAsciiToTrapTranslationTrapSeverity.setStatus("mandatory")
_BasicPortAsciiToTrapTranslationMessages_Type = Counter32
_BasicPortAsciiToTrapTranslationMessages_Object = MibTableColumn
basicPortAsciiToTrapTranslationMessages = _BasicPortAsciiToTrapTranslationMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 81),
    _BasicPortAsciiToTrapTranslationMessages_Type()
)
basicPortAsciiToTrapTranslationMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortAsciiToTrapTranslationMessages.setStatus("mandatory")


class _BasicPortAsciiToTrapTranslationLastMessage_Type(DisplayString):
    """Custom type basicPortAsciiToTrapTranslationLastMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasicPortAsciiToTrapTranslationLastMessage_Type.__name__ = "DisplayString"
_BasicPortAsciiToTrapTranslationLastMessage_Object = MibTableColumn
basicPortAsciiToTrapTranslationLastMessage = _BasicPortAsciiToTrapTranslationLastMessage_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 82),
    _BasicPortAsciiToTrapTranslationLastMessage_Type()
)
basicPortAsciiToTrapTranslationLastMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortAsciiToTrapTranslationLastMessage.setStatus("mandatory")


class _BasicPortPowerMasterAlarmSeverity_Type(Integer32):
    """Custom type basicPortPowerMasterAlarmSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicPortPowerMasterAlarmSeverity_Type.__name__ = "Integer32"
_BasicPortPowerMasterAlarmSeverity_Object = MibTableColumn
basicPortPowerMasterAlarmSeverity = _BasicPortPowerMasterAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 83),
    _BasicPortPowerMasterAlarmSeverity_Type()
)
basicPortPowerMasterAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPowerMasterAlarmSeverity.setStatus("mandatory")


class _BasicPortPowerMasterDeviceStatus_Type(Integer32):
    """Custom type basicPortPowerMasterDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicPortPowerMasterDeviceStatus_Type.__name__ = "Integer32"
_BasicPortPowerMasterDeviceStatus_Object = MibTableColumn
basicPortPowerMasterDeviceStatus = _BasicPortPowerMasterDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 84),
    _BasicPortPowerMasterDeviceStatus_Type()
)
basicPortPowerMasterDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortPowerMasterDeviceStatus.setStatus("mandatory")


class _BasicPortBuffering_Type(Integer32):
    """Custom type basicPortBuffering based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortBuffering_Type.__name__ = "Integer32"
_BasicPortBuffering_Object = MibTableColumn
basicPortBuffering = _BasicPortBuffering_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 85),
    _BasicPortBuffering_Type()
)
basicPortBuffering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortBuffering.setStatus("mandatory")


class _BasicPortLogFacilityLevel_Type(Integer32):
    """Custom type basicPortLogFacilityLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("local0", 2),
          ("local1", 3),
          ("local2", 4),
          ("local3", 5),
          ("local4", 6),
          ("local5", 7),
          ("local6", 8),
          ("local7", 9),
          ("none", 1),
          ("user", 10))
    )


_BasicPortLogFacilityLevel_Type.__name__ = "Integer32"
_BasicPortLogFacilityLevel_Object = MibTableColumn
basicPortLogFacilityLevel = _BasicPortLogFacilityLevel_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 86),
    _BasicPortLogFacilityLevel_Type()
)
basicPortLogFacilityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortLogFacilityLevel.setStatus("mandatory")


class _BasicPortPppDialBackup_Type(Integer32):
    """Custom type basicPortPppDialBackup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortPppDialBackup_Type.__name__ = "Integer32"
_BasicPortPppDialBackup_Object = MibTableColumn
basicPortPppDialBackup = _BasicPortPppDialBackup_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 87),
    _BasicPortPppDialBackup_Type()
)
basicPortPppDialBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPppDialBackup.setStatus("mandatory")


class _BasicPortPppDialBackupNumber_Type(DisplayString):
    """Custom type basicPortPppDialBackupNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicPortPppDialBackupNumber_Type.__name__ = "DisplayString"
_BasicPortPppDialBackupNumber_Object = MibTableColumn
basicPortPppDialBackupNumber = _BasicPortPppDialBackupNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 88),
    _BasicPortPppDialBackupNumber_Type()
)
basicPortPppDialBackupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPppDialBackupNumber.setStatus("mandatory")


class _BasicPortPppDialBackupRedialTimer_Type(Integer32):
    """Custom type basicPortPppDialBackupRedialTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_BasicPortPppDialBackupRedialTimer_Type.__name__ = "Integer32"
_BasicPortPppDialBackupRedialTimer_Object = MibTableColumn
basicPortPppDialBackupRedialTimer = _BasicPortPppDialBackupRedialTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 89),
    _BasicPortPppDialBackupRedialTimer_Type()
)
basicPortPppDialBackupRedialTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPppDialBackupRedialTimer.setStatus("mandatory")


class _BasicPortPppDialBackupRedialRetries_Type(Integer32):
    """Custom type basicPortPppDialBackupRedialRetries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BasicPortPppDialBackupRedialRetries_Type.__name__ = "Integer32"
_BasicPortPppDialBackupRedialRetries_Object = MibTableColumn
basicPortPppDialBackupRedialRetries = _BasicPortPppDialBackupRedialRetries_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 90),
    _BasicPortPppDialBackupRedialRetries_Type()
)
basicPortPppDialBackupRedialRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPppDialBackupRedialRetries.setStatus("mandatory")


class _BasicPortPppDialBackupDisconnectTimer_Type(Integer32):
    """Custom type basicPortPppDialBackupDisconnectTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BasicPortPppDialBackupDisconnectTimer_Type.__name__ = "Integer32"
_BasicPortPppDialBackupDisconnectTimer_Object = MibTableColumn
basicPortPppDialBackupDisconnectTimer = _BasicPortPppDialBackupDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 91),
    _BasicPortPppDialBackupDisconnectTimer_Type()
)
basicPortPppDialBackupDisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPppDialBackupDisconnectTimer.setStatus("mandatory")
_BasicPortPppDialBackupLocalAddress_Type = IpAddress
_BasicPortPppDialBackupLocalAddress_Object = MibTableColumn
basicPortPppDialBackupLocalAddress = _BasicPortPppDialBackupLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 92),
    _BasicPortPppDialBackupLocalAddress_Type()
)
basicPortPppDialBackupLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPppDialBackupLocalAddress.setStatus("mandatory")
_BasicPortPppDialBackupDestinationAddress_Type = IpAddress
_BasicPortPppDialBackupDestinationAddress_Object = MibTableColumn
basicPortPppDialBackupDestinationAddress = _BasicPortPppDialBackupDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 93),
    _BasicPortPppDialBackupDestinationAddress_Type()
)
basicPortPppDialBackupDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPppDialBackupDestinationAddress.setStatus("mandatory")


class _BasicPortPppDialBackupAddresses_Type(Integer32):
    """Custom type basicPortPppDialBackupAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_BasicPortPppDialBackupAddresses_Type.__name__ = "Integer32"
_BasicPortPppDialBackupAddresses_Object = MibTableColumn
basicPortPppDialBackupAddresses = _BasicPortPppDialBackupAddresses_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 94),
    _BasicPortPppDialBackupAddresses_Type()
)
basicPortPppDialBackupAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortPppDialBackupAddresses.setStatus("mandatory")
_BasicSerialPortTable_Object = MibTable
basicSerialPortTable = _BasicSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18)
)
if mibBuilder.loadTexts:
    basicSerialPortTable.setStatus("mandatory")
_BasicSerialPortEntry_Object = MibTableRow
basicSerialPortEntry = _BasicSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1)
)
basicSerialPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicSerialPortIndex"),
)
if mibBuilder.loadTexts:
    basicSerialPortEntry.setStatus("mandatory")
_BasicSerialPortIndex_Type = Integer32
_BasicSerialPortIndex_Object = MibTableColumn
basicSerialPortIndex = _BasicSerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 1),
    _BasicSerialPortIndex_Type()
)
basicSerialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicSerialPortIndex.setStatus("mandatory")


class _BasicSerialPortBreak_Type(Integer32):
    """Custom type basicSerialPortBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("localSwitch", 2),
          ("sendRemote", 3))
    )


_BasicSerialPortBreak_Type.__name__ = "Integer32"
_BasicSerialPortBreak_Object = MibTableColumn
basicSerialPortBreak = _BasicSerialPortBreak_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 2),
    _BasicSerialPortBreak_Type()
)
basicSerialPortBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortBreak.setStatus("mandatory")


class _BasicSerialPortInterrupts_Type(Integer32):
    """Custom type basicSerialPortInterrupts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortInterrupts_Type.__name__ = "Integer32"
_BasicSerialPortInterrupts_Object = MibTableColumn
basicSerialPortInterrupts = _BasicSerialPortInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 3),
    _BasicSerialPortInterrupts_Type()
)
basicSerialPortInterrupts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortInterrupts.setStatus("mandatory")


class _BasicSerialPortNoLoss_Type(Integer32):
    """Custom type basicSerialPortNoLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortNoLoss_Type.__name__ = "Integer32"
_BasicSerialPortNoLoss_Object = MibTableColumn
basicSerialPortNoLoss = _BasicSerialPortNoLoss_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 4),
    _BasicSerialPortNoLoss_Type()
)
basicSerialPortNoLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortNoLoss.setStatus("mandatory")


class _BasicSerialPortPause_Type(Integer32):
    """Custom type basicSerialPortPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortPause_Type.__name__ = "Integer32"
_BasicSerialPortPause_Object = MibTableColumn
basicSerialPortPause = _BasicSerialPortPause_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 5),
    _BasicSerialPortPause_Type()
)
basicSerialPortPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortPause.setStatus("mandatory")


class _BasicSerialPortPrompt_Type(DisplayString):
    """Custom type basicSerialPortPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BasicSerialPortPrompt_Type.__name__ = "DisplayString"
_BasicSerialPortPrompt_Object = MibTableColumn
basicSerialPortPrompt = _BasicSerialPortPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 6),
    _BasicSerialPortPrompt_Type()
)
basicSerialPortPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortPrompt.setStatus("mandatory")


class _BasicSerialPortTerminalType_Type(Integer32):
    """Custom type basicSerialPortTerminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("hardcopy", 2),
          ("softcopy", 3))
    )


_BasicSerialPortTerminalType_Type.__name__ = "Integer32"
_BasicSerialPortTerminalType_Object = MibTableColumn
basicSerialPortTerminalType = _BasicSerialPortTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 7),
    _BasicSerialPortTerminalType_Type()
)
basicSerialPortTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortTerminalType.setStatus("mandatory")


class _BasicSerialPortTypeaheadLimit_Type(Integer32):
    """Custom type basicSerialPortTypeaheadLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 16384),
    )


_BasicSerialPortTypeaheadLimit_Type.__name__ = "Integer32"
_BasicSerialPortTypeaheadLimit_Object = MibTableColumn
basicSerialPortTypeaheadLimit = _BasicSerialPortTypeaheadLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 8),
    _BasicSerialPortTypeaheadLimit_Type()
)
basicSerialPortTypeaheadLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortTypeaheadLimit.setStatus("mandatory")


class _BasicSerialPortBackwardSwitch_Type(Integer32):
    """Custom type basicSerialPortBackwardSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortBackwardSwitch_Type.__name__ = "Integer32"
_BasicSerialPortBackwardSwitch_Object = MibTableColumn
basicSerialPortBackwardSwitch = _BasicSerialPortBackwardSwitch_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 9),
    _BasicSerialPortBackwardSwitch_Type()
)
basicSerialPortBackwardSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortBackwardSwitch.setStatus("mandatory")


class _BasicSerialPortForwardSwitch_Type(Integer32):
    """Custom type basicSerialPortForwardSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortForwardSwitch_Type.__name__ = "Integer32"
_BasicSerialPortForwardSwitch_Object = MibTableColumn
basicSerialPortForwardSwitch = _BasicSerialPortForwardSwitch_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 10),
    _BasicSerialPortForwardSwitch_Type()
)
basicSerialPortForwardSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortForwardSwitch.setStatus("mandatory")


class _BasicSerialPortLocalSwitch_Type(Integer32):
    """Custom type basicSerialPortLocalSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLocalSwitch_Type.__name__ = "Integer32"
_BasicSerialPortLocalSwitch_Object = MibTableColumn
basicSerialPortLocalSwitch = _BasicSerialPortLocalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 11),
    _BasicSerialPortLocalSwitch_Type()
)
basicSerialPortLocalSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLocalSwitch.setStatus("mandatory")


class _BasicSerialPortModemControl_Type(Integer32):
    """Custom type basicSerialPortModemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortModemControl_Type.__name__ = "Integer32"
_BasicSerialPortModemControl_Object = MibTableColumn
basicSerialPortModemControl = _BasicSerialPortModemControl_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 12),
    _BasicSerialPortModemControl_Type()
)
basicSerialPortModemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortModemControl.setStatus("mandatory")


class _BasicSerialPortSignalCheck_Type(Integer32):
    """Custom type basicSerialPortSignalCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortSignalCheck_Type.__name__ = "Integer32"
_BasicSerialPortSignalCheck_Object = MibTableColumn
basicSerialPortSignalCheck = _BasicSerialPortSignalCheck_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 13),
    _BasicSerialPortSignalCheck_Type()
)
basicSerialPortSignalCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortSignalCheck.setStatus("mandatory")


class _BasicSerialPortDSRLogout_Type(Integer32):
    """Custom type basicSerialPortDSRLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortDSRLogout_Type.__name__ = "Integer32"
_BasicSerialPortDSRLogout_Object = MibTableColumn
basicSerialPortDSRLogout = _BasicSerialPortDSRLogout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 14),
    _BasicSerialPortDSRLogout_Type()
)
basicSerialPortDSRLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortDSRLogout.setStatus("mandatory")


class _BasicSerialPortDSRObserve_Type(Integer32):
    """Custom type basicSerialPortDSRObserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortDSRObserve_Type.__name__ = "Integer32"
_BasicSerialPortDSRObserve_Object = MibTableColumn
basicSerialPortDSRObserve = _BasicSerialPortDSRObserve_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 15),
    _BasicSerialPortDSRObserve_Type()
)
basicSerialPortDSRObserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortDSRObserve.setStatus("mandatory")


class _BasicSerialPortDCDTimeout_Type(Integer32):
    """Custom type basicSerialPortDCDTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_BasicSerialPortDCDTimeout_Type.__name__ = "Integer32"
_BasicSerialPortDCDTimeout_Object = MibTableColumn
basicSerialPortDCDTimeout = _BasicSerialPortDCDTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 16),
    _BasicSerialPortDCDTimeout_Type()
)
basicSerialPortDCDTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortDCDTimeout.setStatus("mandatory")


class _BasicSerialPortDTRAssert_Type(Integer32):
    """Custom type basicSerialPortDTRAssert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("onConnection", 3),
          ("onConnectionOrRing", 2),
          ("onRing", 4))
    )


_BasicSerialPortDTRAssert_Type.__name__ = "Integer32"
_BasicSerialPortDTRAssert_Object = MibTableColumn
basicSerialPortDTRAssert = _BasicSerialPortDTRAssert_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 17),
    _BasicSerialPortDTRAssert_Type()
)
basicSerialPortDTRAssert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortDTRAssert.setStatus("mandatory")


class _BasicSerialPortLimitedCommands_Type(Integer32):
    """Custom type basicSerialPortLimitedCommands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortLimitedCommands_Type.__name__ = "Integer32"
_BasicSerialPortLimitedCommands_Object = MibTableColumn
basicSerialPortLimitedCommands = _BasicSerialPortLimitedCommands_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 18),
    _BasicSerialPortLimitedCommands_Type()
)
basicSerialPortLimitedCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLimitedCommands.setStatus("mandatory")


class _BasicSerialPortLimitedView_Type(Integer32):
    """Custom type basicSerialPortLimitedView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortLimitedView_Type.__name__ = "Integer32"
_BasicSerialPortLimitedView_Object = MibTableColumn
basicSerialPortLimitedView = _BasicSerialPortLimitedView_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 19),
    _BasicSerialPortLimitedView_Type()
)
basicSerialPortLimitedView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLimitedView.setStatus("mandatory")


class _BasicSerialPortPassword_Type(Integer32):
    """Custom type basicSerialPortPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortPassword_Type.__name__ = "Integer32"
_BasicSerialPortPassword_Object = MibTableColumn
basicSerialPortPassword = _BasicSerialPortPassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 20),
    _BasicSerialPortPassword_Type()
)
basicSerialPortPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortPassword.setStatus("mandatory")


class _BasicSerialPortLineEditor_Type(Integer32):
    """Custom type basicSerialPortLineEditor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortLineEditor_Type.__name__ = "Integer32"
_BasicSerialPortLineEditor_Object = MibTableColumn
basicSerialPortLineEditor = _BasicSerialPortLineEditor_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 21),
    _BasicSerialPortLineEditor_Type()
)
basicSerialPortLineEditor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditor.setStatus("mandatory")


class _BasicSerialPortLineEditorBackspace_Type(Integer32):
    """Custom type basicSerialPortLineEditorBackspace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorBackspace_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorBackspace_Object = MibTableColumn
basicSerialPortLineEditorBackspace = _BasicSerialPortLineEditorBackspace_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 22),
    _BasicSerialPortLineEditorBackspace_Type()
)
basicSerialPortLineEditorBackspace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorBackspace.setStatus("mandatory")


class _BasicSerialPortLineEditorBeginning_Type(Integer32):
    """Custom type basicSerialPortLineEditorBeginning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorBeginning_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorBeginning_Object = MibTableColumn
basicSerialPortLineEditorBeginning = _BasicSerialPortLineEditorBeginning_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 23),
    _BasicSerialPortLineEditorBeginning_Type()
)
basicSerialPortLineEditorBeginning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorBeginning.setStatus("mandatory")


class _BasicSerialPortLineEditorCancel_Type(Integer32):
    """Custom type basicSerialPortLineEditorCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorCancel_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorCancel_Object = MibTableColumn
basicSerialPortLineEditorCancel = _BasicSerialPortLineEditorCancel_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 24),
    _BasicSerialPortLineEditorCancel_Type()
)
basicSerialPortLineEditorCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorCancel.setStatus("mandatory")


class _BasicSerialPortLineEditorDeleteBeginning_Type(Integer32):
    """Custom type basicSerialPortLineEditorDeleteBeginning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorDeleteBeginning_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorDeleteBeginning_Object = MibTableColumn
basicSerialPortLineEditorDeleteBeginning = _BasicSerialPortLineEditorDeleteBeginning_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 25),
    _BasicSerialPortLineEditorDeleteBeginning_Type()
)
basicSerialPortLineEditorDeleteBeginning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorDeleteBeginning.setStatus("mandatory")


class _BasicSerialPortLineEditorDeleteLine_Type(Integer32):
    """Custom type basicSerialPortLineEditorDeleteLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorDeleteLine_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorDeleteLine_Object = MibTableColumn
basicSerialPortLineEditorDeleteLine = _BasicSerialPortLineEditorDeleteLine_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 26),
    _BasicSerialPortLineEditorDeleteLine_Type()
)
basicSerialPortLineEditorDeleteLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorDeleteLine.setStatus("mandatory")


class _BasicSerialPortLineEditorEnd_Type(Integer32):
    """Custom type basicSerialPortLineEditorEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorEnd_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorEnd_Object = MibTableColumn
basicSerialPortLineEditorEnd = _BasicSerialPortLineEditorEnd_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 27),
    _BasicSerialPortLineEditorEnd_Type()
)
basicSerialPortLineEditorEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorEnd.setStatus("mandatory")


class _BasicSerialPortLineEditorForward_Type(Integer32):
    """Custom type basicSerialPortLineEditorForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorForward_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorForward_Object = MibTableColumn
basicSerialPortLineEditorForward = _BasicSerialPortLineEditorForward_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 28),
    _BasicSerialPortLineEditorForward_Type()
)
basicSerialPortLineEditorForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorForward.setStatus("mandatory")


class _BasicSerialPortLineEditorInsertToggle_Type(Integer32):
    """Custom type basicSerialPortLineEditorInsertToggle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorInsertToggle_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorInsertToggle_Object = MibTableColumn
basicSerialPortLineEditorInsertToggle = _BasicSerialPortLineEditorInsertToggle_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 29),
    _BasicSerialPortLineEditorInsertToggle_Type()
)
basicSerialPortLineEditorInsertToggle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorInsertToggle.setStatus("mandatory")


class _BasicSerialPortLineEditorNextLine_Type(Integer32):
    """Custom type basicSerialPortLineEditorNextLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorNextLine_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorNextLine_Object = MibTableColumn
basicSerialPortLineEditorNextLine = _BasicSerialPortLineEditorNextLine_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 30),
    _BasicSerialPortLineEditorNextLine_Type()
)
basicSerialPortLineEditorNextLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorNextLine.setStatus("mandatory")


class _BasicSerialPortLineEditorPreviousLine_Type(Integer32):
    """Custom type basicSerialPortLineEditorPreviousLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorPreviousLine_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorPreviousLine_Object = MibTableColumn
basicSerialPortLineEditorPreviousLine = _BasicSerialPortLineEditorPreviousLine_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 31),
    _BasicSerialPortLineEditorPreviousLine_Type()
)
basicSerialPortLineEditorPreviousLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorPreviousLine.setStatus("mandatory")


class _BasicSerialPortLineEditorQuotingCharacter_Type(Integer32):
    """Custom type basicSerialPortLineEditorQuotingCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorQuotingCharacter_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorQuotingCharacter_Object = MibTableColumn
basicSerialPortLineEditorQuotingCharacter = _BasicSerialPortLineEditorQuotingCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 32),
    _BasicSerialPortLineEditorQuotingCharacter_Type()
)
basicSerialPortLineEditorQuotingCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorQuotingCharacter.setStatus("mandatory")


class _BasicSerialPortLineEditorRedisplay_Type(Integer32):
    """Custom type basicSerialPortLineEditorRedisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorRedisplay_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorRedisplay_Object = MibTableColumn
basicSerialPortLineEditorRedisplay = _BasicSerialPortLineEditorRedisplay_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 33),
    _BasicSerialPortLineEditorRedisplay_Type()
)
basicSerialPortLineEditorRedisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorRedisplay.setStatus("mandatory")


class _BasicSerialPortQuadartReceiveDiscard_Type(Integer32):
    """Custom type basicSerialPortQuadartReceiveDiscard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortQuadartReceiveDiscard_Type.__name__ = "Integer32"
_BasicSerialPortQuadartReceiveDiscard_Object = MibTableColumn
basicSerialPortQuadartReceiveDiscard = _BasicSerialPortQuadartReceiveDiscard_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 34),
    _BasicSerialPortQuadartReceiveDiscard_Type()
)
basicSerialPortQuadartReceiveDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortQuadartReceiveDiscard.setStatus("mandatory")


class _BasicSerialPortAPDProtocols_Type(OctetString):
    """Custom type basicSerialPortAPDProtocols based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BasicSerialPortAPDProtocols_Type.__name__ = "OctetString"
_BasicSerialPortAPDProtocols_Object = MibTableColumn
basicSerialPortAPDProtocols = _BasicSerialPortAPDProtocols_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 35),
    _BasicSerialPortAPDProtocols_Type()
)
basicSerialPortAPDProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortAPDProtocols.setStatus("mandatory")


class _BasicSerialPortAPDTimeout_Type(Integer32):
    """Custom type basicSerialPortAPDTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortAPDTimeout_Type.__name__ = "Integer32"
_BasicSerialPortAPDTimeout_Object = MibTableColumn
basicSerialPortAPDTimeout = _BasicSerialPortAPDTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 36),
    _BasicSerialPortAPDTimeout_Type()
)
basicSerialPortAPDTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortAPDTimeout.setStatus("mandatory")


class _BasicSerialPortAPDDefaultProtocol_Type(OctetString):
    """Custom type basicSerialPortAPDDefaultProtocol based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BasicSerialPortAPDDefaultProtocol_Type.__name__ = "OctetString"
_BasicSerialPortAPDDefaultProtocol_Object = MibTableColumn
basicSerialPortAPDDefaultProtocol = _BasicSerialPortAPDDefaultProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 37),
    _BasicSerialPortAPDDefaultProtocol_Type()
)
basicSerialPortAPDDefaultProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortAPDDefaultProtocol.setStatus("mandatory")


class _BasicSerialPortUsernameCharSet_Type(Integer32):
    """Custom type basicSerialPortUsernameCharSet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("seven-bit", 2))
    )


_BasicSerialPortUsernameCharSet_Type.__name__ = "Integer32"
_BasicSerialPortUsernameCharSet_Object = MibTableColumn
basicSerialPortUsernameCharSet = _BasicSerialPortUsernameCharSet_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 38),
    _BasicSerialPortUsernameCharSet_Type()
)
basicSerialPortUsernameCharSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortUsernameCharSet.setStatus("mandatory")


class _BasicSerialPortAutoHangup_Type(Integer32):
    """Custom type basicSerialPortAutoHangup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortAutoHangup_Type.__name__ = "Integer32"
_BasicSerialPortAutoHangup_Object = MibTableColumn
basicSerialPortAutoHangup = _BasicSerialPortAutoHangup_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 39),
    _BasicSerialPortAutoHangup_Type()
)
basicSerialPortAutoHangup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortAutoHangup.setStatus("mandatory")


class _BasicSerialPortCommandSize_Type(Integer32):
    """Custom type basicSerialPortCommandSize based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 16384),
    )


_BasicSerialPortCommandSize_Type.__name__ = "Integer32"
_BasicSerialPortCommandSize_Object = MibTableColumn
basicSerialPortCommandSize = _BasicSerialPortCommandSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 40),
    _BasicSerialPortCommandSize_Type()
)
basicSerialPortCommandSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortCommandSize.setStatus("mandatory")


class _BasicSerialPortAutoProtocolDetectPrompt_Type(Integer32):
    """Custom type basicSerialPortAutoProtocolDetectPrompt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortAutoProtocolDetectPrompt_Type.__name__ = "Integer32"
_BasicSerialPortAutoProtocolDetectPrompt_Object = MibTableColumn
basicSerialPortAutoProtocolDetectPrompt = _BasicSerialPortAutoProtocolDetectPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 41),
    _BasicSerialPortAutoProtocolDetectPrompt_Type()
)
basicSerialPortAutoProtocolDetectPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortAutoProtocolDetectPrompt.setStatus("mandatory")


class _BasicSerialPortUsernamePrompt_Type(DisplayString):
    """Custom type basicSerialPortUsernamePrompt based on DisplayString"""
    defaultValue = OctetString("Enter username>")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_BasicSerialPortUsernamePrompt_Type.__name__ = "DisplayString"
_BasicSerialPortUsernamePrompt_Object = MibTableColumn
basicSerialPortUsernamePrompt = _BasicSerialPortUsernamePrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 42),
    _BasicSerialPortUsernamePrompt_Type()
)
basicSerialPortUsernamePrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortUsernamePrompt.setStatus("mandatory")


class _BasicSerialPortPasswordPrompt_Type(DisplayString):
    """Custom type basicSerialPortPasswordPrompt based on DisplayString"""
    defaultValue = OctetString("Enter user password>")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_BasicSerialPortPasswordPrompt_Type.__name__ = "DisplayString"
_BasicSerialPortPasswordPrompt_Object = MibTableColumn
basicSerialPortPasswordPrompt = _BasicSerialPortPasswordPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 43),
    _BasicSerialPortPasswordPrompt_Type()
)
basicSerialPortPasswordPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortPasswordPrompt.setStatus("mandatory")


class _BasicSerialPortAutoProtocolDetectSecurityInteractiveOnly_Type(Integer32):
    """Custom type basicSerialPortAutoProtocolDetectSecurityInteractiveOnly based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortAutoProtocolDetectSecurityInteractiveOnly_Type.__name__ = "Integer32"
_BasicSerialPortAutoProtocolDetectSecurityInteractiveOnly_Object = MibTableColumn
basicSerialPortAutoProtocolDetectSecurityInteractiveOnly = _BasicSerialPortAutoProtocolDetectSecurityInteractiveOnly_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 44),
    _BasicSerialPortAutoProtocolDetectSecurityInteractiveOnly_Type()
)
basicSerialPortAutoProtocolDetectSecurityInteractiveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortAutoProtocolDetectSecurityInteractiveOnly.setStatus("mandatory")


class _BasicSerialPortDedicatedUserData_Type(DisplayString):
    """Custom type basicSerialPortDedicatedUserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicSerialPortDedicatedUserData_Type.__name__ = "DisplayString"
_BasicSerialPortDedicatedUserData_Object = MibTableColumn
basicSerialPortDedicatedUserData = _BasicSerialPortDedicatedUserData_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 45),
    _BasicSerialPortDedicatedUserData_Type()
)
basicSerialPortDedicatedUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortDedicatedUserData.setStatus("mandatory")


class _BasicSerialPortIpAutoDiscovery_Type(Integer32):
    """Custom type basicSerialPortIpAutoDiscovery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortIpAutoDiscovery_Type.__name__ = "Integer32"
_BasicSerialPortIpAutoDiscovery_Object = MibTableColumn
basicSerialPortIpAutoDiscovery = _BasicSerialPortIpAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 47),
    _BasicSerialPortIpAutoDiscovery_Type()
)
basicSerialPortIpAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortIpAutoDiscovery.setStatus("deprecated")


class _BasicSerialPortDedicatedKickStartData_Type(DisplayString):
    """Custom type basicSerialPortDedicatedKickStartData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicSerialPortDedicatedKickStartData_Type.__name__ = "DisplayString"
_BasicSerialPortDedicatedKickStartData_Object = MibTableColumn
basicSerialPortDedicatedKickStartData = _BasicSerialPortDedicatedKickStartData_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 48),
    _BasicSerialPortDedicatedKickStartData_Type()
)
basicSerialPortDedicatedKickStartData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortDedicatedKickStartData.setStatus("mandatory")


class _BasicSerialPortBreakLength_Type(Integer32):
    """Custom type basicSerialPortBreakLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms250", 1),
          ("ms500", 2),
          ("ms750", 3))
    )


_BasicSerialPortBreakLength_Type.__name__ = "Integer32"
_BasicSerialPortBreakLength_Object = MibTableColumn
basicSerialPortBreakLength = _BasicSerialPortBreakLength_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 50),
    _BasicSerialPortBreakLength_Type()
)
basicSerialPortBreakLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortBreakLength.setStatus("mandatory")


class _BasicSerialPortRotaryRoundRobin_Type(Integer32):
    """Custom type basicSerialPortRotaryRoundRobin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortRotaryRoundRobin_Type.__name__ = "Integer32"
_BasicSerialPortRotaryRoundRobin_Object = MibTableColumn
basicSerialPortRotaryRoundRobin = _BasicSerialPortRotaryRoundRobin_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 51),
    _BasicSerialPortRotaryRoundRobin_Type()
)
basicSerialPortRotaryRoundRobin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortRotaryRoundRobin.setStatus("mandatory")


class _BasicSerialPortWelcomeBeforeAuthentication_Type(Integer32):
    """Custom type basicSerialPortWelcomeBeforeAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortWelcomeBeforeAuthentication_Type.__name__ = "Integer32"
_BasicSerialPortWelcomeBeforeAuthentication_Object = MibTableColumn
basicSerialPortWelcomeBeforeAuthentication = _BasicSerialPortWelcomeBeforeAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 52),
    _BasicSerialPortWelcomeBeforeAuthentication_Type()
)
basicSerialPortWelcomeBeforeAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortWelcomeBeforeAuthentication.setStatus("mandatory")


class _BasicSerialPortGatewayAutoDiscovery_Type(Integer32):
    """Custom type basicSerialPortGatewayAutoDiscovery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortGatewayAutoDiscovery_Type.__name__ = "Integer32"
_BasicSerialPortGatewayAutoDiscovery_Object = MibTableColumn
basicSerialPortGatewayAutoDiscovery = _BasicSerialPortGatewayAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 53),
    _BasicSerialPortGatewayAutoDiscovery_Type()
)
basicSerialPortGatewayAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortGatewayAutoDiscovery.setStatus("deprecated")


class _BasicSerialPortSubnetAutoDiscovery_Type(Integer32):
    """Custom type basicSerialPortSubnetAutoDiscovery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortSubnetAutoDiscovery_Type.__name__ = "Integer32"
_BasicSerialPortSubnetAutoDiscovery_Object = MibTableColumn
basicSerialPortSubnetAutoDiscovery = _BasicSerialPortSubnetAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 54),
    _BasicSerialPortSubnetAutoDiscovery_Type()
)
basicSerialPortSubnetAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortSubnetAutoDiscovery.setStatus("deprecated")


class _BasicSerialPortRaiseLowerDtr_Type(Integer32):
    """Custom type basicSerialPortRaiseLowerDtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_BasicSerialPortRaiseLowerDtr_Type.__name__ = "Integer32"
_BasicSerialPortRaiseLowerDtr_Object = MibTableColumn
basicSerialPortRaiseLowerDtr = _BasicSerialPortRaiseLowerDtr_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 55),
    _BasicSerialPortRaiseLowerDtr_Type()
)
basicSerialPortRaiseLowerDtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortRaiseLowerDtr.setStatus("mandatory")


class _BasicSerialPortRaiseControlDtr_Type(Integer32):
    """Custom type basicSerialPortRaiseControlDtr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortRaiseControlDtr_Type.__name__ = "Integer32"
_BasicSerialPortRaiseControlDtr_Object = MibTableColumn
basicSerialPortRaiseControlDtr = _BasicSerialPortRaiseControlDtr_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 56),
    _BasicSerialPortRaiseControlDtr_Type()
)
basicSerialPortRaiseControlDtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortRaiseControlDtr.setStatus("mandatory")


class _BasicSerialPortIpConfigureBootp_Type(Integer32):
    """Custom type basicSerialPortIpConfigureBootp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortIpConfigureBootp_Type.__name__ = "Integer32"
_BasicSerialPortIpConfigureBootp_Object = MibTableColumn
basicSerialPortIpConfigureBootp = _BasicSerialPortIpConfigureBootp_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 57),
    _BasicSerialPortIpConfigureBootp_Type()
)
basicSerialPortIpConfigureBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortIpConfigureBootp.setStatus("deprecated")


class _BasicConsoleLogoutDisconnect_Type(Integer32):
    """Custom type basicConsoleLogoutDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicConsoleLogoutDisconnect_Type.__name__ = "Integer32"
_BasicConsoleLogoutDisconnect_Object = MibScalar
basicConsoleLogoutDisconnect = _BasicConsoleLogoutDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 19),
    _BasicConsoleLogoutDisconnect_Type()
)
basicConsoleLogoutDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicConsoleLogoutDisconnect.setStatus("mandatory")


class _BasicControlledPorts_Type(Integer32):
    """Custom type basicControlledPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicControlledPorts_Type.__name__ = "Integer32"
_BasicControlledPorts_Object = MibScalar
basicControlledPorts = _BasicControlledPorts_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 20),
    _BasicControlledPorts_Type()
)
basicControlledPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicControlledPorts.setStatus("mandatory")
_BasicPortSessionTable_Object = MibTable
basicPortSessionTable = _BasicPortSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 21)
)
if mibBuilder.loadTexts:
    basicPortSessionTable.setStatus("mandatory")
_BasicPortSessEntry_Object = MibTableRow
basicPortSessEntry = _BasicPortSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 21, 1)
)
basicPortSessEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicPortPortIndex"),
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicPortSessIndex"),
)
if mibBuilder.loadTexts:
    basicPortSessEntry.setStatus("mandatory")
_BasicPortPortIndex_Type = Integer32
_BasicPortPortIndex_Object = MibTableColumn
basicPortPortIndex = _BasicPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 21, 1, 1),
    _BasicPortPortIndex_Type()
)
basicPortPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortPortIndex.setStatus("mandatory")
_BasicPortSessIndex_Type = Integer32
_BasicPortSessIndex_Object = MibTableColumn
basicPortSessIndex = _BasicPortSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 21, 1, 2),
    _BasicPortSessIndex_Type()
)
basicPortSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortSessIndex.setStatus("mandatory")


class _BasicSessControlled_Type(Integer32):
    """Custom type basicSessControlled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSessControlled_Type.__name__ = "Integer32"
_BasicSessControlled_Object = MibTableColumn
basicSessControlled = _BasicSessControlled_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 21, 1, 3),
    _BasicSessControlled_Type()
)
basicSessControlled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicSessControlled.setStatus("mandatory")


class _BasicPortSessEncryption_Type(Integer32):
    """Custom type basicPortSessEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortSessEncryption_Type.__name__ = "Integer32"
_BasicPortSessEncryption_Object = MibScalar
basicPortSessEncryption = _BasicPortSessEncryption_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 22),
    _BasicPortSessEncryption_Type()
)
basicPortSessEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortSessEncryption.setStatus("mandatory")


class _BasicTemperatureUnits_Type(Integer32):
    """Custom type basicTemperatureUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celcius", 2),
          ("fahrenheit", 1))
    )


_BasicTemperatureUnits_Type.__name__ = "Integer32"
_BasicTemperatureUnits_Object = MibScalar
basicTemperatureUnits = _BasicTemperatureUnits_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 23),
    _BasicTemperatureUnits_Type()
)
basicTemperatureUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicTemperatureUnits.setStatus("mandatory")


class _BasicEnvironmentalManagerCircuitBreaker_Type(Integer32):
    """Custom type basicEnvironmentalManagerCircuitBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicEnvironmentalManagerCircuitBreaker_Type.__name__ = "Integer32"
_BasicEnvironmentalManagerCircuitBreaker_Object = MibScalar
basicEnvironmentalManagerCircuitBreaker = _BasicEnvironmentalManagerCircuitBreaker_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 24),
    _BasicEnvironmentalManagerCircuitBreaker_Type()
)
basicEnvironmentalManagerCircuitBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicEnvironmentalManagerCircuitBreaker.setStatus("mandatory")
_BasicContactClosureOrAlarmInputTable_Object = MibTable
basicContactClosureOrAlarmInputTable = _BasicContactClosureOrAlarmInputTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25)
)
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputTable.setStatus("mandatory")
_BasicContactClosureOrAlarmInputEntry_Object = MibTableRow
basicContactClosureOrAlarmInputEntry = _BasicContactClosureOrAlarmInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1)
)
basicContactClosureOrAlarmInputEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
)
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputEntry.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputValue_Type(Integer32):
    """Custom type basicContactClosureOrAlarmInputValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_BasicContactClosureOrAlarmInputValue_Type.__name__ = "Integer32"
_BasicContactClosureOrAlarmInputValue_Object = MibTableColumn
basicContactClosureOrAlarmInputValue = _BasicContactClosureOrAlarmInputValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 1),
    _BasicContactClosureOrAlarmInputValue_Type()
)
basicContactClosureOrAlarmInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputValue.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputName_Type(DisplayString):
    """Custom type basicContactClosureOrAlarmInputName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicContactClosureOrAlarmInputName_Type.__name__ = "DisplayString"
_BasicContactClosureOrAlarmInputName_Object = MibTableColumn
basicContactClosureOrAlarmInputName = _BasicContactClosureOrAlarmInputName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 2),
    _BasicContactClosureOrAlarmInputName_Type()
)
basicContactClosureOrAlarmInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputName.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputTrapEnable_Type(Integer32):
    """Custom type basicContactClosureOrAlarmInputTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicContactClosureOrAlarmInputTrapEnable_Type.__name__ = "Integer32"
_BasicContactClosureOrAlarmInputTrapEnable_Object = MibTableColumn
basicContactClosureOrAlarmInputTrapEnable = _BasicContactClosureOrAlarmInputTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 3),
    _BasicContactClosureOrAlarmInputTrapEnable_Type()
)
basicContactClosureOrAlarmInputTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputTrapEnable.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputFaultSeverity_Type(Integer32):
    """Custom type basicContactClosureOrAlarmInputFaultSeverity based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicContactClosureOrAlarmInputFaultSeverity_Type.__name__ = "Integer32"
_BasicContactClosureOrAlarmInputFaultSeverity_Object = MibTableColumn
basicContactClosureOrAlarmInputFaultSeverity = _BasicContactClosureOrAlarmInputFaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 4),
    _BasicContactClosureOrAlarmInputFaultSeverity_Type()
)
basicContactClosureOrAlarmInputFaultSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputFaultSeverity.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputFaultState_Type(Integer32):
    """Custom type basicContactClosureOrAlarmInputFaultState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_BasicContactClosureOrAlarmInputFaultState_Type.__name__ = "Integer32"
_BasicContactClosureOrAlarmInputFaultState_Object = MibTableColumn
basicContactClosureOrAlarmInputFaultState = _BasicContactClosureOrAlarmInputFaultState_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 5),
    _BasicContactClosureOrAlarmInputFaultState_Type()
)
basicContactClosureOrAlarmInputFaultState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputFaultState.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputStatus_Type(Integer32):
    """Custom type basicContactClosureOrAlarmInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicContactClosureOrAlarmInputStatus_Type.__name__ = "Integer32"
_BasicContactClosureOrAlarmInputStatus_Object = MibTableColumn
basicContactClosureOrAlarmInputStatus = _BasicContactClosureOrAlarmInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 6),
    _BasicContactClosureOrAlarmInputStatus_Type()
)
basicContactClosureOrAlarmInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputStatus.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputZone_Type(DisplayString):
    """Custom type basicContactClosureOrAlarmInputZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicContactClosureOrAlarmInputZone_Type.__name__ = "DisplayString"
_BasicContactClosureOrAlarmInputZone_Object = MibTableColumn
basicContactClosureOrAlarmInputZone = _BasicContactClosureOrAlarmInputZone_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 7),
    _BasicContactClosureOrAlarmInputZone_Type()
)
basicContactClosureOrAlarmInputZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputZone.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputRelatedEquipment_Type(DisplayString):
    """Custom type basicContactClosureOrAlarmInputRelatedEquipment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicContactClosureOrAlarmInputRelatedEquipment_Type.__name__ = "DisplayString"
_BasicContactClosureOrAlarmInputRelatedEquipment_Object = MibTableColumn
basicContactClosureOrAlarmInputRelatedEquipment = _BasicContactClosureOrAlarmInputRelatedEquipment_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 8),
    _BasicContactClosureOrAlarmInputRelatedEquipment_Type()
)
basicContactClosureOrAlarmInputRelatedEquipment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputRelatedEquipment.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputSiteId_Type(DisplayString):
    """Custom type basicContactClosureOrAlarmInputSiteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicContactClosureOrAlarmInputSiteId_Type.__name__ = "DisplayString"
_BasicContactClosureOrAlarmInputSiteId_Object = MibTableColumn
basicContactClosureOrAlarmInputSiteId = _BasicContactClosureOrAlarmInputSiteId_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 9),
    _BasicContactClosureOrAlarmInputSiteId_Type()
)
basicContactClosureOrAlarmInputSiteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputSiteId.setStatus("mandatory")
_BasicContactClosureOrAlarmInputIndex_Type = Integer32
_BasicContactClosureOrAlarmInputIndex_Object = MibTableColumn
basicContactClosureOrAlarmInputIndex = _BasicContactClosureOrAlarmInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 10),
    _BasicContactClosureOrAlarmInputIndex_Type()
)
basicContactClosureOrAlarmInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputIndex.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputManufacturer_Type(DisplayString):
    """Custom type basicContactClosureOrAlarmInputManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicContactClosureOrAlarmInputManufacturer_Type.__name__ = "DisplayString"
_BasicContactClosureOrAlarmInputManufacturer_Object = MibTableColumn
basicContactClosureOrAlarmInputManufacturer = _BasicContactClosureOrAlarmInputManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 11),
    _BasicContactClosureOrAlarmInputManufacturer_Type()
)
basicContactClosureOrAlarmInputManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputManufacturer.setStatus("mandatory")


class _BasicContactClosureOrAlarmInputModel_Type(DisplayString):
    """Custom type basicContactClosureOrAlarmInputModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicContactClosureOrAlarmInputModel_Type.__name__ = "DisplayString"
_BasicContactClosureOrAlarmInputModel_Object = MibTableColumn
basicContactClosureOrAlarmInputModel = _BasicContactClosureOrAlarmInputModel_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 25, 1, 12),
    _BasicContactClosureOrAlarmInputModel_Type()
)
basicContactClosureOrAlarmInputModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicContactClosureOrAlarmInputModel.setStatus("mandatory")
_BasicPowerOutletTable_Object = MibTable
basicPowerOutletTable = _BasicPowerOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 26)
)
if mibBuilder.loadTexts:
    basicPowerOutletTable.setStatus("mandatory")
_BasicPowerOutletEntry_Object = MibTableRow
basicPowerOutletEntry = _BasicPowerOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 26, 1)
)
basicPowerOutletEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicPowerOutletIndex"),
)
if mibBuilder.loadTexts:
    basicPowerOutletEntry.setStatus("mandatory")


class _BasicPowerOutletOnOff_Type(Integer32):
    """Custom type basicPowerOutletOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BasicPowerOutletOnOff_Type.__name__ = "Integer32"
_BasicPowerOutletOnOff_Object = MibTableColumn
basicPowerOutletOnOff = _BasicPowerOutletOnOff_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 26, 1, 1),
    _BasicPowerOutletOnOff_Type()
)
basicPowerOutletOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPowerOutletOnOff.setStatus("mandatory")


class _BasicPowerOutletReboot_Type(Integer32):
    """Custom type basicPowerOutletReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_BasicPowerOutletReboot_Type.__name__ = "Integer32"
_BasicPowerOutletReboot_Object = MibTableColumn
basicPowerOutletReboot = _BasicPowerOutletReboot_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 26, 1, 2),
    _BasicPowerOutletReboot_Type()
)
basicPowerOutletReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPowerOutletReboot.setStatus("mandatory")


class _BasicPowerOutletName_Type(DisplayString):
    """Custom type basicPowerOutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPowerOutletName_Type.__name__ = "DisplayString"
_BasicPowerOutletName_Object = MibTableColumn
basicPowerOutletName = _BasicPowerOutletName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 26, 1, 3),
    _BasicPowerOutletName_Type()
)
basicPowerOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPowerOutletName.setStatus("mandatory")


class _BasicPowerOutletRedundant_Type(Integer32):
    """Custom type basicPowerOutletRedundant based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPowerOutletRedundant_Type.__name__ = "Integer32"
_BasicPowerOutletRedundant_Object = MibTableColumn
basicPowerOutletRedundant = _BasicPowerOutletRedundant_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 26, 1, 4),
    _BasicPowerOutletRedundant_Type()
)
basicPowerOutletRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPowerOutletRedundant.setStatus("mandatory")


class _BasicPowerOutletConsoleName_Type(DisplayString):
    """Custom type basicPowerOutletConsoleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPowerOutletConsoleName_Type.__name__ = "DisplayString"
_BasicPowerOutletConsoleName_Object = MibTableColumn
basicPowerOutletConsoleName = _BasicPowerOutletConsoleName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 26, 1, 5),
    _BasicPowerOutletConsoleName_Type()
)
basicPowerOutletConsoleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPowerOutletConsoleName.setStatus("mandatory")


class _BasicPowerOutletHighCurrent_Type(Integer32):
    """Custom type basicPowerOutletHighCurrent based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPowerOutletHighCurrent_Type.__name__ = "Integer32"
_BasicPowerOutletHighCurrent_Object = MibTableColumn
basicPowerOutletHighCurrent = _BasicPowerOutletHighCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 26, 1, 6),
    _BasicPowerOutletHighCurrent_Type()
)
basicPowerOutletHighCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPowerOutletHighCurrent.setStatus("mandatory")
_BasicPowerOutletIndex_Type = Integer32
_BasicPowerOutletIndex_Object = MibTableColumn
basicPowerOutletIndex = _BasicPowerOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 26, 1, 10),
    _BasicPowerOutletIndex_Type()
)
basicPowerOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPowerOutletIndex.setStatus("mandatory")
_BasicTemperatureHumiditySensor_ObjectIdentity = ObjectIdentity
basicTemperatureHumiditySensor = _BasicTemperatureHumiditySensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27)
)
_BasicTemperatureSensorTable_Object = MibTable
basicTemperatureSensorTable = _BasicTemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 1)
)
if mibBuilder.loadTexts:
    basicTemperatureSensorTable.setStatus("mandatory")
_BasicTemperatureSensorEntry_Object = MibTableRow
basicTemperatureSensorEntry = _BasicTemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 1, 1)
)
basicTemperatureSensorEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    basicTemperatureSensorEntry.setStatus("mandatory")
_BasicTempTrapHighThreshold_Type = Integer32
_BasicTempTrapHighThreshold_Object = MibTableColumn
basicTempTrapHighThreshold = _BasicTempTrapHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 1, 1, 1),
    _BasicTempTrapHighThreshold_Type()
)
basicTempTrapHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicTempTrapHighThreshold.setStatus("mandatory")
_BasicTempTrapLowThreshold_Type = Integer32
_BasicTempTrapLowThreshold_Object = MibTableColumn
basicTempTrapLowThreshold = _BasicTempTrapLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 1, 1, 2),
    _BasicTempTrapLowThreshold_Type()
)
basicTempTrapLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicTempTrapLowThreshold.setStatus("mandatory")


class _BasicTemperatureSensor_Type(Integer32):
    """Custom type basicTemperatureSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicTemperatureSensor_Type.__name__ = "Integer32"
_BasicTemperatureSensor_Object = MibTableColumn
basicTemperatureSensor = _BasicTemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 1, 1, 3),
    _BasicTemperatureSensor_Type()
)
basicTemperatureSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicTemperatureSensor.setStatus("mandatory")
_BasicTemperatureValue_Type = Integer32
_BasicTemperatureValue_Object = MibTableColumn
basicTemperatureValue = _BasicTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 1, 1, 4),
    _BasicTemperatureValue_Type()
)
basicTemperatureValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicTemperatureValue.setStatus("mandatory")


class _BasicTemperatureAlarmSeverity_Type(Integer32):
    """Custom type basicTemperatureAlarmSeverity based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicTemperatureAlarmSeverity_Type.__name__ = "Integer32"
_BasicTemperatureAlarmSeverity_Object = MibTableColumn
basicTemperatureAlarmSeverity = _BasicTemperatureAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 1, 1, 5),
    _BasicTemperatureAlarmSeverity_Type()
)
basicTemperatureAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicTemperatureAlarmSeverity.setStatus("mandatory")


class _BasicTemperatureAlarmStatus_Type(Integer32):
    """Custom type basicTemperatureAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicTemperatureAlarmStatus_Type.__name__ = "Integer32"
_BasicTemperatureAlarmStatus_Object = MibTableColumn
basicTemperatureAlarmStatus = _BasicTemperatureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 1, 1, 6),
    _BasicTemperatureAlarmStatus_Type()
)
basicTemperatureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicTemperatureAlarmStatus.setStatus("mandatory")


class _BasicTemperatureHumiditySensorName_Type(DisplayString):
    """Custom type basicTemperatureHumiditySensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicTemperatureHumiditySensorName_Type.__name__ = "DisplayString"
_BasicTemperatureHumiditySensorName_Object = MibTableColumn
basicTemperatureHumiditySensorName = _BasicTemperatureHumiditySensorName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 1, 1, 7),
    _BasicTemperatureHumiditySensorName_Type()
)
basicTemperatureHumiditySensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicTemperatureHumiditySensorName.setStatus("mandatory")
_BasicTemperatureSensorIndex_Type = Integer32
_BasicTemperatureSensorIndex_Object = MibTableColumn
basicTemperatureSensorIndex = _BasicTemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 1, 1, 10),
    _BasicTemperatureSensorIndex_Type()
)
basicTemperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicTemperatureSensorIndex.setStatus("mandatory")
_BasicHumiditySensorTable_Object = MibTable
basicHumiditySensorTable = _BasicHumiditySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 2)
)
if mibBuilder.loadTexts:
    basicHumiditySensorTable.setStatus("mandatory")
_BasicHumiditySensorEntry_Object = MibTableRow
basicHumiditySensorEntry = _BasicHumiditySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 2, 1)
)
basicHumiditySensorEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicHumiditySensorIndex"),
)
if mibBuilder.loadTexts:
    basicHumiditySensorEntry.setStatus("mandatory")
_BasicHumidityTrapHighThreshold_Type = Integer32
_BasicHumidityTrapHighThreshold_Object = MibTableColumn
basicHumidityTrapHighThreshold = _BasicHumidityTrapHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 2, 1, 1),
    _BasicHumidityTrapHighThreshold_Type()
)
basicHumidityTrapHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicHumidityTrapHighThreshold.setStatus("mandatory")
_BasicHumidityTrapLowThreshold_Type = Integer32
_BasicHumidityTrapLowThreshold_Object = MibTableColumn
basicHumidityTrapLowThreshold = _BasicHumidityTrapLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 2, 1, 2),
    _BasicHumidityTrapLowThreshold_Type()
)
basicHumidityTrapLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicHumidityTrapLowThreshold.setStatus("mandatory")


class _BasicHumiditySensor_Type(Integer32):
    """Custom type basicHumiditySensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicHumiditySensor_Type.__name__ = "Integer32"
_BasicHumiditySensor_Object = MibTableColumn
basicHumiditySensor = _BasicHumiditySensor_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 2, 1, 3),
    _BasicHumiditySensor_Type()
)
basicHumiditySensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicHumiditySensor.setStatus("mandatory")
_BasicHumidityValue_Type = Integer32
_BasicHumidityValue_Object = MibTableColumn
basicHumidityValue = _BasicHumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 2, 1, 4),
    _BasicHumidityValue_Type()
)
basicHumidityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicHumidityValue.setStatus("mandatory")


class _BasicHumidityAlarmSeverity_Type(Integer32):
    """Custom type basicHumidityAlarmSeverity based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicHumidityAlarmSeverity_Type.__name__ = "Integer32"
_BasicHumidityAlarmSeverity_Object = MibTableColumn
basicHumidityAlarmSeverity = _BasicHumidityAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 2, 1, 5),
    _BasicHumidityAlarmSeverity_Type()
)
basicHumidityAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicHumidityAlarmSeverity.setStatus("mandatory")


class _BasicHumidityAlarmStatus_Type(Integer32):
    """Custom type basicHumidityAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicHumidityAlarmStatus_Type.__name__ = "Integer32"
_BasicHumidityAlarmStatus_Object = MibTableColumn
basicHumidityAlarmStatus = _BasicHumidityAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 2, 1, 6),
    _BasicHumidityAlarmStatus_Type()
)
basicHumidityAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHumidityAlarmStatus.setStatus("mandatory")
_BasicHumiditySensorIndex_Type = Integer32
_BasicHumiditySensorIndex_Object = MibTableColumn
basicHumiditySensorIndex = _BasicHumiditySensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 27, 2, 1, 10),
    _BasicHumiditySensorIndex_Type()
)
basicHumiditySensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHumiditySensorIndex.setStatus("mandatory")
_BasicControlSignalTable_Object = MibTable
basicControlSignalTable = _BasicControlSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 28)
)
if mibBuilder.loadTexts:
    basicControlSignalTable.setStatus("mandatory")
_BasicControlSignalEntry_Object = MibTableRow
basicControlSignalEntry = _BasicControlSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 28, 1)
)
basicControlSignalEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicControlSignalIndex"),
)
if mibBuilder.loadTexts:
    basicControlSignalEntry.setStatus("mandatory")


class _BasicControlSignalValue_Type(Integer32):
    """Custom type basicControlSignalValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_BasicControlSignalValue_Type.__name__ = "Integer32"
_BasicControlSignalValue_Object = MibTableColumn
basicControlSignalValue = _BasicControlSignalValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 28, 1, 1),
    _BasicControlSignalValue_Type()
)
basicControlSignalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicControlSignalValue.setStatus("mandatory")
_BasicControlSignalIndex_Type = Integer32
_BasicControlSignalIndex_Object = MibTableColumn
basicControlSignalIndex = _BasicControlSignalIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 28, 1, 10),
    _BasicControlSignalIndex_Type()
)
basicControlSignalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicControlSignalIndex.setStatus("mandatory")


class _BasicPowerAlarmTimer_Type(Integer32):
    """Custom type basicPowerAlarmTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_BasicPowerAlarmTimer_Type.__name__ = "Integer32"
_BasicPowerAlarmTimer_Object = MibScalar
basicPowerAlarmTimer = _BasicPowerAlarmTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 29),
    _BasicPowerAlarmTimer_Type()
)
basicPowerAlarmTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPowerAlarmTimer.setStatus("mandatory")
_BasicControlOutputTable_Object = MibTable
basicControlOutputTable = _BasicControlOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 30)
)
if mibBuilder.loadTexts:
    basicControlOutputTable.setStatus("mandatory")
_BasicControlOutputEntry_Object = MibTableRow
basicControlOutputEntry = _BasicControlOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 30, 1)
)
basicControlOutputEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicControlOutputIndex"),
)
if mibBuilder.loadTexts:
    basicControlOutputEntry.setStatus("mandatory")


class _BasicControlOutputSignalDtrRts_Type(Integer32):
    """Custom type basicControlOutputSignalDtrRts based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_BasicControlOutputSignalDtrRts_Type.__name__ = "Integer32"
_BasicControlOutputSignalDtrRts_Object = MibTableColumn
basicControlOutputSignalDtrRts = _BasicControlOutputSignalDtrRts_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 30, 1, 1),
    _BasicControlOutputSignalDtrRts_Type()
)
basicControlOutputSignalDtrRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicControlOutputSignalDtrRts.setStatus("mandatory")


class _BasicControlOutputName_Type(DisplayString):
    """Custom type basicControlOutputName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicControlOutputName_Type.__name__ = "DisplayString"
_BasicControlOutputName_Object = MibTableColumn
basicControlOutputName = _BasicControlOutputName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 30, 1, 2),
    _BasicControlOutputName_Type()
)
basicControlOutputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicControlOutputName.setStatus("mandatory")
_BasicControlOutputIndex_Type = Integer32
_BasicControlOutputIndex_Object = MibTableColumn
basicControlOutputIndex = _BasicControlOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 30, 1, 10),
    _BasicControlOutputIndex_Type()
)
basicControlOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicControlOutputIndex.setStatus("mandatory")


class _BasicPowerStatusFuseA_Type(Integer32):
    """Custom type basicPowerStatusFuseA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BasicPowerStatusFuseA_Type.__name__ = "Integer32"
_BasicPowerStatusFuseA_Object = MibScalar
basicPowerStatusFuseA = _BasicPowerStatusFuseA_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 31),
    _BasicPowerStatusFuseA_Type()
)
basicPowerStatusFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPowerStatusFuseA.setStatus("mandatory")


class _BasicPowerStatusFuseB_Type(Integer32):
    """Custom type basicPowerStatusFuseB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BasicPowerStatusFuseB_Type.__name__ = "Integer32"
_BasicPowerStatusFuseB_Object = MibScalar
basicPowerStatusFuseB = _BasicPowerStatusFuseB_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 32),
    _BasicPowerStatusFuseB_Type()
)
basicPowerStatusFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPowerStatusFuseB.setStatus("mandatory")


class _BasicPowerSupplyStatusA_Type(Integer32):
    """Custom type basicPowerSupplyStatusA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BasicPowerSupplyStatusA_Type.__name__ = "Integer32"
_BasicPowerSupplyStatusA_Object = MibScalar
basicPowerSupplyStatusA = _BasicPowerSupplyStatusA_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 33),
    _BasicPowerSupplyStatusA_Type()
)
basicPowerSupplyStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPowerSupplyStatusA.setStatus("mandatory")


class _BasicPowerSupplyStatusB_Type(Integer32):
    """Custom type basicPowerSupplyStatusB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BasicPowerSupplyStatusB_Type.__name__ = "Integer32"
_BasicPowerSupplyStatusB_Object = MibScalar
basicPowerSupplyStatusB = _BasicPowerSupplyStatusB_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 34),
    _BasicPowerSupplyStatusB_Type()
)
basicPowerSupplyStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPowerSupplyStatusB.setStatus("mandatory")
_BasicPortTrapTable_Object = MibTable
basicPortTrapTable = _BasicPortTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 35)
)
if mibBuilder.loadTexts:
    basicPortTrapTable.setStatus("mandatory")
_BasicPortTrapEntry_Object = MibTableRow
basicPortTrapEntry = _BasicPortTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 35, 1)
)
basicPortTrapEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicPortTrapIndex"),
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicPortSignalName"),
)
if mibBuilder.loadTexts:
    basicPortTrapEntry.setStatus("mandatory")
_BasicPortTrapIndex_Type = Integer32
_BasicPortTrapIndex_Object = MibTableColumn
basicPortTrapIndex = _BasicPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 35, 1, 1),
    _BasicPortTrapIndex_Type()
)
basicPortTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortTrapIndex.setStatus("mandatory")


class _BasicPortSignalName_Type(Integer32):
    """Custom type basicPortSignalName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cts", 2),
          ("dcd", 6),
          ("dsr", 3),
          ("dtr", 4),
          ("ri", 5),
          ("rts", 1))
    )


_BasicPortSignalName_Type.__name__ = "Integer32"
_BasicPortSignalName_Object = MibTableColumn
basicPortSignalName = _BasicPortSignalName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 35, 1, 2),
    _BasicPortSignalName_Type()
)
basicPortSignalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortSignalName.setStatus("mandatory")


class _BasicPortTrapStatus_Type(Integer32):
    """Custom type basicPortTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortTrapStatus_Type.__name__ = "Integer32"
_BasicPortTrapStatus_Object = MibTableColumn
basicPortTrapStatus = _BasicPortTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 35, 1, 3),
    _BasicPortTrapStatus_Type()
)
basicPortTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortTrapStatus.setStatus("mandatory")
_BasicAlarmMasterInputTable_Object = MibTable
basicAlarmMasterInputTable = _BasicAlarmMasterInputTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36)
)
if mibBuilder.loadTexts:
    basicAlarmMasterInputTable.setStatus("mandatory")
_BasicAlarmMasterInputEntry_Object = MibTableRow
basicAlarmMasterInputEntry = _BasicAlarmMasterInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1)
)
basicAlarmMasterInputEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
)
if mibBuilder.loadTexts:
    basicAlarmMasterInputEntry.setStatus("mandatory")
_BasicAlarmMasterInputPort_Type = Integer32
_BasicAlarmMasterInputPort_Object = MibTableColumn
basicAlarmMasterInputPort = _BasicAlarmMasterInputPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 1),
    _BasicAlarmMasterInputPort_Type()
)
basicAlarmMasterInputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicAlarmMasterInputPort.setStatus("mandatory")
_BasicAlarmMasterInputSlot_Type = Integer32
_BasicAlarmMasterInputSlot_Object = MibTableColumn
basicAlarmMasterInputSlot = _BasicAlarmMasterInputSlot_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 2),
    _BasicAlarmMasterInputSlot_Type()
)
basicAlarmMasterInputSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicAlarmMasterInputSlot.setStatus("mandatory")
_BasicAlarmMasterInputPoint_Type = Integer32
_BasicAlarmMasterInputPoint_Object = MibTableColumn
basicAlarmMasterInputPoint = _BasicAlarmMasterInputPoint_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 3),
    _BasicAlarmMasterInputPoint_Type()
)
basicAlarmMasterInputPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicAlarmMasterInputPoint.setStatus("mandatory")


class _BasicAlarmMasterInputName_Type(DisplayString):
    """Custom type basicAlarmMasterInputName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicAlarmMasterInputName_Type.__name__ = "DisplayString"
_BasicAlarmMasterInputName_Object = MibTableColumn
basicAlarmMasterInputName = _BasicAlarmMasterInputName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 4),
    _BasicAlarmMasterInputName_Type()
)
basicAlarmMasterInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputName.setStatus("mandatory")


class _BasicAlarmMasterInputTrapEnable_Type(Integer32):
    """Custom type basicAlarmMasterInputTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicAlarmMasterInputTrapEnable_Type.__name__ = "Integer32"
_BasicAlarmMasterInputTrapEnable_Object = MibTableColumn
basicAlarmMasterInputTrapEnable = _BasicAlarmMasterInputTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 5),
    _BasicAlarmMasterInputTrapEnable_Type()
)
basicAlarmMasterInputTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputTrapEnable.setStatus("mandatory")


class _BasicAlarmMasterControlOutputSignal_Type(Integer32):
    """Custom type basicAlarmMasterControlOutputSignal based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_BasicAlarmMasterControlOutputSignal_Type.__name__ = "Integer32"
_BasicAlarmMasterControlOutputSignal_Object = MibTableColumn
basicAlarmMasterControlOutputSignal = _BasicAlarmMasterControlOutputSignal_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 6),
    _BasicAlarmMasterControlOutputSignal_Type()
)
basicAlarmMasterControlOutputSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterControlOutputSignal.setStatus("mandatory")


class _BasicAlarmMasterInputEnable_Type(Integer32):
    """Custom type basicAlarmMasterInputEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicAlarmMasterInputEnable_Type.__name__ = "Integer32"
_BasicAlarmMasterInputEnable_Object = MibTableColumn
basicAlarmMasterInputEnable = _BasicAlarmMasterInputEnable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 7),
    _BasicAlarmMasterInputEnable_Type()
)
basicAlarmMasterInputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputEnable.setStatus("mandatory")


class _BasicAlarmMasterInputDebounceInterval_Type(Integer32):
    """Custom type basicAlarmMasterInputDebounceInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_BasicAlarmMasterInputDebounceInterval_Type.__name__ = "Integer32"
_BasicAlarmMasterInputDebounceInterval_Object = MibTableColumn
basicAlarmMasterInputDebounceInterval = _BasicAlarmMasterInputDebounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 8),
    _BasicAlarmMasterInputDebounceInterval_Type()
)
basicAlarmMasterInputDebounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputDebounceInterval.setStatus("mandatory")


class _BasicAlarmMasterInputFaultSeverity_Type(Integer32):
    """Custom type basicAlarmMasterInputFaultSeverity based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicAlarmMasterInputFaultSeverity_Type.__name__ = "Integer32"
_BasicAlarmMasterInputFaultSeverity_Object = MibTableColumn
basicAlarmMasterInputFaultSeverity = _BasicAlarmMasterInputFaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 9),
    _BasicAlarmMasterInputFaultSeverity_Type()
)
basicAlarmMasterInputFaultSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputFaultSeverity.setStatus("mandatory")


class _BasicAlarmMasterInputFaultState_Type(Integer32):
    """Custom type basicAlarmMasterInputFaultState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_BasicAlarmMasterInputFaultState_Type.__name__ = "Integer32"
_BasicAlarmMasterInputFaultState_Object = MibTableColumn
basicAlarmMasterInputFaultState = _BasicAlarmMasterInputFaultState_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 10),
    _BasicAlarmMasterInputFaultState_Type()
)
basicAlarmMasterInputFaultState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputFaultState.setStatus("mandatory")


class _BasicAlarmMasterInputStatus_Type(Integer32):
    """Custom type basicAlarmMasterInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_BasicAlarmMasterInputStatus_Type.__name__ = "Integer32"
_BasicAlarmMasterInputStatus_Object = MibTableColumn
basicAlarmMasterInputStatus = _BasicAlarmMasterInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 11),
    _BasicAlarmMasterInputStatus_Type()
)
basicAlarmMasterInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicAlarmMasterInputStatus.setStatus("mandatory")


class _BasicAlarmMasterInputValue_Type(Integer32):
    """Custom type basicAlarmMasterInputValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_BasicAlarmMasterInputValue_Type.__name__ = "Integer32"
_BasicAlarmMasterInputValue_Object = MibTableColumn
basicAlarmMasterInputValue = _BasicAlarmMasterInputValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 12),
    _BasicAlarmMasterInputValue_Type()
)
basicAlarmMasterInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicAlarmMasterInputValue.setStatus("mandatory")


class _BasicAlarmMasterDisplay_Type(Integer32):
    """Custom type basicAlarmMasterDisplay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicAlarmMasterDisplay_Type.__name__ = "Integer32"
_BasicAlarmMasterDisplay_Object = MibTableColumn
basicAlarmMasterDisplay = _BasicAlarmMasterDisplay_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 13),
    _BasicAlarmMasterDisplay_Type()
)
basicAlarmMasterDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterDisplay.setStatus("mandatory")


class _BasicAlarmMasterInputZone_Type(DisplayString):
    """Custom type basicAlarmMasterInputZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicAlarmMasterInputZone_Type.__name__ = "DisplayString"
_BasicAlarmMasterInputZone_Object = MibTableColumn
basicAlarmMasterInputZone = _BasicAlarmMasterInputZone_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 14),
    _BasicAlarmMasterInputZone_Type()
)
basicAlarmMasterInputZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputZone.setStatus("mandatory")


class _BasicAlarmMasterInputRelatedEquipment_Type(DisplayString):
    """Custom type basicAlarmMasterInputRelatedEquipment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicAlarmMasterInputRelatedEquipment_Type.__name__ = "DisplayString"
_BasicAlarmMasterInputRelatedEquipment_Object = MibTableColumn
basicAlarmMasterInputRelatedEquipment = _BasicAlarmMasterInputRelatedEquipment_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 15),
    _BasicAlarmMasterInputRelatedEquipment_Type()
)
basicAlarmMasterInputRelatedEquipment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputRelatedEquipment.setStatus("mandatory")


class _BasicAlarmMasterInputSiteId_Type(DisplayString):
    """Custom type basicAlarmMasterInputSiteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicAlarmMasterInputSiteId_Type.__name__ = "DisplayString"
_BasicAlarmMasterInputSiteId_Object = MibTableColumn
basicAlarmMasterInputSiteId = _BasicAlarmMasterInputSiteId_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 16),
    _BasicAlarmMasterInputSiteId_Type()
)
basicAlarmMasterInputSiteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputSiteId.setStatus("mandatory")


class _BasicAlarmMasterInputManufacturer_Type(DisplayString):
    """Custom type basicAlarmMasterInputManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicAlarmMasterInputManufacturer_Type.__name__ = "DisplayString"
_BasicAlarmMasterInputManufacturer_Object = MibTableColumn
basicAlarmMasterInputManufacturer = _BasicAlarmMasterInputManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 17),
    _BasicAlarmMasterInputManufacturer_Type()
)
basicAlarmMasterInputManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputManufacturer.setStatus("mandatory")


class _BasicAlarmMasterInputModel_Type(DisplayString):
    """Custom type basicAlarmMasterInputModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicAlarmMasterInputModel_Type.__name__ = "DisplayString"
_BasicAlarmMasterInputModel_Object = MibTableColumn
basicAlarmMasterInputModel = _BasicAlarmMasterInputModel_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 36, 1, 18),
    _BasicAlarmMasterInputModel_Type()
)
basicAlarmMasterInputModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAlarmMasterInputModel.setStatus("mandatory")
_BasicPowerMasterOutletTable_Object = MibTable
basicPowerMasterOutletTable = _BasicPowerMasterOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 37)
)
if mibBuilder.loadTexts:
    basicPowerMasterOutletTable.setStatus("mandatory")
_BasicPowerMasterOutletEntry_Object = MibTableRow
basicPowerMasterOutletEntry = _BasicPowerMasterOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 37, 1)
)
basicPowerMasterOutletEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicPowerMasterPortIndex"),
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicPowerMasterOutletIndex"),
)
if mibBuilder.loadTexts:
    basicPowerMasterOutletEntry.setStatus("mandatory")
_BasicPowerMasterPortIndex_Type = Integer32
_BasicPowerMasterPortIndex_Object = MibTableColumn
basicPowerMasterPortIndex = _BasicPowerMasterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 37, 1, 1),
    _BasicPowerMasterPortIndex_Type()
)
basicPowerMasterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPowerMasterPortIndex.setStatus("mandatory")
_BasicPowerMasterOutletIndex_Type = Integer32
_BasicPowerMasterOutletIndex_Object = MibTableColumn
basicPowerMasterOutletIndex = _BasicPowerMasterOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 37, 1, 2),
    _BasicPowerMasterOutletIndex_Type()
)
basicPowerMasterOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPowerMasterOutletIndex.setStatus("mandatory")


class _BasicPowerMasterOutletName_Type(DisplayString):
    """Custom type basicPowerMasterOutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicPowerMasterOutletName_Type.__name__ = "DisplayString"
_BasicPowerMasterOutletName_Object = MibTableColumn
basicPowerMasterOutletName = _BasicPowerMasterOutletName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 37, 1, 3),
    _BasicPowerMasterOutletName_Type()
)
basicPowerMasterOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPowerMasterOutletName.setStatus("mandatory")


class _BasicPowerMasterOutletState_Type(Integer32):
    """Custom type basicPowerMasterOutletState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BasicPowerMasterOutletState_Type.__name__ = "Integer32"
_BasicPowerMasterOutletState_Object = MibTableColumn
basicPowerMasterOutletState = _BasicPowerMasterOutletState_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 37, 1, 4),
    _BasicPowerMasterOutletState_Type()
)
basicPowerMasterOutletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPowerMasterOutletState.setStatus("mandatory")


class _BasicPowerMasterOutletAmperageStatus_Type(DisplayString):
    """Custom type basicPowerMasterOutletAmperageStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BasicPowerMasterOutletAmperageStatus_Type.__name__ = "DisplayString"
_BasicPowerMasterOutletAmperageStatus_Object = MibTableColumn
basicPowerMasterOutletAmperageStatus = _BasicPowerMasterOutletAmperageStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 37, 1, 5),
    _BasicPowerMasterOutletAmperageStatus_Type()
)
basicPowerMasterOutletAmperageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPowerMasterOutletAmperageStatus.setStatus("mandatory")
_BasicControlOutputRelayTable_Object = MibTable
basicControlOutputRelayTable = _BasicControlOutputRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 38)
)
if mibBuilder.loadTexts:
    basicControlOutputRelayTable.setStatus("mandatory")
_BasicControlOutputRelayEntry_Object = MibTableRow
basicControlOutputRelayEntry = _BasicControlOutputRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 38, 1)
)
basicControlOutputRelayEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "basicControlOutputRelayIndex"),
)
if mibBuilder.loadTexts:
    basicControlOutputRelayEntry.setStatus("mandatory")
_BasicControlOutputRelayIndex_Type = Integer32
_BasicControlOutputRelayIndex_Object = MibTableColumn
basicControlOutputRelayIndex = _BasicControlOutputRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 38, 1, 1),
    _BasicControlOutputRelayIndex_Type()
)
basicControlOutputRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicControlOutputRelayIndex.setStatus("mandatory")


class _BasicControlOutputRelayName_Type(DisplayString):
    """Custom type basicControlOutputRelayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicControlOutputRelayName_Type.__name__ = "DisplayString"
_BasicControlOutputRelayName_Object = MibTableColumn
basicControlOutputRelayName = _BasicControlOutputRelayName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 38, 1, 2),
    _BasicControlOutputRelayName_Type()
)
basicControlOutputRelayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicControlOutputRelayName.setStatus("mandatory")


class _BasicControlOutputRelayState_Type(Integer32):
    """Custom type basicControlOutputRelayState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_BasicControlOutputRelayState_Type.__name__ = "Integer32"
_BasicControlOutputRelayState_Object = MibTableColumn
basicControlOutputRelayState = _BasicControlOutputRelayState_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 38, 1, 3),
    _BasicControlOutputRelayState_Type()
)
basicControlOutputRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicControlOutputRelayState.setStatus("mandatory")


class _BasicControlOutputRelayStatus_Type(Integer32):
    """Custom type basicControlOutputRelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_BasicControlOutputRelayStatus_Type.__name__ = "Integer32"
_BasicControlOutputRelayStatus_Object = MibTableColumn
basicControlOutputRelayStatus = _BasicControlOutputRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 38, 1, 4),
    _BasicControlOutputRelayStatus_Type()
)
basicControlOutputRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicControlOutputRelayStatus.setStatus("mandatory")


class _BasicAutoProtocolDetectMessage_Type(DisplayString):
    """Custom type basicAutoProtocolDetectMessage based on DisplayString"""
    defaultValue = OctetString("AutoProtocolDetect - Begin protocol or enter 4 returns for interactive mode.")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BasicAutoProtocolDetectMessage_Type.__name__ = "DisplayString"
_BasicAutoProtocolDetectMessage_Object = MibScalar
basicAutoProtocolDetectMessage = _BasicAutoProtocolDetectMessage_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 100),
    _BasicAutoProtocolDetectMessage_Type()
)
basicAutoProtocolDetectMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicAutoProtocolDetectMessage.setStatus("mandatory")
_XQueue_ObjectIdentity = ObjectIdentity
xQueue = _XQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 2)
)


class _QueueLimit_Type(Integer32):
    """Custom type queueLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_QueueLimit_Type.__name__ = "Integer32"
_QueueLimit_Object = MibScalar
queueLimit = _QueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 1),
    _QueueLimit_Type()
)
queueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueLimit.setStatus("mandatory")
_QueueHigh_Type = Gauge32
_QueueHigh_Object = MibScalar
queueHigh = _QueueHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 2),
    _QueueHigh_Type()
)
queueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueHigh.setStatus("mandatory")
_QueueNumber_Type = Gauge32
_QueueNumber_Object = MibScalar
queueNumber = _QueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 3),
    _QueueNumber_Type()
)
queueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueNumber.setStatus("mandatory")
_QueueTable_Object = MibTable
queueTable = _QueueTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4)
)
if mibBuilder.loadTexts:
    queueTable.setStatus("mandatory")
_QueueEntry_Object = MibTableRow
queueEntry = _QueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1)
)
queueEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "queueJob"),
)
if mibBuilder.loadTexts:
    queueEntry.setStatus("mandatory")
_QueueJob_Type = Integer32
_QueueJob_Object = MibTableColumn
queueJob = _QueueJob_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 1),
    _QueueJob_Type()
)
queueJob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueJob.setStatus("mandatory")


class _QueueStatus_Type(Integer32):
    """Custom type queueStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_QueueStatus_Type.__name__ = "Integer32"
_QueueStatus_Object = MibTableColumn
queueStatus = _QueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 2),
    _QueueStatus_Type()
)
queueStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueStatus.setStatus("mandatory")


class _QueueSourceName_Type(DisplayString):
    """Custom type queueSourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_QueueSourceName_Type.__name__ = "DisplayString"
_QueueSourceName_Object = MibTableColumn
queueSourceName = _QueueSourceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 3),
    _QueueSourceName_Type()
)
queueSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueSourceName.setStatus("mandatory")


class _QueueServiceName_Type(DisplayString):
    """Custom type queueServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_QueueServiceName_Type.__name__ = "DisplayString"
_QueueServiceName_Object = MibTableColumn
queueServiceName = _QueueServiceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 4),
    _QueueServiceName_Type()
)
queueServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueServiceName.setStatus("mandatory")
_QueueServicePortIndex_Type = Integer32
_QueueServicePortIndex_Object = MibTableColumn
queueServicePortIndex = _QueueServicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 5),
    _QueueServicePortIndex_Type()
)
queueServicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueServicePortIndex.setStatus("mandatory")


class _QueueServicePortName_Type(DisplayString):
    """Custom type queueServicePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_QueueServicePortName_Type.__name__ = "DisplayString"
_QueueServicePortName_Object = MibTableColumn
queueServicePortName = _QueueServicePortName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 6),
    _QueueServicePortName_Type()
)
queueServicePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueServicePortName.setStatus("mandatory")
_QueuePortTable_Object = MibTable
queuePortTable = _QueuePortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 5)
)
if mibBuilder.loadTexts:
    queuePortTable.setStatus("mandatory")
_QueuePortEntry_Object = MibTableRow
queuePortEntry = _QueuePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 5, 1)
)
queuePortEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "queuePortIndex"),
)
if mibBuilder.loadTexts:
    queuePortEntry.setStatus("mandatory")
_QueuePortIndex_Type = Integer32
_QueuePortIndex_Object = MibTableColumn
queuePortIndex = _QueuePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 5, 1, 1),
    _QueuePortIndex_Type()
)
queuePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuePortIndex.setStatus("mandatory")


class _QueuePortQueuing_Type(Integer32):
    """Custom type queuePortQueuing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QueuePortQueuing_Type.__name__ = "Integer32"
_QueuePortQueuing_Object = MibTableColumn
queuePortQueuing = _QueuePortQueuing_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 5, 1, 2),
    _QueuePortQueuing_Type()
)
queuePortQueuing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuePortQueuing.setStatus("mandatory")
_XMenu_ObjectIdentity = ObjectIdentity
xMenu = _XMenu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 3)
)
_MenuNumber_Type = Gauge32
_MenuNumber_Object = MibScalar
menuNumber = _MenuNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 1),
    _MenuNumber_Type()
)
menuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    menuNumber.setStatus("mandatory")


class _MenuContinuePrompt_Type(DisplayString):
    """Custom type menuContinuePrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MenuContinuePrompt_Type.__name__ = "DisplayString"
_MenuContinuePrompt_Object = MibScalar
menuContinuePrompt = _MenuContinuePrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 2),
    _MenuContinuePrompt_Type()
)
menuContinuePrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuContinuePrompt.setStatus("mandatory")


class _MenuSelectionPrompt_Type(DisplayString):
    """Custom type menuSelectionPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MenuSelectionPrompt_Type.__name__ = "DisplayString"
_MenuSelectionPrompt_Object = MibScalar
menuSelectionPrompt = _MenuSelectionPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 3),
    _MenuSelectionPrompt_Type()
)
menuSelectionPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuSelectionPrompt.setStatus("mandatory")
_MenuTable_Object = MibTable
menuTable = _MenuTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4)
)
if mibBuilder.loadTexts:
    menuTable.setStatus("mandatory")
_MenuEntry_Object = MibTableRow
menuEntry = _MenuEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4, 1)
)
menuEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "menuIndex"),
)
if mibBuilder.loadTexts:
    menuEntry.setStatus("mandatory")
_MenuIndex_Type = Integer32
_MenuIndex_Object = MibTableColumn
menuIndex = _MenuIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4, 1, 1),
    _MenuIndex_Type()
)
menuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    menuIndex.setStatus("mandatory")


class _MenuStatus_Type(Integer32):
    """Custom type menuStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_MenuStatus_Type.__name__ = "Integer32"
_MenuStatus_Object = MibTableColumn
menuStatus = _MenuStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4, 1, 2),
    _MenuStatus_Type()
)
menuStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuStatus.setStatus("mandatory")


class _MenuText_Type(DisplayString):
    """Custom type menuText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MenuText_Type.__name__ = "DisplayString"
_MenuText_Object = MibTableColumn
menuText = _MenuText_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4, 1, 3),
    _MenuText_Type()
)
menuText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText.setStatus("mandatory")


class _MenuCommand_Type(DisplayString):
    """Custom type menuCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MenuCommand_Type.__name__ = "DisplayString"
_MenuCommand_Object = MibTableColumn
menuCommand = _MenuCommand_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4, 1, 4),
    _MenuCommand_Type()
)
menuCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand.setStatus("mandatory")
_MenuPortTable_Object = MibTable
menuPortTable = _MenuPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5)
)
if mibBuilder.loadTexts:
    menuPortTable.setStatus("mandatory")
_MenuPortEntry_Object = MibTableRow
menuPortEntry = _MenuPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5, 1)
)
menuPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "menuPortIndex"),
)
if mibBuilder.loadTexts:
    menuPortEntry.setStatus("mandatory")
_MenuPortIndex_Type = Integer32
_MenuPortIndex_Object = MibTableColumn
menuPortIndex = _MenuPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5, 1, 1),
    _MenuPortIndex_Type()
)
menuPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    menuPortIndex.setStatus("mandatory")


class _MenuPortMenuStatus_Type(Integer32):
    """Custom type menuPortMenuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("privileged", 3))
    )


_MenuPortMenuStatus_Type.__name__ = "Integer32"
_MenuPortMenuStatus_Object = MibTableColumn
menuPortMenuStatus = _MenuPortMenuStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5, 1, 2),
    _MenuPortMenuStatus_Type()
)
menuPortMenuStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuPortMenuStatus.setStatus("mandatory")


class _MenuPortNestedMenuStatus_Type(Integer32):
    """Custom type menuPortNestedMenuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("required", 3))
    )


_MenuPortNestedMenuStatus_Type.__name__ = "Integer32"
_MenuPortNestedMenuStatus_Object = MibTableColumn
menuPortNestedMenuStatus = _MenuPortNestedMenuStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5, 1, 3),
    _MenuPortNestedMenuStatus_Type()
)
menuPortNestedMenuStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuPortNestedMenuStatus.setStatus("mandatory")


class _MenuPortNestedMenuPrivilege_Type(Integer32):
    """Custom type menuPortNestedMenuPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MenuPortNestedMenuPrivilege_Type.__name__ = "Integer32"
_MenuPortNestedMenuPrivilege_Object = MibTableColumn
menuPortNestedMenuPrivilege = _MenuPortNestedMenuPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5, 1, 4),
    _MenuPortNestedMenuPrivilege_Type()
)
menuPortNestedMenuPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuPortNestedMenuPrivilege.setStatus("mandatory")


class _MenuPortNestedTopLevel_Type(Integer32):
    """Custom type menuPortNestedTopLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MenuPortNestedTopLevel_Type.__name__ = "Integer32"
_MenuPortNestedTopLevel_Object = MibTableColumn
menuPortNestedTopLevel = _MenuPortNestedTopLevel_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5, 1, 5),
    _MenuPortNestedTopLevel_Type()
)
menuPortNestedTopLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuPortNestedTopLevel.setStatus("mandatory")


class _MenuNestedName_Type(DisplayString):
    """Custom type menuNestedName based on DisplayString"""
    defaultValue = OctetString("NESTMENU.TXT")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MenuNestedName_Type.__name__ = "DisplayString"
_MenuNestedName_Object = MibScalar
menuNestedName = _MenuNestedName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 6),
    _MenuNestedName_Type()
)
menuNestedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuNestedName.setStatus("mandatory")


class _MenuNestedScriptMaximum_Type(Integer32):
    """Custom type menuNestedScriptMaximum based on Integer32"""
    defaultValue = 16384

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 204800),
    )


_MenuNestedScriptMaximum_Type.__name__ = "Integer32"
_MenuNestedScriptMaximum_Object = MibScalar
menuNestedScriptMaximum = _MenuNestedScriptMaximum_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 7),
    _MenuNestedScriptMaximum_Type()
)
menuNestedScriptMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuNestedScriptMaximum.setStatus("mandatory")


class _MenuNestedSystemName_Type(Integer32):
    """Custom type menuNestedSystemName based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MenuNestedSystemName_Type.__name__ = "Integer32"
_MenuNestedSystemName_Object = MibScalar
menuNestedSystemName = _MenuNestedSystemName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 8),
    _MenuNestedSystemName_Type()
)
menuNestedSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuNestedSystemName.setStatus("mandatory")


class _MenuNestedEthernet_Type(Integer32):
    """Custom type menuNestedEthernet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MenuNestedEthernet_Type.__name__ = "Integer32"
_MenuNestedEthernet_Object = MibScalar
menuNestedEthernet = _MenuNestedEthernet_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 9),
    _MenuNestedEthernet_Type()
)
menuNestedEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuNestedEthernet.setStatus("mandatory")
_XNetLogin_ObjectIdentity = ObjectIdentity
xNetLogin = _XNetLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 4)
)
_NetLoginNumber_Type = Integer32
_NetLoginNumber_Object = MibScalar
netLoginNumber = _NetLoginNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 1),
    _NetLoginNumber_Type()
)
netLoginNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginNumber.setStatus("mandatory")
_NetLoginServerTable_Object = MibTable
netLoginServerTable = _NetLoginServerTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2)
)
if mibBuilder.loadTexts:
    netLoginServerTable.setStatus("mandatory")
_NetLoginServerEntry_Object = MibTableRow
netLoginServerEntry = _NetLoginServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2, 1)
)
netLoginServerEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "netLoginServerName"),
)
if mibBuilder.loadTexts:
    netLoginServerEntry.setStatus("mandatory")


class _NetLoginServerName_Type(DisplayString):
    """Custom type netLoginServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_NetLoginServerName_Type.__name__ = "DisplayString"
_NetLoginServerName_Object = MibTableColumn
netLoginServerName = _NetLoginServerName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2, 1, 1),
    _NetLoginServerName_Type()
)
netLoginServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginServerName.setStatus("mandatory")


class _NetLoginServerStatus_Type(Integer32):
    """Custom type netLoginServerStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_NetLoginServerStatus_Type.__name__ = "Integer32"
_NetLoginServerStatus_Object = MibTableColumn
netLoginServerStatus = _NetLoginServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2, 1, 2),
    _NetLoginServerStatus_Type()
)
netLoginServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginServerStatus.setStatus("mandatory")


class _NetLoginServerPath_Type(DisplayString):
    """Custom type netLoginServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_NetLoginServerPath_Type.__name__ = "DisplayString"
_NetLoginServerPath_Object = MibTableColumn
netLoginServerPath = _NetLoginServerPath_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2, 1, 3),
    _NetLoginServerPath_Type()
)
netLoginServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginServerPath.setStatus("mandatory")


class _NetLoginServerSeparator_Type(DisplayString):
    """Custom type netLoginServerSeparator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_NetLoginServerSeparator_Type.__name__ = "DisplayString"
_NetLoginServerSeparator_Object = MibTableColumn
netLoginServerSeparator = _NetLoginServerSeparator_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2, 1, 4),
    _NetLoginServerSeparator_Type()
)
netLoginServerSeparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginServerSeparator.setStatus("mandatory")
_NetLoginPortTable_Object = MibTable
netLoginPortTable = _NetLoginPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3)
)
if mibBuilder.loadTexts:
    netLoginPortTable.setStatus("mandatory")
_NetLoginPortEntry_Object = MibTableRow
netLoginPortEntry = _NetLoginPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1)
)
netLoginPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "netLoginPortIndex"),
)
if mibBuilder.loadTexts:
    netLoginPortEntry.setStatus("mandatory")
_NetLoginPortIndex_Type = Integer32
_NetLoginPortIndex_Object = MibTableColumn
netLoginPortIndex = _NetLoginPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 1),
    _NetLoginPortIndex_Type()
)
netLoginPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginPortIndex.setStatus("mandatory")


class _NetLoginPortScriptUse_Type(Integer32):
    """Custom type netLoginPortScriptUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("required", 3))
    )


_NetLoginPortScriptUse_Type.__name__ = "Integer32"
_NetLoginPortScriptUse_Object = MibTableColumn
netLoginPortScriptUse = _NetLoginPortScriptUse_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 2),
    _NetLoginPortScriptUse_Type()
)
netLoginPortScriptUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginPortScriptUse.setStatus("mandatory")


class _NetLoginPortScriptEcho_Type(Integer32):
    """Custom type netLoginPortScriptEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NetLoginPortScriptEcho_Type.__name__ = "Integer32"
_NetLoginPortScriptEcho_Object = MibTableColumn
netLoginPortScriptEcho = _NetLoginPortScriptEcho_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 3),
    _NetLoginPortScriptEcho_Type()
)
netLoginPortScriptEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginPortScriptEcho.setStatus("mandatory")
_NetLoginPortLoaderAddressType_Type = AddressType
_NetLoginPortLoaderAddressType_Object = MibTableColumn
netLoginPortLoaderAddressType = _NetLoginPortLoaderAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 4),
    _NetLoginPortLoaderAddressType_Type()
)
netLoginPortLoaderAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginPortLoaderAddressType.setStatus("mandatory")
_NetLoginPortLoaderAddress_Type = OctetString
_NetLoginPortLoaderAddress_Object = MibTableColumn
netLoginPortLoaderAddress = _NetLoginPortLoaderAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 5),
    _NetLoginPortLoaderAddress_Type()
)
netLoginPortLoaderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginPortLoaderAddress.setStatus("mandatory")
_NetLoginPortLoaderFile_Type = DisplayString
_NetLoginPortLoaderFile_Object = MibTableColumn
netLoginPortLoaderFile = _NetLoginPortLoaderFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 6),
    _NetLoginPortLoaderFile_Type()
)
netLoginPortLoaderFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginPortLoaderFile.setStatus("mandatory")


class _NetLoginPortExecuteFile_Type(DisplayString):
    """Custom type netLoginPortExecuteFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_NetLoginPortExecuteFile_Type.__name__ = "DisplayString"
_NetLoginPortExecuteFile_Object = MibTableColumn
netLoginPortExecuteFile = _NetLoginPortExecuteFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 7),
    _NetLoginPortExecuteFile_Type()
)
netLoginPortExecuteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginPortExecuteFile.setStatus("mandatory")
_XDial_ObjectIdentity = ObjectIdentity
xDial = _XDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 5)
)
_DialPortTable_Object = MibTable
dialPortTable = _DialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1)
)
if mibBuilder.loadTexts:
    dialPortTable.setStatus("mandatory")
_DialPortEntry_Object = MibTableRow
dialPortEntry = _DialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1, 1)
)
dialPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "dialPortIndex"),
)
if mibBuilder.loadTexts:
    dialPortEntry.setStatus("mandatory")
_DialPortIndex_Type = Integer32
_DialPortIndex_Object = MibTableColumn
dialPortIndex = _DialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1, 1, 1),
    _DialPortIndex_Type()
)
dialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialPortIndex.setStatus("mandatory")


class _DialPortDialback_Type(Integer32):
    """Custom type dialPortDialback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DialPortDialback_Type.__name__ = "Integer32"
_DialPortDialback_Object = MibTableColumn
dialPortDialback = _DialPortDialback_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1, 1, 2),
    _DialPortDialback_Type()
)
dialPortDialback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPortDialback.setStatus("mandatory")


class _DialPortDialbackTimeout_Type(Integer32):
    """Custom type dialPortDialbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_DialPortDialbackTimeout_Type.__name__ = "Integer32"
_DialPortDialbackTimeout_Object = MibTableColumn
dialPortDialbackTimeout = _DialPortDialbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1, 1, 3),
    _DialPortDialbackTimeout_Type()
)
dialPortDialbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPortDialbackTimeout.setStatus("mandatory")


class _DialPortDialout_Type(Integer32):
    """Custom type dialPortDialout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ppp", 4),
          ("query", 2),
          ("slip", 3))
    )


_DialPortDialout_Type.__name__ = "Integer32"
_DialPortDialout_Object = MibTableColumn
dialPortDialout = _DialPortDialout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1, 1, 4),
    _DialPortDialout_Type()
)
dialPortDialout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPortDialout.setStatus("mandatory")


class _DialPortDialbackNoUsername_Type(Integer32):
    """Custom type dialPortDialbackNoUsername based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DialPortDialbackNoUsername_Type.__name__ = "Integer32"
_DialPortDialbackNoUsername_Object = MibTableColumn
dialPortDialbackNoUsername = _DialPortDialbackNoUsername_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1, 1, 5),
    _DialPortDialbackNoUsername_Type()
)
dialPortDialbackNoUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPortDialbackNoUsername.setStatus("mandatory")
_XSessionLog_ObjectIdentity = ObjectIdentity
xSessionLog = _XSessionLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 6)
)


class _SessionLogLimit_Type(Integer32):
    """Custom type sessionLogLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SessionLogLimit_Type.__name__ = "Integer32"
_SessionLogLimit_Object = MibScalar
sessionLogLimit = _SessionLogLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 1),
    _SessionLogLimit_Type()
)
sessionLogLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogLimit.setStatus("mandatory")
_SessionLogTable_Object = MibTable
sessionLogTable = _SessionLogTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2)
)
if mibBuilder.loadTexts:
    sessionLogTable.setStatus("mandatory")
_SessionLogEntry_Object = MibTableRow
sessionLogEntry = _SessionLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1)
)
sessionLogEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "sessionLogIndex"),
)
if mibBuilder.loadTexts:
    sessionLogEntry.setStatus("mandatory")
_SessionLogIndex_Type = Integer32
_SessionLogIndex_Object = MibTableColumn
sessionLogIndex = _SessionLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 1),
    _SessionLogIndex_Type()
)
sessionLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogIndex.setStatus("mandatory")


class _SessionLogConnectionID_Type(Integer32):
    """Custom type sessionLogConnectionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SessionLogConnectionID_Type.__name__ = "Integer32"
_SessionLogConnectionID_Object = MibTableColumn
sessionLogConnectionID = _SessionLogConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 2),
    _SessionLogConnectionID_Type()
)
sessionLogConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogConnectionID.setStatus("mandatory")
_SessionLogPort_Type = Integer32
_SessionLogPort_Object = MibTableColumn
sessionLogPort = _SessionLogPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 3),
    _SessionLogPort_Type()
)
sessionLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogPort.setStatus("mandatory")


class _SessionLogEvent_Type(Integer32):
    """Custom type sessionLogEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("connectLocal", 2),
          ("connectRemote", 3),
          ("disconnect", 4),
          ("login", 1),
          ("processDefined", 15),
          ("rCPConnect", 5),
          ("rCPDisconnect", 6),
          ("x25Connect", 13),
          ("x25Disconnect", 14))
    )


_SessionLogEvent_Type.__name__ = "Integer32"
_SessionLogEvent_Object = MibTableColumn
sessionLogEvent = _SessionLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 4),
    _SessionLogEvent_Type()
)
sessionLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogEvent.setStatus("mandatory")


class _SessionLogEventDetail_Type(Integer32):
    """Custom type sessionLogEventDetail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 28),
          ("badCircuitTimer", 15),
          ("badMessageOrSlot", 17),
          ("badPassword", 22),
          ("badServiceClass", 16),
          ("domainTooLong", 32),
          ("duplicateQueueID", 6),
          ("internetConnectDisabled", 36),
          ("noImmeditatAccess", 27),
          ("noNodeResources", 12),
          ("noProgress", 19),
          ("noServiceResourced", 8),
          ("noSuchNode", 33),
          ("noSuchPort", 21),
          ("noSuchService", 24),
          ("noSuchServiceOnNode", 34),
          ("noUsers", 7),
          ("nodeUserdisconnect", 14),
          ("none", 1),
          ("notInQueue", 26),
          ("protocolBadCircuit", 2),
          ("protocolBadCredits", 3),
          ("protocolBadRange", 5),
          ("protocolBadReasonCode", 30),
          ("protocolBadSolicit", 29),
          ("protocolBadStartOrRun", 4),
          ("rejectService", 35),
          ("serverUserDisconnect", 11),
          ("serviceBusy", 23),
          ("serviceDisabled", 25),
          ("serviceNotOnPort", 20),
          ("serviceUnavailable", 10),
          ("serviceUserDisconnect", 9),
          ("systemShutdown", 13),
          ("timeout", 18),
          ("unsupportedTest", 31))
    )


_SessionLogEventDetail_Type.__name__ = "Integer32"
_SessionLogEventDetail_Object = MibTableColumn
sessionLogEventDetail = _SessionLogEventDetail_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 5),
    _SessionLogEventDetail_Type()
)
sessionLogEventDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogEventDetail.setStatus("mandatory")


class _SessionLogUserName_Type(DisplayString):
    """Custom type sessionLogUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SessionLogUserName_Type.__name__ = "DisplayString"
_SessionLogUserName_Object = MibTableColumn
sessionLogUserName = _SessionLogUserName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 6),
    _SessionLogUserName_Type()
)
sessionLogUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogUserName.setStatus("mandatory")


class _SessionLogRemoteName_Type(DisplayString):
    """Custom type sessionLogRemoteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionLogRemoteName_Type.__name__ = "DisplayString"
_SessionLogRemoteName_Object = MibTableColumn
sessionLogRemoteName = _SessionLogRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 7),
    _SessionLogRemoteName_Type()
)
sessionLogRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogRemoteName.setStatus("mandatory")
_SessionLogConnectTime_Type = DateTime
_SessionLogConnectTime_Object = MibTableColumn
sessionLogConnectTime = _SessionLogConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 8),
    _SessionLogConnectTime_Type()
)
sessionLogConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogConnectTime.setStatus("mandatory")
_SessionLogDisconnectTime_Type = DateTime
_SessionLogDisconnectTime_Object = MibTableColumn
sessionLogDisconnectTime = _SessionLogDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 9),
    _SessionLogDisconnectTime_Type()
)
sessionLogDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogDisconnectTime.setStatus("mandatory")
_SessionLogInCharacters_Type = Counter32
_SessionLogInCharacters_Object = MibTableColumn
sessionLogInCharacters = _SessionLogInCharacters_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 10),
    _SessionLogInCharacters_Type()
)
sessionLogInCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogInCharacters.setStatus("mandatory")
_SessionLogOutCharacters_Type = Counter32
_SessionLogOutCharacters_Object = MibTableColumn
sessionLogOutCharacters = _SessionLogOutCharacters_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 11),
    _SessionLogOutCharacters_Type()
)
sessionLogOutCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogOutCharacters.setStatus("mandatory")


class _SessionLogVerboseEvent_Type(Integer32):
    """Custom type sessionLogVerboseEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("connectLocal", 2),
          ("connectRcp", 5),
          ("connectRemote", 3),
          ("connectX25", 13),
          ("disconnect", 4),
          ("disconnectRcp", 6),
          ("disconnectX25", 14),
          ("login", 1),
          ("lpd", 12),
          ("telnetMaint", 7),
          ("userDefined", 15),
          ("xprinter", 9),
          ("xremote", 8))
    )


_SessionLogVerboseEvent_Type.__name__ = "Integer32"
_SessionLogVerboseEvent_Object = MibTableColumn
sessionLogVerboseEvent = _SessionLogVerboseEvent_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 12),
    _SessionLogVerboseEvent_Type()
)
sessionLogVerboseEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogVerboseEvent.setStatus("mandatory")


class _SessionLogX25Direction_Type(Integer32):
    """Custom type sessionLogX25Direction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_SessionLogX25Direction_Type.__name__ = "Integer32"
_SessionLogX25Direction_Object = MibTableColumn
sessionLogX25Direction = _SessionLogX25Direction_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 13),
    _SessionLogX25Direction_Type()
)
sessionLogX25Direction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogX25Direction.setStatus("mandatory")
_SessionLogVerboseMessage_Type = DisplayString
_SessionLogVerboseMessage_Object = MibTableColumn
sessionLogVerboseMessage = _SessionLogVerboseMessage_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 14),
    _SessionLogVerboseMessage_Type()
)
sessionLogVerboseMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogVerboseMessage.setStatus("mandatory")


class _SessionLogX25CallerAddress_Type(OctetString):
    """Custom type sessionLogX25CallerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SessionLogX25CallerAddress_Type.__name__ = "OctetString"
_SessionLogX25CallerAddress_Object = MibTableColumn
sessionLogX25CallerAddress = _SessionLogX25CallerAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 15),
    _SessionLogX25CallerAddress_Type()
)
sessionLogX25CallerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogX25CallerAddress.setStatus("mandatory")


class _SessionLogX25CalledAddress_Type(OctetString):
    """Custom type sessionLogX25CalledAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SessionLogX25CalledAddress_Type.__name__ = "OctetString"
_SessionLogX25CalledAddress_Object = MibTableColumn
sessionLogX25CalledAddress = _SessionLogX25CalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 16),
    _SessionLogX25CalledAddress_Type()
)
sessionLogX25CalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogX25CalledAddress.setStatus("mandatory")
_SessionLogX25DisconnectCause_Type = Integer32
_SessionLogX25DisconnectCause_Object = MibTableColumn
sessionLogX25DisconnectCause = _SessionLogX25DisconnectCause_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 17),
    _SessionLogX25DisconnectCause_Type()
)
sessionLogX25DisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogX25DisconnectCause.setStatus("mandatory")
_SessionLogX25DisconnectDiagnostic_Type = Integer32
_SessionLogX25DisconnectDiagnostic_Object = MibTableColumn
sessionLogX25DisconnectDiagnostic = _SessionLogX25DisconnectDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 18),
    _SessionLogX25DisconnectDiagnostic_Type()
)
sessionLogX25DisconnectDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogX25DisconnectDiagnostic.setStatus("mandatory")


class _SessionLogHostType_Type(Integer32):
    """Custom type sessionLogHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unix", 2))
    )


_SessionLogHostType_Type.__name__ = "Integer32"
_SessionLogHostType_Object = MibScalar
sessionLogHostType = _SessionLogHostType_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 3),
    _SessionLogHostType_Type()
)
sessionLogHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogHostType.setStatus("mandatory")


class _SessionLogHostAddress_Type(OctetString):
    """Custom type sessionLogHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SessionLogHostAddress_Type.__name__ = "OctetString"
_SessionLogHostAddress_Object = MibScalar
sessionLogHostAddress = _SessionLogHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 4),
    _SessionLogHostAddress_Type()
)
sessionLogHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogHostAddress.setStatus("mandatory")


class _SessionLogVerbose_Type(Integer32):
    """Custom type sessionLogVerbose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SessionLogVerbose_Type.__name__ = "Integer32"
_SessionLogVerbose_Object = MibScalar
sessionLogVerbose = _SessionLogVerbose_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 5),
    _SessionLogVerbose_Type()
)
sessionLogVerbose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogVerbose.setStatus("mandatory")


class _SessionLogPriority_Type(Integer32):
    """Custom type sessionLogPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SessionLogPriority_Type.__name__ = "Integer32"
_SessionLogPriority_Object = MibScalar
sessionLogPriority = _SessionLogPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 6),
    _SessionLogPriority_Type()
)
sessionLogPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogPriority.setStatus("mandatory")


class _SessionLogEmpty_Type(Integer32):
    """Custom type sessionLogEmpty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SessionLogEmpty_Type.__name__ = "Integer32"
_SessionLogEmpty_Object = MibScalar
sessionLogEmpty = _SessionLogEmpty_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 7),
    _SessionLogEmpty_Type()
)
sessionLogEmpty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogEmpty.setStatus("mandatory")


class _SessionLogFacility_Type(Integer32):
    """Custom type sessionLogFacility based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8),
          ("user", 9))
    )


_SessionLogFacility_Type.__name__ = "Integer32"
_SessionLogFacility_Object = MibScalar
sessionLogFacility = _SessionLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 8),
    _SessionLogFacility_Type()
)
sessionLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogFacility.setStatus("mandatory")


class _SessionLogReliable_Type(Integer32):
    """Custom type sessionLogReliable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SessionLogReliable_Type.__name__ = "Integer32"
_SessionLogReliable_Object = MibScalar
sessionLogReliable = _SessionLogReliable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 9),
    _SessionLogReliable_Type()
)
sessionLogReliable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogReliable.setStatus("mandatory")


class _SessionLogHostSecondaryType_Type(Integer32):
    """Custom type sessionLogHostSecondaryType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unix", 2))
    )


_SessionLogHostSecondaryType_Type.__name__ = "Integer32"
_SessionLogHostSecondaryType_Object = MibScalar
sessionLogHostSecondaryType = _SessionLogHostSecondaryType_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 10),
    _SessionLogHostSecondaryType_Type()
)
sessionLogHostSecondaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogHostSecondaryType.setStatus("mandatory")


class _SessionLogHostSecondaryAddress_Type(OctetString):
    """Custom type sessionLogHostSecondaryAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SessionLogHostSecondaryAddress_Type.__name__ = "OctetString"
_SessionLogHostSecondaryAddress_Object = MibScalar
sessionLogHostSecondaryAddress = _SessionLogHostSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 11),
    _SessionLogHostSecondaryAddress_Type()
)
sessionLogHostSecondaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogHostSecondaryAddress.setStatus("mandatory")


class _SessionLogZeroAccountingAll_Type(Integer32):
    """Custom type sessionLogZeroAccountingAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SessionLogZeroAccountingAll_Type.__name__ = "Integer32"
_SessionLogZeroAccountingAll_Object = MibScalar
sessionLogZeroAccountingAll = _SessionLogZeroAccountingAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 12),
    _SessionLogZeroAccountingAll_Type()
)
sessionLogZeroAccountingAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogZeroAccountingAll.setStatus("mandatory")


class _SessionLogZeroCommandLogging_Type(Integer32):
    """Custom type sessionLogZeroCommandLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SessionLogZeroCommandLogging_Type.__name__ = "Integer32"
_SessionLogZeroCommandLogging_Object = MibScalar
sessionLogZeroCommandLogging = _SessionLogZeroCommandLogging_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 13),
    _SessionLogZeroCommandLogging_Type()
)
sessionLogZeroCommandLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogZeroCommandLogging.setStatus("mandatory")


class _SessionLogTl1AutonomousLogSize_Type(Integer32):
    """Custom type sessionLogTl1AutonomousLogSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SessionLogTl1AutonomousLogSize_Type.__name__ = "Integer32"
_SessionLogTl1AutonomousLogSize_Object = MibScalar
sessionLogTl1AutonomousLogSize = _SessionLogTl1AutonomousLogSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 14),
    _SessionLogTl1AutonomousLogSize_Type()
)
sessionLogTl1AutonomousLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogTl1AutonomousLogSize.setStatus("mandatory")


class _SessionLogTl1CommandLogSize_Type(Integer32):
    """Custom type sessionLogTl1CommandLogSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SessionLogTl1CommandLogSize_Type.__name__ = "Integer32"
_SessionLogTl1CommandLogSize_Object = MibScalar
sessionLogTl1CommandLogSize = _SessionLogTl1CommandLogSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 15),
    _SessionLogTl1CommandLogSize_Type()
)
sessionLogTl1CommandLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogTl1CommandLogSize.setStatus("mandatory")


class _SessionLogZeroDataLogging_Type(Integer32):
    """Custom type sessionLogZeroDataLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SessionLogZeroDataLogging_Type.__name__ = "Integer32"
_SessionLogZeroDataLogging_Object = MibScalar
sessionLogZeroDataLogging = _SessionLogZeroDataLogging_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 16),
    _SessionLogZeroDataLogging_Type()
)
sessionLogZeroDataLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogZeroDataLogging.setStatus("mandatory")


class _SessionLogZeroAlarmLogging_Type(Integer32):
    """Custom type sessionLogZeroAlarmLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SessionLogZeroAlarmLogging_Type.__name__ = "Integer32"
_SessionLogZeroAlarmLogging_Object = MibScalar
sessionLogZeroAlarmLogging = _SessionLogZeroAlarmLogging_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 17),
    _SessionLogZeroAlarmLogging_Type()
)
sessionLogZeroAlarmLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogZeroAlarmLogging.setStatus("mandatory")
_XCcl_ObjectIdentity = ObjectIdentity
xCcl = _XCcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 7)
)
_CclParsedScriptTable_Object = MibTable
cclParsedScriptTable = _CclParsedScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 7, 1)
)
if mibBuilder.loadTexts:
    cclParsedScriptTable.setStatus("mandatory")
_CclParsedScriptEntry_Object = MibTableRow
cclParsedScriptEntry = _CclParsedScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 7, 1, 1)
)
cclParsedScriptEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "cclScriptName"),
)
if mibBuilder.loadTexts:
    cclParsedScriptEntry.setStatus("mandatory")


class _CclScriptName_Type(DisplayString):
    """Custom type cclScriptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CclScriptName_Type.__name__ = "DisplayString"
_CclScriptName_Object = MibTableColumn
cclScriptName = _CclScriptName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 7, 1, 1, 1),
    _CclScriptName_Type()
)
cclScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cclScriptName.setStatus("mandatory")


class _CclScriptControl_Type(Integer32):
    """Custom type cclScriptControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("refresh", 1))
    )


_CclScriptControl_Type.__name__ = "Integer32"
_CclScriptControl_Object = MibTableColumn
cclScriptControl = _CclScriptControl_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 7, 1, 1, 2),
    _CclScriptControl_Type()
)
cclScriptControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cclScriptControl.setStatus("mandatory")
_CclPortTable_Object = MibTable
cclPortTable = _CclPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 7, 2)
)
if mibBuilder.loadTexts:
    cclPortTable.setStatus("mandatory")
_CclPortEntry_Object = MibTableRow
cclPortEntry = _CclPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 7, 2, 1)
)
cclPortEntry.setIndexNames(
    (0, "RFC1316-MIB", "charPortIndex"),
)
if mibBuilder.loadTexts:
    cclPortEntry.setStatus("mandatory")


class _CclPortCclName_Type(DisplayString):
    """Custom type cclPortCclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CclPortCclName_Type.__name__ = "DisplayString"
_CclPortCclName_Object = MibTableColumn
cclPortCclName = _CclPortCclName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 7, 2, 1, 1),
    _CclPortCclName_Type()
)
cclPortCclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cclPortCclName.setStatus("mandatory")


class _CclPortModemAudible_Type(Integer32):
    """Custom type cclPortModemAudible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CclPortModemAudible_Type.__name__ = "Integer32"
_CclPortModemAudible_Object = MibTableColumn
cclPortModemAudible = _CclPortModemAudible_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 7, 2, 1, 2),
    _CclPortModemAudible_Type()
)
cclPortModemAudible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cclPortModemAudible.setStatus("mandatory")
_XBroadcastGroup_ObjectIdentity = ObjectIdentity
xBroadcastGroup = _XBroadcastGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 8)
)
_BroadcastGroupTable_Object = MibTable
broadcastGroupTable = _BroadcastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 8, 1)
)
if mibBuilder.loadTexts:
    broadcastGroupTable.setStatus("mandatory")
_BroadcastGroupEntry_Object = MibTableRow
broadcastGroupEntry = _BroadcastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 8, 1, 1)
)
broadcastGroupEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "broadcastGroupIndex"),
)
if mibBuilder.loadTexts:
    broadcastGroupEntry.setStatus("mandatory")


class _BroadcastGroupIndex_Type(Integer32):
    """Custom type broadcastGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BroadcastGroupIndex_Type.__name__ = "Integer32"
_BroadcastGroupIndex_Object = MibTableColumn
broadcastGroupIndex = _BroadcastGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 8, 1, 1, 1),
    _BroadcastGroupIndex_Type()
)
broadcastGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadcastGroupIndex.setStatus("mandatory")


class _BroadcastGroupStatus_Type(Integer32):
    """Custom type broadcastGroupStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BroadcastGroupStatus_Type.__name__ = "Integer32"
_BroadcastGroupStatus_Object = MibTableColumn
broadcastGroupStatus = _BroadcastGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 8, 1, 1, 2),
    _BroadcastGroupStatus_Type()
)
broadcastGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastGroupStatus.setStatus("mandatory")
_BroadcastGroupMaster_Type = Integer32
_BroadcastGroupMaster_Object = MibTableColumn
broadcastGroupMaster = _BroadcastGroupMaster_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 8, 1, 1, 3),
    _BroadcastGroupMaster_Type()
)
broadcastGroupMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastGroupMaster.setStatus("mandatory")
_BroadcastGroupSlaves_Type = OctetString
_BroadcastGroupSlaves_Object = MibTableColumn
broadcastGroupSlaves = _BroadcastGroupSlaves_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 8, 1, 1, 4),
    _BroadcastGroupSlaves_Type()
)
broadcastGroupSlaves.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastGroupSlaves.setStatus("mandatory")
_BroadcastGroupSlavesBroadcastOnly_Type = OctetString
_BroadcastGroupSlavesBroadcastOnly_Object = MibTableColumn
broadcastGroupSlavesBroadcastOnly = _BroadcastGroupSlavesBroadcastOnly_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 8, 1, 1, 5),
    _BroadcastGroupSlavesBroadcastOnly_Type()
)
broadcastGroupSlavesBroadcastOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastGroupSlavesBroadcastOnly.setStatus("mandatory")


class _BroadcastGroupSlaveTcpPort_Type(Integer32):
    """Custom type broadcastGroupSlaveTcpPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65554),
    )


_BroadcastGroupSlaveTcpPort_Type.__name__ = "Integer32"
_BroadcastGroupSlaveTcpPort_Object = MibTableColumn
broadcastGroupSlaveTcpPort = _BroadcastGroupSlaveTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 8, 1, 1, 6),
    _BroadcastGroupSlaveTcpPort_Type()
)
broadcastGroupSlaveTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastGroupSlaveTcpPort.setStatus("mandatory")


class _BroadcastGroupSlaveTcpBroadcastOnly_Type(Integer32):
    """Custom type broadcastGroupSlaveTcpBroadcastOnly based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BroadcastGroupSlaveTcpBroadcastOnly_Type.__name__ = "Integer32"
_BroadcastGroupSlaveTcpBroadcastOnly_Object = MibTableColumn
broadcastGroupSlaveTcpBroadcastOnly = _BroadcastGroupSlaveTcpBroadcastOnly_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 8, 1, 1, 7),
    _BroadcastGroupSlaveTcpBroadcastOnly_Type()
)
broadcastGroupSlaveTcpBroadcastOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastGroupSlaveTcpBroadcastOnly.setStatus("mandatory")
_XPingHosts_ObjectIdentity = ObjectIdentity
xPingHosts = _XPingHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 9)
)
_PingHostsTable_Object = MibTable
pingHostsTable = _PingHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 9, 1)
)
if mibBuilder.loadTexts:
    pingHostsTable.setStatus("mandatory")
_PingHostsEntry_Object = MibTableRow
pingHostsEntry = _PingHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 9, 1, 1)
)
pingHostsEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostIndex"),
)
if mibBuilder.loadTexts:
    pingHostsEntry.setStatus("mandatory")


class _IcmpPingHostIndex_Type(Integer32):
    """Custom type icmpPingHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_IcmpPingHostIndex_Type.__name__ = "Integer32"
_IcmpPingHostIndex_Object = MibTableColumn
icmpPingHostIndex = _IcmpPingHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 9, 1, 1, 1),
    _IcmpPingHostIndex_Type()
)
icmpPingHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpPingHostIndex.setStatus("mandatory")
_IcmpPingHostAddress_Type = IpAddress
_IcmpPingHostAddress_Object = MibTableColumn
icmpPingHostAddress = _IcmpPingHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 9, 1, 1, 2),
    _IcmpPingHostAddress_Type()
)
icmpPingHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpPingHostAddress.setStatus("mandatory")


class _IcmpPingHostDescription_Type(DisplayString):
    """Custom type icmpPingHostDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IcmpPingHostDescription_Type.__name__ = "DisplayString"
_IcmpPingHostDescription_Object = MibTableColumn
icmpPingHostDescription = _IcmpPingHostDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 9, 1, 1, 3),
    _IcmpPingHostDescription_Type()
)
icmpPingHostDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpPingHostDescription.setStatus("mandatory")


class _IcmpPingHostNotificationType_Type(Integer32):
    """Custom type icmpPingHostNotificationType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("snmp", 2))
    )


_IcmpPingHostNotificationType_Type.__name__ = "Integer32"
_IcmpPingHostNotificationType_Object = MibTableColumn
icmpPingHostNotificationType = _IcmpPingHostNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 9, 1, 1, 4),
    _IcmpPingHostNotificationType_Type()
)
icmpPingHostNotificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpPingHostNotificationType.setStatus("mandatory")


class _IcmpPingHostPollingInterval_Type(Integer32):
    """Custom type icmpPingHostPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_IcmpPingHostPollingInterval_Type.__name__ = "Integer32"
_IcmpPingHostPollingInterval_Object = MibTableColumn
icmpPingHostPollingInterval = _IcmpPingHostPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 9, 1, 1, 5),
    _IcmpPingHostPollingInterval_Type()
)
icmpPingHostPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpPingHostPollingInterval.setStatus("mandatory")


class _IcmpPingHostMaximumRetries_Type(Integer32):
    """Custom type icmpPingHostMaximumRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IcmpPingHostMaximumRetries_Type.__name__ = "Integer32"
_IcmpPingHostMaximumRetries_Object = MibTableColumn
icmpPingHostMaximumRetries = _IcmpPingHostMaximumRetries_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 9, 1, 1, 6),
    _IcmpPingHostMaximumRetries_Type()
)
icmpPingHostMaximumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpPingHostMaximumRetries.setStatus("mandatory")


class _IcmpPingHostTrapSeverityLevel_Type(Integer32):
    """Custom type icmpPingHostTrapSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_IcmpPingHostTrapSeverityLevel_Type.__name__ = "Integer32"
_IcmpPingHostTrapSeverityLevel_Object = MibTableColumn
icmpPingHostTrapSeverityLevel = _IcmpPingHostTrapSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 9, 1, 1, 7),
    _IcmpPingHostTrapSeverityLevel_Type()
)
icmpPingHostTrapSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpPingHostTrapSeverityLevel.setStatus("mandatory")


class _IcmpPingHostStatus_Type(Integer32):
    """Custom type icmpPingHostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_IcmpPingHostStatus_Type.__name__ = "Integer32"
_IcmpPingHostStatus_Object = MibTableColumn
icmpPingHostStatus = _IcmpPingHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 9, 1, 1, 8),
    _IcmpPingHostStatus_Type()
)
icmpPingHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpPingHostStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

contactClosureChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30)
)
contactClosureChanged.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    contactClosureChanged.setStatus(
        ""
    )

powerAlarmFuseBankA = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 31)
)
powerAlarmFuseBankA.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicPowerStatusFuseA"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    powerAlarmFuseBankA.setStatus(
        ""
    )

powerAlarmFuseBankB = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 32)
)
powerAlarmFuseBankB.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicPowerStatusFuseB"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    powerAlarmFuseBankB.setStatus(
        ""
    )

powerSupplyAlarmA = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 33)
)
powerSupplyAlarmA.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicPowerSupplyStatusA"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    powerSupplyAlarmA.setStatus(
        ""
    )

powerSupplyAlarmB = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 34)
)
powerSupplyAlarmB.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicPowerSupplyStatusB"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    powerSupplyAlarmB.setStatus(
        ""
    )

portInputSignalChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 35)
)
portInputSignalChange.setObjects(
      *(("RFC1317-MIB", "rs232InSigState"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RFC1317-MIB", "rs232PortIndex"))
)
if mibBuilder.loadTexts:
    portInputSignalChange.setStatus(
        ""
    )

portOutputSignalChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 36)
)
portOutputSignalChange.setObjects(
      *(("RFC1317-MIB", "rs232OutSigState"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RFC1317-MIB", "rs232PortIndex"))
)
if mibBuilder.loadTexts:
    portOutputSignalChange.setStatus(
        ""
    )

humidityThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 37)
)
humidityThresholdExceeded.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicHumidityValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureHumiditySensorName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicHumiditySensorIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicHumidityAlarmStatus"))
)
if mibBuilder.loadTexts:
    humidityThresholdExceeded.setStatus(
        ""
    )

temperatureThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 38)
)
temperatureThresholdExceeded.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureHumiditySensorName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureSensorIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureAlarmStatus"))
)
if mibBuilder.loadTexts:
    temperatureThresholdExceeded.setStatus(
        ""
    )

alarmMasterNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 39)
)
alarmMasterNotResponding.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicPortIndex"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicPortAlarmMasterStatus"))
)
if mibBuilder.loadTexts:
    alarmMasterNotResponding.setStatus(
        ""
    )

alarmMasterInputStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 41)
)
alarmMasterInputStateChange.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"))
)
if mibBuilder.loadTexts:
    alarmMasterInputStateChange.setStatus(
        ""
    )

asciiToTrapTranslation = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 42)
)
asciiToTrapTranslation.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicPortAsciiToTrapTranslationTrapSeverity"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicPortAsciiToTrapTranslationLastMessage"))
)
if mibBuilder.loadTexts:
    asciiToTrapTranslation.setStatus(
        ""
    )

powerMasterNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 43)
)
powerMasterNotResponding.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicPortIndex"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicPortPowerMasterDeviceStatus"))
)
if mibBuilder.loadTexts:
    powerMasterNotResponding.setStatus(
        ""
    )

temperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 44)
)
temperatureNormal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureHumiditySensorName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureSensorIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureAlarmStatus"))
)
if mibBuilder.loadTexts:
    temperatureNormal.setStatus(
        ""
    )

humidityNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 45)
)
humidityNormal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicHumidityValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicTemperatureHumiditySensorName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicHumiditySensorIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicHumidityAlarmStatus"))
)
if mibBuilder.loadTexts:
    humidityNormal.setStatus(
        ""
    )

alarmMasterSideAOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 46)
)
alarmMasterSideAOff.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicPortIndex"))
)
if mibBuilder.loadTexts:
    alarmMasterSideAOff.setStatus(
        ""
    )

alarmMasterSideBOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 47)
)
alarmMasterSideBOff.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicPortIndex"))
)
if mibBuilder.loadTexts:
    alarmMasterSideBOff.setStatus(
        ""
    )

alarmMasterSideAOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 48)
)
alarmMasterSideAOn.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicPortIndex"))
)
if mibBuilder.loadTexts:
    alarmMasterSideAOn.setStatus(
        ""
    )

alarmMasterSideBOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 49)
)
alarmMasterSideBOn.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicPortIndex"))
)
if mibBuilder.loadTexts:
    alarmMasterSideBOn.setStatus(
        ""
    )

icmpPingHostNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 50)
)
icmpPingHostNotReachable.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostAddress"),
        ("MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostDescription"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostPollingInterval"),
        ("MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostMaximumRetries"),
        ("MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostStatus"))
)
if mibBuilder.loadTexts:
    icmpPingHostNotReachable.setStatus(
        ""
    )

icmpPingHostResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 51)
)
icmpPingHostResponding.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostAddress"),
        ("MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostDescription"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostPollingInterval"),
        ("MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostMaximumRetries"),
        ("MRV-IN-REACH-CHARACTER-MIB", "icmpPingHostStatus"))
)
if mibBuilder.loadTexts:
    icmpPingHostResponding.setStatus(
        ""
    )

alarmInputLowDensity0001Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10001)
)
alarmInputLowDensity0001Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0001Alarm.setStatus(
        ""
    )

alarmInputLowDensity0002Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10002)
)
alarmInputLowDensity0002Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0002Alarm.setStatus(
        ""
    )

alarmInputLowDensity0003Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10003)
)
alarmInputLowDensity0003Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0003Alarm.setStatus(
        ""
    )

alarmInputLowDensity0004Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10004)
)
alarmInputLowDensity0004Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0004Alarm.setStatus(
        ""
    )

alarmInputLowDensity0005Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10005)
)
alarmInputLowDensity0005Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0005Alarm.setStatus(
        ""
    )

alarmInputLowDensity0006Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10006)
)
alarmInputLowDensity0006Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0006Alarm.setStatus(
        ""
    )

alarmInputLowDensity0007Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10007)
)
alarmInputLowDensity0007Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0007Alarm.setStatus(
        ""
    )

alarmInputLowDensity0008Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10008)
)
alarmInputLowDensity0008Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0008Alarm.setStatus(
        ""
    )

alarmInputLowDensity0009Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10009)
)
alarmInputLowDensity0009Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0009Alarm.setStatus(
        ""
    )

alarmInputLowDensity0010Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10010)
)
alarmInputLowDensity0010Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0010Alarm.setStatus(
        ""
    )

alarmInputLowDensity0011Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10011)
)
alarmInputLowDensity0011Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0011Alarm.setStatus(
        ""
    )

alarmInputLowDensity0012Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10012)
)
alarmInputLowDensity0012Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0012Alarm.setStatus(
        ""
    )

alarmInputLowDensity0013Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10013)
)
alarmInputLowDensity0013Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0013Alarm.setStatus(
        ""
    )

alarmInputLowDensity0014Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10014)
)
alarmInputLowDensity0014Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0014Alarm.setStatus(
        ""
    )

alarmInputLowDensity0015Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10015)
)
alarmInputLowDensity0015Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0015Alarm.setStatus(
        ""
    )

alarmInputLowDensity0016Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10016)
)
alarmInputLowDensity0016Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0016Alarm.setStatus(
        ""
    )

alarmInputLowDensity0017Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10017)
)
alarmInputLowDensity0017Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0017Alarm.setStatus(
        ""
    )

alarmInputLowDensity0018Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10018)
)
alarmInputLowDensity0018Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0018Alarm.setStatus(
        ""
    )

alarmInputLowDensity0019Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10019)
)
alarmInputLowDensity0019Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0019Alarm.setStatus(
        ""
    )

alarmInputLowDensity0020Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10020)
)
alarmInputLowDensity0020Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0020Alarm.setStatus(
        ""
    )

alarmInputLowDensity0021Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10021)
)
alarmInputLowDensity0021Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0021Alarm.setStatus(
        ""
    )

alarmInputLowDensity0022Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10022)
)
alarmInputLowDensity0022Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0022Alarm.setStatus(
        ""
    )

alarmInputLowDensity0023Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10023)
)
alarmInputLowDensity0023Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0023Alarm.setStatus(
        ""
    )

alarmInputLowDensity0024Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10024)
)
alarmInputLowDensity0024Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0024Alarm.setStatus(
        ""
    )

alarmInputLowDensity0025Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10025)
)
alarmInputLowDensity0025Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0025Alarm.setStatus(
        ""
    )

alarmInputLowDensity0026Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10026)
)
alarmInputLowDensity0026Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0026Alarm.setStatus(
        ""
    )

alarmInputLowDensity0027Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10027)
)
alarmInputLowDensity0027Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0027Alarm.setStatus(
        ""
    )

alarmInputLowDensity0028Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10028)
)
alarmInputLowDensity0028Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0028Alarm.setStatus(
        ""
    )

alarmInputLowDensity0029Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10029)
)
alarmInputLowDensity0029Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0029Alarm.setStatus(
        ""
    )

alarmInputLowDensity0030Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10030)
)
alarmInputLowDensity0030Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0030Alarm.setStatus(
        ""
    )

alarmInputLowDensity0031Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10031)
)
alarmInputLowDensity0031Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0031Alarm.setStatus(
        ""
    )

alarmInputLowDensity0032Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10032)
)
alarmInputLowDensity0032Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0032Alarm.setStatus(
        ""
    )

alarmInputLowDensity0033Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10033)
)
alarmInputLowDensity0033Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0033Alarm.setStatus(
        ""
    )

alarmInputLowDensity0034Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10034)
)
alarmInputLowDensity0034Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0034Alarm.setStatus(
        ""
    )

alarmInputLowDensity0035Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10035)
)
alarmInputLowDensity0035Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0035Alarm.setStatus(
        ""
    )

alarmInputLowDensity0036Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10036)
)
alarmInputLowDensity0036Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0036Alarm.setStatus(
        ""
    )

alarmInputLowDensity0037Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10037)
)
alarmInputLowDensity0037Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0037Alarm.setStatus(
        ""
    )

alarmInputLowDensity0038Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10038)
)
alarmInputLowDensity0038Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0038Alarm.setStatus(
        ""
    )

alarmInputLowDensity0039Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10039)
)
alarmInputLowDensity0039Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0039Alarm.setStatus(
        ""
    )

alarmInputLowDensity0040Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10040)
)
alarmInputLowDensity0040Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0040Alarm.setStatus(
        ""
    )

alarmInputLowDensity0041Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10041)
)
alarmInputLowDensity0041Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0041Alarm.setStatus(
        ""
    )

alarmInputLowDensity0042Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10042)
)
alarmInputLowDensity0042Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0042Alarm.setStatus(
        ""
    )

alarmInputLowDensity0043Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10043)
)
alarmInputLowDensity0043Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0043Alarm.setStatus(
        ""
    )

alarmInputLowDensity0044Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10044)
)
alarmInputLowDensity0044Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0044Alarm.setStatus(
        ""
    )

alarmInputLowDensity0045Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10045)
)
alarmInputLowDensity0045Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0045Alarm.setStatus(
        ""
    )

alarmInputLowDensity0046Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10046)
)
alarmInputLowDensity0046Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0046Alarm.setStatus(
        ""
    )

alarmInputLowDensity0047Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10047)
)
alarmInputLowDensity0047Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0047Alarm.setStatus(
        ""
    )

alarmInputLowDensity0048Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10048)
)
alarmInputLowDensity0048Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0048Alarm.setStatus(
        ""
    )

alarmInputLowDensity0049Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10049)
)
alarmInputLowDensity0049Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0049Alarm.setStatus(
        ""
    )

alarmInputLowDensity0050Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10050)
)
alarmInputLowDensity0050Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0050Alarm.setStatus(
        ""
    )

alarmInputLowDensity0051Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10051)
)
alarmInputLowDensity0051Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0051Alarm.setStatus(
        ""
    )

alarmInputLowDensity0052Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10052)
)
alarmInputLowDensity0052Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0052Alarm.setStatus(
        ""
    )

alarmInputLowDensity0053Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10053)
)
alarmInputLowDensity0053Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0053Alarm.setStatus(
        ""
    )

alarmInputLowDensity0054Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10054)
)
alarmInputLowDensity0054Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0054Alarm.setStatus(
        ""
    )

alarmInputLowDensity0055Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10055)
)
alarmInputLowDensity0055Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0055Alarm.setStatus(
        ""
    )

alarmInputLowDensity0056Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10056)
)
alarmInputLowDensity0056Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0056Alarm.setStatus(
        ""
    )

alarmInputLowDensity0057Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10057)
)
alarmInputLowDensity0057Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0057Alarm.setStatus(
        ""
    )

alarmInputLowDensity0058Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10058)
)
alarmInputLowDensity0058Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0058Alarm.setStatus(
        ""
    )

alarmInputLowDensity0059Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10059)
)
alarmInputLowDensity0059Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0059Alarm.setStatus(
        ""
    )

alarmInputLowDensity0060Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10060)
)
alarmInputLowDensity0060Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0060Alarm.setStatus(
        ""
    )

alarmInputLowDensity0061Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10061)
)
alarmInputLowDensity0061Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0061Alarm.setStatus(
        ""
    )

alarmInputLowDensity0062Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10062)
)
alarmInputLowDensity0062Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0062Alarm.setStatus(
        ""
    )

alarmInputLowDensity0063Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10063)
)
alarmInputLowDensity0063Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0063Alarm.setStatus(
        ""
    )

alarmInputLowDensity0064Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10064)
)
alarmInputLowDensity0064Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0064Alarm.setStatus(
        ""
    )

alarmInputLowDensity0065Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10065)
)
alarmInputLowDensity0065Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0065Alarm.setStatus(
        ""
    )

alarmInputLowDensity0066Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10066)
)
alarmInputLowDensity0066Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0066Alarm.setStatus(
        ""
    )

alarmInputLowDensity0067Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10067)
)
alarmInputLowDensity0067Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0067Alarm.setStatus(
        ""
    )

alarmInputLowDensity0068Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10068)
)
alarmInputLowDensity0068Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0068Alarm.setStatus(
        ""
    )

alarmInputLowDensity0069Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10069)
)
alarmInputLowDensity0069Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0069Alarm.setStatus(
        ""
    )

alarmInputLowDensity0070Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10070)
)
alarmInputLowDensity0070Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0070Alarm.setStatus(
        ""
    )

alarmInputLowDensity0071Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10071)
)
alarmInputLowDensity0071Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0071Alarm.setStatus(
        ""
    )

alarmInputLowDensity0072Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10072)
)
alarmInputLowDensity0072Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0072Alarm.setStatus(
        ""
    )

alarmInputLowDensity0073Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10073)
)
alarmInputLowDensity0073Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0073Alarm.setStatus(
        ""
    )

alarmInputLowDensity0074Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10074)
)
alarmInputLowDensity0074Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0074Alarm.setStatus(
        ""
    )

alarmInputLowDensity0075Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10075)
)
alarmInputLowDensity0075Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0075Alarm.setStatus(
        ""
    )

alarmInputLowDensity0076Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10076)
)
alarmInputLowDensity0076Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0076Alarm.setStatus(
        ""
    )

alarmInputLowDensity0077Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10077)
)
alarmInputLowDensity0077Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0077Alarm.setStatus(
        ""
    )

alarmInputLowDensity0078Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10078)
)
alarmInputLowDensity0078Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0078Alarm.setStatus(
        ""
    )

alarmInputLowDensity0079Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10079)
)
alarmInputLowDensity0079Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0079Alarm.setStatus(
        ""
    )

alarmInputLowDensity0080Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 10080)
)
alarmInputLowDensity0080Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0080Alarm.setStatus(
        ""
    )

alarmInputLowDensity0001Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20001)
)
alarmInputLowDensity0001Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0001Normal.setStatus(
        ""
    )

alarmInputLowDensity0002Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20002)
)
alarmInputLowDensity0002Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0002Normal.setStatus(
        ""
    )

alarmInputLowDensity0003Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20003)
)
alarmInputLowDensity0003Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0003Normal.setStatus(
        ""
    )

alarmInputLowDensity0004Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20004)
)
alarmInputLowDensity0004Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0004Normal.setStatus(
        ""
    )

alarmInputLowDensity0005Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20005)
)
alarmInputLowDensity0005Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0005Normal.setStatus(
        ""
    )

alarmInputLowDensity0006Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20006)
)
alarmInputLowDensity0006Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0006Normal.setStatus(
        ""
    )

alarmInputLowDensity0007Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20007)
)
alarmInputLowDensity0007Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0007Normal.setStatus(
        ""
    )

alarmInputLowDensity0008Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20008)
)
alarmInputLowDensity0008Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0008Normal.setStatus(
        ""
    )

alarmInputLowDensity0009Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20009)
)
alarmInputLowDensity0009Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0009Normal.setStatus(
        ""
    )

alarmInputLowDensity0010Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20010)
)
alarmInputLowDensity0010Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0010Normal.setStatus(
        ""
    )

alarmInputLowDensity0011Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20011)
)
alarmInputLowDensity0011Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0011Normal.setStatus(
        ""
    )

alarmInputLowDensity0012Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20012)
)
alarmInputLowDensity0012Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0012Normal.setStatus(
        ""
    )

alarmInputLowDensity0013Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20013)
)
alarmInputLowDensity0013Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0013Normal.setStatus(
        ""
    )

alarmInputLowDensity0014Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20014)
)
alarmInputLowDensity0014Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0014Normal.setStatus(
        ""
    )

alarmInputLowDensity0015Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20015)
)
alarmInputLowDensity0015Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0015Normal.setStatus(
        ""
    )

alarmInputLowDensity0016Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20016)
)
alarmInputLowDensity0016Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0016Normal.setStatus(
        ""
    )

alarmInputLowDensity0017Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20017)
)
alarmInputLowDensity0017Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0017Normal.setStatus(
        ""
    )

alarmInputLowDensity0018Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20018)
)
alarmInputLowDensity0018Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0018Normal.setStatus(
        ""
    )

alarmInputLowDensity0019Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20019)
)
alarmInputLowDensity0019Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0019Normal.setStatus(
        ""
    )

alarmInputLowDensity0020Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20020)
)
alarmInputLowDensity0020Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0020Normal.setStatus(
        ""
    )

alarmInputLowDensity0021Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20021)
)
alarmInputLowDensity0021Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0021Normal.setStatus(
        ""
    )

alarmInputLowDensity0022Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20022)
)
alarmInputLowDensity0022Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0022Normal.setStatus(
        ""
    )

alarmInputLowDensity0023Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20023)
)
alarmInputLowDensity0023Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0023Normal.setStatus(
        ""
    )

alarmInputLowDensity0024Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20024)
)
alarmInputLowDensity0024Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0024Normal.setStatus(
        ""
    )

alarmInputLowDensity0025Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20025)
)
alarmInputLowDensity0025Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0025Normal.setStatus(
        ""
    )

alarmInputLowDensity0026Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20026)
)
alarmInputLowDensity0026Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0026Normal.setStatus(
        ""
    )

alarmInputLowDensity0027Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20027)
)
alarmInputLowDensity0027Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0027Normal.setStatus(
        ""
    )

alarmInputLowDensity0028Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20028)
)
alarmInputLowDensity0028Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0028Normal.setStatus(
        ""
    )

alarmInputLowDensity0029Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20029)
)
alarmInputLowDensity0029Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0029Normal.setStatus(
        ""
    )

alarmInputLowDensity0030Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20030)
)
alarmInputLowDensity0030Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0030Normal.setStatus(
        ""
    )

alarmInputLowDensity0031Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20031)
)
alarmInputLowDensity0031Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0031Normal.setStatus(
        ""
    )

alarmInputLowDensity0032Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20032)
)
alarmInputLowDensity0032Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0032Normal.setStatus(
        ""
    )

alarmInputLowDensity0033Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20033)
)
alarmInputLowDensity0033Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0033Normal.setStatus(
        ""
    )

alarmInputLowDensity0034Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20034)
)
alarmInputLowDensity0034Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0034Normal.setStatus(
        ""
    )

alarmInputLowDensity0035Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20035)
)
alarmInputLowDensity0035Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0035Normal.setStatus(
        ""
    )

alarmInputLowDensity0036Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20036)
)
alarmInputLowDensity0036Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0036Normal.setStatus(
        ""
    )

alarmInputLowDensity0037Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20037)
)
alarmInputLowDensity0037Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0037Normal.setStatus(
        ""
    )

alarmInputLowDensity0038Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20038)
)
alarmInputLowDensity0038Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0038Normal.setStatus(
        ""
    )

alarmInputLowDensity0039Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20039)
)
alarmInputLowDensity0039Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0039Normal.setStatus(
        ""
    )

alarmInputLowDensity0040Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20040)
)
alarmInputLowDensity0040Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0040Normal.setStatus(
        ""
    )

alarmInputLowDensity0041Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20041)
)
alarmInputLowDensity0041Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0041Normal.setStatus(
        ""
    )

alarmInputLowDensity0042Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20042)
)
alarmInputLowDensity0042Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0042Normal.setStatus(
        ""
    )

alarmInputLowDensity0043Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20043)
)
alarmInputLowDensity0043Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0043Normal.setStatus(
        ""
    )

alarmInputLowDensity0044Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20044)
)
alarmInputLowDensity0044Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0044Normal.setStatus(
        ""
    )

alarmInputLowDensity0045Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20045)
)
alarmInputLowDensity0045Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0045Normal.setStatus(
        ""
    )

alarmInputLowDensity0046Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20046)
)
alarmInputLowDensity0046Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0046Normal.setStatus(
        ""
    )

alarmInputLowDensity0047Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20047)
)
alarmInputLowDensity0047Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0047Normal.setStatus(
        ""
    )

alarmInputLowDensity0048Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20048)
)
alarmInputLowDensity0048Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0048Normal.setStatus(
        ""
    )

alarmInputLowDensity0049Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20049)
)
alarmInputLowDensity0049Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0049Normal.setStatus(
        ""
    )

alarmInputLowDensity0050Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20050)
)
alarmInputLowDensity0050Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0050Normal.setStatus(
        ""
    )

alarmInputLowDensity0051Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20051)
)
alarmInputLowDensity0051Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0051Normal.setStatus(
        ""
    )

alarmInputLowDensity0052Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20052)
)
alarmInputLowDensity0052Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0052Normal.setStatus(
        ""
    )

alarmInputLowDensity0053Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20053)
)
alarmInputLowDensity0053Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0053Normal.setStatus(
        ""
    )

alarmInputLowDensity0054Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20054)
)
alarmInputLowDensity0054Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0054Normal.setStatus(
        ""
    )

alarmInputLowDensity0055Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20055)
)
alarmInputLowDensity0055Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0055Normal.setStatus(
        ""
    )

alarmInputLowDensity0056Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20056)
)
alarmInputLowDensity0056Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0056Normal.setStatus(
        ""
    )

alarmInputLowDensity0057Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20057)
)
alarmInputLowDensity0057Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0057Normal.setStatus(
        ""
    )

alarmInputLowDensity0058Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20058)
)
alarmInputLowDensity0058Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0058Normal.setStatus(
        ""
    )

alarmInputLowDensity0059Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20059)
)
alarmInputLowDensity0059Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0059Normal.setStatus(
        ""
    )

alarmInputLowDensity0060Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20060)
)
alarmInputLowDensity0060Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0060Normal.setStatus(
        ""
    )

alarmInputLowDensity0061Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20061)
)
alarmInputLowDensity0061Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0061Normal.setStatus(
        ""
    )

alarmInputLowDensity0062Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20062)
)
alarmInputLowDensity0062Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0062Normal.setStatus(
        ""
    )

alarmInputLowDensity0063Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20063)
)
alarmInputLowDensity0063Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0063Normal.setStatus(
        ""
    )

alarmInputLowDensity0064Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20064)
)
alarmInputLowDensity0064Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0064Normal.setStatus(
        ""
    )

alarmInputLowDensity0065Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20065)
)
alarmInputLowDensity0065Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0065Normal.setStatus(
        ""
    )

alarmInputLowDensity0066Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20066)
)
alarmInputLowDensity0066Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0066Normal.setStatus(
        ""
    )

alarmInputLowDensity0067Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20067)
)
alarmInputLowDensity0067Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0067Normal.setStatus(
        ""
    )

alarmInputLowDensity0068Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20068)
)
alarmInputLowDensity0068Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0068Normal.setStatus(
        ""
    )

alarmInputLowDensity0069Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20069)
)
alarmInputLowDensity0069Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0069Normal.setStatus(
        ""
    )

alarmInputLowDensity0070Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20070)
)
alarmInputLowDensity0070Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0070Normal.setStatus(
        ""
    )

alarmInputLowDensity0071Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20071)
)
alarmInputLowDensity0071Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0071Normal.setStatus(
        ""
    )

alarmInputLowDensity0072Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20072)
)
alarmInputLowDensity0072Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0072Normal.setStatus(
        ""
    )

alarmInputLowDensity0073Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20073)
)
alarmInputLowDensity0073Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0073Normal.setStatus(
        ""
    )

alarmInputLowDensity0074Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20074)
)
alarmInputLowDensity0074Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0074Normal.setStatus(
        ""
    )

alarmInputLowDensity0075Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20075)
)
alarmInputLowDensity0075Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0075Normal.setStatus(
        ""
    )

alarmInputLowDensity0076Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20076)
)
alarmInputLowDensity0076Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0076Normal.setStatus(
        ""
    )

alarmInputLowDensity0077Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20077)
)
alarmInputLowDensity0077Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0077Normal.setStatus(
        ""
    )

alarmInputLowDensity0078Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20078)
)
alarmInputLowDensity0078Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0078Normal.setStatus(
        ""
    )

alarmInputLowDensity0079Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20079)
)
alarmInputLowDensity0079Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0079Normal.setStatus(
        ""
    )

alarmInputLowDensity0080Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 20080)
)
alarmInputLowDensity0080Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputIndex"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicContactClosureOrAlarmInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputLowDensity0080Normal.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IN-REACH-CHARACTER-MIB",
    **{"contactClosureChanged": contactClosureChanged,
       "powerAlarmFuseBankA": powerAlarmFuseBankA,
       "powerAlarmFuseBankB": powerAlarmFuseBankB,
       "powerSupplyAlarmA": powerSupplyAlarmA,
       "powerSupplyAlarmB": powerSupplyAlarmB,
       "portInputSignalChange": portInputSignalChange,
       "portOutputSignalChange": portOutputSignalChange,
       "humidityThresholdExceeded": humidityThresholdExceeded,
       "temperatureThresholdExceeded": temperatureThresholdExceeded,
       "alarmMasterNotResponding": alarmMasterNotResponding,
       "alarmMasterInputStateChange": alarmMasterInputStateChange,
       "asciiToTrapTranslation": asciiToTrapTranslation,
       "powerMasterNotResponding": powerMasterNotResponding,
       "temperatureNormal": temperatureNormal,
       "humidityNormal": humidityNormal,
       "alarmMasterSideAOff": alarmMasterSideAOff,
       "alarmMasterSideBOff": alarmMasterSideBOff,
       "alarmMasterSideAOn": alarmMasterSideAOn,
       "alarmMasterSideBOn": alarmMasterSideBOn,
       "icmpPingHostNotReachable": icmpPingHostNotReachable,
       "icmpPingHostResponding": icmpPingHostResponding,
       "alarmInputLowDensity0001Alarm": alarmInputLowDensity0001Alarm,
       "alarmInputLowDensity0002Alarm": alarmInputLowDensity0002Alarm,
       "alarmInputLowDensity0003Alarm": alarmInputLowDensity0003Alarm,
       "alarmInputLowDensity0004Alarm": alarmInputLowDensity0004Alarm,
       "alarmInputLowDensity0005Alarm": alarmInputLowDensity0005Alarm,
       "alarmInputLowDensity0006Alarm": alarmInputLowDensity0006Alarm,
       "alarmInputLowDensity0007Alarm": alarmInputLowDensity0007Alarm,
       "alarmInputLowDensity0008Alarm": alarmInputLowDensity0008Alarm,
       "alarmInputLowDensity0009Alarm": alarmInputLowDensity0009Alarm,
       "alarmInputLowDensity0010Alarm": alarmInputLowDensity0010Alarm,
       "alarmInputLowDensity0011Alarm": alarmInputLowDensity0011Alarm,
       "alarmInputLowDensity0012Alarm": alarmInputLowDensity0012Alarm,
       "alarmInputLowDensity0013Alarm": alarmInputLowDensity0013Alarm,
       "alarmInputLowDensity0014Alarm": alarmInputLowDensity0014Alarm,
       "alarmInputLowDensity0015Alarm": alarmInputLowDensity0015Alarm,
       "alarmInputLowDensity0016Alarm": alarmInputLowDensity0016Alarm,
       "alarmInputLowDensity0017Alarm": alarmInputLowDensity0017Alarm,
       "alarmInputLowDensity0018Alarm": alarmInputLowDensity0018Alarm,
       "alarmInputLowDensity0019Alarm": alarmInputLowDensity0019Alarm,
       "alarmInputLowDensity0020Alarm": alarmInputLowDensity0020Alarm,
       "alarmInputLowDensity0021Alarm": alarmInputLowDensity0021Alarm,
       "alarmInputLowDensity0022Alarm": alarmInputLowDensity0022Alarm,
       "alarmInputLowDensity0023Alarm": alarmInputLowDensity0023Alarm,
       "alarmInputLowDensity0024Alarm": alarmInputLowDensity0024Alarm,
       "alarmInputLowDensity0025Alarm": alarmInputLowDensity0025Alarm,
       "alarmInputLowDensity0026Alarm": alarmInputLowDensity0026Alarm,
       "alarmInputLowDensity0027Alarm": alarmInputLowDensity0027Alarm,
       "alarmInputLowDensity0028Alarm": alarmInputLowDensity0028Alarm,
       "alarmInputLowDensity0029Alarm": alarmInputLowDensity0029Alarm,
       "alarmInputLowDensity0030Alarm": alarmInputLowDensity0030Alarm,
       "alarmInputLowDensity0031Alarm": alarmInputLowDensity0031Alarm,
       "alarmInputLowDensity0032Alarm": alarmInputLowDensity0032Alarm,
       "alarmInputLowDensity0033Alarm": alarmInputLowDensity0033Alarm,
       "alarmInputLowDensity0034Alarm": alarmInputLowDensity0034Alarm,
       "alarmInputLowDensity0035Alarm": alarmInputLowDensity0035Alarm,
       "alarmInputLowDensity0036Alarm": alarmInputLowDensity0036Alarm,
       "alarmInputLowDensity0037Alarm": alarmInputLowDensity0037Alarm,
       "alarmInputLowDensity0038Alarm": alarmInputLowDensity0038Alarm,
       "alarmInputLowDensity0039Alarm": alarmInputLowDensity0039Alarm,
       "alarmInputLowDensity0040Alarm": alarmInputLowDensity0040Alarm,
       "alarmInputLowDensity0041Alarm": alarmInputLowDensity0041Alarm,
       "alarmInputLowDensity0042Alarm": alarmInputLowDensity0042Alarm,
       "alarmInputLowDensity0043Alarm": alarmInputLowDensity0043Alarm,
       "alarmInputLowDensity0044Alarm": alarmInputLowDensity0044Alarm,
       "alarmInputLowDensity0045Alarm": alarmInputLowDensity0045Alarm,
       "alarmInputLowDensity0046Alarm": alarmInputLowDensity0046Alarm,
       "alarmInputLowDensity0047Alarm": alarmInputLowDensity0047Alarm,
       "alarmInputLowDensity0048Alarm": alarmInputLowDensity0048Alarm,
       "alarmInputLowDensity0049Alarm": alarmInputLowDensity0049Alarm,
       "alarmInputLowDensity0050Alarm": alarmInputLowDensity0050Alarm,
       "alarmInputLowDensity0051Alarm": alarmInputLowDensity0051Alarm,
       "alarmInputLowDensity0052Alarm": alarmInputLowDensity0052Alarm,
       "alarmInputLowDensity0053Alarm": alarmInputLowDensity0053Alarm,
       "alarmInputLowDensity0054Alarm": alarmInputLowDensity0054Alarm,
       "alarmInputLowDensity0055Alarm": alarmInputLowDensity0055Alarm,
       "alarmInputLowDensity0056Alarm": alarmInputLowDensity0056Alarm,
       "alarmInputLowDensity0057Alarm": alarmInputLowDensity0057Alarm,
       "alarmInputLowDensity0058Alarm": alarmInputLowDensity0058Alarm,
       "alarmInputLowDensity0059Alarm": alarmInputLowDensity0059Alarm,
       "alarmInputLowDensity0060Alarm": alarmInputLowDensity0060Alarm,
       "alarmInputLowDensity0061Alarm": alarmInputLowDensity0061Alarm,
       "alarmInputLowDensity0062Alarm": alarmInputLowDensity0062Alarm,
       "alarmInputLowDensity0063Alarm": alarmInputLowDensity0063Alarm,
       "alarmInputLowDensity0064Alarm": alarmInputLowDensity0064Alarm,
       "alarmInputLowDensity0065Alarm": alarmInputLowDensity0065Alarm,
       "alarmInputLowDensity0066Alarm": alarmInputLowDensity0066Alarm,
       "alarmInputLowDensity0067Alarm": alarmInputLowDensity0067Alarm,
       "alarmInputLowDensity0068Alarm": alarmInputLowDensity0068Alarm,
       "alarmInputLowDensity0069Alarm": alarmInputLowDensity0069Alarm,
       "alarmInputLowDensity0070Alarm": alarmInputLowDensity0070Alarm,
       "alarmInputLowDensity0071Alarm": alarmInputLowDensity0071Alarm,
       "alarmInputLowDensity0072Alarm": alarmInputLowDensity0072Alarm,
       "alarmInputLowDensity0073Alarm": alarmInputLowDensity0073Alarm,
       "alarmInputLowDensity0074Alarm": alarmInputLowDensity0074Alarm,
       "alarmInputLowDensity0075Alarm": alarmInputLowDensity0075Alarm,
       "alarmInputLowDensity0076Alarm": alarmInputLowDensity0076Alarm,
       "alarmInputLowDensity0077Alarm": alarmInputLowDensity0077Alarm,
       "alarmInputLowDensity0078Alarm": alarmInputLowDensity0078Alarm,
       "alarmInputLowDensity0079Alarm": alarmInputLowDensity0079Alarm,
       "alarmInputLowDensity0080Alarm": alarmInputLowDensity0080Alarm,
       "alarmInputLowDensity0001Normal": alarmInputLowDensity0001Normal,
       "alarmInputLowDensity0002Normal": alarmInputLowDensity0002Normal,
       "alarmInputLowDensity0003Normal": alarmInputLowDensity0003Normal,
       "alarmInputLowDensity0004Normal": alarmInputLowDensity0004Normal,
       "alarmInputLowDensity0005Normal": alarmInputLowDensity0005Normal,
       "alarmInputLowDensity0006Normal": alarmInputLowDensity0006Normal,
       "alarmInputLowDensity0007Normal": alarmInputLowDensity0007Normal,
       "alarmInputLowDensity0008Normal": alarmInputLowDensity0008Normal,
       "alarmInputLowDensity0009Normal": alarmInputLowDensity0009Normal,
       "alarmInputLowDensity0010Normal": alarmInputLowDensity0010Normal,
       "alarmInputLowDensity0011Normal": alarmInputLowDensity0011Normal,
       "alarmInputLowDensity0012Normal": alarmInputLowDensity0012Normal,
       "alarmInputLowDensity0013Normal": alarmInputLowDensity0013Normal,
       "alarmInputLowDensity0014Normal": alarmInputLowDensity0014Normal,
       "alarmInputLowDensity0015Normal": alarmInputLowDensity0015Normal,
       "alarmInputLowDensity0016Normal": alarmInputLowDensity0016Normal,
       "alarmInputLowDensity0017Normal": alarmInputLowDensity0017Normal,
       "alarmInputLowDensity0018Normal": alarmInputLowDensity0018Normal,
       "alarmInputLowDensity0019Normal": alarmInputLowDensity0019Normal,
       "alarmInputLowDensity0020Normal": alarmInputLowDensity0020Normal,
       "alarmInputLowDensity0021Normal": alarmInputLowDensity0021Normal,
       "alarmInputLowDensity0022Normal": alarmInputLowDensity0022Normal,
       "alarmInputLowDensity0023Normal": alarmInputLowDensity0023Normal,
       "alarmInputLowDensity0024Normal": alarmInputLowDensity0024Normal,
       "alarmInputLowDensity0025Normal": alarmInputLowDensity0025Normal,
       "alarmInputLowDensity0026Normal": alarmInputLowDensity0026Normal,
       "alarmInputLowDensity0027Normal": alarmInputLowDensity0027Normal,
       "alarmInputLowDensity0028Normal": alarmInputLowDensity0028Normal,
       "alarmInputLowDensity0029Normal": alarmInputLowDensity0029Normal,
       "alarmInputLowDensity0030Normal": alarmInputLowDensity0030Normal,
       "alarmInputLowDensity0031Normal": alarmInputLowDensity0031Normal,
       "alarmInputLowDensity0032Normal": alarmInputLowDensity0032Normal,
       "alarmInputLowDensity0033Normal": alarmInputLowDensity0033Normal,
       "alarmInputLowDensity0034Normal": alarmInputLowDensity0034Normal,
       "alarmInputLowDensity0035Normal": alarmInputLowDensity0035Normal,
       "alarmInputLowDensity0036Normal": alarmInputLowDensity0036Normal,
       "alarmInputLowDensity0037Normal": alarmInputLowDensity0037Normal,
       "alarmInputLowDensity0038Normal": alarmInputLowDensity0038Normal,
       "alarmInputLowDensity0039Normal": alarmInputLowDensity0039Normal,
       "alarmInputLowDensity0040Normal": alarmInputLowDensity0040Normal,
       "alarmInputLowDensity0041Normal": alarmInputLowDensity0041Normal,
       "alarmInputLowDensity0042Normal": alarmInputLowDensity0042Normal,
       "alarmInputLowDensity0043Normal": alarmInputLowDensity0043Normal,
       "alarmInputLowDensity0044Normal": alarmInputLowDensity0044Normal,
       "alarmInputLowDensity0045Normal": alarmInputLowDensity0045Normal,
       "alarmInputLowDensity0046Normal": alarmInputLowDensity0046Normal,
       "alarmInputLowDensity0047Normal": alarmInputLowDensity0047Normal,
       "alarmInputLowDensity0048Normal": alarmInputLowDensity0048Normal,
       "alarmInputLowDensity0049Normal": alarmInputLowDensity0049Normal,
       "alarmInputLowDensity0050Normal": alarmInputLowDensity0050Normal,
       "alarmInputLowDensity0051Normal": alarmInputLowDensity0051Normal,
       "alarmInputLowDensity0052Normal": alarmInputLowDensity0052Normal,
       "alarmInputLowDensity0053Normal": alarmInputLowDensity0053Normal,
       "alarmInputLowDensity0054Normal": alarmInputLowDensity0054Normal,
       "alarmInputLowDensity0055Normal": alarmInputLowDensity0055Normal,
       "alarmInputLowDensity0056Normal": alarmInputLowDensity0056Normal,
       "alarmInputLowDensity0057Normal": alarmInputLowDensity0057Normal,
       "alarmInputLowDensity0058Normal": alarmInputLowDensity0058Normal,
       "alarmInputLowDensity0059Normal": alarmInputLowDensity0059Normal,
       "alarmInputLowDensity0060Normal": alarmInputLowDensity0060Normal,
       "alarmInputLowDensity0061Normal": alarmInputLowDensity0061Normal,
       "alarmInputLowDensity0062Normal": alarmInputLowDensity0062Normal,
       "alarmInputLowDensity0063Normal": alarmInputLowDensity0063Normal,
       "alarmInputLowDensity0064Normal": alarmInputLowDensity0064Normal,
       "alarmInputLowDensity0065Normal": alarmInputLowDensity0065Normal,
       "alarmInputLowDensity0066Normal": alarmInputLowDensity0066Normal,
       "alarmInputLowDensity0067Normal": alarmInputLowDensity0067Normal,
       "alarmInputLowDensity0068Normal": alarmInputLowDensity0068Normal,
       "alarmInputLowDensity0069Normal": alarmInputLowDensity0069Normal,
       "alarmInputLowDensity0070Normal": alarmInputLowDensity0070Normal,
       "alarmInputLowDensity0071Normal": alarmInputLowDensity0071Normal,
       "alarmInputLowDensity0072Normal": alarmInputLowDensity0072Normal,
       "alarmInputLowDensity0073Normal": alarmInputLowDensity0073Normal,
       "alarmInputLowDensity0074Normal": alarmInputLowDensity0074Normal,
       "alarmInputLowDensity0075Normal": alarmInputLowDensity0075Normal,
       "alarmInputLowDensity0076Normal": alarmInputLowDensity0076Normal,
       "alarmInputLowDensity0077Normal": alarmInputLowDensity0077Normal,
       "alarmInputLowDensity0078Normal": alarmInputLowDensity0078Normal,
       "alarmInputLowDensity0079Normal": alarmInputLowDensity0079Normal,
       "alarmInputLowDensity0080Normal": alarmInputLowDensity0080Normal,
       "characterDep": characterDep,
       "xCharacter": xCharacter,
       "xBasic": xBasic,
       "basicBroadcast": basicBroadcast,
       "basicErrorReport": basicErrorReport,
       "basicLock": basicLock,
       "basicInactivityTimer": basicInactivityTimer,
       "basicPasswordRetryLimit": basicPasswordRetryLimit,
       "basicPrivilegedPassword": basicPrivilegedPassword,
       "basicLoginPassword": basicLoginPassword,
       "basicLoginPrompt": basicLoginPrompt,
       "basicWelcome": basicWelcome,
       "basicActivePorts": basicActivePorts,
       "basicActivePortsHigh": basicActivePortsHigh,
       "basicActiveUsers": basicActiveUsers,
       "basicActiveUsersHigh": basicActiveUsersHigh,
       "basicSessions": basicSessions,
       "basicSessionsHigh": basicSessionsHigh,
       "basicSessionsLimit": basicSessionsLimit,
       "basicPortTable": basicPortTable,
       "basicPortEntry": basicPortEntry,
       "basicPortIndex": basicPortIndex,
       "basicPortDefaultDestAction": basicPortDefaultDestAction,
       "basicPortDefaultDestProtocol": basicPortDefaultDestProtocol,
       "basicPortDefaultDestName": basicPortDefaultDestName,
       "basicPortDefaultDestLATNodeName": basicPortDefaultDestLATNodeName,
       "basicPortDefaultDestLATPortName": basicPortDefaultDestLATPortName,
       "basicPortAutoConnect": basicPortAutoConnect,
       "basicPortAutoLogin": basicPortAutoLogin,
       "basicPortBroadcast": basicPortBroadcast,
       "basicPortConnectResume": basicPortConnectResume,
       "basicPortDialup": basicPortDialup,
       "basicPortIdleTimeout": basicPortIdleTimeout,
       "basicPortInactivityLogout": basicPortInactivityLogout,
       "basicPortLossNotification": basicPortLossNotification,
       "basicPortMessageCodes": basicPortMessageCodes,
       "basicPortMultisessions": basicPortMultisessions,
       "basicPortDefaultUserName": basicPortDefaultUserName,
       "basicPortVerification": basicPortVerification,
       "basicPortDefaultProtocol": basicPortDefaultProtocol,
       "basicPortLogins": basicPortLogins,
       "basicPortRemoteSessions": basicPortRemoteSessions,
       "basicPortIdleTimeouts": basicPortIdleTimeouts,
       "basicPortStatus": basicPortStatus,
       "basicPortLastInCharacter": basicPortLastInCharacter,
       "basicPortLastOutCharacter": basicPortLastOutCharacter,
       "basicPortActiveUserName": basicPortActiveUserName,
       "basicPortDefaultSessionMode": basicPortDefaultSessionMode,
       "basicPortZero": basicPortZero,
       "basicPortZeroTime": basicPortZeroTime,
       "basicPortUnixCommands": basicPortUnixCommands,
       "basicPortSessionMode": basicPortSessionMode,
       "basicPortRemoteDisconnectNotify": basicPortRemoteDisconnectNotify,
       "basicPortDefaultDestControlled": basicPortDefaultDestControlled,
       "basicPortControlledPortLogin": basicPortControlledPortLogin,
       "basicPortControlledPortLogout": basicPortControlledPortLogout,
       "basicPortControlledSessionInitialize": basicPortControlledSessionInitialize,
       "basicPortControlledSessionTerminate": basicPortControlledSessionTerminate,
       "basicPortRloginTransparentMode": basicPortRloginTransparentMode,
       "basicPortLoginDuration": basicPortLoginDuration,
       "basicPortOutboundSecurity": basicPortOutboundSecurity,
       "basicPortXonTimer": basicPortXonTimer,
       "basicPortDefaultDedicatedSessionType": basicPortDefaultDedicatedSessionType,
       "basicPortIdleTimeReceive": basicPortIdleTimeReceive,
       "basicPortIdleTimeTransmit": basicPortIdleTimeTransmit,
       "basicPortZeroDisconnectSession": basicPortZeroDisconnectSession,
       "basicPortConsolePort": basicPortConsolePort,
       "basicPortLoginPassword": basicPortLoginPassword,
       "basicPortSensor": basicPortSensor,
       "basicPortAlarmControl": basicPortAlarmControl,
       "basicPortCommandLogging": basicPortCommandLogging,
       "basicPortBreakSequence": basicPortBreakSequence,
       "basicPortTl1Mode": basicPortTl1Mode,
       "basicPortTl1Console": basicPortTl1Console,
       "basicPortFallThrough": basicPortFallThrough,
       "basicPortCommandLoggingSuppressControlCharacters": basicPortCommandLoggingSuppressControlCharacters,
       "basicPortDataLogging": basicPortDataLogging,
       "basicPortDataLoggingSuppressControlCharacters": basicPortDataLoggingSuppressControlCharacters,
       "basicPortOnboardSecurity": basicPortOnboardSecurity,
       "basicPortFallBack": basicPortFallBack,
       "basicPortAlarmMaster": basicPortAlarmMaster,
       "basicPortAlarmMasterAccounting": basicPortAlarmMasterAccounting,
       "basicPortAlarmMasterAudibleAlarm": basicPortAlarmMasterAudibleAlarm,
       "basicPortAlarmMasterFixTime": basicPortAlarmMasterFixTime,
       "basicPortAlarmMasterLcdDisplayString": basicPortAlarmMasterLcdDisplayString,
       "basicPortAlarmMasterReboot": basicPortAlarmMasterReboot,
       "basicPortAlarmMasterUpdateFirmwareHost": basicPortAlarmMasterUpdateFirmwareHost,
       "basicPortAlarmMasterUpdateFirmwareFileName": basicPortAlarmMasterUpdateFirmwareFileName,
       "basicPortAlarmMasterUpdateFirmware": basicPortAlarmMasterUpdateFirmware,
       "basicPortAlarmMasterStatus": basicPortAlarmMasterStatus,
       "basicPortAlarmMasterFaultSeverity": basicPortAlarmMasterFaultSeverity,
       "basicPortPowerMaster": basicPortPowerMaster,
       "basicPortPowerMasterTimeDelay": basicPortPowerMasterTimeDelay,
       "basicPortPowerMasterSwitch": basicPortPowerMasterSwitch,
       "basicPortPowerMasterModel": basicPortPowerMasterModel,
       "basicPortPowerMasterSerialNumber": basicPortPowerMasterSerialNumber,
       "basicPortPowerMasterFirmware": basicPortPowerMasterFirmware,
       "basicPortLockout": basicPortLockout,
       "basicPortAsciiToTrapTranslation": basicPortAsciiToTrapTranslation,
       "basicPortAsciiToTrapTranslationTrapSeverity": basicPortAsciiToTrapTranslationTrapSeverity,
       "basicPortAsciiToTrapTranslationMessages": basicPortAsciiToTrapTranslationMessages,
       "basicPortAsciiToTrapTranslationLastMessage": basicPortAsciiToTrapTranslationLastMessage,
       "basicPortPowerMasterAlarmSeverity": basicPortPowerMasterAlarmSeverity,
       "basicPortPowerMasterDeviceStatus": basicPortPowerMasterDeviceStatus,
       "basicPortBuffering": basicPortBuffering,
       "basicPortLogFacilityLevel": basicPortLogFacilityLevel,
       "basicPortPppDialBackup": basicPortPppDialBackup,
       "basicPortPppDialBackupNumber": basicPortPppDialBackupNumber,
       "basicPortPppDialBackupRedialTimer": basicPortPppDialBackupRedialTimer,
       "basicPortPppDialBackupRedialRetries": basicPortPppDialBackupRedialRetries,
       "basicPortPppDialBackupDisconnectTimer": basicPortPppDialBackupDisconnectTimer,
       "basicPortPppDialBackupLocalAddress": basicPortPppDialBackupLocalAddress,
       "basicPortPppDialBackupDestinationAddress": basicPortPppDialBackupDestinationAddress,
       "basicPortPppDialBackupAddresses": basicPortPppDialBackupAddresses,
       "basicSerialPortTable": basicSerialPortTable,
       "basicSerialPortEntry": basicSerialPortEntry,
       "basicSerialPortIndex": basicSerialPortIndex,
       "basicSerialPortBreak": basicSerialPortBreak,
       "basicSerialPortInterrupts": basicSerialPortInterrupts,
       "basicSerialPortNoLoss": basicSerialPortNoLoss,
       "basicSerialPortPause": basicSerialPortPause,
       "basicSerialPortPrompt": basicSerialPortPrompt,
       "basicSerialPortTerminalType": basicSerialPortTerminalType,
       "basicSerialPortTypeaheadLimit": basicSerialPortTypeaheadLimit,
       "basicSerialPortBackwardSwitch": basicSerialPortBackwardSwitch,
       "basicSerialPortForwardSwitch": basicSerialPortForwardSwitch,
       "basicSerialPortLocalSwitch": basicSerialPortLocalSwitch,
       "basicSerialPortModemControl": basicSerialPortModemControl,
       "basicSerialPortSignalCheck": basicSerialPortSignalCheck,
       "basicSerialPortDSRLogout": basicSerialPortDSRLogout,
       "basicSerialPortDSRObserve": basicSerialPortDSRObserve,
       "basicSerialPortDCDTimeout": basicSerialPortDCDTimeout,
       "basicSerialPortDTRAssert": basicSerialPortDTRAssert,
       "basicSerialPortLimitedCommands": basicSerialPortLimitedCommands,
       "basicSerialPortLimitedView": basicSerialPortLimitedView,
       "basicSerialPortPassword": basicSerialPortPassword,
       "basicSerialPortLineEditor": basicSerialPortLineEditor,
       "basicSerialPortLineEditorBackspace": basicSerialPortLineEditorBackspace,
       "basicSerialPortLineEditorBeginning": basicSerialPortLineEditorBeginning,
       "basicSerialPortLineEditorCancel": basicSerialPortLineEditorCancel,
       "basicSerialPortLineEditorDeleteBeginning": basicSerialPortLineEditorDeleteBeginning,
       "basicSerialPortLineEditorDeleteLine": basicSerialPortLineEditorDeleteLine,
       "basicSerialPortLineEditorEnd": basicSerialPortLineEditorEnd,
       "basicSerialPortLineEditorForward": basicSerialPortLineEditorForward,
       "basicSerialPortLineEditorInsertToggle": basicSerialPortLineEditorInsertToggle,
       "basicSerialPortLineEditorNextLine": basicSerialPortLineEditorNextLine,
       "basicSerialPortLineEditorPreviousLine": basicSerialPortLineEditorPreviousLine,
       "basicSerialPortLineEditorQuotingCharacter": basicSerialPortLineEditorQuotingCharacter,
       "basicSerialPortLineEditorRedisplay": basicSerialPortLineEditorRedisplay,
       "basicSerialPortQuadartReceiveDiscard": basicSerialPortQuadartReceiveDiscard,
       "basicSerialPortAPDProtocols": basicSerialPortAPDProtocols,
       "basicSerialPortAPDTimeout": basicSerialPortAPDTimeout,
       "basicSerialPortAPDDefaultProtocol": basicSerialPortAPDDefaultProtocol,
       "basicSerialPortUsernameCharSet": basicSerialPortUsernameCharSet,
       "basicSerialPortAutoHangup": basicSerialPortAutoHangup,
       "basicSerialPortCommandSize": basicSerialPortCommandSize,
       "basicSerialPortAutoProtocolDetectPrompt": basicSerialPortAutoProtocolDetectPrompt,
       "basicSerialPortUsernamePrompt": basicSerialPortUsernamePrompt,
       "basicSerialPortPasswordPrompt": basicSerialPortPasswordPrompt,
       "basicSerialPortAutoProtocolDetectSecurityInteractiveOnly": basicSerialPortAutoProtocolDetectSecurityInteractiveOnly,
       "basicSerialPortDedicatedUserData": basicSerialPortDedicatedUserData,
       "basicSerialPortIpAutoDiscovery": basicSerialPortIpAutoDiscovery,
       "basicSerialPortDedicatedKickStartData": basicSerialPortDedicatedKickStartData,
       "basicSerialPortBreakLength": basicSerialPortBreakLength,
       "basicSerialPortRotaryRoundRobin": basicSerialPortRotaryRoundRobin,
       "basicSerialPortWelcomeBeforeAuthentication": basicSerialPortWelcomeBeforeAuthentication,
       "basicSerialPortGatewayAutoDiscovery": basicSerialPortGatewayAutoDiscovery,
       "basicSerialPortSubnetAutoDiscovery": basicSerialPortSubnetAutoDiscovery,
       "basicSerialPortRaiseLowerDtr": basicSerialPortRaiseLowerDtr,
       "basicSerialPortRaiseControlDtr": basicSerialPortRaiseControlDtr,
       "basicSerialPortIpConfigureBootp": basicSerialPortIpConfigureBootp,
       "basicConsoleLogoutDisconnect": basicConsoleLogoutDisconnect,
       "basicControlledPorts": basicControlledPorts,
       "basicPortSessionTable": basicPortSessionTable,
       "basicPortSessEntry": basicPortSessEntry,
       "basicPortPortIndex": basicPortPortIndex,
       "basicPortSessIndex": basicPortSessIndex,
       "basicSessControlled": basicSessControlled,
       "basicPortSessEncryption": basicPortSessEncryption,
       "basicTemperatureUnits": basicTemperatureUnits,
       "basicEnvironmentalManagerCircuitBreaker": basicEnvironmentalManagerCircuitBreaker,
       "basicContactClosureOrAlarmInputTable": basicContactClosureOrAlarmInputTable,
       "basicContactClosureOrAlarmInputEntry": basicContactClosureOrAlarmInputEntry,
       "basicContactClosureOrAlarmInputValue": basicContactClosureOrAlarmInputValue,
       "basicContactClosureOrAlarmInputName": basicContactClosureOrAlarmInputName,
       "basicContactClosureOrAlarmInputTrapEnable": basicContactClosureOrAlarmInputTrapEnable,
       "basicContactClosureOrAlarmInputFaultSeverity": basicContactClosureOrAlarmInputFaultSeverity,
       "basicContactClosureOrAlarmInputFaultState": basicContactClosureOrAlarmInputFaultState,
       "basicContactClosureOrAlarmInputStatus": basicContactClosureOrAlarmInputStatus,
       "basicContactClosureOrAlarmInputZone": basicContactClosureOrAlarmInputZone,
       "basicContactClosureOrAlarmInputRelatedEquipment": basicContactClosureOrAlarmInputRelatedEquipment,
       "basicContactClosureOrAlarmInputSiteId": basicContactClosureOrAlarmInputSiteId,
       "basicContactClosureOrAlarmInputIndex": basicContactClosureOrAlarmInputIndex,
       "basicContactClosureOrAlarmInputManufacturer": basicContactClosureOrAlarmInputManufacturer,
       "basicContactClosureOrAlarmInputModel": basicContactClosureOrAlarmInputModel,
       "basicPowerOutletTable": basicPowerOutletTable,
       "basicPowerOutletEntry": basicPowerOutletEntry,
       "basicPowerOutletOnOff": basicPowerOutletOnOff,
       "basicPowerOutletReboot": basicPowerOutletReboot,
       "basicPowerOutletName": basicPowerOutletName,
       "basicPowerOutletRedundant": basicPowerOutletRedundant,
       "basicPowerOutletConsoleName": basicPowerOutletConsoleName,
       "basicPowerOutletHighCurrent": basicPowerOutletHighCurrent,
       "basicPowerOutletIndex": basicPowerOutletIndex,
       "basicTemperatureHumiditySensor": basicTemperatureHumiditySensor,
       "basicTemperatureSensorTable": basicTemperatureSensorTable,
       "basicTemperatureSensorEntry": basicTemperatureSensorEntry,
       "basicTempTrapHighThreshold": basicTempTrapHighThreshold,
       "basicTempTrapLowThreshold": basicTempTrapLowThreshold,
       "basicTemperatureSensor": basicTemperatureSensor,
       "basicTemperatureValue": basicTemperatureValue,
       "basicTemperatureAlarmSeverity": basicTemperatureAlarmSeverity,
       "basicTemperatureAlarmStatus": basicTemperatureAlarmStatus,
       "basicTemperatureHumiditySensorName": basicTemperatureHumiditySensorName,
       "basicTemperatureSensorIndex": basicTemperatureSensorIndex,
       "basicHumiditySensorTable": basicHumiditySensorTable,
       "basicHumiditySensorEntry": basicHumiditySensorEntry,
       "basicHumidityTrapHighThreshold": basicHumidityTrapHighThreshold,
       "basicHumidityTrapLowThreshold": basicHumidityTrapLowThreshold,
       "basicHumiditySensor": basicHumiditySensor,
       "basicHumidityValue": basicHumidityValue,
       "basicHumidityAlarmSeverity": basicHumidityAlarmSeverity,
       "basicHumidityAlarmStatus": basicHumidityAlarmStatus,
       "basicHumiditySensorIndex": basicHumiditySensorIndex,
       "basicControlSignalTable": basicControlSignalTable,
       "basicControlSignalEntry": basicControlSignalEntry,
       "basicControlSignalValue": basicControlSignalValue,
       "basicControlSignalIndex": basicControlSignalIndex,
       "basicPowerAlarmTimer": basicPowerAlarmTimer,
       "basicControlOutputTable": basicControlOutputTable,
       "basicControlOutputEntry": basicControlOutputEntry,
       "basicControlOutputSignalDtrRts": basicControlOutputSignalDtrRts,
       "basicControlOutputName": basicControlOutputName,
       "basicControlOutputIndex": basicControlOutputIndex,
       "basicPowerStatusFuseA": basicPowerStatusFuseA,
       "basicPowerStatusFuseB": basicPowerStatusFuseB,
       "basicPowerSupplyStatusA": basicPowerSupplyStatusA,
       "basicPowerSupplyStatusB": basicPowerSupplyStatusB,
       "basicPortTrapTable": basicPortTrapTable,
       "basicPortTrapEntry": basicPortTrapEntry,
       "basicPortTrapIndex": basicPortTrapIndex,
       "basicPortSignalName": basicPortSignalName,
       "basicPortTrapStatus": basicPortTrapStatus,
       "basicAlarmMasterInputTable": basicAlarmMasterInputTable,
       "basicAlarmMasterInputEntry": basicAlarmMasterInputEntry,
       "basicAlarmMasterInputPort": basicAlarmMasterInputPort,
       "basicAlarmMasterInputSlot": basicAlarmMasterInputSlot,
       "basicAlarmMasterInputPoint": basicAlarmMasterInputPoint,
       "basicAlarmMasterInputName": basicAlarmMasterInputName,
       "basicAlarmMasterInputTrapEnable": basicAlarmMasterInputTrapEnable,
       "basicAlarmMasterControlOutputSignal": basicAlarmMasterControlOutputSignal,
       "basicAlarmMasterInputEnable": basicAlarmMasterInputEnable,
       "basicAlarmMasterInputDebounceInterval": basicAlarmMasterInputDebounceInterval,
       "basicAlarmMasterInputFaultSeverity": basicAlarmMasterInputFaultSeverity,
       "basicAlarmMasterInputFaultState": basicAlarmMasterInputFaultState,
       "basicAlarmMasterInputStatus": basicAlarmMasterInputStatus,
       "basicAlarmMasterInputValue": basicAlarmMasterInputValue,
       "basicAlarmMasterDisplay": basicAlarmMasterDisplay,
       "basicAlarmMasterInputZone": basicAlarmMasterInputZone,
       "basicAlarmMasterInputRelatedEquipment": basicAlarmMasterInputRelatedEquipment,
       "basicAlarmMasterInputSiteId": basicAlarmMasterInputSiteId,
       "basicAlarmMasterInputManufacturer": basicAlarmMasterInputManufacturer,
       "basicAlarmMasterInputModel": basicAlarmMasterInputModel,
       "basicPowerMasterOutletTable": basicPowerMasterOutletTable,
       "basicPowerMasterOutletEntry": basicPowerMasterOutletEntry,
       "basicPowerMasterPortIndex": basicPowerMasterPortIndex,
       "basicPowerMasterOutletIndex": basicPowerMasterOutletIndex,
       "basicPowerMasterOutletName": basicPowerMasterOutletName,
       "basicPowerMasterOutletState": basicPowerMasterOutletState,
       "basicPowerMasterOutletAmperageStatus": basicPowerMasterOutletAmperageStatus,
       "basicControlOutputRelayTable": basicControlOutputRelayTable,
       "basicControlOutputRelayEntry": basicControlOutputRelayEntry,
       "basicControlOutputRelayIndex": basicControlOutputRelayIndex,
       "basicControlOutputRelayName": basicControlOutputRelayName,
       "basicControlOutputRelayState": basicControlOutputRelayState,
       "basicControlOutputRelayStatus": basicControlOutputRelayStatus,
       "basicAutoProtocolDetectMessage": basicAutoProtocolDetectMessage,
       "xQueue": xQueue,
       "queueLimit": queueLimit,
       "queueHigh": queueHigh,
       "queueNumber": queueNumber,
       "queueTable": queueTable,
       "queueEntry": queueEntry,
       "queueJob": queueJob,
       "queueStatus": queueStatus,
       "queueSourceName": queueSourceName,
       "queueServiceName": queueServiceName,
       "queueServicePortIndex": queueServicePortIndex,
       "queueServicePortName": queueServicePortName,
       "queuePortTable": queuePortTable,
       "queuePortEntry": queuePortEntry,
       "queuePortIndex": queuePortIndex,
       "queuePortQueuing": queuePortQueuing,
       "xMenu": xMenu,
       "menuNumber": menuNumber,
       "menuContinuePrompt": menuContinuePrompt,
       "menuSelectionPrompt": menuSelectionPrompt,
       "menuTable": menuTable,
       "menuEntry": menuEntry,
       "menuIndex": menuIndex,
       "menuStatus": menuStatus,
       "menuText": menuText,
       "menuCommand": menuCommand,
       "menuPortTable": menuPortTable,
       "menuPortEntry": menuPortEntry,
       "menuPortIndex": menuPortIndex,
       "menuPortMenuStatus": menuPortMenuStatus,
       "menuPortNestedMenuStatus": menuPortNestedMenuStatus,
       "menuPortNestedMenuPrivilege": menuPortNestedMenuPrivilege,
       "menuPortNestedTopLevel": menuPortNestedTopLevel,
       "menuNestedName": menuNestedName,
       "menuNestedScriptMaximum": menuNestedScriptMaximum,
       "menuNestedSystemName": menuNestedSystemName,
       "menuNestedEthernet": menuNestedEthernet,
       "xNetLogin": xNetLogin,
       "netLoginNumber": netLoginNumber,
       "netLoginServerTable": netLoginServerTable,
       "netLoginServerEntry": netLoginServerEntry,
       "netLoginServerName": netLoginServerName,
       "netLoginServerStatus": netLoginServerStatus,
       "netLoginServerPath": netLoginServerPath,
       "netLoginServerSeparator": netLoginServerSeparator,
       "netLoginPortTable": netLoginPortTable,
       "netLoginPortEntry": netLoginPortEntry,
       "netLoginPortIndex": netLoginPortIndex,
       "netLoginPortScriptUse": netLoginPortScriptUse,
       "netLoginPortScriptEcho": netLoginPortScriptEcho,
       "netLoginPortLoaderAddressType": netLoginPortLoaderAddressType,
       "netLoginPortLoaderAddress": netLoginPortLoaderAddress,
       "netLoginPortLoaderFile": netLoginPortLoaderFile,
       "netLoginPortExecuteFile": netLoginPortExecuteFile,
       "xDial": xDial,
       "dialPortTable": dialPortTable,
       "dialPortEntry": dialPortEntry,
       "dialPortIndex": dialPortIndex,
       "dialPortDialback": dialPortDialback,
       "dialPortDialbackTimeout": dialPortDialbackTimeout,
       "dialPortDialout": dialPortDialout,
       "dialPortDialbackNoUsername": dialPortDialbackNoUsername,
       "xSessionLog": xSessionLog,
       "sessionLogLimit": sessionLogLimit,
       "sessionLogTable": sessionLogTable,
       "sessionLogEntry": sessionLogEntry,
       "sessionLogIndex": sessionLogIndex,
       "sessionLogConnectionID": sessionLogConnectionID,
       "sessionLogPort": sessionLogPort,
       "sessionLogEvent": sessionLogEvent,
       "sessionLogEventDetail": sessionLogEventDetail,
       "sessionLogUserName": sessionLogUserName,
       "sessionLogRemoteName": sessionLogRemoteName,
       "sessionLogConnectTime": sessionLogConnectTime,
       "sessionLogDisconnectTime": sessionLogDisconnectTime,
       "sessionLogInCharacters": sessionLogInCharacters,
       "sessionLogOutCharacters": sessionLogOutCharacters,
       "sessionLogVerboseEvent": sessionLogVerboseEvent,
       "sessionLogX25Direction": sessionLogX25Direction,
       "sessionLogVerboseMessage": sessionLogVerboseMessage,
       "sessionLogX25CallerAddress": sessionLogX25CallerAddress,
       "sessionLogX25CalledAddress": sessionLogX25CalledAddress,
       "sessionLogX25DisconnectCause": sessionLogX25DisconnectCause,
       "sessionLogX25DisconnectDiagnostic": sessionLogX25DisconnectDiagnostic,
       "sessionLogHostType": sessionLogHostType,
       "sessionLogHostAddress": sessionLogHostAddress,
       "sessionLogVerbose": sessionLogVerbose,
       "sessionLogPriority": sessionLogPriority,
       "sessionLogEmpty": sessionLogEmpty,
       "sessionLogFacility": sessionLogFacility,
       "sessionLogReliable": sessionLogReliable,
       "sessionLogHostSecondaryType": sessionLogHostSecondaryType,
       "sessionLogHostSecondaryAddress": sessionLogHostSecondaryAddress,
       "sessionLogZeroAccountingAll": sessionLogZeroAccountingAll,
       "sessionLogZeroCommandLogging": sessionLogZeroCommandLogging,
       "sessionLogTl1AutonomousLogSize": sessionLogTl1AutonomousLogSize,
       "sessionLogTl1CommandLogSize": sessionLogTl1CommandLogSize,
       "sessionLogZeroDataLogging": sessionLogZeroDataLogging,
       "sessionLogZeroAlarmLogging": sessionLogZeroAlarmLogging,
       "xCcl": xCcl,
       "cclParsedScriptTable": cclParsedScriptTable,
       "cclParsedScriptEntry": cclParsedScriptEntry,
       "cclScriptName": cclScriptName,
       "cclScriptControl": cclScriptControl,
       "cclPortTable": cclPortTable,
       "cclPortEntry": cclPortEntry,
       "cclPortCclName": cclPortCclName,
       "cclPortModemAudible": cclPortModemAudible,
       "xBroadcastGroup": xBroadcastGroup,
       "broadcastGroupTable": broadcastGroupTable,
       "broadcastGroupEntry": broadcastGroupEntry,
       "broadcastGroupIndex": broadcastGroupIndex,
       "broadcastGroupStatus": broadcastGroupStatus,
       "broadcastGroupMaster": broadcastGroupMaster,
       "broadcastGroupSlaves": broadcastGroupSlaves,
       "broadcastGroupSlavesBroadcastOnly": broadcastGroupSlavesBroadcastOnly,
       "broadcastGroupSlaveTcpPort": broadcastGroupSlaveTcpPort,
       "broadcastGroupSlaveTcpBroadcastOnly": broadcastGroupSlaveTcpBroadcastOnly,
       "xPingHosts": xPingHosts,
       "pingHostsTable": pingHostsTable,
       "pingHostsEntry": pingHostsEntry,
       "icmpPingHostIndex": icmpPingHostIndex,
       "icmpPingHostAddress": icmpPingHostAddress,
       "icmpPingHostDescription": icmpPingHostDescription,
       "icmpPingHostNotificationType": icmpPingHostNotificationType,
       "icmpPingHostPollingInterval": icmpPingHostPollingInterval,
       "icmpPingHostMaximumRetries": icmpPingHostMaximumRetries,
       "icmpPingHostTrapSeverityLevel": icmpPingHostTrapSeverityLevel,
       "icmpPingHostStatus": icmpPingHostStatus}
)
