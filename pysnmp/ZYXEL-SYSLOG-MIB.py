# SNMP MIB module (ZYXEL-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:53 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelSysLog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelSysLogSetup_ObjectIdentity = ObjectIdentity
zyxelSysLogSetup = _ZyxelSysLogSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1)
)
_ZySysLogState_Type = EnabledStatus
_ZySysLogState_Object = MibScalar
zySysLogState = _ZySysLogState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 1),
    _ZySysLogState_Type()
)
zySysLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysLogState.setStatus("current")
_ZyxelSysLogTypeTable_Object = MibTable
zyxelSysLogTypeTable = _ZyxelSysLogTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelSysLogTypeTable.setStatus("current")
_ZyxelSysLogTypeEntry_Object = MibTableRow
zyxelSysLogTypeEntry = _ZyxelSysLogTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1)
)
zyxelSysLogTypeEntry.setIndexNames(
    (0, "ZYXEL-SYSLOG-MIB", "zySysLogTypeIndex"),
)
if mibBuilder.loadTexts:
    zyxelSysLogTypeEntry.setStatus("current")
_ZySysLogTypeIndex_Type = Integer32
_ZySysLogTypeIndex_Object = MibTableColumn
zySysLogTypeIndex = _ZySysLogTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 1),
    _ZySysLogTypeIndex_Type()
)
zySysLogTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySysLogTypeIndex.setStatus("current")
_ZySysLogTypeName_Type = DisplayString
_ZySysLogTypeName_Object = MibTableColumn
zySysLogTypeName = _ZySysLogTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 2),
    _ZySysLogTypeName_Type()
)
zySysLogTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysLogTypeName.setStatus("current")
_ZySysLogTypeState_Type = EnabledStatus
_ZySysLogTypeState_Object = MibTableColumn
zySysLogTypeState = _ZySysLogTypeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 3),
    _ZySysLogTypeState_Type()
)
zySysLogTypeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysLogTypeState.setStatus("current")


class _ZySysLogTypeFacility_Type(Integer32):
    """Custom type zySysLogTypeFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localUser0", 0),
          ("localUser1", 1),
          ("localUser2", 2),
          ("localUser3", 3),
          ("localUser4", 4),
          ("localUser5", 5),
          ("localUser6", 6),
          ("localUser7", 7))
    )


_ZySysLogTypeFacility_Type.__name__ = "Integer32"
_ZySysLogTypeFacility_Object = MibTableColumn
zySysLogTypeFacility = _ZySysLogTypeFacility_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 4),
    _ZySysLogTypeFacility_Type()
)
zySysLogTypeFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysLogTypeFacility.setStatus("current")
_ZySysLogMaxNumberOfServers_Type = Integer32
_ZySysLogMaxNumberOfServers_Object = MibScalar
zySysLogMaxNumberOfServers = _ZySysLogMaxNumberOfServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 3),
    _ZySysLogMaxNumberOfServers_Type()
)
zySysLogMaxNumberOfServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysLogMaxNumberOfServers.setStatus("current")
_ZyxelSysLogServerTable_Object = MibTable
zyxelSysLogServerTable = _ZyxelSysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelSysLogServerTable.setStatus("current")
_ZyxelSysLogServerEntry_Object = MibTableRow
zyxelSysLogServerEntry = _ZyxelSysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 4, 1)
)
zyxelSysLogServerEntry.setIndexNames(
    (0, "ZYXEL-SYSLOG-MIB", "zySysLogServerIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelSysLogServerEntry.setStatus("current")
_ZySysLogServerIpAddress_Type = IpAddress
_ZySysLogServerIpAddress_Object = MibTableColumn
zySysLogServerIpAddress = _ZySysLogServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 4, 1, 1),
    _ZySysLogServerIpAddress_Type()
)
zySysLogServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySysLogServerIpAddress.setStatus("current")


class _ZySysLogServerLogLevel_Type(Integer32):
    """Custom type zySysLogServerLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("level0", 0),
          ("level0To1", 1),
          ("level0To2", 2),
          ("level0To3", 3),
          ("level0To4", 4),
          ("level0To5", 5),
          ("level0To6", 6),
          ("level0To7", 7))
    )


_ZySysLogServerLogLevel_Type.__name__ = "Integer32"
_ZySysLogServerLogLevel_Object = MibTableColumn
zySysLogServerLogLevel = _ZySysLogServerLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 4, 1, 2),
    _ZySysLogServerLogLevel_Type()
)
zySysLogServerLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysLogServerLogLevel.setStatus("current")
_ZySysLogServerRowStatus_Type = RowStatus
_ZySysLogServerRowStatus_Object = MibTableColumn
zySysLogServerRowStatus = _ZySysLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 4, 1, 3),
    _ZySysLogServerRowStatus_Type()
)
zySysLogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zySysLogServerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SYSLOG-MIB",
    **{"zyxelSysLog": zyxelSysLog,
       "zyxelSysLogSetup": zyxelSysLogSetup,
       "zySysLogState": zySysLogState,
       "zyxelSysLogTypeTable": zyxelSysLogTypeTable,
       "zyxelSysLogTypeEntry": zyxelSysLogTypeEntry,
       "zySysLogTypeIndex": zySysLogTypeIndex,
       "zySysLogTypeName": zySysLogTypeName,
       "zySysLogTypeState": zySysLogTypeState,
       "zySysLogTypeFacility": zySysLogTypeFacility,
       "zySysLogMaxNumberOfServers": zySysLogMaxNumberOfServers,
       "zyxelSysLogServerTable": zyxelSysLogServerTable,
       "zyxelSysLogServerEntry": zyxelSysLogServerEntry,
       "zySysLogServerIpAddress": zySysLogServerIpAddress,
       "zySysLogServerLogLevel": zySysLogServerLogLevel,
       "zySysLogServerRowStatus": zySysLogServerRowStatus}
)
