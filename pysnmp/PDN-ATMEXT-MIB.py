# SNMP MIB module (PDN-ATMEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-ATMEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:16 2024
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

(aal5VccEntry,
 atmInterfaceConfEntry,
 atmTrafficDescrParamEntry,
 atmVcCrossConnectAdminStatus,
 atmVpCrossConnectAdminStatus) = mibBuilder.importSymbols(
    "ATM-MIB",
    "aal5VccEntry",
    "atmInterfaceConfEntry",
    "atmTrafficDescrParamEntry",
    "atmVcCrossConnectAdminStatus",
    "atmVpCrossConnectAdminStatus")

(ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifOperStatus")

(pdnAtm,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnAtm")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pdnAtmExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5)
)
pdnAtmExtMIB.setRevisions(
        ("2003-05-15 00:00",
         "2003-05-11 00:00",
         "1970-01-01 00:00",
         "2003-03-31 00:00",
         "2002-03-27 00:00",
         "2000-12-29 00:00",
         "2000-12-01 00:00",
         "2000-07-06 00:00",
         "2000-04-28 00:00",
         "2000-03-11 00:00",
         "2000-02-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnAtmExtMIBObjects_ObjectIdentity = ObjectIdentity
pdnAtmExtMIBObjects = _PdnAtmExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1)
)
_PdnAtmIfConfExtTable_Object = MibTable
pdnAtmIfConfExtTable = _PdnAtmIfConfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1)
)
if mibBuilder.loadTexts:
    pdnAtmIfConfExtTable.setStatus("current")
_PdnAtmIfConfExtEntry_Object = MibTableRow
pdnAtmIfConfExtEntry = _PdnAtmIfConfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnAtmIfConfExtEntry.setStatus("current")


class _PdnAtmIfConfExtVbrRtBandwidthUtil_Type(Integer32):
    """Custom type pdnAtmIfConfExtVbrRtBandwidthUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PdnAtmIfConfExtVbrRtBandwidthUtil_Type.__name__ = "Integer32"
_PdnAtmIfConfExtVbrRtBandwidthUtil_Object = MibTableColumn
pdnAtmIfConfExtVbrRtBandwidthUtil = _PdnAtmIfConfExtVbrRtBandwidthUtil_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 1),
    _PdnAtmIfConfExtVbrRtBandwidthUtil_Type()
)
pdnAtmIfConfExtVbrRtBandwidthUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtVbrRtBandwidthUtil.setStatus("current")


class _PdnAtmIfConfExtVbrNrtBandwidthUtil_Type(Integer32):
    """Custom type pdnAtmIfConfExtVbrNrtBandwidthUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PdnAtmIfConfExtVbrNrtBandwidthUtil_Type.__name__ = "Integer32"
_PdnAtmIfConfExtVbrNrtBandwidthUtil_Object = MibTableColumn
pdnAtmIfConfExtVbrNrtBandwidthUtil = _PdnAtmIfConfExtVbrNrtBandwidthUtil_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 2),
    _PdnAtmIfConfExtVbrNrtBandwidthUtil_Type()
)
pdnAtmIfConfExtVbrNrtBandwidthUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtVbrNrtBandwidthUtil.setStatus("current")


class _PdnAtmIfConfExtHecErrorThreshold_Type(Integer32):
    """Custom type pdnAtmIfConfExtHecErrorThreshold based on Integer32"""
    defaultValue = 100


_PdnAtmIfConfExtHecErrorThreshold_Object = MibTableColumn
pdnAtmIfConfExtHecErrorThreshold = _PdnAtmIfConfExtHecErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 3),
    _PdnAtmIfConfExtHecErrorThreshold_Type()
)
pdnAtmIfConfExtHecErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtHecErrorThreshold.setStatus("current")


class _PdnAtmIfConfExtUnknownCellThreshold_Type(Integer32):
    """Custom type pdnAtmIfConfExtUnknownCellThreshold based on Integer32"""
    defaultValue = 10


_PdnAtmIfConfExtUnknownCellThreshold_Object = MibTableColumn
pdnAtmIfConfExtUnknownCellThreshold = _PdnAtmIfConfExtUnknownCellThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 4),
    _PdnAtmIfConfExtUnknownCellThreshold_Type()
)
pdnAtmIfConfExtUnknownCellThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtUnknownCellThreshold.setStatus("current")


class _PdnAtmIfConfExtOcdEventThreshold_Type(Integer32):
    """Custom type pdnAtmIfConfExtOcdEventThreshold based on Integer32"""
    defaultValue = 0


_PdnAtmIfConfExtOcdEventThreshold_Object = MibTableColumn
pdnAtmIfConfExtOcdEventThreshold = _PdnAtmIfConfExtOcdEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 5),
    _PdnAtmIfConfExtOcdEventThreshold_Type()
)
pdnAtmIfConfExtOcdEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtOcdEventThreshold.setStatus("current")
_PdnAtmIfConfExtBandwidthUtilCbrReserved_Type = Integer32
_PdnAtmIfConfExtBandwidthUtilCbrReserved_Object = MibTableColumn
pdnAtmIfConfExtBandwidthUtilCbrReserved = _PdnAtmIfConfExtBandwidthUtilCbrReserved_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 6),
    _PdnAtmIfConfExtBandwidthUtilCbrReserved_Type()
)
pdnAtmIfConfExtBandwidthUtilCbrReserved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtBandwidthUtilCbrReserved.setStatus("current")
_PdnAtmIfConfExtBandwidthUtilCbrAssigned_Type = Integer32
_PdnAtmIfConfExtBandwidthUtilCbrAssigned_Object = MibTableColumn
pdnAtmIfConfExtBandwidthUtilCbrAssigned = _PdnAtmIfConfExtBandwidthUtilCbrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 7),
    _PdnAtmIfConfExtBandwidthUtilCbrAssigned_Type()
)
pdnAtmIfConfExtBandwidthUtilCbrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtBandwidthUtilCbrAssigned.setStatus("current")
_PdnAtmIfConfExtBandwidthUtilVbrRtReserved_Type = Integer32
_PdnAtmIfConfExtBandwidthUtilVbrRtReserved_Object = MibTableColumn
pdnAtmIfConfExtBandwidthUtilVbrRtReserved = _PdnAtmIfConfExtBandwidthUtilVbrRtReserved_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 8),
    _PdnAtmIfConfExtBandwidthUtilVbrRtReserved_Type()
)
pdnAtmIfConfExtBandwidthUtilVbrRtReserved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtBandwidthUtilVbrRtReserved.setStatus("current")
_PdnAtmIfConfExtBandwidthUtilVbrRtAssigned_Type = Integer32
_PdnAtmIfConfExtBandwidthUtilVbrRtAssigned_Object = MibTableColumn
pdnAtmIfConfExtBandwidthUtilVbrRtAssigned = _PdnAtmIfConfExtBandwidthUtilVbrRtAssigned_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 9),
    _PdnAtmIfConfExtBandwidthUtilVbrRtAssigned_Type()
)
pdnAtmIfConfExtBandwidthUtilVbrRtAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtBandwidthUtilVbrRtAssigned.setStatus("current")
_PdnAtmIfConfExtBandwidthUtilVbrNrtReserved_Type = Integer32
_PdnAtmIfConfExtBandwidthUtilVbrNrtReserved_Object = MibTableColumn
pdnAtmIfConfExtBandwidthUtilVbrNrtReserved = _PdnAtmIfConfExtBandwidthUtilVbrNrtReserved_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 10),
    _PdnAtmIfConfExtBandwidthUtilVbrNrtReserved_Type()
)
pdnAtmIfConfExtBandwidthUtilVbrNrtReserved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtBandwidthUtilVbrNrtReserved.setStatus("current")
_PdnAtmIfConfExtBandwidthUtilVbrNrtAssigned_Type = Integer32
_PdnAtmIfConfExtBandwidthUtilVbrNrtAssigned_Object = MibTableColumn
pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned = _PdnAtmIfConfExtBandwidthUtilVbrNrtAssigned_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 11),
    _PdnAtmIfConfExtBandwidthUtilVbrNrtAssigned_Type()
)
pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned.setStatus("current")
_PdnAtmIfConfExtBandwidthUtilUbrReserved_Type = Integer32
_PdnAtmIfConfExtBandwidthUtilUbrReserved_Object = MibTableColumn
pdnAtmIfConfExtBandwidthUtilUbrReserved = _PdnAtmIfConfExtBandwidthUtilUbrReserved_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 12),
    _PdnAtmIfConfExtBandwidthUtilUbrReserved_Type()
)
pdnAtmIfConfExtBandwidthUtilUbrReserved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtBandwidthUtilUbrReserved.setStatus("current")
_PdnAtmIfConfExtBandwidthUtilUbrAssigned_Type = Integer32
_PdnAtmIfConfExtBandwidthUtilUbrAssigned_Object = MibTableColumn
pdnAtmIfConfExtBandwidthUtilUbrAssigned = _PdnAtmIfConfExtBandwidthUtilUbrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 13),
    _PdnAtmIfConfExtBandwidthUtilUbrAssigned_Type()
)
pdnAtmIfConfExtBandwidthUtilUbrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtBandwidthUtilUbrAssigned.setStatus("current")


class _PdnAtmIfConfExtRateShape_Type(Integer32):
    """Custom type pdnAtmIfConfExtRateShape based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 46080),
    )


_PdnAtmIfConfExtRateShape_Type.__name__ = "Integer32"
_PdnAtmIfConfExtRateShape_Object = MibTableColumn
pdnAtmIfConfExtRateShape = _PdnAtmIfConfExtRateShape_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 1, 1, 14),
    _PdnAtmIfConfExtRateShape_Type()
)
pdnAtmIfConfExtRateShape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtRateShape.setStatus("current")
if mibBuilder.loadTexts:
    pdnAtmIfConfExtRateShape.setUnits("Kbps")
_PdnAtmTrafficDescrParamExtTable_Object = MibTable
pdnAtmTrafficDescrParamExtTable = _PdnAtmTrafficDescrParamExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pdnAtmTrafficDescrParamExtTable.setStatus("current")
_PdnAtmTrafficDescrParamExtEntry_Object = MibTableRow
pdnAtmTrafficDescrParamExtEntry = _PdnAtmTrafficDescrParamExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pdnAtmTrafficDescrParamExtEntry.setStatus("current")


class _PdnAtmTrafficDescrParamName_Type(DisplayString):
    """Custom type pdnAtmTrafficDescrParamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_PdnAtmTrafficDescrParamName_Type.__name__ = "DisplayString"
_PdnAtmTrafficDescrParamName_Object = MibTableColumn
pdnAtmTrafficDescrParamName = _PdnAtmTrafficDescrParamName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 2, 1, 1),
    _PdnAtmTrafficDescrParamName_Type()
)
pdnAtmTrafficDescrParamName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAtmTrafficDescrParamName.setStatus("current")
_PdnAtmTrafficPolicing_Type = TruthValue
_PdnAtmTrafficPolicing_Object = MibTableColumn
pdnAtmTrafficPolicing = _PdnAtmTrafficPolicing_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 2, 1, 2),
    _PdnAtmTrafficPolicing_Type()
)
pdnAtmTrafficPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAtmTrafficPolicing.setStatus("current")
_PdnAtmTrafficShaping_Type = TruthValue
_PdnAtmTrafficShaping_Object = MibTableColumn
pdnAtmTrafficShaping = _PdnAtmTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 2, 1, 3),
    _PdnAtmTrafficShaping_Type()
)
pdnAtmTrafficShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAtmTrafficShaping.setStatus("current")
_PdnAal5VccExtTable_Object = MibTable
pdnAal5VccExtTable = _PdnAal5VccExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 3)
)
if mibBuilder.loadTexts:
    pdnAal5VccExtTable.setStatus("current")
_PdnAal5VccExtEntry_Object = MibTableRow
pdnAal5VccExtEntry = _PdnAal5VccExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pdnAal5VccExtEntry.setStatus("current")
_PdnAal5VccExtOutPDUs_Type = Unsigned32
_PdnAal5VccExtOutPDUs_Object = MibTableColumn
pdnAal5VccExtOutPDUs = _PdnAal5VccExtOutPDUs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 3, 1, 1),
    _PdnAal5VccExtOutPDUs_Type()
)
pdnAal5VccExtOutPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAal5VccExtOutPDUs.setStatus("current")
_PdnAal5VccExtInPDUs_Type = Unsigned32
_PdnAal5VccExtInPDUs_Object = MibTableColumn
pdnAal5VccExtInPDUs = _PdnAal5VccExtInPDUs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 1, 3, 1, 2),
    _PdnAal5VccExtInPDUs_Type()
)
pdnAal5VccExtInPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAal5VccExtInPDUs.setStatus("current")
_PdnAtmExtMIBTraps_ObjectIdentity = ObjectIdentity
pdnAtmExtMIBTraps = _PdnAtmExtMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 2)
)
_PdnAtmExtMIBTrapPrefix_ObjectIdentity = ObjectIdentity
pdnAtmExtMIBTrapPrefix = _PdnAtmExtMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 2, 0)
)
_PdnAtmExtMIBConformance_ObjectIdentity = ObjectIdentity
pdnAtmExtMIBConformance = _PdnAtmExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 3)
)
_PdnAtmExtMibCompliances_ObjectIdentity = ObjectIdentity
pdnAtmExtMibCompliances = _PdnAtmExtMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 3, 1)
)
_PdnAtmExtMibGroups_ObjectIdentity = ObjectIdentity
pdnAtmExtMibGroups = _PdnAtmExtMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 3, 2)
)
_PdnAtmExtMIBTrafficDescriptorTypes_ObjectIdentity = ObjectIdentity
pdnAtmExtMIBTrafficDescriptorTypes = _PdnAtmExtMIBTrafficDescriptorTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 4)
)
_PdnAtmNoClpTaggingNoScrCdvtMdcr_ObjectIdentity = ObjectIdentity
pdnAtmNoClpTaggingNoScrCdvtMdcr = _PdnAtmNoClpTaggingNoScrCdvtMdcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 4, 1)
)
if mibBuilder.loadTexts:
    pdnAtmNoClpTaggingNoScrCdvtMdcr.setStatus("current")
_PdnAtmNoClpNoScrCdvtMdcr_ObjectIdentity = ObjectIdentity
pdnAtmNoClpNoScrCdvtMdcr = _PdnAtmNoClpNoScrCdvtMdcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 4, 2)
)
if mibBuilder.loadTexts:
    pdnAtmNoClpNoScrCdvtMdcr.setStatus("current")
atmInterfaceConfEntry.registerAugmentions(
    ("PDN-ATMEXT-MIB",
     "pdnAtmIfConfExtEntry")
)
pdnAtmIfConfExtEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
atmTrafficDescrParamEntry.registerAugmentions(
    ("PDN-ATMEXT-MIB",
     "pdnAtmTrafficDescrParamExtEntry")
)
pdnAtmTrafficDescrParamExtEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
aal5VccEntry.registerAugmentions(
    ("PDN-ATMEXT-MIB",
     "pdnAal5VccExtEntry")
)
pdnAal5VccExtEntry.setIndexNames(*aal5VccEntry.getIndexNames())

# Managed Objects groups

pdnAtmIfConfExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 3, 2, 1)
)
pdnAtmIfConfExtGroup.setObjects(
      *(("PDN-ATMEXT-MIB", "pdnAtmIfConfExtVbrRtBandwidthUtil"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtVbrNrtBandwidthUtil"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtHecErrorThreshold"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtUnknownCellThreshold"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtOcdEventThreshold"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtBandwidthUtilCbrReserved"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtBandwidthUtilCbrAssigned"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtBandwidthUtilVbrRtReserved"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtBandwidthUtilVbrRtAssigned"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtBandwidthUtilVbrNrtReserved"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtBandwidthUtilUbrReserved"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtBandwidthUtilUbrAssigned"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtRateShape"))
)
if mibBuilder.loadTexts:
    pdnAtmIfConfExtGroup.setStatus("current")

pdnAtmTrafficDescrParamExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 3, 2, 2)
)
pdnAtmTrafficDescrParamExtGroup.setObjects(
      *(("PDN-ATMEXT-MIB", "pdnAtmTrafficDescrParamName"),
        ("PDN-ATMEXT-MIB", "pdnAtmTrafficPolicing"),
        ("PDN-ATMEXT-MIB", "pdnAtmTrafficShaping"))
)
if mibBuilder.loadTexts:
    pdnAtmTrafficDescrParamExtGroup.setStatus("current")

pdnAal5VccExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 3, 2, 3)
)
pdnAal5VccExtGroup.setObjects(
      *(("PDN-ATMEXT-MIB", "pdnAal5VccExtInPDUs"),
        ("PDN-ATMEXT-MIB", "pdnAal5VccExtOutPDUs"))
)
if mibBuilder.loadTexts:
    pdnAal5VccExtGroup.setStatus("current")


# Notification objects

pdnAtmIfConfExtExcessInvalidCellsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 2, 0, 1)
)
pdnAtmIfConfExtExcessInvalidCellsAlarm.setObjects(
      *(("IF-MIB", "ifOperStatus"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtUnknownCellThreshold"))
)
if mibBuilder.loadTexts:
    pdnAtmIfConfExtExcessInvalidCellsAlarm.setStatus(
        "current"
    )

pdnAtmIfConfExtEgressLineRateAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 2, 0, 2)
)
pdnAtmIfConfExtEgressLineRateAlarmSet.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    pdnAtmIfConfExtEgressLineRateAlarmSet.setStatus(
        "current"
    )

pdnAtmIfConfExtVplNoBandwidthAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 2, 0, 3)
)
pdnAtmIfConfExtVplNoBandwidthAvail.setObjects(
    ("ATM-MIB", "atmVpCrossConnectAdminStatus")
)
if mibBuilder.loadTexts:
    pdnAtmIfConfExtVplNoBandwidthAvail.setStatus(
        "current"
    )

pdnAtmIfConfExtVclNoBandwidthAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 2, 0, 4)
)
pdnAtmIfConfExtVclNoBandwidthAvail.setObjects(
    ("ATM-MIB", "atmVcCrossConnectAdminStatus")
)
if mibBuilder.loadTexts:
    pdnAtmIfConfExtVclNoBandwidthAvail.setStatus(
        "current"
    )

pdnAtmIfConfExtIngressLineRateAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 2, 0, 5)
)
pdnAtmIfConfExtIngressLineRateAlarmSet.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    pdnAtmIfConfExtIngressLineRateAlarmSet.setStatus(
        "current"
    )

pdnAtmIfConfExtEgressLineRateAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 2, 0, 102)
)
pdnAtmIfConfExtEgressLineRateAlarmClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    pdnAtmIfConfExtEgressLineRateAlarmClear.setStatus(
        "current"
    )

pdnAtmIfConfExtIngressLineRateAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 2, 0, 105)
)
pdnAtmIfConfExtIngressLineRateAlarmClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    pdnAtmIfConfExtIngressLineRateAlarmClear.setStatus(
        "current"
    )


# Notifications groups

pdnAtmExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 5, 3, 2, 4)
)
pdnAtmExtNotificationGroup.setObjects(
      *(("PDN-ATMEXT-MIB", "pdnAtmIfConfExtExcessInvalidCellsAlarm"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtEgressLineRateAlarmSet"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtEgressLineRateAlarmClear"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtVplNoBandwidthAvail"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtVclNoBandwidthAvail"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtIngressLineRateAlarmSet"),
        ("PDN-ATMEXT-MIB", "pdnAtmIfConfExtIngressLineRateAlarmClear"))
)
if mibBuilder.loadTexts:
    pdnAtmExtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ATMEXT-MIB",
    **{"pdnAtmExtMIB": pdnAtmExtMIB,
       "pdnAtmExtMIBObjects": pdnAtmExtMIBObjects,
       "pdnAtmIfConfExtTable": pdnAtmIfConfExtTable,
       "pdnAtmIfConfExtEntry": pdnAtmIfConfExtEntry,
       "pdnAtmIfConfExtVbrRtBandwidthUtil": pdnAtmIfConfExtVbrRtBandwidthUtil,
       "pdnAtmIfConfExtVbrNrtBandwidthUtil": pdnAtmIfConfExtVbrNrtBandwidthUtil,
       "pdnAtmIfConfExtHecErrorThreshold": pdnAtmIfConfExtHecErrorThreshold,
       "pdnAtmIfConfExtUnknownCellThreshold": pdnAtmIfConfExtUnknownCellThreshold,
       "pdnAtmIfConfExtOcdEventThreshold": pdnAtmIfConfExtOcdEventThreshold,
       "pdnAtmIfConfExtBandwidthUtilCbrReserved": pdnAtmIfConfExtBandwidthUtilCbrReserved,
       "pdnAtmIfConfExtBandwidthUtilCbrAssigned": pdnAtmIfConfExtBandwidthUtilCbrAssigned,
       "pdnAtmIfConfExtBandwidthUtilVbrRtReserved": pdnAtmIfConfExtBandwidthUtilVbrRtReserved,
       "pdnAtmIfConfExtBandwidthUtilVbrRtAssigned": pdnAtmIfConfExtBandwidthUtilVbrRtAssigned,
       "pdnAtmIfConfExtBandwidthUtilVbrNrtReserved": pdnAtmIfConfExtBandwidthUtilVbrNrtReserved,
       "pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned": pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned,
       "pdnAtmIfConfExtBandwidthUtilUbrReserved": pdnAtmIfConfExtBandwidthUtilUbrReserved,
       "pdnAtmIfConfExtBandwidthUtilUbrAssigned": pdnAtmIfConfExtBandwidthUtilUbrAssigned,
       "pdnAtmIfConfExtRateShape": pdnAtmIfConfExtRateShape,
       "pdnAtmTrafficDescrParamExtTable": pdnAtmTrafficDescrParamExtTable,
       "pdnAtmTrafficDescrParamExtEntry": pdnAtmTrafficDescrParamExtEntry,
       "pdnAtmTrafficDescrParamName": pdnAtmTrafficDescrParamName,
       "pdnAtmTrafficPolicing": pdnAtmTrafficPolicing,
       "pdnAtmTrafficShaping": pdnAtmTrafficShaping,
       "pdnAal5VccExtTable": pdnAal5VccExtTable,
       "pdnAal5VccExtEntry": pdnAal5VccExtEntry,
       "pdnAal5VccExtOutPDUs": pdnAal5VccExtOutPDUs,
       "pdnAal5VccExtInPDUs": pdnAal5VccExtInPDUs,
       "pdnAtmExtMIBTraps": pdnAtmExtMIBTraps,
       "pdnAtmExtMIBTrapPrefix": pdnAtmExtMIBTrapPrefix,
       "pdnAtmIfConfExtExcessInvalidCellsAlarm": pdnAtmIfConfExtExcessInvalidCellsAlarm,
       "pdnAtmIfConfExtEgressLineRateAlarmSet": pdnAtmIfConfExtEgressLineRateAlarmSet,
       "pdnAtmIfConfExtVplNoBandwidthAvail": pdnAtmIfConfExtVplNoBandwidthAvail,
       "pdnAtmIfConfExtVclNoBandwidthAvail": pdnAtmIfConfExtVclNoBandwidthAvail,
       "pdnAtmIfConfExtIngressLineRateAlarmSet": pdnAtmIfConfExtIngressLineRateAlarmSet,
       "pdnAtmIfConfExtEgressLineRateAlarmClear": pdnAtmIfConfExtEgressLineRateAlarmClear,
       "pdnAtmIfConfExtIngressLineRateAlarmClear": pdnAtmIfConfExtIngressLineRateAlarmClear,
       "pdnAtmExtMIBConformance": pdnAtmExtMIBConformance,
       "pdnAtmExtMibCompliances": pdnAtmExtMibCompliances,
       "pdnAtmExtMibGroups": pdnAtmExtMibGroups,
       "pdnAtmIfConfExtGroup": pdnAtmIfConfExtGroup,
       "pdnAtmTrafficDescrParamExtGroup": pdnAtmTrafficDescrParamExtGroup,
       "pdnAal5VccExtGroup": pdnAal5VccExtGroup,
       "pdnAtmExtNotificationGroup": pdnAtmExtNotificationGroup,
       "pdnAtmExtMIBTrafficDescriptorTypes": pdnAtmExtMIBTrafficDescriptorTypes,
       "pdnAtmNoClpTaggingNoScrCdvtMdcr": pdnAtmNoClpTaggingNoScrCdvtMdcr,
       "pdnAtmNoClpNoScrCdvtMdcr": pdnAtmNoClpNoScrCdvtMdcr}
)
