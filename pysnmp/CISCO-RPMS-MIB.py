# SNMP MIB module (CISCO-RPMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RPMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:41 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoRpmsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84)
)
ciscoRpmsMIB.setRevisions(
        ("2002-04-17 00:00",
         "2001-11-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoRpmsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRpmsMIBObjects = _CiscoRpmsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1)
)
_CrpmsSystem_ObjectIdentity = ObjectIdentity
crpmsSystem = _CrpmsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1)
)
_CrpmsSubsystemTable_Object = MibTable
crpmsSubsystemTable = _CrpmsSubsystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1)
)
if mibBuilder.loadTexts:
    crpmsSubsystemTable.setStatus("current")
_CrpmsSubsystemEntry_Object = MibTableRow
crpmsSubsystemEntry = _CrpmsSubsystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1)
)
crpmsSubsystemEntry.setIndexNames(
    (0, "CISCO-RPMS-MIB", "crpmsSubsystemIndex"),
)
if mibBuilder.loadTexts:
    crpmsSubsystemEntry.setStatus("current")


class _CrpmsSubsystemIndex_Type(Unsigned32):
    """Custom type crpmsSubsystemIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CrpmsSubsystemIndex_Type.__name__ = "Unsigned32"
_CrpmsSubsystemIndex_Object = MibTableColumn
crpmsSubsystemIndex = _CrpmsSubsystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1, 1),
    _CrpmsSubsystemIndex_Type()
)
crpmsSubsystemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crpmsSubsystemIndex.setStatus("current")


class _CrpmsSubsystemName_Type(SnmpAdminString):
    """Custom type crpmsSubsystemName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CrpmsSubsystemName_Type.__name__ = "SnmpAdminString"
_CrpmsSubsystemName_Object = MibTableColumn
crpmsSubsystemName = _CrpmsSubsystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1, 2),
    _CrpmsSubsystemName_Type()
)
crpmsSubsystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsSubsystemName.setStatus("current")
_CrpmsSubsystemUptime_Type = TimeStamp
_CrpmsSubsystemUptime_Object = MibTableColumn
crpmsSubsystemUptime = _CrpmsSubsystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1, 3),
    _CrpmsSubsystemUptime_Type()
)
crpmsSubsystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsSubsystemUptime.setStatus("current")
_CrpmsCustomerProfile_ObjectIdentity = ObjectIdentity
crpmsCustomerProfile = _CrpmsCustomerProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2)
)
_CrpmsCpTable_Object = MibTable
crpmsCpTable = _CrpmsCpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1)
)
if mibBuilder.loadTexts:
    crpmsCpTable.setStatus("current")
_CrpmsCpEntry_Object = MibTableRow
crpmsCpEntry = _CrpmsCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1)
)
crpmsCpEntry.setIndexNames(
    (1, "CISCO-RPMS-MIB", "crpmsCpName"),
)
if mibBuilder.loadTexts:
    crpmsCpEntry.setStatus("current")


class _CrpmsCpName_Type(SnmpAdminString):
    """Custom type crpmsCpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CrpmsCpName_Type.__name__ = "SnmpAdminString"
_CrpmsCpName_Object = MibTableColumn
crpmsCpName = _CrpmsCpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 1),
    _CrpmsCpName_Type()
)
crpmsCpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crpmsCpName.setStatus("current")


class _CrpmsCpLimit_Type(Unsigned32):
    """Custom type crpmsCpLimit based on Unsigned32"""
    defaultValue = 0


_CrpmsCpLimit_Object = MibTableColumn
crpmsCpLimit = _CrpmsCpLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 2),
    _CrpmsCpLimit_Type()
)
crpmsCpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsCpLimit.setStatus("current")


class _CrpmsCpOverflowLimit_Type(Unsigned32):
    """Custom type crpmsCpOverflowLimit based on Unsigned32"""
    defaultValue = 0


_CrpmsCpOverflowLimit_Object = MibTableColumn
crpmsCpOverflowLimit = _CrpmsCpOverflowLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 3),
    _CrpmsCpOverflowLimit_Type()
)
crpmsCpOverflowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsCpOverflowLimit.setStatus("current")
_CrpmsCpActiveCalls_Type = Gauge32
_CrpmsCpActiveCalls_Object = MibTableColumn
crpmsCpActiveCalls = _CrpmsCpActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 4),
    _CrpmsCpActiveCalls_Type()
)
crpmsCpActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsCpActiveCalls.setStatus("current")
_CrpmsCpActiveOverflowCalls_Type = Gauge32
_CrpmsCpActiveOverflowCalls_Object = MibTableColumn
crpmsCpActiveOverflowCalls = _CrpmsCpActiveOverflowCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 5),
    _CrpmsCpActiveOverflowCalls_Type()
)
crpmsCpActiveOverflowCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsCpActiveOverflowCalls.setStatus("current")
_CrpmsCpAttemptedCalls_Type = Counter32
_CrpmsCpAttemptedCalls_Object = MibTableColumn
crpmsCpAttemptedCalls = _CrpmsCpAttemptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 6),
    _CrpmsCpAttemptedCalls_Type()
)
crpmsCpAttemptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsCpAttemptedCalls.setStatus("current")
_CrpmsCpAttemptedOverflowCalls_Type = Counter32
_CrpmsCpAttemptedOverflowCalls_Object = MibTableColumn
crpmsCpAttemptedOverflowCalls = _CrpmsCpAttemptedOverflowCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 7),
    _CrpmsCpAttemptedOverflowCalls_Type()
)
crpmsCpAttemptedOverflowCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsCpAttemptedOverflowCalls.setStatus("current")
_CrpmsCpRejections_Type = Counter32
_CrpmsCpRejections_Object = MibTableColumn
crpmsCpRejections = _CrpmsCpRejections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 8),
    _CrpmsCpRejections_Type()
)
crpmsCpRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsCpRejections.setStatus("current")
_CrpmsCpOverflowRejections_Type = Counter32
_CrpmsCpOverflowRejections_Object = MibTableColumn
crpmsCpOverflowRejections = _CrpmsCpOverflowRejections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 9),
    _CrpmsCpOverflowRejections_Type()
)
crpmsCpOverflowRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsCpOverflowRejections.setStatus("current")


class _CrpmsCpLimitThreshold_Type(Unsigned32):
    """Custom type crpmsCpLimitThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CrpmsCpLimitThreshold_Type.__name__ = "Unsigned32"
_CrpmsCpLimitThreshold_Object = MibTableColumn
crpmsCpLimitThreshold = _CrpmsCpLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 10),
    _CrpmsCpLimitThreshold_Type()
)
crpmsCpLimitThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsCpLimitThreshold.setStatus("current")
if mibBuilder.loadTexts:
    crpmsCpLimitThreshold.setUnits("percent")


class _CrpmsCpOverflowLimitThreshold_Type(Unsigned32):
    """Custom type crpmsCpOverflowLimitThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CrpmsCpOverflowLimitThreshold_Type.__name__ = "Unsigned32"
_CrpmsCpOverflowLimitThreshold_Object = MibTableColumn
crpmsCpOverflowLimitThreshold = _CrpmsCpOverflowLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 11),
    _CrpmsCpOverflowLimitThreshold_Type()
)
crpmsCpOverflowLimitThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsCpOverflowLimitThreshold.setStatus("current")
if mibBuilder.loadTexts:
    crpmsCpOverflowLimitThreshold.setUnits("percent")


class _CrpmsCpCallRejectionThreshold_Type(Unsigned32):
    """Custom type crpmsCpCallRejectionThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CrpmsCpCallRejectionThreshold_Type.__name__ = "Unsigned32"
_CrpmsCpCallRejectionThreshold_Object = MibTableColumn
crpmsCpCallRejectionThreshold = _CrpmsCpCallRejectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 12),
    _CrpmsCpCallRejectionThreshold_Type()
)
crpmsCpCallRejectionThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsCpCallRejectionThreshold.setStatus("current")
if mibBuilder.loadTexts:
    crpmsCpCallRejectionThreshold.setUnits("percent")


class _CrpmsCpOverflowRejectThreshold_Type(Unsigned32):
    """Custom type crpmsCpOverflowRejectThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CrpmsCpOverflowRejectThreshold_Type.__name__ = "Unsigned32"
_CrpmsCpOverflowRejectThreshold_Object = MibTableColumn
crpmsCpOverflowRejectThreshold = _CrpmsCpOverflowRejectThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 13),
    _CrpmsCpOverflowRejectThreshold_Type()
)
crpmsCpOverflowRejectThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsCpOverflowRejectThreshold.setStatus("current")
if mibBuilder.loadTexts:
    crpmsCpOverflowRejectThreshold.setUnits("percent")
_CrpmsCpEntryStatus_Type = RowStatus
_CrpmsCpEntryStatus_Object = MibTableColumn
crpmsCpEntryStatus = _CrpmsCpEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 14),
    _CrpmsCpEntryStatus_Type()
)
crpmsCpEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsCpEntryStatus.setStatus("current")
_CrpmsVpdn_ObjectIdentity = ObjectIdentity
crpmsVpdn = _CrpmsVpdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3)
)
_CrpmsVpdnGroupTable_Object = MibTable
crpmsVpdnGroupTable = _CrpmsVpdnGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1)
)
if mibBuilder.loadTexts:
    crpmsVpdnGroupTable.setStatus("current")
_CrpmsVpdnGroupEntry_Object = MibTableRow
crpmsVpdnGroupEntry = _CrpmsVpdnGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1)
)
crpmsVpdnGroupEntry.setIndexNames(
    (1, "CISCO-RPMS-MIB", "crpmsVpdnGroupName"),
)
if mibBuilder.loadTexts:
    crpmsVpdnGroupEntry.setStatus("current")


class _CrpmsVpdnGroupName_Type(SnmpAdminString):
    """Custom type crpmsVpdnGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CrpmsVpdnGroupName_Type.__name__ = "SnmpAdminString"
_CrpmsVpdnGroupName_Object = MibTableColumn
crpmsVpdnGroupName = _CrpmsVpdnGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 1),
    _CrpmsVpdnGroupName_Type()
)
crpmsVpdnGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crpmsVpdnGroupName.setStatus("current")
_CrpmsVpdnTunnelId_Type = SnmpAdminString
_CrpmsVpdnTunnelId_Object = MibTableColumn
crpmsVpdnTunnelId = _CrpmsVpdnTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 2),
    _CrpmsVpdnTunnelId_Type()
)
crpmsVpdnTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsVpdnTunnelId.setStatus("current")


class _CrpmsVpdnTunnelProtocol_Type(Integer32):
    """Custom type crpmsVpdnTunnelProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2f", 1),
          ("l2tp", 2))
    )


_CrpmsVpdnTunnelProtocol_Type.__name__ = "Integer32"
_CrpmsVpdnTunnelProtocol_Object = MibTableColumn
crpmsVpdnTunnelProtocol = _CrpmsVpdnTunnelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 3),
    _CrpmsVpdnTunnelProtocol_Type()
)
crpmsVpdnTunnelProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsVpdnTunnelProtocol.setStatus("current")


class _CrpmsVpdnLimit_Type(Unsigned32):
    """Custom type crpmsVpdnLimit based on Unsigned32"""
    defaultValue = 0


_CrpmsVpdnLimit_Object = MibTableColumn
crpmsVpdnLimit = _CrpmsVpdnLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 4),
    _CrpmsVpdnLimit_Type()
)
crpmsVpdnLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsVpdnLimit.setStatus("current")


class _CrpmsVpdnOverflowLimit_Type(Unsigned32):
    """Custom type crpmsVpdnOverflowLimit based on Unsigned32"""
    defaultValue = 0


_CrpmsVpdnOverflowLimit_Object = MibTableColumn
crpmsVpdnOverflowLimit = _CrpmsVpdnOverflowLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 5),
    _CrpmsVpdnOverflowLimit_Type()
)
crpmsVpdnOverflowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsVpdnOverflowLimit.setStatus("current")


class _CrpmsVpdnMlpBundleLimit_Type(Unsigned32):
    """Custom type crpmsVpdnMlpBundleLimit based on Unsigned32"""
    defaultValue = 0


_CrpmsVpdnMlpBundleLimit_Object = MibTableColumn
crpmsVpdnMlpBundleLimit = _CrpmsVpdnMlpBundleLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 6),
    _CrpmsVpdnMlpBundleLimit_Type()
)
crpmsVpdnMlpBundleLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsVpdnMlpBundleLimit.setStatus("current")


class _CrpmsVpdnLinksPerBundleLimit_Type(Unsigned32):
    """Custom type crpmsVpdnLinksPerBundleLimit based on Unsigned32"""
    defaultValue = 0


_CrpmsVpdnLinksPerBundleLimit_Object = MibTableColumn
crpmsVpdnLinksPerBundleLimit = _CrpmsVpdnLinksPerBundleLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 7),
    _CrpmsVpdnLinksPerBundleLimit_Type()
)
crpmsVpdnLinksPerBundleLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsVpdnLinksPerBundleLimit.setStatus("current")
_CrpmsVpdnBundles_Type = Gauge32
_CrpmsVpdnBundles_Object = MibTableColumn
crpmsVpdnBundles = _CrpmsVpdnBundles_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 8),
    _CrpmsVpdnBundles_Type()
)
crpmsVpdnBundles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsVpdnBundles.setStatus("current")
_CrpmsVpdnActiveCalls_Type = Gauge32
_CrpmsVpdnActiveCalls_Object = MibTableColumn
crpmsVpdnActiveCalls = _CrpmsVpdnActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 9),
    _CrpmsVpdnActiveCalls_Type()
)
crpmsVpdnActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsVpdnActiveCalls.setStatus("current")
_CrpmsVpdnActiveOverflowCalls_Type = Gauge32
_CrpmsVpdnActiveOverflowCalls_Object = MibTableColumn
crpmsVpdnActiveOverflowCalls = _CrpmsVpdnActiveOverflowCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 10),
    _CrpmsVpdnActiveOverflowCalls_Type()
)
crpmsVpdnActiveOverflowCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsVpdnActiveOverflowCalls.setStatus("current")
_CrpmsVpdnRejections_Type = Counter32
_CrpmsVpdnRejections_Object = MibTableColumn
crpmsVpdnRejections = _CrpmsVpdnRejections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 11),
    _CrpmsVpdnRejections_Type()
)
crpmsVpdnRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsVpdnRejections.setStatus("current")
_CrpmsVpdnSizeRejections_Type = Counter32
_CrpmsVpdnSizeRejections_Object = MibTableColumn
crpmsVpdnSizeRejections = _CrpmsVpdnSizeRejections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 12),
    _CrpmsVpdnSizeRejections_Type()
)
crpmsVpdnSizeRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crpmsVpdnSizeRejections.setStatus("current")


class _CrpmsVpdnLimitThreshold_Type(Unsigned32):
    """Custom type crpmsVpdnLimitThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CrpmsVpdnLimitThreshold_Type.__name__ = "Unsigned32"
_CrpmsVpdnLimitThreshold_Object = MibTableColumn
crpmsVpdnLimitThreshold = _CrpmsVpdnLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 13),
    _CrpmsVpdnLimitThreshold_Type()
)
crpmsVpdnLimitThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsVpdnLimitThreshold.setStatus("current")
if mibBuilder.loadTexts:
    crpmsVpdnLimitThreshold.setUnits("percent")
_CrpmsVpdnEntryStatus_Type = RowStatus
_CrpmsVpdnEntryStatus_Object = MibTableColumn
crpmsVpdnEntryStatus = _CrpmsVpdnEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 14),
    _CrpmsVpdnEntryStatus_Type()
)
crpmsVpdnEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsVpdnEntryStatus.setStatus("current")
_CrpmsVpdnGroupCpTable_Object = MibTable
crpmsVpdnGroupCpTable = _CrpmsVpdnGroupCpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2)
)
if mibBuilder.loadTexts:
    crpmsVpdnGroupCpTable.setStatus("current")
_CrpmsVpdnGroupCpEntry_Object = MibTableRow
crpmsVpdnGroupCpEntry = _CrpmsVpdnGroupCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1)
)
crpmsVpdnGroupCpEntry.setIndexNames(
    (0, "CISCO-RPMS-MIB", "crpmsVpdnGroupCpVpdnGroupName"),
    (1, "CISCO-RPMS-MIB", "crpmsVpdnGroupCpCpName"),
)
if mibBuilder.loadTexts:
    crpmsVpdnGroupCpEntry.setStatus("current")


class _CrpmsVpdnGroupCpVpdnGroupName_Type(SnmpAdminString):
    """Custom type crpmsVpdnGroupCpVpdnGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CrpmsVpdnGroupCpVpdnGroupName_Type.__name__ = "SnmpAdminString"
_CrpmsVpdnGroupCpVpdnGroupName_Object = MibTableColumn
crpmsVpdnGroupCpVpdnGroupName = _CrpmsVpdnGroupCpVpdnGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1, 1),
    _CrpmsVpdnGroupCpVpdnGroupName_Type()
)
crpmsVpdnGroupCpVpdnGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crpmsVpdnGroupCpVpdnGroupName.setStatus("current")


class _CrpmsVpdnGroupCpCpName_Type(SnmpAdminString):
    """Custom type crpmsVpdnGroupCpCpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CrpmsVpdnGroupCpCpName_Type.__name__ = "SnmpAdminString"
_CrpmsVpdnGroupCpCpName_Object = MibTableColumn
crpmsVpdnGroupCpCpName = _CrpmsVpdnGroupCpCpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1, 2),
    _CrpmsVpdnGroupCpCpName_Type()
)
crpmsVpdnGroupCpCpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crpmsVpdnGroupCpCpName.setStatus("current")
_CrpmsVpdnGroupCpEntryStatus_Type = RowStatus
_CrpmsVpdnGroupCpEntryStatus_Object = MibTableColumn
crpmsVpdnGroupCpEntryStatus = _CrpmsVpdnGroupCpEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1, 3),
    _CrpmsVpdnGroupCpEntryStatus_Type()
)
crpmsVpdnGroupCpEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crpmsVpdnGroupCpEntryStatus.setStatus("current")
_CrpmsNotif_ObjectIdentity = ObjectIdentity
crpmsNotif = _CrpmsNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4)
)
_CrpmsAlarmObject_Type = ObjectIdentifier
_CrpmsAlarmObject_Object = MibScalar
crpmsAlarmObject = _CrpmsAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4, 1),
    _CrpmsAlarmObject_Type()
)
crpmsAlarmObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crpmsAlarmObject.setStatus("current")
_CrpmsAlarmValue_Type = Unsigned32
_CrpmsAlarmValue_Object = MibScalar
crpmsAlarmValue = _CrpmsAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4, 2),
    _CrpmsAlarmValue_Type()
)
crpmsAlarmValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crpmsAlarmValue.setStatus("current")
_CrpmsAlarmThresholdObject_Type = ObjectIdentifier
_CrpmsAlarmThresholdObject_Object = MibScalar
crpmsAlarmThresholdObject = _CrpmsAlarmThresholdObject_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4, 3),
    _CrpmsAlarmThresholdObject_Type()
)
crpmsAlarmThresholdObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crpmsAlarmThresholdObject.setStatus("current")
_CiscoRpmsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoRpmsMIBNotificationPrefix = _CiscoRpmsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 2)
)
_CiscoRpmsMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoRpmsMIBNotifications = _CiscoRpmsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 2, 0)
)
_CiscoRpmsMIBConformance_ObjectIdentity = ObjectIdentity
ciscoRpmsMIBConformance = _CiscoRpmsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 3)
)
_CiscoRpmsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoRpmsMIBCompliances = _CiscoRpmsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 1)
)
_CiscoRpmsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoRpmsMIBGroups = _CiscoRpmsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2)
)

# Managed Objects groups

crpmsSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 1)
)
crpmsSystemGroup.setObjects(
      *(("CISCO-RPMS-MIB", "crpmsSubsystemName"),
        ("CISCO-RPMS-MIB", "crpmsSubsystemUptime"))
)
if mibBuilder.loadTexts:
    crpmsSystemGroup.setStatus("current")

crpmsCpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 2)
)
crpmsCpGroup.setObjects(
      *(("CISCO-RPMS-MIB", "crpmsCpLimit"),
        ("CISCO-RPMS-MIB", "crpmsCpOverflowLimit"),
        ("CISCO-RPMS-MIB", "crpmsCpActiveCalls"),
        ("CISCO-RPMS-MIB", "crpmsCpActiveOverflowCalls"),
        ("CISCO-RPMS-MIB", "crpmsCpAttemptedCalls"),
        ("CISCO-RPMS-MIB", "crpmsCpAttemptedOverflowCalls"),
        ("CISCO-RPMS-MIB", "crpmsCpRejections"),
        ("CISCO-RPMS-MIB", "crpmsCpOverflowRejections"),
        ("CISCO-RPMS-MIB", "crpmsCpLimitThreshold"),
        ("CISCO-RPMS-MIB", "crpmsCpOverflowLimitThreshold"),
        ("CISCO-RPMS-MIB", "crpmsCpCallRejectionThreshold"),
        ("CISCO-RPMS-MIB", "crpmsCpOverflowRejectThreshold"),
        ("CISCO-RPMS-MIB", "crpmsCpEntryStatus"))
)
if mibBuilder.loadTexts:
    crpmsCpGroup.setStatus("current")

crpmsVpdnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 3)
)
crpmsVpdnGroup.setObjects(
      *(("CISCO-RPMS-MIB", "crpmsVpdnTunnelId"),
        ("CISCO-RPMS-MIB", "crpmsVpdnTunnelProtocol"),
        ("CISCO-RPMS-MIB", "crpmsVpdnLimit"),
        ("CISCO-RPMS-MIB", "crpmsVpdnOverflowLimit"),
        ("CISCO-RPMS-MIB", "crpmsVpdnMlpBundleLimit"),
        ("CISCO-RPMS-MIB", "crpmsVpdnLinksPerBundleLimit"),
        ("CISCO-RPMS-MIB", "crpmsVpdnBundles"),
        ("CISCO-RPMS-MIB", "crpmsVpdnActiveCalls"),
        ("CISCO-RPMS-MIB", "crpmsVpdnActiveOverflowCalls"),
        ("CISCO-RPMS-MIB", "crpmsVpdnRejections"),
        ("CISCO-RPMS-MIB", "crpmsVpdnSizeRejections"),
        ("CISCO-RPMS-MIB", "crpmsVpdnLimitThreshold"),
        ("CISCO-RPMS-MIB", "crpmsVpdnEntryStatus"),
        ("CISCO-RPMS-MIB", "crpmsVpdnGroupCpEntryStatus"))
)
if mibBuilder.loadTexts:
    crpmsVpdnGroup.setStatus("current")

crpmsNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 4)
)
crpmsNotifGroup.setObjects(
      *(("CISCO-RPMS-MIB", "crpmsAlarmObject"),
        ("CISCO-RPMS-MIB", "crpmsAlarmValue"),
        ("CISCO-RPMS-MIB", "crpmsAlarmThresholdObject"))
)
if mibBuilder.loadTexts:
    crpmsNotifGroup.setStatus("current")


# Notification objects

crpmsRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 2, 0, 1)
)
crpmsRisingAlarm.setObjects(
      *(("CISCO-RPMS-MIB", "crpmsAlarmObject"),
        ("CISCO-RPMS-MIB", "crpmsAlarmValue"),
        ("CISCO-RPMS-MIB", "crpmsAlarmThresholdObject"))
)
if mibBuilder.loadTexts:
    crpmsRisingAlarm.setStatus(
        "current"
    )

crpmsFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 2, 0, 2)
)
crpmsFallingAlarm.setObjects(
      *(("CISCO-RPMS-MIB", "crpmsAlarmObject"),
        ("CISCO-RPMS-MIB", "crpmsAlarmValue"),
        ("CISCO-RPMS-MIB", "crpmsAlarmThresholdObject"))
)
if mibBuilder.loadTexts:
    crpmsFallingAlarm.setStatus(
        "current"
    )


# Notifications groups

crpmsThresholdNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 5)
)
crpmsThresholdNotifGroup.setObjects(
      *(("CISCO-RPMS-MIB", "crpmsRisingAlarm"),
        ("CISCO-RPMS-MIB", "crpmsFallingAlarm"))
)
if mibBuilder.loadTexts:
    crpmsThresholdNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoRpmsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRpmsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RPMS-MIB",
    **{"ciscoRpmsMIB": ciscoRpmsMIB,
       "ciscoRpmsMIBObjects": ciscoRpmsMIBObjects,
       "crpmsSystem": crpmsSystem,
       "crpmsSubsystemTable": crpmsSubsystemTable,
       "crpmsSubsystemEntry": crpmsSubsystemEntry,
       "crpmsSubsystemIndex": crpmsSubsystemIndex,
       "crpmsSubsystemName": crpmsSubsystemName,
       "crpmsSubsystemUptime": crpmsSubsystemUptime,
       "crpmsCustomerProfile": crpmsCustomerProfile,
       "crpmsCpTable": crpmsCpTable,
       "crpmsCpEntry": crpmsCpEntry,
       "crpmsCpName": crpmsCpName,
       "crpmsCpLimit": crpmsCpLimit,
       "crpmsCpOverflowLimit": crpmsCpOverflowLimit,
       "crpmsCpActiveCalls": crpmsCpActiveCalls,
       "crpmsCpActiveOverflowCalls": crpmsCpActiveOverflowCalls,
       "crpmsCpAttemptedCalls": crpmsCpAttemptedCalls,
       "crpmsCpAttemptedOverflowCalls": crpmsCpAttemptedOverflowCalls,
       "crpmsCpRejections": crpmsCpRejections,
       "crpmsCpOverflowRejections": crpmsCpOverflowRejections,
       "crpmsCpLimitThreshold": crpmsCpLimitThreshold,
       "crpmsCpOverflowLimitThreshold": crpmsCpOverflowLimitThreshold,
       "crpmsCpCallRejectionThreshold": crpmsCpCallRejectionThreshold,
       "crpmsCpOverflowRejectThreshold": crpmsCpOverflowRejectThreshold,
       "crpmsCpEntryStatus": crpmsCpEntryStatus,
       "crpmsVpdn": crpmsVpdn,
       "crpmsVpdnGroupTable": crpmsVpdnGroupTable,
       "crpmsVpdnGroupEntry": crpmsVpdnGroupEntry,
       "crpmsVpdnGroupName": crpmsVpdnGroupName,
       "crpmsVpdnTunnelId": crpmsVpdnTunnelId,
       "crpmsVpdnTunnelProtocol": crpmsVpdnTunnelProtocol,
       "crpmsVpdnLimit": crpmsVpdnLimit,
       "crpmsVpdnOverflowLimit": crpmsVpdnOverflowLimit,
       "crpmsVpdnMlpBundleLimit": crpmsVpdnMlpBundleLimit,
       "crpmsVpdnLinksPerBundleLimit": crpmsVpdnLinksPerBundleLimit,
       "crpmsVpdnBundles": crpmsVpdnBundles,
       "crpmsVpdnActiveCalls": crpmsVpdnActiveCalls,
       "crpmsVpdnActiveOverflowCalls": crpmsVpdnActiveOverflowCalls,
       "crpmsVpdnRejections": crpmsVpdnRejections,
       "crpmsVpdnSizeRejections": crpmsVpdnSizeRejections,
       "crpmsVpdnLimitThreshold": crpmsVpdnLimitThreshold,
       "crpmsVpdnEntryStatus": crpmsVpdnEntryStatus,
       "crpmsVpdnGroupCpTable": crpmsVpdnGroupCpTable,
       "crpmsVpdnGroupCpEntry": crpmsVpdnGroupCpEntry,
       "crpmsVpdnGroupCpVpdnGroupName": crpmsVpdnGroupCpVpdnGroupName,
       "crpmsVpdnGroupCpCpName": crpmsVpdnGroupCpCpName,
       "crpmsVpdnGroupCpEntryStatus": crpmsVpdnGroupCpEntryStatus,
       "crpmsNotif": crpmsNotif,
       "crpmsAlarmObject": crpmsAlarmObject,
       "crpmsAlarmValue": crpmsAlarmValue,
       "crpmsAlarmThresholdObject": crpmsAlarmThresholdObject,
       "ciscoRpmsMIBNotificationPrefix": ciscoRpmsMIBNotificationPrefix,
       "ciscoRpmsMIBNotifications": ciscoRpmsMIBNotifications,
       "crpmsRisingAlarm": crpmsRisingAlarm,
       "crpmsFallingAlarm": crpmsFallingAlarm,
       "ciscoRpmsMIBConformance": ciscoRpmsMIBConformance,
       "ciscoRpmsMIBCompliances": ciscoRpmsMIBCompliances,
       "ciscoRpmsMIBCompliance": ciscoRpmsMIBCompliance,
       "ciscoRpmsMIBGroups": ciscoRpmsMIBGroups,
       "crpmsSystemGroup": crpmsSystemGroup,
       "crpmsCpGroup": crpmsCpGroup,
       "crpmsVpdnGroup": crpmsVpdnGroup,
       "crpmsNotifGroup": crpmsNotifGroup,
       "crpmsThresholdNotifGroup": crpmsThresholdNotifGroup}
)
