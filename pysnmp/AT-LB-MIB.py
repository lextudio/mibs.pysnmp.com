# SNMP MIB module (AT-LB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-LB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:21 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104)
)
lb.setRevisions(
        ("2006-06-28 12:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LbShowGlobalTable_Object = MibTable
lbShowGlobalTable = _LbShowGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1)
)
if mibBuilder.loadTexts:
    lbShowGlobalTable.setStatus("current")
_LbShowGlobalEntry_Object = MibTableRow
lbShowGlobalEntry = _LbShowGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1)
)
lbShowGlobalEntry.setIndexNames(
    (0, "AT-LB-MIB", "lbGlobalIndex"),
)
if mibBuilder.loadTexts:
    lbShowGlobalEntry.setStatus("current")
_LbGlobalIndex_Type = Integer32
_LbGlobalIndex_Object = MibTableColumn
lbGlobalIndex = _LbGlobalIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 1),
    _LbGlobalIndex_Type()
)
lbGlobalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbGlobalIndex.setStatus("current")
_LbAffinityTimeOut_Type = Integer32
_LbAffinityTimeOut_Object = MibTableColumn
lbAffinityTimeOut = _LbAffinityTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 2),
    _LbAffinityTimeOut_Type()
)
lbAffinityTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffinityTimeOut.setStatus("current")
_LbOrphanTimeOut_Type = Integer32
_LbOrphanTimeOut_Object = MibTableColumn
lbOrphanTimeOut = _LbOrphanTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 3),
    _LbOrphanTimeOut_Type()
)
lbOrphanTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOrphanTimeOut.setStatus("current")
_LbCriticalRst_Type = Integer32
_LbCriticalRst_Object = MibTableColumn
lbCriticalRst = _LbCriticalRst_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 4),
    _LbCriticalRst_Type()
)
lbCriticalRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbCriticalRst.setStatus("current")
_LbTotalResources_Type = Integer32
_LbTotalResources_Object = MibTableColumn
lbTotalResources = _LbTotalResources_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 5),
    _LbTotalResources_Type()
)
lbTotalResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTotalResources.setStatus("current")
_LbTotalResPools_Type = Integer32
_LbTotalResPools_Object = MibTableColumn
lbTotalResPools = _LbTotalResPools_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 6),
    _LbTotalResPools_Type()
)
lbTotalResPools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTotalResPools.setStatus("current")
_LbTotalVirtBals_Type = Integer32
_LbTotalVirtBals_Object = MibTableColumn
lbTotalVirtBals = _LbTotalVirtBals_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 7),
    _LbTotalVirtBals_Type()
)
lbTotalVirtBals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTotalVirtBals.setStatus("current")
_LbCurrentConnections_Type = Integer32
_LbCurrentConnections_Object = MibTableColumn
lbCurrentConnections = _LbCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 1, 1, 8),
    _LbCurrentConnections_Type()
)
lbCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbCurrentConnections.setStatus("current")
_LbShowResTable_Object = MibTable
lbShowResTable = _LbShowResTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2)
)
if mibBuilder.loadTexts:
    lbShowResTable.setStatus("current")
_LbShowResEntry_Object = MibTableRow
lbShowResEntry = _LbShowResEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1)
)
lbShowResEntry.setIndexNames(
    (0, "AT-LB-MIB", "lbResIndex"),
)
if mibBuilder.loadTexts:
    lbShowResEntry.setStatus("current")
_LbResIndex_Type = Integer32
_LbResIndex_Object = MibTableColumn
lbResIndex = _LbResIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 1),
    _LbResIndex_Type()
)
lbResIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResIndex.setStatus("current")
_LbResource_Type = DisplayString
_LbResource_Object = MibTableColumn
lbResource = _LbResource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 2),
    _LbResource_Type()
)
lbResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResource.setStatus("current")
_LbResIp_Type = IpAddress
_LbResIp_Object = MibTableColumn
lbResIp = _LbResIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 3),
    _LbResIp_Type()
)
lbResIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResIp.setStatus("current")
_LbResPort_Type = Integer32
_LbResPort_Object = MibTableColumn
lbResPort = _LbResPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 4),
    _LbResPort_Type()
)
lbResPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPort.setStatus("current")
_LbResState_Type = DisplayString
_LbResState_Object = MibTableColumn
lbResState = _LbResState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 5),
    _LbResState_Type()
)
lbResState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResState.setStatus("current")
_LbResWeight_Type = Integer32
_LbResWeight_Object = MibTableColumn
lbResWeight = _LbResWeight_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 6),
    _LbResWeight_Type()
)
lbResWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResWeight.setStatus("current")
_LbResTotalConnections_Type = Integer32
_LbResTotalConnections_Object = MibTableColumn
lbResTotalConnections = _LbResTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 7),
    _LbResTotalConnections_Type()
)
lbResTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResTotalConnections.setStatus("current")
_LbResCurrentConnections_Type = Integer32
_LbResCurrentConnections_Object = MibTableColumn
lbResCurrentConnections = _LbResCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 2, 1, 8),
    _LbResCurrentConnections_Type()
)
lbResCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResCurrentConnections.setStatus("current")
_LbShowResPoolTable_Object = MibTable
lbShowResPoolTable = _LbShowResPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3)
)
if mibBuilder.loadTexts:
    lbShowResPoolTable.setStatus("current")
_LbShowResPoolEntry_Object = MibTableRow
lbShowResPoolEntry = _LbShowResPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1)
)
lbShowResPoolEntry.setIndexNames(
    (0, "AT-LB-MIB", "lbResPoolIndex"),
    (0, "AT-LB-MIB", "lbResPoolResourceIndex"),
)
if mibBuilder.loadTexts:
    lbShowResPoolEntry.setStatus("current")
_LbResPoolIndex_Type = Integer32
_LbResPoolIndex_Object = MibTableColumn
lbResPoolIndex = _LbResPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 1),
    _LbResPoolIndex_Type()
)
lbResPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolIndex.setStatus("current")
_LbResPoolResourceIndex_Type = Integer32
_LbResPoolResourceIndex_Object = MibTableColumn
lbResPoolResourceIndex = _LbResPoolResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 2),
    _LbResPoolResourceIndex_Type()
)
lbResPoolResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolResourceIndex.setStatus("current")
_LbResPool_Type = DisplayString
_LbResPool_Object = MibTableColumn
lbResPool = _LbResPool_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 3),
    _LbResPool_Type()
)
lbResPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPool.setStatus("current")
_LbResPoolSelectionAlg_Type = DisplayString
_LbResPoolSelectionAlg_Object = MibTableColumn
lbResPoolSelectionAlg = _LbResPoolSelectionAlg_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 4),
    _LbResPoolSelectionAlg_Type()
)
lbResPoolSelectionAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolSelectionAlg.setStatus("current")
_LbResPoolFailOnLast_Type = DisplayString
_LbResPoolFailOnLast_Object = MibTableColumn
lbResPoolFailOnLast = _LbResPoolFailOnLast_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 5),
    _LbResPoolFailOnLast_Type()
)
lbResPoolFailOnLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolFailOnLast.setStatus("current")
_LbResPoolTotalConnections_Type = DisplayString
_LbResPoolTotalConnections_Object = MibTableColumn
lbResPoolTotalConnections = _LbResPoolTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 6),
    _LbResPoolTotalConnections_Type()
)
lbResPoolTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolTotalConnections.setStatus("current")
_LbResPoolResources_Type = DisplayString
_LbResPoolResources_Object = MibTableColumn
lbResPoolResources = _LbResPoolResources_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 3, 1, 7),
    _LbResPoolResources_Type()
)
lbResPoolResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbResPoolResources.setStatus("current")
_LbShowVirtBalTable_Object = MibTable
lbShowVirtBalTable = _LbShowVirtBalTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4)
)
if mibBuilder.loadTexts:
    lbShowVirtBalTable.setStatus("current")
_LbShowVirtBalEntry_Object = MibTableRow
lbShowVirtBalEntry = _LbShowVirtBalEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1)
)
lbShowVirtBalEntry.setIndexNames(
    (0, "AT-LB-MIB", "lbVirtBalIndex"),
)
if mibBuilder.loadTexts:
    lbShowVirtBalEntry.setStatus("current")
_LbVirtBalIndex_Type = Integer32
_LbVirtBalIndex_Object = MibTableColumn
lbVirtBalIndex = _LbVirtBalIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 1),
    _LbVirtBalIndex_Type()
)
lbVirtBalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalIndex.setStatus("current")
_LbVirtBal_Type = DisplayString
_LbVirtBal_Object = MibTableColumn
lbVirtBal = _LbVirtBal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 2),
    _LbVirtBal_Type()
)
lbVirtBal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBal.setStatus("current")
_LbVirtBalPublicIp_Type = IpAddress
_LbVirtBalPublicIp_Object = MibTableColumn
lbVirtBalPublicIp = _LbVirtBalPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 3),
    _LbVirtBalPublicIp_Type()
)
lbVirtBalPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalPublicIp.setStatus("current")
_LbVirtBalPublicPort_Type = Integer32
_LbVirtBalPublicPort_Object = MibTableColumn
lbVirtBalPublicPort = _LbVirtBalPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 4),
    _LbVirtBalPublicPort_Type()
)
lbVirtBalPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalPublicPort.setStatus("current")
_LbVirtBalState_Type = DisplayString
_LbVirtBalState_Object = MibTableColumn
lbVirtBalState = _LbVirtBalState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 5),
    _LbVirtBalState_Type()
)
lbVirtBalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalState.setStatus("current")
_LbVirtBalResPool_Type = DisplayString
_LbVirtBalResPool_Object = MibTableColumn
lbVirtBalResPool = _LbVirtBalResPool_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 6),
    _LbVirtBalResPool_Type()
)
lbVirtBalResPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalResPool.setStatus("current")
_LbVirtBalType_Type = DisplayString
_LbVirtBalType_Object = MibTableColumn
lbVirtBalType = _LbVirtBalType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 7),
    _LbVirtBalType_Type()
)
lbVirtBalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalType.setStatus("current")
_LbVirtBalTotalConnections_Type = Integer32
_LbVirtBalTotalConnections_Object = MibTableColumn
lbVirtBalTotalConnections = _LbVirtBalTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 8),
    _LbVirtBalTotalConnections_Type()
)
lbVirtBalTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalTotalConnections.setStatus("current")
_LbVirtBalAffinity_Type = DisplayString
_LbVirtBalAffinity_Object = MibTableColumn
lbVirtBalAffinity = _LbVirtBalAffinity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 9),
    _LbVirtBalAffinity_Type()
)
lbVirtBalAffinity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalAffinity.setStatus("current")
_LbVirtBalHttpErrorCode_Type = DisplayString
_LbVirtBalHttpErrorCode_Object = MibTableColumn
lbVirtBalHttpErrorCode = _LbVirtBalHttpErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 4, 1, 10),
    _LbVirtBalHttpErrorCode_Type()
)
lbVirtBalHttpErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbVirtBalHttpErrorCode.setStatus("current")
_LbShowAffTable_Object = MibTable
lbShowAffTable = _LbShowAffTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5)
)
if mibBuilder.loadTexts:
    lbShowAffTable.setStatus("current")
_LbShowAffEntry_Object = MibTableRow
lbShowAffEntry = _LbShowAffEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1)
)
lbShowAffEntry.setIndexNames(
    (0, "AT-LB-MIB", "lbAffIndex"),
)
if mibBuilder.loadTexts:
    lbShowAffEntry.setStatus("current")
_LbAffIndex_Type = Integer32
_LbAffIndex_Object = MibTableColumn
lbAffIndex = _LbAffIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 1),
    _LbAffIndex_Type()
)
lbAffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffIndex.setStatus("current")
_LbAffVirtBal_Type = DisplayString
_LbAffVirtBal_Object = MibTableColumn
lbAffVirtBal = _LbAffVirtBal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 2),
    _LbAffVirtBal_Type()
)
lbAffVirtBal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffVirtBal.setStatus("current")
_LbAffClientIp_Type = IpAddress
_LbAffClientIp_Object = MibTableColumn
lbAffClientIp = _LbAffClientIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 3),
    _LbAffClientIp_Type()
)
lbAffClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffClientIp.setStatus("current")
_LbAffCookie_Type = DisplayString
_LbAffCookie_Object = MibTableColumn
lbAffCookie = _LbAffCookie_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 4),
    _LbAffCookie_Type()
)
lbAffCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffCookie.setStatus("current")
_LbAffResource_Type = DisplayString
_LbAffResource_Object = MibTableColumn
lbAffResource = _LbAffResource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 5),
    _LbAffResource_Type()
)
lbAffResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffResource.setStatus("current")
_LbAffExpiry_Type = Integer32
_LbAffExpiry_Object = MibTableColumn
lbAffExpiry = _LbAffExpiry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 5, 1, 6),
    _LbAffExpiry_Type()
)
lbAffExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbAffExpiry.setStatus("current")
_LbShowConTable_Object = MibTable
lbShowConTable = _LbShowConTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6)
)
if mibBuilder.loadTexts:
    lbShowConTable.setStatus("current")
_LbShowConEntry_Object = MibTableRow
lbShowConEntry = _LbShowConEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1)
)
lbShowConEntry.setIndexNames(
    (0, "AT-LB-MIB", "lbConIndex"),
)
if mibBuilder.loadTexts:
    lbShowConEntry.setStatus("current")
_LbConIndex_Type = Integer32
_LbConIndex_Object = MibTableColumn
lbConIndex = _LbConIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1, 1),
    _LbConIndex_Type()
)
lbConIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbConIndex.setStatus("current")
_LbConVirtBal_Type = DisplayString
_LbConVirtBal_Object = MibTableColumn
lbConVirtBal = _LbConVirtBal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1, 2),
    _LbConVirtBal_Type()
)
lbConVirtBal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbConVirtBal.setStatus("current")
_LbConClientIp_Type = IpAddress
_LbConClientIp_Object = MibTableColumn
lbConClientIp = _LbConClientIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1, 3),
    _LbConClientIp_Type()
)
lbConClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbConClientIp.setStatus("current")
_LbConPort_Type = Integer32
_LbConPort_Object = MibTableColumn
lbConPort = _LbConPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1, 4),
    _LbConPort_Type()
)
lbConPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbConPort.setStatus("current")
_LbConResource_Type = DisplayString
_LbConResource_Object = MibTableColumn
lbConResource = _LbConResource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 104, 6, 1, 5),
    _LbConResource_Type()
)
lbConResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbConResource.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-LB-MIB",
    **{"lb": lb,
       "lbShowGlobalTable": lbShowGlobalTable,
       "lbShowGlobalEntry": lbShowGlobalEntry,
       "lbGlobalIndex": lbGlobalIndex,
       "lbAffinityTimeOut": lbAffinityTimeOut,
       "lbOrphanTimeOut": lbOrphanTimeOut,
       "lbCriticalRst": lbCriticalRst,
       "lbTotalResources": lbTotalResources,
       "lbTotalResPools": lbTotalResPools,
       "lbTotalVirtBals": lbTotalVirtBals,
       "lbCurrentConnections": lbCurrentConnections,
       "lbShowResTable": lbShowResTable,
       "lbShowResEntry": lbShowResEntry,
       "lbResIndex": lbResIndex,
       "lbResource": lbResource,
       "lbResIp": lbResIp,
       "lbResPort": lbResPort,
       "lbResState": lbResState,
       "lbResWeight": lbResWeight,
       "lbResTotalConnections": lbResTotalConnections,
       "lbResCurrentConnections": lbResCurrentConnections,
       "lbShowResPoolTable": lbShowResPoolTable,
       "lbShowResPoolEntry": lbShowResPoolEntry,
       "lbResPoolIndex": lbResPoolIndex,
       "lbResPoolResourceIndex": lbResPoolResourceIndex,
       "lbResPool": lbResPool,
       "lbResPoolSelectionAlg": lbResPoolSelectionAlg,
       "lbResPoolFailOnLast": lbResPoolFailOnLast,
       "lbResPoolTotalConnections": lbResPoolTotalConnections,
       "lbResPoolResources": lbResPoolResources,
       "lbShowVirtBalTable": lbShowVirtBalTable,
       "lbShowVirtBalEntry": lbShowVirtBalEntry,
       "lbVirtBalIndex": lbVirtBalIndex,
       "lbVirtBal": lbVirtBal,
       "lbVirtBalPublicIp": lbVirtBalPublicIp,
       "lbVirtBalPublicPort": lbVirtBalPublicPort,
       "lbVirtBalState": lbVirtBalState,
       "lbVirtBalResPool": lbVirtBalResPool,
       "lbVirtBalType": lbVirtBalType,
       "lbVirtBalTotalConnections": lbVirtBalTotalConnections,
       "lbVirtBalAffinity": lbVirtBalAffinity,
       "lbVirtBalHttpErrorCode": lbVirtBalHttpErrorCode,
       "lbShowAffTable": lbShowAffTable,
       "lbShowAffEntry": lbShowAffEntry,
       "lbAffIndex": lbAffIndex,
       "lbAffVirtBal": lbAffVirtBal,
       "lbAffClientIp": lbAffClientIp,
       "lbAffCookie": lbAffCookie,
       "lbAffResource": lbAffResource,
       "lbAffExpiry": lbAffExpiry,
       "lbShowConTable": lbShowConTable,
       "lbShowConEntry": lbShowConEntry,
       "lbConIndex": lbConIndex,
       "lbConVirtBal": lbConVirtBal,
       "lbConClientIp": lbConClientIp,
       "lbConPort": lbConPort,
       "lbConResource": lbConResource}
)
