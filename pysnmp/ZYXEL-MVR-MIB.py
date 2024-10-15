# SNMP MIB module (ZYXEL-MVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-MVR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:25 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

zyxelMvr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMvrSetup_ObjectIdentity = ObjectIdentity
zyxelMvrSetup = _ZyxelMvrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1)
)
_ZyMvrMaxNumberOfVlans_Type = Integer32
_ZyMvrMaxNumberOfVlans_Object = MibScalar
zyMvrMaxNumberOfVlans = _ZyMvrMaxNumberOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 1),
    _ZyMvrMaxNumberOfVlans_Type()
)
zyMvrMaxNumberOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMvrMaxNumberOfVlans.setStatus("current")
_ZyxelMvrTable_Object = MibTable
zyxelMvrTable = _ZyxelMvrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelMvrTable.setStatus("current")
_ZyxelMvrEntry_Object = MibTableRow
zyxelMvrEntry = _ZyxelMvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 2, 1)
)
zyxelMvrEntry.setIndexNames(
    (0, "ZYXEL-MVR-MIB", "zyMvrVid"),
)
if mibBuilder.loadTexts:
    zyxelMvrEntry.setStatus("current")
_ZyMvrVid_Type = Integer32
_ZyMvrVid_Object = MibTableColumn
zyMvrVid = _ZyMvrVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 2, 1, 1),
    _ZyMvrVid_Type()
)
zyMvrVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMvrVid.setStatus("current")
_ZyMvrName_Type = DisplayString
_ZyMvrName_Object = MibTableColumn
zyMvrName = _ZyMvrName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 2, 1, 2),
    _ZyMvrName_Type()
)
zyMvrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMvrName.setStatus("current")


class _ZyMvrMode_Type(Integer32):
    """Custom type zyMvrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 1),
          ("dynamic", 0))
    )


_ZyMvrMode_Type.__name__ = "Integer32"
_ZyMvrMode_Object = MibTableColumn
zyMvrMode = _ZyMvrMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 2, 1, 3),
    _ZyMvrMode_Type()
)
zyMvrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMvrMode.setStatus("current")
_ZyMvr8021pPriority_Type = Integer32
_ZyMvr8021pPriority_Object = MibTableColumn
zyMvr8021pPriority = _ZyMvr8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 2, 1, 4),
    _ZyMvr8021pPriority_Type()
)
zyMvr8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMvr8021pPriority.setStatus("current")
_ZyMvrRowStatus_Type = RowStatus
_ZyMvrRowStatus_Object = MibTableColumn
zyMvrRowStatus = _ZyMvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 2, 1, 5),
    _ZyMvrRowStatus_Type()
)
zyMvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyMvrRowStatus.setStatus("current")
_ZyxelMvrPortTable_Object = MibTable
zyxelMvrPortTable = _ZyxelMvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelMvrPortTable.setStatus("current")
_ZyxelMvrPortEntry_Object = MibTableRow
zyxelMvrPortEntry = _ZyxelMvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 3, 1)
)
zyxelMvrPortEntry.setIndexNames(
    (0, "ZYXEL-MVR-MIB", "zyMvrVid"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMvrPortEntry.setStatus("current")


class _ZyMvrPortRole_Type(Integer32):
    """Custom type zyMvrPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("receiverPort", 3),
          ("sourcePort", 2))
    )


_ZyMvrPortRole_Type.__name__ = "Integer32"
_ZyMvrPortRole_Object = MibTableColumn
zyMvrPortRole = _ZyMvrPortRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 3, 1, 1),
    _ZyMvrPortRole_Type()
)
zyMvrPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMvrPortRole.setStatus("current")
_ZyMvrPortTagging_Type = EnabledStatus
_ZyMvrPortTagging_Object = MibTableColumn
zyMvrPortTagging = _ZyMvrPortTagging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 3, 1, 2),
    _ZyMvrPortTagging_Type()
)
zyMvrPortTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMvrPortTagging.setStatus("current")
_ZyMvrMaxNumberOfGroups_Type = Integer32
_ZyMvrMaxNumberOfGroups_Object = MibScalar
zyMvrMaxNumberOfGroups = _ZyMvrMaxNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 4),
    _ZyMvrMaxNumberOfGroups_Type()
)
zyMvrMaxNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMvrMaxNumberOfGroups.setStatus("current")
_ZyxelMvrGroupTable_Object = MibTable
zyxelMvrGroupTable = _ZyxelMvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelMvrGroupTable.setStatus("current")
_ZyxelMvrGroupEntry_Object = MibTableRow
zyxelMvrGroupEntry = _ZyxelMvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 5, 1)
)
zyxelMvrGroupEntry.setIndexNames(
    (0, "ZYXEL-MVR-MIB", "zyMvrVid"),
    (0, "ZYXEL-MVR-MIB", "zyMvrGroupName"),
)
if mibBuilder.loadTexts:
    zyxelMvrGroupEntry.setStatus("current")
_ZyMvrGroupName_Type = DisplayString
_ZyMvrGroupName_Object = MibTableColumn
zyMvrGroupName = _ZyMvrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 5, 1, 1),
    _ZyMvrGroupName_Type()
)
zyMvrGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMvrGroupName.setStatus("current")
_ZyMvrGroupStartIpAddressType_Type = InetAddressType
_ZyMvrGroupStartIpAddressType_Object = MibTableColumn
zyMvrGroupStartIpAddressType = _ZyMvrGroupStartIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 5, 1, 2),
    _ZyMvrGroupStartIpAddressType_Type()
)
zyMvrGroupStartIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMvrGroupStartIpAddressType.setStatus("current")
_ZyMvrGroupStartIpAddress_Type = InetAddress
_ZyMvrGroupStartIpAddress_Object = MibTableColumn
zyMvrGroupStartIpAddress = _ZyMvrGroupStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 5, 1, 3),
    _ZyMvrGroupStartIpAddress_Type()
)
zyMvrGroupStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMvrGroupStartIpAddress.setStatus("current")
_ZyMvrGroupEndIpAddressType_Type = InetAddressType
_ZyMvrGroupEndIpAddressType_Object = MibTableColumn
zyMvrGroupEndIpAddressType = _ZyMvrGroupEndIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 5, 1, 4),
    _ZyMvrGroupEndIpAddressType_Type()
)
zyMvrGroupEndIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMvrGroupEndIpAddressType.setStatus("current")
_ZyMvrGroupEndIpAddress_Type = InetAddress
_ZyMvrGroupEndIpAddress_Object = MibTableColumn
zyMvrGroupEndIpAddress = _ZyMvrGroupEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 5, 1, 5),
    _ZyMvrGroupEndIpAddress_Type()
)
zyMvrGroupEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMvrGroupEndIpAddress.setStatus("current")
_ZyMvrGroupRowStatus_Type = RowStatus
_ZyMvrGroupRowStatus_Object = MibTableColumn
zyMvrGroupRowStatus = _ZyMvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 55, 1, 5, 1, 6),
    _ZyMvrGroupRowStatus_Type()
)
zyMvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyMvrGroupRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MVR-MIB",
    **{"zyxelMvr": zyxelMvr,
       "zyxelMvrSetup": zyxelMvrSetup,
       "zyMvrMaxNumberOfVlans": zyMvrMaxNumberOfVlans,
       "zyxelMvrTable": zyxelMvrTable,
       "zyxelMvrEntry": zyxelMvrEntry,
       "zyMvrVid": zyMvrVid,
       "zyMvrName": zyMvrName,
       "zyMvrMode": zyMvrMode,
       "zyMvr8021pPriority": zyMvr8021pPriority,
       "zyMvrRowStatus": zyMvrRowStatus,
       "zyxelMvrPortTable": zyxelMvrPortTable,
       "zyxelMvrPortEntry": zyxelMvrPortEntry,
       "zyMvrPortRole": zyMvrPortRole,
       "zyMvrPortTagging": zyMvrPortTagging,
       "zyMvrMaxNumberOfGroups": zyMvrMaxNumberOfGroups,
       "zyxelMvrGroupTable": zyxelMvrGroupTable,
       "zyxelMvrGroupEntry": zyxelMvrGroupEntry,
       "zyMvrGroupName": zyMvrGroupName,
       "zyMvrGroupStartIpAddressType": zyMvrGroupStartIpAddressType,
       "zyMvrGroupStartIpAddress": zyMvrGroupStartIpAddress,
       "zyMvrGroupEndIpAddressType": zyMvrGroupEndIpAddressType,
       "zyMvrGroupEndIpAddress": zyMvrGroupEndIpAddress,
       "zyMvrGroupRowStatus": zyMvrGroupRowStatus}
)
