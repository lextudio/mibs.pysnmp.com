# SNMP MIB module (BAS-CMTS-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-CMTS-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:22 2024
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

(basDocsIfCmtsCmStatusEntry,) = mibBuilder.importSymbols(
    "BAS-ALIAS-DOCS-IF-MIB",
    "basDocsIfCmtsCmStatusEntry")

(basExtCmts,) = mibBuilder.importSymbols(
    "BAS-MIB",
    "basExtCmts")

(docsIfCmtsCmStatusEntry,
 docsIfCmtsModulationEntry,
 docsIfCmtsServiceEntry,
 docsIfDownstreamChannelEntry,
 docsIfUpstreamChannelEntry) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsCmStatusEntry",
    "docsIfCmtsModulationEntry",
    "docsIfCmtsServiceEntry",
    "docsIfDownstreamChannelEntry",
    "docsIfUpstreamChannelEntry")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

basCmtsConfigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BasCmtsInt8(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )



class BasCmtsUInt8(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class BasCmtsByte(BasCmtsUInt8, TextualConvention):
    status = "current"
    displayHint = "d"


class BasCmtsInt16(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class BasCmtsUInt16(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BasCmtsInt32(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class BasCmtsUInt32(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class BasCmtsRowAction(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basCmtsRowActionApply", 2),
          ("basCmtsRowActionNone", 1))
    )



class TenthdBmV(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class BasCmtsHeadEndMapMode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(99, 99),
    )



class BasCmtsHeadEndMacAddr(OctetString, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class BasCmtsHeadEndAuthString(OctetString, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class BasCmtsUpChannelPreamblePattern(OctetString, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class BasCmtsModulationWsPattern(OctetString, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



# MIB Managed Objects in the order of their OIDs

_BasCmtsConfigObjects_ObjectIdentity = ObjectIdentity
basCmtsConfigObjects = _BasCmtsConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1)
)
_BasCmtsHeadEndTable_Object = MibTable
basCmtsHeadEndTable = _BasCmtsHeadEndTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basCmtsHeadEndTable.setStatus("current")
_BasCmtsHeadEndEntry_Object = MibTableRow
basCmtsHeadEndEntry = _BasCmtsHeadEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1)
)
basCmtsHeadEndEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    basCmtsHeadEndEntry.setStatus("current")


class _BasCmtsHeDsChanId_Type(BasCmtsByte):
    """Custom type basCmtsHeDsChanId based on BasCmtsByte"""
    defaultValue = 0


_BasCmtsHeDsChanId_Object = MibTableColumn
basCmtsHeDsChanId = _BasCmtsHeDsChanId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 1),
    _BasCmtsHeDsChanId_Type()
)
basCmtsHeDsChanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHeDsChanId.setStatus("current")


class _BasCmtsHeHwMapTimerPeriodMicrosec_Type(BasCmtsUInt16):
    """Custom type basCmtsHeHwMapTimerPeriodMicrosec based on BasCmtsUInt16"""
    defaultValue = 2000


_BasCmtsHeHwMapTimerPeriodMicrosec_Object = MibTableColumn
basCmtsHeHwMapTimerPeriodMicrosec = _BasCmtsHeHwMapTimerPeriodMicrosec_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 2),
    _BasCmtsHeHwMapTimerPeriodMicrosec_Type()
)
basCmtsHeHwMapTimerPeriodMicrosec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHeHwMapTimerPeriodMicrosec.setStatus("current")


class _BasCmtsHeImMapTimerPeriodMillisec_Type(BasCmtsUInt16):
    """Custom type basCmtsHeImMapTimerPeriodMillisec based on BasCmtsUInt16"""
    defaultValue = 2000


_BasCmtsHeImMapTimerPeriodMillisec_Object = MibTableColumn
basCmtsHeImMapTimerPeriodMillisec = _BasCmtsHeImMapTimerPeriodMillisec_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 3),
    _BasCmtsHeImMapTimerPeriodMillisec_Type()
)
basCmtsHeImMapTimerPeriodMillisec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHeImMapTimerPeriodMillisec.setStatus("current")
_BasCmtsHePerRngTimerPeriodSec_Type = BasCmtsUInt16
_BasCmtsHePerRngTimerPeriodSec_Object = MibTableColumn
basCmtsHePerRngTimerPeriodSec = _BasCmtsHePerRngTimerPeriodSec_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 4),
    _BasCmtsHePerRngTimerPeriodSec_Type()
)
basCmtsHePerRngTimerPeriodSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHePerRngTimerPeriodSec.setStatus("current")


class _BasCmtsHeUcdTimerPerMillisec_Type(BasCmtsUInt16):
    """Custom type basCmtsHeUcdTimerPerMillisec based on BasCmtsUInt16"""
    defaultValue = 2000


_BasCmtsHeUcdTimerPerMillisec_Object = MibTableColumn
basCmtsHeUcdTimerPerMillisec = _BasCmtsHeUcdTimerPerMillisec_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 5),
    _BasCmtsHeUcdTimerPerMillisec_Type()
)
basCmtsHeUcdTimerPerMillisec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHeUcdTimerPerMillisec.setStatus("current")


class _BasCmtsHeMapMode_Type(BasCmtsHeadEndMapMode):
    """Custom type basCmtsHeMapMode based on BasCmtsHeadEndMapMode"""
    defaultValue = 0


_BasCmtsHeMapMode_Object = MibTableColumn
basCmtsHeMapMode = _BasCmtsHeMapMode_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 6),
    _BasCmtsHeMapMode_Type()
)
basCmtsHeMapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHeMapMode.setStatus("current")
_BasCmtsHeMacAddr_Type = BasCmtsHeadEndMacAddr
_BasCmtsHeMacAddr_Object = MibTableColumn
basCmtsHeMacAddr = _BasCmtsHeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 7),
    _BasCmtsHeMacAddr_Type()
)
basCmtsHeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsHeMacAddr.setStatus("current")


class _BasCmtsHeLenAuthString_Type(BasCmtsByte):
    """Custom type basCmtsHeLenAuthString based on BasCmtsByte"""
    defaultValue = 0


_BasCmtsHeLenAuthString_Object = MibTableColumn
basCmtsHeLenAuthString = _BasCmtsHeLenAuthString_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 8),
    _BasCmtsHeLenAuthString_Type()
)
basCmtsHeLenAuthString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHeLenAuthString.setStatus("current")


class _BasCmtsHeAuthString_Type(BasCmtsHeadEndAuthString):
    """Custom type basCmtsHeAuthString based on BasCmtsHeadEndAuthString"""
    defaultHexValue = "0"


_BasCmtsHeAuthString_Object = MibTableColumn
basCmtsHeAuthString = _BasCmtsHeAuthString_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 9),
    _BasCmtsHeAuthString_Type()
)
basCmtsHeAuthString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHeAuthString.setStatus("current")
_BasCmtsHeRowAction_Type = BasCmtsRowAction
_BasCmtsHeRowAction_Object = MibTableColumn
basCmtsHeRowAction = _BasCmtsHeRowAction_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 10),
    _BasCmtsHeRowAction_Type()
)
basCmtsHeRowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHeRowAction.setStatus("current")
_BasCmtsHePlantPropDelay_Type = BasCmtsUInt32
_BasCmtsHePlantPropDelay_Object = MibTableColumn
basCmtsHePlantPropDelay = _BasCmtsHePlantPropDelay_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 11),
    _BasCmtsHePlantPropDelay_Type()
)
basCmtsHePlantPropDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHePlantPropDelay.setStatus("current")
_BasCmtsHeSupplMapLeadDelay_Type = BasCmtsInt32
_BasCmtsHeSupplMapLeadDelay_Object = MibTableColumn
basCmtsHeSupplMapLeadDelay = _BasCmtsHeSupplMapLeadDelay_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 1, 1, 12),
    _BasCmtsHeSupplMapLeadDelay_Type()
)
basCmtsHeSupplMapLeadDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsHeSupplMapLeadDelay.setStatus("current")
_BasCmtsMacTable_Object = MibTable
basCmtsMacTable = _BasCmtsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basCmtsMacTable.setStatus("current")
_BasCmtsMacEntry_Object = MibTableRow
basCmtsMacEntry = _BasCmtsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1)
)
basCmtsMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    basCmtsMacEntry.setStatus("current")


class _BasCmtsMacNumUsBds_Type(BasCmtsUInt16):
    """Custom type basCmtsMacNumUsBds based on BasCmtsUInt16"""
    defaultValue = 32

    subtypeSpec = BasCmtsUInt16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BasCmtsMacNumUsBds_Type.__name__ = "BasCmtsUInt16"
_BasCmtsMacNumUsBds_Object = MibTableColumn
basCmtsMacNumUsBds = _BasCmtsMacNumUsBds_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 1),
    _BasCmtsMacNumUsBds_Type()
)
basCmtsMacNumUsBds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacNumUsBds.setStatus("current")


class _BasCmtsMacNumDsMsgBds_Type(BasCmtsUInt16):
    """Custom type basCmtsMacNumDsMsgBds based on BasCmtsUInt16"""
    defaultValue = 32

    subtypeSpec = BasCmtsUInt16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BasCmtsMacNumDsMsgBds_Type.__name__ = "BasCmtsUInt16"
_BasCmtsMacNumDsMsgBds_Object = MibTableColumn
basCmtsMacNumDsMsgBds = _BasCmtsMacNumDsMsgBds_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 2),
    _BasCmtsMacNumDsMsgBds_Type()
)
basCmtsMacNumDsMsgBds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacNumDsMsgBds.setStatus("current")


class _BasCmtsMacNumDsDataBds_Type(BasCmtsUInt16):
    """Custom type basCmtsMacNumDsDataBds based on BasCmtsUInt16"""
    defaultValue = 32

    subtypeSpec = BasCmtsUInt16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BasCmtsMacNumDsDataBds_Type.__name__ = "BasCmtsUInt16"
_BasCmtsMacNumDsDataBds_Object = MibTableColumn
basCmtsMacNumDsDataBds = _BasCmtsMacNumDsDataBds_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 3),
    _BasCmtsMacNumDsDataBds_Type()
)
basCmtsMacNumDsDataBds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacNumDsDataBds.setStatus("current")


class _BasCmtsMacNumIpBuffers_Type(BasCmtsUInt16):
    """Custom type basCmtsMacNumIpBuffers based on BasCmtsUInt16"""
    defaultValue = 32

    subtypeSpec = BasCmtsUInt16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BasCmtsMacNumIpBuffers_Type.__name__ = "BasCmtsUInt16"
_BasCmtsMacNumIpBuffers_Object = MibTableColumn
basCmtsMacNumIpBuffers = _BasCmtsMacNumIpBuffers_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 4),
    _BasCmtsMacNumIpBuffers_Type()
)
basCmtsMacNumIpBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacNumIpBuffers.setStatus("current")


class _BasCmtsMacPciDmaSize_Type(BasCmtsByte):
    """Custom type basCmtsMacPciDmaSize based on BasCmtsByte"""
    defaultHexValue = 128


_BasCmtsMacPciDmaSize_Object = MibTableColumn
basCmtsMacPciDmaSize = _BasCmtsMacPciDmaSize_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 5),
    _BasCmtsMacPciDmaSize_Type()
)
basCmtsMacPciDmaSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacPciDmaSize.setStatus("current")


class _BasCmtsMacUpdateFirstParticleLast_Type(TruthValue):
    """Custom type basCmtsMacUpdateFirstParticleLast based on TruthValue"""


_BasCmtsMacUpdateFirstParticleLast_Object = MibTableColumn
basCmtsMacUpdateFirstParticleLast = _BasCmtsMacUpdateFirstParticleLast_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 6),
    _BasCmtsMacUpdateFirstParticleLast_Type()
)
basCmtsMacUpdateFirstParticleLast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacUpdateFirstParticleLast.setStatus("current")


class _BasCmtsMacDirectModeDma_Type(TruthValue):
    """Custom type basCmtsMacDirectModeDma based on TruthValue"""


_BasCmtsMacDirectModeDma_Object = MibTableColumn
basCmtsMacDirectModeDma = _BasCmtsMacDirectModeDma_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 7),
    _BasCmtsMacDirectModeDma_Type()
)
basCmtsMacDirectModeDma.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacDirectModeDma.setStatus("current")


class _BasCmtsMacPackedPart_Type(TruthValue):
    """Custom type basCmtsMacPackedPart based on TruthValue"""


_BasCmtsMacPackedPart_Object = MibTableColumn
basCmtsMacPackedPart = _BasCmtsMacPackedPart_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 8),
    _BasCmtsMacPackedPart_Type()
)
basCmtsMacPackedPart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacPackedPart.setStatus("current")


class _BasCmtsMacPackedPartOffset_Type(BasCmtsUInt16):
    """Custom type basCmtsMacPackedPartOffset based on BasCmtsUInt16"""
    defaultValue = 12


_BasCmtsMacPackedPartOffset_Object = MibTableColumn
basCmtsMacPackedPartOffset = _BasCmtsMacPackedPartOffset_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 9),
    _BasCmtsMacPackedPartOffset_Type()
)
basCmtsMacPackedPartOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacPackedPartOffset.setStatus("current")


class _BasCmtsMacSpiClkDivider_Type(BasCmtsByte):
    """Custom type basCmtsMacSpiClkDivider based on BasCmtsByte"""
    defaultHexValue = 16


_BasCmtsMacSpiClkDivider_Object = MibTableColumn
basCmtsMacSpiClkDivider = _BasCmtsMacSpiClkDivider_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 10),
    _BasCmtsMacSpiClkDivider_Type()
)
basCmtsMacSpiClkDivider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacSpiClkDivider.setStatus("current")


class _BasCmtsMacSyncRate_Type(BasCmtsUInt32):
    """Custom type basCmtsMacSyncRate based on BasCmtsUInt32"""
    defaultValue = 10


_BasCmtsMacSyncRate_Object = MibTableColumn
basCmtsMacSyncRate = _BasCmtsMacSyncRate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 11),
    _BasCmtsMacSyncRate_Type()
)
basCmtsMacSyncRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacSyncRate.setStatus("current")
_BasCmtsMacRowAction_Type = BasCmtsRowAction
_BasCmtsMacRowAction_Object = MibTableColumn
basCmtsMacRowAction = _BasCmtsMacRowAction_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 2, 1, 12),
    _BasCmtsMacRowAction_Type()
)
basCmtsMacRowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacRowAction.setStatus("current")
_BasCmtsMacDsHwTable_Object = MibTable
basCmtsMacDsHwTable = _BasCmtsMacDsHwTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    basCmtsMacDsHwTable.setStatus("current")
_BasCmtsMacDsHwEntry_Object = MibTableRow
basCmtsMacDsHwEntry = _BasCmtsMacDsHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    basCmtsMacDsHwEntry.setStatus("current")


class _BasCmtsMacDsHwInterleaverDepth_Type(Integer32):
    """Custom type basCmtsMacDsHwInterleaverDepth based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("basCmtsMacDsHwIntDepth128", 128),
          ("basCmtsMacDsHwIntDepth16", 16),
          ("basCmtsMacDsHwIntDepth32", 32),
          ("basCmtsMacDsHwIntDepth64", 64),
          ("basCmtsMacDsHwIntDepth8", 8))
    )


_BasCmtsMacDsHwInterleaverDepth_Type.__name__ = "Integer32"
_BasCmtsMacDsHwInterleaverDepth_Object = MibTableColumn
basCmtsMacDsHwInterleaverDepth = _BasCmtsMacDsHwInterleaverDepth_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 3, 1, 1),
    _BasCmtsMacDsHwInterleaverDepth_Type()
)
basCmtsMacDsHwInterleaverDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacDsHwInterleaverDepth.setStatus("current")


class _BasCmtsMacDsHwQamctl_Type(Integer32):
    """Custom type basCmtsMacDsHwQamctl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("basCmtsMacDsHwQamctl256QAM", 5),
          ("basCmtsMacDsHwQamctl64QAM", 3))
    )


_BasCmtsMacDsHwQamctl_Type.__name__ = "Integer32"
_BasCmtsMacDsHwQamctl_Object = MibTableColumn
basCmtsMacDsHwQamctl = _BasCmtsMacDsHwQamctl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 3, 1, 2),
    _BasCmtsMacDsHwQamctl_Type()
)
basCmtsMacDsHwQamctl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacDsHwQamctl.setStatus("current")


class _BasCmtsMacDsHwSymbolRate_Type(BasCmtsUInt32):
    """Custom type basCmtsMacDsHwSymbolRate based on BasCmtsUInt32"""
    defaultValue = 5056941


_BasCmtsMacDsHwSymbolRate_Object = MibTableColumn
basCmtsMacDsHwSymbolRate = _BasCmtsMacDsHwSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 3, 1, 3),
    _BasCmtsMacDsHwSymbolRate_Type()
)
basCmtsMacDsHwSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacDsHwSymbolRate.setStatus("current")


class _BasCmtsMacDsHwIfFreq_Type(BasCmtsUInt32):
    """Custom type basCmtsMacDsHwIfFreq based on BasCmtsUInt32"""
    defaultValue = 43750000


_BasCmtsMacDsHwIfFreq_Object = MibTableColumn
basCmtsMacDsHwIfFreq = _BasCmtsMacDsHwIfFreq_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 3, 1, 4),
    _BasCmtsMacDsHwIfFreq_Type()
)
basCmtsMacDsHwIfFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacDsHwIfFreq.setStatus("current")


class _BasCmtsMacDsHwRefFreq_Type(BasCmtsUInt32):
    """Custom type basCmtsMacDsHwRefFreq based on BasCmtsUInt32"""
    defaultValue = 28500000


_BasCmtsMacDsHwRefFreq_Object = MibTableColumn
basCmtsMacDsHwRefFreq = _BasCmtsMacDsHwRefFreq_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 3, 1, 5),
    _BasCmtsMacDsHwRefFreq_Type()
)
basCmtsMacDsHwRefFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacDsHwRefFreq.setStatus("current")


class _BasCmtsMacDsHwOscMultFactor_Type(BasCmtsByte):
    """Custom type basCmtsMacDsHwOscMultFactor based on BasCmtsByte"""
    defaultValue = 4


_BasCmtsMacDsHwOscMultFactor_Object = MibTableColumn
basCmtsMacDsHwOscMultFactor = _BasCmtsMacDsHwOscMultFactor_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 3, 1, 6),
    _BasCmtsMacDsHwOscMultFactor_Type()
)
basCmtsMacDsHwOscMultFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMacDsHwOscMultFactor.setStatus("current")
_BasCmtsUpstreamChannelTable_Object = MibTable
basCmtsUpstreamChannelTable = _BasCmtsUpstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    basCmtsUpstreamChannelTable.setStatus("current")
_BasCmtsUpstreamChannelEntry_Object = MibTableRow
basCmtsUpstreamChannelEntry = _BasCmtsUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    basCmtsUpstreamChannelEntry.setStatus("current")


class _BasCmtsUpChannelMslotPerTick_Type(BasCmtsByte):
    """Custom type basCmtsUpChannelMslotPerTick based on BasCmtsByte"""
    defaultValue = 4


_BasCmtsUpChannelMslotPerTick_Object = MibTableColumn
basCmtsUpChannelMslotPerTick = _BasCmtsUpChannelMslotPerTick_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 4, 1, 1),
    _BasCmtsUpChannelMslotPerTick_Type()
)
basCmtsUpChannelMslotPerTick.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUpChannelMslotPerTick.setStatus("current")


class _BasCmtsUpChannelSymbolRate160KSymPerSec_Type(BasCmtsByte):
    """Custom type basCmtsUpChannelSymbolRate160KSymPerSec based on BasCmtsByte"""
    defaultValue = 8


_BasCmtsUpChannelSymbolRate160KSymPerSec_Object = MibTableColumn
basCmtsUpChannelSymbolRate160KSymPerSec = _BasCmtsUpChannelSymbolRate160KSymPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 4, 1, 2),
    _BasCmtsUpChannelSymbolRate160KSymPerSec_Type()
)
basCmtsUpChannelSymbolRate160KSymPerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUpChannelSymbolRate160KSymPerSec.setStatus("current")


class _BasCmtsUpChannelLenPreamblePattern_Type(BasCmtsByte):
    """Custom type basCmtsUpChannelLenPreamblePattern based on BasCmtsByte"""
    defaultValue = 16


_BasCmtsUpChannelLenPreamblePattern_Object = MibTableColumn
basCmtsUpChannelLenPreamblePattern = _BasCmtsUpChannelLenPreamblePattern_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 4, 1, 3),
    _BasCmtsUpChannelLenPreamblePattern_Type()
)
basCmtsUpChannelLenPreamblePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUpChannelLenPreamblePattern.setStatus("current")


class _BasCmtsUpChannelPreamblePattern_Type(BasCmtsUpChannelPreamblePattern):
    """Custom type basCmtsUpChannelPreamblePattern based on BasCmtsUpChannelPreamblePattern"""
    defaultHexValue = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC0D0D"


_BasCmtsUpChannelPreamblePattern_Object = MibTableColumn
basCmtsUpChannelPreamblePattern = _BasCmtsUpChannelPreamblePattern_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 4, 1, 4),
    _BasCmtsUpChannelPreamblePattern_Type()
)
basCmtsUpChannelPreamblePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUpChannelPreamblePattern.setStatus("current")
_BasCmtsUpChannelRowAction_Type = BasCmtsRowAction
_BasCmtsUpChannelRowAction_Object = MibTableColumn
basCmtsUpChannelRowAction = _BasCmtsUpChannelRowAction_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 4, 1, 5),
    _BasCmtsUpChannelRowAction_Type()
)
basCmtsUpChannelRowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUpChannelRowAction.setStatus("current")
_BasCmtsUpChannelReceivePower_Type = TenthdBmV
_BasCmtsUpChannelReceivePower_Object = MibTableColumn
basCmtsUpChannelReceivePower = _BasCmtsUpChannelReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 4, 1, 6),
    _BasCmtsUpChannelReceivePower_Type()
)
basCmtsUpChannelReceivePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUpChannelReceivePower.setStatus("current")
_BasCmtsModulationTable_Object = MibTable
basCmtsModulationTable = _BasCmtsModulationTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    basCmtsModulationTable.setStatus("current")
_BasCmtsModulationEntry_Object = MibTableRow
basCmtsModulationEntry = _BasCmtsModulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    basCmtsModulationEntry.setStatus("current")


class _BasCmtsModUwLenBytes_Type(BasCmtsByte):
    """Custom type basCmtsModUwLenBytes based on BasCmtsByte"""
    defaultValue = 2


_BasCmtsModUwLenBytes_Object = MibTableColumn
basCmtsModUwLenBytes = _BasCmtsModUwLenBytes_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 5, 1, 1),
    _BasCmtsModUwLenBytes_Type()
)
basCmtsModUwLenBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsModUwLenBytes.setStatus("current")


class _BasCmtsModUwPattern_Type(BasCmtsModulationWsPattern):
    """Custom type basCmtsModUwPattern based on BasCmtsModulationWsPattern"""
    defaultHexValue = "0d0d"


_BasCmtsModUwPattern_Object = MibTableColumn
basCmtsModUwPattern = _BasCmtsModUwPattern_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 5, 1, 2),
    _BasCmtsModUwPattern_Type()
)
basCmtsModUwPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsModUwPattern.setStatus("current")


class _BasCmtsModUwDetectionWindow_Type(BasCmtsByte):
    """Custom type basCmtsModUwDetectionWindow based on BasCmtsByte"""
    defaultHexValue = 4


_BasCmtsModUwDetectionWindow_Object = MibTableColumn
basCmtsModUwDetectionWindow = _BasCmtsModUwDetectionWindow_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 5, 1, 3),
    _BasCmtsModUwDetectionWindow_Type()
)
basCmtsModUwDetectionWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsModUwDetectionWindow.setStatus("current")


class _BasCmtsModUwMismatchThresholdBits_Type(BasCmtsByte):
    """Custom type basCmtsModUwMismatchThresholdBits based on BasCmtsByte"""
    defaultValue = 1


_BasCmtsModUwMismatchThresholdBits_Object = MibTableColumn
basCmtsModUwMismatchThresholdBits = _BasCmtsModUwMismatchThresholdBits_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 5, 1, 4),
    _BasCmtsModUwMismatchThresholdBits_Type()
)
basCmtsModUwMismatchThresholdBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsModUwMismatchThresholdBits.setStatus("current")
_BasCmtsModPreambleValueOffset_Type = BasCmtsUInt16
_BasCmtsModPreambleValueOffset_Object = MibTableColumn
basCmtsModPreambleValueOffset = _BasCmtsModPreambleValueOffset_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 5, 1, 5),
    _BasCmtsModPreambleValueOffset_Type()
)
basCmtsModPreambleValueOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsModPreambleValueOffset.setStatus("current")
_BasCmtsUsHwTable_Object = MibTable
basCmtsUsHwTable = _BasCmtsUsHwTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    basCmtsUsHwTable.setStatus("current")
_BasCmtsUsHwEntry_Object = MibTableRow
basCmtsUsHwEntry = _BasCmtsUsHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    basCmtsUsHwEntry.setStatus("current")


class _BasCmtsUsHwTestProbe_Type(BasCmtsByte):
    """Custom type basCmtsUsHwTestProbe based on BasCmtsByte"""
    defaultHexValue = 6


_BasCmtsUsHwTestProbe_Object = MibTableColumn
basCmtsUsHwTestProbe = _BasCmtsUsHwTestProbe_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 1),
    _BasCmtsUsHwTestProbe_Type()
)
basCmtsUsHwTestProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwTestProbe.setStatus("current")


class _BasCmtsUsHwGenCfg1_Type(BasCmtsByte):
    """Custom type basCmtsUsHwGenCfg1 based on BasCmtsByte"""
    defaultHexValue = 3


_BasCmtsUsHwGenCfg1_Object = MibTableColumn
basCmtsUsHwGenCfg1 = _BasCmtsUsHwGenCfg1_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 2),
    _BasCmtsUsHwGenCfg1_Type()
)
basCmtsUsHwGenCfg1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwGenCfg1.setStatus("current")


class _BasCmtsUsHwGenCfg2_Type(BasCmtsByte):
    """Custom type basCmtsUsHwGenCfg2 based on BasCmtsByte"""
    defaultHexValue = 61


_BasCmtsUsHwGenCfg2_Object = MibTableColumn
basCmtsUsHwGenCfg2 = _BasCmtsUsHwGenCfg2_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 3),
    _BasCmtsUsHwGenCfg2_Type()
)
basCmtsUsHwGenCfg2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwGenCfg2.setStatus("current")


class _BasCmtsUsHwPreambleCtl_Type(BasCmtsByte):
    """Custom type basCmtsUsHwPreambleCtl based on BasCmtsByte"""
    defaultHexValue = 125


_BasCmtsUsHwPreambleCtl_Object = MibTableColumn
basCmtsUsHwPreambleCtl = _BasCmtsUsHwPreambleCtl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 4),
    _BasCmtsUsHwPreambleCtl_Type()
)
basCmtsUsHwPreambleCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwPreambleCtl.setStatus("current")


class _BasCmtsUsHwCarrAcf_Type(BasCmtsByte):
    """Custom type basCmtsUsHwCarrAcf based on BasCmtsByte"""
    defaultHexValue = 35


_BasCmtsUsHwCarrAcf_Object = MibTableColumn
basCmtsUsHwCarrAcf = _BasCmtsUsHwCarrAcf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 5),
    _BasCmtsUsHwCarrAcf_Type()
)
basCmtsUsHwCarrAcf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwCarrAcf.setStatus("current")


class _BasCmtsUsHwCarrTcf_Type(BasCmtsByte):
    """Custom type basCmtsUsHwCarrTcf based on BasCmtsByte"""
    defaultHexValue = 51


_BasCmtsUsHwCarrTcf_Object = MibTableColumn
basCmtsUsHwCarrTcf = _BasCmtsUsHwCarrTcf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 6),
    _BasCmtsUsHwCarrTcf_Type()
)
basCmtsUsHwCarrTcf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwCarrTcf.setStatus("current")


class _BasCmtsUsHwBaudAtcf_Type(BasCmtsByte):
    """Custom type basCmtsUsHwBaudAtcf based on BasCmtsByte"""
    defaultHexValue = 51


_BasCmtsUsHwBaudAtcf_Object = MibTableColumn
basCmtsUsHwBaudAtcf = _BasCmtsUsHwBaudAtcf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 7),
    _BasCmtsUsHwBaudAtcf_Type()
)
basCmtsUsHwBaudAtcf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwBaudAtcf.setStatus("current")


class _BasCmtsUsHwBaudIntcf_Type(BasCmtsByte):
    """Custom type basCmtsUsHwBaudIntcf based on BasCmtsByte"""
    defaultHexValue = 1


_BasCmtsUsHwBaudIntcf_Object = MibTableColumn
basCmtsUsHwBaudIntcf = _BasCmtsUsHwBaudIntcf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 8),
    _BasCmtsUsHwBaudIntcf_Type()
)
basCmtsUsHwBaudIntcf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwBaudIntcf.setStatus("current")


class _BasCmtsUsHwMaxPwrThr_Type(BasCmtsByte):
    """Custom type basCmtsUsHwMaxPwrThr based on BasCmtsByte"""
    defaultHexValue = 64


_BasCmtsUsHwMaxPwrThr_Object = MibTableColumn
basCmtsUsHwMaxPwrThr = _BasCmtsUsHwMaxPwrThr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 9),
    _BasCmtsUsHwMaxPwrThr_Type()
)
basCmtsUsHwMaxPwrThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwMaxPwrThr.setStatus("current")


class _BasCmtsUsHwMinPwrThr_Type(BasCmtsUInt16):
    """Custom type basCmtsUsHwMinPwrThr based on BasCmtsUInt16"""
    defaultHexValue = 128


_BasCmtsUsHwMinPwrThr_Object = MibTableColumn
basCmtsUsHwMinPwrThr = _BasCmtsUsHwMinPwrThr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 10),
    _BasCmtsUsHwMinPwrThr_Type()
)
basCmtsUsHwMinPwrThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwMinPwrThr.setStatus("current")


class _BasCmtsUsHwTimeErrThr_Type(BasCmtsUInt16):
    """Custom type basCmtsUsHwTimeErrThr based on BasCmtsUInt16"""
    defaultHexValue = 8


_BasCmtsUsHwTimeErrThr_Object = MibTableColumn
basCmtsUsHwTimeErrThr = _BasCmtsUsHwTimeErrThr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 11),
    _BasCmtsUsHwTimeErrThr_Type()
)
basCmtsUsHwTimeErrThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwTimeErrThr.setStatus("current")


class _BasCmtsUsHwAdcClipCtl_Type(BasCmtsByte):
    """Custom type basCmtsUsHwAdcClipCtl based on BasCmtsByte"""
    defaultHexValue = 8


_BasCmtsUsHwAdcClipCtl_Object = MibTableColumn
basCmtsUsHwAdcClipCtl = _BasCmtsUsHwAdcClipCtl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 12),
    _BasCmtsUsHwAdcClipCtl_Type()
)
basCmtsUsHwAdcClipCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwAdcClipCtl.setStatus("current")


class _BasCmtsUsHwLoopCheck_Type(BasCmtsByte):
    """Custom type basCmtsUsHwLoopCheck based on BasCmtsByte"""
    defaultHexValue = 0


_BasCmtsUsHwLoopCheck_Object = MibTableColumn
basCmtsUsHwLoopCheck = _BasCmtsUsHwLoopCheck_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 13),
    _BasCmtsUsHwLoopCheck_Type()
)
basCmtsUsHwLoopCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwLoopCheck.setStatus("current")


class _BasCmtsUsHwSlcrErrThr_Type(BasCmtsByte):
    """Custom type basCmtsUsHwSlcrErrThr based on BasCmtsByte"""
    defaultHexValue = 8


_BasCmtsUsHwSlcrErrThr_Object = MibTableColumn
basCmtsUsHwSlcrErrThr = _BasCmtsUsHwSlcrErrThr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 14),
    _BasCmtsUsHwSlcrErrThr_Type()
)
basCmtsUsHwSlcrErrThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwSlcrErrThr.setStatus("current")


class _BasCmtsUsHwAfltSelThr_Type(BasCmtsByte):
    """Custom type basCmtsUsHwAfltSelThr based on BasCmtsByte"""
    defaultHexValue = 28


_BasCmtsUsHwAfltSelThr_Object = MibTableColumn
basCmtsUsHwAfltSelThr = _BasCmtsUsHwAfltSelThr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 15),
    _BasCmtsUsHwAfltSelThr_Type()
)
basCmtsUsHwAfltSelThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwAfltSelThr.setStatus("current")


class _BasCmtsUsHwBurstGain_Type(BasCmtsUInt16):
    """Custom type basCmtsUsHwBurstGain based on BasCmtsUInt16"""
    defaultHexValue = 256


_BasCmtsUsHwBurstGain_Object = MibTableColumn
basCmtsUsHwBurstGain = _BasCmtsUsHwBurstGain_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 16),
    _BasCmtsUsHwBurstGain_Type()
)
basCmtsUsHwBurstGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwBurstGain.setStatus("current")


class _BasCmtsUsHwLoopCtl_Type(BasCmtsByte):
    """Custom type basCmtsUsHwLoopCtl based on BasCmtsByte"""
    defaultHexValue = 20


_BasCmtsUsHwLoopCtl_Object = MibTableColumn
basCmtsUsHwLoopCtl = _BasCmtsUsHwLoopCtl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 17),
    _BasCmtsUsHwLoopCtl_Type()
)
basCmtsUsHwLoopCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwLoopCtl.setStatus("current")


class _BasCmtsUsHwEqRsCtl_Type(BasCmtsByte):
    """Custom type basCmtsUsHwEqRsCtl based on BasCmtsByte"""
    defaultHexValue = 16


_BasCmtsUsHwEqRsCtl_Object = MibTableColumn
basCmtsUsHwEqRsCtl = _BasCmtsUsHwEqRsCtl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 18),
    _BasCmtsUsHwEqRsCtl_Type()
)
basCmtsUsHwEqRsCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwEqRsCtl.setStatus("current")


class _BasCmtsUsHwEqSteps_Type(BasCmtsByte):
    """Custom type basCmtsUsHwEqSteps based on BasCmtsByte"""
    defaultHexValue = 33


_BasCmtsUsHwEqSteps_Object = MibTableColumn
basCmtsUsHwEqSteps = _BasCmtsUsHwEqSteps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 6, 1, 19),
    _BasCmtsUsHwEqSteps_Type()
)
basCmtsUsHwEqSteps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsHwEqSteps.setStatus("current")
_BasCmtsUsMapTable_Object = MibTable
basCmtsUsMapTable = _BasCmtsUsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    basCmtsUsMapTable.setStatus("current")
_BasCmtsUsMapEntry_Object = MibTableRow
basCmtsUsMapEntry = _BasCmtsUsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    basCmtsUsMapEntry.setStatus("current")


class _BasCmtsUsMapMaxMapLenHwMapPeriods_Type(BasCmtsUInt16):
    """Custom type basCmtsUsMapMaxMapLenHwMapPeriods based on BasCmtsUInt16"""
    defaultValue = 4


_BasCmtsUsMapMaxMapLenHwMapPeriods_Object = MibTableColumn
basCmtsUsMapMaxMapLenHwMapPeriods = _BasCmtsUsMapMaxMapLenHwMapPeriods_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 7, 1, 1),
    _BasCmtsUsMapMaxMapLenHwMapPeriods_Type()
)
basCmtsUsMapMaxMapLenHwMapPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsMapMaxMapLenHwMapPeriods.setStatus("current")


class _BasCmtsUsMapInitMainRegionSizeMicrosec_Type(BasCmtsUInt16):
    """Custom type basCmtsUsMapInitMainRegionSizeMicrosec based on BasCmtsUInt16"""
    defaultValue = 2000


_BasCmtsUsMapInitMainRegionSizeMicrosec_Object = MibTableColumn
basCmtsUsMapInitMainRegionSizeMicrosec = _BasCmtsUsMapInitMainRegionSizeMicrosec_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 7, 1, 2),
    _BasCmtsUsMapInitMainRegionSizeMicrosec_Type()
)
basCmtsUsMapInitMainRegionSizeMicrosec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsMapInitMainRegionSizeMicrosec.setStatus("current")


class _BasCmtsUsMapNewUcdGrantSizeMicrosec_Type(BasCmtsUInt16):
    """Custom type basCmtsUsMapNewUcdGrantSizeMicrosec based on BasCmtsUInt16"""
    defaultValue = 3000


_BasCmtsUsMapNewUcdGrantSizeMicrosec_Object = MibTableColumn
basCmtsUsMapNewUcdGrantSizeMicrosec = _BasCmtsUsMapNewUcdGrantSizeMicrosec_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 7, 1, 3),
    _BasCmtsUsMapNewUcdGrantSizeMicrosec_Type()
)
basCmtsUsMapNewUcdGrantSizeMicrosec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsMapNewUcdGrantSizeMicrosec.setStatus("current")


class _BasCmtsUsMapMaxDeferredRngIE_Type(BasCmtsUInt16):
    """Custom type basCmtsUsMapMaxDeferredRngIE based on BasCmtsUInt16"""
    defaultValue = 4


_BasCmtsUsMapMaxDeferredRngIE_Object = MibTableColumn
basCmtsUsMapMaxDeferredRngIE = _BasCmtsUsMapMaxDeferredRngIE_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 7, 1, 4),
    _BasCmtsUsMapMaxDeferredRngIE_Type()
)
basCmtsUsMapMaxDeferredRngIE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsMapMaxDeferredRngIE.setStatus("current")


class _BasCmtsUsMapMapLeadTimeMillisec_Type(BasCmtsUInt16):
    """Custom type basCmtsUsMapMapLeadTimeMillisec based on BasCmtsUInt16"""
    defaultValue = 6


_BasCmtsUsMapMapLeadTimeMillisec_Object = MibTableColumn
basCmtsUsMapMapLeadTimeMillisec = _BasCmtsUsMapMapLeadTimeMillisec_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 7, 1, 5),
    _BasCmtsUsMapMapLeadTimeMillisec_Type()
)
basCmtsUsMapMapLeadTimeMillisec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsMapMapLeadTimeMillisec.setStatus("deprecated")


class _BasCmtsUsMapRequestLimitMslot_Type(BasCmtsUInt16):
    """Custom type basCmtsUsMapRequestLimitMslot based on BasCmtsUInt16"""
    defaultValue = 20


_BasCmtsUsMapRequestLimitMslot_Object = MibTableColumn
basCmtsUsMapRequestLimitMslot = _BasCmtsUsMapRequestLimitMslot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 7, 1, 6),
    _BasCmtsUsMapRequestLimitMslot_Type()
)
basCmtsUsMapRequestLimitMslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsMapRequestLimitMslot.setStatus("current")
_BasCmtsUsMapMapLeadTime_Type = BasCmtsUInt16
_BasCmtsUsMapMapLeadTime_Object = MibTableColumn
basCmtsUsMapMapLeadTime = _BasCmtsUsMapMapLeadTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 7, 1, 7),
    _BasCmtsUsMapMapLeadTime_Type()
)
basCmtsUsMapMapLeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsMapMapLeadTime.setStatus("current")
_BasCmtsUsRngTable_Object = MibTable
basCmtsUsRngTable = _BasCmtsUsRngTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    basCmtsUsRngTable.setStatus("current")
_BasCmtsUsRngEntry_Object = MibTableRow
basCmtsUsRngEntry = _BasCmtsUsRngEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    basCmtsUsRngEntry.setStatus("current")


class _BasCmtsUsRngTimingOffsetThr_Type(BasCmtsUInt32):
    """Custom type basCmtsUsRngTimingOffsetThr based on BasCmtsUInt32"""
    defaultValue = 2


_BasCmtsUsRngTimingOffsetThr_Object = MibTableColumn
basCmtsUsRngTimingOffsetThr = _BasCmtsUsRngTimingOffsetThr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 1),
    _BasCmtsUsRngTimingOffsetThr_Type()
)
basCmtsUsRngTimingOffsetThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngTimingOffsetThr.setStatus("current")


class _BasCmtsUsRngFreqOffsetThr_Type(BasCmtsUInt16):
    """Custom type basCmtsUsRngFreqOffsetThr based on BasCmtsUInt16"""
    defaultValue = 3200


_BasCmtsUsRngFreqOffsetThr_Object = MibTableColumn
basCmtsUsRngFreqOffsetThr = _BasCmtsUsRngFreqOffsetThr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 2),
    _BasCmtsUsRngFreqOffsetThr_Type()
)
basCmtsUsRngFreqOffsetThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngFreqOffsetThr.setStatus("current")


class _BasCmtsUsRngPowerOffsetThr_Type(BasCmtsByte):
    """Custom type basCmtsUsRngPowerOffsetThr based on BasCmtsByte"""
    defaultValue = 8


_BasCmtsUsRngPowerOffsetThr_Object = MibTableColumn
basCmtsUsRngPowerOffsetThr = _BasCmtsUsRngPowerOffsetThr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 3),
    _BasCmtsUsRngPowerOffsetThr_Type()
)
basCmtsUsRngPowerOffsetThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngPowerOffsetThr.setStatus("current")


class _BasCmtsUsRngPowerDesired_Type(BasCmtsUInt16):
    """Custom type basCmtsUsRngPowerDesired based on BasCmtsUInt16"""
    defaultValue = 4096


_BasCmtsUsRngPowerDesired_Object = MibTableColumn
basCmtsUsRngPowerDesired = _BasCmtsUsRngPowerDesired_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 4),
    _BasCmtsUsRngPowerDesired_Type()
)
basCmtsUsRngPowerDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngPowerDesired.setStatus("current")


class _BasCmtsUsRngMaxIgnoredInvitations_Type(BasCmtsUInt16):
    """Custom type basCmtsUsRngMaxIgnoredInvitations based on BasCmtsUInt16"""
    defaultValue = 20


_BasCmtsUsRngMaxIgnoredInvitations_Object = MibTableColumn
basCmtsUsRngMaxIgnoredInvitations = _BasCmtsUsRngMaxIgnoredInvitations_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 5),
    _BasCmtsUsRngMaxIgnoredInvitations_Type()
)
basCmtsUsRngMaxIgnoredInvitations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsRngMaxIgnoredInvitations.setStatus("current")


class _BasCmtsUsRngCmRngInviteTimeout_Type(BasCmtsUInt16):
    """Custom type basCmtsUsRngCmRngInviteTimeout based on BasCmtsUInt16"""
    defaultValue = 100


_BasCmtsUsRngCmRngInviteTimeout_Object = MibTableColumn
basCmtsUsRngCmRngInviteTimeout = _BasCmtsUsRngCmRngInviteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 6),
    _BasCmtsUsRngCmRngInviteTimeout_Type()
)
basCmtsUsRngCmRngInviteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngCmRngInviteTimeout.setStatus("current")


class _BasCmtsUsRngMaxPowerAdjQtrdb_Type(BasCmtsByte):
    """Custom type basCmtsUsRngMaxPowerAdjQtrdb based on BasCmtsByte"""
    defaultValue = 8


_BasCmtsUsRngMaxPowerAdjQtrdb_Object = MibTableColumn
basCmtsUsRngMaxPowerAdjQtrdb = _BasCmtsUsRngMaxPowerAdjQtrdb_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 7),
    _BasCmtsUsRngMaxPowerAdjQtrdb_Type()
)
basCmtsUsRngMaxPowerAdjQtrdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngMaxPowerAdjQtrdb.setStatus("current")


class _BasCmtsUsRngZeroPowerAdj_Type(TruthValue):
    """Custom type basCmtsUsRngZeroPowerAdj based on TruthValue"""


_BasCmtsUsRngZeroPowerAdj_Object = MibTableColumn
basCmtsUsRngZeroPowerAdj = _BasCmtsUsRngZeroPowerAdj_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 8),
    _BasCmtsUsRngZeroPowerAdj_Type()
)
basCmtsUsRngZeroPowerAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngZeroPowerAdj.setStatus("current")


class _BasCmtsUsRngZeroTimingAdj_Type(TruthValue):
    """Custom type basCmtsUsRngZeroTimingAdj based on TruthValue"""


_BasCmtsUsRngZeroTimingAdj_Object = MibTableColumn
basCmtsUsRngZeroTimingAdj = _BasCmtsUsRngZeroTimingAdj_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 9),
    _BasCmtsUsRngZeroTimingAdj_Type()
)
basCmtsUsRngZeroTimingAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngZeroTimingAdj.setStatus("current")


class _BasCmtsUsRngZeroFreqAdj_Type(TruthValue):
    """Custom type basCmtsUsRngZeroFreqAdj based on TruthValue"""


_BasCmtsUsRngZeroFreqAdj_Object = MibTableColumn
basCmtsUsRngZeroFreqAdj = _BasCmtsUsRngZeroFreqAdj_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 10),
    _BasCmtsUsRngZeroFreqAdj_Type()
)
basCmtsUsRngZeroFreqAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngZeroFreqAdj.setStatus("current")
_BasCmtsUsRngRefPowerLevel_Type = Unsigned32
_BasCmtsUsRngRefPowerLevel_Object = MibTableColumn
basCmtsUsRngRefPowerLevel = _BasCmtsUsRngRefPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 11),
    _BasCmtsUsRngRefPowerLevel_Type()
)
basCmtsUsRngRefPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngRefPowerLevel.setStatus("current")
_BasCmtsUsRngCmPeriodicRngInviteTimeout_Type = BasCmtsUInt16
_BasCmtsUsRngCmPeriodicRngInviteTimeout_Object = MibTableColumn
basCmtsUsRngCmPeriodicRngInviteTimeout = _BasCmtsUsRngCmPeriodicRngInviteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 8, 1, 12),
    _BasCmtsUsRngCmPeriodicRngInviteTimeout_Type()
)
basCmtsUsRngCmPeriodicRngInviteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsRngCmPeriodicRngInviteTimeout.setStatus("current")
_BasCmtsServiceTable_Object = MibTable
basCmtsServiceTable = _BasCmtsServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    basCmtsServiceTable.setStatus("current")
_BasCmtsServiceEntry_Object = MibTableRow
basCmtsServiceEntry = _BasCmtsServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    basCmtsServiceEntry.setStatus("current")
_BasCmtsServiceMacAddress_Type = MacAddress
_BasCmtsServiceMacAddress_Object = MibTableColumn
basCmtsServiceMacAddress = _BasCmtsServiceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 1),
    _BasCmtsServiceMacAddress_Type()
)
basCmtsServiceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceMacAddress.setStatus("current")
_BasCmtsServiceIpAddress_Type = IpAddress
_BasCmtsServiceIpAddress_Object = MibTableColumn
basCmtsServiceIpAddress = _BasCmtsServiceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 2),
    _BasCmtsServiceIpAddress_Type()
)
basCmtsServiceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceIpAddress.setStatus("current")


class _BasCmtsServiceAuthState_Type(Integer32):
    """Custom type basCmtsServiceAuthState based on Integer32"""
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
        *(("auth", 4),
          ("initial", 1),
          ("max", 5),
          ("permanent", 3),
          ("temporary", 2))
    )


_BasCmtsServiceAuthState_Type.__name__ = "Integer32"
_BasCmtsServiceAuthState_Object = MibTableColumn
basCmtsServiceAuthState = _BasCmtsServiceAuthState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 3),
    _BasCmtsServiceAuthState_Type()
)
basCmtsServiceAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceAuthState.setStatus("current")
_BasCmtsServiceFilter_Type = BasCmtsUInt16
_BasCmtsServiceFilter_Object = MibTableColumn
basCmtsServiceFilter = _BasCmtsServiceFilter_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 4),
    _BasCmtsServiceFilter_Type()
)
basCmtsServiceFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsServiceFilter.setStatus("current")
_BasCmtsServiceCurrentNumHost_Type = BasCmtsUInt32
_BasCmtsServiceCurrentNumHost_Object = MibTableColumn
basCmtsServiceCurrentNumHost = _BasCmtsServiceCurrentNumHost_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 5),
    _BasCmtsServiceCurrentNumHost_Type()
)
basCmtsServiceCurrentNumHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceCurrentNumHost.setStatus("current")
_BasCmtsServiceMaxNumHost_Type = BasCmtsUInt32
_BasCmtsServiceMaxNumHost_Object = MibTableColumn
basCmtsServiceMaxNumHost = _BasCmtsServiceMaxNumHost_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 6),
    _BasCmtsServiceMaxNumHost_Type()
)
basCmtsServiceMaxNumHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceMaxNumHost.setStatus("current")
_BasCmtsServiceOutOctets_Type = BasCmtsUInt32
_BasCmtsServiceOutOctets_Object = MibTableColumn
basCmtsServiceOutOctets = _BasCmtsServiceOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 7),
    _BasCmtsServiceOutOctets_Type()
)
basCmtsServiceOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceOutOctets.setStatus("current")
_BasCmtsServiceOutPackets_Type = BasCmtsUInt32
_BasCmtsServiceOutPackets_Object = MibTableColumn
basCmtsServiceOutPackets = _BasCmtsServiceOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 8),
    _BasCmtsServiceOutPackets_Type()
)
basCmtsServiceOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceOutPackets.setStatus("current")
_BasCmtsServiceInDiscards_Type = BasCmtsUInt32
_BasCmtsServiceInDiscards_Object = MibTableColumn
basCmtsServiceInDiscards = _BasCmtsServiceInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 9),
    _BasCmtsServiceInDiscards_Type()
)
basCmtsServiceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceInDiscards.setStatus("current")
_BasCmtsServiceOutDiscards_Type = BasCmtsUInt32
_BasCmtsServiceOutDiscards_Object = MibTableColumn
basCmtsServiceOutDiscards = _BasCmtsServiceOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 10),
    _BasCmtsServiceOutDiscards_Type()
)
basCmtsServiceOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceOutDiscards.setStatus("current")
_BasCmtsServiceBwReqCount_Type = BasCmtsUInt32
_BasCmtsServiceBwReqCount_Object = MibTableColumn
basCmtsServiceBwReqCount = _BasCmtsServiceBwReqCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 11),
    _BasCmtsServiceBwReqCount_Type()
)
basCmtsServiceBwReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceBwReqCount.setStatus("current")
_BasCmtsServiceDataGrantCount_Type = BasCmtsUInt32
_BasCmtsServiceDataGrantCount_Object = MibTableColumn
basCmtsServiceDataGrantCount = _BasCmtsServiceDataGrantCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 9, 1, 12),
    _BasCmtsServiceDataGrantCount_Type()
)
basCmtsServiceDataGrantCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsServiceDataGrantCount.setStatus("current")
_BasFlapControlTable_Object = MibTable
basFlapControlTable = _BasFlapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    basFlapControlTable.setStatus("current")
_BasFlapControlEntry_Object = MibTableRow
basFlapControlEntry = _BasFlapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 10, 1)
)
basFlapControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    basFlapControlEntry.setStatus("current")
_BasFlapCtlClearFlag_Type = Integer32
_BasFlapCtlClearFlag_Object = MibTableColumn
basFlapCtlClearFlag = _BasFlapCtlClearFlag_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 10, 1, 1),
    _BasFlapCtlClearFlag_Type()
)
basFlapCtlClearFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basFlapCtlClearFlag.setStatus("current")


class _BasFlapCtlMaxTableSize_Type(Integer32):
    """Custom type basFlapCtlMaxTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_BasFlapCtlMaxTableSize_Type.__name__ = "Integer32"
_BasFlapCtlMaxTableSize_Object = MibTableColumn
basFlapCtlMaxTableSize = _BasFlapCtlMaxTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 10, 1, 2),
    _BasFlapCtlMaxTableSize_Type()
)
basFlapCtlMaxTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basFlapCtlMaxTableSize.setStatus("current")


class _BasFlapCtlAgingThresh_Type(Integer32):
    """Custom type basFlapCtlAgingThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_BasFlapCtlAgingThresh_Type.__name__ = "Integer32"
_BasFlapCtlAgingThresh_Object = MibTableColumn
basFlapCtlAgingThresh = _BasFlapCtlAgingThresh_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 10, 1, 3),
    _BasFlapCtlAgingThresh_Type()
)
basFlapCtlAgingThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basFlapCtlAgingThresh.setStatus("current")


class _BasFlapCtlInsTimeThresh_Type(Integer32):
    """Custom type basFlapCtlInsTimeThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_BasFlapCtlInsTimeThresh_Type.__name__ = "Integer32"
_BasFlapCtlInsTimeThresh_Object = MibTableColumn
basFlapCtlInsTimeThresh = _BasFlapCtlInsTimeThresh_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 10, 1, 4),
    _BasFlapCtlInsTimeThresh_Type()
)
basFlapCtlInsTimeThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basFlapCtlInsTimeThresh.setStatus("current")


class _BasFlapCtlPowerAdjThresh_Type(Integer32):
    """Custom type basFlapCtlPowerAdjThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_BasFlapCtlPowerAdjThresh_Type.__name__ = "Integer32"
_BasFlapCtlPowerAdjThresh_Object = MibTableColumn
basFlapCtlPowerAdjThresh = _BasFlapCtlPowerAdjThresh_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 10, 1, 5),
    _BasFlapCtlPowerAdjThresh_Type()
)
basFlapCtlPowerAdjThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basFlapCtlPowerAdjThresh.setStatus("current")
_BasFlapTable_Object = MibTable
basFlapTable = _BasFlapTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    basFlapTable.setStatus("current")
_BasFlapEntry_Object = MibTableRow
basFlapEntry = _BasFlapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1)
)
basFlapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BAS-CMTS-CONFIG-MIB", "basFlapEntryMacAddress"),
)
if mibBuilder.loadTexts:
    basFlapEntry.setStatus("current")
_BasFlapEntryMacAddress_Type = MacAddress
_BasFlapEntryMacAddress_Object = MibTableColumn
basFlapEntryMacAddress = _BasFlapEntryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 1),
    _BasFlapEntryMacAddress_Type()
)
basFlapEntryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryMacAddress.setStatus("current")
_BasFlapEntryUsChan_Type = Counter32
_BasFlapEntryUsChan_Object = MibTableColumn
basFlapEntryUsChan = _BasFlapEntryUsChan_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 2),
    _BasFlapEntryUsChan_Type()
)
basFlapEntryUsChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryUsChan.setStatus("current")
_BasFlapEntryInsertCount_Type = Counter32
_BasFlapEntryInsertCount_Object = MibTableColumn
basFlapEntryInsertCount = _BasFlapEntryInsertCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 3),
    _BasFlapEntryInsertCount_Type()
)
basFlapEntryInsertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryInsertCount.setStatus("current")
_BasFlapEntryHitCount_Type = Counter32
_BasFlapEntryHitCount_Object = MibTableColumn
basFlapEntryHitCount = _BasFlapEntryHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 4),
    _BasFlapEntryHitCount_Type()
)
basFlapEntryHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryHitCount.setStatus("current")
_BasFlapEntryMissCount_Type = Counter32
_BasFlapEntryMissCount_Object = MibTableColumn
basFlapEntryMissCount = _BasFlapEntryMissCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 5),
    _BasFlapEntryMissCount_Type()
)
basFlapEntryMissCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryMissCount.setStatus("current")
_BasFlapEntryCRCErrCount_Type = Counter32
_BasFlapEntryCRCErrCount_Object = MibTableColumn
basFlapEntryCRCErrCount = _BasFlapEntryCRCErrCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 6),
    _BasFlapEntryCRCErrCount_Type()
)
basFlapEntryCRCErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryCRCErrCount.setStatus("current")
_BasFlapEntryPAdjCount_Type = Counter32
_BasFlapEntryPAdjCount_Object = MibTableColumn
basFlapEntryPAdjCount = _BasFlapEntryPAdjCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 7),
    _BasFlapEntryPAdjCount_Type()
)
basFlapEntryPAdjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryPAdjCount.setStatus("current")
_BasFlapEntryFlapCount_Type = Counter32
_BasFlapEntryFlapCount_Object = MibTableColumn
basFlapEntryFlapCount = _BasFlapEntryFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 8),
    _BasFlapEntryFlapCount_Type()
)
basFlapEntryFlapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryFlapCount.setStatus("current")


class _BasFlapEntryLastModemState_Type(Integer32):
    """Custom type basFlapEntryLastModemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 7),
          ("ipComplete", 5),
          ("other", 1),
          ("ranging", 2),
          ("rangingAborted", 3),
          ("rangingComplete", 4),
          ("registrationComplete", 6))
    )


_BasFlapEntryLastModemState_Type.__name__ = "Integer32"
_BasFlapEntryLastModemState_Object = MibTableColumn
basFlapEntryLastModemState = _BasFlapEntryLastModemState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 9),
    _BasFlapEntryLastModemState_Type()
)
basFlapEntryLastModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryLastModemState.setStatus("current")
_BasFlapEntryInsertTime_Type = TimeTicks
_BasFlapEntryInsertTime_Object = MibTableColumn
basFlapEntryInsertTime = _BasFlapEntryInsertTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 10),
    _BasFlapEntryInsertTime_Type()
)
basFlapEntryInsertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryInsertTime.setStatus("current")
_BasFlapEntryRemoveTime_Type = TimeTicks
_BasFlapEntryRemoveTime_Object = MibTableColumn
basFlapEntryRemoveTime = _BasFlapEntryRemoveTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 11),
    _BasFlapEntryRemoveTime_Type()
)
basFlapEntryRemoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryRemoveTime.setStatus("current")


class _BasFlapEntryLastBasModemState_Type(Integer32):
    """Custom type basFlapEntryLastBasModemState based on Integer32"""
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
        *(("basDhcpDiscoverRcvd", 5),
          ("basDhcpRequestRcvd", 6),
          ("basInitRngRcvd", 2),
          ("basKekReject", 16),
          ("basModemOffline", 1),
          ("basRanging", 3),
          ("basRangingComplete", 4),
          ("basRegFailAuthFailure", 15),
          ("basRegFailBadCMTSMic", 13),
          ("basRegFailBadCOS", 14),
          ("basRegisteredBPIKekAssigned", 11),
          ("basRegisteredBPITekAssigned", 12),
          ("basRegisteredNetAccessDisabled", 10),
          ("basRegisteredNetAccessEnabled", 9),
          ("basTekReject", 17),
          ("basTftpReqRcvd", 8),
          ("basTimeReqRcvd", 7))
    )


_BasFlapEntryLastBasModemState_Type.__name__ = "Integer32"
_BasFlapEntryLastBasModemState_Object = MibTableColumn
basFlapEntryLastBasModemState = _BasFlapEntryLastBasModemState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 11, 1, 12),
    _BasFlapEntryLastBasModemState_Type()
)
basFlapEntryLastBasModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFlapEntryLastBasModemState.setStatus("current")
_BasCmtsCmStatusTable_Object = MibTable
basCmtsCmStatusTable = _BasCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 12)
)
if mibBuilder.loadTexts:
    basCmtsCmStatusTable.setStatus("current")
_BasCmtsCmStatusEntry_Object = MibTableRow
basCmtsCmStatusEntry = _BasCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    basCmtsCmStatusEntry.setStatus("current")
_BasCmtsCmStatusAbortFlag_Type = Integer32
_BasCmtsCmStatusAbortFlag_Object = MibTableColumn
basCmtsCmStatusAbortFlag = _BasCmtsCmStatusAbortFlag_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 12, 1, 1),
    _BasCmtsCmStatusAbortFlag_Type()
)
basCmtsCmStatusAbortFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsCmStatusAbortFlag.setStatus("current")
_BasCmtsCmStatusPrimarySid_Type = Integer32
_BasCmtsCmStatusPrimarySid_Object = MibTableColumn
basCmtsCmStatusPrimarySid = _BasCmtsCmStatusPrimarySid_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 12, 1, 2),
    _BasCmtsCmStatusPrimarySid_Type()
)
basCmtsCmStatusPrimarySid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsCmStatusPrimarySid.setStatus("current")


class _BasCmtsCmStatusValue_Type(Integer32):
    """Custom type basCmtsCmStatusValue based on Integer32"""
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
        *(("basDhcpDiscoverRcvd", 5),
          ("basDhcpRequestRcvd", 6),
          ("basInitRngRcvd", 2),
          ("basKekReject", 16),
          ("basModemOffline", 1),
          ("basRanging", 3),
          ("basRangingComplete", 4),
          ("basRegFailAuthFailure", 15),
          ("basRegFailBadCMTSMic", 13),
          ("basRegFailBadCOS", 14),
          ("basRegisteredBPIKekAssigned", 11),
          ("basRegisteredBPITekAssigned", 12),
          ("basRegisteredNetAccessDisabled", 10),
          ("basRegisteredNetAccessEnabled", 9),
          ("basTekReject", 17),
          ("basTftpReqRcvd", 8),
          ("basTimeReqRcvd", 7))
    )


_BasCmtsCmStatusValue_Type.__name__ = "Integer32"
_BasCmtsCmStatusValue_Object = MibTableColumn
basCmtsCmStatusValue = _BasCmtsCmStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 12, 1, 3),
    _BasCmtsCmStatusValue_Type()
)
basCmtsCmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsCmStatusValue.setStatus("current")
_BasCmtsUsStatsTable_Object = MibTable
basCmtsUsStatsTable = _BasCmtsUsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13)
)
if mibBuilder.loadTexts:
    basCmtsUsStatsTable.setStatus("current")
_BasCmtsUsStatsEntry_Object = MibTableRow
basCmtsUsStatsEntry = _BasCmtsUsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    basCmtsUsStatsEntry.setStatus("current")
_BasCmtsUsStatsClearFlag_Type = BasCmtsUInt32
_BasCmtsUsStatsClearFlag_Object = MibTableColumn
basCmtsUsStatsClearFlag = _BasCmtsUsStatsClearFlag_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 1),
    _BasCmtsUsStatsClearFlag_Type()
)
basCmtsUsStatsClearFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsUsStatsClearFlag.setStatus("current")
_BasCmtsUsStatsUSSlots_Type = BasCmtsUInt32
_BasCmtsUsStatsUSSlots_Object = MibTableColumn
basCmtsUsStatsUSSlots = _BasCmtsUsStatsUSSlots_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 2),
    _BasCmtsUsStatsUSSlots_Type()
)
basCmtsUsStatsUSSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsUSSlots.setStatus("current")
_BasCmtsUsStatsNoUW_Type = BasCmtsUInt32
_BasCmtsUsStatsNoUW_Object = MibTableColumn
basCmtsUsStatsNoUW = _BasCmtsUsStatsNoUW_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 3),
    _BasCmtsUsStatsNoUW_Type()
)
basCmtsUsStatsNoUW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsNoUW.setStatus("current")
_BasCmtsUsStatsDataFECorHCSErr_Type = BasCmtsUInt32
_BasCmtsUsStatsDataFECorHCSErr_Object = MibTableColumn
basCmtsUsStatsDataFECorHCSErr = _BasCmtsUsStatsDataFECorHCSErr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 4),
    _BasCmtsUsStatsDataFECorHCSErr_Type()
)
basCmtsUsStatsDataFECorHCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsDataFECorHCSErr.setStatus("current")
_BasCmtsUsStatsRequests_Type = BasCmtsUInt32
_BasCmtsUsStatsRequests_Object = MibTableColumn
basCmtsUsStatsRequests = _BasCmtsUsStatsRequests_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 5),
    _BasCmtsUsStatsRequests_Type()
)
basCmtsUsStatsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsRequests.setStatus("current")
_BasCmtsUsStatsRequestColl_Type = BasCmtsUInt32
_BasCmtsUsStatsRequestColl_Object = MibTableColumn
basCmtsUsStatsRequestColl = _BasCmtsUsStatsRequestColl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 6),
    _BasCmtsUsStatsRequestColl_Type()
)
basCmtsUsStatsRequestColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsRequestColl.setStatus("current")
_BasCmtsUsStatsReqFECorHCSErr_Type = BasCmtsUInt32
_BasCmtsUsStatsReqFECorHCSErr_Object = MibTableColumn
basCmtsUsStatsReqFECorHCSErr = _BasCmtsUsStatsReqFECorHCSErr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 7),
    _BasCmtsUsStatsReqFECorHCSErr_Type()
)
basCmtsUsStatsReqFECorHCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsReqFECorHCSErr.setStatus("current")
_BasCmtsUsStatsReqNoEnergy_Type = BasCmtsUInt32
_BasCmtsUsStatsReqNoEnergy_Object = MibTableColumn
basCmtsUsStatsReqNoEnergy = _BasCmtsUsStatsReqNoEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 8),
    _BasCmtsUsStatsReqNoEnergy_Type()
)
basCmtsUsStatsReqNoEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsReqNoEnergy.setStatus("current")
_BasCmtsUsStatsReqData_Type = BasCmtsUInt32
_BasCmtsUsStatsReqData_Object = MibTableColumn
basCmtsUsStatsReqData = _BasCmtsUsStatsReqData_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 9),
    _BasCmtsUsStatsReqData_Type()
)
basCmtsUsStatsReqData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsReqData.setStatus("current")
_BasCmtsUsStatsReqDataColl_Type = BasCmtsUInt32
_BasCmtsUsStatsReqDataColl_Object = MibTableColumn
basCmtsUsStatsReqDataColl = _BasCmtsUsStatsReqDataColl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 10),
    _BasCmtsUsStatsReqDataColl_Type()
)
basCmtsUsStatsReqDataColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsReqDataColl.setStatus("current")
_BasCmtsUsStatsReqDataFECorHCSErr_Type = BasCmtsUInt32
_BasCmtsUsStatsReqDataFECorHCSErr_Object = MibTableColumn
basCmtsUsStatsReqDataFECorHCSErr = _BasCmtsUsStatsReqDataFECorHCSErr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 11),
    _BasCmtsUsStatsReqDataFECorHCSErr_Type()
)
basCmtsUsStatsReqDataFECorHCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsReqDataFECorHCSErr.setStatus("current")
_BasCmtsUsStatsReqDataNoEnergy_Type = BasCmtsUInt32
_BasCmtsUsStatsReqDataNoEnergy_Object = MibTableColumn
basCmtsUsStatsReqDataNoEnergy = _BasCmtsUsStatsReqDataNoEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 12),
    _BasCmtsUsStatsReqDataNoEnergy_Type()
)
basCmtsUsStatsReqDataNoEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsReqDataNoEnergy.setStatus("current")
_BasCmtsUsStatsRanging_Type = BasCmtsUInt32
_BasCmtsUsStatsRanging_Object = MibTableColumn
basCmtsUsStatsRanging = _BasCmtsUsStatsRanging_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 13),
    _BasCmtsUsStatsRanging_Type()
)
basCmtsUsStatsRanging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsRanging.setStatus("current")
_BasCmtsUsStatsRangeFECorHCSErr_Type = BasCmtsUInt32
_BasCmtsUsStatsRangeFECorHCSErr_Object = MibTableColumn
basCmtsUsStatsRangeFECorHCSErr = _BasCmtsUsStatsRangeFECorHCSErr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 14),
    _BasCmtsUsStatsRangeFECorHCSErr_Type()
)
basCmtsUsStatsRangeFECorHCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsRangeFECorHCSErr.setStatus("current")
_BasCmtsUsStatsMapsTooLate_Type = BasCmtsUInt32
_BasCmtsUsStatsMapsTooLate_Object = MibTableColumn
basCmtsUsStatsMapsTooLate = _BasCmtsUsStatsMapsTooLate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 1, 13, 1, 15),
    _BasCmtsUsStatsMapsTooLate_Type()
)
basCmtsUsStatsMapsTooLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsUsStatsMapsTooLate.setStatus("current")
_BasCmtsDecodeObjects_ObjectIdentity = ObjectIdentity
basCmtsDecodeObjects = _BasCmtsDecodeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2)
)
_BasCmtsPktDecodeControlTable_Object = MibTable
basCmtsPktDecodeControlTable = _BasCmtsPktDecodeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlTable.setStatus("current")
_BasCmtsPktDecodeControlEntry_Object = MibTableRow
basCmtsPktDecodeControlEntry = _BasCmtsPktDecodeControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1)
)
basCmtsPktDecodeControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlEntry.setStatus("current")


class _BasCmtsPktDecodeControlShowRx_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlShowRx based on TruthValue"""


_BasCmtsPktDecodeControlShowRx_Object = MibTableColumn
basCmtsPktDecodeControlShowRx = _BasCmtsPktDecodeControlShowRx_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 1),
    _BasCmtsPktDecodeControlShowRx_Type()
)
basCmtsPktDecodeControlShowRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlShowRx.setStatus("current")


class _BasCmtsPktDecodeControlShowTx_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlShowTx based on TruthValue"""


_BasCmtsPktDecodeControlShowTx_Object = MibTableColumn
basCmtsPktDecodeControlShowTx = _BasCmtsPktDecodeControlShowTx_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 2),
    _BasCmtsPktDecodeControlShowTx_Type()
)
basCmtsPktDecodeControlShowTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlShowTx.setStatus("current")


class _BasCmtsPktDecodeControlAnalyzeLevel_Type(Integer32):
    """Custom type basCmtsPktDecodeControlAnalyzeLevel based on Integer32"""
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
        *(("highLevel", 3),
          ("levelFour", 4),
          ("lowLevel", 1),
          ("mediumLevel", 2))
    )


_BasCmtsPktDecodeControlAnalyzeLevel_Type.__name__ = "Integer32"
_BasCmtsPktDecodeControlAnalyzeLevel_Object = MibTableColumn
basCmtsPktDecodeControlAnalyzeLevel = _BasCmtsPktDecodeControlAnalyzeLevel_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 3),
    _BasCmtsPktDecodeControlAnalyzeLevel_Type()
)
basCmtsPktDecodeControlAnalyzeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlAnalyzeLevel.setStatus("current")


class _BasCmtsPktDecodeControlFilterUcd_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterUcd based on TruthValue"""


_BasCmtsPktDecodeControlFilterUcd_Object = MibTableColumn
basCmtsPktDecodeControlFilterUcd = _BasCmtsPktDecodeControlFilterUcd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 4),
    _BasCmtsPktDecodeControlFilterUcd_Type()
)
basCmtsPktDecodeControlFilterUcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterUcd.setStatus("current")


class _BasCmtsPktDecodeControlFilterMap_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterMap based on TruthValue"""


_BasCmtsPktDecodeControlFilterMap_Object = MibTableColumn
basCmtsPktDecodeControlFilterMap = _BasCmtsPktDecodeControlFilterMap_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 5),
    _BasCmtsPktDecodeControlFilterMap_Type()
)
basCmtsPktDecodeControlFilterMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterMap.setStatus("current")


class _BasCmtsPktDecodeControlFilterRngReq_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterRngReq based on TruthValue"""


_BasCmtsPktDecodeControlFilterRngReq_Object = MibTableColumn
basCmtsPktDecodeControlFilterRngReq = _BasCmtsPktDecodeControlFilterRngReq_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 6),
    _BasCmtsPktDecodeControlFilterRngReq_Type()
)
basCmtsPktDecodeControlFilterRngReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterRngReq.setStatus("current")


class _BasCmtsPktDecodeControlFilterRngRsp_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterRngRsp based on TruthValue"""


_BasCmtsPktDecodeControlFilterRngRsp_Object = MibTableColumn
basCmtsPktDecodeControlFilterRngRsp = _BasCmtsPktDecodeControlFilterRngRsp_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 7),
    _BasCmtsPktDecodeControlFilterRngRsp_Type()
)
basCmtsPktDecodeControlFilterRngRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterRngRsp.setStatus("current")


class _BasCmtsPktDecodeControlFilterRegReq_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterRegReq based on TruthValue"""


_BasCmtsPktDecodeControlFilterRegReq_Object = MibTableColumn
basCmtsPktDecodeControlFilterRegReq = _BasCmtsPktDecodeControlFilterRegReq_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 8),
    _BasCmtsPktDecodeControlFilterRegReq_Type()
)
basCmtsPktDecodeControlFilterRegReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterRegReq.setStatus("current")


class _BasCmtsPktDecodeControlFilterRegRsp_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterRegRsp based on TruthValue"""


_BasCmtsPktDecodeControlFilterRegRsp_Object = MibTableColumn
basCmtsPktDecodeControlFilterRegRsp = _BasCmtsPktDecodeControlFilterRegRsp_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 9),
    _BasCmtsPktDecodeControlFilterRegRsp_Type()
)
basCmtsPktDecodeControlFilterRegRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterRegRsp.setStatus("current")


class _BasCmtsPktDecodeControlFilterUccReq_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterUccReq based on TruthValue"""


_BasCmtsPktDecodeControlFilterUccReq_Object = MibTableColumn
basCmtsPktDecodeControlFilterUccReq = _BasCmtsPktDecodeControlFilterUccReq_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 10),
    _BasCmtsPktDecodeControlFilterUccReq_Type()
)
basCmtsPktDecodeControlFilterUccReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterUccReq.setStatus("current")


class _BasCmtsPktDecodeControlFilterUccRsp_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterUccRsp based on TruthValue"""


_BasCmtsPktDecodeControlFilterUccRsp_Object = MibTableColumn
basCmtsPktDecodeControlFilterUccRsp = _BasCmtsPktDecodeControlFilterUccRsp_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 11),
    _BasCmtsPktDecodeControlFilterUccRsp_Type()
)
basCmtsPktDecodeControlFilterUccRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterUccRsp.setStatus("current")


class _BasCmtsPktDecodeControlFilterBpkmReq_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterBpkmReq based on TruthValue"""


_BasCmtsPktDecodeControlFilterBpkmReq_Object = MibTableColumn
basCmtsPktDecodeControlFilterBpkmReq = _BasCmtsPktDecodeControlFilterBpkmReq_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 12),
    _BasCmtsPktDecodeControlFilterBpkmReq_Type()
)
basCmtsPktDecodeControlFilterBpkmReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterBpkmReq.setStatus("current")


class _BasCmtsPktDecodeControlFilterBpkmRsp_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterBpkmRsp based on TruthValue"""


_BasCmtsPktDecodeControlFilterBpkmRsp_Object = MibTableColumn
basCmtsPktDecodeControlFilterBpkmRsp = _BasCmtsPktDecodeControlFilterBpkmRsp_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 13),
    _BasCmtsPktDecodeControlFilterBpkmRsp_Type()
)
basCmtsPktDecodeControlFilterBpkmRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterBpkmRsp.setStatus("current")


class _BasCmtsPktDecodeControlFilterPdu_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterPdu based on TruthValue"""


_BasCmtsPktDecodeControlFilterPdu_Object = MibTableColumn
basCmtsPktDecodeControlFilterPdu = _BasCmtsPktDecodeControlFilterPdu_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 14),
    _BasCmtsPktDecodeControlFilterPdu_Type()
)
basCmtsPktDecodeControlFilterPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterPdu.setStatus("current")


class _BasCmtsPktDecodeControlFilterBwReq_Type(TruthValue):
    """Custom type basCmtsPktDecodeControlFilterBwReq based on TruthValue"""


_BasCmtsPktDecodeControlFilterBwReq_Object = MibTableColumn
basCmtsPktDecodeControlFilterBwReq = _BasCmtsPktDecodeControlFilterBwReq_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 1, 1, 15),
    _BasCmtsPktDecodeControlFilterBwReq_Type()
)
basCmtsPktDecodeControlFilterBwReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPktDecodeControlFilterBwReq.setStatus("current")
_BasCmtsMapDecodeControlTable_Object = MibTable
basCmtsMapDecodeControlTable = _BasCmtsMapDecodeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    basCmtsMapDecodeControlTable.setStatus("current")
_BasCmtsMapDecodeControlEntry_Object = MibTableRow
basCmtsMapDecodeControlEntry = _BasCmtsMapDecodeControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 2, 1)
)
basCmtsMapDecodeControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    basCmtsMapDecodeControlEntry.setStatus("current")


class _BasCmtsMapDecodeControlTriggerMapPktCount_Type(Integer32):
    """Custom type basCmtsMapDecodeControlTriggerMapPktCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasCmtsMapDecodeControlTriggerMapPktCount_Type.__name__ = "Integer32"
_BasCmtsMapDecodeControlTriggerMapPktCount_Object = MibTableColumn
basCmtsMapDecodeControlTriggerMapPktCount = _BasCmtsMapDecodeControlTriggerMapPktCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 2, 1, 1),
    _BasCmtsMapDecodeControlTriggerMapPktCount_Type()
)
basCmtsMapDecodeControlTriggerMapPktCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMapDecodeControlTriggerMapPktCount.setStatus("current")


class _BasCmtsMapDecodeControlTriggerDataGrant_Type(Integer32):
    """Custom type basCmtsMapDecodeControlTriggerDataGrant based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("triggerOff", 2),
          ("triggerOn", 1))
    )


_BasCmtsMapDecodeControlTriggerDataGrant_Type.__name__ = "Integer32"
_BasCmtsMapDecodeControlTriggerDataGrant_Object = MibTableColumn
basCmtsMapDecodeControlTriggerDataGrant = _BasCmtsMapDecodeControlTriggerDataGrant_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 2, 1, 2),
    _BasCmtsMapDecodeControlTriggerDataGrant_Type()
)
basCmtsMapDecodeControlTriggerDataGrant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMapDecodeControlTriggerDataGrant.setStatus("current")


class _BasCmtsMapDecodeControlTriggerUcdChange_Type(Integer32):
    """Custom type basCmtsMapDecodeControlTriggerUcdChange based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("triggerOff", 2),
          ("triggerOn", 1))
    )


_BasCmtsMapDecodeControlTriggerUcdChange_Type.__name__ = "Integer32"
_BasCmtsMapDecodeControlTriggerUcdChange_Object = MibTableColumn
basCmtsMapDecodeControlTriggerUcdChange = _BasCmtsMapDecodeControlTriggerUcdChange_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 2, 1, 3),
    _BasCmtsMapDecodeControlTriggerUcdChange_Type()
)
basCmtsMapDecodeControlTriggerUcdChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMapDecodeControlTriggerUcdChange.setStatus("current")


class _BasCmtsMapDecodeControlTriggerShortGrant_Type(Integer32):
    """Custom type basCmtsMapDecodeControlTriggerShortGrant based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("triggerOff", 2),
          ("triggerOn", 1))
    )


_BasCmtsMapDecodeControlTriggerShortGrant_Type.__name__ = "Integer32"
_BasCmtsMapDecodeControlTriggerShortGrant_Object = MibTableColumn
basCmtsMapDecodeControlTriggerShortGrant = _BasCmtsMapDecodeControlTriggerShortGrant_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 2, 1, 4),
    _BasCmtsMapDecodeControlTriggerShortGrant_Type()
)
basCmtsMapDecodeControlTriggerShortGrant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMapDecodeControlTriggerShortGrant.setStatus("current")


class _BasCmtsMapDecodeControlTriggerLongGrant_Type(Integer32):
    """Custom type basCmtsMapDecodeControlTriggerLongGrant based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("triggerOff", 2),
          ("triggerOn", 1))
    )


_BasCmtsMapDecodeControlTriggerLongGrant_Type.__name__ = "Integer32"
_BasCmtsMapDecodeControlTriggerLongGrant_Object = MibTableColumn
basCmtsMapDecodeControlTriggerLongGrant = _BasCmtsMapDecodeControlTriggerLongGrant_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 2, 1, 5),
    _BasCmtsMapDecodeControlTriggerLongGrant_Type()
)
basCmtsMapDecodeControlTriggerLongGrant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMapDecodeControlTriggerLongGrant.setStatus("current")


class _BasCmtsMapDecodeControlTriggerInitMaint_Type(Integer32):
    """Custom type basCmtsMapDecodeControlTriggerInitMaint based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("triggerOff", 2),
          ("triggerOn", 1))
    )


_BasCmtsMapDecodeControlTriggerInitMaint_Type.__name__ = "Integer32"
_BasCmtsMapDecodeControlTriggerInitMaint_Object = MibTableColumn
basCmtsMapDecodeControlTriggerInitMaint = _BasCmtsMapDecodeControlTriggerInitMaint_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 2, 1, 6),
    _BasCmtsMapDecodeControlTriggerInitMaint_Type()
)
basCmtsMapDecodeControlTriggerInitMaint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMapDecodeControlTriggerInitMaint.setStatus("current")


class _BasCmtsMapDecodeControlTriggerStationMaint_Type(Integer32):
    """Custom type basCmtsMapDecodeControlTriggerStationMaint based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("triggerOff", 2),
          ("triggerOn", 1))
    )


_BasCmtsMapDecodeControlTriggerStationMaint_Type.__name__ = "Integer32"
_BasCmtsMapDecodeControlTriggerStationMaint_Object = MibTableColumn
basCmtsMapDecodeControlTriggerStationMaint = _BasCmtsMapDecodeControlTriggerStationMaint_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 2, 1, 7),
    _BasCmtsMapDecodeControlTriggerStationMaint_Type()
)
basCmtsMapDecodeControlTriggerStationMaint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMapDecodeControlTriggerStationMaint.setStatus("current")


class _BasCmtsMapDecodeControlTriggerRequestIe_Type(Integer32):
    """Custom type basCmtsMapDecodeControlTriggerRequestIe based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("triggerOff", 2),
          ("triggerOn", 1))
    )


_BasCmtsMapDecodeControlTriggerRequestIe_Type.__name__ = "Integer32"
_BasCmtsMapDecodeControlTriggerRequestIe_Object = MibTableColumn
basCmtsMapDecodeControlTriggerRequestIe = _BasCmtsMapDecodeControlTriggerRequestIe_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 2, 2, 1, 8),
    _BasCmtsMapDecodeControlTriggerRequestIe_Type()
)
basCmtsMapDecodeControlTriggerRequestIe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMapDecodeControlTriggerRequestIe.setStatus("current")
_BasCmtsMacToSidObjects_ObjectIdentity = ObjectIdentity
basCmtsMacToSidObjects = _BasCmtsMacToSidObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 3)
)
_BasCmtsMacToSidTable_Object = MibTable
basCmtsMacToSidTable = _BasCmtsMacToSidTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    basCmtsMacToSidTable.setStatus("current")
_BasCmtsMacToSidEntry_Object = MibTableRow
basCmtsMacToSidEntry = _BasCmtsMacToSidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 3, 1, 1)
)
basCmtsMacToSidEntry.setIndexNames(
    (0, "BAS-CMTS-CONFIG-MIB", "basCmtsMacToSidMacAddr"),
)
if mibBuilder.loadTexts:
    basCmtsMacToSidEntry.setStatus("current")
_BasCmtsMacToSidMacAddr_Type = MacAddress
_BasCmtsMacToSidMacAddr_Object = MibTableColumn
basCmtsMacToSidMacAddr = _BasCmtsMacToSidMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 3, 1, 1, 1),
    _BasCmtsMacToSidMacAddr_Type()
)
basCmtsMacToSidMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsMacToSidMacAddr.setStatus("current")
_BasCmtsMacToSidServiceId_Type = Integer32
_BasCmtsMacToSidServiceId_Object = MibTableColumn
basCmtsMacToSidServiceId = _BasCmtsMacToSidServiceId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 3, 1, 1, 2),
    _BasCmtsMacToSidServiceId_Type()
)
basCmtsMacToSidServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsMacToSidServiceId.setStatus("current")


class _BasCmtsMacToSidType_Type(Integer32):
    """Custom type basCmtsMacToSidType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cableModem", 2),
          ("host", 3),
          ("none", 1))
    )


_BasCmtsMacToSidType_Type.__name__ = "Integer32"
_BasCmtsMacToSidType_Object = MibTableColumn
basCmtsMacToSidType = _BasCmtsMacToSidType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4, 1, 3, 1, 1, 3),
    _BasCmtsMacToSidType_Type()
)
basCmtsMacToSidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsMacToSidType.setStatus("current")
basCmtsMacEntry.registerAugmentions(
    ("BAS-CMTS-CONFIG-MIB",
     "basCmtsMacDsHwEntry")
)
basCmtsMacDsHwEntry.setIndexNames(*basCmtsMacEntry.getIndexNames())
docsIfUpstreamChannelEntry.registerAugmentions(
    ("BAS-CMTS-CONFIG-MIB",
     "basCmtsUpstreamChannelEntry")
)
basCmtsUpstreamChannelEntry.setIndexNames(*docsIfUpstreamChannelEntry.getIndexNames())
docsIfCmtsModulationEntry.registerAugmentions(
    ("BAS-CMTS-CONFIG-MIB",
     "basCmtsModulationEntry")
)
basCmtsModulationEntry.setIndexNames(*docsIfCmtsModulationEntry.getIndexNames())
basCmtsUpstreamChannelEntry.registerAugmentions(
    ("BAS-CMTS-CONFIG-MIB",
     "basCmtsUsHwEntry")
)
basCmtsUsHwEntry.setIndexNames(*basCmtsUpstreamChannelEntry.getIndexNames())
basCmtsUpstreamChannelEntry.registerAugmentions(
    ("BAS-CMTS-CONFIG-MIB",
     "basCmtsUsMapEntry")
)
basCmtsUsMapEntry.setIndexNames(*basCmtsUpstreamChannelEntry.getIndexNames())
basCmtsUpstreamChannelEntry.registerAugmentions(
    ("BAS-CMTS-CONFIG-MIB",
     "basCmtsUsRngEntry")
)
basCmtsUsRngEntry.setIndexNames(*basCmtsUpstreamChannelEntry.getIndexNames())
docsIfCmtsServiceEntry.registerAugmentions(
    ("BAS-CMTS-CONFIG-MIB",
     "basCmtsServiceEntry")
)
basCmtsServiceEntry.setIndexNames(*docsIfCmtsServiceEntry.getIndexNames())
basDocsIfCmtsCmStatusEntry.registerAugmentions(
    ("BAS-CMTS-CONFIG-MIB",
     "basCmtsCmStatusEntry")
)
basCmtsCmStatusEntry.setIndexNames(*basDocsIfCmtsCmStatusEntry.getIndexNames())
basCmtsUpstreamChannelEntry.registerAugmentions(
    ("BAS-CMTS-CONFIG-MIB",
     "basCmtsUsStatsEntry")
)
basCmtsUsStatsEntry.setIndexNames(*basCmtsUpstreamChannelEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-CMTS-CONFIG-MIB",
    **{"BasCmtsInt8": BasCmtsInt8,
       "BasCmtsUInt8": BasCmtsUInt8,
       "BasCmtsByte": BasCmtsByte,
       "BasCmtsInt16": BasCmtsInt16,
       "BasCmtsUInt16": BasCmtsUInt16,
       "BasCmtsInt32": BasCmtsInt32,
       "BasCmtsUInt32": BasCmtsUInt32,
       "BasCmtsRowAction": BasCmtsRowAction,
       "TenthdBmV": TenthdBmV,
       "BasCmtsHeadEndMapMode": BasCmtsHeadEndMapMode,
       "BasCmtsHeadEndMacAddr": BasCmtsHeadEndMacAddr,
       "BasCmtsHeadEndAuthString": BasCmtsHeadEndAuthString,
       "BasCmtsUpChannelPreamblePattern": BasCmtsUpChannelPreamblePattern,
       "BasCmtsModulationWsPattern": BasCmtsModulationWsPattern,
       "basCmtsConfigMib": basCmtsConfigMib,
       "basCmtsConfigObjects": basCmtsConfigObjects,
       "basCmtsHeadEndTable": basCmtsHeadEndTable,
       "basCmtsHeadEndEntry": basCmtsHeadEndEntry,
       "basCmtsHeDsChanId": basCmtsHeDsChanId,
       "basCmtsHeHwMapTimerPeriodMicrosec": basCmtsHeHwMapTimerPeriodMicrosec,
       "basCmtsHeImMapTimerPeriodMillisec": basCmtsHeImMapTimerPeriodMillisec,
       "basCmtsHePerRngTimerPeriodSec": basCmtsHePerRngTimerPeriodSec,
       "basCmtsHeUcdTimerPerMillisec": basCmtsHeUcdTimerPerMillisec,
       "basCmtsHeMapMode": basCmtsHeMapMode,
       "basCmtsHeMacAddr": basCmtsHeMacAddr,
       "basCmtsHeLenAuthString": basCmtsHeLenAuthString,
       "basCmtsHeAuthString": basCmtsHeAuthString,
       "basCmtsHeRowAction": basCmtsHeRowAction,
       "basCmtsHePlantPropDelay": basCmtsHePlantPropDelay,
       "basCmtsHeSupplMapLeadDelay": basCmtsHeSupplMapLeadDelay,
       "basCmtsMacTable": basCmtsMacTable,
       "basCmtsMacEntry": basCmtsMacEntry,
       "basCmtsMacNumUsBds": basCmtsMacNumUsBds,
       "basCmtsMacNumDsMsgBds": basCmtsMacNumDsMsgBds,
       "basCmtsMacNumDsDataBds": basCmtsMacNumDsDataBds,
       "basCmtsMacNumIpBuffers": basCmtsMacNumIpBuffers,
       "basCmtsMacPciDmaSize": basCmtsMacPciDmaSize,
       "basCmtsMacUpdateFirstParticleLast": basCmtsMacUpdateFirstParticleLast,
       "basCmtsMacDirectModeDma": basCmtsMacDirectModeDma,
       "basCmtsMacPackedPart": basCmtsMacPackedPart,
       "basCmtsMacPackedPartOffset": basCmtsMacPackedPartOffset,
       "basCmtsMacSpiClkDivider": basCmtsMacSpiClkDivider,
       "basCmtsMacSyncRate": basCmtsMacSyncRate,
       "basCmtsMacRowAction": basCmtsMacRowAction,
       "basCmtsMacDsHwTable": basCmtsMacDsHwTable,
       "basCmtsMacDsHwEntry": basCmtsMacDsHwEntry,
       "basCmtsMacDsHwInterleaverDepth": basCmtsMacDsHwInterleaverDepth,
       "basCmtsMacDsHwQamctl": basCmtsMacDsHwQamctl,
       "basCmtsMacDsHwSymbolRate": basCmtsMacDsHwSymbolRate,
       "basCmtsMacDsHwIfFreq": basCmtsMacDsHwIfFreq,
       "basCmtsMacDsHwRefFreq": basCmtsMacDsHwRefFreq,
       "basCmtsMacDsHwOscMultFactor": basCmtsMacDsHwOscMultFactor,
       "basCmtsUpstreamChannelTable": basCmtsUpstreamChannelTable,
       "basCmtsUpstreamChannelEntry": basCmtsUpstreamChannelEntry,
       "basCmtsUpChannelMslotPerTick": basCmtsUpChannelMslotPerTick,
       "basCmtsUpChannelSymbolRate160KSymPerSec": basCmtsUpChannelSymbolRate160KSymPerSec,
       "basCmtsUpChannelLenPreamblePattern": basCmtsUpChannelLenPreamblePattern,
       "basCmtsUpChannelPreamblePattern": basCmtsUpChannelPreamblePattern,
       "basCmtsUpChannelRowAction": basCmtsUpChannelRowAction,
       "basCmtsUpChannelReceivePower": basCmtsUpChannelReceivePower,
       "basCmtsModulationTable": basCmtsModulationTable,
       "basCmtsModulationEntry": basCmtsModulationEntry,
       "basCmtsModUwLenBytes": basCmtsModUwLenBytes,
       "basCmtsModUwPattern": basCmtsModUwPattern,
       "basCmtsModUwDetectionWindow": basCmtsModUwDetectionWindow,
       "basCmtsModUwMismatchThresholdBits": basCmtsModUwMismatchThresholdBits,
       "basCmtsModPreambleValueOffset": basCmtsModPreambleValueOffset,
       "basCmtsUsHwTable": basCmtsUsHwTable,
       "basCmtsUsHwEntry": basCmtsUsHwEntry,
       "basCmtsUsHwTestProbe": basCmtsUsHwTestProbe,
       "basCmtsUsHwGenCfg1": basCmtsUsHwGenCfg1,
       "basCmtsUsHwGenCfg2": basCmtsUsHwGenCfg2,
       "basCmtsUsHwPreambleCtl": basCmtsUsHwPreambleCtl,
       "basCmtsUsHwCarrAcf": basCmtsUsHwCarrAcf,
       "basCmtsUsHwCarrTcf": basCmtsUsHwCarrTcf,
       "basCmtsUsHwBaudAtcf": basCmtsUsHwBaudAtcf,
       "basCmtsUsHwBaudIntcf": basCmtsUsHwBaudIntcf,
       "basCmtsUsHwMaxPwrThr": basCmtsUsHwMaxPwrThr,
       "basCmtsUsHwMinPwrThr": basCmtsUsHwMinPwrThr,
       "basCmtsUsHwTimeErrThr": basCmtsUsHwTimeErrThr,
       "basCmtsUsHwAdcClipCtl": basCmtsUsHwAdcClipCtl,
       "basCmtsUsHwLoopCheck": basCmtsUsHwLoopCheck,
       "basCmtsUsHwSlcrErrThr": basCmtsUsHwSlcrErrThr,
       "basCmtsUsHwAfltSelThr": basCmtsUsHwAfltSelThr,
       "basCmtsUsHwBurstGain": basCmtsUsHwBurstGain,
       "basCmtsUsHwLoopCtl": basCmtsUsHwLoopCtl,
       "basCmtsUsHwEqRsCtl": basCmtsUsHwEqRsCtl,
       "basCmtsUsHwEqSteps": basCmtsUsHwEqSteps,
       "basCmtsUsMapTable": basCmtsUsMapTable,
       "basCmtsUsMapEntry": basCmtsUsMapEntry,
       "basCmtsUsMapMaxMapLenHwMapPeriods": basCmtsUsMapMaxMapLenHwMapPeriods,
       "basCmtsUsMapInitMainRegionSizeMicrosec": basCmtsUsMapInitMainRegionSizeMicrosec,
       "basCmtsUsMapNewUcdGrantSizeMicrosec": basCmtsUsMapNewUcdGrantSizeMicrosec,
       "basCmtsUsMapMaxDeferredRngIE": basCmtsUsMapMaxDeferredRngIE,
       "basCmtsUsMapMapLeadTimeMillisec": basCmtsUsMapMapLeadTimeMillisec,
       "basCmtsUsMapRequestLimitMslot": basCmtsUsMapRequestLimitMslot,
       "basCmtsUsMapMapLeadTime": basCmtsUsMapMapLeadTime,
       "basCmtsUsRngTable": basCmtsUsRngTable,
       "basCmtsUsRngEntry": basCmtsUsRngEntry,
       "basCmtsUsRngTimingOffsetThr": basCmtsUsRngTimingOffsetThr,
       "basCmtsUsRngFreqOffsetThr": basCmtsUsRngFreqOffsetThr,
       "basCmtsUsRngPowerOffsetThr": basCmtsUsRngPowerOffsetThr,
       "basCmtsUsRngPowerDesired": basCmtsUsRngPowerDesired,
       "basCmtsUsRngMaxIgnoredInvitations": basCmtsUsRngMaxIgnoredInvitations,
       "basCmtsUsRngCmRngInviteTimeout": basCmtsUsRngCmRngInviteTimeout,
       "basCmtsUsRngMaxPowerAdjQtrdb": basCmtsUsRngMaxPowerAdjQtrdb,
       "basCmtsUsRngZeroPowerAdj": basCmtsUsRngZeroPowerAdj,
       "basCmtsUsRngZeroTimingAdj": basCmtsUsRngZeroTimingAdj,
       "basCmtsUsRngZeroFreqAdj": basCmtsUsRngZeroFreqAdj,
       "basCmtsUsRngRefPowerLevel": basCmtsUsRngRefPowerLevel,
       "basCmtsUsRngCmPeriodicRngInviteTimeout": basCmtsUsRngCmPeriodicRngInviteTimeout,
       "basCmtsServiceTable": basCmtsServiceTable,
       "basCmtsServiceEntry": basCmtsServiceEntry,
       "basCmtsServiceMacAddress": basCmtsServiceMacAddress,
       "basCmtsServiceIpAddress": basCmtsServiceIpAddress,
       "basCmtsServiceAuthState": basCmtsServiceAuthState,
       "basCmtsServiceFilter": basCmtsServiceFilter,
       "basCmtsServiceCurrentNumHost": basCmtsServiceCurrentNumHost,
       "basCmtsServiceMaxNumHost": basCmtsServiceMaxNumHost,
       "basCmtsServiceOutOctets": basCmtsServiceOutOctets,
       "basCmtsServiceOutPackets": basCmtsServiceOutPackets,
       "basCmtsServiceInDiscards": basCmtsServiceInDiscards,
       "basCmtsServiceOutDiscards": basCmtsServiceOutDiscards,
       "basCmtsServiceBwReqCount": basCmtsServiceBwReqCount,
       "basCmtsServiceDataGrantCount": basCmtsServiceDataGrantCount,
       "basFlapControlTable": basFlapControlTable,
       "basFlapControlEntry": basFlapControlEntry,
       "basFlapCtlClearFlag": basFlapCtlClearFlag,
       "basFlapCtlMaxTableSize": basFlapCtlMaxTableSize,
       "basFlapCtlAgingThresh": basFlapCtlAgingThresh,
       "basFlapCtlInsTimeThresh": basFlapCtlInsTimeThresh,
       "basFlapCtlPowerAdjThresh": basFlapCtlPowerAdjThresh,
       "basFlapTable": basFlapTable,
       "basFlapEntry": basFlapEntry,
       "basFlapEntryMacAddress": basFlapEntryMacAddress,
       "basFlapEntryUsChan": basFlapEntryUsChan,
       "basFlapEntryInsertCount": basFlapEntryInsertCount,
       "basFlapEntryHitCount": basFlapEntryHitCount,
       "basFlapEntryMissCount": basFlapEntryMissCount,
       "basFlapEntryCRCErrCount": basFlapEntryCRCErrCount,
       "basFlapEntryPAdjCount": basFlapEntryPAdjCount,
       "basFlapEntryFlapCount": basFlapEntryFlapCount,
       "basFlapEntryLastModemState": basFlapEntryLastModemState,
       "basFlapEntryInsertTime": basFlapEntryInsertTime,
       "basFlapEntryRemoveTime": basFlapEntryRemoveTime,
       "basFlapEntryLastBasModemState": basFlapEntryLastBasModemState,
       "basCmtsCmStatusTable": basCmtsCmStatusTable,
       "basCmtsCmStatusEntry": basCmtsCmStatusEntry,
       "basCmtsCmStatusAbortFlag": basCmtsCmStatusAbortFlag,
       "basCmtsCmStatusPrimarySid": basCmtsCmStatusPrimarySid,
       "basCmtsCmStatusValue": basCmtsCmStatusValue,
       "basCmtsUsStatsTable": basCmtsUsStatsTable,
       "basCmtsUsStatsEntry": basCmtsUsStatsEntry,
       "basCmtsUsStatsClearFlag": basCmtsUsStatsClearFlag,
       "basCmtsUsStatsUSSlots": basCmtsUsStatsUSSlots,
       "basCmtsUsStatsNoUW": basCmtsUsStatsNoUW,
       "basCmtsUsStatsDataFECorHCSErr": basCmtsUsStatsDataFECorHCSErr,
       "basCmtsUsStatsRequests": basCmtsUsStatsRequests,
       "basCmtsUsStatsRequestColl": basCmtsUsStatsRequestColl,
       "basCmtsUsStatsReqFECorHCSErr": basCmtsUsStatsReqFECorHCSErr,
       "basCmtsUsStatsReqNoEnergy": basCmtsUsStatsReqNoEnergy,
       "basCmtsUsStatsReqData": basCmtsUsStatsReqData,
       "basCmtsUsStatsReqDataColl": basCmtsUsStatsReqDataColl,
       "basCmtsUsStatsReqDataFECorHCSErr": basCmtsUsStatsReqDataFECorHCSErr,
       "basCmtsUsStatsReqDataNoEnergy": basCmtsUsStatsReqDataNoEnergy,
       "basCmtsUsStatsRanging": basCmtsUsStatsRanging,
       "basCmtsUsStatsRangeFECorHCSErr": basCmtsUsStatsRangeFECorHCSErr,
       "basCmtsUsStatsMapsTooLate": basCmtsUsStatsMapsTooLate,
       "basCmtsDecodeObjects": basCmtsDecodeObjects,
       "basCmtsPktDecodeControlTable": basCmtsPktDecodeControlTable,
       "basCmtsPktDecodeControlEntry": basCmtsPktDecodeControlEntry,
       "basCmtsPktDecodeControlShowRx": basCmtsPktDecodeControlShowRx,
       "basCmtsPktDecodeControlShowTx": basCmtsPktDecodeControlShowTx,
       "basCmtsPktDecodeControlAnalyzeLevel": basCmtsPktDecodeControlAnalyzeLevel,
       "basCmtsPktDecodeControlFilterUcd": basCmtsPktDecodeControlFilterUcd,
       "basCmtsPktDecodeControlFilterMap": basCmtsPktDecodeControlFilterMap,
       "basCmtsPktDecodeControlFilterRngReq": basCmtsPktDecodeControlFilterRngReq,
       "basCmtsPktDecodeControlFilterRngRsp": basCmtsPktDecodeControlFilterRngRsp,
       "basCmtsPktDecodeControlFilterRegReq": basCmtsPktDecodeControlFilterRegReq,
       "basCmtsPktDecodeControlFilterRegRsp": basCmtsPktDecodeControlFilterRegRsp,
       "basCmtsPktDecodeControlFilterUccReq": basCmtsPktDecodeControlFilterUccReq,
       "basCmtsPktDecodeControlFilterUccRsp": basCmtsPktDecodeControlFilterUccRsp,
       "basCmtsPktDecodeControlFilterBpkmReq": basCmtsPktDecodeControlFilterBpkmReq,
       "basCmtsPktDecodeControlFilterBpkmRsp": basCmtsPktDecodeControlFilterBpkmRsp,
       "basCmtsPktDecodeControlFilterPdu": basCmtsPktDecodeControlFilterPdu,
       "basCmtsPktDecodeControlFilterBwReq": basCmtsPktDecodeControlFilterBwReq,
       "basCmtsMapDecodeControlTable": basCmtsMapDecodeControlTable,
       "basCmtsMapDecodeControlEntry": basCmtsMapDecodeControlEntry,
       "basCmtsMapDecodeControlTriggerMapPktCount": basCmtsMapDecodeControlTriggerMapPktCount,
       "basCmtsMapDecodeControlTriggerDataGrant": basCmtsMapDecodeControlTriggerDataGrant,
       "basCmtsMapDecodeControlTriggerUcdChange": basCmtsMapDecodeControlTriggerUcdChange,
       "basCmtsMapDecodeControlTriggerShortGrant": basCmtsMapDecodeControlTriggerShortGrant,
       "basCmtsMapDecodeControlTriggerLongGrant": basCmtsMapDecodeControlTriggerLongGrant,
       "basCmtsMapDecodeControlTriggerInitMaint": basCmtsMapDecodeControlTriggerInitMaint,
       "basCmtsMapDecodeControlTriggerStationMaint": basCmtsMapDecodeControlTriggerStationMaint,
       "basCmtsMapDecodeControlTriggerRequestIe": basCmtsMapDecodeControlTriggerRequestIe,
       "basCmtsMacToSidObjects": basCmtsMacToSidObjects,
       "basCmtsMacToSidTable": basCmtsMacToSidTable,
       "basCmtsMacToSidEntry": basCmtsMacToSidEntry,
       "basCmtsMacToSidMacAddr": basCmtsMacToSidMacAddr,
       "basCmtsMacToSidServiceId": basCmtsMacToSidServiceId,
       "basCmtsMacToSidType": basCmtsMacToSidType}
)
