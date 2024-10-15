# SNMP MIB module (DECserver-Accounting-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DECserver-Accounting-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:45 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 enterprises,
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
    "enterprises",
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

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1)
)
_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 36, 2)
)
_Mib_extensions_1_ObjectIdentity = ObjectIdentity
mib_extensions_1 = _Mib_extensions_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18)
)
_DecServeraccounting_ObjectIdentity = ObjectIdentity
decServeraccounting = _DecServeraccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12)
)
_AcctSystem_ObjectIdentity = ObjectIdentity
acctSystem = _AcctSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1)
)


class _AcctConsole_Type(Integer32):
    """Custom type acctConsole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AcctConsole_Type.__name__ = "Integer32"
_AcctConsole_Object = MibScalar
acctConsole = _AcctConsole_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 1),
    _AcctConsole_Type()
)
acctConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctConsole.setStatus("mandatory")


class _AcctAdminLogSize_Type(Integer32):
    """Custom type acctAdminLogSize based on Integer32"""
    defaultValue = 4

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
        *(("none", 1),
          ("size128K", 7),
          ("size16K", 4),
          ("size256K", 8),
          ("size32K", 5),
          ("size4K", 2),
          ("size512K", 9),
          ("size64K", 6),
          ("size8K", 3))
    )


_AcctAdminLogSize_Type.__name__ = "Integer32"
_AcctAdminLogSize_Object = MibScalar
acctAdminLogSize = _AcctAdminLogSize_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 2),
    _AcctAdminLogSize_Type()
)
acctAdminLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctAdminLogSize.setStatus("mandatory")


class _AcctOperLogSize_Type(Integer32):
    """Custom type acctOperLogSize based on Integer32"""
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
        *(("none", 1),
          ("size128K", 7),
          ("size16K", 4),
          ("size256K", 8),
          ("size32K", 5),
          ("size4K", 2),
          ("size512K", 9),
          ("size64K", 6),
          ("size8K", 3))
    )


_AcctOperLogSize_Type.__name__ = "Integer32"
_AcctOperLogSize_Object = MibScalar
acctOperLogSize = _AcctOperLogSize_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 3),
    _AcctOperLogSize_Type()
)
acctOperLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctOperLogSize.setStatus("mandatory")


class _AcctThreshold_Type(Integer32):
    """Custom type acctThreshold based on Integer32"""
    defaultValue = 1

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
        *(("eighth", 5),
          ("end", 2),
          ("half", 3),
          ("none", 1),
          ("quarter", 4))
    )


_AcctThreshold_Type.__name__ = "Integer32"
_AcctThreshold_Object = MibScalar
acctThreshold = _AcctThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 4),
    _AcctThreshold_Type()
)
acctThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctThreshold.setStatus("mandatory")
_AcctTable_Object = MibTable
acctTable = _AcctTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2)
)
if mibBuilder.loadTexts:
    acctTable.setStatus("mandatory")
_AcctEntry_Object = MibTableRow
acctEntry = _AcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1)
)
acctEntry.setIndexNames(
    (0, "DECserver-Accounting-MIB", "acctEntryNonce1"),
    (0, "DECserver-Accounting-MIB", "acctEntryNonce2"),
)
if mibBuilder.loadTexts:
    acctEntry.setStatus("mandatory")


class _AcctEntryNonce1_Type(Integer32):
    """Custom type acctEntryNonce1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcctEntryNonce1_Type.__name__ = "Integer32"
_AcctEntryNonce1_Object = MibTableColumn
acctEntryNonce1 = _AcctEntryNonce1_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 1),
    _AcctEntryNonce1_Type()
)
acctEntryNonce1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryNonce1.setStatus("mandatory")


class _AcctEntryNonce2_Type(Integer32):
    """Custom type acctEntryNonce2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcctEntryNonce2_Type.__name__ = "Integer32"
_AcctEntryNonce2_Object = MibTableColumn
acctEntryNonce2 = _AcctEntryNonce2_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 2),
    _AcctEntryNonce2_Type()
)
acctEntryNonce2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryNonce2.setStatus("mandatory")
_AcctEntryTime_Type = TimeTicks
_AcctEntryTime_Object = MibTableColumn
acctEntryTime = _AcctEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 3),
    _AcctEntryTime_Type()
)
acctEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryTime.setStatus("mandatory")


class _AcctEntryEvent_Type(Integer32):
    """Custom type acctEntryEvent based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("communityFail", 11),
          ("communityModified", 17),
          ("kerberosPasswordFail", 6),
          ("logIn", 2),
          ("logOut", 3),
          ("loginPasswordFail", 9),
          ("loginPasswordModified", 14),
          ("maintenacePasswordModified", 13),
          ("maintenancePasswordFail", 8),
          ("other", 1),
          ("privilegeLevelModified", 16),
          ("privilegedPasswordFail", 7),
          ("privilegedPasswordModified", 12),
          ("remotePasswordFail", 10),
          ("remotePasswordModified", 15),
          ("sessionConnect", 4),
          ("sessionDisconnect", 5))
    )


_AcctEntryEvent_Type.__name__ = "Integer32"
_AcctEntryEvent_Object = MibScalar
acctEntryEvent = _AcctEntryEvent_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 4),
    _AcctEntryEvent_Type()
)
acctEntryEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryEvent.setStatus("mandatory")
_AcctEntryPort_Type = Integer32
_AcctEntryPort_Object = MibTableColumn
acctEntryPort = _AcctEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 5),
    _AcctEntryPort_Type()
)
acctEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryPort.setStatus("mandatory")
_AcctEntryUser_Type = DisplayString
_AcctEntryUser_Object = MibTableColumn
acctEntryUser = _AcctEntryUser_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 6),
    _AcctEntryUser_Type()
)
acctEntryUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryUser.setStatus("mandatory")
_AcctEntrySessionId_Type = Integer32
_AcctEntrySessionId_Object = MibTableColumn
acctEntrySessionId = _AcctEntrySessionId_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 7),
    _AcctEntrySessionId_Type()
)
acctEntrySessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntrySessionId.setStatus("mandatory")


class _AcctEntryProtocol_Type(Integer32):
    """Custom type acctEntryProtocol based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("autolink", 9),
          ("lat", 2),
          ("mop", 6),
          ("none", 1),
          ("other", 11),
          ("ping", 5),
          ("ppp", 7),
          ("slip", 4),
          ("snmp-ip", 10),
          ("telnet", 3),
          ("tn3270", 8))
    )


_AcctEntryProtocol_Type.__name__ = "Integer32"
_AcctEntryProtocol_Object = MibTableColumn
acctEntryProtocol = _AcctEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 8),
    _AcctEntryProtocol_Type()
)
acctEntryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryProtocol.setStatus("mandatory")


class _AcctEntryAccess_Type(Integer32):
    """Custom type acctEntryAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("notApplicable", 1),
          ("remote", 3))
    )


_AcctEntryAccess_Type.__name__ = "Integer32"
_AcctEntryAccess_Object = MibTableColumn
acctEntryAccess = _AcctEntryAccess_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 9),
    _AcctEntryAccess_Type()
)
acctEntryAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryAccess.setStatus("mandatory")
_AcctEntryPeer_Type = DisplayString
_AcctEntryPeer_Object = MibTableColumn
acctEntryPeer = _AcctEntryPeer_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 10),
    _AcctEntryPeer_Type()
)
acctEntryPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryPeer.setStatus("mandatory")


class _AcctEntryReason_Type(Integer32):
    """Custom type acctEntryReason based on Integer32"""
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
        *(("error", 3),
          ("normal", 2),
          ("notApplicable", 1),
          ("other", 4))
    )


_AcctEntryReason_Type.__name__ = "Integer32"
_AcctEntryReason_Object = MibTableColumn
acctEntryReason = _AcctEntryReason_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 11),
    _AcctEntryReason_Type()
)
acctEntryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryReason.setStatus("mandatory")
_AcctEntrySentBytes_Type = Counter32
_AcctEntrySentBytes_Object = MibTableColumn
acctEntrySentBytes = _AcctEntrySentBytes_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 12),
    _AcctEntrySentBytes_Type()
)
acctEntrySentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntrySentBytes.setStatus("mandatory")
_AcctEntryReceivedBytes_Type = Counter32
_AcctEntryReceivedBytes_Object = MibTableColumn
acctEntryReceivedBytes = _AcctEntryReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 13),
    _AcctEntryReceivedBytes_Type()
)
acctEntryReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctEntryReceivedBytes.setStatus("mandatory")
_AcctTraps_ObjectIdentity = ObjectIdentity
acctTraps = _AcctTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 3)
)

# Managed Objects groups


# Notification objects

acctThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 3, 0, 1)
)
acctThresholdExceeded.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("DECserver-Accounting-MIB", "acctThreshold"))
)
if mibBuilder.loadTexts:
    acctThresholdExceeded.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DECserver-Accounting-MIB",
    **{"private": private,
       "dec": dec,
       "ema": ema,
       "mib-extensions-1": mib_extensions_1,
       "decServeraccounting": decServeraccounting,
       "acctSystem": acctSystem,
       "acctConsole": acctConsole,
       "acctAdminLogSize": acctAdminLogSize,
       "acctOperLogSize": acctOperLogSize,
       "acctThreshold": acctThreshold,
       "acctTable": acctTable,
       "acctEntry": acctEntry,
       "acctEntryNonce1": acctEntryNonce1,
       "acctEntryNonce2": acctEntryNonce2,
       "acctEntryTime": acctEntryTime,
       "acctEntryEvent": acctEntryEvent,
       "acctEntryPort": acctEntryPort,
       "acctEntryUser": acctEntryUser,
       "acctEntrySessionId": acctEntrySessionId,
       "acctEntryProtocol": acctEntryProtocol,
       "acctEntryAccess": acctEntryAccess,
       "acctEntryPeer": acctEntryPeer,
       "acctEntryReason": acctEntryReason,
       "acctEntrySentBytes": acctEntrySentBytes,
       "acctEntryReceivedBytes": acctEntryReceivedBytes,
       "acctTraps": acctTraps,
       "acctThresholdExceeded": acctThresholdExceeded}
)
