# SNMP MIB module (CBS-MODULE-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CBS-MODULE-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:47 2024
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

(cbsHwModuleID,) = mibBuilder.importSymbols(
    "CBS-HARDWARE-MIB",
    "cbsHwModuleID")

(cbsVgVapGroupID,) = mibBuilder.importSymbols(
    "CBS-VAPGROUP-MIB",
    "cbsVgVapGroupID")

(cbsMIBs,
 cbsMgmt,
 cbsTraps) = mibBuilder.importSymbols(
    "CROSSBEAM-SYSTEMS-MIB",
    "cbsMIBs",
    "cbsMgmt",
    "cbsTraps")

(KBytes,
 ProductID) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "KBytes",
    "ProductID")

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

cbsModuleResourcesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 3, 3)
)
cbsModuleResourcesMIB.setRevisions(
        ("2002-03-18 00:00",
         "2002-08-01 00:00",
         "2002-12-11 00:00",
         "2007-12-17 00:00",
         "2009-06-10 00:00",
         "2009-07-17 00:00",
         "2009-09-10 00:00",
         "2009-10-16 00:00",
         "2010-01-07 00:00",
         "2010-04-13 00:00",
         "2010-05-13 00:00",
         "2010-05-22 00:00",
         "2010-05-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UtilSeverityLvl(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("major", 2),
          ("minor", 1),
          ("none", 0))
    )



class BadSdramMemCfgStat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad-total-memory-error", 2),
          ("no-error", 0),
          ("no-four-4gig-dimms-error", 3),
          ("no-four-gig-dimms-error", 1))
    )



class BadDiskCfgStat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-error", 0),
          ("no-raid-1-config-error", 1),
          ("no-two-500GB-or-greater-disks-error", 2))
    )



class GuestHealthSeverityLvl(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("major", 2),
          ("minor", 1),
          ("none", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CbsModuleResources_ObjectIdentity = ObjectIdentity
cbsModuleResources = _CbsModuleResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3)
)
_CbsModuleCPULoadTable_Object = MibTable
cbsModuleCPULoadTable = _CbsModuleCPULoadTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cbsModuleCPULoadTable.setStatus("current")
_CbsModuleCPULoadEntry_Object = MibTableRow
cbsModuleCPULoadEntry = _CbsModuleCPULoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 1, 1)
)
cbsModuleCPULoadEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleCPULoadEntry.setStatus("current")
_CbsModuleCPUSpeed_Type = Integer32
_CbsModuleCPUSpeed_Object = MibTableColumn
cbsModuleCPUSpeed = _CbsModuleCPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 1, 1, 1),
    _CbsModuleCPUSpeed_Type()
)
cbsModuleCPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUSpeed.setStatus("current")


class _CbsModuleCPUCount_Type(Integer32):
    """Custom type cbsModuleCPUCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CbsModuleCPUCount_Type.__name__ = "Integer32"
_CbsModuleCPUCount_Object = MibTableColumn
cbsModuleCPUCount = _CbsModuleCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 1, 1, 2),
    _CbsModuleCPUCount_Type()
)
cbsModuleCPUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUCount.setStatus("current")
_CbsModuleCPULoad1_Type = Gauge32
_CbsModuleCPULoad1_Object = MibTableColumn
cbsModuleCPULoad1 = _CbsModuleCPULoad1_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 1, 1, 3),
    _CbsModuleCPULoad1_Type()
)
cbsModuleCPULoad1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPULoad1.setStatus("current")
_CbsModuleCPULoad5_Type = Gauge32
_CbsModuleCPULoad5_Object = MibTableColumn
cbsModuleCPULoad5 = _CbsModuleCPULoad5_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 1, 1, 4),
    _CbsModuleCPULoad5_Type()
)
cbsModuleCPULoad5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPULoad5.setStatus("current")
_CbsModuleCPULoad15_Type = Gauge32
_CbsModuleCPULoad15_Object = MibTableColumn
cbsModuleCPULoad15 = _CbsModuleCPULoad15_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 1, 1, 5),
    _CbsModuleCPULoad15_Type()
)
cbsModuleCPULoad15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPULoad15.setStatus("current")


class _CbsModuleCPUUtil1_Type(Gauge32):
    """Custom type cbsModuleCPUUtil1 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsModuleCPUUtil1_Type.__name__ = "Gauge32"
_CbsModuleCPUUtil1_Object = MibTableColumn
cbsModuleCPUUtil1 = _CbsModuleCPUUtil1_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 1, 1, 6),
    _CbsModuleCPUUtil1_Type()
)
cbsModuleCPUUtil1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUUtil1.setStatus("current")


class _CbsModuleCPUUtil5_Type(Gauge32):
    """Custom type cbsModuleCPUUtil5 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsModuleCPUUtil5_Type.__name__ = "Gauge32"
_CbsModuleCPUUtil5_Object = MibTableColumn
cbsModuleCPUUtil5 = _CbsModuleCPUUtil5_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 1, 1, 7),
    _CbsModuleCPUUtil5_Type()
)
cbsModuleCPUUtil5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUUtil5.setStatus("current")


class _CbsModuleCPUUtil15_Type(Gauge32):
    """Custom type cbsModuleCPUUtil15 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsModuleCPUUtil15_Type.__name__ = "Gauge32"
_CbsModuleCPUUtil15_Object = MibTableColumn
cbsModuleCPUUtil15 = _CbsModuleCPUUtil15_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 1, 1, 8),
    _CbsModuleCPUUtil15_Type()
)
cbsModuleCPUUtil15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUUtil15.setStatus("current")
_CbsModuleMemoryTable_Object = MibTable
cbsModuleMemoryTable = _CbsModuleMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cbsModuleMemoryTable.setStatus("current")
_CbsModuleMemoryEntry_Object = MibTableRow
cbsModuleMemoryEntry = _CbsModuleMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1)
)
cbsModuleMemoryEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleMemoryEntry.setStatus("current")
_CbsModuleMemoryTotal_Type = KBytes
_CbsModuleMemoryTotal_Object = MibTableColumn
cbsModuleMemoryTotal = _CbsModuleMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 1),
    _CbsModuleMemoryTotal_Type()
)
cbsModuleMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryTotal.setStatus("current")
_CbsModuleMemoryUsed_Type = KBytes
_CbsModuleMemoryUsed_Object = MibTableColumn
cbsModuleMemoryUsed = _CbsModuleMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 2),
    _CbsModuleMemoryUsed_Type()
)
cbsModuleMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryUsed.setStatus("current")
_CbsModuleMemoryFree_Type = KBytes
_CbsModuleMemoryFree_Object = MibTableColumn
cbsModuleMemoryFree = _CbsModuleMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 3),
    _CbsModuleMemoryFree_Type()
)
cbsModuleMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryFree.setStatus("current")
_CbsModuleMemoryTotalSwap_Type = KBytes
_CbsModuleMemoryTotalSwap_Object = MibTableColumn
cbsModuleMemoryTotalSwap = _CbsModuleMemoryTotalSwap_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 4),
    _CbsModuleMemoryTotalSwap_Type()
)
cbsModuleMemoryTotalSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryTotalSwap.setStatus("current")
_CbsModuleMemoryAvailSwap_Type = KBytes
_CbsModuleMemoryAvailSwap_Object = MibTableColumn
cbsModuleMemoryAvailSwap = _CbsModuleMemoryAvailSwap_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 5),
    _CbsModuleMemoryAvailSwap_Type()
)
cbsModuleMemoryAvailSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryAvailSwap.setStatus("current")
_CbsModuleMemoryTotalReal_Type = KBytes
_CbsModuleMemoryTotalReal_Object = MibTableColumn
cbsModuleMemoryTotalReal = _CbsModuleMemoryTotalReal_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 6),
    _CbsModuleMemoryTotalReal_Type()
)
cbsModuleMemoryTotalReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryTotalReal.setStatus("current")
_CbsModuleMemoryAvailReal_Type = KBytes
_CbsModuleMemoryAvailReal_Object = MibTableColumn
cbsModuleMemoryAvailReal = _CbsModuleMemoryAvailReal_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 7),
    _CbsModuleMemoryAvailReal_Type()
)
cbsModuleMemoryAvailReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryAvailReal.setStatus("current")
_CbsModuleMemoryTotalFree_Type = KBytes
_CbsModuleMemoryTotalFree_Object = MibTableColumn
cbsModuleMemoryTotalFree = _CbsModuleMemoryTotalFree_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 8),
    _CbsModuleMemoryTotalFree_Type()
)
cbsModuleMemoryTotalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryTotalFree.setStatus("current")
_CbsModuleMemoryShared_Type = KBytes
_CbsModuleMemoryShared_Object = MibTableColumn
cbsModuleMemoryShared = _CbsModuleMemoryShared_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 9),
    _CbsModuleMemoryShared_Type()
)
cbsModuleMemoryShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryShared.setStatus("current")
_CbsModuleMemoryBuffer_Type = KBytes
_CbsModuleMemoryBuffer_Object = MibTableColumn
cbsModuleMemoryBuffer = _CbsModuleMemoryBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 10),
    _CbsModuleMemoryBuffer_Type()
)
cbsModuleMemoryBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryBuffer.setStatus("current")
_CbsModuleMemoryCached_Type = KBytes
_CbsModuleMemoryCached_Object = MibTableColumn
cbsModuleMemoryCached = _CbsModuleMemoryCached_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 11),
    _CbsModuleMemoryCached_Type()
)
cbsModuleMemoryCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryCached.setStatus("current")
_CbsModuleMemoryHiTotal_Type = KBytes
_CbsModuleMemoryHiTotal_Object = MibTableColumn
cbsModuleMemoryHiTotal = _CbsModuleMemoryHiTotal_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 12),
    _CbsModuleMemoryHiTotal_Type()
)
cbsModuleMemoryHiTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryHiTotal.setStatus("current")
_CbsModuleMemoryHiFree_Type = KBytes
_CbsModuleMemoryHiFree_Object = MibTableColumn
cbsModuleMemoryHiFree = _CbsModuleMemoryHiFree_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 13),
    _CbsModuleMemoryHiFree_Type()
)
cbsModuleMemoryHiFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryHiFree.setStatus("current")
_CbsModuleMemoryLoTotal_Type = KBytes
_CbsModuleMemoryLoTotal_Object = MibTableColumn
cbsModuleMemoryLoTotal = _CbsModuleMemoryLoTotal_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 14),
    _CbsModuleMemoryLoTotal_Type()
)
cbsModuleMemoryLoTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryLoTotal.setStatus("current")
_CbsModuleMemoryLoFree_Type = KBytes
_CbsModuleMemoryLoFree_Object = MibTableColumn
cbsModuleMemoryLoFree = _CbsModuleMemoryLoFree_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 2, 1, 15),
    _CbsModuleMemoryLoFree_Type()
)
cbsModuleMemoryLoFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleMemoryLoFree.setStatus("current")
_CbsModuleSwapTable_Object = MibTable
cbsModuleSwapTable = _CbsModuleSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 3)
)
if mibBuilder.loadTexts:
    cbsModuleSwapTable.setStatus("current")
_CbsModuleSwapEntry_Object = MibTableRow
cbsModuleSwapEntry = _CbsModuleSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 3, 1)
)
cbsModuleSwapEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleSwapEntry.setStatus("current")
_CbsModuleSwapTotal_Type = KBytes
_CbsModuleSwapTotal_Object = MibTableColumn
cbsModuleSwapTotal = _CbsModuleSwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 3, 1, 1),
    _CbsModuleSwapTotal_Type()
)
cbsModuleSwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSwapTotal.setStatus("current")
_CbsModuleSwapUsed_Type = KBytes
_CbsModuleSwapUsed_Object = MibTableColumn
cbsModuleSwapUsed = _CbsModuleSwapUsed_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 3, 1, 2),
    _CbsModuleSwapUsed_Type()
)
cbsModuleSwapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSwapUsed.setStatus("current")
_CbsModuleSwapFree_Type = KBytes
_CbsModuleSwapFree_Object = MibTableColumn
cbsModuleSwapFree = _CbsModuleSwapFree_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 3, 1, 3),
    _CbsModuleSwapFree_Type()
)
cbsModuleSwapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSwapFree.setStatus("current")
_CbsModuleDUTable_Object = MibTable
cbsModuleDUTable = _CbsModuleDUTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 4)
)
if mibBuilder.loadTexts:
    cbsModuleDUTable.setStatus("current")
_CbsModuleDUEntry_Object = MibTableRow
cbsModuleDUEntry = _CbsModuleDUEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 4, 1)
)
cbsModuleDUEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleDUEntry.setStatus("current")


class _CbsModuleDURoot_Type(Gauge32):
    """Custom type cbsModuleDURoot based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsModuleDURoot_Type.__name__ = "Gauge32"
_CbsModuleDURoot_Object = MibTableColumn
cbsModuleDURoot = _CbsModuleDURoot_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 4, 1, 1),
    _CbsModuleDURoot_Type()
)
cbsModuleDURoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleDURoot.setStatus("current")


class _CbsModuleDUBoot_Type(Gauge32):
    """Custom type cbsModuleDUBoot based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsModuleDUBoot_Type.__name__ = "Gauge32"
_CbsModuleDUBoot_Object = MibTableColumn
cbsModuleDUBoot = _CbsModuleDUBoot_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 4, 1, 2),
    _CbsModuleDUBoot_Type()
)
cbsModuleDUBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleDUBoot.setStatus("current")


class _CbsModuleDUCbconfig_Type(Gauge32):
    """Custom type cbsModuleDUCbconfig based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsModuleDUCbconfig_Type.__name__ = "Gauge32"
_CbsModuleDUCbconfig_Object = MibTableColumn
cbsModuleDUCbconfig = _CbsModuleDUCbconfig_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 4, 1, 3),
    _CbsModuleDUCbconfig_Type()
)
cbsModuleDUCbconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleDUCbconfig.setStatus("current")


class _CbsModuleDUTftpboot_Type(Gauge32):
    """Custom type cbsModuleDUTftpboot based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsModuleDUTftpboot_Type.__name__ = "Gauge32"
_CbsModuleDUTftpboot_Object = MibTableColumn
cbsModuleDUTftpboot = _CbsModuleDUTftpboot_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 4, 1, 4),
    _CbsModuleDUTftpboot_Type()
)
cbsModuleDUTftpboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleDUTftpboot.setStatus("current")


class _CbsModuleDUMgmt_Type(Gauge32):
    """Custom type cbsModuleDUMgmt based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsModuleDUMgmt_Type.__name__ = "Gauge32"
_CbsModuleDUMgmt_Object = MibTableColumn
cbsModuleDUMgmt = _CbsModuleDUMgmt_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 4, 1, 5),
    _CbsModuleDUMgmt_Type()
)
cbsModuleDUMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleDUMgmt.setStatus("current")


class _CbsModuleDUVar_Type(Gauge32):
    """Custom type cbsModuleDUVar based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsModuleDUVar_Type.__name__ = "Gauge32"
_CbsModuleDUVar_Object = MibTableColumn
cbsModuleDUVar = _CbsModuleDUVar_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 4, 1, 6),
    _CbsModuleDUVar_Type()
)
cbsModuleDUVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleDUVar.setStatus("current")
_CbsModuleFreePageTable_Object = MibTable
cbsModuleFreePageTable = _CbsModuleFreePageTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 5)
)
if mibBuilder.loadTexts:
    cbsModuleFreePageTable.setStatus("current")
_CbsModuleFreePageEntry_Object = MibTableRow
cbsModuleFreePageEntry = _CbsModuleFreePageEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 5, 1)
)
cbsModuleFreePageEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleFreePageEntry.setStatus("current")
_CbsModuleFreePageAvailable_Type = KBytes
_CbsModuleFreePageAvailable_Object = MibTableColumn
cbsModuleFreePageAvailable = _CbsModuleFreePageAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 5, 1, 1),
    _CbsModuleFreePageAvailable_Type()
)
cbsModuleFreePageAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleFreePageAvailable.setStatus("current")
_CbsModuleFreePageThreshold_Type = KBytes
_CbsModuleFreePageThreshold_Object = MibScalar
cbsModuleFreePageThreshold = _CbsModuleFreePageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 5, 1, 2),
    _CbsModuleFreePageThreshold_Type()
)
cbsModuleFreePageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleFreePageThreshold.setStatus("current")
_CbsModuleFreePageSeverity_Type = KBytes
_CbsModuleFreePageSeverity_Object = MibScalar
cbsModuleFreePageSeverity = _CbsModuleFreePageSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 5, 1, 3),
    _CbsModuleFreePageSeverity_Type()
)
cbsModuleFreePageSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleFreePageSeverity.setStatus("current")
_CbsModuleFreePageVapName_Type = DisplayString
_CbsModuleFreePageVapName_Object = MibScalar
cbsModuleFreePageVapName = _CbsModuleFreePageVapName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 5, 1, 4),
    _CbsModuleFreePageVapName_Type()
)
cbsModuleFreePageVapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleFreePageVapName.setStatus("current")
_CbsModuleCPUAvgUtilTable_Object = MibTable
cbsModuleCPUAvgUtilTable = _CbsModuleCPUAvgUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6)
)
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilTable.setStatus("current")
_CbsModuleCPUAvgUtilEntry_Object = MibTableRow
cbsModuleCPUAvgUtilEntry = _CbsModuleCPUAvgUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1)
)
cbsModuleCPUAvgUtilEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilEntry.setStatus("current")
_CbsModuleCPUAvgUtilCore1User_Type = Integer32
_CbsModuleCPUAvgUtilCore1User_Object = MibTableColumn
cbsModuleCPUAvgUtilCore1User = _CbsModuleCPUAvgUtilCore1User_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 1),
    _CbsModuleCPUAvgUtilCore1User_Type()
)
cbsModuleCPUAvgUtilCore1User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore1User.setStatus("current")
_CbsModuleCPUAvgUtilCore1Nice_Type = Integer32
_CbsModuleCPUAvgUtilCore1Nice_Object = MibTableColumn
cbsModuleCPUAvgUtilCore1Nice = _CbsModuleCPUAvgUtilCore1Nice_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 2),
    _CbsModuleCPUAvgUtilCore1Nice_Type()
)
cbsModuleCPUAvgUtilCore1Nice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore1Nice.setStatus("current")
_CbsModuleCPUAvgUtilCore1Syst_Type = Integer32
_CbsModuleCPUAvgUtilCore1Syst_Object = MibTableColumn
cbsModuleCPUAvgUtilCore1Syst = _CbsModuleCPUAvgUtilCore1Syst_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 3),
    _CbsModuleCPUAvgUtilCore1Syst_Type()
)
cbsModuleCPUAvgUtilCore1Syst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore1Syst.setStatus("current")
_CbsModuleCPUAvgUtilCore1Idle_Type = Integer32
_CbsModuleCPUAvgUtilCore1Idle_Object = MibTableColumn
cbsModuleCPUAvgUtilCore1Idle = _CbsModuleCPUAvgUtilCore1Idle_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 4),
    _CbsModuleCPUAvgUtilCore1Idle_Type()
)
cbsModuleCPUAvgUtilCore1Idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore1Idle.setStatus("current")
_CbsModuleCPUAvgUtilCore1IRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore1IRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore1IRQ = _CbsModuleCPUAvgUtilCore1IRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 5),
    _CbsModuleCPUAvgUtilCore1IRQ_Type()
)
cbsModuleCPUAvgUtilCore1IRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore1IRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore1SoftIRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore1SoftIRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore1SoftIRQ = _CbsModuleCPUAvgUtilCore1SoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 6),
    _CbsModuleCPUAvgUtilCore1SoftIRQ_Type()
)
cbsModuleCPUAvgUtilCore1SoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore1SoftIRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore1IOWait_Type = Integer32
_CbsModuleCPUAvgUtilCore1IOWait_Object = MibTableColumn
cbsModuleCPUAvgUtilCore1IOWait = _CbsModuleCPUAvgUtilCore1IOWait_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 7),
    _CbsModuleCPUAvgUtilCore1IOWait_Type()
)
cbsModuleCPUAvgUtilCore1IOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore1IOWait.setStatus("current")
_CbsModuleCPUAvgUtilCore2User_Type = Integer32
_CbsModuleCPUAvgUtilCore2User_Object = MibTableColumn
cbsModuleCPUAvgUtilCore2User = _CbsModuleCPUAvgUtilCore2User_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 8),
    _CbsModuleCPUAvgUtilCore2User_Type()
)
cbsModuleCPUAvgUtilCore2User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore2User.setStatus("current")
_CbsModuleCPUAvgUtilCore2Nice_Type = Integer32
_CbsModuleCPUAvgUtilCore2Nice_Object = MibTableColumn
cbsModuleCPUAvgUtilCore2Nice = _CbsModuleCPUAvgUtilCore2Nice_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 9),
    _CbsModuleCPUAvgUtilCore2Nice_Type()
)
cbsModuleCPUAvgUtilCore2Nice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore2Nice.setStatus("current")
_CbsModuleCPUAvgUtilCore2Syst_Type = Integer32
_CbsModuleCPUAvgUtilCore2Syst_Object = MibTableColumn
cbsModuleCPUAvgUtilCore2Syst = _CbsModuleCPUAvgUtilCore2Syst_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 10),
    _CbsModuleCPUAvgUtilCore2Syst_Type()
)
cbsModuleCPUAvgUtilCore2Syst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore2Syst.setStatus("current")
_CbsModuleCPUAvgUtilCore2Idle_Type = Integer32
_CbsModuleCPUAvgUtilCore2Idle_Object = MibTableColumn
cbsModuleCPUAvgUtilCore2Idle = _CbsModuleCPUAvgUtilCore2Idle_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 11),
    _CbsModuleCPUAvgUtilCore2Idle_Type()
)
cbsModuleCPUAvgUtilCore2Idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore2Idle.setStatus("current")
_CbsModuleCPUAvgUtilCore2IRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore2IRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore2IRQ = _CbsModuleCPUAvgUtilCore2IRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 12),
    _CbsModuleCPUAvgUtilCore2IRQ_Type()
)
cbsModuleCPUAvgUtilCore2IRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore2IRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore2SoftIRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore2SoftIRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore2SoftIRQ = _CbsModuleCPUAvgUtilCore2SoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 13),
    _CbsModuleCPUAvgUtilCore2SoftIRQ_Type()
)
cbsModuleCPUAvgUtilCore2SoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore2SoftIRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore2IOWait_Type = Integer32
_CbsModuleCPUAvgUtilCore2IOWait_Object = MibTableColumn
cbsModuleCPUAvgUtilCore2IOWait = _CbsModuleCPUAvgUtilCore2IOWait_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 14),
    _CbsModuleCPUAvgUtilCore2IOWait_Type()
)
cbsModuleCPUAvgUtilCore2IOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore2IOWait.setStatus("current")
_CbsModuleCPUAvgUtilCore3User_Type = Integer32
_CbsModuleCPUAvgUtilCore3User_Object = MibTableColumn
cbsModuleCPUAvgUtilCore3User = _CbsModuleCPUAvgUtilCore3User_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 15),
    _CbsModuleCPUAvgUtilCore3User_Type()
)
cbsModuleCPUAvgUtilCore3User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore3User.setStatus("current")
_CbsModuleCPUAvgUtilCore3Nice_Type = Integer32
_CbsModuleCPUAvgUtilCore3Nice_Object = MibTableColumn
cbsModuleCPUAvgUtilCore3Nice = _CbsModuleCPUAvgUtilCore3Nice_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 16),
    _CbsModuleCPUAvgUtilCore3Nice_Type()
)
cbsModuleCPUAvgUtilCore3Nice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore3Nice.setStatus("current")
_CbsModuleCPUAvgUtilCore3Syst_Type = Integer32
_CbsModuleCPUAvgUtilCore3Syst_Object = MibTableColumn
cbsModuleCPUAvgUtilCore3Syst = _CbsModuleCPUAvgUtilCore3Syst_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 17),
    _CbsModuleCPUAvgUtilCore3Syst_Type()
)
cbsModuleCPUAvgUtilCore3Syst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore3Syst.setStatus("current")
_CbsModuleCPUAvgUtilCore3Idle_Type = Integer32
_CbsModuleCPUAvgUtilCore3Idle_Object = MibTableColumn
cbsModuleCPUAvgUtilCore3Idle = _CbsModuleCPUAvgUtilCore3Idle_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 18),
    _CbsModuleCPUAvgUtilCore3Idle_Type()
)
cbsModuleCPUAvgUtilCore3Idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore3Idle.setStatus("current")
_CbsModuleCPUAvgUtilCore3IRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore3IRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore3IRQ = _CbsModuleCPUAvgUtilCore3IRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 19),
    _CbsModuleCPUAvgUtilCore3IRQ_Type()
)
cbsModuleCPUAvgUtilCore3IRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore3IRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore3SoftIRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore3SoftIRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore3SoftIRQ = _CbsModuleCPUAvgUtilCore3SoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 20),
    _CbsModuleCPUAvgUtilCore3SoftIRQ_Type()
)
cbsModuleCPUAvgUtilCore3SoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore3SoftIRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore3IOWait_Type = Integer32
_CbsModuleCPUAvgUtilCore3IOWait_Object = MibTableColumn
cbsModuleCPUAvgUtilCore3IOWait = _CbsModuleCPUAvgUtilCore3IOWait_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 21),
    _CbsModuleCPUAvgUtilCore3IOWait_Type()
)
cbsModuleCPUAvgUtilCore3IOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore3IOWait.setStatus("current")
_CbsModuleCPUAvgUtilCore4User_Type = Integer32
_CbsModuleCPUAvgUtilCore4User_Object = MibTableColumn
cbsModuleCPUAvgUtilCore4User = _CbsModuleCPUAvgUtilCore4User_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 22),
    _CbsModuleCPUAvgUtilCore4User_Type()
)
cbsModuleCPUAvgUtilCore4User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore4User.setStatus("current")
_CbsModuleCPUAvgUtilCore4Nice_Type = Integer32
_CbsModuleCPUAvgUtilCore4Nice_Object = MibTableColumn
cbsModuleCPUAvgUtilCore4Nice = _CbsModuleCPUAvgUtilCore4Nice_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 23),
    _CbsModuleCPUAvgUtilCore4Nice_Type()
)
cbsModuleCPUAvgUtilCore4Nice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore4Nice.setStatus("current")
_CbsModuleCPUAvgUtilCore4Syst_Type = Integer32
_CbsModuleCPUAvgUtilCore4Syst_Object = MibTableColumn
cbsModuleCPUAvgUtilCore4Syst = _CbsModuleCPUAvgUtilCore4Syst_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 24),
    _CbsModuleCPUAvgUtilCore4Syst_Type()
)
cbsModuleCPUAvgUtilCore4Syst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore4Syst.setStatus("current")
_CbsModuleCPUAvgUtilCore4Idle_Type = Integer32
_CbsModuleCPUAvgUtilCore4Idle_Object = MibTableColumn
cbsModuleCPUAvgUtilCore4Idle = _CbsModuleCPUAvgUtilCore4Idle_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 25),
    _CbsModuleCPUAvgUtilCore4Idle_Type()
)
cbsModuleCPUAvgUtilCore4Idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore4Idle.setStatus("current")
_CbsModuleCPUAvgUtilCore4IRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore4IRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore4IRQ = _CbsModuleCPUAvgUtilCore4IRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 26),
    _CbsModuleCPUAvgUtilCore4IRQ_Type()
)
cbsModuleCPUAvgUtilCore4IRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore4IRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore4SoftIRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore4SoftIRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore4SoftIRQ = _CbsModuleCPUAvgUtilCore4SoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 27),
    _CbsModuleCPUAvgUtilCore4SoftIRQ_Type()
)
cbsModuleCPUAvgUtilCore4SoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore4SoftIRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore4IOWait_Type = Integer32
_CbsModuleCPUAvgUtilCore4IOWait_Object = MibTableColumn
cbsModuleCPUAvgUtilCore4IOWait = _CbsModuleCPUAvgUtilCore4IOWait_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 28),
    _CbsModuleCPUAvgUtilCore4IOWait_Type()
)
cbsModuleCPUAvgUtilCore4IOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore4IOWait.setStatus("current")
_CbsModuleCPUAvgUtilCore5User_Type = Integer32
_CbsModuleCPUAvgUtilCore5User_Object = MibTableColumn
cbsModuleCPUAvgUtilCore5User = _CbsModuleCPUAvgUtilCore5User_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 29),
    _CbsModuleCPUAvgUtilCore5User_Type()
)
cbsModuleCPUAvgUtilCore5User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore5User.setStatus("current")
_CbsModuleCPUAvgUtilCore5Nice_Type = Integer32
_CbsModuleCPUAvgUtilCore5Nice_Object = MibTableColumn
cbsModuleCPUAvgUtilCore5Nice = _CbsModuleCPUAvgUtilCore5Nice_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 30),
    _CbsModuleCPUAvgUtilCore5Nice_Type()
)
cbsModuleCPUAvgUtilCore5Nice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore5Nice.setStatus("current")
_CbsModuleCPUAvgUtilCore5Syst_Type = Integer32
_CbsModuleCPUAvgUtilCore5Syst_Object = MibTableColumn
cbsModuleCPUAvgUtilCore5Syst = _CbsModuleCPUAvgUtilCore5Syst_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 31),
    _CbsModuleCPUAvgUtilCore5Syst_Type()
)
cbsModuleCPUAvgUtilCore5Syst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore5Syst.setStatus("current")
_CbsModuleCPUAvgUtilCore5Idle_Type = Integer32
_CbsModuleCPUAvgUtilCore5Idle_Object = MibTableColumn
cbsModuleCPUAvgUtilCore5Idle = _CbsModuleCPUAvgUtilCore5Idle_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 32),
    _CbsModuleCPUAvgUtilCore5Idle_Type()
)
cbsModuleCPUAvgUtilCore5Idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore5Idle.setStatus("current")
_CbsModuleCPUAvgUtilCore5IRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore5IRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore5IRQ = _CbsModuleCPUAvgUtilCore5IRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 33),
    _CbsModuleCPUAvgUtilCore5IRQ_Type()
)
cbsModuleCPUAvgUtilCore5IRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore5IRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore5SoftIRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore5SoftIRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore5SoftIRQ = _CbsModuleCPUAvgUtilCore5SoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 34),
    _CbsModuleCPUAvgUtilCore5SoftIRQ_Type()
)
cbsModuleCPUAvgUtilCore5SoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore5SoftIRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore5IOWait_Type = Integer32
_CbsModuleCPUAvgUtilCore5IOWait_Object = MibTableColumn
cbsModuleCPUAvgUtilCore5IOWait = _CbsModuleCPUAvgUtilCore5IOWait_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 35),
    _CbsModuleCPUAvgUtilCore5IOWait_Type()
)
cbsModuleCPUAvgUtilCore5IOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore5IOWait.setStatus("current")
_CbsModuleCPUAvgUtilCore6User_Type = Integer32
_CbsModuleCPUAvgUtilCore6User_Object = MibTableColumn
cbsModuleCPUAvgUtilCore6User = _CbsModuleCPUAvgUtilCore6User_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 36),
    _CbsModuleCPUAvgUtilCore6User_Type()
)
cbsModuleCPUAvgUtilCore6User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore6User.setStatus("current")
_CbsModuleCPUAvgUtilCore6Nice_Type = Integer32
_CbsModuleCPUAvgUtilCore6Nice_Object = MibTableColumn
cbsModuleCPUAvgUtilCore6Nice = _CbsModuleCPUAvgUtilCore6Nice_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 37),
    _CbsModuleCPUAvgUtilCore6Nice_Type()
)
cbsModuleCPUAvgUtilCore6Nice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore6Nice.setStatus("current")
_CbsModuleCPUAvgUtilCore6Syst_Type = Integer32
_CbsModuleCPUAvgUtilCore6Syst_Object = MibTableColumn
cbsModuleCPUAvgUtilCore6Syst = _CbsModuleCPUAvgUtilCore6Syst_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 38),
    _CbsModuleCPUAvgUtilCore6Syst_Type()
)
cbsModuleCPUAvgUtilCore6Syst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore6Syst.setStatus("current")
_CbsModuleCPUAvgUtilCore6Idle_Type = Integer32
_CbsModuleCPUAvgUtilCore6Idle_Object = MibTableColumn
cbsModuleCPUAvgUtilCore6Idle = _CbsModuleCPUAvgUtilCore6Idle_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 39),
    _CbsModuleCPUAvgUtilCore6Idle_Type()
)
cbsModuleCPUAvgUtilCore6Idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore6Idle.setStatus("current")
_CbsModuleCPUAvgUtilCore6IRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore6IRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore6IRQ = _CbsModuleCPUAvgUtilCore6IRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 40),
    _CbsModuleCPUAvgUtilCore6IRQ_Type()
)
cbsModuleCPUAvgUtilCore6IRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore6IRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore6SoftIRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore6SoftIRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore6SoftIRQ = _CbsModuleCPUAvgUtilCore6SoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 41),
    _CbsModuleCPUAvgUtilCore6SoftIRQ_Type()
)
cbsModuleCPUAvgUtilCore6SoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore6SoftIRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore6IOWait_Type = Integer32
_CbsModuleCPUAvgUtilCore6IOWait_Object = MibTableColumn
cbsModuleCPUAvgUtilCore6IOWait = _CbsModuleCPUAvgUtilCore6IOWait_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 42),
    _CbsModuleCPUAvgUtilCore6IOWait_Type()
)
cbsModuleCPUAvgUtilCore6IOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore6IOWait.setStatus("current")
_CbsModuleCPUAvgUtilCore7User_Type = Integer32
_CbsModuleCPUAvgUtilCore7User_Object = MibTableColumn
cbsModuleCPUAvgUtilCore7User = _CbsModuleCPUAvgUtilCore7User_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 43),
    _CbsModuleCPUAvgUtilCore7User_Type()
)
cbsModuleCPUAvgUtilCore7User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore7User.setStatus("current")
_CbsModuleCPUAvgUtilCore7Nice_Type = Integer32
_CbsModuleCPUAvgUtilCore7Nice_Object = MibTableColumn
cbsModuleCPUAvgUtilCore7Nice = _CbsModuleCPUAvgUtilCore7Nice_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 44),
    _CbsModuleCPUAvgUtilCore7Nice_Type()
)
cbsModuleCPUAvgUtilCore7Nice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore7Nice.setStatus("current")
_CbsModuleCPUAvgUtilCore7Syst_Type = Integer32
_CbsModuleCPUAvgUtilCore7Syst_Object = MibTableColumn
cbsModuleCPUAvgUtilCore7Syst = _CbsModuleCPUAvgUtilCore7Syst_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 45),
    _CbsModuleCPUAvgUtilCore7Syst_Type()
)
cbsModuleCPUAvgUtilCore7Syst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore7Syst.setStatus("current")
_CbsModuleCPUAvgUtilCore7Idle_Type = Integer32
_CbsModuleCPUAvgUtilCore7Idle_Object = MibTableColumn
cbsModuleCPUAvgUtilCore7Idle = _CbsModuleCPUAvgUtilCore7Idle_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 46),
    _CbsModuleCPUAvgUtilCore7Idle_Type()
)
cbsModuleCPUAvgUtilCore7Idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore7Idle.setStatus("current")
_CbsModuleCPUAvgUtilCore7IRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore7IRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore7IRQ = _CbsModuleCPUAvgUtilCore7IRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 47),
    _CbsModuleCPUAvgUtilCore7IRQ_Type()
)
cbsModuleCPUAvgUtilCore7IRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore7IRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore7SoftIRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore7SoftIRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore7SoftIRQ = _CbsModuleCPUAvgUtilCore7SoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 48),
    _CbsModuleCPUAvgUtilCore7SoftIRQ_Type()
)
cbsModuleCPUAvgUtilCore7SoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore7SoftIRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore7IOWait_Type = Integer32
_CbsModuleCPUAvgUtilCore7IOWait_Object = MibTableColumn
cbsModuleCPUAvgUtilCore7IOWait = _CbsModuleCPUAvgUtilCore7IOWait_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 49),
    _CbsModuleCPUAvgUtilCore7IOWait_Type()
)
cbsModuleCPUAvgUtilCore7IOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore7IOWait.setStatus("current")
_CbsModuleCPUAvgUtilCore8User_Type = Integer32
_CbsModuleCPUAvgUtilCore8User_Object = MibTableColumn
cbsModuleCPUAvgUtilCore8User = _CbsModuleCPUAvgUtilCore8User_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 50),
    _CbsModuleCPUAvgUtilCore8User_Type()
)
cbsModuleCPUAvgUtilCore8User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore8User.setStatus("current")
_CbsModuleCPUAvgUtilCore8Nice_Type = Integer32
_CbsModuleCPUAvgUtilCore8Nice_Object = MibTableColumn
cbsModuleCPUAvgUtilCore8Nice = _CbsModuleCPUAvgUtilCore8Nice_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 51),
    _CbsModuleCPUAvgUtilCore8Nice_Type()
)
cbsModuleCPUAvgUtilCore8Nice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore8Nice.setStatus("current")
_CbsModuleCPUAvgUtilCore8Syst_Type = Integer32
_CbsModuleCPUAvgUtilCore8Syst_Object = MibTableColumn
cbsModuleCPUAvgUtilCore8Syst = _CbsModuleCPUAvgUtilCore8Syst_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 52),
    _CbsModuleCPUAvgUtilCore8Syst_Type()
)
cbsModuleCPUAvgUtilCore8Syst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore8Syst.setStatus("current")
_CbsModuleCPUAvgUtilCore8Idle_Type = Integer32
_CbsModuleCPUAvgUtilCore8Idle_Object = MibTableColumn
cbsModuleCPUAvgUtilCore8Idle = _CbsModuleCPUAvgUtilCore8Idle_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 53),
    _CbsModuleCPUAvgUtilCore8Idle_Type()
)
cbsModuleCPUAvgUtilCore8Idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore8Idle.setStatus("current")
_CbsModuleCPUAvgUtilCore8IRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore8IRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore8IRQ = _CbsModuleCPUAvgUtilCore8IRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 54),
    _CbsModuleCPUAvgUtilCore8IRQ_Type()
)
cbsModuleCPUAvgUtilCore8IRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore8IRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore8SoftIRQ_Type = Integer32
_CbsModuleCPUAvgUtilCore8SoftIRQ_Object = MibTableColumn
cbsModuleCPUAvgUtilCore8SoftIRQ = _CbsModuleCPUAvgUtilCore8SoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 55),
    _CbsModuleCPUAvgUtilCore8SoftIRQ_Type()
)
cbsModuleCPUAvgUtilCore8SoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore8SoftIRQ.setStatus("current")
_CbsModuleCPUAvgUtilCore8IOWait_Type = Integer32
_CbsModuleCPUAvgUtilCore8IOWait_Object = MibTableColumn
cbsModuleCPUAvgUtilCore8IOWait = _CbsModuleCPUAvgUtilCore8IOWait_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 6, 1, 56),
    _CbsModuleCPUAvgUtilCore8IOWait_Type()
)
cbsModuleCPUAvgUtilCore8IOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCPUAvgUtilCore8IOWait.setStatus("current")
_CbsModuleSDPTable_Object = MibTable
cbsModuleSDPTable = _CbsModuleSDPTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7)
)
if mibBuilder.loadTexts:
    cbsModuleSDPTable.setStatus("current")
_CbsModuleSDPEntry_Object = MibTableRow
cbsModuleSDPEntry = _CbsModuleSDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1)
)
cbsModuleSDPEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleSDPEntry.setStatus("current")
_CbsModuleSDP0OutPkts_Type = Counter64
_CbsModuleSDP0OutPkts_Object = MibTableColumn
cbsModuleSDP0OutPkts = _CbsModuleSDP0OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 1),
    _CbsModuleSDP0OutPkts_Type()
)
cbsModuleSDP0OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP0OutPkts.setStatus("current")
_CbsModuleSDP0OutOctets_Type = Counter64
_CbsModuleSDP0OutOctets_Object = MibTableColumn
cbsModuleSDP0OutOctets = _CbsModuleSDP0OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 2),
    _CbsModuleSDP0OutOctets_Type()
)
cbsModuleSDP0OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP0OutOctets.setStatus("current")
_CbsModuleSDP0InPkts_Type = Counter64
_CbsModuleSDP0InPkts_Object = MibTableColumn
cbsModuleSDP0InPkts = _CbsModuleSDP0InPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 3),
    _CbsModuleSDP0InPkts_Type()
)
cbsModuleSDP0InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP0InPkts.setStatus("current")
_CbsModuleSDP0InOctets_Type = Counter64
_CbsModuleSDP0InOctets_Object = MibTableColumn
cbsModuleSDP0InOctets = _CbsModuleSDP0InOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 4),
    _CbsModuleSDP0InOctets_Type()
)
cbsModuleSDP0InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP0InOctets.setStatus("current")
_CbsModuleSDP1OutPkts_Type = Counter64
_CbsModuleSDP1OutPkts_Object = MibTableColumn
cbsModuleSDP1OutPkts = _CbsModuleSDP1OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 5),
    _CbsModuleSDP1OutPkts_Type()
)
cbsModuleSDP1OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP1OutPkts.setStatus("current")
_CbsModuleSDP1OutOctets_Type = Counter64
_CbsModuleSDP1OutOctets_Object = MibTableColumn
cbsModuleSDP1OutOctets = _CbsModuleSDP1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 6),
    _CbsModuleSDP1OutOctets_Type()
)
cbsModuleSDP1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP1OutOctets.setStatus("current")
_CbsModuleSDP1InPkts_Type = Counter64
_CbsModuleSDP1InPkts_Object = MibTableColumn
cbsModuleSDP1InPkts = _CbsModuleSDP1InPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 7),
    _CbsModuleSDP1InPkts_Type()
)
cbsModuleSDP1InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP1InPkts.setStatus("current")
_CbsModuleSDP1InOctets_Type = Counter64
_CbsModuleSDP1InOctets_Object = MibTableColumn
cbsModuleSDP1InOctets = _CbsModuleSDP1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 8),
    _CbsModuleSDP1InOctets_Type()
)
cbsModuleSDP1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP1InOctets.setStatus("current")
_CbsModuleSDP2OutPkts_Type = Counter64
_CbsModuleSDP2OutPkts_Object = MibTableColumn
cbsModuleSDP2OutPkts = _CbsModuleSDP2OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 9),
    _CbsModuleSDP2OutPkts_Type()
)
cbsModuleSDP2OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP2OutPkts.setStatus("current")
_CbsModuleSDP2OutOctets_Type = Counter64
_CbsModuleSDP2OutOctets_Object = MibTableColumn
cbsModuleSDP2OutOctets = _CbsModuleSDP2OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 10),
    _CbsModuleSDP2OutOctets_Type()
)
cbsModuleSDP2OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP2OutOctets.setStatus("current")
_CbsModuleSDP2InPkts_Type = Counter64
_CbsModuleSDP2InPkts_Object = MibTableColumn
cbsModuleSDP2InPkts = _CbsModuleSDP2InPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 11),
    _CbsModuleSDP2InPkts_Type()
)
cbsModuleSDP2InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP2InPkts.setStatus("current")
_CbsModuleSDP2InOctets_Type = Counter64
_CbsModuleSDP2InOctets_Object = MibTableColumn
cbsModuleSDP2InOctets = _CbsModuleSDP2InOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 12),
    _CbsModuleSDP2InOctets_Type()
)
cbsModuleSDP2InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP2InOctets.setStatus("current")
_CbsModuleSDP3OutPkts_Type = Counter64
_CbsModuleSDP3OutPkts_Object = MibTableColumn
cbsModuleSDP3OutPkts = _CbsModuleSDP3OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 13),
    _CbsModuleSDP3OutPkts_Type()
)
cbsModuleSDP3OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP3OutPkts.setStatus("current")
_CbsModuleSDP3OutOctets_Type = Counter64
_CbsModuleSDP3OutOctets_Object = MibTableColumn
cbsModuleSDP3OutOctets = _CbsModuleSDP3OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 14),
    _CbsModuleSDP3OutOctets_Type()
)
cbsModuleSDP3OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP3OutOctets.setStatus("current")
_CbsModuleSDP3InPkts_Type = Counter64
_CbsModuleSDP3InPkts_Object = MibTableColumn
cbsModuleSDP3InPkts = _CbsModuleSDP3InPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 15),
    _CbsModuleSDP3InPkts_Type()
)
cbsModuleSDP3InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP3InPkts.setStatus("current")
_CbsModuleSDP3InOctets_Type = Counter64
_CbsModuleSDP3InOctets_Object = MibTableColumn
cbsModuleSDP3InOctets = _CbsModuleSDP3InOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 16),
    _CbsModuleSDP3InOctets_Type()
)
cbsModuleSDP3InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP3InOctets.setStatus("current")
_CbsModuleSDP4OutPkts_Type = Counter64
_CbsModuleSDP4OutPkts_Object = MibTableColumn
cbsModuleSDP4OutPkts = _CbsModuleSDP4OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 17),
    _CbsModuleSDP4OutPkts_Type()
)
cbsModuleSDP4OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP4OutPkts.setStatus("current")
_CbsModuleSDP4OutOctets_Type = Counter64
_CbsModuleSDP4OutOctets_Object = MibTableColumn
cbsModuleSDP4OutOctets = _CbsModuleSDP4OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 18),
    _CbsModuleSDP4OutOctets_Type()
)
cbsModuleSDP4OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP4OutOctets.setStatus("current")
_CbsModuleSDP4InPkts_Type = Counter64
_CbsModuleSDP4InPkts_Object = MibTableColumn
cbsModuleSDP4InPkts = _CbsModuleSDP4InPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 19),
    _CbsModuleSDP4InPkts_Type()
)
cbsModuleSDP4InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP4InPkts.setStatus("current")
_CbsModuleSDP4InOctets_Type = Counter64
_CbsModuleSDP4InOctets_Object = MibTableColumn
cbsModuleSDP4InOctets = _CbsModuleSDP4InOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 20),
    _CbsModuleSDP4InOctets_Type()
)
cbsModuleSDP4InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP4InOctets.setStatus("current")
_CbsModuleSDP5OutPkts_Type = Counter64
_CbsModuleSDP5OutPkts_Object = MibTableColumn
cbsModuleSDP5OutPkts = _CbsModuleSDP5OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 21),
    _CbsModuleSDP5OutPkts_Type()
)
cbsModuleSDP5OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP5OutPkts.setStatus("current")
_CbsModuleSDP5OutOctets_Type = Counter64
_CbsModuleSDP5OutOctets_Object = MibTableColumn
cbsModuleSDP5OutOctets = _CbsModuleSDP5OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 22),
    _CbsModuleSDP5OutOctets_Type()
)
cbsModuleSDP5OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP5OutOctets.setStatus("current")
_CbsModuleSDP5InPkts_Type = Counter64
_CbsModuleSDP5InPkts_Object = MibTableColumn
cbsModuleSDP5InPkts = _CbsModuleSDP5InPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 23),
    _CbsModuleSDP5InPkts_Type()
)
cbsModuleSDP5InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP5InPkts.setStatus("current")
_CbsModuleSDP5InOctets_Type = Counter64
_CbsModuleSDP5InOctets_Object = MibTableColumn
cbsModuleSDP5InOctets = _CbsModuleSDP5InOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 24),
    _CbsModuleSDP5InOctets_Type()
)
cbsModuleSDP5InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP5InOctets.setStatus("current")
_CbsModuleSDP6OutPkts_Type = Counter64
_CbsModuleSDP6OutPkts_Object = MibTableColumn
cbsModuleSDP6OutPkts = _CbsModuleSDP6OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 25),
    _CbsModuleSDP6OutPkts_Type()
)
cbsModuleSDP6OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP6OutPkts.setStatus("current")
_CbsModuleSDP6OutOctets_Type = Counter64
_CbsModuleSDP6OutOctets_Object = MibTableColumn
cbsModuleSDP6OutOctets = _CbsModuleSDP6OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 26),
    _CbsModuleSDP6OutOctets_Type()
)
cbsModuleSDP6OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP6OutOctets.setStatus("current")
_CbsModuleSDP6InPkts_Type = Counter64
_CbsModuleSDP6InPkts_Object = MibTableColumn
cbsModuleSDP6InPkts = _CbsModuleSDP6InPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 27),
    _CbsModuleSDP6InPkts_Type()
)
cbsModuleSDP6InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP6InPkts.setStatus("current")
_CbsModuleSDP6InOctets_Type = Counter64
_CbsModuleSDP6InOctets_Object = MibTableColumn
cbsModuleSDP6InOctets = _CbsModuleSDP6InOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 28),
    _CbsModuleSDP6InOctets_Type()
)
cbsModuleSDP6InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP6InOctets.setStatus("current")
_CbsModuleSDP7OutPkts_Type = Counter64
_CbsModuleSDP7OutPkts_Object = MibTableColumn
cbsModuleSDP7OutPkts = _CbsModuleSDP7OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 29),
    _CbsModuleSDP7OutPkts_Type()
)
cbsModuleSDP7OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP7OutPkts.setStatus("current")
_CbsModuleSDP7OutOctets_Type = Counter64
_CbsModuleSDP7OutOctets_Object = MibTableColumn
cbsModuleSDP7OutOctets = _CbsModuleSDP7OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 30),
    _CbsModuleSDP7OutOctets_Type()
)
cbsModuleSDP7OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP7OutOctets.setStatus("current")
_CbsModuleSDP7InPkts_Type = Counter64
_CbsModuleSDP7InPkts_Object = MibTableColumn
cbsModuleSDP7InPkts = _CbsModuleSDP7InPkts_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 31),
    _CbsModuleSDP7InPkts_Type()
)
cbsModuleSDP7InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP7InPkts.setStatus("current")
_CbsModuleSDP7InOctets_Type = Counter64
_CbsModuleSDP7InOctets_Object = MibTableColumn
cbsModuleSDP7InOctets = _CbsModuleSDP7InOctets_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 7, 1, 32),
    _CbsModuleSDP7InOctets_Type()
)
cbsModuleSDP7InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSDP7InOctets.setStatus("current")
_CbsModuleUptimeTable_Object = MibTable
cbsModuleUptimeTable = _CbsModuleUptimeTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 8)
)
if mibBuilder.loadTexts:
    cbsModuleUptimeTable.setStatus("current")
_CbsModuleUptimeEntry_Object = MibTableRow
cbsModuleUptimeEntry = _CbsModuleUptimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 8, 1)
)
cbsModuleUptimeEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleUptimeEntry.setStatus("current")
_CbsModuleUptime_Type = TimeTicks
_CbsModuleUptime_Object = MibTableColumn
cbsModuleUptime = _CbsModuleUptime_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 8, 1, 1),
    _CbsModuleUptime_Type()
)
cbsModuleUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleUptime.setStatus("current")
_CbsModuleNPMFlowCountTable_Object = MibTable
cbsModuleNPMFlowCountTable = _CbsModuleNPMFlowCountTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 9)
)
if mibBuilder.loadTexts:
    cbsModuleNPMFlowCountTable.setStatus("current")
_CbsModuleNPMFlowCountEntry_Object = MibTableRow
cbsModuleNPMFlowCountEntry = _CbsModuleNPMFlowCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 9, 1)
)
cbsModuleNPMFlowCountEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleNPMFlowCountEntry.setStatus("current")
_CbsModuleNPMFlowCount_Type = Integer32
_CbsModuleNPMFlowCount_Object = MibTableColumn
cbsModuleNPMFlowCount = _CbsModuleNPMFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 9, 1, 1),
    _CbsModuleNPMFlowCount_Type()
)
cbsModuleNPMFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleNPMFlowCount.setStatus("current")
_CbsModuleAppMonTable_Object = MibTable
cbsModuleAppMonTable = _CbsModuleAppMonTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10)
)
if mibBuilder.loadTexts:
    cbsModuleAppMonTable.setStatus("current")
_CbsModuleAppMonEntry_Object = MibTableRow
cbsModuleAppMonEntry = _CbsModuleAppMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1)
)
cbsModuleAppMonEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleAppMonEntry.setStatus("current")
_CbsModuleAppName_Type = DisplayString
_CbsModuleAppName_Object = MibTableColumn
cbsModuleAppName = _CbsModuleAppName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 1),
    _CbsModuleAppName_Type()
)
cbsModuleAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleAppName.setStatus("current")
_CbsModuleAppVersion_Type = DisplayString
_CbsModuleAppVersion_Object = MibTableColumn
cbsModuleAppVersion = _CbsModuleAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 2),
    _CbsModuleAppVersion_Type()
)
cbsModuleAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleAppVersion.setStatus("current")
_CbsModuleAppRelease_Type = DisplayString
_CbsModuleAppRelease_Object = MibTableColumn
cbsModuleAppRelease = _CbsModuleAppRelease_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 3),
    _CbsModuleAppRelease_Type()
)
cbsModuleAppRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleAppRelease.setStatus("current")
_CbsModuleAppCPMHostName_Type = DisplayString
_CbsModuleAppCPMHostName_Object = MibTableColumn
cbsModuleAppCPMHostName = _CbsModuleAppCPMHostName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 4),
    _CbsModuleAppCPMHostName_Type()
)
cbsModuleAppCPMHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbsModuleAppCPMHostName.setStatus("current")
_CbsModuleAppCPMIPAddress_Type = DisplayString
_CbsModuleAppCPMIPAddress_Object = MibTableColumn
cbsModuleAppCPMIPAddress = _CbsModuleAppCPMIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 5),
    _CbsModuleAppCPMIPAddress_Type()
)
cbsModuleAppCPMIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbsModuleAppCPMIPAddress.setStatus("current")
_CbsModuleAppVAPGroupName_Type = DisplayString
_CbsModuleAppVAPGroupName_Object = MibTableColumn
cbsModuleAppVAPGroupName = _CbsModuleAppVAPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 6),
    _CbsModuleAppVAPGroupName_Type()
)
cbsModuleAppVAPGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleAppVAPGroupName.setStatus("current")
_CbsModuleAppVAPIndex_Type = Integer32
_CbsModuleAppVAPIndex_Object = MibTableColumn
cbsModuleAppVAPIndex = _CbsModuleAppVAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 7),
    _CbsModuleAppVAPIndex_Type()
)
cbsModuleAppVAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleAppVAPIndex.setStatus("current")
_CbsModuleAppOldState_Type = DisplayString
_CbsModuleAppOldState_Object = MibTableColumn
cbsModuleAppOldState = _CbsModuleAppOldState_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 8),
    _CbsModuleAppOldState_Type()
)
cbsModuleAppOldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleAppOldState.setStatus("current")
_CbsModuleAppNewState_Type = DisplayString
_CbsModuleAppNewState_Object = MibTableColumn
cbsModuleAppNewState = _CbsModuleAppNewState_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 9),
    _CbsModuleAppNewState_Type()
)
cbsModuleAppNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleAppNewState.setStatus("current")
_CbsModuleRSWName_Type = DisplayString
_CbsModuleRSWName_Object = MibTableColumn
cbsModuleRSWName = _CbsModuleRSWName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 10),
    _CbsModuleRSWName_Type()
)
cbsModuleRSWName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleRSWName.setStatus("current")
_CbsModuleRSWVersion_Type = DisplayString
_CbsModuleRSWVersion_Object = MibTableColumn
cbsModuleRSWVersion = _CbsModuleRSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 11),
    _CbsModuleRSWVersion_Type()
)
cbsModuleRSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleRSWVersion.setStatus("current")
_CbsModuleRSWRelease_Type = DisplayString
_CbsModuleRSWRelease_Object = MibTableColumn
cbsModuleRSWRelease = _CbsModuleRSWRelease_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 12),
    _CbsModuleRSWRelease_Type()
)
cbsModuleRSWRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleRSWRelease.setStatus("current")
_CbsModuleRSWStartOnBoot_Type = DisplayString
_CbsModuleRSWStartOnBoot_Object = MibTableColumn
cbsModuleRSWStartOnBoot = _CbsModuleRSWStartOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 13),
    _CbsModuleRSWStartOnBoot_Type()
)
cbsModuleRSWStartOnBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleRSWStartOnBoot.setStatus("current")
_CbsModuleRSWCPMHostName_Type = DisplayString
_CbsModuleRSWCPMHostName_Object = MibTableColumn
cbsModuleRSWCPMHostName = _CbsModuleRSWCPMHostName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 14),
    _CbsModuleRSWCPMHostName_Type()
)
cbsModuleRSWCPMHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbsModuleRSWCPMHostName.setStatus("current")
_CbsModuleRSWCPMIPAddress_Type = DisplayString
_CbsModuleRSWCPMIPAddress_Object = MibTableColumn
cbsModuleRSWCPMIPAddress = _CbsModuleRSWCPMIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 15),
    _CbsModuleRSWCPMIPAddress_Type()
)
cbsModuleRSWCPMIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbsModuleRSWCPMIPAddress.setStatus("current")
_CbsModuleRSWVAPGroupName_Type = DisplayString
_CbsModuleRSWVAPGroupName_Object = MibTableColumn
cbsModuleRSWVAPGroupName = _CbsModuleRSWVAPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 16),
    _CbsModuleRSWVAPGroupName_Type()
)
cbsModuleRSWVAPGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleRSWVAPGroupName.setStatus("current")
_CbsModuleRSWVAPIndex_Type = Integer32
_CbsModuleRSWVAPIndex_Object = MibTableColumn
cbsModuleRSWVAPIndex = _CbsModuleRSWVAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 17),
    _CbsModuleRSWVAPIndex_Type()
)
cbsModuleRSWVAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleRSWVAPIndex.setStatus("current")
_CbsModuleRSWOldState_Type = DisplayString
_CbsModuleRSWOldState_Object = MibTableColumn
cbsModuleRSWOldState = _CbsModuleRSWOldState_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 18),
    _CbsModuleRSWOldState_Type()
)
cbsModuleRSWOldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleRSWOldState.setStatus("current")
_CbsModuleRSWNewState_Type = DisplayString
_CbsModuleRSWNewState_Object = MibTableColumn
cbsModuleRSWNewState = _CbsModuleRSWNewState_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 10, 1, 19),
    _CbsModuleRSWNewState_Type()
)
cbsModuleRSWNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleRSWNewState.setStatus("current")
_CbsModuleNtpdMonTable_Object = MibTable
cbsModuleNtpdMonTable = _CbsModuleNtpdMonTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 11)
)
if mibBuilder.loadTexts:
    cbsModuleNtpdMonTable.setStatus("current")
_CbsModuleNtpdMonEntry_Object = MibTableRow
cbsModuleNtpdMonEntry = _CbsModuleNtpdMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 11, 1)
)
cbsModuleNtpdMonEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleNtpdMonEntry.setStatus("current")
_CbsModuleNtpdCPMHostName_Type = DisplayString
_CbsModuleNtpdCPMHostName_Object = MibTableColumn
cbsModuleNtpdCPMHostName = _CbsModuleNtpdCPMHostName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 11, 1, 1),
    _CbsModuleNtpdCPMHostName_Type()
)
cbsModuleNtpdCPMHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleNtpdCPMHostName.setStatus("current")
_CbsModuleNtpdCPMIPAddress_Type = DisplayString
_CbsModuleNtpdCPMIPAddress_Object = MibTableColumn
cbsModuleNtpdCPMIPAddress = _CbsModuleNtpdCPMIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 11, 1, 2),
    _CbsModuleNtpdCPMIPAddress_Type()
)
cbsModuleNtpdCPMIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleNtpdCPMIPAddress.setStatus("current")
_CbsModuleNtpdState_Type = DisplayString
_CbsModuleNtpdState_Object = MibTableColumn
cbsModuleNtpdState = _CbsModuleNtpdState_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 11, 1, 3),
    _CbsModuleNtpdState_Type()
)
cbsModuleNtpdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleNtpdState.setStatus("current")
_CbsModuleCpuCoreHiUtilTable_Object = MibTable
cbsModuleCpuCoreHiUtilTable = _CbsModuleCpuCoreHiUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 12)
)
if mibBuilder.loadTexts:
    cbsModuleCpuCoreHiUtilTable.setStatus("current")
_CbsModuleCpuCoreHiUtilEntry_Object = MibTableRow
cbsModuleCpuCoreHiUtilEntry = _CbsModuleCpuCoreHiUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 12, 1)
)
cbsModuleCpuCoreHiUtilEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleCpuCoreHiUtilEntry.setStatus("current")
_CbsModuleCpuCoreHiUtilSeverity_Type = UtilSeverityLvl
_CbsModuleCpuCoreHiUtilSeverity_Object = MibTableColumn
cbsModuleCpuCoreHiUtilSeverity = _CbsModuleCpuCoreHiUtilSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 12, 1, 1),
    _CbsModuleCpuCoreHiUtilSeverity_Type()
)
cbsModuleCpuCoreHiUtilSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCpuCoreHiUtilSeverity.setStatus("current")
_CbsModuleCpuCoreHiUtilPerc_Type = Integer32
_CbsModuleCpuCoreHiUtilPerc_Object = MibTableColumn
cbsModuleCpuCoreHiUtilPerc = _CbsModuleCpuCoreHiUtilPerc_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 12, 1, 2),
    _CbsModuleCpuCoreHiUtilPerc_Type()
)
cbsModuleCpuCoreHiUtilPerc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCpuCoreHiUtilPerc.setStatus("current")


class _CbsModuleCpuCoreHiUtilCores_Type(Bits):
    """Custom type cbsModuleCpuCoreHiUtilCores based on Bits"""
    namedValues = NamedValues(
        *(("core0", 7),
          ("core1", 6),
          ("core10", 13),
          ("core11", 12),
          ("core12", 11),
          ("core13", 10),
          ("core14", 9),
          ("core15", 8),
          ("core16", 23),
          ("core17", 22),
          ("core18", 21),
          ("core19", 20),
          ("core2", 5),
          ("core20", 19),
          ("core21", 18),
          ("core22", 17),
          ("core23", 16),
          ("core24", 31),
          ("core25", 30),
          ("core26", 29),
          ("core27", 28),
          ("core28", 27),
          ("core29", 26),
          ("core3", 4),
          ("core30", 25),
          ("core31", 24),
          ("core4", 3),
          ("core5", 2),
          ("core6", 1),
          ("core7", 0),
          ("core8", 15),
          ("core9", 14))
    )

_CbsModuleCpuCoreHiUtilCores_Type.__name__ = "Bits"
_CbsModuleCpuCoreHiUtilCores_Object = MibTableColumn
cbsModuleCpuCoreHiUtilCores = _CbsModuleCpuCoreHiUtilCores_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 12, 1, 3),
    _CbsModuleCpuCoreHiUtilCores_Type()
)
cbsModuleCpuCoreHiUtilCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCpuCoreHiUtilCores.setStatus("current")
_CbsModuleCpuCoreHiUtilDuration_Type = Integer32
_CbsModuleCpuCoreHiUtilDuration_Object = MibTableColumn
cbsModuleCpuCoreHiUtilDuration = _CbsModuleCpuCoreHiUtilDuration_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 12, 1, 4),
    _CbsModuleCpuCoreHiUtilDuration_Type()
)
cbsModuleCpuCoreHiUtilDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleCpuCoreHiUtilDuration.setStatus("current")
_CbsNpmFlowTableUtilTable_Object = MibTable
cbsNpmFlowTableUtilTable = _CbsNpmFlowTableUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13)
)
if mibBuilder.loadTexts:
    cbsNpmFlowTableUtilTable.setStatus("current")
_CbsNpmFlowTableUtilEntry_Object = MibTableRow
cbsNpmFlowTableUtilEntry = _CbsNpmFlowTableUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1)
)
cbsNpmFlowTableUtilEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsNpmFlowTableUtilEntry.setStatus("current")
_CbsNpmFTUtilSeverity_Type = UtilSeverityLvl
_CbsNpmFTUtilSeverity_Object = MibTableColumn
cbsNpmFTUtilSeverity = _CbsNpmFTUtilSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 1),
    _CbsNpmFTUtilSeverity_Type()
)
cbsNpmFTUtilSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTUtilSeverity.setStatus("current")


class _CbsNpmFTTriggerThreshold_Type(Integer32):
    """Custom type cbsNpmFTTriggerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTTriggerThreshold_Type.__name__ = "Integer32"
_CbsNpmFTTriggerThreshold_Object = MibTableColumn
cbsNpmFTTriggerThreshold = _CbsNpmFTTriggerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 2),
    _CbsNpmFTTriggerThreshold_Type()
)
cbsNpmFTTriggerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTTriggerThreshold.setStatus("current")


class _CbsNpmFTUsage_Type(Integer32):
    """Custom type cbsNpmFTUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTUsage_Type.__name__ = "Integer32"
_CbsNpmFTUsage_Object = MibTableColumn
cbsNpmFTUsage = _CbsNpmFTUsage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 3),
    _CbsNpmFTUsage_Type()
)
cbsNpmFTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTUsage.setStatus("current")


class _CbsNpmFTUdpLimitThreshold_Type(Integer32):
    """Custom type cbsNpmFTUdpLimitThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTUdpLimitThreshold_Type.__name__ = "Integer32"
_CbsNpmFTUdpLimitThreshold_Object = MibTableColumn
cbsNpmFTUdpLimitThreshold = _CbsNpmFTUdpLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 4),
    _CbsNpmFTUdpLimitThreshold_Type()
)
cbsNpmFTUdpLimitThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTUdpLimitThreshold.setStatus("current")


class _CbsNpmFTUdpMedianThreshold_Type(Integer32):
    """Custom type cbsNpmFTUdpMedianThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTUdpMedianThreshold_Type.__name__ = "Integer32"
_CbsNpmFTUdpMedianThreshold_Object = MibTableColumn
cbsNpmFTUdpMedianThreshold = _CbsNpmFTUdpMedianThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 5),
    _CbsNpmFTUdpMedianThreshold_Type()
)
cbsNpmFTUdpMedianThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTUdpMedianThreshold.setStatus("current")


class _CbsNpmFTUdpQuotaUsage_Type(Integer32):
    """Custom type cbsNpmFTUdpQuotaUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTUdpQuotaUsage_Type.__name__ = "Integer32"
_CbsNpmFTUdpQuotaUsage_Object = MibTableColumn
cbsNpmFTUdpQuotaUsage = _CbsNpmFTUdpQuotaUsage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 6),
    _CbsNpmFTUdpQuotaUsage_Type()
)
cbsNpmFTUdpQuotaUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTUdpQuotaUsage.setStatus("current")


class _CbsNpmFTTcpLimitThreshold_Type(Integer32):
    """Custom type cbsNpmFTTcpLimitThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTTcpLimitThreshold_Type.__name__ = "Integer32"
_CbsNpmFTTcpLimitThreshold_Object = MibTableColumn
cbsNpmFTTcpLimitThreshold = _CbsNpmFTTcpLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 7),
    _CbsNpmFTTcpLimitThreshold_Type()
)
cbsNpmFTTcpLimitThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTTcpLimitThreshold.setStatus("current")


class _CbsNpmFTTcpMedianThreshold_Type(Integer32):
    """Custom type cbsNpmFTTcpMedianThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTTcpMedianThreshold_Type.__name__ = "Integer32"
_CbsNpmFTTcpMedianThreshold_Object = MibTableColumn
cbsNpmFTTcpMedianThreshold = _CbsNpmFTTcpMedianThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 8),
    _CbsNpmFTTcpMedianThreshold_Type()
)
cbsNpmFTTcpMedianThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTTcpMedianThreshold.setStatus("current")


class _CbsNpmFTTcpQuotaUsage_Type(Integer32):
    """Custom type cbsNpmFTTcpQuotaUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTTcpQuotaUsage_Type.__name__ = "Integer32"
_CbsNpmFTTcpQuotaUsage_Object = MibTableColumn
cbsNpmFTTcpQuotaUsage = _CbsNpmFTTcpQuotaUsage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 9),
    _CbsNpmFTTcpQuotaUsage_Type()
)
cbsNpmFTTcpQuotaUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTTcpQuotaUsage.setStatus("current")


class _CbsNpmFTIcmpLimitThreshold_Type(Integer32):
    """Custom type cbsNpmFTIcmpLimitThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTIcmpLimitThreshold_Type.__name__ = "Integer32"
_CbsNpmFTIcmpLimitThreshold_Object = MibTableColumn
cbsNpmFTIcmpLimitThreshold = _CbsNpmFTIcmpLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 10),
    _CbsNpmFTIcmpLimitThreshold_Type()
)
cbsNpmFTIcmpLimitThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTIcmpLimitThreshold.setStatus("current")


class _CbsNpmFTIcmpMedianThreshold_Type(Integer32):
    """Custom type cbsNpmFTIcmpMedianThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTIcmpMedianThreshold_Type.__name__ = "Integer32"
_CbsNpmFTIcmpMedianThreshold_Object = MibTableColumn
cbsNpmFTIcmpMedianThreshold = _CbsNpmFTIcmpMedianThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 11),
    _CbsNpmFTIcmpMedianThreshold_Type()
)
cbsNpmFTIcmpMedianThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTIcmpMedianThreshold.setStatus("current")


class _CbsNpmFTIcmpQuotaUsage_Type(Integer32):
    """Custom type cbsNpmFTIcmpQuotaUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTIcmpQuotaUsage_Type.__name__ = "Integer32"
_CbsNpmFTIcmpQuotaUsage_Object = MibTableColumn
cbsNpmFTIcmpQuotaUsage = _CbsNpmFTIcmpQuotaUsage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 12),
    _CbsNpmFTIcmpQuotaUsage_Type()
)
cbsNpmFTIcmpQuotaUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTIcmpQuotaUsage.setStatus("current")


class _CbsNpmFTOtherIpLimitThreshold_Type(Integer32):
    """Custom type cbsNpmFTOtherIpLimitThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTOtherIpLimitThreshold_Type.__name__ = "Integer32"
_CbsNpmFTOtherIpLimitThreshold_Object = MibTableColumn
cbsNpmFTOtherIpLimitThreshold = _CbsNpmFTOtherIpLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 13),
    _CbsNpmFTOtherIpLimitThreshold_Type()
)
cbsNpmFTOtherIpLimitThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTOtherIpLimitThreshold.setStatus("current")


class _CbsNpmFTOtherIpMedianThreshold_Type(Integer32):
    """Custom type cbsNpmFTOtherIpMedianThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTOtherIpMedianThreshold_Type.__name__ = "Integer32"
_CbsNpmFTOtherIpMedianThreshold_Object = MibTableColumn
cbsNpmFTOtherIpMedianThreshold = _CbsNpmFTOtherIpMedianThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 14),
    _CbsNpmFTOtherIpMedianThreshold_Type()
)
cbsNpmFTOtherIpMedianThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTOtherIpMedianThreshold.setStatus("current")


class _CbsNpmFTOtherIpQuotaUsage_Type(Integer32):
    """Custom type cbsNpmFTOtherIpQuotaUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsNpmFTOtherIpQuotaUsage_Type.__name__ = "Integer32"
_CbsNpmFTOtherIpQuotaUsage_Object = MibTableColumn
cbsNpmFTOtherIpQuotaUsage = _CbsNpmFTOtherIpQuotaUsage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 13, 1, 15),
    _CbsNpmFTOtherIpQuotaUsage_Type()
)
cbsNpmFTOtherIpQuotaUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmFTOtherIpQuotaUsage.setStatus("current")
_CbsModuleSdramMemCfgStatTable_Object = MibTable
cbsModuleSdramMemCfgStatTable = _CbsModuleSdramMemCfgStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 14)
)
if mibBuilder.loadTexts:
    cbsModuleSdramMemCfgStatTable.setStatus("current")
_CbsModuleSdramMemCfgStatEntry_Object = MibTableRow
cbsModuleSdramMemCfgStatEntry = _CbsModuleSdramMemCfgStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 14, 1)
)
cbsModuleSdramMemCfgStatEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleSdramMemCfgStatEntry.setStatus("current")
_CbsModuleSdramMemCfgStat_Type = BadSdramMemCfgStat
_CbsModuleSdramMemCfgStat_Object = MibTableColumn
cbsModuleSdramMemCfgStat = _CbsModuleSdramMemCfgStat_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 14, 1, 1),
    _CbsModuleSdramMemCfgStat_Type()
)
cbsModuleSdramMemCfgStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleSdramMemCfgStat.setStatus("current")
_CbsModuleGuestHealthTable_Object = MibTable
cbsModuleGuestHealthTable = _CbsModuleGuestHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 15)
)
if mibBuilder.loadTexts:
    cbsModuleGuestHealthTable.setStatus("current")
_CbsModuleGuestHealthTableEntry_Object = MibTableRow
cbsModuleGuestHealthTableEntry = _CbsModuleGuestHealthTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 15, 1)
)
cbsModuleGuestHealthTableEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsModuleGuestHealthTableEntry.setStatus("current")
_CbsApmGuestHealthSeverity_Type = GuestHealthSeverityLvl
_CbsApmGuestHealthSeverity_Object = MibTableColumn
cbsApmGuestHealthSeverity = _CbsApmGuestHealthSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 15, 1, 1),
    _CbsApmGuestHealthSeverity_Type()
)
cbsApmGuestHealthSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsApmGuestHealthSeverity.setStatus("current")
_CbsCpmDiskCfgStat_Type = BadDiskCfgStat
_CbsCpmDiskCfgStat_Object = MibScalar
cbsCpmDiskCfgStat = _CbsCpmDiskCfgStat_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 16),
    _CbsCpmDiskCfgStat_Type()
)
cbsCpmDiskCfgStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsCpmDiskCfgStat.setStatus("current")
_CbsModuleApplicationTable_Object = MibTable
cbsModuleApplicationTable = _CbsModuleApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 17)
)
if mibBuilder.loadTexts:
    cbsModuleApplicationTable.setStatus("current")
_CbsModuleApplicationEntry_Object = MibTableRow
cbsModuleApplicationEntry = _CbsModuleApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 17, 1)
)
cbsModuleApplicationEntry.setIndexNames(
    (0, "CBS-VAPGROUP-MIB", "cbsVgVapGroupID"),
)
if mibBuilder.loadTexts:
    cbsModuleApplicationEntry.setStatus("current")
_CbsModuleApplicationName_Type = DisplayString
_CbsModuleApplicationName_Object = MibTableColumn
cbsModuleApplicationName = _CbsModuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 17, 1, 1),
    _CbsModuleApplicationName_Type()
)
cbsModuleApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleApplicationName.setStatus("current")
_CbsModuleApplicationVersion_Type = DisplayString
_CbsModuleApplicationVersion_Object = MibTableColumn
cbsModuleApplicationVersion = _CbsModuleApplicationVersion_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 17, 1, 2),
    _CbsModuleApplicationVersion_Type()
)
cbsModuleApplicationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleApplicationVersion.setStatus("current")
_CbsModuleApplicationRelease_Type = DisplayString
_CbsModuleApplicationRelease_Object = MibTableColumn
cbsModuleApplicationRelease = _CbsModuleApplicationRelease_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 17, 1, 3),
    _CbsModuleApplicationRelease_Type()
)
cbsModuleApplicationRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleApplicationRelease.setStatus("current")
_CbsModuleApplicationMonEnabled_Type = TruthValue
_CbsModuleApplicationMonEnabled_Object = MibTableColumn
cbsModuleApplicationMonEnabled = _CbsModuleApplicationMonEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 17, 1, 4),
    _CbsModuleApplicationMonEnabled_Type()
)
cbsModuleApplicationMonEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleApplicationMonEnabled.setStatus("current")
_CbsModuleApplicationVgName_Type = DisplayString
_CbsModuleApplicationVgName_Object = MibTableColumn
cbsModuleApplicationVgName = _CbsModuleApplicationVgName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 17, 1, 5),
    _CbsModuleApplicationVgName_Type()
)
cbsModuleApplicationVgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsModuleApplicationVgName.setStatus("current")
_CbsFlowTablePartitionThreshold_Type = Integer32
_CbsFlowTablePartitionThreshold_Object = MibScalar
cbsFlowTablePartitionThreshold = _CbsFlowTablePartitionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 18),
    _CbsFlowTablePartitionThreshold_Type()
)
cbsFlowTablePartitionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsFlowTablePartitionThreshold.setStatus("current")
_CbsFlowTableCriticalAlarm_Type = Integer32
_CbsFlowTableCriticalAlarm_Object = MibScalar
cbsFlowTableCriticalAlarm = _CbsFlowTableCriticalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 19),
    _CbsFlowTableCriticalAlarm_Type()
)
cbsFlowTableCriticalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsFlowTableCriticalAlarm.setStatus("current")
_CbsFlowTableUtilization_Type = Integer32
_CbsFlowTableUtilization_Object = MibScalar
cbsFlowTableUtilization = _CbsFlowTableUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 20),
    _CbsFlowTableUtilization_Type()
)
cbsFlowTableUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsFlowTableUtilization.setStatus("current")
_CbsFlowTableUtilTcpFlowEntries_Type = Integer32
_CbsFlowTableUtilTcpFlowEntries_Object = MibScalar
cbsFlowTableUtilTcpFlowEntries = _CbsFlowTableUtilTcpFlowEntries_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 21),
    _CbsFlowTableUtilTcpFlowEntries_Type()
)
cbsFlowTableUtilTcpFlowEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsFlowTableUtilTcpFlowEntries.setStatus("current")
_CbsFlowTableUtilUdpFlowEntries_Type = Integer32
_CbsFlowTableUtilUdpFlowEntries_Object = MibScalar
cbsFlowTableUtilUdpFlowEntries = _CbsFlowTableUtilUdpFlowEntries_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 22),
    _CbsFlowTableUtilUdpFlowEntries_Type()
)
cbsFlowTableUtilUdpFlowEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsFlowTableUtilUdpFlowEntries.setStatus("current")
_CbsFlowTableUtilIcmpFlowEntries_Type = Integer32
_CbsFlowTableUtilIcmpFlowEntries_Object = MibScalar
cbsFlowTableUtilIcmpFlowEntries = _CbsFlowTableUtilIcmpFlowEntries_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 23),
    _CbsFlowTableUtilIcmpFlowEntries_Type()
)
cbsFlowTableUtilIcmpFlowEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsFlowTableUtilIcmpFlowEntries.setStatus("current")
_CbsFlowTableUtilOtherIpFlowEntries_Type = Integer32
_CbsFlowTableUtilOtherIpFlowEntries_Object = MibScalar
cbsFlowTableUtilOtherIpFlowEntries = _CbsFlowTableUtilOtherIpFlowEntries_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 24),
    _CbsFlowTableUtilOtherIpFlowEntries_Type()
)
cbsFlowTableUtilOtherIpFlowEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsFlowTableUtilOtherIpFlowEntries.setStatus("current")
_CbsNpmFlowDistTable_Object = MibTable
cbsNpmFlowDistTable = _CbsNpmFlowDistTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 25)
)
if mibBuilder.loadTexts:
    cbsNpmFlowDistTable.setStatus("current")
_CbsNpmFlowDistEntry_Object = MibTableRow
cbsNpmFlowDistEntry = _CbsNpmFlowDistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 25, 1)
)
cbsNpmFlowDistEntry.setIndexNames(
    (0, "CBS-MODULE-RESOURCES-MIB", "cbsNpmSlotId"),
)
if mibBuilder.loadTexts:
    cbsNpmFlowDistEntry.setStatus("current")


class _CbsNpmSlotId_Type(Integer32):
    """Custom type cbsNpmSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_CbsNpmSlotId_Type.__name__ = "Integer32"
_CbsNpmSlotId_Object = MibTableColumn
cbsNpmSlotId = _CbsNpmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 25, 1, 1),
    _CbsNpmSlotId_Type()
)
cbsNpmSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmSlotId.setStatus("current")
_CbsNpmTcpCurrentFlows_Type = Integer32
_CbsNpmTcpCurrentFlows_Object = MibTableColumn
cbsNpmTcpCurrentFlows = _CbsNpmTcpCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 25, 1, 2),
    _CbsNpmTcpCurrentFlows_Type()
)
cbsNpmTcpCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmTcpCurrentFlows.setStatus("current")
_CbsNpmUdpCurrentFlows_Type = Integer32
_CbsNpmUdpCurrentFlows_Object = MibTableColumn
cbsNpmUdpCurrentFlows = _CbsNpmUdpCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 25, 1, 3),
    _CbsNpmUdpCurrentFlows_Type()
)
cbsNpmUdpCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmUdpCurrentFlows.setStatus("current")
_CbsNpmIcmpCurrentFlows_Type = Integer32
_CbsNpmIcmpCurrentFlows_Object = MibTableColumn
cbsNpmIcmpCurrentFlows = _CbsNpmIcmpCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 25, 1, 4),
    _CbsNpmIcmpCurrentFlows_Type()
)
cbsNpmIcmpCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmIcmpCurrentFlows.setStatus("current")
_CbsNpmOtherIpCurrentFlows_Type = Integer32
_CbsNpmOtherIpCurrentFlows_Object = MibTableColumn
cbsNpmOtherIpCurrentFlows = _CbsNpmOtherIpCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 25, 1, 5),
    _CbsNpmOtherIpCurrentFlows_Type()
)
cbsNpmOtherIpCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmOtherIpCurrentFlows.setStatus("current")
_CbsNpmNewFlowRate_Type = Integer32
_CbsNpmNewFlowRate_Object = MibTableColumn
cbsNpmNewFlowRate = _CbsNpmNewFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 25, 1, 6),
    _CbsNpmNewFlowRate_Type()
)
cbsNpmNewFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmNewFlowRate.setStatus("current")
_CbsNpmAgedFlowRate_Type = Integer32
_CbsNpmAgedFlowRate_Object = MibTableColumn
cbsNpmAgedFlowRate = _CbsNpmAgedFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 25, 1, 7),
    _CbsNpmAgedFlowRate_Type()
)
cbsNpmAgedFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsNpmAgedFlowRate.setStatus("current")
_CbsVapFlowDistTable_Object = MibTable
cbsVapFlowDistTable = _CbsVapFlowDistTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 26)
)
if mibBuilder.loadTexts:
    cbsVapFlowDistTable.setStatus("current")
_CbsVapFlowDistEntry_Object = MibTableRow
cbsVapFlowDistEntry = _CbsVapFlowDistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 26, 1)
)
cbsVapFlowDistEntry.setIndexNames(
    (0, "CBS-MODULE-RESOURCES-MIB", "cbsVapFlowGroupID"),
    (0, "CBS-MODULE-RESOURCES-MIB", "cbsVapFlowIndex"),
)
if mibBuilder.loadTexts:
    cbsVapFlowDistEntry.setStatus("current")


class _CbsVapFlowGroupID_Type(Integer32):
    """Custom type cbsVapFlowGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CbsVapFlowGroupID_Type.__name__ = "Integer32"
_CbsVapFlowGroupID_Object = MibTableColumn
cbsVapFlowGroupID = _CbsVapFlowGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 26, 1, 1),
    _CbsVapFlowGroupID_Type()
)
cbsVapFlowGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVapFlowGroupID.setStatus("current")


class _CbsVapFlowIndex_Type(Integer32):
    """Custom type cbsVapFlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CbsVapFlowIndex_Type.__name__ = "Integer32"
_CbsVapFlowIndex_Object = MibTableColumn
cbsVapFlowIndex = _CbsVapFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 26, 1, 2),
    _CbsVapFlowIndex_Type()
)
cbsVapFlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVapFlowIndex.setStatus("current")
_CbsVapName_Type = DisplayString
_CbsVapName_Object = MibTableColumn
cbsVapName = _CbsVapName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 26, 1, 3),
    _CbsVapName_Type()
)
cbsVapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVapName.setStatus("current")
_CbsVapCurrentFlows_Type = Integer32
_CbsVapCurrentFlows_Object = MibTableColumn
cbsVapCurrentFlows = _CbsVapCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 26, 1, 4),
    _CbsVapCurrentFlows_Type()
)
cbsVapCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVapCurrentFlows.setStatus("current")
_CbsVapNewFlowRate_Type = Integer32
_CbsVapNewFlowRate_Object = MibTableColumn
cbsVapNewFlowRate = _CbsVapNewFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 26, 1, 5),
    _CbsVapNewFlowRate_Type()
)
cbsVapNewFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVapNewFlowRate.setStatus("current")
_CbsVapAgedFlowRate_Type = Integer32
_CbsVapAgedFlowRate_Object = MibTableColumn
cbsVapAgedFlowRate = _CbsVapAgedFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 3, 26, 1, 6),
    _CbsVapAgedFlowRate_Type()
)
cbsVapAgedFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVapAgedFlowRate.setStatus("current")
_CbsModuleResourceTraps_ObjectIdentity = ObjectIdentity
cbsModuleResourceTraps = _CbsModuleResourceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2)
)

# Managed Objects groups


# Notification objects

cbsModuleCPULoadExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 1)
)
cbsModuleCPULoadExceeded.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleCPULoad1")
)
if mibBuilder.loadTexts:
    cbsModuleCPULoadExceeded.setStatus(
        "obsolete"
    )

cbsModuleCPULoadNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 2)
)
cbsModuleCPULoadNormal.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleCPULoad1")
)
if mibBuilder.loadTexts:
    cbsModuleCPULoadNormal.setStatus(
        "obsolete"
    )

cbsModuleMemoryUsageExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 3)
)
cbsModuleMemoryUsageExceeded.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsModuleMemoryTotal"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleMemoryUsed"))
)
if mibBuilder.loadTexts:
    cbsModuleMemoryUsageExceeded.setStatus(
        "obsolete"
    )

cbsModuleMemoryUsageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 4)
)
cbsModuleMemoryUsageNormal.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsModuleMemoryTotal"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleMemoryUsed"))
)
if mibBuilder.loadTexts:
    cbsModuleMemoryUsageNormal.setStatus(
        "obsolete"
    )

cbsModuleCPUUtilExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 5)
)
cbsModuleCPUUtilExceeded.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleCPUUtil1")
)
if mibBuilder.loadTexts:
    cbsModuleCPUUtilExceeded.setStatus(
        "current"
    )

cbsModuleCPUUtilNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 6)
)
cbsModuleCPUUtilNormal.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleCPUUtil1")
)
if mibBuilder.loadTexts:
    cbsModuleCPUUtilNormal.setStatus(
        "current"
    )

cbsModuleDURootHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 7)
)
cbsModuleDURootHigh.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDURoot")
)
if mibBuilder.loadTexts:
    cbsModuleDURootHigh.setStatus(
        "current"
    )

cbsModuleDURootNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 8)
)
cbsModuleDURootNormal.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDURoot")
)
if mibBuilder.loadTexts:
    cbsModuleDURootNormal.setStatus(
        "current"
    )

cbsModuleDUBootHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 9)
)
cbsModuleDUBootHigh.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDUBoot")
)
if mibBuilder.loadTexts:
    cbsModuleDUBootHigh.setStatus(
        "current"
    )

cbsModuleDUBootNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 10)
)
cbsModuleDUBootNormal.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDUBoot")
)
if mibBuilder.loadTexts:
    cbsModuleDUBootNormal.setStatus(
        "current"
    )

cbsModuleDUCbconfigHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 11)
)
cbsModuleDUCbconfigHigh.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDUCbconfig")
)
if mibBuilder.loadTexts:
    cbsModuleDUCbconfigHigh.setStatus(
        "current"
    )

cbsModuleDUCbconfigNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 12)
)
cbsModuleDUCbconfigNormal.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDUCbconfig")
)
if mibBuilder.loadTexts:
    cbsModuleDUCbconfigNormal.setStatus(
        "current"
    )

cbsModuleDUTftpbootHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 13)
)
cbsModuleDUTftpbootHigh.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDUTftpboot")
)
if mibBuilder.loadTexts:
    cbsModuleDUTftpbootHigh.setStatus(
        "current"
    )

cbsModuleDUTftpbootNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 14)
)
cbsModuleDUTftpbootNormal.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDUTftpboot")
)
if mibBuilder.loadTexts:
    cbsModuleDUTftpbootNormal.setStatus(
        "current"
    )

cbsModuleFreePageAvailableHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 15)
)
cbsModuleFreePageAvailableHigh.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsModuleFreePageAvailable"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleFreePageThreshold"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleFreePageSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleFreePageVapName"))
)
if mibBuilder.loadTexts:
    cbsModuleFreePageAvailableHigh.setStatus(
        "current"
    )

cbsModuleFreePageAvailableNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 16)
)
cbsModuleFreePageAvailableNorm.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsModuleFreePageAvailable"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleFreePageThreshold"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleFreePageSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleFreePageVapName"))
)
if mibBuilder.loadTexts:
    cbsModuleFreePageAvailableNorm.setStatus(
        "current"
    )

cbsModuleMUHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 17)
)
cbsModuleMUHigh.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleID")
)
if mibBuilder.loadTexts:
    cbsModuleMUHigh.setStatus(
        "current"
    )

cbsModuleMUNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 18)
)
cbsModuleMUNormal.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleID")
)
if mibBuilder.loadTexts:
    cbsModuleMUNormal.setStatus(
        "current"
    )

cbsModuleFRHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 19)
)
cbsModuleFRHigh.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleID")
)
if mibBuilder.loadTexts:
    cbsModuleFRHigh.setStatus(
        "current"
    )

cbsModuleFRNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 20)
)
cbsModuleFRNormal.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleID")
)
if mibBuilder.loadTexts:
    cbsModuleFRNormal.setStatus(
        "current"
    )

cbsModuleBUHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 21)
)
cbsModuleBUHigh.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleID")
)
if mibBuilder.loadTexts:
    cbsModuleBUHigh.setStatus(
        "current"
    )

cbsModuleBUNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 22)
)
cbsModuleBUNormal.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleID")
)
if mibBuilder.loadTexts:
    cbsModuleBUNormal.setStatus(
        "current"
    )

cbsModuleAppStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 23)
)
cbsModuleAppStateChange.setObjects(
      *(("CBS-HARDWARE-MIB", "cbsHwModuleID"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleAppName"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleAppVersion"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleAppRelease"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleAppCPMHostName"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleAppCPMIPAddress"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleAppVAPGroupName"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleAppVAPIndex"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleAppOldState"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleAppNewState"))
)
if mibBuilder.loadTexts:
    cbsModuleAppStateChange.setStatus(
        "current"
    )

cbsModuleNtpdMonStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 24)
)
cbsModuleNtpdMonStateChange.setObjects(
      *(("CBS-HARDWARE-MIB", "cbsHwModuleID"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleNtpdCPMHostName"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleNtpdCPMIPAddress"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleNtpdState"))
)
if mibBuilder.loadTexts:
    cbsModuleNtpdMonStateChange.setStatus(
        "current"
    )

cbsModuleDUMgmtHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 25)
)
cbsModuleDUMgmtHigh.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDUMgmt")
)
if mibBuilder.loadTexts:
    cbsModuleDUMgmtHigh.setStatus(
        "current"
    )

cbsModuleDUMgmtNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 26)
)
cbsModuleDUMgmtNormal.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDUMgmt")
)
if mibBuilder.loadTexts:
    cbsModuleDUMgmtNormal.setStatus(
        "current"
    )

cbsModuleCpuCoreUtilExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 27)
)
cbsModuleCpuCoreUtilExceeded.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsModuleCpuCoreHiUtilSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleCpuCoreHiUtilPerc"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleCpuCoreHiUtilDuration"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleCpuCoreHiUtilCores"))
)
if mibBuilder.loadTexts:
    cbsModuleCpuCoreUtilExceeded.setStatus(
        "current"
    )

cbsModuleCpuCoreUtilNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 28)
)
cbsModuleCpuCoreUtilNormal.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleCpuCoreHiUtilPerc")
)
if mibBuilder.loadTexts:
    cbsModuleCpuCoreUtilNormal.setStatus(
        "current"
    )

cbsNpmFlowTableUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 29)
)
cbsNpmFlowTableUsageHigh.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUtilSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTTriggerThreshold"))
)
if mibBuilder.loadTexts:
    cbsNpmFlowTableUsageHigh.setStatus(
        "current"
    )

cbsNpmFlowTableUsageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 30)
)
if mibBuilder.loadTexts:
    cbsNpmFlowTableUsageNormal.setStatus(
        "current"
    )

cbsNpmFTUdpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 31)
)
cbsNpmFTUdpLimitExceeded.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUtilSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUdpLimitThreshold"))
)
if mibBuilder.loadTexts:
    cbsNpmFTUdpLimitExceeded.setStatus(
        "current"
    )

cbsNpmFTUdpLimitNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 32)
)
if mibBuilder.loadTexts:
    cbsNpmFTUdpLimitNormal.setStatus(
        "current"
    )

cbsNpmFTUdpMedianExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 33)
)
cbsNpmFTUdpMedianExceeded.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUtilSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUdpLimitThreshold"))
)
if mibBuilder.loadTexts:
    cbsNpmFTUdpMedianExceeded.setStatus(
        "current"
    )

cbsNpmFTUdpMedianNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 34)
)
if mibBuilder.loadTexts:
    cbsNpmFTUdpMedianNormal.setStatus(
        "current"
    )

cbsNpmFTTcpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 35)
)
cbsNpmFTTcpLimitExceeded.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUtilSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTTcpLimitThreshold"))
)
if mibBuilder.loadTexts:
    cbsNpmFTTcpLimitExceeded.setStatus(
        "current"
    )

cbsNpmFTTcpLimitNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 36)
)
if mibBuilder.loadTexts:
    cbsNpmFTTcpLimitNormal.setStatus(
        "current"
    )

cbsNpmFTTcpMedianExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 37)
)
cbsNpmFTTcpMedianExceeded.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUtilSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTTcpLimitThreshold"))
)
if mibBuilder.loadTexts:
    cbsNpmFTTcpMedianExceeded.setStatus(
        "current"
    )

cbsNpmFTTcpMedianNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 38)
)
if mibBuilder.loadTexts:
    cbsNpmFTTcpMedianNormal.setStatus(
        "current"
    )

cbsNpmFTIcmpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 39)
)
cbsNpmFTIcmpLimitExceeded.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUtilSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTIcmpLimitThreshold"))
)
if mibBuilder.loadTexts:
    cbsNpmFTIcmpLimitExceeded.setStatus(
        "current"
    )

cbsNpmFTIcmpLimitNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 40)
)
if mibBuilder.loadTexts:
    cbsNpmFTIcmpLimitNormal.setStatus(
        "current"
    )

cbsNpmFTIcmpMedianExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 41)
)
cbsNpmFTIcmpMedianExceeded.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUtilSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTIcmpLimitThreshold"))
)
if mibBuilder.loadTexts:
    cbsNpmFTIcmpMedianExceeded.setStatus(
        "current"
    )

cbsNpmFTIcmpMedianNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 42)
)
if mibBuilder.loadTexts:
    cbsNpmFTIcmpMedianNormal.setStatus(
        "current"
    )

cbsNpmFTOtherIpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 43)
)
cbsNpmFTOtherIpLimitExceeded.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUtilSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTOtherIpLimitThreshold"))
)
if mibBuilder.loadTexts:
    cbsNpmFTOtherIpLimitExceeded.setStatus(
        "current"
    )

cbsNpmFTOtherIpLimitNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 44)
)
if mibBuilder.loadTexts:
    cbsNpmFTOtherIpLimitNormal.setStatus(
        "current"
    )

cbsNpmFTOtherIpMedianExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 45)
)
cbsNpmFTOtherIpMedianExceeded.setObjects(
      *(("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTUtilSeverity"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsNpmFTOtherIpLimitThreshold"))
)
if mibBuilder.loadTexts:
    cbsNpmFTOtherIpMedianExceeded.setStatus(
        "current"
    )

cbsNpmFTOtherIpMedianNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 46)
)
if mibBuilder.loadTexts:
    cbsNpmFTOtherIpMedianNormal.setStatus(
        "current"
    )

cbsModuleSdramCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 47)
)
cbsModuleSdramCheck.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleSdramMemCfgStat")
)
if mibBuilder.loadTexts:
    cbsModuleSdramCheck.setStatus(
        "current"
    )

cbsApmGuestHealthCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 48)
)
cbsApmGuestHealthCheck.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsApmGuestHealthSeverity")
)
if mibBuilder.loadTexts:
    cbsApmGuestHealthCheck.setStatus(
        "current"
    )

cbsCpmDiskCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 49)
)
cbsCpmDiskCheck.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsCpmDiskCfgStat")
)
if mibBuilder.loadTexts:
    cbsCpmDiskCheck.setStatus(
        "current"
    )

cbsModuleDUVarHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 50)
)
cbsModuleDUVarHigh.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDUVar")
)
if mibBuilder.loadTexts:
    cbsModuleDUVarHigh.setStatus(
        "current"
    )

cbsModuleDUVarNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 51)
)
cbsModuleDUVarNormal.setObjects(
    ("CBS-MODULE-RESOURCES-MIB", "cbsModuleDUVar")
)
if mibBuilder.loadTexts:
    cbsModuleDUVarNormal.setStatus(
        "current"
    )

cbsModuleRSWStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 2, 52)
)
cbsModuleRSWStateChange.setObjects(
      *(("CBS-HARDWARE-MIB", "cbsHwModuleID"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleRSWName"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleRSWVersion"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleRSWRelease"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleRSWStartOnBoot"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleRSWCPMHostName"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleRSWCPMIPAddress"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleRSWVAPGroupName"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleRSWVAPIndex"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleRSWOldState"),
        ("CBS-MODULE-RESOURCES-MIB", "cbsModuleRSWNewState"))
)
if mibBuilder.loadTexts:
    cbsModuleRSWStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CBS-MODULE-RESOURCES-MIB",
    **{"UtilSeverityLvl": UtilSeverityLvl,
       "BadSdramMemCfgStat": BadSdramMemCfgStat,
       "BadDiskCfgStat": BadDiskCfgStat,
       "GuestHealthSeverityLvl": GuestHealthSeverityLvl,
       "cbsModuleResources": cbsModuleResources,
       "cbsModuleCPULoadTable": cbsModuleCPULoadTable,
       "cbsModuleCPULoadEntry": cbsModuleCPULoadEntry,
       "cbsModuleCPUSpeed": cbsModuleCPUSpeed,
       "cbsModuleCPUCount": cbsModuleCPUCount,
       "cbsModuleCPULoad1": cbsModuleCPULoad1,
       "cbsModuleCPULoad5": cbsModuleCPULoad5,
       "cbsModuleCPULoad15": cbsModuleCPULoad15,
       "cbsModuleCPUUtil1": cbsModuleCPUUtil1,
       "cbsModuleCPUUtil5": cbsModuleCPUUtil5,
       "cbsModuleCPUUtil15": cbsModuleCPUUtil15,
       "cbsModuleMemoryTable": cbsModuleMemoryTable,
       "cbsModuleMemoryEntry": cbsModuleMemoryEntry,
       "cbsModuleMemoryTotal": cbsModuleMemoryTotal,
       "cbsModuleMemoryUsed": cbsModuleMemoryUsed,
       "cbsModuleMemoryFree": cbsModuleMemoryFree,
       "cbsModuleMemoryTotalSwap": cbsModuleMemoryTotalSwap,
       "cbsModuleMemoryAvailSwap": cbsModuleMemoryAvailSwap,
       "cbsModuleMemoryTotalReal": cbsModuleMemoryTotalReal,
       "cbsModuleMemoryAvailReal": cbsModuleMemoryAvailReal,
       "cbsModuleMemoryTotalFree": cbsModuleMemoryTotalFree,
       "cbsModuleMemoryShared": cbsModuleMemoryShared,
       "cbsModuleMemoryBuffer": cbsModuleMemoryBuffer,
       "cbsModuleMemoryCached": cbsModuleMemoryCached,
       "cbsModuleMemoryHiTotal": cbsModuleMemoryHiTotal,
       "cbsModuleMemoryHiFree": cbsModuleMemoryHiFree,
       "cbsModuleMemoryLoTotal": cbsModuleMemoryLoTotal,
       "cbsModuleMemoryLoFree": cbsModuleMemoryLoFree,
       "cbsModuleSwapTable": cbsModuleSwapTable,
       "cbsModuleSwapEntry": cbsModuleSwapEntry,
       "cbsModuleSwapTotal": cbsModuleSwapTotal,
       "cbsModuleSwapUsed": cbsModuleSwapUsed,
       "cbsModuleSwapFree": cbsModuleSwapFree,
       "cbsModuleDUTable": cbsModuleDUTable,
       "cbsModuleDUEntry": cbsModuleDUEntry,
       "cbsModuleDURoot": cbsModuleDURoot,
       "cbsModuleDUBoot": cbsModuleDUBoot,
       "cbsModuleDUCbconfig": cbsModuleDUCbconfig,
       "cbsModuleDUTftpboot": cbsModuleDUTftpboot,
       "cbsModuleDUMgmt": cbsModuleDUMgmt,
       "cbsModuleDUVar": cbsModuleDUVar,
       "cbsModuleFreePageTable": cbsModuleFreePageTable,
       "cbsModuleFreePageEntry": cbsModuleFreePageEntry,
       "cbsModuleFreePageAvailable": cbsModuleFreePageAvailable,
       "cbsModuleFreePageThreshold": cbsModuleFreePageThreshold,
       "cbsModuleFreePageSeverity": cbsModuleFreePageSeverity,
       "cbsModuleFreePageVapName": cbsModuleFreePageVapName,
       "cbsModuleCPUAvgUtilTable": cbsModuleCPUAvgUtilTable,
       "cbsModuleCPUAvgUtilEntry": cbsModuleCPUAvgUtilEntry,
       "cbsModuleCPUAvgUtilCore1User": cbsModuleCPUAvgUtilCore1User,
       "cbsModuleCPUAvgUtilCore1Nice": cbsModuleCPUAvgUtilCore1Nice,
       "cbsModuleCPUAvgUtilCore1Syst": cbsModuleCPUAvgUtilCore1Syst,
       "cbsModuleCPUAvgUtilCore1Idle": cbsModuleCPUAvgUtilCore1Idle,
       "cbsModuleCPUAvgUtilCore1IRQ": cbsModuleCPUAvgUtilCore1IRQ,
       "cbsModuleCPUAvgUtilCore1SoftIRQ": cbsModuleCPUAvgUtilCore1SoftIRQ,
       "cbsModuleCPUAvgUtilCore1IOWait": cbsModuleCPUAvgUtilCore1IOWait,
       "cbsModuleCPUAvgUtilCore2User": cbsModuleCPUAvgUtilCore2User,
       "cbsModuleCPUAvgUtilCore2Nice": cbsModuleCPUAvgUtilCore2Nice,
       "cbsModuleCPUAvgUtilCore2Syst": cbsModuleCPUAvgUtilCore2Syst,
       "cbsModuleCPUAvgUtilCore2Idle": cbsModuleCPUAvgUtilCore2Idle,
       "cbsModuleCPUAvgUtilCore2IRQ": cbsModuleCPUAvgUtilCore2IRQ,
       "cbsModuleCPUAvgUtilCore2SoftIRQ": cbsModuleCPUAvgUtilCore2SoftIRQ,
       "cbsModuleCPUAvgUtilCore2IOWait": cbsModuleCPUAvgUtilCore2IOWait,
       "cbsModuleCPUAvgUtilCore3User": cbsModuleCPUAvgUtilCore3User,
       "cbsModuleCPUAvgUtilCore3Nice": cbsModuleCPUAvgUtilCore3Nice,
       "cbsModuleCPUAvgUtilCore3Syst": cbsModuleCPUAvgUtilCore3Syst,
       "cbsModuleCPUAvgUtilCore3Idle": cbsModuleCPUAvgUtilCore3Idle,
       "cbsModuleCPUAvgUtilCore3IRQ": cbsModuleCPUAvgUtilCore3IRQ,
       "cbsModuleCPUAvgUtilCore3SoftIRQ": cbsModuleCPUAvgUtilCore3SoftIRQ,
       "cbsModuleCPUAvgUtilCore3IOWait": cbsModuleCPUAvgUtilCore3IOWait,
       "cbsModuleCPUAvgUtilCore4User": cbsModuleCPUAvgUtilCore4User,
       "cbsModuleCPUAvgUtilCore4Nice": cbsModuleCPUAvgUtilCore4Nice,
       "cbsModuleCPUAvgUtilCore4Syst": cbsModuleCPUAvgUtilCore4Syst,
       "cbsModuleCPUAvgUtilCore4Idle": cbsModuleCPUAvgUtilCore4Idle,
       "cbsModuleCPUAvgUtilCore4IRQ": cbsModuleCPUAvgUtilCore4IRQ,
       "cbsModuleCPUAvgUtilCore4SoftIRQ": cbsModuleCPUAvgUtilCore4SoftIRQ,
       "cbsModuleCPUAvgUtilCore4IOWait": cbsModuleCPUAvgUtilCore4IOWait,
       "cbsModuleCPUAvgUtilCore5User": cbsModuleCPUAvgUtilCore5User,
       "cbsModuleCPUAvgUtilCore5Nice": cbsModuleCPUAvgUtilCore5Nice,
       "cbsModuleCPUAvgUtilCore5Syst": cbsModuleCPUAvgUtilCore5Syst,
       "cbsModuleCPUAvgUtilCore5Idle": cbsModuleCPUAvgUtilCore5Idle,
       "cbsModuleCPUAvgUtilCore5IRQ": cbsModuleCPUAvgUtilCore5IRQ,
       "cbsModuleCPUAvgUtilCore5SoftIRQ": cbsModuleCPUAvgUtilCore5SoftIRQ,
       "cbsModuleCPUAvgUtilCore5IOWait": cbsModuleCPUAvgUtilCore5IOWait,
       "cbsModuleCPUAvgUtilCore6User": cbsModuleCPUAvgUtilCore6User,
       "cbsModuleCPUAvgUtilCore6Nice": cbsModuleCPUAvgUtilCore6Nice,
       "cbsModuleCPUAvgUtilCore6Syst": cbsModuleCPUAvgUtilCore6Syst,
       "cbsModuleCPUAvgUtilCore6Idle": cbsModuleCPUAvgUtilCore6Idle,
       "cbsModuleCPUAvgUtilCore6IRQ": cbsModuleCPUAvgUtilCore6IRQ,
       "cbsModuleCPUAvgUtilCore6SoftIRQ": cbsModuleCPUAvgUtilCore6SoftIRQ,
       "cbsModuleCPUAvgUtilCore6IOWait": cbsModuleCPUAvgUtilCore6IOWait,
       "cbsModuleCPUAvgUtilCore7User": cbsModuleCPUAvgUtilCore7User,
       "cbsModuleCPUAvgUtilCore7Nice": cbsModuleCPUAvgUtilCore7Nice,
       "cbsModuleCPUAvgUtilCore7Syst": cbsModuleCPUAvgUtilCore7Syst,
       "cbsModuleCPUAvgUtilCore7Idle": cbsModuleCPUAvgUtilCore7Idle,
       "cbsModuleCPUAvgUtilCore7IRQ": cbsModuleCPUAvgUtilCore7IRQ,
       "cbsModuleCPUAvgUtilCore7SoftIRQ": cbsModuleCPUAvgUtilCore7SoftIRQ,
       "cbsModuleCPUAvgUtilCore7IOWait": cbsModuleCPUAvgUtilCore7IOWait,
       "cbsModuleCPUAvgUtilCore8User": cbsModuleCPUAvgUtilCore8User,
       "cbsModuleCPUAvgUtilCore8Nice": cbsModuleCPUAvgUtilCore8Nice,
       "cbsModuleCPUAvgUtilCore8Syst": cbsModuleCPUAvgUtilCore8Syst,
       "cbsModuleCPUAvgUtilCore8Idle": cbsModuleCPUAvgUtilCore8Idle,
       "cbsModuleCPUAvgUtilCore8IRQ": cbsModuleCPUAvgUtilCore8IRQ,
       "cbsModuleCPUAvgUtilCore8SoftIRQ": cbsModuleCPUAvgUtilCore8SoftIRQ,
       "cbsModuleCPUAvgUtilCore8IOWait": cbsModuleCPUAvgUtilCore8IOWait,
       "cbsModuleSDPTable": cbsModuleSDPTable,
       "cbsModuleSDPEntry": cbsModuleSDPEntry,
       "cbsModuleSDP0OutPkts": cbsModuleSDP0OutPkts,
       "cbsModuleSDP0OutOctets": cbsModuleSDP0OutOctets,
       "cbsModuleSDP0InPkts": cbsModuleSDP0InPkts,
       "cbsModuleSDP0InOctets": cbsModuleSDP0InOctets,
       "cbsModuleSDP1OutPkts": cbsModuleSDP1OutPkts,
       "cbsModuleSDP1OutOctets": cbsModuleSDP1OutOctets,
       "cbsModuleSDP1InPkts": cbsModuleSDP1InPkts,
       "cbsModuleSDP1InOctets": cbsModuleSDP1InOctets,
       "cbsModuleSDP2OutPkts": cbsModuleSDP2OutPkts,
       "cbsModuleSDP2OutOctets": cbsModuleSDP2OutOctets,
       "cbsModuleSDP2InPkts": cbsModuleSDP2InPkts,
       "cbsModuleSDP2InOctets": cbsModuleSDP2InOctets,
       "cbsModuleSDP3OutPkts": cbsModuleSDP3OutPkts,
       "cbsModuleSDP3OutOctets": cbsModuleSDP3OutOctets,
       "cbsModuleSDP3InPkts": cbsModuleSDP3InPkts,
       "cbsModuleSDP3InOctets": cbsModuleSDP3InOctets,
       "cbsModuleSDP4OutPkts": cbsModuleSDP4OutPkts,
       "cbsModuleSDP4OutOctets": cbsModuleSDP4OutOctets,
       "cbsModuleSDP4InPkts": cbsModuleSDP4InPkts,
       "cbsModuleSDP4InOctets": cbsModuleSDP4InOctets,
       "cbsModuleSDP5OutPkts": cbsModuleSDP5OutPkts,
       "cbsModuleSDP5OutOctets": cbsModuleSDP5OutOctets,
       "cbsModuleSDP5InPkts": cbsModuleSDP5InPkts,
       "cbsModuleSDP5InOctets": cbsModuleSDP5InOctets,
       "cbsModuleSDP6OutPkts": cbsModuleSDP6OutPkts,
       "cbsModuleSDP6OutOctets": cbsModuleSDP6OutOctets,
       "cbsModuleSDP6InPkts": cbsModuleSDP6InPkts,
       "cbsModuleSDP6InOctets": cbsModuleSDP6InOctets,
       "cbsModuleSDP7OutPkts": cbsModuleSDP7OutPkts,
       "cbsModuleSDP7OutOctets": cbsModuleSDP7OutOctets,
       "cbsModuleSDP7InPkts": cbsModuleSDP7InPkts,
       "cbsModuleSDP7InOctets": cbsModuleSDP7InOctets,
       "cbsModuleUptimeTable": cbsModuleUptimeTable,
       "cbsModuleUptimeEntry": cbsModuleUptimeEntry,
       "cbsModuleUptime": cbsModuleUptime,
       "cbsModuleNPMFlowCountTable": cbsModuleNPMFlowCountTable,
       "cbsModuleNPMFlowCountEntry": cbsModuleNPMFlowCountEntry,
       "cbsModuleNPMFlowCount": cbsModuleNPMFlowCount,
       "cbsModuleAppMonTable": cbsModuleAppMonTable,
       "cbsModuleAppMonEntry": cbsModuleAppMonEntry,
       "cbsModuleAppName": cbsModuleAppName,
       "cbsModuleAppVersion": cbsModuleAppVersion,
       "cbsModuleAppRelease": cbsModuleAppRelease,
       "cbsModuleAppCPMHostName": cbsModuleAppCPMHostName,
       "cbsModuleAppCPMIPAddress": cbsModuleAppCPMIPAddress,
       "cbsModuleAppVAPGroupName": cbsModuleAppVAPGroupName,
       "cbsModuleAppVAPIndex": cbsModuleAppVAPIndex,
       "cbsModuleAppOldState": cbsModuleAppOldState,
       "cbsModuleAppNewState": cbsModuleAppNewState,
       "cbsModuleRSWName": cbsModuleRSWName,
       "cbsModuleRSWVersion": cbsModuleRSWVersion,
       "cbsModuleRSWRelease": cbsModuleRSWRelease,
       "cbsModuleRSWStartOnBoot": cbsModuleRSWStartOnBoot,
       "cbsModuleRSWCPMHostName": cbsModuleRSWCPMHostName,
       "cbsModuleRSWCPMIPAddress": cbsModuleRSWCPMIPAddress,
       "cbsModuleRSWVAPGroupName": cbsModuleRSWVAPGroupName,
       "cbsModuleRSWVAPIndex": cbsModuleRSWVAPIndex,
       "cbsModuleRSWOldState": cbsModuleRSWOldState,
       "cbsModuleRSWNewState": cbsModuleRSWNewState,
       "cbsModuleNtpdMonTable": cbsModuleNtpdMonTable,
       "cbsModuleNtpdMonEntry": cbsModuleNtpdMonEntry,
       "cbsModuleNtpdCPMHostName": cbsModuleNtpdCPMHostName,
       "cbsModuleNtpdCPMIPAddress": cbsModuleNtpdCPMIPAddress,
       "cbsModuleNtpdState": cbsModuleNtpdState,
       "cbsModuleCpuCoreHiUtilTable": cbsModuleCpuCoreHiUtilTable,
       "cbsModuleCpuCoreHiUtilEntry": cbsModuleCpuCoreHiUtilEntry,
       "cbsModuleCpuCoreHiUtilSeverity": cbsModuleCpuCoreHiUtilSeverity,
       "cbsModuleCpuCoreHiUtilPerc": cbsModuleCpuCoreHiUtilPerc,
       "cbsModuleCpuCoreHiUtilCores": cbsModuleCpuCoreHiUtilCores,
       "cbsModuleCpuCoreHiUtilDuration": cbsModuleCpuCoreHiUtilDuration,
       "cbsNpmFlowTableUtilTable": cbsNpmFlowTableUtilTable,
       "cbsNpmFlowTableUtilEntry": cbsNpmFlowTableUtilEntry,
       "cbsNpmFTUtilSeverity": cbsNpmFTUtilSeverity,
       "cbsNpmFTTriggerThreshold": cbsNpmFTTriggerThreshold,
       "cbsNpmFTUsage": cbsNpmFTUsage,
       "cbsNpmFTUdpLimitThreshold": cbsNpmFTUdpLimitThreshold,
       "cbsNpmFTUdpMedianThreshold": cbsNpmFTUdpMedianThreshold,
       "cbsNpmFTUdpQuotaUsage": cbsNpmFTUdpQuotaUsage,
       "cbsNpmFTTcpLimitThreshold": cbsNpmFTTcpLimitThreshold,
       "cbsNpmFTTcpMedianThreshold": cbsNpmFTTcpMedianThreshold,
       "cbsNpmFTTcpQuotaUsage": cbsNpmFTTcpQuotaUsage,
       "cbsNpmFTIcmpLimitThreshold": cbsNpmFTIcmpLimitThreshold,
       "cbsNpmFTIcmpMedianThreshold": cbsNpmFTIcmpMedianThreshold,
       "cbsNpmFTIcmpQuotaUsage": cbsNpmFTIcmpQuotaUsage,
       "cbsNpmFTOtherIpLimitThreshold": cbsNpmFTOtherIpLimitThreshold,
       "cbsNpmFTOtherIpMedianThreshold": cbsNpmFTOtherIpMedianThreshold,
       "cbsNpmFTOtherIpQuotaUsage": cbsNpmFTOtherIpQuotaUsage,
       "cbsModuleSdramMemCfgStatTable": cbsModuleSdramMemCfgStatTable,
       "cbsModuleSdramMemCfgStatEntry": cbsModuleSdramMemCfgStatEntry,
       "cbsModuleSdramMemCfgStat": cbsModuleSdramMemCfgStat,
       "cbsModuleGuestHealthTable": cbsModuleGuestHealthTable,
       "cbsModuleGuestHealthTableEntry": cbsModuleGuestHealthTableEntry,
       "cbsApmGuestHealthSeverity": cbsApmGuestHealthSeverity,
       "cbsCpmDiskCfgStat": cbsCpmDiskCfgStat,
       "cbsModuleApplicationTable": cbsModuleApplicationTable,
       "cbsModuleApplicationEntry": cbsModuleApplicationEntry,
       "cbsModuleApplicationName": cbsModuleApplicationName,
       "cbsModuleApplicationVersion": cbsModuleApplicationVersion,
       "cbsModuleApplicationRelease": cbsModuleApplicationRelease,
       "cbsModuleApplicationMonEnabled": cbsModuleApplicationMonEnabled,
       "cbsModuleApplicationVgName": cbsModuleApplicationVgName,
       "cbsFlowTablePartitionThreshold": cbsFlowTablePartitionThreshold,
       "cbsFlowTableCriticalAlarm": cbsFlowTableCriticalAlarm,
       "cbsFlowTableUtilization": cbsFlowTableUtilization,
       "cbsFlowTableUtilTcpFlowEntries": cbsFlowTableUtilTcpFlowEntries,
       "cbsFlowTableUtilUdpFlowEntries": cbsFlowTableUtilUdpFlowEntries,
       "cbsFlowTableUtilIcmpFlowEntries": cbsFlowTableUtilIcmpFlowEntries,
       "cbsFlowTableUtilOtherIpFlowEntries": cbsFlowTableUtilOtherIpFlowEntries,
       "cbsNpmFlowDistTable": cbsNpmFlowDistTable,
       "cbsNpmFlowDistEntry": cbsNpmFlowDistEntry,
       "cbsNpmSlotId": cbsNpmSlotId,
       "cbsNpmTcpCurrentFlows": cbsNpmTcpCurrentFlows,
       "cbsNpmUdpCurrentFlows": cbsNpmUdpCurrentFlows,
       "cbsNpmIcmpCurrentFlows": cbsNpmIcmpCurrentFlows,
       "cbsNpmOtherIpCurrentFlows": cbsNpmOtherIpCurrentFlows,
       "cbsNpmNewFlowRate": cbsNpmNewFlowRate,
       "cbsNpmAgedFlowRate": cbsNpmAgedFlowRate,
       "cbsVapFlowDistTable": cbsVapFlowDistTable,
       "cbsVapFlowDistEntry": cbsVapFlowDistEntry,
       "cbsVapFlowGroupID": cbsVapFlowGroupID,
       "cbsVapFlowIndex": cbsVapFlowIndex,
       "cbsVapName": cbsVapName,
       "cbsVapCurrentFlows": cbsVapCurrentFlows,
       "cbsVapNewFlowRate": cbsVapNewFlowRate,
       "cbsVapAgedFlowRate": cbsVapAgedFlowRate,
       "cbsModuleResourcesMIB": cbsModuleResourcesMIB,
       "cbsModuleResourceTraps": cbsModuleResourceTraps,
       "cbsModuleCPULoadExceeded": cbsModuleCPULoadExceeded,
       "cbsModuleCPULoadNormal": cbsModuleCPULoadNormal,
       "cbsModuleMemoryUsageExceeded": cbsModuleMemoryUsageExceeded,
       "cbsModuleMemoryUsageNormal": cbsModuleMemoryUsageNormal,
       "cbsModuleCPUUtilExceeded": cbsModuleCPUUtilExceeded,
       "cbsModuleCPUUtilNormal": cbsModuleCPUUtilNormal,
       "cbsModuleDURootHigh": cbsModuleDURootHigh,
       "cbsModuleDURootNormal": cbsModuleDURootNormal,
       "cbsModuleDUBootHigh": cbsModuleDUBootHigh,
       "cbsModuleDUBootNormal": cbsModuleDUBootNormal,
       "cbsModuleDUCbconfigHigh": cbsModuleDUCbconfigHigh,
       "cbsModuleDUCbconfigNormal": cbsModuleDUCbconfigNormal,
       "cbsModuleDUTftpbootHigh": cbsModuleDUTftpbootHigh,
       "cbsModuleDUTftpbootNormal": cbsModuleDUTftpbootNormal,
       "cbsModuleFreePageAvailableHigh": cbsModuleFreePageAvailableHigh,
       "cbsModuleFreePageAvailableNorm": cbsModuleFreePageAvailableNorm,
       "cbsModuleMUHigh": cbsModuleMUHigh,
       "cbsModuleMUNormal": cbsModuleMUNormal,
       "cbsModuleFRHigh": cbsModuleFRHigh,
       "cbsModuleFRNormal": cbsModuleFRNormal,
       "cbsModuleBUHigh": cbsModuleBUHigh,
       "cbsModuleBUNormal": cbsModuleBUNormal,
       "cbsModuleAppStateChange": cbsModuleAppStateChange,
       "cbsModuleNtpdMonStateChange": cbsModuleNtpdMonStateChange,
       "cbsModuleDUMgmtHigh": cbsModuleDUMgmtHigh,
       "cbsModuleDUMgmtNormal": cbsModuleDUMgmtNormal,
       "cbsModuleCpuCoreUtilExceeded": cbsModuleCpuCoreUtilExceeded,
       "cbsModuleCpuCoreUtilNormal": cbsModuleCpuCoreUtilNormal,
       "cbsNpmFlowTableUsageHigh": cbsNpmFlowTableUsageHigh,
       "cbsNpmFlowTableUsageNormal": cbsNpmFlowTableUsageNormal,
       "cbsNpmFTUdpLimitExceeded": cbsNpmFTUdpLimitExceeded,
       "cbsNpmFTUdpLimitNormal": cbsNpmFTUdpLimitNormal,
       "cbsNpmFTUdpMedianExceeded": cbsNpmFTUdpMedianExceeded,
       "cbsNpmFTUdpMedianNormal": cbsNpmFTUdpMedianNormal,
       "cbsNpmFTTcpLimitExceeded": cbsNpmFTTcpLimitExceeded,
       "cbsNpmFTTcpLimitNormal": cbsNpmFTTcpLimitNormal,
       "cbsNpmFTTcpMedianExceeded": cbsNpmFTTcpMedianExceeded,
       "cbsNpmFTTcpMedianNormal": cbsNpmFTTcpMedianNormal,
       "cbsNpmFTIcmpLimitExceeded": cbsNpmFTIcmpLimitExceeded,
       "cbsNpmFTIcmpLimitNormal": cbsNpmFTIcmpLimitNormal,
       "cbsNpmFTIcmpMedianExceeded": cbsNpmFTIcmpMedianExceeded,
       "cbsNpmFTIcmpMedianNormal": cbsNpmFTIcmpMedianNormal,
       "cbsNpmFTOtherIpLimitExceeded": cbsNpmFTOtherIpLimitExceeded,
       "cbsNpmFTOtherIpLimitNormal": cbsNpmFTOtherIpLimitNormal,
       "cbsNpmFTOtherIpMedianExceeded": cbsNpmFTOtherIpMedianExceeded,
       "cbsNpmFTOtherIpMedianNormal": cbsNpmFTOtherIpMedianNormal,
       "cbsModuleSdramCheck": cbsModuleSdramCheck,
       "cbsApmGuestHealthCheck": cbsApmGuestHealthCheck,
       "cbsCpmDiskCheck": cbsCpmDiskCheck,
       "cbsModuleDUVarHigh": cbsModuleDUVarHigh,
       "cbsModuleDUVarNormal": cbsModuleDUVarNormal,
       "cbsModuleRSWStateChange": cbsModuleRSWStateChange}
)
