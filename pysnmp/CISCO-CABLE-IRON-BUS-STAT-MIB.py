# SNMP MIB module (CISCO-CABLE-IRON-BUS-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CABLE-IRON-BUS-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:36 2024
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

(NonZeroPercent,) = mibBuilder.importSymbols(
    "CISCO-CABLE-ADMISSION-CTRL-MIB",
    "NonZeroPercent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCableIronBusStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 821)
)
ciscoCableIronBusStatMIB.setRevisions(
        ("2014-08-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCableIronBusStatMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCableIronBusStatMIBNotifs = _CiscoCableIronBusStatMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 0)
)
_CiscoCableIronBusStatMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCableIronBusStatMIBObjects = _CiscoCableIronBusStatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1)
)
_CiscoCableIronBusStatTable_Object = MibTable
ciscoCableIronBusStatTable = _CiscoCableIronBusStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCableIronBusStatTable.setStatus("current")
_CiscoCableIronBusStatEntry_Object = MibTableRow
ciscoCableIronBusStatEntry = _CiscoCableIronBusStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1)
)
ciscoCableIronBusStatEntry.setIndexNames(
    (0, "CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatIndex"),
)
if mibBuilder.loadTexts:
    ciscoCableIronBusStatEntry.setStatus("current")
_CiscoCableIronBusStatIndex_Type = Integer32
_CiscoCableIronBusStatIndex_Object = MibTableColumn
ciscoCableIronBusStatIndex = _CiscoCableIronBusStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 1),
    _CiscoCableIronBusStatIndex_Type()
)
ciscoCableIronBusStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatIndex.setStatus("current")


class _CiscoCableIronBusStatFibBandwidth_Type(NonZeroPercent):
    """Custom type ciscoCableIronBusStatFibBandwidth based on NonZeroPercent"""
    subtypeSpec = NonZeroPercent.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CiscoCableIronBusStatFibBandwidth_Type.__name__ = "NonZeroPercent"
_CiscoCableIronBusStatFibBandwidth_Object = MibTableColumn
ciscoCableIronBusStatFibBandwidth = _CiscoCableIronBusStatFibBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 2),
    _CiscoCableIronBusStatFibBandwidth_Type()
)
ciscoCableIronBusStatFibBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatFibBandwidth.setStatus("current")


class _CiscoCableIronBusStatTibBandwidth_Type(NonZeroPercent):
    """Custom type ciscoCableIronBusStatTibBandwidth based on NonZeroPercent"""
    subtypeSpec = NonZeroPercent.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CiscoCableIronBusStatTibBandwidth_Type.__name__ = "NonZeroPercent"
_CiscoCableIronBusStatTibBandwidth_Object = MibTableColumn
ciscoCableIronBusStatTibBandwidth = _CiscoCableIronBusStatTibBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 3),
    _CiscoCableIronBusStatTibBandwidth_Type()
)
ciscoCableIronBusStatTibBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatTibBandwidth.setStatus("current")


class _CiscoCableIronBusStatMessageIntervalCurrent_Type(Integer32):
    """Custom type ciscoCableIronBusStatMessageIntervalCurrent based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CiscoCableIronBusStatMessageIntervalCurrent_Type.__name__ = "Integer32"
_CiscoCableIronBusStatMessageIntervalCurrent_Object = MibTableColumn
ciscoCableIronBusStatMessageIntervalCurrent = _CiscoCableIronBusStatMessageIntervalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 4),
    _CiscoCableIronBusStatMessageIntervalCurrent_Type()
)
ciscoCableIronBusStatMessageIntervalCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatMessageIntervalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatMessageIntervalCurrent.setUnits("minutes")


class _CiscoCableIronBusStatBandwidthCurrent_Type(NonZeroPercent):
    """Custom type ciscoCableIronBusStatBandwidthCurrent based on NonZeroPercent"""
    defaultValue = 90

    subtypeSpec = NonZeroPercent.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100),
    )


_CiscoCableIronBusStatBandwidthCurrent_Type.__name__ = "NonZeroPercent"
_CiscoCableIronBusStatBandwidthCurrent_Object = MibTableColumn
ciscoCableIronBusStatBandwidthCurrent = _CiscoCableIronBusStatBandwidthCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 5),
    _CiscoCableIronBusStatBandwidthCurrent_Type()
)
ciscoCableIronBusStatBandwidthCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatBandwidthCurrent.setStatus("current")


class _CiscoCableIronBusStatMessageIntervalDefault_Type(Integer32):
    """Custom type ciscoCableIronBusStatMessageIntervalDefault based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CiscoCableIronBusStatMessageIntervalDefault_Type.__name__ = "Integer32"
_CiscoCableIronBusStatMessageIntervalDefault_Object = MibTableColumn
ciscoCableIronBusStatMessageIntervalDefault = _CiscoCableIronBusStatMessageIntervalDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 6),
    _CiscoCableIronBusStatMessageIntervalDefault_Type()
)
ciscoCableIronBusStatMessageIntervalDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatMessageIntervalDefault.setStatus("current")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatMessageIntervalDefault.setUnits("minutes")


class _CiscoCableIronBusStatBandwidthDefault_Type(NonZeroPercent):
    """Custom type ciscoCableIronBusStatBandwidthDefault based on NonZeroPercent"""
    defaultValue = 90

    subtypeSpec = NonZeroPercent.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CiscoCableIronBusStatBandwidthDefault_Type.__name__ = "NonZeroPercent"
_CiscoCableIronBusStatBandwidthDefault_Object = MibTableColumn
ciscoCableIronBusStatBandwidthDefault = _CiscoCableIronBusStatBandwidthDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 7),
    _CiscoCableIronBusStatBandwidthDefault_Type()
)
ciscoCableIronBusStatBandwidthDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatBandwidthDefault.setStatus("current")
_CiscoCableIronBusStatFibPktsRcv_Type = Counter64
_CiscoCableIronBusStatFibPktsRcv_Object = MibTableColumn
ciscoCableIronBusStatFibPktsRcv = _CiscoCableIronBusStatFibPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 8),
    _CiscoCableIronBusStatFibPktsRcv_Type()
)
ciscoCableIronBusStatFibPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatFibPktsRcv.setStatus("current")
_CiscoCableIronBusStatFibBytesRcv_Type = Counter64
_CiscoCableIronBusStatFibBytesRcv_Object = MibTableColumn
ciscoCableIronBusStatFibBytesRcv = _CiscoCableIronBusStatFibBytesRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 9),
    _CiscoCableIronBusStatFibBytesRcv_Type()
)
ciscoCableIronBusStatFibBytesRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatFibBytesRcv.setStatus("current")
_CiscoCableIronBusStatTibPktsSent_Type = Counter64
_CiscoCableIronBusStatTibPktsSent_Object = MibTableColumn
ciscoCableIronBusStatTibPktsSent = _CiscoCableIronBusStatTibPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 10),
    _CiscoCableIronBusStatTibPktsSent_Type()
)
ciscoCableIronBusStatTibPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatTibPktsSent.setStatus("current")
_CiscoCableIronBusStatTibByteSent_Type = Counter64
_CiscoCableIronBusStatTibByteSent_Object = MibTableColumn
ciscoCableIronBusStatTibByteSent = _CiscoCableIronBusStatTibByteSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 11),
    _CiscoCableIronBusStatTibByteSent_Type()
)
ciscoCableIronBusStatTibByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatTibByteSent.setStatus("current")
_CiscoCableIronBusStatFibPktsPerSec_Type = Counter64
_CiscoCableIronBusStatFibPktsPerSec_Object = MibTableColumn
ciscoCableIronBusStatFibPktsPerSec = _CiscoCableIronBusStatFibPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 12),
    _CiscoCableIronBusStatFibPktsPerSec_Type()
)
ciscoCableIronBusStatFibPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatFibPktsPerSec.setStatus("current")
_CiscoCableIronBusStatTibPktPerSec_Type = Counter64
_CiscoCableIronBusStatTibPktPerSec_Object = MibTableColumn
ciscoCableIronBusStatTibPktPerSec = _CiscoCableIronBusStatTibPktPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 1, 1, 1, 13),
    _CiscoCableIronBusStatTibPktPerSec_Type()
)
ciscoCableIronBusStatTibPktPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableIronBusStatTibPktPerSec.setStatus("current")
_CiscoCableIronBusStatMIBConform_ObjectIdentity = ObjectIdentity
ciscoCableIronBusStatMIBConform = _CiscoCableIronBusStatMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 2)
)
_CiscoCableIronBusStatMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCableIronBusStatMIBCompliances = _CiscoCableIronBusStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 2, 1)
)
_CiscoCableIronBusStatMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCableIronBusStatMIBGroups = _CiscoCableIronBusStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 2, 2)
)

# Managed Objects groups

ciscoCableIronBusStatObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 2, 2, 1)
)
ciscoCableIronBusStatObjectGroup.setObjects(
      *(("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatFibBandwidth"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatMessageIntervalCurrent"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatBandwidthCurrent"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatBandwidthDefault"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatFibPktsRcv"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatFibBytesRcv"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatTibPktsSent"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatTibByteSent"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatFibPktsPerSec"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatTibPktPerSec"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatTibBandwidth"),
        ("CISCO-CABLE-IRON-BUS-STAT-MIB", "ciscoCableIronBusStatMessageIntervalDefault"))
)
if mibBuilder.loadTexts:
    ciscoCableIronBusStatObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCableIronBusStatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 821, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCableIronBusStatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-IRON-BUS-STAT-MIB",
    **{"ciscoCableIronBusStatMIB": ciscoCableIronBusStatMIB,
       "ciscoCableIronBusStatMIBNotifs": ciscoCableIronBusStatMIBNotifs,
       "ciscoCableIronBusStatMIBObjects": ciscoCableIronBusStatMIBObjects,
       "ciscoCableIronBusStatTable": ciscoCableIronBusStatTable,
       "ciscoCableIronBusStatEntry": ciscoCableIronBusStatEntry,
       "ciscoCableIronBusStatIndex": ciscoCableIronBusStatIndex,
       "ciscoCableIronBusStatFibBandwidth": ciscoCableIronBusStatFibBandwidth,
       "ciscoCableIronBusStatTibBandwidth": ciscoCableIronBusStatTibBandwidth,
       "ciscoCableIronBusStatMessageIntervalCurrent": ciscoCableIronBusStatMessageIntervalCurrent,
       "ciscoCableIronBusStatBandwidthCurrent": ciscoCableIronBusStatBandwidthCurrent,
       "ciscoCableIronBusStatMessageIntervalDefault": ciscoCableIronBusStatMessageIntervalDefault,
       "ciscoCableIronBusStatBandwidthDefault": ciscoCableIronBusStatBandwidthDefault,
       "ciscoCableIronBusStatFibPktsRcv": ciscoCableIronBusStatFibPktsRcv,
       "ciscoCableIronBusStatFibBytesRcv": ciscoCableIronBusStatFibBytesRcv,
       "ciscoCableIronBusStatTibPktsSent": ciscoCableIronBusStatTibPktsSent,
       "ciscoCableIronBusStatTibByteSent": ciscoCableIronBusStatTibByteSent,
       "ciscoCableIronBusStatFibPktsPerSec": ciscoCableIronBusStatFibPktsPerSec,
       "ciscoCableIronBusStatTibPktPerSec": ciscoCableIronBusStatTibPktPerSec,
       "ciscoCableIronBusStatMIBConform": ciscoCableIronBusStatMIBConform,
       "ciscoCableIronBusStatMIBCompliances": ciscoCableIronBusStatMIBCompliances,
       "ciscoCableIronBusStatMIBCompliance": ciscoCableIronBusStatMIBCompliance,
       "ciscoCableIronBusStatMIBGroups": ciscoCableIronBusStatMIBGroups,
       "ciscoCableIronBusStatObjectGroup": ciscoCableIronBusStatObjectGroup}
)
