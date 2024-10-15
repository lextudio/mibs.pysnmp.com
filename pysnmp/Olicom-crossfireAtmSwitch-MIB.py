# SNMP MIB module (Olicom-crossfireAtmSwitch-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Olicom-crossfireAtmSwitch-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:53 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(controlTime,
 ocmibsCrossfireAtmMIB) = mibBuilder.importSymbols(
    "Olicom-MIB",
    "controlTime",
    "ocmibsCrossfireAtmMIB")

(MacAddress,) = mibBuilder.importSymbols(
    "RFC1231-MIB",
    "MacAddress")

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



class AtmAddress(OctetString):
    """Custom type AtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Olicom_ObjectIdentity = ObjectIdentity
olicom = _Olicom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285)
)
_Ocmibs_ObjectIdentity = ObjectIdentity
ocmibs = _Ocmibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2)
)
_OcmibsCrossfireAtmMIB_ObjectIdentity = ObjectIdentity
ocmibsCrossfireAtmMIB = _OcmibsCrossfireAtmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6)
)
_CrossfireAtmInfo_ObjectIdentity = ObjectIdentity
crossfireAtmInfo = _CrossfireAtmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1)
)
_InfoProcessorModule_ObjectIdentity = ObjectIdentity
infoProcessorModule = _InfoProcessorModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 1)
)
_InfoProcessorModuleHwProductId_Type = DisplayString
_InfoProcessorModuleHwProductId_Object = MibScalar
infoProcessorModuleHwProductId = _InfoProcessorModuleHwProductId_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 1, 1),
    _InfoProcessorModuleHwProductId_Type()
)
infoProcessorModuleHwProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoProcessorModuleHwProductId.setStatus("mandatory")
_InfoProcessorModuleHwVersion_Type = DisplayString
_InfoProcessorModuleHwVersion_Object = MibScalar
infoProcessorModuleHwVersion = _InfoProcessorModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 1, 2),
    _InfoProcessorModuleHwVersion_Type()
)
infoProcessorModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoProcessorModuleHwVersion.setStatus("mandatory")
_InfoProcessorModuleHwEcoLevel_Type = DisplayString
_InfoProcessorModuleHwEcoLevel_Object = MibScalar
infoProcessorModuleHwEcoLevel = _InfoProcessorModuleHwEcoLevel_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 1, 3),
    _InfoProcessorModuleHwEcoLevel_Type()
)
infoProcessorModuleHwEcoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoProcessorModuleHwEcoLevel.setStatus("mandatory")
_InfoProcessorModuleHwSerialNumber_Type = DisplayString
_InfoProcessorModuleHwSerialNumber_Object = MibScalar
infoProcessorModuleHwSerialNumber = _InfoProcessorModuleHwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 1, 4),
    _InfoProcessorModuleHwSerialNumber_Type()
)
infoProcessorModuleHwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoProcessorModuleHwSerialNumber.setStatus("mandatory")
_InfoProcessorModuleHwOptionTable_Object = MibTable
infoProcessorModuleHwOptionTable = _InfoProcessorModuleHwOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    infoProcessorModuleHwOptionTable.setStatus("mandatory")
_InfoProcessorModuleHwOptionEntry_Object = MibTableRow
infoProcessorModuleHwOptionEntry = _InfoProcessorModuleHwOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 1, 5, 1)
)
infoProcessorModuleHwOptionEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "infoProcessorModuleHwOptionNo"),
)
if mibBuilder.loadTexts:
    infoProcessorModuleHwOptionEntry.setStatus("mandatory")
_InfoProcessorModuleHwOptionNo_Type = Integer32
_InfoProcessorModuleHwOptionNo_Object = MibTableColumn
infoProcessorModuleHwOptionNo = _InfoProcessorModuleHwOptionNo_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 1, 5, 1, 1),
    _InfoProcessorModuleHwOptionNo_Type()
)
infoProcessorModuleHwOptionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoProcessorModuleHwOptionNo.setStatus("mandatory")
_InfoProcessorModuleHwOption_Type = DisplayString
_InfoProcessorModuleHwOption_Object = MibTableColumn
infoProcessorModuleHwOption = _InfoProcessorModuleHwOption_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 1, 5, 1, 2),
    _InfoProcessorModuleHwOption_Type()
)
infoProcessorModuleHwOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoProcessorModuleHwOption.setStatus("mandatory")
_InfoFeatureModule_ObjectIdentity = ObjectIdentity
infoFeatureModule = _InfoFeatureModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 2)
)
_InfoFeatureModuleHwProductId_Type = DisplayString
_InfoFeatureModuleHwProductId_Object = MibScalar
infoFeatureModuleHwProductId = _InfoFeatureModuleHwProductId_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 2, 1),
    _InfoFeatureModuleHwProductId_Type()
)
infoFeatureModuleHwProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFeatureModuleHwProductId.setStatus("mandatory")
_InfoFeatureModuleHwVersion_Type = DisplayString
_InfoFeatureModuleHwVersion_Object = MibScalar
infoFeatureModuleHwVersion = _InfoFeatureModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 2, 2),
    _InfoFeatureModuleHwVersion_Type()
)
infoFeatureModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFeatureModuleHwVersion.setStatus("mandatory")
_InfoFeatureModuleHwEcoLevel_Type = DisplayString
_InfoFeatureModuleHwEcoLevel_Object = MibScalar
infoFeatureModuleHwEcoLevel = _InfoFeatureModuleHwEcoLevel_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 2, 3),
    _InfoFeatureModuleHwEcoLevel_Type()
)
infoFeatureModuleHwEcoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFeatureModuleHwEcoLevel.setStatus("mandatory")
_InfoFeatureModuleHwSerialNumber_Type = DisplayString
_InfoFeatureModuleHwSerialNumber_Object = MibScalar
infoFeatureModuleHwSerialNumber = _InfoFeatureModuleHwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 2, 4),
    _InfoFeatureModuleHwSerialNumber_Type()
)
infoFeatureModuleHwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFeatureModuleHwSerialNumber.setStatus("mandatory")
_InfoFeatureModuleHwOptionTable_Object = MibTable
infoFeatureModuleHwOptionTable = _InfoFeatureModuleHwOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 2, 5)
)
if mibBuilder.loadTexts:
    infoFeatureModuleHwOptionTable.setStatus("mandatory")
_InfoFeatureModuleHwOptionEntry_Object = MibTableRow
infoFeatureModuleHwOptionEntry = _InfoFeatureModuleHwOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 2, 5, 1)
)
infoFeatureModuleHwOptionEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "infoFeatureModuleHwOptionNo"),
)
if mibBuilder.loadTexts:
    infoFeatureModuleHwOptionEntry.setStatus("mandatory")
_InfoFeatureModuleHwOptionNo_Type = Integer32
_InfoFeatureModuleHwOptionNo_Object = MibTableColumn
infoFeatureModuleHwOptionNo = _InfoFeatureModuleHwOptionNo_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 2, 5, 1, 1),
    _InfoFeatureModuleHwOptionNo_Type()
)
infoFeatureModuleHwOptionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFeatureModuleHwOptionNo.setStatus("mandatory")
_InfoFeatureModuleHwOption_Type = DisplayString
_InfoFeatureModuleHwOption_Object = MibTableColumn
infoFeatureModuleHwOption = _InfoFeatureModuleHwOption_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 2, 5, 1, 2),
    _InfoFeatureModuleHwOption_Type()
)
infoFeatureModuleHwOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFeatureModuleHwOption.setStatus("mandatory")
_InfoXModule_ObjectIdentity = ObjectIdentity
infoXModule = _InfoXModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3)
)
_InfoXModuleTable_Object = MibTable
infoXModuleTable = _InfoXModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    infoXModuleTable.setStatus("mandatory")
_InfoXModuleEntry_Object = MibTableRow
infoXModuleEntry = _InfoXModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 1, 1)
)
infoXModuleEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "infoXModuleSlotIndex"),
)
if mibBuilder.loadTexts:
    infoXModuleEntry.setStatus("mandatory")


class _InfoXModuleSlotIndex_Type(Integer32):
    """Custom type infoXModuleSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_InfoXModuleSlotIndex_Type.__name__ = "Integer32"
_InfoXModuleSlotIndex_Object = MibTableColumn
infoXModuleSlotIndex = _InfoXModuleSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 1, 1, 1),
    _InfoXModuleSlotIndex_Type()
)
infoXModuleSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXModuleSlotIndex.setStatus("mandatory")
_InfoXModuleHwProductId_Type = DisplayString
_InfoXModuleHwProductId_Object = MibTableColumn
infoXModuleHwProductId = _InfoXModuleHwProductId_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 1, 1, 2),
    _InfoXModuleHwProductId_Type()
)
infoXModuleHwProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXModuleHwProductId.setStatus("mandatory")
_InfoXModuleHwVersion_Type = DisplayString
_InfoXModuleHwVersion_Object = MibTableColumn
infoXModuleHwVersion = _InfoXModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 1, 1, 3),
    _InfoXModuleHwVersion_Type()
)
infoXModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXModuleHwVersion.setStatus("mandatory")
_InfoXModuleHwEcoLevel_Type = DisplayString
_InfoXModuleHwEcoLevel_Object = MibTableColumn
infoXModuleHwEcoLevel = _InfoXModuleHwEcoLevel_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 1, 1, 4),
    _InfoXModuleHwEcoLevel_Type()
)
infoXModuleHwEcoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXModuleHwEcoLevel.setStatus("mandatory")
_InfoXModuleHwSerialNumber_Type = DisplayString
_InfoXModuleHwSerialNumber_Object = MibTableColumn
infoXModuleHwSerialNumber = _InfoXModuleHwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 1, 1, 5),
    _InfoXModuleHwSerialNumber_Type()
)
infoXModuleHwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXModuleHwSerialNumber.setStatus("mandatory")
_InfoXModuleHwOptionTable_Object = MibTable
infoXModuleHwOptionTable = _InfoXModuleHwOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    infoXModuleHwOptionTable.setStatus("mandatory")
_InfoXModuleHwOptionEntry_Object = MibTableRow
infoXModuleHwOptionEntry = _InfoXModuleHwOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 2, 1)
)
infoXModuleHwOptionEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "infoXModuleHwOptionSlotIndex"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "infoXModuleHwOptionNo"),
)
if mibBuilder.loadTexts:
    infoXModuleHwOptionEntry.setStatus("mandatory")
_InfoXModuleHwOptionSlotIndex_Type = Integer32
_InfoXModuleHwOptionSlotIndex_Object = MibTableColumn
infoXModuleHwOptionSlotIndex = _InfoXModuleHwOptionSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 2, 1, 1),
    _InfoXModuleHwOptionSlotIndex_Type()
)
infoXModuleHwOptionSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXModuleHwOptionSlotIndex.setStatus("mandatory")
_InfoXModuleHwOptionNo_Type = Integer32
_InfoXModuleHwOptionNo_Object = MibTableColumn
infoXModuleHwOptionNo = _InfoXModuleHwOptionNo_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 2, 1, 2),
    _InfoXModuleHwOptionNo_Type()
)
infoXModuleHwOptionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXModuleHwOptionNo.setStatus("mandatory")
_InfoXModuleHwOption_Type = DisplayString
_InfoXModuleHwOption_Object = MibTableColumn
infoXModuleHwOption = _InfoXModuleHwOption_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 3, 2, 1, 3),
    _InfoXModuleHwOption_Type()
)
infoXModuleHwOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXModuleHwOption.setStatus("mandatory")
_InfoIfIndex_ObjectIdentity = ObjectIdentity
infoIfIndex = _InfoIfIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 4)
)
_InfoIfIndexLan_Type = Integer32
_InfoIfIndexLan_Object = MibScalar
infoIfIndexLan = _InfoIfIndexLan_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 4, 1),
    _InfoIfIndexLan_Type()
)
infoIfIndexLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIfIndexLan.setStatus("mandatory")
_InfoIfIndexSlip_Type = Integer32
_InfoIfIndexSlip_Object = MibScalar
infoIfIndexSlip = _InfoIfIndexSlip_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 4, 2),
    _InfoIfIndexSlip_Type()
)
infoIfIndexSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIfIndexSlip.setStatus("mandatory")
_InfoIfIndexElan_Type = Integer32
_InfoIfIndexElan_Object = MibScalar
infoIfIndexElan = _InfoIfIndexElan_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 4, 3),
    _InfoIfIndexElan_Type()
)
infoIfIndexElan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIfIndexElan.setStatus("mandatory")
_InfoIfIndexClassicalIp_Type = Integer32
_InfoIfIndexClassicalIp_Object = MibScalar
infoIfIndexClassicalIp = _InfoIfIndexClassicalIp_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 4, 4),
    _InfoIfIndexClassicalIp_Type()
)
infoIfIndexClassicalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIfIndexClassicalIp.setStatus("mandatory")
_InfoIfIndexRfc1483Bridged_Type = Integer32
_InfoIfIndexRfc1483Bridged_Object = MibScalar
infoIfIndexRfc1483Bridged = _InfoIfIndexRfc1483Bridged_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 4, 5),
    _InfoIfIndexRfc1483Bridged_Type()
)
infoIfIndexRfc1483Bridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIfIndexRfc1483Bridged.setStatus("mandatory")
_InfoIfIndexRfc1483Routed_Type = Integer32
_InfoIfIndexRfc1483Routed_Object = MibScalar
infoIfIndexRfc1483Routed = _InfoIfIndexRfc1483Routed_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 4, 6),
    _InfoIfIndexRfc1483Routed_Type()
)
infoIfIndexRfc1483Routed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIfIndexRfc1483Routed.setStatus("mandatory")
_InfoIfIndexAtmNode_Type = Integer32
_InfoIfIndexAtmNode_Object = MibScalar
infoIfIndexAtmNode = _InfoIfIndexAtmNode_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 4, 7),
    _InfoIfIndexAtmNode_Type()
)
infoIfIndexAtmNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIfIndexAtmNode.setStatus("mandatory")
_TermRestartInfo_ObjectIdentity = ObjectIdentity
termRestartInfo = _TermRestartInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5)
)
_TermRestartInfoRestartTime_Type = Integer32
_TermRestartInfoRestartTime_Object = MibScalar
termRestartInfoRestartTime = _TermRestartInfoRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 1),
    _TermRestartInfoRestartTime_Type()
)
termRestartInfoRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoRestartTime.setStatus("mandatory")
_TermRestartInfoSwSection1StatusWord_Type = Integer32
_TermRestartInfoSwSection1StatusWord_Object = MibScalar
termRestartInfoSwSection1StatusWord = _TermRestartInfoSwSection1StatusWord_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 2),
    _TermRestartInfoSwSection1StatusWord_Type()
)
termRestartInfoSwSection1StatusWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoSwSection1StatusWord.setStatus("mandatory")
_TermRestartInfoSwSection2StatusWord_Type = Integer32
_TermRestartInfoSwSection2StatusWord_Object = MibScalar
termRestartInfoSwSection2StatusWord = _TermRestartInfoSwSection2StatusWord_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 3),
    _TermRestartInfoSwSection2StatusWord_Type()
)
termRestartInfoSwSection2StatusWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoSwSection2StatusWord.setStatus("mandatory")


class _TermRestartInfoSwImageLoaded_Type(Integer32):
    """Custom type termRestartInfoSwImageLoaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_TermRestartInfoSwImageLoaded_Type.__name__ = "Integer32"
_TermRestartInfoSwImageLoaded_Object = MibScalar
termRestartInfoSwImageLoaded = _TermRestartInfoSwImageLoaded_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 4),
    _TermRestartInfoSwImageLoaded_Type()
)
termRestartInfoSwImageLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoSwImageLoaded.setStatus("mandatory")


class _TermRestartInfoFutureTestMode_Type(Integer32):
    """Custom type termRestartInfoFutureTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_TermRestartInfoFutureTestMode_Type.__name__ = "Integer32"
_TermRestartInfoFutureTestMode_Object = MibScalar
termRestartInfoFutureTestMode = _TermRestartInfoFutureTestMode_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 5),
    _TermRestartInfoFutureTestMode_Type()
)
termRestartInfoFutureTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoFutureTestMode.setStatus("mandatory")


class _TermRestartInfoBootpExecuted_Type(Integer32):
    """Custom type termRestartInfoBootpExecuted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_TermRestartInfoBootpExecuted_Type.__name__ = "Integer32"
_TermRestartInfoBootpExecuted_Object = MibScalar
termRestartInfoBootpExecuted = _TermRestartInfoBootpExecuted_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 6),
    _TermRestartInfoBootpExecuted_Type()
)
termRestartInfoBootpExecuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoBootpExecuted.setStatus("mandatory")
_TermRestartInfoReloadTime_Type = Integer32
_TermRestartInfoReloadTime_Object = MibScalar
termRestartInfoReloadTime = _TermRestartInfoReloadTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 7),
    _TermRestartInfoReloadTime_Type()
)
termRestartInfoReloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoReloadTime.setStatus("mandatory")


class _TermRestartInfoBootpReason_Type(Integer32):
    """Custom type termRestartInfoBootpReason based on Integer32"""
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
        *(("chksumError", 2),
          ("invalidSwStatus", 3),
          ("noSw", 1),
          ("pushButtons", 4),
          ("undefined", 5))
    )


_TermRestartInfoBootpReason_Type.__name__ = "Integer32"
_TermRestartInfoBootpReason_Object = MibScalar
termRestartInfoBootpReason = _TermRestartInfoBootpReason_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 8),
    _TermRestartInfoBootpReason_Type()
)
termRestartInfoBootpReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoBootpReason.setStatus("mandatory")
_TermRestartInfoServerIpAddress_Type = IpAddress
_TermRestartInfoServerIpAddress_Object = MibScalar
termRestartInfoServerIpAddress = _TermRestartInfoServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 9),
    _TermRestartInfoServerIpAddress_Type()
)
termRestartInfoServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoServerIpAddress.setStatus("mandatory")
_TermRestartInfoServerMacAddress_Type = MacAddress
_TermRestartInfoServerMacAddress_Object = MibScalar
termRestartInfoServerMacAddress = _TermRestartInfoServerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 10),
    _TermRestartInfoServerMacAddress_Type()
)
termRestartInfoServerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoServerMacAddress.setStatus("mandatory")
_TermRestartInfoFileName_Type = DisplayString
_TermRestartInfoFileName_Object = MibScalar
termRestartInfoFileName = _TermRestartInfoFileName_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 11),
    _TermRestartInfoFileName_Type()
)
termRestartInfoFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoFileName.setStatus("mandatory")
_TermRestartInfoBbsramTerminationTimestamp_Type = Integer32
_TermRestartInfoBbsramTerminationTimestamp_Object = MibScalar
termRestartInfoBbsramTerminationTimestamp = _TermRestartInfoBbsramTerminationTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 12),
    _TermRestartInfoBbsramTerminationTimestamp_Type()
)
termRestartInfoBbsramTerminationTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoBbsramTerminationTimestamp.setStatus("mandatory")


class _TermRestartInfoTerminationReason_Type(Integer32):
    """Custom type termRestartInfoTerminationReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("controlled", 2),
          ("controlledHalt", 3),
          ("fatal", 4),
          ("featureModuleRemoved", 8),
          ("psuFailure", 7),
          ("temperatureAlarm", 6),
          ("unknown", 1),
          ("watchdog", 5))
    )


_TermRestartInfoTerminationReason_Type.__name__ = "Integer32"
_TermRestartInfoTerminationReason_Object = MibScalar
termRestartInfoTerminationReason = _TermRestartInfoTerminationReason_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 13),
    _TermRestartInfoTerminationReason_Type()
)
termRestartInfoTerminationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoTerminationReason.setStatus("mandatory")


class _TermRestartInfoRestartReason_Type(Integer32):
    """Custom type termRestartInfoRestartReason based on Integer32"""
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
        *(("coldStart", 7),
          ("controlled", 6),
          ("default", 2),
          ("fatal", 5),
          ("featureModuleRemoved", 9),
          ("reset", 1),
          ("resetDefault", 3),
          ("unknown", 8),
          ("watchdog", 4))
    )


_TermRestartInfoRestartReason_Type.__name__ = "Integer32"
_TermRestartInfoRestartReason_Object = MibScalar
termRestartInfoRestartReason = _TermRestartInfoRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 14),
    _TermRestartInfoRestartReason_Type()
)
termRestartInfoRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoRestartReason.setStatus("mandatory")


class _TermRestartInfoHwReconfigState_Type(Integer32):
    """Custom type termRestartInfoHwReconfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noReconfig", 3),
          ("partialReconfig", 2),
          ("totalReconfig", 1))
    )


_TermRestartInfoHwReconfigState_Type.__name__ = "Integer32"
_TermRestartInfoHwReconfigState_Object = MibScalar
termRestartInfoHwReconfigState = _TermRestartInfoHwReconfigState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 15),
    _TermRestartInfoHwReconfigState_Type()
)
termRestartInfoHwReconfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoHwReconfigState.setStatus("mandatory")


class _TermRestartInfoBbsram_Type(OctetString):
    """Custom type termRestartInfoBbsram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_TermRestartInfoBbsram_Type.__name__ = "OctetString"
_TermRestartInfoBbsram_Object = MibScalar
termRestartInfoBbsram = _TermRestartInfoBbsram_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 1, 5, 16),
    _TermRestartInfoBbsram_Type()
)
termRestartInfoBbsram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRestartInfoBbsram.setStatus("mandatory")
_CrossfireAtmConfiguration_ObjectIdentity = ObjectIdentity
crossfireAtmConfiguration = _CrossfireAtmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2)
)
_ConfigAddressing_ObjectIdentity = ObjectIdentity
configAddressing = _ConfigAddressing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 1)
)


class _ConfigSwitchAddrPrefixType_Type(Integer32):
    """Custom type configSwitchAddrPrefixType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(57,
              69,
              71)
        )
    )
    namedValues = NamedValues(
        *(("dcc", 57),
          ("icd", 71),
          ("iso", 69))
    )


_ConfigSwitchAddrPrefixType_Type.__name__ = "Integer32"
_ConfigSwitchAddrPrefixType_Object = MibScalar
configSwitchAddrPrefixType = _ConfigSwitchAddrPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 1, 1),
    _ConfigSwitchAddrPrefixType_Type()
)
configSwitchAddrPrefixType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSwitchAddrPrefixType.setStatus("mandatory")


class _ConfigSwitchAddrPrefixSize_Type(Integer32):
    """Custom type configSwitchAddrPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ConfigSwitchAddrPrefixSize_Type.__name__ = "Integer32"
_ConfigSwitchAddrPrefixSize_Object = MibScalar
configSwitchAddrPrefixSize = _ConfigSwitchAddrPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 1, 2),
    _ConfigSwitchAddrPrefixSize_Type()
)
configSwitchAddrPrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSwitchAddrPrefixSize.setStatus("mandatory")


class _ConfigSwitchAddrAtmPrefix_Type(OctetString):
    """Custom type configSwitchAddrAtmPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_ConfigSwitchAddrAtmPrefix_Type.__name__ = "OctetString"
_ConfigSwitchAddrAtmPrefix_Object = MibScalar
configSwitchAddrAtmPrefix = _ConfigSwitchAddrAtmPrefix_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 1, 3),
    _ConfigSwitchAddrAtmPrefix_Type()
)
configSwitchAddrAtmPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSwitchAddrAtmPrefix.setStatus("mandatory")
_ConfigSwitchAddrAtmAddress_Type = AtmAddress
_ConfigSwitchAddrAtmAddress_Object = MibScalar
configSwitchAddrAtmAddress = _ConfigSwitchAddrAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 1, 4),
    _ConfigSwitchAddrAtmAddress_Type()
)
configSwitchAddrAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configSwitchAddrAtmAddress.setStatus("mandatory")
_ConfigClocking_ObjectIdentity = ObjectIdentity
configClocking = _ConfigClocking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 2)
)


class _ConfigNetworkClockSource_Type(Integer32):
    """Custom type configNetworkClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_ConfigNetworkClockSource_Type.__name__ = "Integer32"
_ConfigNetworkClockSource_Object = MibScalar
configNetworkClockSource = _ConfigNetworkClockSource_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 2, 1),
    _ConfigNetworkClockSource_Type()
)
configNetworkClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNetworkClockSource.setStatus("mandatory")
_ConfigNetworkClockEPortIndex_Type = Integer32
_ConfigNetworkClockEPortIndex_Object = MibScalar
configNetworkClockEPortIndex = _ConfigNetworkClockEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 2, 2),
    _ConfigNetworkClockEPortIndex_Type()
)
configNetworkClockEPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNetworkClockEPortIndex.setStatus("mandatory")
_ConfigLane_ObjectIdentity = ObjectIdentity
configLane = _ConfigLane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 3)
)


class _ConfigLaneControlAdminStatus_Type(Integer32):
    """Custom type configLaneControlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigLaneControlAdminStatus_Type.__name__ = "Integer32"
_ConfigLaneControlAdminStatus_Object = MibScalar
configLaneControlAdminStatus = _ConfigLaneControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 3, 1),
    _ConfigLaneControlAdminStatus_Type()
)
configLaneControlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLaneControlAdminStatus.setStatus("mandatory")


class _ConfigLaneControlLecsAdminStatus_Type(Integer32):
    """Custom type configLaneControlLecsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigLaneControlLecsAdminStatus_Type.__name__ = "Integer32"
_ConfigLaneControlLecsAdminStatus_Object = MibScalar
configLaneControlLecsAdminStatus = _ConfigLaneControlLecsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 3, 2),
    _ConfigLaneControlLecsAdminStatus_Type()
)
configLaneControlLecsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLaneControlLecsAdminStatus.setStatus("mandatory")


class _ConfigLaneControlLesBusAdminStatus_Type(Integer32):
    """Custom type configLaneControlLesBusAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigLaneControlLesBusAdminStatus_Type.__name__ = "Integer32"
_ConfigLaneControlLesBusAdminStatus_Object = MibScalar
configLaneControlLesBusAdminStatus = _ConfigLaneControlLesBusAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 3, 3),
    _ConfigLaneControlLesBusAdminStatus_Type()
)
configLaneControlLesBusAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLaneControlLesBusAdminStatus.setStatus("mandatory")
_ConfigMonitoring_ObjectIdentity = ObjectIdentity
configMonitoring = _ConfigMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 4)
)


class _ConfigMonitorEPortAdminStatus_Type(Integer32):
    """Custom type configMonitorEPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigMonitorEPortAdminStatus_Type.__name__ = "Integer32"
_ConfigMonitorEPortAdminStatus_Object = MibScalar
configMonitorEPortAdminStatus = _ConfigMonitorEPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 4, 1),
    _ConfigMonitorEPortAdminStatus_Type()
)
configMonitorEPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMonitorEPortAdminStatus.setStatus("mandatory")


class _ConfigMonitorEPortIPortSlotIndex_Type(Integer32):
    """Custom type configMonitorEPortIPortSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ConfigMonitorEPortIPortSlotIndex_Type.__name__ = "Integer32"
_ConfigMonitorEPortIPortSlotIndex_Object = MibScalar
configMonitorEPortIPortSlotIndex = _ConfigMonitorEPortIPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 4, 2),
    _ConfigMonitorEPortIPortSlotIndex_Type()
)
configMonitorEPortIPortSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMonitorEPortIPortSlotIndex.setStatus("mandatory")


class _ConfigMonitorEPortIPortRIndex_Type(Integer32):
    """Custom type configMonitorEPortIPortRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ConfigMonitorEPortIPortRIndex_Type.__name__ = "Integer32"
_ConfigMonitorEPortIPortRIndex_Object = MibScalar
configMonitorEPortIPortRIndex = _ConfigMonitorEPortIPortRIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 4, 3),
    _ConfigMonitorEPortIPortRIndex_Type()
)
configMonitorEPortIPortRIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMonitorEPortIPortRIndex.setStatus("mandatory")


class _ConfigMonitorEPortDirection_Type(Integer32):
    """Custom type configMonitorEPortDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_ConfigMonitorEPortDirection_Type.__name__ = "Integer32"
_ConfigMonitorEPortDirection_Object = MibScalar
configMonitorEPortDirection = _ConfigMonitorEPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 4, 4),
    _ConfigMonitorEPortDirection_Type()
)
configMonitorEPortDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMonitorEPortDirection.setStatus("mandatory")
_ConfigTm_ObjectIdentity = ObjectIdentity
configTm = _ConfigTm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6)
)


class _ConfigTmControlMode_Type(Integer32):
    """Custom type configTmControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("efci", 1),
          ("er", 2),
          ("none", 3))
    )


_ConfigTmControlMode_Type.__name__ = "Integer32"
_ConfigTmControlMode_Object = MibScalar
configTmControlMode = _ConfigTmControlMode_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 1),
    _ConfigTmControlMode_Type()
)
configTmControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlMode.setStatus("mandatory")


class _ConfigTmControlEarlyPacketDiscardAdminStatus_Type(Integer32):
    """Custom type configTmControlEarlyPacketDiscardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigTmControlEarlyPacketDiscardAdminStatus_Type.__name__ = "Integer32"
_ConfigTmControlEarlyPacketDiscardAdminStatus_Object = MibScalar
configTmControlEarlyPacketDiscardAdminStatus = _ConfigTmControlEarlyPacketDiscardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 2),
    _ConfigTmControlEarlyPacketDiscardAdminStatus_Type()
)
configTmControlEarlyPacketDiscardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlEarlyPacketDiscardAdminStatus.setStatus("mandatory")


class _ConfigTmControlVbrTrafficAllocation_Type(Integer32):
    """Custom type configTmControlVbrTrafficAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overSubscribe", 2),
          ("strictAllocation", 1))
    )


_ConfigTmControlVbrTrafficAllocation_Type.__name__ = "Integer32"
_ConfigTmControlVbrTrafficAllocation_Object = MibScalar
configTmControlVbrTrafficAllocation = _ConfigTmControlVbrTrafficAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 3),
    _ConfigTmControlVbrTrafficAllocation_Type()
)
configTmControlVbrTrafficAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlVbrTrafficAllocation.setStatus("mandatory")
_ConfigTmControlErTuningAlpha_Type = Integer32
_ConfigTmControlErTuningAlpha_Object = MibScalar
configTmControlErTuningAlpha = _ConfigTmControlErTuningAlpha_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 4),
    _ConfigTmControlErTuningAlpha_Type()
)
configTmControlErTuningAlpha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlErTuningAlpha.setStatus("mandatory")
_ConfigTmControlErTuningBeta_Type = Integer32
_ConfigTmControlErTuningBeta_Object = MibScalar
configTmControlErTuningBeta = _ConfigTmControlErTuningBeta_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 5),
    _ConfigTmControlErTuningBeta_Type()
)
configTmControlErTuningBeta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlErTuningBeta.setStatus("mandatory")
_ConfigTmControlErTuningGamma_Type = Integer32
_ConfigTmControlErTuningGamma_Object = MibScalar
configTmControlErTuningGamma = _ConfigTmControlErTuningGamma_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 6),
    _ConfigTmControlErTuningGamma_Type()
)
configTmControlErTuningGamma.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlErTuningGamma.setStatus("mandatory")
_ConfigTmControlErTuningDelta_Type = Integer32
_ConfigTmControlErTuningDelta_Object = MibScalar
configTmControlErTuningDelta = _ConfigTmControlErTuningDelta_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 7),
    _ConfigTmControlErTuningDelta_Type()
)
configTmControlErTuningDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlErTuningDelta.setStatus("mandatory")
_ConfigTmControlErTuningLambda_Type = Integer32
_ConfigTmControlErTuningLambda_Object = MibScalar
configTmControlErTuningLambda = _ConfigTmControlErTuningLambda_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 8),
    _ConfigTmControlErTuningLambda_Type()
)
configTmControlErTuningLambda.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlErTuningLambda.setStatus("mandatory")
_ConfigTmControlErTuningTau_Type = Integer32
_ConfigTmControlErTuningTau_Object = MibScalar
configTmControlErTuningTau = _ConfigTmControlErTuningTau_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 9),
    _ConfigTmControlErTuningTau_Type()
)
configTmControlErTuningTau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlErTuningTau.setStatus("mandatory")
_ConfigTmControlErTuningPhi_Type = Integer32
_ConfigTmControlErTuningPhi_Object = MibScalar
configTmControlErTuningPhi = _ConfigTmControlErTuningPhi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 10),
    _ConfigTmControlErTuningPhi_Type()
)
configTmControlErTuningPhi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlErTuningPhi.setStatus("mandatory")
_ConfigTmControlErTuningPsi_Type = Integer32
_ConfigTmControlErTuningPsi_Object = MibScalar
configTmControlErTuningPsi = _ConfigTmControlErTuningPsi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 11),
    _ConfigTmControlErTuningPsi_Type()
)
configTmControlErTuningPsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmControlErTuningPsi.setStatus("mandatory")
_ConfigTmServiceClassMapTable_Object = MibTable
configTmServiceClassMapTable = _ConfigTmServiceClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 12)
)
if mibBuilder.loadTexts:
    configTmServiceClassMapTable.setStatus("mandatory")
_ConfigTmServiceClassMapEntry_Object = MibTableRow
configTmServiceClassMapEntry = _ConfigTmServiceClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 12, 1)
)
configTmServiceClassMapEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configTmServiceClassMapServiceClass"),
)
if mibBuilder.loadTexts:
    configTmServiceClassMapEntry.setStatus("mandatory")


class _ConfigTmServiceClassMapServiceClass_Type(Integer32):
    """Custom type configTmServiceClassMapServiceClass based on Integer32"""
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
        *(("abr", 5),
          ("cbr", 2),
          ("nrtVbr", 4),
          ("other", 1),
          ("rtVbr", 3),
          ("ubr", 6))
    )


_ConfigTmServiceClassMapServiceClass_Type.__name__ = "Integer32"
_ConfigTmServiceClassMapServiceClass_Object = MibTableColumn
configTmServiceClassMapServiceClass = _ConfigTmServiceClassMapServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 12, 1, 1),
    _ConfigTmServiceClassMapServiceClass_Type()
)
configTmServiceClassMapServiceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTmServiceClassMapServiceClass.setStatus("mandatory")


class _ConfigTmServiceClassMapSchedulingQueue_Type(Integer32):
    """Custom type configTmServiceClassMapSchedulingQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ConfigTmServiceClassMapSchedulingQueue_Type.__name__ = "Integer32"
_ConfigTmServiceClassMapSchedulingQueue_Object = MibTableColumn
configTmServiceClassMapSchedulingQueue = _ConfigTmServiceClassMapSchedulingQueue_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 6, 12, 1, 2),
    _ConfigTmServiceClassMapSchedulingQueue_Type()
)
configTmServiceClassMapSchedulingQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTmServiceClassMapSchedulingQueue.setStatus("mandatory")
_ConfigTrafficDescr_ObjectIdentity = ObjectIdentity
configTrafficDescr = _ConfigTrafficDescr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7)
)
_TrafficDescriptorTableNextIndex_Type = Integer32
_TrafficDescriptorTableNextIndex_Object = MibScalar
trafficDescriptorTableNextIndex = _TrafficDescriptorTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 1),
    _TrafficDescriptorTableNextIndex_Type()
)
trafficDescriptorTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficDescriptorTableNextIndex.setStatus("mandatory")
_TrafficDescriptorTable_Object = MibTable
trafficDescriptorTable = _TrafficDescriptorTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2)
)
if mibBuilder.loadTexts:
    trafficDescriptorTable.setStatus("mandatory")
_TrafficDescriptorEntry_Object = MibTableRow
trafficDescriptorEntry = _TrafficDescriptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1)
)
trafficDescriptorEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "trafficDescriptorIndex"),
)
if mibBuilder.loadTexts:
    trafficDescriptorEntry.setStatus("mandatory")
_TrafficDescriptorIndex_Type = Integer32
_TrafficDescriptorIndex_Object = MibTableColumn
trafficDescriptorIndex = _TrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 1),
    _TrafficDescriptorIndex_Type()
)
trafficDescriptorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficDescriptorIndex.setStatus("mandatory")


class _TrafficDescriptorCreationMode_Type(Integer32):
    """Custom type trafficDescriptorCreationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("management", 2),
          ("switchedConnection", 1))
    )


_TrafficDescriptorCreationMode_Type.__name__ = "Integer32"
_TrafficDescriptorCreationMode_Object = MibTableColumn
trafficDescriptorCreationMode = _TrafficDescriptorCreationMode_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 2),
    _TrafficDescriptorCreationMode_Type()
)
trafficDescriptorCreationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficDescriptorCreationMode.setStatus("mandatory")


class _TrafficDescriptorServiceClass_Type(Integer32):
    """Custom type trafficDescriptorServiceClass based on Integer32"""
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
        *(("abr", 5),
          ("cbr", 2),
          ("nrtVbr", 4),
          ("other", 1),
          ("rtVbr", 3),
          ("ubr", 6))
    )


_TrafficDescriptorServiceClass_Type.__name__ = "Integer32"
_TrafficDescriptorServiceClass_Object = MibTableColumn
trafficDescriptorServiceClass = _TrafficDescriptorServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 3),
    _TrafficDescriptorServiceClass_Type()
)
trafficDescriptorServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorServiceClass.setStatus("mandatory")
_TrafficDescriptorPcr01_Type = Integer32
_TrafficDescriptorPcr01_Object = MibTableColumn
trafficDescriptorPcr01 = _TrafficDescriptorPcr01_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 4),
    _TrafficDescriptorPcr01_Type()
)
trafficDescriptorPcr01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorPcr01.setStatus("mandatory")
_TrafficDescriptorPcr0_Type = Integer32
_TrafficDescriptorPcr0_Object = MibTableColumn
trafficDescriptorPcr0 = _TrafficDescriptorPcr0_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 5),
    _TrafficDescriptorPcr0_Type()
)
trafficDescriptorPcr0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorPcr0.setStatus("mandatory")
_TrafficDescriptorScr01_Type = Integer32
_TrafficDescriptorScr01_Object = MibTableColumn
trafficDescriptorScr01 = _TrafficDescriptorScr01_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 6),
    _TrafficDescriptorScr01_Type()
)
trafficDescriptorScr01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorScr01.setStatus("mandatory")
_TrafficDescriptorScr0_Type = Integer32
_TrafficDescriptorScr0_Object = MibTableColumn
trafficDescriptorScr0 = _TrafficDescriptorScr0_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 7),
    _TrafficDescriptorScr0_Type()
)
trafficDescriptorScr0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorScr0.setStatus("mandatory")
_TrafficDescriptorMbs01_Type = Integer32
_TrafficDescriptorMbs01_Object = MibTableColumn
trafficDescriptorMbs01 = _TrafficDescriptorMbs01_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 8),
    _TrafficDescriptorMbs01_Type()
)
trafficDescriptorMbs01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorMbs01.setStatus("mandatory")
_TrafficDescriptorMbs0_Type = Integer32
_TrafficDescriptorMbs0_Object = MibTableColumn
trafficDescriptorMbs0 = _TrafficDescriptorMbs0_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 9),
    _TrafficDescriptorMbs0_Type()
)
trafficDescriptorMbs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorMbs0.setStatus("mandatory")


class _TrafficDescriptorTaggingFlag_Type(Integer32):
    """Custom type trafficDescriptorTaggingFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTagging", 1),
          ("tagging", 2))
    )


_TrafficDescriptorTaggingFlag_Type.__name__ = "Integer32"
_TrafficDescriptorTaggingFlag_Object = MibTableColumn
trafficDescriptorTaggingFlag = _TrafficDescriptorTaggingFlag_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 10),
    _TrafficDescriptorTaggingFlag_Type()
)
trafficDescriptorTaggingFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorTaggingFlag.setStatus("mandatory")


class _TrafficDescriptorFrameDiscardFlag_Type(Integer32):
    """Custom type trafficDescriptorFrameDiscardFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("noDiscard", 1))
    )


_TrafficDescriptorFrameDiscardFlag_Type.__name__ = "Integer32"
_TrafficDescriptorFrameDiscardFlag_Object = MibTableColumn
trafficDescriptorFrameDiscardFlag = _TrafficDescriptorFrameDiscardFlag_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 11),
    _TrafficDescriptorFrameDiscardFlag_Type()
)
trafficDescriptorFrameDiscardFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorFrameDiscardFlag.setStatus("mandatory")


class _TrafficDescriptorBestEffortFlag_Type(Integer32):
    """Custom type trafficDescriptorBestEffortFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 2),
          ("noBestEffort", 1))
    )


_TrafficDescriptorBestEffortFlag_Type.__name__ = "Integer32"
_TrafficDescriptorBestEffortFlag_Object = MibTableColumn
trafficDescriptorBestEffortFlag = _TrafficDescriptorBestEffortFlag_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 12),
    _TrafficDescriptorBestEffortFlag_Type()
)
trafficDescriptorBestEffortFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorBestEffortFlag.setStatus("mandatory")
_TrafficDescriptorMcr_Type = Integer32
_TrafficDescriptorMcr_Object = MibTableColumn
trafficDescriptorMcr = _TrafficDescriptorMcr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 13),
    _TrafficDescriptorMcr_Type()
)
trafficDescriptorMcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorMcr.setStatus("mandatory")
_TrafficDescriptorAbrIcr_Type = Integer32
_TrafficDescriptorAbrIcr_Object = MibTableColumn
trafficDescriptorAbrIcr = _TrafficDescriptorAbrIcr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 14),
    _TrafficDescriptorAbrIcr_Type()
)
trafficDescriptorAbrIcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorAbrIcr.setStatus("mandatory")
_TrafficDescriptorAbrTbe_Type = Integer32
_TrafficDescriptorAbrTbe_Object = MibTableColumn
trafficDescriptorAbrTbe = _TrafficDescriptorAbrTbe_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 15),
    _TrafficDescriptorAbrTbe_Type()
)
trafficDescriptorAbrTbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorAbrTbe.setStatus("mandatory")
_TrafficDescriptorAbrFrtt_Type = Integer32
_TrafficDescriptorAbrFrtt_Object = MibTableColumn
trafficDescriptorAbrFrtt = _TrafficDescriptorAbrFrtt_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 16),
    _TrafficDescriptorAbrFrtt_Type()
)
trafficDescriptorAbrFrtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorAbrFrtt.setStatus("mandatory")


class _TrafficDescriptorAbrRif_Type(Integer32):
    """Custom type trafficDescriptorAbrRif based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("rifOne", 16),
          ("rifOneOver1024", 6),
          ("rifOneOver128", 9),
          ("rifOneOver16", 12),
          ("rifOneOver16384", 2),
          ("rifOneOver2", 15),
          ("rifOneOver2048", 5),
          ("rifOneOver256", 8),
          ("rifOneOver32", 11),
          ("rifOneOver32768", 1),
          ("rifOneOver4", 14),
          ("rifOneOver4096", 4),
          ("rifOneOver512", 7),
          ("rifOneOver64", 10),
          ("rifOneOver8", 13),
          ("rifOneOver8192", 3))
    )


_TrafficDescriptorAbrRif_Type.__name__ = "Integer32"
_TrafficDescriptorAbrRif_Object = MibTableColumn
trafficDescriptorAbrRif = _TrafficDescriptorAbrRif_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 17),
    _TrafficDescriptorAbrRif_Type()
)
trafficDescriptorAbrRif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorAbrRif.setStatus("mandatory")


class _TrafficDescriptorAbrRdf_Type(Integer32):
    """Custom type trafficDescriptorAbrRdf based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("rdfOne", 16),
          ("rdfOneOver1024", 6),
          ("rdfOneOver128", 9),
          ("rdfOneOver16", 12),
          ("rdfOneOver16384", 2),
          ("rdfOneOver2", 15),
          ("rdfOneOver2048", 5),
          ("rdfOneOver256", 8),
          ("rdfOneOver32", 11),
          ("rdfOneOver32768", 1),
          ("rdfOneOver4", 14),
          ("rdfOneOver4096", 4),
          ("rdfOneOver512", 7),
          ("rdfOneOver64", 10),
          ("rdfOneOver8", 13),
          ("rdfOneOver8192", 3))
    )


_TrafficDescriptorAbrRdf_Type.__name__ = "Integer32"
_TrafficDescriptorAbrRdf_Object = MibTableColumn
trafficDescriptorAbrRdf = _TrafficDescriptorAbrRdf_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 18),
    _TrafficDescriptorAbrRdf_Type()
)
trafficDescriptorAbrRdf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorAbrRdf.setStatus("mandatory")


class _TrafficDescriptorAbrNrm_Type(Integer32):
    """Custom type trafficDescriptorAbrNrm based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("nrm128", 7),
          ("nrm16", 4),
          ("nrm2", 1),
          ("nrm256", 8),
          ("nrm32", 5),
          ("nrm4", 2),
          ("nrm64", 6),
          ("nrm8", 3))
    )


_TrafficDescriptorAbrNrm_Type.__name__ = "Integer32"
_TrafficDescriptorAbrNrm_Object = MibTableColumn
trafficDescriptorAbrNrm = _TrafficDescriptorAbrNrm_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 19),
    _TrafficDescriptorAbrNrm_Type()
)
trafficDescriptorAbrNrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorAbrNrm.setStatus("mandatory")


class _TrafficDescriptorAbrTrm_Type(Integer32):
    """Custom type trafficDescriptorAbrTrm based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("trm0Point78125", 1),
          ("trm100", 8),
          ("trm12Point5", 5),
          ("trm1Point5625", 2),
          ("trm25", 6),
          ("trm3Point125", 3),
          ("trm50", 7),
          ("trm6Point25", 4))
    )


_TrafficDescriptorAbrTrm_Type.__name__ = "Integer32"
_TrafficDescriptorAbrTrm_Object = MibTableColumn
trafficDescriptorAbrTrm = _TrafficDescriptorAbrTrm_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 20),
    _TrafficDescriptorAbrTrm_Type()
)
trafficDescriptorAbrTrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorAbrTrm.setStatus("mandatory")


class _TrafficDescriptorAbrCdf_Type(Integer32):
    """Custom type trafficDescriptorAbrCdf based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cdf0", 1),
          ("cdfOne", 8),
          ("cdfOneOver16", 4),
          ("cdfOneOver2", 7),
          ("cdfOneOver32", 3),
          ("cdfOneOver4", 6),
          ("cdfOneOver64", 2),
          ("cdfOneOver8", 5))
    )


_TrafficDescriptorAbrCdf_Type.__name__ = "Integer32"
_TrafficDescriptorAbrCdf_Object = MibTableColumn
trafficDescriptorAbrCdf = _TrafficDescriptorAbrCdf_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 21),
    _TrafficDescriptorAbrCdf_Type()
)
trafficDescriptorAbrCdf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorAbrCdf.setStatus("mandatory")
_TrafficDescriptorAbrAdtf_Type = Integer32
_TrafficDescriptorAbrAdtf_Object = MibTableColumn
trafficDescriptorAbrAdtf = _TrafficDescriptorAbrAdtf_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 22),
    _TrafficDescriptorAbrAdtf_Type()
)
trafficDescriptorAbrAdtf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorAbrAdtf.setStatus("mandatory")


class _TrafficDescriptorTrafficType_Type(Integer32):
    """Custom type trafficDescriptorTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TrafficDescriptorTrafficType_Type.__name__ = "Integer32"
_TrafficDescriptorTrafficType_Object = MibTableColumn
trafficDescriptorTrafficType = _TrafficDescriptorTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 23),
    _TrafficDescriptorTrafficType_Type()
)
trafficDescriptorTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficDescriptorTrafficType.setStatus("mandatory")


class _TrafficDescriptorRowStatus_Type(Integer32):
    """Custom type trafficDescriptorRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_TrafficDescriptorRowStatus_Type.__name__ = "Integer32"
_TrafficDescriptorRowStatus_Object = MibTableColumn
trafficDescriptorRowStatus = _TrafficDescriptorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 24),
    _TrafficDescriptorRowStatus_Type()
)
trafficDescriptorRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorRowStatus.setStatus("mandatory")
_TrafficDescriptorCtd_Type = Integer32
_TrafficDescriptorCtd_Object = MibTableColumn
trafficDescriptorCtd = _TrafficDescriptorCtd_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 25),
    _TrafficDescriptorCtd_Type()
)
trafficDescriptorCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorCtd.setStatus("mandatory")
_TrafficDescriptorCdv_Type = Integer32
_TrafficDescriptorCdv_Object = MibTableColumn
trafficDescriptorCdv = _TrafficDescriptorCdv_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 26),
    _TrafficDescriptorCdv_Type()
)
trafficDescriptorCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorCdv.setStatus("mandatory")
_TrafficDescriptorLogClr_Type = Integer32
_TrafficDescriptorLogClr_Object = MibTableColumn
trafficDescriptorLogClr = _TrafficDescriptorLogClr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 7, 2, 1, 27),
    _TrafficDescriptorLogClr_Type()
)
trafficDescriptorLogClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficDescriptorLogClr.setStatus("mandatory")
_ConfigServiceReg_ObjectIdentity = ObjectIdentity
configServiceReg = _ConfigServiceReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 8)
)
_ConfigIlmiServiceRegistryTable_Object = MibTable
configIlmiServiceRegistryTable = _ConfigIlmiServiceRegistryTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 8, 1)
)
if mibBuilder.loadTexts:
    configIlmiServiceRegistryTable.setStatus("mandatory")
_ConfigIlmiServiceRegistryEntry_Object = MibTableRow
configIlmiServiceRegistryEntry = _ConfigIlmiServiceRegistryEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 8, 1, 1)
)
configIlmiServiceRegistryEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configIlmiServiceRegistryServiceId"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "configIlmiServiceRegistryAddressIndex"),
)
if mibBuilder.loadTexts:
    configIlmiServiceRegistryEntry.setStatus("mandatory")
_ConfigIlmiServiceRegistryAddressIndex_Type = Integer32
_ConfigIlmiServiceRegistryAddressIndex_Object = MibTableColumn
configIlmiServiceRegistryAddressIndex = _ConfigIlmiServiceRegistryAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 8, 1, 1, 1),
    _ConfigIlmiServiceRegistryAddressIndex_Type()
)
configIlmiServiceRegistryAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIlmiServiceRegistryAddressIndex.setStatus("mandatory")
_ConfigIlmiServiceRegistryServiceId_Type = ObjectIdentifier
_ConfigIlmiServiceRegistryServiceId_Object = MibTableColumn
configIlmiServiceRegistryServiceId = _ConfigIlmiServiceRegistryServiceId_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 8, 1, 1, 2),
    _ConfigIlmiServiceRegistryServiceId_Type()
)
configIlmiServiceRegistryServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIlmiServiceRegistryServiceId.setStatus("mandatory")
_ConfigIlmiServiceRegistryAtmAddress_Type = AtmAddress
_ConfigIlmiServiceRegistryAtmAddress_Object = MibTableColumn
configIlmiServiceRegistryAtmAddress = _ConfigIlmiServiceRegistryAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 8, 1, 1, 3),
    _ConfigIlmiServiceRegistryAtmAddress_Type()
)
configIlmiServiceRegistryAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIlmiServiceRegistryAtmAddress.setStatus("mandatory")


class _ConfigIlmiServiceRegistryParm1_Type(OctetString):
    """Custom type configIlmiServiceRegistryParm1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ConfigIlmiServiceRegistryParm1_Type.__name__ = "OctetString"
_ConfigIlmiServiceRegistryParm1_Object = MibTableColumn
configIlmiServiceRegistryParm1 = _ConfigIlmiServiceRegistryParm1_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 8, 1, 1, 4),
    _ConfigIlmiServiceRegistryParm1_Type()
)
configIlmiServiceRegistryParm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIlmiServiceRegistryParm1.setStatus("mandatory")


class _ConfigIlmiServiceRegistryRowStatus_Type(Integer32):
    """Custom type configIlmiServiceRegistryRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ConfigIlmiServiceRegistryRowStatus_Type.__name__ = "Integer32"
_ConfigIlmiServiceRegistryRowStatus_Object = MibTableColumn
configIlmiServiceRegistryRowStatus = _ConfigIlmiServiceRegistryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 8, 1, 1, 5),
    _ConfigIlmiServiceRegistryRowStatus_Type()
)
configIlmiServiceRegistryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIlmiServiceRegistryRowStatus.setStatus("mandatory")
_ConfigSar_ObjectIdentity = ObjectIdentity
configSar = _ConfigSar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 9)
)


class _ConfigSarMuxFillThreshold_Type(Integer32):
    """Custom type configSarMuxFillThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_ConfigSarMuxFillThreshold_Type.__name__ = "Integer32"
_ConfigSarMuxFillThreshold_Object = MibScalar
configSarMuxFillThreshold = _ConfigSarMuxFillThreshold_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 9, 1),
    _ConfigSarMuxFillThreshold_Type()
)
configSarMuxFillThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSarMuxFillThreshold.setStatus("mandatory")


class _ConfigSarMuxSarVpi_Type(Integer32):
    """Custom type configSarMuxSarVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigSarMuxSarVpi_Type.__name__ = "Integer32"
_ConfigSarMuxSarVpi_Object = MibScalar
configSarMuxSarVpi = _ConfigSarMuxSarVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 9, 2),
    _ConfigSarMuxSarVpi_Type()
)
configSarMuxSarVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSarMuxSarVpi.setStatus("mandatory")


class _ConfigSarEmptyCellHandling_Type(Integer32):
    """Custom type configSarEmptyCellHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("unassigned", 2))
    )


_ConfigSarEmptyCellHandling_Type.__name__ = "Integer32"
_ConfigSarEmptyCellHandling_Object = MibScalar
configSarEmptyCellHandling = _ConfigSarEmptyCellHandling_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 9, 3),
    _ConfigSarEmptyCellHandling_Type()
)
configSarEmptyCellHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSarEmptyCellHandling.setStatus("mandatory")
_ConfigXModule_ObjectIdentity = ObjectIdentity
configXModule = _ConfigXModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 10)
)
_ConfigXModuleTable_Object = MibTable
configXModuleTable = _ConfigXModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 10, 1)
)
if mibBuilder.loadTexts:
    configXModuleTable.setStatus("mandatory")
_ConfigXModuleEntry_Object = MibTableRow
configXModuleEntry = _ConfigXModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 10, 1, 1)
)
configXModuleEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configXModuleSlotIndex"),
)
if mibBuilder.loadTexts:
    configXModuleEntry.setStatus("mandatory")


class _ConfigXModuleSlotIndex_Type(Integer32):
    """Custom type configXModuleSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ConfigXModuleSlotIndex_Type.__name__ = "Integer32"
_ConfigXModuleSlotIndex_Object = MibTableColumn
configXModuleSlotIndex = _ConfigXModuleSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 10, 1, 1, 1),
    _ConfigXModuleSlotIndex_Type()
)
configXModuleSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configXModuleSlotIndex.setStatus("mandatory")


class _ConfigXModuleAdminStatus_Type(Integer32):
    """Custom type configXModuleAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("reset", 3),
          ("up", 1))
    )


_ConfigXModuleAdminStatus_Type.__name__ = "Integer32"
_ConfigXModuleAdminStatus_Object = MibTableColumn
configXModuleAdminStatus = _ConfigXModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 10, 1, 1, 2),
    _ConfigXModuleAdminStatus_Type()
)
configXModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configXModuleAdminStatus.setStatus("mandatory")
_ConfigFeatureModule_ObjectIdentity = ObjectIdentity
configFeatureModule = _ConfigFeatureModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 11)
)


class _ConfigFeatureModuleAdminStatus_Type(Integer32):
    """Custom type configFeatureModuleAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigFeatureModuleAdminStatus_Type.__name__ = "Integer32"
_ConfigFeatureModuleAdminStatus_Object = MibScalar
configFeatureModuleAdminStatus = _ConfigFeatureModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 11, 1),
    _ConfigFeatureModuleAdminStatus_Type()
)
configFeatureModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFeatureModuleAdminStatus.setStatus("mandatory")
_ConfigCommonEPort_ObjectIdentity = ObjectIdentity
configCommonEPort = _ConfigCommonEPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12)
)


class _ConfigCommonEPortIlmiAdminStatus_Type(Integer32):
    """Custom type configCommonEPortIlmiAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("off", 3))
    )


_ConfigCommonEPortIlmiAdminStatus_Type.__name__ = "Integer32"
_ConfigCommonEPortIlmiAdminStatus_Object = MibScalar
configCommonEPortIlmiAdminStatus = _ConfigCommonEPortIlmiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 1),
    _ConfigCommonEPortIlmiAdminStatus_Type()
)
configCommonEPortIlmiAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortIlmiAdminStatus.setStatus("mandatory")


class _ConfigCommonEPortAddrRegistrationAdminStatus_Type(Integer32):
    """Custom type configCommonEPortAddrRegistrationAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_ConfigCommonEPortAddrRegistrationAdminStatus_Type.__name__ = "Integer32"
_ConfigCommonEPortAddrRegistrationAdminStatus_Object = MibScalar
configCommonEPortAddrRegistrationAdminStatus = _ConfigCommonEPortAddrRegistrationAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 2),
    _ConfigCommonEPortAddrRegistrationAdminStatus_Type()
)
configCommonEPortAddrRegistrationAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortAddrRegistrationAdminStatus.setStatus("mandatory")


class _ConfigCommonEPortMaxVpcs_Type(Integer32):
    """Custom type configCommonEPortMaxVpcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigCommonEPortMaxVpcs_Type.__name__ = "Integer32"
_ConfigCommonEPortMaxVpcs_Object = MibScalar
configCommonEPortMaxVpcs = _ConfigCommonEPortMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 3),
    _ConfigCommonEPortMaxVpcs_Type()
)
configCommonEPortMaxVpcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortMaxVpcs.setStatus("mandatory")


class _ConfigCommonEPortMaxVccs_Type(Integer32):
    """Custom type configCommonEPortMaxVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_ConfigCommonEPortMaxVccs_Type.__name__ = "Integer32"
_ConfigCommonEPortMaxVccs_Object = MibScalar
configCommonEPortMaxVccs = _ConfigCommonEPortMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 4),
    _ConfigCommonEPortMaxVccs_Type()
)
configCommonEPortMaxVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortMaxVccs.setStatus("mandatory")


class _ConfigCommonEPortMaxVpiBits_Type(Integer32):
    """Custom type configCommonEPortMaxVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ConfigCommonEPortMaxVpiBits_Type.__name__ = "Integer32"
_ConfigCommonEPortMaxVpiBits_Object = MibScalar
configCommonEPortMaxVpiBits = _ConfigCommonEPortMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 5),
    _ConfigCommonEPortMaxVpiBits_Type()
)
configCommonEPortMaxVpiBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortMaxVpiBits.setStatus("mandatory")


class _ConfigCommonEPortMaxVciBits_Type(Integer32):
    """Custom type configCommonEPortMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ConfigCommonEPortMaxVciBits_Type.__name__ = "Integer32"
_ConfigCommonEPortMaxVciBits_Object = MibScalar
configCommonEPortMaxVciBits = _ConfigCommonEPortMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 6),
    _ConfigCommonEPortMaxVciBits_Type()
)
configCommonEPortMaxVciBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortMaxVciBits.setStatus("mandatory")


class _ConfigCommonEPortUniType_Type(Integer32):
    """Custom type configCommonEPortUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_ConfigCommonEPortUniType_Type.__name__ = "Integer32"
_ConfigCommonEPortUniType_Object = MibScalar
configCommonEPortUniType = _ConfigCommonEPortUniType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 7),
    _ConfigCommonEPortUniType_Type()
)
configCommonEPortUniType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortUniType.setStatus("mandatory")


class _ConfigCommonEPortUniVersion_Type(Integer32):
    """Custom type configCommonEPortUniVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("version3point0", 2),
          ("version3point1", 3),
          ("version4point0", 4))
    )


_ConfigCommonEPortUniVersion_Type.__name__ = "Integer32"
_ConfigCommonEPortUniVersion_Object = MibScalar
configCommonEPortUniVersion = _ConfigCommonEPortUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 8),
    _ConfigCommonEPortUniVersion_Type()
)
configCommonEPortUniVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortUniVersion.setStatus("mandatory")


class _ConfigCommonEPortDeviceType_Type(Integer32):
    """Custom type configCommonEPortDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("user", 1))
    )


_ConfigCommonEPortDeviceType_Type.__name__ = "Integer32"
_ConfigCommonEPortDeviceType_Object = MibScalar
configCommonEPortDeviceType = _ConfigCommonEPortDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 9),
    _ConfigCommonEPortDeviceType_Type()
)
configCommonEPortDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortDeviceType.setStatus("mandatory")


class _ConfigCommonEPortIlmiVersion_Type(Integer32):
    """Custom type configCommonEPortIlmiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("version4point0", 2))
    )


_ConfigCommonEPortIlmiVersion_Type.__name__ = "Integer32"
_ConfigCommonEPortIlmiVersion_Object = MibScalar
configCommonEPortIlmiVersion = _ConfigCommonEPortIlmiVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 10),
    _ConfigCommonEPortIlmiVersion_Type()
)
configCommonEPortIlmiVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortIlmiVersion.setStatus("mandatory")


class _ConfigCommonEPortNniSigVersion_Type(Integer32):
    """Custom type configCommonEPortNniSigVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 2),
          ("pnniVersion1point0", 3),
          ("unsupported", 1))
    )


_ConfigCommonEPortNniSigVersion_Type.__name__ = "Integer32"
_ConfigCommonEPortNniSigVersion_Object = MibScalar
configCommonEPortNniSigVersion = _ConfigCommonEPortNniSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 11),
    _ConfigCommonEPortNniSigVersion_Type()
)
configCommonEPortNniSigVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortNniSigVersion.setStatus("mandatory")


class _ConfigCommonEPortSignallingVpi_Type(Integer32):
    """Custom type configCommonEPortSignallingVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigCommonEPortSignallingVpi_Type.__name__ = "Integer32"
_ConfigCommonEPortSignallingVpi_Object = MibScalar
configCommonEPortSignallingVpi = _ConfigCommonEPortSignallingVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 12),
    _ConfigCommonEPortSignallingVpi_Type()
)
configCommonEPortSignallingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortSignallingVpi.setStatus("mandatory")


class _ConfigCommonEPortSignallingVci_Type(Integer32):
    """Custom type configCommonEPortSignallingVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigCommonEPortSignallingVci_Type.__name__ = "Integer32"
_ConfigCommonEPortSignallingVci_Object = MibScalar
configCommonEPortSignallingVci = _ConfigCommonEPortSignallingVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 13),
    _ConfigCommonEPortSignallingVci_Type()
)
configCommonEPortSignallingVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortSignallingVci.setStatus("mandatory")


class _ConfigCommonEPortIlmiVpi_Type(Integer32):
    """Custom type configCommonEPortIlmiVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigCommonEPortIlmiVpi_Type.__name__ = "Integer32"
_ConfigCommonEPortIlmiVpi_Object = MibScalar
configCommonEPortIlmiVpi = _ConfigCommonEPortIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 14),
    _ConfigCommonEPortIlmiVpi_Type()
)
configCommonEPortIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortIlmiVpi.setStatus("mandatory")


class _ConfigCommonEPortIlmiVci_Type(Integer32):
    """Custom type configCommonEPortIlmiVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigCommonEPortIlmiVci_Type.__name__ = "Integer32"
_ConfigCommonEPortIlmiVci_Object = MibScalar
configCommonEPortIlmiVci = _ConfigCommonEPortIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 15),
    _ConfigCommonEPortIlmiVci_Type()
)
configCommonEPortIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortIlmiVci.setStatus("mandatory")


class _ConfigCommonEPortLecsVpi_Type(Integer32):
    """Custom type configCommonEPortLecsVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigCommonEPortLecsVpi_Type.__name__ = "Integer32"
_ConfigCommonEPortLecsVpi_Object = MibScalar
configCommonEPortLecsVpi = _ConfigCommonEPortLecsVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 16),
    _ConfigCommonEPortLecsVpi_Type()
)
configCommonEPortLecsVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortLecsVpi.setStatus("mandatory")


class _ConfigCommonEPortLecsVci_Type(Integer32):
    """Custom type configCommonEPortLecsVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigCommonEPortLecsVci_Type.__name__ = "Integer32"
_ConfigCommonEPortLecsVci_Object = MibScalar
configCommonEPortLecsVci = _ConfigCommonEPortLecsVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 17),
    _ConfigCommonEPortLecsVci_Type()
)
configCommonEPortLecsVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortLecsVci.setStatus("mandatory")


class _ConfigCommonEPortPnniVpi_Type(Integer32):
    """Custom type configCommonEPortPnniVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigCommonEPortPnniVpi_Type.__name__ = "Integer32"
_ConfigCommonEPortPnniVpi_Object = MibScalar
configCommonEPortPnniVpi = _ConfigCommonEPortPnniVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 18),
    _ConfigCommonEPortPnniVpi_Type()
)
configCommonEPortPnniVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortPnniVpi.setStatus("mandatory")


class _ConfigCommonEPortPnniVci_Type(Integer32):
    """Custom type configCommonEPortPnniVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigCommonEPortPnniVci_Type.__name__ = "Integer32"
_ConfigCommonEPortPnniVci_Object = MibScalar
configCommonEPortPnniVci = _ConfigCommonEPortPnniVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 19),
    _ConfigCommonEPortPnniVci_Type()
)
configCommonEPortPnniVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortPnniVci.setStatus("mandatory")


class _ConfigCommonEPortAbrBandwidthAllocation_Type(Integer32):
    """Custom type configCommonEPortAbrBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigCommonEPortAbrBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigCommonEPortAbrBandwidthAllocation_Object = MibScalar
configCommonEPortAbrBandwidthAllocation = _ConfigCommonEPortAbrBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 20),
    _ConfigCommonEPortAbrBandwidthAllocation_Type()
)
configCommonEPortAbrBandwidthAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortAbrBandwidthAllocation.setStatus("mandatory")


class _ConfigCommonEPortVbrRtBandwidthAllocation_Type(Integer32):
    """Custom type configCommonEPortVbrRtBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigCommonEPortVbrRtBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigCommonEPortVbrRtBandwidthAllocation_Object = MibScalar
configCommonEPortVbrRtBandwidthAllocation = _ConfigCommonEPortVbrRtBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 21),
    _ConfigCommonEPortVbrRtBandwidthAllocation_Type()
)
configCommonEPortVbrRtBandwidthAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortVbrRtBandwidthAllocation.setStatus("mandatory")


class _ConfigCommonEPortVbrNrtBandwidthAllocation_Type(Integer32):
    """Custom type configCommonEPortVbrNrtBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigCommonEPortVbrNrtBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigCommonEPortVbrNrtBandwidthAllocation_Object = MibScalar
configCommonEPortVbrNrtBandwidthAllocation = _ConfigCommonEPortVbrNrtBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 22),
    _ConfigCommonEPortVbrNrtBandwidthAllocation_Type()
)
configCommonEPortVbrNrtBandwidthAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortVbrNrtBandwidthAllocation.setStatus("mandatory")


class _ConfigCommonEPortCbrBandwidthAllocation_Type(Integer32):
    """Custom type configCommonEPortCbrBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigCommonEPortCbrBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigCommonEPortCbrBandwidthAllocation_Object = MibScalar
configCommonEPortCbrBandwidthAllocation = _ConfigCommonEPortCbrBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 23),
    _ConfigCommonEPortCbrBandwidthAllocation_Type()
)
configCommonEPortCbrBandwidthAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortCbrBandwidthAllocation.setStatus("mandatory")


class _ConfigStaticEPortIlmiPollFrequency_Type(Integer32):
    """Custom type configStaticEPortIlmiPollFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ConfigStaticEPortIlmiPollFrequency_Type.__name__ = "Integer32"
_ConfigStaticEPortIlmiPollFrequency_Object = MibScalar
configStaticEPortIlmiPollFrequency = _ConfigStaticEPortIlmiPollFrequency_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 24),
    _ConfigStaticEPortIlmiPollFrequency_Type()
)
configStaticEPortIlmiPollFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configStaticEPortIlmiPollFrequency.setStatus("mandatory")


class _ConfigStaticEPortIlmiPollRetries_Type(Integer32):
    """Custom type configStaticEPortIlmiPollRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ConfigStaticEPortIlmiPollRetries_Type.__name__ = "Integer32"
_ConfigStaticEPortIlmiPollRetries_Object = MibScalar
configStaticEPortIlmiPollRetries = _ConfigStaticEPortIlmiPollRetries_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 25),
    _ConfigStaticEPortIlmiPollRetries_Type()
)
configStaticEPortIlmiPollRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configStaticEPortIlmiPollRetries.setStatus("mandatory")


class _ConfigStaticEPortMaxTransientPhyFailureTime_Type(Integer32):
    """Custom type configStaticEPortMaxTransientPhyFailureTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ConfigStaticEPortMaxTransientPhyFailureTime_Type.__name__ = "Integer32"
_ConfigStaticEPortMaxTransientPhyFailureTime_Object = MibScalar
configStaticEPortMaxTransientPhyFailureTime = _ConfigStaticEPortMaxTransientPhyFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 26),
    _ConfigStaticEPortMaxTransientPhyFailureTime_Type()
)
configStaticEPortMaxTransientPhyFailureTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configStaticEPortMaxTransientPhyFailureTime.setStatus("mandatory")


class _ConfigStaticEPortMaxPhyFailuresPerMinute_Type(Integer32):
    """Custom type configStaticEPortMaxPhyFailuresPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ConfigStaticEPortMaxPhyFailuresPerMinute_Type.__name__ = "Integer32"
_ConfigStaticEPortMaxPhyFailuresPerMinute_Object = MibScalar
configStaticEPortMaxPhyFailuresPerMinute = _ConfigStaticEPortMaxPhyFailuresPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 27),
    _ConfigStaticEPortMaxPhyFailuresPerMinute_Type()
)
configStaticEPortMaxPhyFailuresPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configStaticEPortMaxPhyFailuresPerMinute.setStatus("deprecated")
_ConfigCommonEPortLinkDelay_Type = Integer32
_ConfigCommonEPortLinkDelay_Object = MibScalar
configCommonEPortLinkDelay = _ConfigCommonEPortLinkDelay_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 28),
    _ConfigCommonEPortLinkDelay_Type()
)
configCommonEPortLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortLinkDelay.setStatus("mandatory")
_ConfigCommonEPortTransientPhyOffTime_Type = Integer32
_ConfigCommonEPortTransientPhyOffTime_Object = MibScalar
configCommonEPortTransientPhyOffTime = _ConfigCommonEPortTransientPhyOffTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 29),
    _ConfigCommonEPortTransientPhyOffTime_Type()
)
configCommonEPortTransientPhyOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortTransientPhyOffTime.setStatus("deprecated")
_ConfigCommonEPortTransientPhyWindowTime_Type = Integer32
_ConfigCommonEPortTransientPhyWindowTime_Object = MibScalar
configCommonEPortTransientPhyWindowTime = _ConfigCommonEPortTransientPhyWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 30),
    _ConfigCommonEPortTransientPhyWindowTime_Type()
)
configCommonEPortTransientPhyWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortTransientPhyWindowTime.setStatus("deprecated")


class _ConfigCommonEPortTransientPhyDisconnectCount_Type(Integer32):
    """Custom type configCommonEPortTransientPhyDisconnectCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ConfigCommonEPortTransientPhyDisconnectCount_Type.__name__ = "Integer32"
_ConfigCommonEPortTransientPhyDisconnectCount_Object = MibScalar
configCommonEPortTransientPhyDisconnectCount = _ConfigCommonEPortTransientPhyDisconnectCount_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 31),
    _ConfigCommonEPortTransientPhyDisconnectCount_Type()
)
configCommonEPortTransientPhyDisconnectCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortTransientPhyDisconnectCount.setStatus("mandatory")
_ConfigCommonEPortTransientPhyDisconnectTimer_Type = Integer32
_ConfigCommonEPortTransientPhyDisconnectTimer_Object = MibScalar
configCommonEPortTransientPhyDisconnectTimer = _ConfigCommonEPortTransientPhyDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 32),
    _ConfigCommonEPortTransientPhyDisconnectTimer_Type()
)
configCommonEPortTransientPhyDisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortTransientPhyDisconnectTimer.setStatus("mandatory")


class _ConfigCommonEPortDefaultSigVersion_Type(Integer32):
    """Custom type configCommonEPortDefaultSigVersion based on Integer32"""
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
        *(("iispNetworkSide", 3),
          ("iispUserSide", 4),
          ("pnni", 2),
          ("uni", 1))
    )


_ConfigCommonEPortDefaultSigVersion_Type.__name__ = "Integer32"
_ConfigCommonEPortDefaultSigVersion_Object = MibScalar
configCommonEPortDefaultSigVersion = _ConfigCommonEPortDefaultSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 33),
    _ConfigCommonEPortDefaultSigVersion_Type()
)
configCommonEPortDefaultSigVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortDefaultSigVersion.setStatus("mandatory")


class _ConfigCommonEPortMaxSvpcVpi_Type(Integer32):
    """Custom type configCommonEPortMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ConfigCommonEPortMaxSvpcVpi_Type.__name__ = "Integer32"
_ConfigCommonEPortMaxSvpcVpi_Object = MibScalar
configCommonEPortMaxSvpcVpi = _ConfigCommonEPortMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 34),
    _ConfigCommonEPortMaxSvpcVpi_Type()
)
configCommonEPortMaxSvpcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortMaxSvpcVpi.setStatus("mandatory")


class _ConfigCommonEPortMaxSvccVpi_Type(Integer32):
    """Custom type configCommonEPortMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ConfigCommonEPortMaxSvccVpi_Type.__name__ = "Integer32"
_ConfigCommonEPortMaxSvccVpi_Object = MibScalar
configCommonEPortMaxSvccVpi = _ConfigCommonEPortMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 35),
    _ConfigCommonEPortMaxSvccVpi_Type()
)
configCommonEPortMaxSvccVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortMaxSvccVpi.setStatus("mandatory")


class _ConfigCommonEPortMinSvccVci_Type(Integer32):
    """Custom type configCommonEPortMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_ConfigCommonEPortMinSvccVci_Type.__name__ = "Integer32"
_ConfigCommonEPortMinSvccVci_Object = MibScalar
configCommonEPortMinSvccVci = _ConfigCommonEPortMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 12, 36),
    _ConfigCommonEPortMinSvccVci_Type()
)
configCommonEPortMinSvccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonEPortMinSvccVci.setStatus("mandatory")
_ConfigEPort_ObjectIdentity = ObjectIdentity
configEPort = _ConfigEPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13)
)


class _ConfigEPortScratchPadScratchPadStatus_Type(Integer32):
    """Custom type configEPortScratchPadScratchPadStatus based on Integer32"""
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
        *(("copied", 3),
          ("copy", 2),
          ("notReady", 1),
          ("updateAndGo", 4))
    )


_ConfigEPortScratchPadScratchPadStatus_Type.__name__ = "Integer32"
_ConfigEPortScratchPadScratchPadStatus_Object = MibScalar
configEPortScratchPadScratchPadStatus = _ConfigEPortScratchPadScratchPadStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 1),
    _ConfigEPortScratchPadScratchPadStatus_Type()
)
configEPortScratchPadScratchPadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadScratchPadStatus.setStatus("mandatory")
_ConfigEPortScratchPadEPortIndex_Type = Integer32
_ConfigEPortScratchPadEPortIndex_Object = MibScalar
configEPortScratchPadEPortIndex = _ConfigEPortScratchPadEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 2),
    _ConfigEPortScratchPadEPortIndex_Type()
)
configEPortScratchPadEPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadEPortIndex.setStatus("mandatory")
_ConfigEPortScratchPadIpAddress_Type = IpAddress
_ConfigEPortScratchPadIpAddress_Object = MibScalar
configEPortScratchPadIpAddress = _ConfigEPortScratchPadIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 3),
    _ConfigEPortScratchPadIpAddress_Type()
)
configEPortScratchPadIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortScratchPadIpAddress.setStatus("mandatory")


class _ConfigEPortScratchPadActionStatus_Type(Integer32):
    """Custom type configEPortScratchPadActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("notPossible", 3),
          ("ok", 1))
    )


_ConfigEPortScratchPadActionStatus_Type.__name__ = "Integer32"
_ConfigEPortScratchPadActionStatus_Object = MibScalar
configEPortScratchPadActionStatus = _ConfigEPortScratchPadActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 4),
    _ConfigEPortScratchPadActionStatus_Type()
)
configEPortScratchPadActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortScratchPadActionStatus.setStatus("mandatory")


class _ConfigEPortScratchPadHwConfigTxClocking_Type(Integer32):
    """Custom type configEPortScratchPadHwConfigTxClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("network", 1))
    )


_ConfigEPortScratchPadHwConfigTxClocking_Type.__name__ = "Integer32"
_ConfigEPortScratchPadHwConfigTxClocking_Object = MibScalar
configEPortScratchPadHwConfigTxClocking = _ConfigEPortScratchPadHwConfigTxClocking_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 5),
    _ConfigEPortScratchPadHwConfigTxClocking_Type()
)
configEPortScratchPadHwConfigTxClocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadHwConfigTxClocking.setStatus("mandatory")


class _ConfigEPortScratchPadHwConfigSonetSdh_Type(Integer32):
    """Custom type configEPortScratchPadHwConfigSonetSdh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("sdh", 2),
          ("sonet", 1))
    )


_ConfigEPortScratchPadHwConfigSonetSdh_Type.__name__ = "Integer32"
_ConfigEPortScratchPadHwConfigSonetSdh_Object = MibScalar
configEPortScratchPadHwConfigSonetSdh = _ConfigEPortScratchPadHwConfigSonetSdh_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 6),
    _ConfigEPortScratchPadHwConfigSonetSdh_Type()
)
configEPortScratchPadHwConfigSonetSdh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadHwConfigSonetSdh.setStatus("mandatory")


class _ConfigEPortScratchPadUseCommonEPortConfig_Type(Integer32):
    """Custom type configEPortScratchPadUseCommonEPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ConfigEPortScratchPadUseCommonEPortConfig_Type.__name__ = "Integer32"
_ConfigEPortScratchPadUseCommonEPortConfig_Object = MibScalar
configEPortScratchPadUseCommonEPortConfig = _ConfigEPortScratchPadUseCommonEPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 7),
    _ConfigEPortScratchPadUseCommonEPortConfig_Type()
)
configEPortScratchPadUseCommonEPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadUseCommonEPortConfig.setStatus("mandatory")


class _ConfigEPortScratchPadLoopback_Type(Integer32):
    """Custom type configEPortScratchPadLoopback based on Integer32"""
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
        *(("diag", 4),
          ("externalLine", 5),
          ("line", 2),
          ("none", 1),
          ("payload", 3))
    )


_ConfigEPortScratchPadLoopback_Type.__name__ = "Integer32"
_ConfigEPortScratchPadLoopback_Object = MibScalar
configEPortScratchPadLoopback = _ConfigEPortScratchPadLoopback_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 8),
    _ConfigEPortScratchPadLoopback_Type()
)
configEPortScratchPadLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadLoopback.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigIlmiAdminStatus_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigIlmiAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("off", 3))
    )


_ConfigEPortScratchPadIlmiConfigIlmiAdminStatus_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigIlmiAdminStatus_Object = MibScalar
configEPortScratchPadIlmiConfigIlmiAdminStatus = _ConfigEPortScratchPadIlmiConfigIlmiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 9),
    _ConfigEPortScratchPadIlmiConfigIlmiAdminStatus_Type()
)
configEPortScratchPadIlmiConfigIlmiAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigIlmiAdminStatus.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigAddrRegistrationAdminStatus_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigAddrRegistrationAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_ConfigEPortScratchPadIlmiConfigAddrRegistrationAdminStatus_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigAddrRegistrationAdminStatus_Object = MibScalar
configEPortScratchPadIlmiConfigAddrRegistrationAdminStatus = _ConfigEPortScratchPadIlmiConfigAddrRegistrationAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 10),
    _ConfigEPortScratchPadIlmiConfigAddrRegistrationAdminStatus_Type()
)
configEPortScratchPadIlmiConfigAddrRegistrationAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigAddrRegistrationAdminStatus.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigMaxVpcs_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigMaxVpcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigEPortScratchPadIlmiConfigMaxVpcs_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigMaxVpcs_Object = MibScalar
configEPortScratchPadIlmiConfigMaxVpcs = _ConfigEPortScratchPadIlmiConfigMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 11),
    _ConfigEPortScratchPadIlmiConfigMaxVpcs_Type()
)
configEPortScratchPadIlmiConfigMaxVpcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigMaxVpcs.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigMaxVccs_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigMaxVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_ConfigEPortScratchPadIlmiConfigMaxVccs_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigMaxVccs_Object = MibScalar
configEPortScratchPadIlmiConfigMaxVccs = _ConfigEPortScratchPadIlmiConfigMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 12),
    _ConfigEPortScratchPadIlmiConfigMaxVccs_Type()
)
configEPortScratchPadIlmiConfigMaxVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigMaxVccs.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigMaxVpiBits_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigMaxVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ConfigEPortScratchPadIlmiConfigMaxVpiBits_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigMaxVpiBits_Object = MibScalar
configEPortScratchPadIlmiConfigMaxVpiBits = _ConfigEPortScratchPadIlmiConfigMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 13),
    _ConfigEPortScratchPadIlmiConfigMaxVpiBits_Type()
)
configEPortScratchPadIlmiConfigMaxVpiBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigMaxVpiBits.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigMaxVciBits_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ConfigEPortScratchPadIlmiConfigMaxVciBits_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigMaxVciBits_Object = MibScalar
configEPortScratchPadIlmiConfigMaxVciBits = _ConfigEPortScratchPadIlmiConfigMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 14),
    _ConfigEPortScratchPadIlmiConfigMaxVciBits_Type()
)
configEPortScratchPadIlmiConfigMaxVciBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigMaxVciBits.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigUniType_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_ConfigEPortScratchPadIlmiConfigUniType_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigUniType_Object = MibScalar
configEPortScratchPadIlmiConfigUniType = _ConfigEPortScratchPadIlmiConfigUniType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 15),
    _ConfigEPortScratchPadIlmiConfigUniType_Type()
)
configEPortScratchPadIlmiConfigUniType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigUniType.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigUniVersion_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigUniVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("version3point0", 2),
          ("version3point1", 3),
          ("version4point0", 4))
    )


_ConfigEPortScratchPadIlmiConfigUniVersion_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigUniVersion_Object = MibScalar
configEPortScratchPadIlmiConfigUniVersion = _ConfigEPortScratchPadIlmiConfigUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 16),
    _ConfigEPortScratchPadIlmiConfigUniVersion_Type()
)
configEPortScratchPadIlmiConfigUniVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigUniVersion.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigDeviceType_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("user", 1))
    )


_ConfigEPortScratchPadIlmiConfigDeviceType_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigDeviceType_Object = MibScalar
configEPortScratchPadIlmiConfigDeviceType = _ConfigEPortScratchPadIlmiConfigDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 17),
    _ConfigEPortScratchPadIlmiConfigDeviceType_Type()
)
configEPortScratchPadIlmiConfigDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigDeviceType.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigIlmiVersion_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigIlmiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("version4point0", 2))
    )


_ConfigEPortScratchPadIlmiConfigIlmiVersion_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigIlmiVersion_Object = MibScalar
configEPortScratchPadIlmiConfigIlmiVersion = _ConfigEPortScratchPadIlmiConfigIlmiVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 18),
    _ConfigEPortScratchPadIlmiConfigIlmiVersion_Type()
)
configEPortScratchPadIlmiConfigIlmiVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigIlmiVersion.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigNniSigVersion_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigNniSigVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 2),
          ("pnniVersion1point0", 3),
          ("unsupported", 1))
    )


_ConfigEPortScratchPadIlmiConfigNniSigVersion_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigNniSigVersion_Object = MibScalar
configEPortScratchPadIlmiConfigNniSigVersion = _ConfigEPortScratchPadIlmiConfigNniSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 19),
    _ConfigEPortScratchPadIlmiConfigNniSigVersion_Type()
)
configEPortScratchPadIlmiConfigNniSigVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigNniSigVersion.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigSignallingVpi_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigSignallingVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigEPortScratchPadIlmiConfigSignallingVpi_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigSignallingVpi_Object = MibScalar
configEPortScratchPadIlmiConfigSignallingVpi = _ConfigEPortScratchPadIlmiConfigSignallingVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 20),
    _ConfigEPortScratchPadIlmiConfigSignallingVpi_Type()
)
configEPortScratchPadIlmiConfigSignallingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigSignallingVpi.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigSignallingVci_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigSignallingVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigEPortScratchPadIlmiConfigSignallingVci_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigSignallingVci_Object = MibScalar
configEPortScratchPadIlmiConfigSignallingVci = _ConfigEPortScratchPadIlmiConfigSignallingVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 21),
    _ConfigEPortScratchPadIlmiConfigSignallingVci_Type()
)
configEPortScratchPadIlmiConfigSignallingVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigSignallingVci.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigIlmiVpi_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigIlmiVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigEPortScratchPadIlmiConfigIlmiVpi_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigIlmiVpi_Object = MibScalar
configEPortScratchPadIlmiConfigIlmiVpi = _ConfigEPortScratchPadIlmiConfigIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 22),
    _ConfigEPortScratchPadIlmiConfigIlmiVpi_Type()
)
configEPortScratchPadIlmiConfigIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigIlmiVpi.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigIlmiVci_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigIlmiVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigEPortScratchPadIlmiConfigIlmiVci_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigIlmiVci_Object = MibScalar
configEPortScratchPadIlmiConfigIlmiVci = _ConfigEPortScratchPadIlmiConfigIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 23),
    _ConfigEPortScratchPadIlmiConfigIlmiVci_Type()
)
configEPortScratchPadIlmiConfigIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigIlmiVci.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigLecsVpi_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigLecsVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigEPortScratchPadIlmiConfigLecsVpi_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigLecsVpi_Object = MibScalar
configEPortScratchPadIlmiConfigLecsVpi = _ConfigEPortScratchPadIlmiConfigLecsVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 24),
    _ConfigEPortScratchPadIlmiConfigLecsVpi_Type()
)
configEPortScratchPadIlmiConfigLecsVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigLecsVpi.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigLecsVci_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigLecsVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigEPortScratchPadIlmiConfigLecsVci_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigLecsVci_Object = MibScalar
configEPortScratchPadIlmiConfigLecsVci = _ConfigEPortScratchPadIlmiConfigLecsVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 25),
    _ConfigEPortScratchPadIlmiConfigLecsVci_Type()
)
configEPortScratchPadIlmiConfigLecsVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigLecsVci.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigPnniVpi_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigPnniVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigEPortScratchPadIlmiConfigPnniVpi_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigPnniVpi_Object = MibScalar
configEPortScratchPadIlmiConfigPnniVpi = _ConfigEPortScratchPadIlmiConfigPnniVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 26),
    _ConfigEPortScratchPadIlmiConfigPnniVpi_Type()
)
configEPortScratchPadIlmiConfigPnniVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigPnniVpi.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigPnniVci_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigPnniVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigEPortScratchPadIlmiConfigPnniVci_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigPnniVci_Object = MibScalar
configEPortScratchPadIlmiConfigPnniVci = _ConfigEPortScratchPadIlmiConfigPnniVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 27),
    _ConfigEPortScratchPadIlmiConfigPnniVci_Type()
)
configEPortScratchPadIlmiConfigPnniVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigPnniVci.setStatus("mandatory")


class _ConfigEPortScratchPadAbrBandwidthAllocation_Type(Integer32):
    """Custom type configEPortScratchPadAbrBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigEPortScratchPadAbrBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigEPortScratchPadAbrBandwidthAllocation_Object = MibScalar
configEPortScratchPadAbrBandwidthAllocation = _ConfigEPortScratchPadAbrBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 28),
    _ConfigEPortScratchPadAbrBandwidthAllocation_Type()
)
configEPortScratchPadAbrBandwidthAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadAbrBandwidthAllocation.setStatus("mandatory")


class _ConfigEPortScratchPadVbrRtBandwidthAllocation_Type(Integer32):
    """Custom type configEPortScratchPadVbrRtBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigEPortScratchPadVbrRtBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigEPortScratchPadVbrRtBandwidthAllocation_Object = MibScalar
configEPortScratchPadVbrRtBandwidthAllocation = _ConfigEPortScratchPadVbrRtBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 29),
    _ConfigEPortScratchPadVbrRtBandwidthAllocation_Type()
)
configEPortScratchPadVbrRtBandwidthAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadVbrRtBandwidthAllocation.setStatus("mandatory")


class _ConfigEPortScratchPadVbrNrtBandwidthAllocation_Type(Integer32):
    """Custom type configEPortScratchPadVbrNrtBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigEPortScratchPadVbrNrtBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigEPortScratchPadVbrNrtBandwidthAllocation_Object = MibScalar
configEPortScratchPadVbrNrtBandwidthAllocation = _ConfigEPortScratchPadVbrNrtBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 30),
    _ConfigEPortScratchPadVbrNrtBandwidthAllocation_Type()
)
configEPortScratchPadVbrNrtBandwidthAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadVbrNrtBandwidthAllocation.setStatus("mandatory")


class _ConfigEPortScratchPadCbrBandwidthAllocation_Type(Integer32):
    """Custom type configEPortScratchPadCbrBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigEPortScratchPadCbrBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigEPortScratchPadCbrBandwidthAllocation_Object = MibScalar
configEPortScratchPadCbrBandwidthAllocation = _ConfigEPortScratchPadCbrBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 31),
    _ConfigEPortScratchPadCbrBandwidthAllocation_Type()
)
configEPortScratchPadCbrBandwidthAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadCbrBandwidthAllocation.setStatus("mandatory")
_ConfigEPortScratchPadLinkDelay_Type = Integer32
_ConfigEPortScratchPadLinkDelay_Object = MibScalar
configEPortScratchPadLinkDelay = _ConfigEPortScratchPadLinkDelay_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 32),
    _ConfigEPortScratchPadLinkDelay_Type()
)
configEPortScratchPadLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadLinkDelay.setStatus("mandatory")
_ConfigEPortScratchPadTransientPhyOffTime_Type = Integer32
_ConfigEPortScratchPadTransientPhyOffTime_Object = MibScalar
configEPortScratchPadTransientPhyOffTime = _ConfigEPortScratchPadTransientPhyOffTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 33),
    _ConfigEPortScratchPadTransientPhyOffTime_Type()
)
configEPortScratchPadTransientPhyOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadTransientPhyOffTime.setStatus("deprecated")
_ConfigEPortScratchPadTransientPhyWindowTime_Type = Integer32
_ConfigEPortScratchPadTransientPhyWindowTime_Object = MibScalar
configEPortScratchPadTransientPhyWindowTime = _ConfigEPortScratchPadTransientPhyWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 34),
    _ConfigEPortScratchPadTransientPhyWindowTime_Type()
)
configEPortScratchPadTransientPhyWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadTransientPhyWindowTime.setStatus("deprecated")


class _ConfigEPortScratchPadTransientPhyDisconnectCount_Type(Integer32):
    """Custom type configEPortScratchPadTransientPhyDisconnectCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ConfigEPortScratchPadTransientPhyDisconnectCount_Type.__name__ = "Integer32"
_ConfigEPortScratchPadTransientPhyDisconnectCount_Object = MibScalar
configEPortScratchPadTransientPhyDisconnectCount = _ConfigEPortScratchPadTransientPhyDisconnectCount_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 35),
    _ConfigEPortScratchPadTransientPhyDisconnectCount_Type()
)
configEPortScratchPadTransientPhyDisconnectCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadTransientPhyDisconnectCount.setStatus("mandatory")
_ConfigEPortScratchPadTransientPhyDisconnectTimer_Type = Integer32
_ConfigEPortScratchPadTransientPhyDisconnectTimer_Object = MibScalar
configEPortScratchPadTransientPhyDisconnectTimer = _ConfigEPortScratchPadTransientPhyDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 36),
    _ConfigEPortScratchPadTransientPhyDisconnectTimer_Type()
)
configEPortScratchPadTransientPhyDisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadTransientPhyDisconnectTimer.setStatus("mandatory")
_ConfigEPortScratchPadBandwidthLimit_Type = Integer32
_ConfigEPortScratchPadBandwidthLimit_Object = MibScalar
configEPortScratchPadBandwidthLimit = _ConfigEPortScratchPadBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 37),
    _ConfigEPortScratchPadBandwidthLimit_Type()
)
configEPortScratchPadBandwidthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadBandwidthLimit.setStatus("mandatory")
_ConfigEPortTable_Object = MibTable
configEPortTable = _ConfigEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38)
)
if mibBuilder.loadTexts:
    configEPortTable.setStatus("mandatory")
_ConfigEPortEntry_Object = MibTableRow
configEPortEntry = _ConfigEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1)
)
configEPortEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configEPortIfIndex"),
)
if mibBuilder.loadTexts:
    configEPortEntry.setStatus("mandatory")
_ConfigEPortIfIndex_Type = Integer32
_ConfigEPortIfIndex_Object = MibTableColumn
configEPortIfIndex = _ConfigEPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 1),
    _ConfigEPortIfIndex_Type()
)
configEPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIfIndex.setStatus("mandatory")


class _ConfigEPortHwConfigTxClocking_Type(Integer32):
    """Custom type configEPortHwConfigTxClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("network", 1))
    )


_ConfigEPortHwConfigTxClocking_Type.__name__ = "Integer32"
_ConfigEPortHwConfigTxClocking_Object = MibTableColumn
configEPortHwConfigTxClocking = _ConfigEPortHwConfigTxClocking_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 2),
    _ConfigEPortHwConfigTxClocking_Type()
)
configEPortHwConfigTxClocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortHwConfigTxClocking.setStatus("mandatory")


class _ConfigEPortHwConfigSonetSdh_Type(Integer32):
    """Custom type configEPortHwConfigSonetSdh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("sdh", 2),
          ("sonet", 1))
    )


_ConfigEPortHwConfigSonetSdh_Type.__name__ = "Integer32"
_ConfigEPortHwConfigSonetSdh_Object = MibTableColumn
configEPortHwConfigSonetSdh = _ConfigEPortHwConfigSonetSdh_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 3),
    _ConfigEPortHwConfigSonetSdh_Type()
)
configEPortHwConfigSonetSdh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortHwConfigSonetSdh.setStatus("mandatory")


class _ConfigEPortUseCommonEPortConfig_Type(Integer32):
    """Custom type configEPortUseCommonEPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ConfigEPortUseCommonEPortConfig_Type.__name__ = "Integer32"
_ConfigEPortUseCommonEPortConfig_Object = MibTableColumn
configEPortUseCommonEPortConfig = _ConfigEPortUseCommonEPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 4),
    _ConfigEPortUseCommonEPortConfig_Type()
)
configEPortUseCommonEPortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortUseCommonEPortConfig.setStatus("mandatory")


class _ConfigEPortLoopback_Type(Integer32):
    """Custom type configEPortLoopback based on Integer32"""
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
        *(("diag", 4),
          ("externalLine", 5),
          ("line", 2),
          ("none", 1),
          ("payload", 3))
    )


_ConfigEPortLoopback_Type.__name__ = "Integer32"
_ConfigEPortLoopback_Object = MibTableColumn
configEPortLoopback = _ConfigEPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 5),
    _ConfigEPortLoopback_Type()
)
configEPortLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortLoopback.setStatus("mandatory")


class _ConfigEPortIlmiConfigIlmiAdminStatus_Type(Integer32):
    """Custom type configEPortIlmiConfigIlmiAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("off", 3))
    )


_ConfigEPortIlmiConfigIlmiAdminStatus_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigIlmiAdminStatus_Object = MibTableColumn
configEPortIlmiConfigIlmiAdminStatus = _ConfigEPortIlmiConfigIlmiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 6),
    _ConfigEPortIlmiConfigIlmiAdminStatus_Type()
)
configEPortIlmiConfigIlmiAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigIlmiAdminStatus.setStatus("mandatory")


class _ConfigEPortIlmiConfigAddrRegistrationAdminStatus_Type(Integer32):
    """Custom type configEPortIlmiConfigAddrRegistrationAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_ConfigEPortIlmiConfigAddrRegistrationAdminStatus_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigAddrRegistrationAdminStatus_Object = MibTableColumn
configEPortIlmiConfigAddrRegistrationAdminStatus = _ConfigEPortIlmiConfigAddrRegistrationAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 7),
    _ConfigEPortIlmiConfigAddrRegistrationAdminStatus_Type()
)
configEPortIlmiConfigAddrRegistrationAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigAddrRegistrationAdminStatus.setStatus("mandatory")


class _ConfigEPortIlmiConfigMaxVpcs_Type(Integer32):
    """Custom type configEPortIlmiConfigMaxVpcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigEPortIlmiConfigMaxVpcs_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigMaxVpcs_Object = MibTableColumn
configEPortIlmiConfigMaxVpcs = _ConfigEPortIlmiConfigMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 8),
    _ConfigEPortIlmiConfigMaxVpcs_Type()
)
configEPortIlmiConfigMaxVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigMaxVpcs.setStatus("mandatory")


class _ConfigEPortIlmiConfigMaxVccs_Type(Integer32):
    """Custom type configEPortIlmiConfigMaxVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_ConfigEPortIlmiConfigMaxVccs_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigMaxVccs_Object = MibTableColumn
configEPortIlmiConfigMaxVccs = _ConfigEPortIlmiConfigMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 9),
    _ConfigEPortIlmiConfigMaxVccs_Type()
)
configEPortIlmiConfigMaxVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigMaxVccs.setStatus("mandatory")


class _ConfigEPortIlmiConfigMaxVpiBits_Type(Integer32):
    """Custom type configEPortIlmiConfigMaxVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ConfigEPortIlmiConfigMaxVpiBits_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigMaxVpiBits_Object = MibTableColumn
configEPortIlmiConfigMaxVpiBits = _ConfigEPortIlmiConfigMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 10),
    _ConfigEPortIlmiConfigMaxVpiBits_Type()
)
configEPortIlmiConfigMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigMaxVpiBits.setStatus("mandatory")


class _ConfigEPortIlmiConfigMaxVciBits_Type(Integer32):
    """Custom type configEPortIlmiConfigMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ConfigEPortIlmiConfigMaxVciBits_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigMaxVciBits_Object = MibTableColumn
configEPortIlmiConfigMaxVciBits = _ConfigEPortIlmiConfigMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 11),
    _ConfigEPortIlmiConfigMaxVciBits_Type()
)
configEPortIlmiConfigMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigMaxVciBits.setStatus("mandatory")


class _ConfigEPortIlmiConfigUniType_Type(Integer32):
    """Custom type configEPortIlmiConfigUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_ConfigEPortIlmiConfigUniType_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigUniType_Object = MibTableColumn
configEPortIlmiConfigUniType = _ConfigEPortIlmiConfigUniType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 12),
    _ConfigEPortIlmiConfigUniType_Type()
)
configEPortIlmiConfigUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigUniType.setStatus("mandatory")


class _ConfigEPortIlmiConfigUniVersion_Type(Integer32):
    """Custom type configEPortIlmiConfigUniVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("version3point0", 2),
          ("version3point1", 3),
          ("version4point0", 4))
    )


_ConfigEPortIlmiConfigUniVersion_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigUniVersion_Object = MibTableColumn
configEPortIlmiConfigUniVersion = _ConfigEPortIlmiConfigUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 13),
    _ConfigEPortIlmiConfigUniVersion_Type()
)
configEPortIlmiConfigUniVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigUniVersion.setStatus("mandatory")


class _ConfigEPortIlmiConfigDeviceType_Type(Integer32):
    """Custom type configEPortIlmiConfigDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("user", 1))
    )


_ConfigEPortIlmiConfigDeviceType_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigDeviceType_Object = MibTableColumn
configEPortIlmiConfigDeviceType = _ConfigEPortIlmiConfigDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 14),
    _ConfigEPortIlmiConfigDeviceType_Type()
)
configEPortIlmiConfigDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigDeviceType.setStatus("mandatory")


class _ConfigEPortIlmiConfigIlmiVersion_Type(Integer32):
    """Custom type configEPortIlmiConfigIlmiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("version4point0", 2))
    )


_ConfigEPortIlmiConfigIlmiVersion_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigIlmiVersion_Object = MibTableColumn
configEPortIlmiConfigIlmiVersion = _ConfigEPortIlmiConfigIlmiVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 15),
    _ConfigEPortIlmiConfigIlmiVersion_Type()
)
configEPortIlmiConfigIlmiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigIlmiVersion.setStatus("mandatory")


class _ConfigEPortIlmiConfigNniSigVersion_Type(Integer32):
    """Custom type configEPortIlmiConfigNniSigVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 2),
          ("pnniVersion1point0", 3),
          ("unsupported", 1))
    )


_ConfigEPortIlmiConfigNniSigVersion_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigNniSigVersion_Object = MibTableColumn
configEPortIlmiConfigNniSigVersion = _ConfigEPortIlmiConfigNniSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 16),
    _ConfigEPortIlmiConfigNniSigVersion_Type()
)
configEPortIlmiConfigNniSigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigNniSigVersion.setStatus("mandatory")


class _ConfigEPortIlmiConfigSignallingVpi_Type(Integer32):
    """Custom type configEPortIlmiConfigSignallingVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigEPortIlmiConfigSignallingVpi_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigSignallingVpi_Object = MibTableColumn
configEPortIlmiConfigSignallingVpi = _ConfigEPortIlmiConfigSignallingVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 17),
    _ConfigEPortIlmiConfigSignallingVpi_Type()
)
configEPortIlmiConfigSignallingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigSignallingVpi.setStatus("mandatory")


class _ConfigEPortIlmiConfigSignallingVci_Type(Integer32):
    """Custom type configEPortIlmiConfigSignallingVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigEPortIlmiConfigSignallingVci_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigSignallingVci_Object = MibTableColumn
configEPortIlmiConfigSignallingVci = _ConfigEPortIlmiConfigSignallingVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 18),
    _ConfigEPortIlmiConfigSignallingVci_Type()
)
configEPortIlmiConfigSignallingVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigSignallingVci.setStatus("mandatory")


class _ConfigEPortIlmiConfigIlmiVpi_Type(Integer32):
    """Custom type configEPortIlmiConfigIlmiVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigEPortIlmiConfigIlmiVpi_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigIlmiVpi_Object = MibTableColumn
configEPortIlmiConfigIlmiVpi = _ConfigEPortIlmiConfigIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 19),
    _ConfigEPortIlmiConfigIlmiVpi_Type()
)
configEPortIlmiConfigIlmiVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigIlmiVpi.setStatus("mandatory")


class _ConfigEPortIlmiConfigIlmiVci_Type(Integer32):
    """Custom type configEPortIlmiConfigIlmiVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigEPortIlmiConfigIlmiVci_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigIlmiVci_Object = MibTableColumn
configEPortIlmiConfigIlmiVci = _ConfigEPortIlmiConfigIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 20),
    _ConfigEPortIlmiConfigIlmiVci_Type()
)
configEPortIlmiConfigIlmiVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigIlmiVci.setStatus("mandatory")


class _ConfigEPortIlmiConfigLecsVpi_Type(Integer32):
    """Custom type configEPortIlmiConfigLecsVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigEPortIlmiConfigLecsVpi_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigLecsVpi_Object = MibTableColumn
configEPortIlmiConfigLecsVpi = _ConfigEPortIlmiConfigLecsVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 21),
    _ConfigEPortIlmiConfigLecsVpi_Type()
)
configEPortIlmiConfigLecsVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigLecsVpi.setStatus("mandatory")


class _ConfigEPortIlmiConfigLecsVci_Type(Integer32):
    """Custom type configEPortIlmiConfigLecsVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigEPortIlmiConfigLecsVci_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigLecsVci_Object = MibTableColumn
configEPortIlmiConfigLecsVci = _ConfigEPortIlmiConfigLecsVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 22),
    _ConfigEPortIlmiConfigLecsVci_Type()
)
configEPortIlmiConfigLecsVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigLecsVci.setStatus("mandatory")


class _ConfigEPortIlmiConfigPnniVpi_Type(Integer32):
    """Custom type configEPortIlmiConfigPnniVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigEPortIlmiConfigPnniVpi_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigPnniVpi_Object = MibTableColumn
configEPortIlmiConfigPnniVpi = _ConfigEPortIlmiConfigPnniVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 23),
    _ConfigEPortIlmiConfigPnniVpi_Type()
)
configEPortIlmiConfigPnniVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigPnniVpi.setStatus("mandatory")


class _ConfigEPortIlmiConfigPnniVci_Type(Integer32):
    """Custom type configEPortIlmiConfigPnniVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ConfigEPortIlmiConfigPnniVci_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigPnniVci_Object = MibTableColumn
configEPortIlmiConfigPnniVci = _ConfigEPortIlmiConfigPnniVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 24),
    _ConfigEPortIlmiConfigPnniVci_Type()
)
configEPortIlmiConfigPnniVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigPnniVci.setStatus("mandatory")


class _ConfigEPortAbrBandwidthAllocation_Type(Integer32):
    """Custom type configEPortAbrBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigEPortAbrBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigEPortAbrBandwidthAllocation_Object = MibTableColumn
configEPortAbrBandwidthAllocation = _ConfigEPortAbrBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 25),
    _ConfigEPortAbrBandwidthAllocation_Type()
)
configEPortAbrBandwidthAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortAbrBandwidthAllocation.setStatus("mandatory")


class _ConfigEPortVbrRtBandwidthAllocation_Type(Integer32):
    """Custom type configEPortVbrRtBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigEPortVbrRtBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigEPortVbrRtBandwidthAllocation_Object = MibTableColumn
configEPortVbrRtBandwidthAllocation = _ConfigEPortVbrRtBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 26),
    _ConfigEPortVbrRtBandwidthAllocation_Type()
)
configEPortVbrRtBandwidthAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortVbrRtBandwidthAllocation.setStatus("mandatory")


class _ConfigEPortVbrNrtBandwidthAllocation_Type(Integer32):
    """Custom type configEPortVbrNrtBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigEPortVbrNrtBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigEPortVbrNrtBandwidthAllocation_Object = MibTableColumn
configEPortVbrNrtBandwidthAllocation = _ConfigEPortVbrNrtBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 27),
    _ConfigEPortVbrNrtBandwidthAllocation_Type()
)
configEPortVbrNrtBandwidthAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortVbrNrtBandwidthAllocation.setStatus("mandatory")


class _ConfigEPortCbrBandwidthAllocation_Type(Integer32):
    """Custom type configEPortCbrBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConfigEPortCbrBandwidthAllocation_Type.__name__ = "Integer32"
_ConfigEPortCbrBandwidthAllocation_Object = MibTableColumn
configEPortCbrBandwidthAllocation = _ConfigEPortCbrBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 28),
    _ConfigEPortCbrBandwidthAllocation_Type()
)
configEPortCbrBandwidthAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortCbrBandwidthAllocation.setStatus("mandatory")
_ConfigEPortLinkDelay_Type = Integer32
_ConfigEPortLinkDelay_Object = MibTableColumn
configEPortLinkDelay = _ConfigEPortLinkDelay_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 29),
    _ConfigEPortLinkDelay_Type()
)
configEPortLinkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortLinkDelay.setStatus("mandatory")
_ConfigEPortTransientPhyOffTime_Type = Integer32
_ConfigEPortTransientPhyOffTime_Object = MibTableColumn
configEPortTransientPhyOffTime = _ConfigEPortTransientPhyOffTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 30),
    _ConfigEPortTransientPhyOffTime_Type()
)
configEPortTransientPhyOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortTransientPhyOffTime.setStatus("deprecated")
_ConfigEPortTransientPhyWindowTime_Type = Integer32
_ConfigEPortTransientPhyWindowTime_Object = MibTableColumn
configEPortTransientPhyWindowTime = _ConfigEPortTransientPhyWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 31),
    _ConfigEPortTransientPhyWindowTime_Type()
)
configEPortTransientPhyWindowTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortTransientPhyWindowTime.setStatus("deprecated")


class _ConfigEPortTransientPhyDisconnectCount_Type(Integer32):
    """Custom type configEPortTransientPhyDisconnectCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ConfigEPortTransientPhyDisconnectCount_Type.__name__ = "Integer32"
_ConfigEPortTransientPhyDisconnectCount_Object = MibTableColumn
configEPortTransientPhyDisconnectCount = _ConfigEPortTransientPhyDisconnectCount_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 32),
    _ConfigEPortTransientPhyDisconnectCount_Type()
)
configEPortTransientPhyDisconnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortTransientPhyDisconnectCount.setStatus("mandatory")
_ConfigEPortTransientPhyDisconnectTimer_Type = Integer32
_ConfigEPortTransientPhyDisconnectTimer_Object = MibTableColumn
configEPortTransientPhyDisconnectTimer = _ConfigEPortTransientPhyDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 33),
    _ConfigEPortTransientPhyDisconnectTimer_Type()
)
configEPortTransientPhyDisconnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortTransientPhyDisconnectTimer.setStatus("mandatory")
_ConfigEPortBandwidthLimit_Type = Integer32
_ConfigEPortBandwidthLimit_Object = MibTableColumn
configEPortBandwidthLimit = _ConfigEPortBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 34),
    _ConfigEPortBandwidthLimit_Type()
)
configEPortBandwidthLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortBandwidthLimit.setStatus("mandatory")


class _ConfigEPortDefaultSigVersion_Type(Integer32):
    """Custom type configEPortDefaultSigVersion based on Integer32"""
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
        *(("iispNetworkSide", 3),
          ("iispUserSide", 4),
          ("pnni", 2),
          ("uni", 1))
    )


_ConfigEPortDefaultSigVersion_Type.__name__ = "Integer32"
_ConfigEPortDefaultSigVersion_Object = MibTableColumn
configEPortDefaultSigVersion = _ConfigEPortDefaultSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 35),
    _ConfigEPortDefaultSigVersion_Type()
)
configEPortDefaultSigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortDefaultSigVersion.setStatus("mandatory")


class _ConfigEPortIlmiConfigMaxSvpcVpi_Type(Integer32):
    """Custom type configEPortIlmiConfigMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ConfigEPortIlmiConfigMaxSvpcVpi_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigMaxSvpcVpi_Object = MibTableColumn
configEPortIlmiConfigMaxSvpcVpi = _ConfigEPortIlmiConfigMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 36),
    _ConfigEPortIlmiConfigMaxSvpcVpi_Type()
)
configEPortIlmiConfigMaxSvpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigMaxSvpcVpi.setStatus("mandatory")


class _ConfigEPortIlmiConfigMaxSvccVpi_Type(Integer32):
    """Custom type configEPortIlmiConfigMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ConfigEPortIlmiConfigMaxSvccVpi_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigMaxSvccVpi_Object = MibTableColumn
configEPortIlmiConfigMaxSvccVpi = _ConfigEPortIlmiConfigMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 37),
    _ConfigEPortIlmiConfigMaxSvccVpi_Type()
)
configEPortIlmiConfigMaxSvccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigMaxSvccVpi.setStatus("mandatory")


class _ConfigEPortIlmiConfigMinSvccVci_Type(Integer32):
    """Custom type configEPortIlmiConfigMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_ConfigEPortIlmiConfigMinSvccVci_Type.__name__ = "Integer32"
_ConfigEPortIlmiConfigMinSvccVci_Object = MibTableColumn
configEPortIlmiConfigMinSvccVci = _ConfigEPortIlmiConfigMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 38, 1, 38),
    _ConfigEPortIlmiConfigMinSvccVci_Type()
)
configEPortIlmiConfigMinSvccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPortIlmiConfigMinSvccVci.setStatus("mandatory")


class _ConfigEPortScratchPadDefaultSigVersion_Type(Integer32):
    """Custom type configEPortScratchPadDefaultSigVersion based on Integer32"""
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
        *(("iispNetworkSide", 3),
          ("iispUserSide", 4),
          ("pnni", 2),
          ("uni", 1))
    )


_ConfigEPortScratchPadDefaultSigVersion_Type.__name__ = "Integer32"
_ConfigEPortScratchPadDefaultSigVersion_Object = MibScalar
configEPortScratchPadDefaultSigVersion = _ConfigEPortScratchPadDefaultSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 39),
    _ConfigEPortScratchPadDefaultSigVersion_Type()
)
configEPortScratchPadDefaultSigVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadDefaultSigVersion.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigMaxSvpcVpi_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ConfigEPortScratchPadIlmiConfigMaxSvpcVpi_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigMaxSvpcVpi_Object = MibScalar
configEPortScratchPadIlmiConfigMaxSvpcVpi = _ConfigEPortScratchPadIlmiConfigMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 40),
    _ConfigEPortScratchPadIlmiConfigMaxSvpcVpi_Type()
)
configEPortScratchPadIlmiConfigMaxSvpcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigMaxSvpcVpi.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigMaxSvccVpi_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ConfigEPortScratchPadIlmiConfigMaxSvccVpi_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigMaxSvccVpi_Object = MibScalar
configEPortScratchPadIlmiConfigMaxSvccVpi = _ConfigEPortScratchPadIlmiConfigMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 41),
    _ConfigEPortScratchPadIlmiConfigMaxSvccVpi_Type()
)
configEPortScratchPadIlmiConfigMaxSvccVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigMaxSvccVpi.setStatus("mandatory")


class _ConfigEPortScratchPadIlmiConfigMinSvccVci_Type(Integer32):
    """Custom type configEPortScratchPadIlmiConfigMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_ConfigEPortScratchPadIlmiConfigMinSvccVci_Type.__name__ = "Integer32"
_ConfigEPortScratchPadIlmiConfigMinSvccVci_Object = MibScalar
configEPortScratchPadIlmiConfigMinSvccVci = _ConfigEPortScratchPadIlmiConfigMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 13, 42),
    _ConfigEPortScratchPadIlmiConfigMinSvccVci_Type()
)
configEPortScratchPadIlmiConfigMinSvccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEPortScratchPadIlmiConfigMinSvccVci.setStatus("mandatory")
_ConfigCpuQ_ObjectIdentity = ObjectIdentity
configCpuQ = _ConfigCpuQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 14)
)
_ConfigCpuPortCpuQueueSize_Type = Integer32
_ConfigCpuPortCpuQueueSize_Object = MibScalar
configCpuPortCpuQueueSize = _ConfigCpuPortCpuQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 14, 1),
    _ConfigCpuPortCpuQueueSize_Type()
)
configCpuPortCpuQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCpuPortCpuQueueSize.setStatus("mandatory")
_ConfigCpuPortResetQueueSize_Type = Integer32
_ConfigCpuPortResetQueueSize_Object = MibScalar
configCpuPortResetQueueSize = _ConfigCpuPortResetQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 14, 2),
    _ConfigCpuPortResetQueueSize_Type()
)
configCpuPortResetQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCpuPortResetQueueSize.setStatus("mandatory")
_ConfigCommonIPort_ObjectIdentity = ObjectIdentity
configCommonIPort = _ConfigCommonIPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15)
)
_ConfigCommonIPortQueueTable_Object = MibTable
configCommonIPortQueueTable = _ConfigCommonIPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15, 1)
)
if mibBuilder.loadTexts:
    configCommonIPortQueueTable.setStatus("mandatory")
_ConfigCommonIPortQueueEntry_Object = MibTableRow
configCommonIPortQueueEntry = _ConfigCommonIPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15, 1, 1)
)
configCommonIPortQueueEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configCommonIPortQueueIndex"),
)
if mibBuilder.loadTexts:
    configCommonIPortQueueEntry.setStatus("mandatory")


class _ConfigCommonIPortQueueIndex_Type(Integer32):
    """Custom type configCommonIPortQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ConfigCommonIPortQueueIndex_Type.__name__ = "Integer32"
_ConfigCommonIPortQueueIndex_Object = MibTableColumn
configCommonIPortQueueIndex = _ConfigCommonIPortQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15, 1, 1, 1),
    _ConfigCommonIPortQueueIndex_Type()
)
configCommonIPortQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configCommonIPortQueueIndex.setStatus("mandatory")


class _ConfigCommonIPortEfciTaggingAdminStatus_Type(Integer32):
    """Custom type configCommonIPortEfciTaggingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigCommonIPortEfciTaggingAdminStatus_Type.__name__ = "Integer32"
_ConfigCommonIPortEfciTaggingAdminStatus_Object = MibTableColumn
configCommonIPortEfciTaggingAdminStatus = _ConfigCommonIPortEfciTaggingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15, 1, 1, 2),
    _ConfigCommonIPortEfciTaggingAdminStatus_Type()
)
configCommonIPortEfciTaggingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonIPortEfciTaggingAdminStatus.setStatus("mandatory")


class _ConfigCommonIPortClpDiscardAdminStatus_Type(Integer32):
    """Custom type configCommonIPortClpDiscardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigCommonIPortClpDiscardAdminStatus_Type.__name__ = "Integer32"
_ConfigCommonIPortClpDiscardAdminStatus_Object = MibTableColumn
configCommonIPortClpDiscardAdminStatus = _ConfigCommonIPortClpDiscardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15, 1, 1, 3),
    _ConfigCommonIPortClpDiscardAdminStatus_Type()
)
configCommonIPortClpDiscardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonIPortClpDiscardAdminStatus.setStatus("mandatory")


class _ConfigCommonIPortEfciTaggingThreshold_Type(Integer32):
    """Custom type configCommonIPortEfciTaggingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneEighth", 1),
          ("oneFourth", 2),
          ("oneHalf", 3))
    )


_ConfigCommonIPortEfciTaggingThreshold_Type.__name__ = "Integer32"
_ConfigCommonIPortEfciTaggingThreshold_Object = MibTableColumn
configCommonIPortEfciTaggingThreshold = _ConfigCommonIPortEfciTaggingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15, 1, 1, 4),
    _ConfigCommonIPortEfciTaggingThreshold_Type()
)
configCommonIPortEfciTaggingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonIPortEfciTaggingThreshold.setStatus("mandatory")


class _ConfigCommonIPortClpDiscardThreshold_Type(Integer32):
    """Custom type configCommonIPortClpDiscardThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneEighth", 1),
          ("oneFourth", 2),
          ("oneHalf", 3))
    )


_ConfigCommonIPortClpDiscardThreshold_Type.__name__ = "Integer32"
_ConfigCommonIPortClpDiscardThreshold_Object = MibTableColumn
configCommonIPortClpDiscardThreshold = _ConfigCommonIPortClpDiscardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15, 1, 1, 5),
    _ConfigCommonIPortClpDiscardThreshold_Type()
)
configCommonIPortClpDiscardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonIPortClpDiscardThreshold.setStatus("mandatory")
_ConfigCommonIPortQueueSize_Type = Integer32
_ConfigCommonIPortQueueSize_Object = MibTableColumn
configCommonIPortQueueSize = _ConfigCommonIPortQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15, 1, 1, 6),
    _ConfigCommonIPortQueueSize_Type()
)
configCommonIPortQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonIPortQueueSize.setStatus("mandatory")
_ConfigCommonIPortLogClr_Type = Integer32
_ConfigCommonIPortLogClr_Object = MibTableColumn
configCommonIPortLogClr = _ConfigCommonIPortLogClr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15, 1, 1, 7),
    _ConfigCommonIPortLogClr_Type()
)
configCommonIPortLogClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonIPortLogClr.setStatus("mandatory")
_ConfigCommonIPortCdv_Type = Integer32
_ConfigCommonIPortCdv_Object = MibTableColumn
configCommonIPortCdv = _ConfigCommonIPortCdv_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 15, 1, 1, 8),
    _ConfigCommonIPortCdv_Type()
)
configCommonIPortCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonIPortCdv.setStatus("mandatory")
_ConfigIPort_ObjectIdentity = ObjectIdentity
configIPort = _ConfigIPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16)
)


class _ConfigIPortScratchPadScratchPadStatus_Type(Integer32):
    """Custom type configIPortScratchPadScratchPadStatus based on Integer32"""
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
        *(("copied", 3),
          ("copy", 2),
          ("notReady", 1),
          ("updateAndGo", 4))
    )


_ConfigIPortScratchPadScratchPadStatus_Type.__name__ = "Integer32"
_ConfigIPortScratchPadScratchPadStatus_Object = MibScalar
configIPortScratchPadScratchPadStatus = _ConfigIPortScratchPadScratchPadStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 1),
    _ConfigIPortScratchPadScratchPadStatus_Type()
)
configIPortScratchPadScratchPadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadScratchPadStatus.setStatus("mandatory")


class _ConfigIPortScratchPadSlotIndex_Type(Integer32):
    """Custom type configIPortScratchPadSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ConfigIPortScratchPadSlotIndex_Type.__name__ = "Integer32"
_ConfigIPortScratchPadSlotIndex_Object = MibScalar
configIPortScratchPadSlotIndex = _ConfigIPortScratchPadSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 2),
    _ConfigIPortScratchPadSlotIndex_Type()
)
configIPortScratchPadSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadSlotIndex.setStatus("mandatory")


class _ConfigIPortScratchPadIPortRIndex_Type(Integer32):
    """Custom type configIPortScratchPadIPortRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ConfigIPortScratchPadIPortRIndex_Type.__name__ = "Integer32"
_ConfigIPortScratchPadIPortRIndex_Object = MibScalar
configIPortScratchPadIPortRIndex = _ConfigIPortScratchPadIPortRIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 3),
    _ConfigIPortScratchPadIPortRIndex_Type()
)
configIPortScratchPadIPortRIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadIPortRIndex.setStatus("mandatory")
_ConfigIPortScratchPadIpAddress_Type = IpAddress
_ConfigIPortScratchPadIpAddress_Object = MibScalar
configIPortScratchPadIpAddress = _ConfigIPortScratchPadIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 4),
    _ConfigIPortScratchPadIpAddress_Type()
)
configIPortScratchPadIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortScratchPadIpAddress.setStatus("mandatory")


class _ConfigIPortScratchPadActionStatus_Type(Integer32):
    """Custom type configIPortScratchPadActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("notPossible", 3),
          ("ok", 1))
    )


_ConfigIPortScratchPadActionStatus_Type.__name__ = "Integer32"
_ConfigIPortScratchPadActionStatus_Object = MibScalar
configIPortScratchPadActionStatus = _ConfigIPortScratchPadActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 5),
    _ConfigIPortScratchPadActionStatus_Type()
)
configIPortScratchPadActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortScratchPadActionStatus.setStatus("mandatory")


class _ConfigIPortScratchPadUseCommonIPortConfig_Type(Integer32):
    """Custom type configIPortScratchPadUseCommonIPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ConfigIPortScratchPadUseCommonIPortConfig_Type.__name__ = "Integer32"
_ConfigIPortScratchPadUseCommonIPortConfig_Object = MibScalar
configIPortScratchPadUseCommonIPortConfig = _ConfigIPortScratchPadUseCommonIPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 6),
    _ConfigIPortScratchPadUseCommonIPortConfig_Type()
)
configIPortScratchPadUseCommonIPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadUseCommonIPortConfig.setStatus("mandatory")
_ConfigIPortScratchPadQueueTable_Object = MibTable
configIPortScratchPadQueueTable = _ConfigIPortScratchPadQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 7)
)
if mibBuilder.loadTexts:
    configIPortScratchPadQueueTable.setStatus("mandatory")
_ConfigIPortScratchPadQueueEntry_Object = MibTableRow
configIPortScratchPadQueueEntry = _ConfigIPortScratchPadQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 7, 1)
)
configIPortScratchPadQueueEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configIPortScratchPadQueueQueueIndex"),
)
if mibBuilder.loadTexts:
    configIPortScratchPadQueueEntry.setStatus("mandatory")


class _ConfigIPortScratchPadQueueQueueIndex_Type(Integer32):
    """Custom type configIPortScratchPadQueueQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ConfigIPortScratchPadQueueQueueIndex_Type.__name__ = "Integer32"
_ConfigIPortScratchPadQueueQueueIndex_Object = MibTableColumn
configIPortScratchPadQueueQueueIndex = _ConfigIPortScratchPadQueueQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 7, 1, 1),
    _ConfigIPortScratchPadQueueQueueIndex_Type()
)
configIPortScratchPadQueueQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortScratchPadQueueQueueIndex.setStatus("mandatory")


class _ConfigIPortScratchPadQueueEfciTaggingAdminStatus_Type(Integer32):
    """Custom type configIPortScratchPadQueueEfciTaggingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigIPortScratchPadQueueEfciTaggingAdminStatus_Type.__name__ = "Integer32"
_ConfigIPortScratchPadQueueEfciTaggingAdminStatus_Object = MibTableColumn
configIPortScratchPadQueueEfciTaggingAdminStatus = _ConfigIPortScratchPadQueueEfciTaggingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 7, 1, 2),
    _ConfigIPortScratchPadQueueEfciTaggingAdminStatus_Type()
)
configIPortScratchPadQueueEfciTaggingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadQueueEfciTaggingAdminStatus.setStatus("mandatory")


class _ConfigIPortScratchPadQueueClpDiscardAdminStatus_Type(Integer32):
    """Custom type configIPortScratchPadQueueClpDiscardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigIPortScratchPadQueueClpDiscardAdminStatus_Type.__name__ = "Integer32"
_ConfigIPortScratchPadQueueClpDiscardAdminStatus_Object = MibTableColumn
configIPortScratchPadQueueClpDiscardAdminStatus = _ConfigIPortScratchPadQueueClpDiscardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 7, 1, 3),
    _ConfigIPortScratchPadQueueClpDiscardAdminStatus_Type()
)
configIPortScratchPadQueueClpDiscardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadQueueClpDiscardAdminStatus.setStatus("mandatory")


class _ConfigIPortScratchPadQueueEfciTaggingThreshold_Type(Integer32):
    """Custom type configIPortScratchPadQueueEfciTaggingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneEighth", 1),
          ("oneFourth", 2),
          ("oneHalf", 3))
    )


_ConfigIPortScratchPadQueueEfciTaggingThreshold_Type.__name__ = "Integer32"
_ConfigIPortScratchPadQueueEfciTaggingThreshold_Object = MibTableColumn
configIPortScratchPadQueueEfciTaggingThreshold = _ConfigIPortScratchPadQueueEfciTaggingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 7, 1, 4),
    _ConfigIPortScratchPadQueueEfciTaggingThreshold_Type()
)
configIPortScratchPadQueueEfciTaggingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadQueueEfciTaggingThreshold.setStatus("mandatory")


class _ConfigIPortScratchPadQueueClpDiscardThreshold_Type(Integer32):
    """Custom type configIPortScratchPadQueueClpDiscardThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneEighth", 1),
          ("oneFourth", 2),
          ("oneHalf", 3))
    )


_ConfigIPortScratchPadQueueClpDiscardThreshold_Type.__name__ = "Integer32"
_ConfigIPortScratchPadQueueClpDiscardThreshold_Object = MibTableColumn
configIPortScratchPadQueueClpDiscardThreshold = _ConfigIPortScratchPadQueueClpDiscardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 7, 1, 5),
    _ConfigIPortScratchPadQueueClpDiscardThreshold_Type()
)
configIPortScratchPadQueueClpDiscardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadQueueClpDiscardThreshold.setStatus("mandatory")
_ConfigIPortScratchPadQueueSize_Type = Integer32
_ConfigIPortScratchPadQueueSize_Object = MibTableColumn
configIPortScratchPadQueueSize = _ConfigIPortScratchPadQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 7, 1, 6),
    _ConfigIPortScratchPadQueueSize_Type()
)
configIPortScratchPadQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadQueueSize.setStatus("mandatory")
_ConfigIPortScratchPadQueueLogClr_Type = Integer32
_ConfigIPortScratchPadQueueLogClr_Object = MibTableColumn
configIPortScratchPadQueueLogClr = _ConfigIPortScratchPadQueueLogClr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 7, 1, 7),
    _ConfigIPortScratchPadQueueLogClr_Type()
)
configIPortScratchPadQueueLogClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadQueueLogClr.setStatus("mandatory")
_ConfigIPortScratchPadQueueCdv_Type = Integer32
_ConfigIPortScratchPadQueueCdv_Object = MibTableColumn
configIPortScratchPadQueueCdv = _ConfigIPortScratchPadQueueCdv_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 7, 1, 8),
    _ConfigIPortScratchPadQueueCdv_Type()
)
configIPortScratchPadQueueCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortScratchPadQueueCdv.setStatus("mandatory")
_ConfigIPortTable_Object = MibTable
configIPortTable = _ConfigIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 8)
)
if mibBuilder.loadTexts:
    configIPortTable.setStatus("mandatory")
_ConfigIPortEntry_Object = MibTableRow
configIPortEntry = _ConfigIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 8, 1)
)
configIPortEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configIPortSlotIndex"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "configIPortRIndex"),
)
if mibBuilder.loadTexts:
    configIPortEntry.setStatus("mandatory")


class _ConfigIPortSlotIndex_Type(Integer32):
    """Custom type configIPortSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ConfigIPortSlotIndex_Type.__name__ = "Integer32"
_ConfigIPortSlotIndex_Object = MibTableColumn
configIPortSlotIndex = _ConfigIPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 8, 1, 1),
    _ConfigIPortSlotIndex_Type()
)
configIPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortSlotIndex.setStatus("mandatory")


class _ConfigIPortRIndex_Type(Integer32):
    """Custom type configIPortRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ConfigIPortRIndex_Type.__name__ = "Integer32"
_ConfigIPortRIndex_Object = MibTableColumn
configIPortRIndex = _ConfigIPortRIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 8, 1, 2),
    _ConfigIPortRIndex_Type()
)
configIPortRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortRIndex.setStatus("mandatory")


class _ConfigIPortUseCommonIPortConfig_Type(Integer32):
    """Custom type configIPortUseCommonIPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ConfigIPortUseCommonIPortConfig_Type.__name__ = "Integer32"
_ConfigIPortUseCommonIPortConfig_Object = MibTableColumn
configIPortUseCommonIPortConfig = _ConfigIPortUseCommonIPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 8, 1, 3),
    _ConfigIPortUseCommonIPortConfig_Type()
)
configIPortUseCommonIPortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortUseCommonIPortConfig.setStatus("mandatory")
_ConfigIPortQueueTable_Object = MibTable
configIPortQueueTable = _ConfigIPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9)
)
if mibBuilder.loadTexts:
    configIPortQueueTable.setStatus("mandatory")
_ConfigIPortQueueEntry_Object = MibTableRow
configIPortQueueEntry = _ConfigIPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1)
)
configIPortQueueEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configIPortQueueSlotIndex"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "configIPortQueueRIndex"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "configIPortQueueQueueIndex"),
)
if mibBuilder.loadTexts:
    configIPortQueueEntry.setStatus("mandatory")


class _ConfigIPortQueueSlotIndex_Type(Integer32):
    """Custom type configIPortQueueSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ConfigIPortQueueSlotIndex_Type.__name__ = "Integer32"
_ConfigIPortQueueSlotIndex_Object = MibTableColumn
configIPortQueueSlotIndex = _ConfigIPortQueueSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1, 1),
    _ConfigIPortQueueSlotIndex_Type()
)
configIPortQueueSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortQueueSlotIndex.setStatus("mandatory")


class _ConfigIPortQueueRIndex_Type(Integer32):
    """Custom type configIPortQueueRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ConfigIPortQueueRIndex_Type.__name__ = "Integer32"
_ConfigIPortQueueRIndex_Object = MibTableColumn
configIPortQueueRIndex = _ConfigIPortQueueRIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1, 2),
    _ConfigIPortQueueRIndex_Type()
)
configIPortQueueRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortQueueRIndex.setStatus("mandatory")


class _ConfigIPortQueueQueueIndex_Type(Integer32):
    """Custom type configIPortQueueQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ConfigIPortQueueQueueIndex_Type.__name__ = "Integer32"
_ConfigIPortQueueQueueIndex_Object = MibTableColumn
configIPortQueueQueueIndex = _ConfigIPortQueueQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1, 3),
    _ConfigIPortQueueQueueIndex_Type()
)
configIPortQueueQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortQueueQueueIndex.setStatus("mandatory")


class _ConfigIPortQueueEfciTaggingAdminStatus_Type(Integer32):
    """Custom type configIPortQueueEfciTaggingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigIPortQueueEfciTaggingAdminStatus_Type.__name__ = "Integer32"
_ConfigIPortQueueEfciTaggingAdminStatus_Object = MibTableColumn
configIPortQueueEfciTaggingAdminStatus = _ConfigIPortQueueEfciTaggingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1, 4),
    _ConfigIPortQueueEfciTaggingAdminStatus_Type()
)
configIPortQueueEfciTaggingAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortQueueEfciTaggingAdminStatus.setStatus("mandatory")


class _ConfigIPortQueueClpDiscardAdminStatus_Type(Integer32):
    """Custom type configIPortQueueClpDiscardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigIPortQueueClpDiscardAdminStatus_Type.__name__ = "Integer32"
_ConfigIPortQueueClpDiscardAdminStatus_Object = MibTableColumn
configIPortQueueClpDiscardAdminStatus = _ConfigIPortQueueClpDiscardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1, 5),
    _ConfigIPortQueueClpDiscardAdminStatus_Type()
)
configIPortQueueClpDiscardAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortQueueClpDiscardAdminStatus.setStatus("mandatory")


class _ConfigIPortQueueEfciTaggingThreshold_Type(Integer32):
    """Custom type configIPortQueueEfciTaggingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneEighth", 1),
          ("oneFourth", 2),
          ("oneHalf", 3))
    )


_ConfigIPortQueueEfciTaggingThreshold_Type.__name__ = "Integer32"
_ConfigIPortQueueEfciTaggingThreshold_Object = MibTableColumn
configIPortQueueEfciTaggingThreshold = _ConfigIPortQueueEfciTaggingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1, 6),
    _ConfigIPortQueueEfciTaggingThreshold_Type()
)
configIPortQueueEfciTaggingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortQueueEfciTaggingThreshold.setStatus("mandatory")


class _ConfigIPortQueueClpDiscardThreshold_Type(Integer32):
    """Custom type configIPortQueueClpDiscardThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneEighth", 1),
          ("oneFourth", 2),
          ("oneHalf", 3))
    )


_ConfigIPortQueueClpDiscardThreshold_Type.__name__ = "Integer32"
_ConfigIPortQueueClpDiscardThreshold_Object = MibTableColumn
configIPortQueueClpDiscardThreshold = _ConfigIPortQueueClpDiscardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1, 7),
    _ConfigIPortQueueClpDiscardThreshold_Type()
)
configIPortQueueClpDiscardThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortQueueClpDiscardThreshold.setStatus("mandatory")
_ConfigIPortQueueSize_Type = Integer32
_ConfigIPortQueueSize_Object = MibTableColumn
configIPortQueueSize = _ConfigIPortQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1, 8),
    _ConfigIPortQueueSize_Type()
)
configIPortQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIPortQueueSize.setStatus("mandatory")
_ConfigIPortQueueLogClr_Type = Integer32
_ConfigIPortQueueLogClr_Object = MibTableColumn
configIPortQueueLogClr = _ConfigIPortQueueLogClr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1, 9),
    _ConfigIPortQueueLogClr_Type()
)
configIPortQueueLogClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortQueueLogClr.setStatus("mandatory")
_ConfigIPortQueueCdv_Type = Integer32
_ConfigIPortQueueCdv_Object = MibTableColumn
configIPortQueueCdv = _ConfigIPortQueueCdv_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 16, 9, 1, 10),
    _ConfigIPortQueueCdv_Type()
)
configIPortQueueCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIPortQueueCdv.setStatus("mandatory")
_ConfigPvpPvc_ObjectIdentity = ObjectIdentity
configPvpPvc = _ConfigPvpPvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17)
)
_PvpSetupTableNextIndex_Type = Integer32
_PvpSetupTableNextIndex_Object = MibScalar
pvpSetupTableNextIndex = _PvpSetupTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 1),
    _PvpSetupTableNextIndex_Type()
)
pvpSetupTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvpSetupTableNextIndex.setStatus("mandatory")
_PvpSetupTable_Object = MibTable
pvpSetupTable = _PvpSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2)
)
if mibBuilder.loadTexts:
    pvpSetupTable.setStatus("mandatory")
_PvpSetupEntry_Object = MibTableRow
pvpSetupEntry = _PvpSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1)
)
pvpSetupEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "pvpSetupIndex"),
)
if mibBuilder.loadTexts:
    pvpSetupEntry.setStatus("mandatory")
_PvpSetupIndex_Type = Integer32
_PvpSetupIndex_Object = MibTableColumn
pvpSetupIndex = _PvpSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1, 1),
    _PvpSetupIndex_Type()
)
pvpSetupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvpSetupIndex.setStatus("mandatory")


class _PvpSetupApplication_Type(Integer32):
    """Custom type pvpSetupApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("softPvpOriginatorVpl", 2),
          ("transitVp", 1))
    )


_PvpSetupApplication_Type.__name__ = "Integer32"
_PvpSetupApplication_Object = MibTableColumn
pvpSetupApplication = _PvpSetupApplication_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1, 2),
    _PvpSetupApplication_Type()
)
pvpSetupApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvpSetupApplication.setStatus("mandatory")
_PvpSetupLowEPortIndex_Type = Integer32
_PvpSetupLowEPortIndex_Object = MibTableColumn
pvpSetupLowEPortIndex = _PvpSetupLowEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1, 3),
    _PvpSetupLowEPortIndex_Type()
)
pvpSetupLowEPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvpSetupLowEPortIndex.setStatus("mandatory")
_PvpSetupLowVpi_Type = Integer32
_PvpSetupLowVpi_Object = MibTableColumn
pvpSetupLowVpi = _PvpSetupLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1, 4),
    _PvpSetupLowVpi_Type()
)
pvpSetupLowVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvpSetupLowVpi.setStatus("mandatory")
_PvpSetupHighEPortIndex_Type = Integer32
_PvpSetupHighEPortIndex_Object = MibTableColumn
pvpSetupHighEPortIndex = _PvpSetupHighEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1, 5),
    _PvpSetupHighEPortIndex_Type()
)
pvpSetupHighEPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvpSetupHighEPortIndex.setStatus("mandatory")
_PvpSetupHighVpi_Type = Integer32
_PvpSetupHighVpi_Object = MibTableColumn
pvpSetupHighVpi = _PvpSetupHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1, 6),
    _PvpSetupHighVpi_Type()
)
pvpSetupHighVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvpSetupHighVpi.setStatus("mandatory")
_PvpSetupVpCrossConnectIndex_Type = Integer32
_PvpSetupVpCrossConnectIndex_Object = MibTableColumn
pvpSetupVpCrossConnectIndex = _PvpSetupVpCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1, 7),
    _PvpSetupVpCrossConnectIndex_Type()
)
pvpSetupVpCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvpSetupVpCrossConnectIndex.setStatus("mandatory")
_PvpSetupL2HTrafficDescriptorIndex_Type = Integer32
_PvpSetupL2HTrafficDescriptorIndex_Object = MibTableColumn
pvpSetupL2HTrafficDescriptorIndex = _PvpSetupL2HTrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1, 8),
    _PvpSetupL2HTrafficDescriptorIndex_Type()
)
pvpSetupL2HTrafficDescriptorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvpSetupL2HTrafficDescriptorIndex.setStatus("mandatory")
_PvpSetupH2LTrafficDescriptorIndex_Type = Integer32
_PvpSetupH2LTrafficDescriptorIndex_Object = MibTableColumn
pvpSetupH2LTrafficDescriptorIndex = _PvpSetupH2LTrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1, 9),
    _PvpSetupH2LTrafficDescriptorIndex_Type()
)
pvpSetupH2LTrafficDescriptorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvpSetupH2LTrafficDescriptorIndex.setStatus("mandatory")


class _PvpSetupRowStatus_Type(Integer32):
    """Custom type pvpSetupRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_PvpSetupRowStatus_Type.__name__ = "Integer32"
_PvpSetupRowStatus_Object = MibTableColumn
pvpSetupRowStatus = _PvpSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 2, 1, 10),
    _PvpSetupRowStatus_Type()
)
pvpSetupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvpSetupRowStatus.setStatus("mandatory")
_PvcSetupTableNextIndex_Type = Integer32
_PvcSetupTableNextIndex_Object = MibScalar
pvcSetupTableNextIndex = _PvcSetupTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 3),
    _PvcSetupTableNextIndex_Type()
)
pvcSetupTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcSetupTableNextIndex.setStatus("mandatory")
_PvcSetupTable_Object = MibTable
pvcSetupTable = _PvcSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4)
)
if mibBuilder.loadTexts:
    pvcSetupTable.setStatus("mandatory")
_PvcSetupEntry_Object = MibTableRow
pvcSetupEntry = _PvcSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1)
)
pvcSetupEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "pvcSetupIndex"),
)
if mibBuilder.loadTexts:
    pvcSetupEntry.setStatus("mandatory")
_PvcSetupIndex_Type = Integer32
_PvcSetupIndex_Object = MibTableColumn
pvcSetupIndex = _PvcSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 1),
    _PvcSetupIndex_Type()
)
pvcSetupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcSetupIndex.setStatus("mandatory")


class _PvcSetupApplication_Type(Integer32):
    """Custom type pvcSetupApplication based on Integer32"""
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
        *(("busMcastSendVcl", 5),
          ("classicalIpArpSrvVcl", 3),
          ("lesCntrlDirectVcl", 4),
          ("softPvcOriginatorVcl", 2),
          ("transitVc", 1))
    )


_PvcSetupApplication_Type.__name__ = "Integer32"
_PvcSetupApplication_Object = MibTableColumn
pvcSetupApplication = _PvcSetupApplication_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 2),
    _PvcSetupApplication_Type()
)
pvcSetupApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSetupApplication.setStatus("mandatory")
_PvcSetupLowEPortIndex_Type = Integer32
_PvcSetupLowEPortIndex_Object = MibTableColumn
pvcSetupLowEPortIndex = _PvcSetupLowEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 3),
    _PvcSetupLowEPortIndex_Type()
)
pvcSetupLowEPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSetupLowEPortIndex.setStatus("mandatory")
_PvcSetupLowVpi_Type = Integer32
_PvcSetupLowVpi_Object = MibTableColumn
pvcSetupLowVpi = _PvcSetupLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 4),
    _PvcSetupLowVpi_Type()
)
pvcSetupLowVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSetupLowVpi.setStatus("mandatory")
_PvcSetupLowVci_Type = Integer32
_PvcSetupLowVci_Object = MibTableColumn
pvcSetupLowVci = _PvcSetupLowVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 5),
    _PvcSetupLowVci_Type()
)
pvcSetupLowVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSetupLowVci.setStatus("mandatory")
_PvcSetupHighEPortIndex_Type = Integer32
_PvcSetupHighEPortIndex_Object = MibTableColumn
pvcSetupHighEPortIndex = _PvcSetupHighEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 6),
    _PvcSetupHighEPortIndex_Type()
)
pvcSetupHighEPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSetupHighEPortIndex.setStatus("mandatory")
_PvcSetupHighVpi_Type = Integer32
_PvcSetupHighVpi_Object = MibTableColumn
pvcSetupHighVpi = _PvcSetupHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 7),
    _PvcSetupHighVpi_Type()
)
pvcSetupHighVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSetupHighVpi.setStatus("mandatory")
_PvcSetupHighVci_Type = Integer32
_PvcSetupHighVci_Object = MibTableColumn
pvcSetupHighVci = _PvcSetupHighVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 8),
    _PvcSetupHighVci_Type()
)
pvcSetupHighVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSetupHighVci.setStatus("mandatory")
_PvcSetupVcCrossConnectIndex_Type = Integer32
_PvcSetupVcCrossConnectIndex_Object = MibTableColumn
pvcSetupVcCrossConnectIndex = _PvcSetupVcCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 9),
    _PvcSetupVcCrossConnectIndex_Type()
)
pvcSetupVcCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcSetupVcCrossConnectIndex.setStatus("mandatory")
_PvcSetupL2HTrafficDescriptorIndex_Type = Integer32
_PvcSetupL2HTrafficDescriptorIndex_Object = MibTableColumn
pvcSetupL2HTrafficDescriptorIndex = _PvcSetupL2HTrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 10),
    _PvcSetupL2HTrafficDescriptorIndex_Type()
)
pvcSetupL2HTrafficDescriptorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSetupL2HTrafficDescriptorIndex.setStatus("mandatory")
_PvcSetupH2LTrafficDescriptorIndex_Type = Integer32
_PvcSetupH2LTrafficDescriptorIndex_Object = MibTableColumn
pvcSetupH2LTrafficDescriptorIndex = _PvcSetupH2LTrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 11),
    _PvcSetupH2LTrafficDescriptorIndex_Type()
)
pvcSetupH2LTrafficDescriptorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSetupH2LTrafficDescriptorIndex.setStatus("mandatory")


class _PvcSetupRowStatus_Type(Integer32):
    """Custom type pvcSetupRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_PvcSetupRowStatus_Type.__name__ = "Integer32"
_PvcSetupRowStatus_Object = MibTableColumn
pvcSetupRowStatus = _PvcSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 17, 4, 1, 12),
    _PvcSetupRowStatus_Type()
)
pvcSetupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSetupRowStatus.setStatus("mandatory")
_ConfigSvpSvc_ObjectIdentity = ObjectIdentity
configSvpSvc = _ConfigSvpSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18)
)
_SvpSetupTableNextIndex_Type = Integer32
_SvpSetupTableNextIndex_Object = MibScalar
svpSetupTableNextIndex = _SvpSetupTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 1),
    _SvpSetupTableNextIndex_Type()
)
svpSetupTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svpSetupTableNextIndex.setStatus("mandatory")
_SvpSetupTable_Object = MibTable
svpSetupTable = _SvpSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2)
)
if mibBuilder.loadTexts:
    svpSetupTable.setStatus("mandatory")
_SvpSetupEntry_Object = MibTableRow
svpSetupEntry = _SvpSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2, 1)
)
svpSetupEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "svpSetupIndex"),
)
if mibBuilder.loadTexts:
    svpSetupEntry.setStatus("mandatory")
_SvpSetupIndex_Type = Integer32
_SvpSetupIndex_Object = MibTableColumn
svpSetupIndex = _SvpSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2, 1, 1),
    _SvpSetupIndex_Type()
)
svpSetupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svpSetupIndex.setStatus("mandatory")


class _SvpSetupApplication_Type(Integer32):
    """Custom type svpSetupApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tunnel", 1)
    )


_SvpSetupApplication_Type.__name__ = "Integer32"
_SvpSetupApplication_Object = MibTableColumn
svpSetupApplication = _SvpSetupApplication_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2, 1, 2),
    _SvpSetupApplication_Type()
)
svpSetupApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svpSetupApplication.setStatus("mandatory")
_SvpSetupEPortIndex_Type = Integer32
_SvpSetupEPortIndex_Object = MibTableColumn
svpSetupEPortIndex = _SvpSetupEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2, 1, 3),
    _SvpSetupEPortIndex_Type()
)
svpSetupEPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svpSetupEPortIndex.setStatus("mandatory")
_SvpSetupPreferredVpi_Type = Integer32
_SvpSetupPreferredVpi_Object = MibTableColumn
svpSetupPreferredVpi = _SvpSetupPreferredVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2, 1, 4),
    _SvpSetupPreferredVpi_Type()
)
svpSetupPreferredVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svpSetupPreferredVpi.setStatus("mandatory")
_SvpSetupTermAtmAddr_Type = AtmAddress
_SvpSetupTermAtmAddr_Object = MibTableColumn
svpSetupTermAtmAddr = _SvpSetupTermAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2, 1, 5),
    _SvpSetupTermAtmAddr_Type()
)
svpSetupTermAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svpSetupTermAtmAddr.setStatus("mandatory")
_SvpSetupVpCrossConnectIndex_Type = Integer32
_SvpSetupVpCrossConnectIndex_Object = MibTableColumn
svpSetupVpCrossConnectIndex = _SvpSetupVpCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2, 1, 6),
    _SvpSetupVpCrossConnectIndex_Type()
)
svpSetupVpCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svpSetupVpCrossConnectIndex.setStatus("mandatory")
_SvpSetupTxTrafficDescriptorIndex_Type = Integer32
_SvpSetupTxTrafficDescriptorIndex_Object = MibTableColumn
svpSetupTxTrafficDescriptorIndex = _SvpSetupTxTrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2, 1, 7),
    _SvpSetupTxTrafficDescriptorIndex_Type()
)
svpSetupTxTrafficDescriptorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svpSetupTxTrafficDescriptorIndex.setStatus("mandatory")
_SvpSetupRxTrafficDescriptorIndex_Type = Integer32
_SvpSetupRxTrafficDescriptorIndex_Object = MibTableColumn
svpSetupRxTrafficDescriptorIndex = _SvpSetupRxTrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2, 1, 8),
    _SvpSetupRxTrafficDescriptorIndex_Type()
)
svpSetupRxTrafficDescriptorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svpSetupRxTrafficDescriptorIndex.setStatus("mandatory")


class _SvpSetupRowStatus_Type(Integer32):
    """Custom type svpSetupRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_SvpSetupRowStatus_Type.__name__ = "Integer32"
_SvpSetupRowStatus_Object = MibTableColumn
svpSetupRowStatus = _SvpSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 2, 1, 9),
    _SvpSetupRowStatus_Type()
)
svpSetupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svpSetupRowStatus.setStatus("mandatory")
_SvcSetupTableNextIndex_Type = Integer32
_SvcSetupTableNextIndex_Object = MibScalar
svcSetupTableNextIndex = _SvcSetupTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 3),
    _SvcSetupTableNextIndex_Type()
)
svcSetupTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSetupTableNextIndex.setStatus("mandatory")
_SvcSetupTable_Object = MibTable
svcSetupTable = _SvcSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 4)
)
if mibBuilder.loadTexts:
    svcSetupTable.setStatus("mandatory")
_SvcSetupEntry_Object = MibTableRow
svcSetupEntry = _SvcSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 4, 1)
)
svcSetupEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "svcSetupIndex"),
)
if mibBuilder.loadTexts:
    svcSetupEntry.setStatus("mandatory")
_SvcSetupIndex_Type = Integer32
_SvcSetupIndex_Object = MibTableColumn
svcSetupIndex = _SvcSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 4, 1, 1),
    _SvcSetupIndex_Type()
)
svcSetupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSetupIndex.setStatus("mandatory")


class _SvcSetupApplication_Type(Integer32):
    """Custom type svcSetupApplication based on Integer32"""
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
        *(("busMcastSendSvc", 4),
          ("classicalIpArpSrv", 1),
          ("lecsConfigDirectSvc", 2),
          ("lesCntrlDirectSvc", 3))
    )


_SvcSetupApplication_Type.__name__ = "Integer32"
_SvcSetupApplication_Object = MibTableColumn
svcSetupApplication = _SvcSetupApplication_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 4, 1, 2),
    _SvcSetupApplication_Type()
)
svcSetupApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSetupApplication.setStatus("mandatory")
_SvcSetupTermAtmAddr_Type = AtmAddress
_SvcSetupTermAtmAddr_Object = MibTableColumn
svcSetupTermAtmAddr = _SvcSetupTermAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 4, 1, 3),
    _SvcSetupTermAtmAddr_Type()
)
svcSetupTermAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcSetupTermAtmAddr.setStatus("mandatory")
_SvcSetupVcCrossConnectIndex_Type = Integer32
_SvcSetupVcCrossConnectIndex_Object = MibTableColumn
svcSetupVcCrossConnectIndex = _SvcSetupVcCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 4, 1, 4),
    _SvcSetupVcCrossConnectIndex_Type()
)
svcSetupVcCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSetupVcCrossConnectIndex.setStatus("mandatory")
_SvcSetupTxTrafficDescriptorIndex_Type = Integer32
_SvcSetupTxTrafficDescriptorIndex_Object = MibTableColumn
svcSetupTxTrafficDescriptorIndex = _SvcSetupTxTrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 4, 1, 5),
    _SvcSetupTxTrafficDescriptorIndex_Type()
)
svcSetupTxTrafficDescriptorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcSetupTxTrafficDescriptorIndex.setStatus("mandatory")
_SvcSetupRxTrafficDescriptorIndex_Type = Integer32
_SvcSetupRxTrafficDescriptorIndex_Object = MibTableColumn
svcSetupRxTrafficDescriptorIndex = _SvcSetupRxTrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 4, 1, 6),
    _SvcSetupRxTrafficDescriptorIndex_Type()
)
svcSetupRxTrafficDescriptorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcSetupRxTrafficDescriptorIndex.setStatus("mandatory")


class _SvcSetupRowStatus_Type(Integer32):
    """Custom type svcSetupRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_SvcSetupRowStatus_Type.__name__ = "Integer32"
_SvcSetupRowStatus_Object = MibTableColumn
svcSetupRowStatus = _SvcSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 18, 4, 1, 7),
    _SvcSetupRowStatus_Type()
)
svcSetupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcSetupRowStatus.setStatus("mandatory")
_ConfigCommonSignalling_ObjectIdentity = ObjectIdentity
configCommonSignalling = _ConfigCommonSignalling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19)
)


class _ConfigCommonSignallingMaxTunnels_Type(Integer32):
    """Custom type configCommonSignallingMaxTunnels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ConfigCommonSignallingMaxTunnels_Type.__name__ = "Integer32"
_ConfigCommonSignallingMaxTunnels_Object = MibScalar
configCommonSignallingMaxTunnels = _ConfigCommonSignallingMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 1),
    _ConfigCommonSignallingMaxTunnels_Type()
)
configCommonSignallingMaxTunnels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingMaxTunnels.setStatus("mandatory")


class _ConfigCommonSignallingMaxSaps_Type(Integer32):
    """Custom type configCommonSignallingMaxSaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_ConfigCommonSignallingMaxSaps_Type.__name__ = "Integer32"
_ConfigCommonSignallingMaxSaps_Object = MibScalar
configCommonSignallingMaxSaps = _ConfigCommonSignallingMaxSaps_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 2),
    _ConfigCommonSignallingMaxSaps_Type()
)
configCommonSignallingMaxSaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingMaxSaps.setStatus("mandatory")


class _ConfigCommonSignallingMaxPvcs_Type(Integer32):
    """Custom type configCommonSignallingMaxPvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_ConfigCommonSignallingMaxPvcs_Type.__name__ = "Integer32"
_ConfigCommonSignallingMaxPvcs_Object = MibScalar
configCommonSignallingMaxPvcs = _ConfigCommonSignallingMaxPvcs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 3),
    _ConfigCommonSignallingMaxPvcs_Type()
)
configCommonSignallingMaxPvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingMaxPvcs.setStatus("obsolete")


class _ConfigCommonSignallingMaxSvcs_Type(Integer32):
    """Custom type configCommonSignallingMaxSvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_ConfigCommonSignallingMaxSvcs_Type.__name__ = "Integer32"
_ConfigCommonSignallingMaxSvcs_Object = MibScalar
configCommonSignallingMaxSvcs = _ConfigCommonSignallingMaxSvcs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 4),
    _ConfigCommonSignallingMaxSvcs_Type()
)
configCommonSignallingMaxSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingMaxSvcs.setStatus("mandatory")


class _ConfigCommonSignallingMaxConManStevs_Type(Integer32):
    """Custom type configCommonSignallingMaxConManStevs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ConfigCommonSignallingMaxConManStevs_Type.__name__ = "Integer32"
_ConfigCommonSignallingMaxConManStevs_Object = MibScalar
configCommonSignallingMaxConManStevs = _ConfigCommonSignallingMaxConManStevs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 5),
    _ConfigCommonSignallingMaxConManStevs_Type()
)
configCommonSignallingMaxConManStevs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingMaxConManStevs.setStatus("obsolete")


class _ConfigCommonSignallingMaxSigProtStevs_Type(Integer32):
    """Custom type configCommonSignallingMaxSigProtStevs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ConfigCommonSignallingMaxSigProtStevs_Type.__name__ = "Integer32"
_ConfigCommonSignallingMaxSigProtStevs_Object = MibScalar
configCommonSignallingMaxSigProtStevs = _ConfigCommonSignallingMaxSigProtStevs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 6),
    _ConfigCommonSignallingMaxSigProtStevs_Type()
)
configCommonSignallingMaxSigProtStevs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingMaxSigProtStevs.setStatus("mandatory")


class _ConfigCommonSignallingT301_Type(Integer32):
    """Custom type configCommonSignallingT301 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConfigCommonSignallingT301_Type.__name__ = "Integer32"
_ConfigCommonSignallingT301_Object = MibScalar
configCommonSignallingT301 = _ConfigCommonSignallingT301_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 7),
    _ConfigCommonSignallingT301_Type()
)
configCommonSignallingT301.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT301.setStatus("mandatory")


class _ConfigCommonSignallingT302_Type(Integer32):
    """Custom type configCommonSignallingT302 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT302_Type.__name__ = "Integer32"
_ConfigCommonSignallingT302_Object = MibScalar
configCommonSignallingT302 = _ConfigCommonSignallingT302_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 8),
    _ConfigCommonSignallingT302_Type()
)
configCommonSignallingT302.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT302.setStatus("mandatory")


class _ConfigCommonSignallingT303_Type(Integer32):
    """Custom type configCommonSignallingT303 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT303_Type.__name__ = "Integer32"
_ConfigCommonSignallingT303_Object = MibScalar
configCommonSignallingT303 = _ConfigCommonSignallingT303_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 9),
    _ConfigCommonSignallingT303_Type()
)
configCommonSignallingT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT303.setStatus("mandatory")


class _ConfigCommonSignallingT304_Type(Integer32):
    """Custom type configCommonSignallingT304 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT304_Type.__name__ = "Integer32"
_ConfigCommonSignallingT304_Object = MibScalar
configCommonSignallingT304 = _ConfigCommonSignallingT304_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 10),
    _ConfigCommonSignallingT304_Type()
)
configCommonSignallingT304.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT304.setStatus("mandatory")


class _ConfigCommonSignallingT306_Type(Integer32):
    """Custom type configCommonSignallingT306 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT306_Type.__name__ = "Integer32"
_ConfigCommonSignallingT306_Object = MibScalar
configCommonSignallingT306 = _ConfigCommonSignallingT306_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 11),
    _ConfigCommonSignallingT306_Type()
)
configCommonSignallingT306.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT306.setStatus("mandatory")


class _ConfigCommonSignallingT308_Type(Integer32):
    """Custom type configCommonSignallingT308 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT308_Type.__name__ = "Integer32"
_ConfigCommonSignallingT308_Object = MibScalar
configCommonSignallingT308 = _ConfigCommonSignallingT308_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 12),
    _ConfigCommonSignallingT308_Type()
)
configCommonSignallingT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT308.setStatus("mandatory")


class _ConfigCommonSignallingT309_Type(Integer32):
    """Custom type configCommonSignallingT309 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT309_Type.__name__ = "Integer32"
_ConfigCommonSignallingT309_Object = MibScalar
configCommonSignallingT309 = _ConfigCommonSignallingT309_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 13),
    _ConfigCommonSignallingT309_Type()
)
configCommonSignallingT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT309.setStatus("mandatory")


class _ConfigCommonSignallingT310_Type(Integer32):
    """Custom type configCommonSignallingT310 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT310_Type.__name__ = "Integer32"
_ConfigCommonSignallingT310_Object = MibScalar
configCommonSignallingT310 = _ConfigCommonSignallingT310_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 14),
    _ConfigCommonSignallingT310_Type()
)
configCommonSignallingT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT310.setStatus("mandatory")


class _ConfigCommonSignallingT313_Type(Integer32):
    """Custom type configCommonSignallingT313 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT313_Type.__name__ = "Integer32"
_ConfigCommonSignallingT313_Object = MibScalar
configCommonSignallingT313 = _ConfigCommonSignallingT313_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 15),
    _ConfigCommonSignallingT313_Type()
)
configCommonSignallingT313.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT313.setStatus("mandatory")


class _ConfigCommonSignallingT316_Type(Integer32):
    """Custom type configCommonSignallingT316 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT316_Type.__name__ = "Integer32"
_ConfigCommonSignallingT316_Object = MibScalar
configCommonSignallingT316 = _ConfigCommonSignallingT316_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 16),
    _ConfigCommonSignallingT316_Type()
)
configCommonSignallingT316.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT316.setStatus("mandatory")


class _ConfigCommonSignallingT317_Type(Integer32):
    """Custom type configCommonSignallingT317 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT317_Type.__name__ = "Integer32"
_ConfigCommonSignallingT317_Object = MibScalar
configCommonSignallingT317 = _ConfigCommonSignallingT317_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 17),
    _ConfigCommonSignallingT317_Type()
)
configCommonSignallingT317.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT317.setStatus("mandatory")


class _ConfigCommonSignallingT322_Type(Integer32):
    """Custom type configCommonSignallingT322 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT322_Type.__name__ = "Integer32"
_ConfigCommonSignallingT322_Object = MibScalar
configCommonSignallingT322 = _ConfigCommonSignallingT322_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 18),
    _ConfigCommonSignallingT322_Type()
)
configCommonSignallingT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT322.setStatus("mandatory")


class _ConfigCommonSignallingT331_Type(Integer32):
    """Custom type configCommonSignallingT331 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT331_Type.__name__ = "Integer32"
_ConfigCommonSignallingT331_Object = MibScalar
configCommonSignallingT331 = _ConfigCommonSignallingT331_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 19),
    _ConfigCommonSignallingT331_Type()
)
configCommonSignallingT331.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT331.setStatus("mandatory")


class _ConfigCommonSignallingT333_Type(Integer32):
    """Custom type configCommonSignallingT333 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT333_Type.__name__ = "Integer32"
_ConfigCommonSignallingT333_Object = MibScalar
configCommonSignallingT333 = _ConfigCommonSignallingT333_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 20),
    _ConfigCommonSignallingT333_Type()
)
configCommonSignallingT333.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT333.setStatus("obsolete")


class _ConfigCommonSignallingT397_Type(Integer32):
    """Custom type configCommonSignallingT397 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ConfigCommonSignallingT397_Type.__name__ = "Integer32"
_ConfigCommonSignallingT397_Object = MibScalar
configCommonSignallingT397 = _ConfigCommonSignallingT397_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 21),
    _ConfigCommonSignallingT397_Type()
)
configCommonSignallingT397.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT397.setStatus("mandatory")


class _ConfigCommonSignallingT398_Type(Integer32):
    """Custom type configCommonSignallingT398 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT398_Type.__name__ = "Integer32"
_ConfigCommonSignallingT398_Object = MibScalar
configCommonSignallingT398 = _ConfigCommonSignallingT398_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 22),
    _ConfigCommonSignallingT398_Type()
)
configCommonSignallingT398.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT398.setStatus("mandatory")


class _ConfigCommonSignallingT399_Type(Integer32):
    """Custom type configCommonSignallingT399 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingT399_Type.__name__ = "Integer32"
_ConfigCommonSignallingT399_Object = MibScalar
configCommonSignallingT399 = _ConfigCommonSignallingT399_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 23),
    _ConfigCommonSignallingT399_Type()
)
configCommonSignallingT399.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingT399.setStatus("mandatory")


class _ConfigCommonSignallingPtmpMaxLeafs_Type(Integer32):
    """Custom type configCommonSignallingPtmpMaxLeafs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_ConfigCommonSignallingPtmpMaxLeafs_Type.__name__ = "Integer32"
_ConfigCommonSignallingPtmpMaxLeafs_Object = MibScalar
configCommonSignallingPtmpMaxLeafs = _ConfigCommonSignallingPtmpMaxLeafs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 24),
    _ConfigCommonSignallingPtmpMaxLeafs_Type()
)
configCommonSignallingPtmpMaxLeafs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingPtmpMaxLeafs.setStatus("mandatory")


class _ConfigCommonSignallingPtmpMaxLeafOperations_Type(Integer32):
    """Custom type configCommonSignallingPtmpMaxLeafOperations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ConfigCommonSignallingPtmpMaxLeafOperations_Type.__name__ = "Integer32"
_ConfigCommonSignallingPtmpMaxLeafOperations_Object = MibScalar
configCommonSignallingPtmpMaxLeafOperations = _ConfigCommonSignallingPtmpMaxLeafOperations_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 25),
    _ConfigCommonSignallingPtmpMaxLeafOperations_Type()
)
configCommonSignallingPtmpMaxLeafOperations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingPtmpMaxLeafOperations.setStatus("mandatory")


class _ConfigCommonSignallingPtmpMaxLeafsDropByClear_Type(Integer32):
    """Custom type configCommonSignallingPtmpMaxLeafsDropByClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSignallingPtmpMaxLeafsDropByClear_Type.__name__ = "Integer32"
_ConfigCommonSignallingPtmpMaxLeafsDropByClear_Object = MibScalar
configCommonSignallingPtmpMaxLeafsDropByClear = _ConfigCommonSignallingPtmpMaxLeafsDropByClear_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 26),
    _ConfigCommonSignallingPtmpMaxLeafsDropByClear_Type()
)
configCommonSignallingPtmpMaxLeafsDropByClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingPtmpMaxLeafsDropByClear.setStatus("mandatory")


class _ConfigCommonSignallingPtmpMaxP2mpSvcs_Type(Integer32):
    """Custom type configCommonSignallingPtmpMaxP2mpSvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ConfigCommonSignallingPtmpMaxP2mpSvcs_Type.__name__ = "Integer32"
_ConfigCommonSignallingPtmpMaxP2mpSvcs_Object = MibScalar
configCommonSignallingPtmpMaxP2mpSvcs = _ConfigCommonSignallingPtmpMaxP2mpSvcs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 27),
    _ConfigCommonSignallingPtmpMaxP2mpSvcs_Type()
)
configCommonSignallingPtmpMaxP2mpSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSignallingPtmpMaxP2mpSvcs.setStatus("mandatory")
_ConfigCommonSscopMaxSaps_Type = Integer32
_ConfigCommonSscopMaxSaps_Object = MibScalar
configCommonSscopMaxSaps = _ConfigCommonSscopMaxSaps_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 28),
    _ConfigCommonSscopMaxSaps_Type()
)
configCommonSscopMaxSaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopMaxSaps.setStatus("obsolete")
_ConfigCommonSscopMaxLinks_Type = Integer32
_ConfigCommonSscopMaxLinks_Object = MibScalar
configCommonSscopMaxLinks = _ConfigCommonSscopMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 29),
    _ConfigCommonSscopMaxLinks_Type()
)
configCommonSscopMaxLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopMaxLinks.setStatus("obsolete")


class _ConfigCommonSscopMaxRcvWinSize_Type(Integer32):
    """Custom type configCommonSscopMaxRcvWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_ConfigCommonSscopMaxRcvWinSize_Type.__name__ = "Integer32"
_ConfigCommonSscopMaxRcvWinSize_Object = MibScalar
configCommonSscopMaxRcvWinSize = _ConfigCommonSscopMaxRcvWinSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 30),
    _ConfigCommonSscopMaxRcvWinSize_Type()
)
configCommonSscopMaxRcvWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopMaxRcvWinSize.setStatus("mandatory")


class _ConfigCommonSscopMaxCc_Type(Integer32):
    """Custom type configCommonSscopMaxCc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSscopMaxCc_Type.__name__ = "Integer32"
_ConfigCommonSscopMaxCc_Object = MibScalar
configCommonSscopMaxCc = _ConfigCommonSscopMaxCc_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 31),
    _ConfigCommonSscopMaxCc_Type()
)
configCommonSscopMaxCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopMaxCc.setStatus("mandatory")


class _ConfigCommonSscopMaxPd_Type(Integer32):
    """Custom type configCommonSscopMaxPd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSscopMaxPd_Type.__name__ = "Integer32"
_ConfigCommonSscopMaxPd_Object = MibScalar
configCommonSscopMaxPd = _ConfigCommonSscopMaxPd_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 32),
    _ConfigCommonSscopMaxPd_Type()
)
configCommonSscopMaxPd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopMaxPd.setStatus("mandatory")


class _ConfigCommonSscopMaxStat_Type(Integer32):
    """Custom type configCommonSscopMaxStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1023),
    )


_ConfigCommonSscopMaxStat_Type.__name__ = "Integer32"
_ConfigCommonSscopMaxStat_Object = MibScalar
configCommonSscopMaxStat = _ConfigCommonSscopMaxStat_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 33),
    _ConfigCommonSscopMaxStat_Type()
)
configCommonSscopMaxStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopMaxStat.setStatus("mandatory")


class _ConfigCommonSscopTimerPoll_Type(Integer32):
    """Custom type configCommonSscopTimerPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ConfigCommonSscopTimerPoll_Type.__name__ = "Integer32"
_ConfigCommonSscopTimerPoll_Object = MibScalar
configCommonSscopTimerPoll = _ConfigCommonSscopTimerPoll_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 34),
    _ConfigCommonSscopTimerPoll_Type()
)
configCommonSscopTimerPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopTimerPoll.setStatus("mandatory")


class _ConfigCommonSscopTimerNoResponse_Type(Integer32):
    """Custom type configCommonSscopTimerNoResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSscopTimerNoResponse_Type.__name__ = "Integer32"
_ConfigCommonSscopTimerNoResponse_Object = MibScalar
configCommonSscopTimerNoResponse = _ConfigCommonSscopTimerNoResponse_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 35),
    _ConfigCommonSscopTimerNoResponse_Type()
)
configCommonSscopTimerNoResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopTimerNoResponse.setStatus("mandatory")


class _ConfigCommonSscopTimerKeepAlive_Type(Integer32):
    """Custom type configCommonSscopTimerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSscopTimerKeepAlive_Type.__name__ = "Integer32"
_ConfigCommonSscopTimerKeepAlive_Object = MibScalar
configCommonSscopTimerKeepAlive = _ConfigCommonSscopTimerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 36),
    _ConfigCommonSscopTimerKeepAlive_Type()
)
configCommonSscopTimerKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopTimerKeepAlive.setStatus("mandatory")


class _ConfigCommonSscopTimerIdle_Type(Integer32):
    """Custom type configCommonSscopTimerIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSscopTimerIdle_Type.__name__ = "Integer32"
_ConfigCommonSscopTimerIdle_Object = MibScalar
configCommonSscopTimerIdle = _ConfigCommonSscopTimerIdle_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 37),
    _ConfigCommonSscopTimerIdle_Type()
)
configCommonSscopTimerIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopTimerIdle.setStatus("mandatory")


class _ConfigCommonSscopTimerCc_Type(Integer32):
    """Custom type configCommonSscopTimerCc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConfigCommonSscopTimerCc_Type.__name__ = "Integer32"
_ConfigCommonSscopTimerCc_Object = MibScalar
configCommonSscopTimerCc = _ConfigCommonSscopTimerCc_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 38),
    _ConfigCommonSscopTimerCc_Type()
)
configCommonSscopTimerCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopTimerCc.setStatus("mandatory")


class _ConfigCommonSscopMaxSduSize_Type(Integer32):
    """Custom type configCommonSscopMaxSduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_ConfigCommonSscopMaxSduSize_Type.__name__ = "Integer32"
_ConfigCommonSscopMaxSduSize_Object = MibScalar
configCommonSscopMaxSduSize = _ConfigCommonSscopMaxSduSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 39),
    _ConfigCommonSscopMaxSduSize_Type()
)
configCommonSscopMaxSduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopMaxSduSize.setStatus("mandatory")


class _ConfigCommonSscopMaxUuSize_Type(Integer32):
    """Custom type configCommonSscopMaxUuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_ConfigCommonSscopMaxUuSize_Type.__name__ = "Integer32"
_ConfigCommonSscopMaxUuSize_Object = MibScalar
configCommonSscopMaxUuSize = _ConfigCommonSscopMaxUuSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 19, 40),
    _ConfigCommonSscopMaxUuSize_Type()
)
configCommonSscopMaxUuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommonSscopMaxUuSize.setStatus("mandatory")
_ConfigIisp_ObjectIdentity = ObjectIdentity
configIisp = _ConfigIisp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 20)
)
_ConfigNextHopRoutingTableNextIndex_Type = Integer32
_ConfigNextHopRoutingTableNextIndex_Object = MibScalar
configNextHopRoutingTableNextIndex = _ConfigNextHopRoutingTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 20, 1),
    _ConfigNextHopRoutingTableNextIndex_Type()
)
configNextHopRoutingTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configNextHopRoutingTableNextIndex.setStatus("mandatory")
_ConfigNextHopRoutingTable_Object = MibTable
configNextHopRoutingTable = _ConfigNextHopRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 20, 2)
)
if mibBuilder.loadTexts:
    configNextHopRoutingTable.setStatus("mandatory")
_ConfigNextHopRoutingEntry_Object = MibTableRow
configNextHopRoutingEntry = _ConfigNextHopRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 20, 2, 1)
)
configNextHopRoutingEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configNextHopRoutingIndex"),
)
if mibBuilder.loadTexts:
    configNextHopRoutingEntry.setStatus("mandatory")
_ConfigNextHopRoutingIndex_Type = Integer32
_ConfigNextHopRoutingIndex_Object = MibTableColumn
configNextHopRoutingIndex = _ConfigNextHopRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 20, 2, 1, 1),
    _ConfigNextHopRoutingIndex_Type()
)
configNextHopRoutingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configNextHopRoutingIndex.setStatus("mandatory")
_ConfigNextHopRoutingAtmAddress_Type = AtmAddress
_ConfigNextHopRoutingAtmAddress_Object = MibTableColumn
configNextHopRoutingAtmAddress = _ConfigNextHopRoutingAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 20, 2, 1, 2),
    _ConfigNextHopRoutingAtmAddress_Type()
)
configNextHopRoutingAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNextHopRoutingAtmAddress.setStatus("mandatory")
_ConfigNextHopRoutingAddressLength_Type = Integer32
_ConfigNextHopRoutingAddressLength_Object = MibTableColumn
configNextHopRoutingAddressLength = _ConfigNextHopRoutingAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 20, 2, 1, 3),
    _ConfigNextHopRoutingAddressLength_Type()
)
configNextHopRoutingAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNextHopRoutingAddressLength.setStatus("mandatory")
_ConfigNextHopRoutingEPort_Type = Integer32
_ConfigNextHopRoutingEPort_Object = MibTableColumn
configNextHopRoutingEPort = _ConfigNextHopRoutingEPort_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 20, 2, 1, 4),
    _ConfigNextHopRoutingEPort_Type()
)
configNextHopRoutingEPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNextHopRoutingEPort.setStatus("mandatory")


class _ConfigNextHopRoutingSignallingType_Type(Integer32):
    """Custom type configNextHopRoutingSignallingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("networkSide", 2),
          ("userSide", 1))
    )


_ConfigNextHopRoutingSignallingType_Type.__name__ = "Integer32"
_ConfigNextHopRoutingSignallingType_Object = MibTableColumn
configNextHopRoutingSignallingType = _ConfigNextHopRoutingSignallingType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 20, 2, 1, 5),
    _ConfigNextHopRoutingSignallingType_Type()
)
configNextHopRoutingSignallingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNextHopRoutingSignallingType.setStatus("obsolete")


class _ConfigNextHopRoutingRowStatus_Type(Integer32):
    """Custom type configNextHopRoutingRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ConfigNextHopRoutingRowStatus_Type.__name__ = "Integer32"
_ConfigNextHopRoutingRowStatus_Object = MibTableColumn
configNextHopRoutingRowStatus = _ConfigNextHopRoutingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 20, 2, 1, 6),
    _ConfigNextHopRoutingRowStatus_Type()
)
configNextHopRoutingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNextHopRoutingRowStatus.setStatus("mandatory")
_ConfigIpArp_ObjectIdentity = ObjectIdentity
configIpArp = _ConfigIpArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21)
)
_AtmIpArpTable_Object = MibTable
atmIpArpTable = _AtmIpArpTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 1)
)
if mibBuilder.loadTexts:
    atmIpArpTable.setStatus("mandatory")
_AtmIpArpEntry_Object = MibTableRow
atmIpArpEntry = _AtmIpArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 1, 1)
)
atmIpArpEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "atmIpArpServerIndex"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "atmIpArpIpAddress"),
)
if mibBuilder.loadTexts:
    atmIpArpEntry.setStatus("mandatory")
_AtmIpArpServerIndex_Type = Integer32
_AtmIpArpServerIndex_Object = MibTableColumn
atmIpArpServerIndex = _AtmIpArpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 1, 1, 1),
    _AtmIpArpServerIndex_Type()
)
atmIpArpServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIpArpServerIndex.setStatus("mandatory")
_AtmIpArpIpAddress_Type = IpAddress
_AtmIpArpIpAddress_Object = MibTableColumn
atmIpArpIpAddress = _AtmIpArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 1, 1, 2),
    _AtmIpArpIpAddress_Type()
)
atmIpArpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIpArpIpAddress.setStatus("mandatory")
_AtmIpArpAtmAddress_Type = AtmAddress
_AtmIpArpAtmAddress_Object = MibTableColumn
atmIpArpAtmAddress = _AtmIpArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 1, 1, 3),
    _AtmIpArpAtmAddress_Type()
)
atmIpArpAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIpArpAtmAddress.setStatus("mandatory")


class _AtmIpArpType_Type(Integer32):
    """Custom type atmIpArpType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_AtmIpArpType_Type.__name__ = "Integer32"
_AtmIpArpType_Object = MibTableColumn
atmIpArpType = _AtmIpArpType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 1, 1, 4),
    _AtmIpArpType_Type()
)
atmIpArpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIpArpType.setStatus("mandatory")
_ConfigIpArpServerTableNextIndex_Type = Integer32
_ConfigIpArpServerTableNextIndex_Object = MibScalar
configIpArpServerTableNextIndex = _ConfigIpArpServerTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 2),
    _ConfigIpArpServerTableNextIndex_Type()
)
configIpArpServerTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIpArpServerTableNextIndex.setStatus("mandatory")
_ConfigIpArpServerTable_Object = MibTable
configIpArpServerTable = _ConfigIpArpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3)
)
if mibBuilder.loadTexts:
    configIpArpServerTable.setStatus("mandatory")
_ConfigIpArpServerEntry_Object = MibTableRow
configIpArpServerEntry = _ConfigIpArpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3, 1)
)
configIpArpServerEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configIpArpServerIndex"),
)
if mibBuilder.loadTexts:
    configIpArpServerEntry.setStatus("mandatory")
_ConfigIpArpServerIndex_Type = Integer32
_ConfigIpArpServerIndex_Object = MibTableColumn
configIpArpServerIndex = _ConfigIpArpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3, 1, 1),
    _ConfigIpArpServerIndex_Type()
)
configIpArpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIpArpServerIndex.setStatus("mandatory")
_ConfigIpArpServerAtmAddressSpec_Type = AtmAddress
_ConfigIpArpServerAtmAddressSpec_Object = MibTableColumn
configIpArpServerAtmAddressSpec = _ConfigIpArpServerAtmAddressSpec_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3, 1, 2),
    _ConfigIpArpServerAtmAddressSpec_Type()
)
configIpArpServerAtmAddressSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpArpServerAtmAddressSpec.setStatus("mandatory")
_ConfigIpArpServerAtmAddressMask_Type = AtmAddress
_ConfigIpArpServerAtmAddressMask_Object = MibTableColumn
configIpArpServerAtmAddressMask = _ConfigIpArpServerAtmAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3, 1, 3),
    _ConfigIpArpServerAtmAddressMask_Type()
)
configIpArpServerAtmAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpArpServerAtmAddressMask.setStatus("mandatory")
_ConfigIpArpServerAtmAddressActual_Type = AtmAddress
_ConfigIpArpServerAtmAddressActual_Object = MibTableColumn
configIpArpServerAtmAddressActual = _ConfigIpArpServerAtmAddressActual_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3, 1, 4),
    _ConfigIpArpServerAtmAddressActual_Type()
)
configIpArpServerAtmAddressActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIpArpServerAtmAddressActual.setStatus("mandatory")
_ConfigIpArpServerIpSubnetAddress_Type = IpAddress
_ConfigIpArpServerIpSubnetAddress_Object = MibTableColumn
configIpArpServerIpSubnetAddress = _ConfigIpArpServerIpSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3, 1, 5),
    _ConfigIpArpServerIpSubnetAddress_Type()
)
configIpArpServerIpSubnetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpArpServerIpSubnetAddress.setStatus("mandatory")
_ConfigIpArpServerIpSubnetMask_Type = IpAddress
_ConfigIpArpServerIpSubnetMask_Object = MibTableColumn
configIpArpServerIpSubnetMask = _ConfigIpArpServerIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3, 1, 6),
    _ConfigIpArpServerIpSubnetMask_Type()
)
configIpArpServerIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpArpServerIpSubnetMask.setStatus("mandatory")


class _ConfigIpArpServerAdminStatus_Type(Integer32):
    """Custom type configIpArpServerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ConfigIpArpServerAdminStatus_Type.__name__ = "Integer32"
_ConfigIpArpServerAdminStatus_Object = MibTableColumn
configIpArpServerAdminStatus = _ConfigIpArpServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3, 1, 7),
    _ConfigIpArpServerAdminStatus_Type()
)
configIpArpServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpArpServerAdminStatus.setStatus("mandatory")


class _ConfigIpArpServerOperStatus_Type(Integer32):
    """Custom type configIpArpServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_ConfigIpArpServerOperStatus_Type.__name__ = "Integer32"
_ConfigIpArpServerOperStatus_Object = MibTableColumn
configIpArpServerOperStatus = _ConfigIpArpServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3, 1, 8),
    _ConfigIpArpServerOperStatus_Type()
)
configIpArpServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIpArpServerOperStatus.setStatus("mandatory")


class _ConfigIpArpServerRowStatus_Type(Integer32):
    """Custom type configIpArpServerRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ConfigIpArpServerRowStatus_Type.__name__ = "Integer32"
_ConfigIpArpServerRowStatus_Object = MibTableColumn
configIpArpServerRowStatus = _ConfigIpArpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 3, 1, 9),
    _ConfigIpArpServerRowStatus_Type()
)
configIpArpServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpArpServerRowStatus.setStatus("mandatory")
_ConfigClipArpServer_Type = AtmAddress
_ConfigClipArpServer_Object = MibScalar
configClipArpServer = _ConfigClipArpServer_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 21, 4),
    _ConfigClipArpServer_Type()
)
configClipArpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configClipArpServer.setStatus("mandatory")
_ConfigQosClass_ObjectIdentity = ObjectIdentity
configQosClass = _ConfigQosClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 22)
)
_QosClassTable_Object = MibTable
qosClassTable = _QosClassTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 22, 1)
)
if mibBuilder.loadTexts:
    qosClassTable.setStatus("mandatory")
_QosClassEntry_Object = MibTableRow
qosClassEntry = _QosClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 22, 1, 1)
)
qosClassEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "qosClassClass"),
)
if mibBuilder.loadTexts:
    qosClassEntry.setStatus("mandatory")


class _QosClassClass_Type(Integer32):
    """Custom type qosClassClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_QosClassClass_Type.__name__ = "Integer32"
_QosClassClass_Object = MibTableColumn
qosClassClass = _QosClassClass_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 22, 1, 1, 1),
    _QosClassClass_Type()
)
qosClassClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosClassClass.setStatus("mandatory")
_QosClassCtd_Type = Integer32
_QosClassCtd_Object = MibTableColumn
qosClassCtd = _QosClassCtd_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 22, 1, 1, 2),
    _QosClassCtd_Type()
)
qosClassCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosClassCtd.setStatus("mandatory")
_QosClassCdv_Type = Integer32
_QosClassCdv_Object = MibTableColumn
qosClassCdv = _QosClassCdv_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 22, 1, 1, 3),
    _QosClassCdv_Type()
)
qosClassCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosClassCdv.setStatus("mandatory")
_QosClassLogClr_Type = Integer32
_QosClassLogClr_Object = MibTableColumn
qosClassLogClr = _QosClassLogClr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 22, 1, 1, 4),
    _QosClassLogClr_Type()
)
qosClassLogClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosClassLogClr.setStatus("mandatory")
_ConfigSerial_ObjectIdentity = ObjectIdentity
configSerial = _ConfigSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 23)
)


class _ConfigSerialObmSlip_Type(Integer32):
    """Custom type configSerialObmSlip based on Integer32"""
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
          ("obm", 2),
          ("slip", 3))
    )


_ConfigSerialObmSlip_Type.__name__ = "Integer32"
_ConfigSerialObmSlip_Object = MibScalar
configSerialObmSlip = _ConfigSerialObmSlip_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 23, 1),
    _ConfigSerialObmSlip_Type()
)
configSerialObmSlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSerialObmSlip.setStatus("mandatory")
_ConfigOam_ObjectIdentity = ObjectIdentity
configOam = _ConfigOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24)
)
_IfMIBObjects_ObjectIdentity = ObjectIdentity
ifMIBObjects = _IfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 1)
)
_IfTestTable_Object = MibTable
ifTestTable = _IfTestTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 1, 3)
)
if mibBuilder.loadTexts:
    ifTestTable.setStatus("mandatory")
_IfTestEntry_Object = MibTableRow
ifTestEntry = _IfTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 1, 3, 1)
)
ifTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifTestEntry.setStatus("mandatory")


class _IfTestId_Type(Integer32):
    """Custom type ifTestId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfTestId_Type.__name__ = "Integer32"
_IfTestId_Object = MibTableColumn
ifTestId = _IfTestId_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 1, 3, 1, 1),
    _IfTestId_Type()
)
ifTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestId.setStatus("mandatory")


class _IfTestStatus_Type(Integer32):
    """Custom type ifTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 2),
          ("notInUse", 1))
    )


_IfTestStatus_Type.__name__ = "Integer32"
_IfTestStatus_Object = MibTableColumn
ifTestStatus = _IfTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 1, 3, 1, 2),
    _IfTestStatus_Type()
)
ifTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestStatus.setStatus("mandatory")
_IfTestType_Type = ObjectIdentifier
_IfTestType_Object = MibTableColumn
ifTestType = _IfTestType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 1, 3, 1, 3),
    _IfTestType_Type()
)
ifTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestType.setStatus("mandatory")


class _IfTestResult_Type(Integer32):
    """Custom type ifTestResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_IfTestResult_Type.__name__ = "Integer32"
_IfTestResult_Object = MibTableColumn
ifTestResult = _IfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 1, 3, 1, 4),
    _IfTestResult_Type()
)
ifTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTestResult.setStatus("mandatory")
_IfTestCode_Type = ObjectIdentifier
_IfTestCode_Object = MibTableColumn
ifTestCode = _IfTestCode_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 1, 3, 1, 5),
    _IfTestCode_Type()
)
ifTestCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTestCode.setStatus("mandatory")


class _IfTestOwner_Type(OctetString):
    """Custom type ifTestOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfTestOwner_Type.__name__ = "OctetString"
_IfTestOwner_Object = MibTableColumn
ifTestOwner = _IfTestOwner_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 1, 3, 1, 6),
    _IfTestOwner_Type()
)
ifTestOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestOwner.setStatus("mandatory")
_AtmTESTMIBObjects_ObjectIdentity = ObjectIdentity
atmTESTMIBObjects = _AtmTESTMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 2)
)
_AtmLoopbackTestGroup_ObjectIdentity = ObjectIdentity
atmLoopbackTestGroup = _AtmLoopbackTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 2, 1)
)
_AtmLoopbackTestTypes_ObjectIdentity = ObjectIdentity
atmLoopbackTestTypes = _AtmLoopbackTestTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 2, 1, 4)
)
_AtmLoopbackVpE2e_ObjectIdentity = ObjectIdentity
atmLoopbackVpE2e = _AtmLoopbackVpE2e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 2, 1, 4, 1)
)
_AtmLoopbackVcE2e_ObjectIdentity = ObjectIdentity
atmLoopbackVcE2e = _AtmLoopbackVcE2e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 2, 1, 4, 2)
)
_AtmLoopbackVpSegment_ObjectIdentity = ObjectIdentity
atmLoopbackVpSegment = _AtmLoopbackVpSegment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 2, 1, 4, 3)
)
_AtmLoopbackVcSegment_ObjectIdentity = ObjectIdentity
atmLoopbackVcSegment = _AtmLoopbackVcSegment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 24, 2, 1, 4, 4)
)
_ConfigTest_ObjectIdentity = ObjectIdentity
configTest = _ConfigTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 25)
)
_ControlDeleteCode_Type = Integer32
_ControlDeleteCode_Object = MibScalar
controlDeleteCode = _ControlDeleteCode_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 25, 1),
    _ControlDeleteCode_Type()
)
controlDeleteCode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    controlDeleteCode.setStatus("optional")
_ControlDeleteConfig_Type = Integer32
_ControlDeleteConfig_Object = MibScalar
controlDeleteConfig = _ControlDeleteConfig_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 25, 2),
    _ControlDeleteConfig_Type()
)
controlDeleteConfig.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    controlDeleteConfig.setStatus("optional")
_ConfigPriorityBuffer_ObjectIdentity = ObjectIdentity
configPriorityBuffer = _ConfigPriorityBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 26)
)
_ConfigPriorityBufferTable_Object = MibTable
configPriorityBufferTable = _ConfigPriorityBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 26, 1)
)
if mibBuilder.loadTexts:
    configPriorityBufferTable.setStatus("mandatory")
_ConfigPriorityBufferEntry_Object = MibTableRow
configPriorityBufferEntry = _ConfigPriorityBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 26, 1, 1)
)
configPriorityBufferEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "configPriorityBufferIndex"),
)
if mibBuilder.loadTexts:
    configPriorityBufferEntry.setStatus("mandatory")


class _ConfigPriorityBufferIndex_Type(Integer32):
    """Custom type configPriorityBufferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ConfigPriorityBufferIndex_Type.__name__ = "Integer32"
_ConfigPriorityBufferIndex_Object = MibTableColumn
configPriorityBufferIndex = _ConfigPriorityBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 26, 1, 1, 1),
    _ConfigPriorityBufferIndex_Type()
)
configPriorityBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPriorityBufferIndex.setStatus("mandatory")
_ConfigPriorityBufferSize_Type = Integer32
_ConfigPriorityBufferSize_Object = MibTableColumn
configPriorityBufferSize = _ConfigPriorityBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 2, 26, 1, 1, 2),
    _ConfigPriorityBufferSize_Type()
)
configPriorityBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPriorityBufferSize.setStatus("mandatory")
_CrossfireAtmStatus_ObjectIdentity = ObjectIdentity
crossfireAtmStatus = _CrossfireAtmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3)
)
_StatusBasicHw_ObjectIdentity = ObjectIdentity
statusBasicHw = _StatusBasicHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1)
)


class _StatusHwChassisCurrentXModules_Type(Integer32):
    """Custom type statusHwChassisCurrentXModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_StatusHwChassisCurrentXModules_Type.__name__ = "Integer32"
_StatusHwChassisCurrentXModules_Object = MibScalar
statusHwChassisCurrentXModules = _StatusHwChassisCurrentXModules_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 1),
    _StatusHwChassisCurrentXModules_Type()
)
statusHwChassisCurrentXModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusHwChassisCurrentXModules.setStatus("mandatory")


class _StatusHwChassisCurrentEPorts_Type(Integer32):
    """Custom type statusHwChassisCurrentEPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_StatusHwChassisCurrentEPorts_Type.__name__ = "Integer32"
_StatusHwChassisCurrentEPorts_Object = MibScalar
statusHwChassisCurrentEPorts = _StatusHwChassisCurrentEPorts_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 2),
    _StatusHwChassisCurrentEPorts_Type()
)
statusHwChassisCurrentEPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusHwChassisCurrentEPorts.setStatus("mandatory")


class _StatusHwChassisUpsOperState_Type(Integer32):
    """Custom type statusHwChassisUpsOperState based on Integer32"""
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
        *(("failed", 3),
          ("inUse", 2),
          ("notPresent", 4),
          ("operational", 1))
    )


_StatusHwChassisUpsOperState_Type.__name__ = "Integer32"
_StatusHwChassisUpsOperState_Object = MibScalar
statusHwChassisUpsOperState = _StatusHwChassisUpsOperState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 3),
    _StatusHwChassisUpsOperState_Type()
)
statusHwChassisUpsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusHwChassisUpsOperState.setStatus("mandatory")


class _StatusHwChassisSwitchingSystemSize_Type(Integer32):
    """Custom type statusHwChassisSwitchingSystemSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 32),
    )


_StatusHwChassisSwitchingSystemSize_Type.__name__ = "Integer32"
_StatusHwChassisSwitchingSystemSize_Object = MibScalar
statusHwChassisSwitchingSystemSize = _StatusHwChassisSwitchingSystemSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 4),
    _StatusHwChassisSwitchingSystemSize_Type()
)
statusHwChassisSwitchingSystemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusHwChassisSwitchingSystemSize.setStatus("mandatory")


class _StatusHwChassisCellBufferSize_Type(Integer32):
    """Custom type statusHwChassisCellBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 64),
    )


_StatusHwChassisCellBufferSize_Type.__name__ = "Integer32"
_StatusHwChassisCellBufferSize_Object = MibScalar
statusHwChassisCellBufferSize = _StatusHwChassisCellBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 5),
    _StatusHwChassisCellBufferSize_Type()
)
statusHwChassisCellBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusHwChassisCellBufferSize.setStatus("mandatory")


class _StatusCurrentTemperatureConditionState_Type(Integer32):
    """Custom type statusCurrentTemperatureConditionState based on Integer32"""
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
        *(("high", 4),
          ("highDecreasing", 2),
          ("normal", 1),
          ("normalIncreasing", 3))
    )


_StatusCurrentTemperatureConditionState_Type.__name__ = "Integer32"
_StatusCurrentTemperatureConditionState_Object = MibScalar
statusCurrentTemperatureConditionState = _StatusCurrentTemperatureConditionState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 6),
    _StatusCurrentTemperatureConditionState_Type()
)
statusCurrentTemperatureConditionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusCurrentTemperatureConditionState.setStatus("mandatory")
_StatusCurrentTemperatureGauge_Type = Gauge32
_StatusCurrentTemperatureGauge_Object = MibScalar
statusCurrentTemperatureGauge = _StatusCurrentTemperatureGauge_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 7),
    _StatusCurrentTemperatureGauge_Type()
)
statusCurrentTemperatureGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusCurrentTemperatureGauge.setStatus("mandatory")


class _StatusCurrentTemperatureLatch_Type(Integer32):
    """Custom type statusCurrentTemperatureLatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StatusCurrentTemperatureLatch_Type.__name__ = "Integer32"
_StatusCurrentTemperatureLatch_Object = MibScalar
statusCurrentTemperatureLatch = _StatusCurrentTemperatureLatch_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 8),
    _StatusCurrentTemperatureLatch_Type()
)
statusCurrentTemperatureLatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusCurrentTemperatureLatch.setStatus("mandatory")
_StatusCurrentTemperatureLatchTime_Type = TimeTicks
_StatusCurrentTemperatureLatchTime_Object = MibScalar
statusCurrentTemperatureLatchTime = _StatusCurrentTemperatureLatchTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 9),
    _StatusCurrentTemperatureLatchTime_Type()
)
statusCurrentTemperatureLatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusCurrentTemperatureLatchTime.setStatus("mandatory")


class _StatusFanOperStatus_Type(Integer32):
    """Custom type statusFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_StatusFanOperStatus_Type.__name__ = "Integer32"
_StatusFanOperStatus_Object = MibScalar
statusFanOperStatus = _StatusFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 10),
    _StatusFanOperStatus_Type()
)
statusFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFanOperStatus.setStatus("mandatory")
_StatusPsuStatusTable_Object = MibTable
statusPsuStatusTable = _StatusPsuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 11)
)
if mibBuilder.loadTexts:
    statusPsuStatusTable.setStatus("mandatory")
_StatusPsuStatusEntry_Object = MibTableRow
statusPsuStatusEntry = _StatusPsuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 11, 1)
)
statusPsuStatusEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "statusPsuIndex"),
)
if mibBuilder.loadTexts:
    statusPsuStatusEntry.setStatus("mandatory")


class _StatusPsuIndex_Type(Integer32):
    """Custom type statusPsuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_StatusPsuIndex_Type.__name__ = "Integer32"
_StatusPsuIndex_Object = MibTableColumn
statusPsuIndex = _StatusPsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 11, 1, 1),
    _StatusPsuIndex_Type()
)
statusPsuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPsuIndex.setStatus("mandatory")


class _StatusPsuOperStatus_Type(Integer32):
    """Custom type statusPsuOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_StatusPsuOperStatus_Type.__name__ = "Integer32"
_StatusPsuOperStatus_Object = MibTableColumn
statusPsuOperStatus = _StatusPsuOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 1, 11, 1, 2),
    _StatusPsuOperStatus_Type()
)
statusPsuOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPsuOperStatus.setStatus("mandatory")
_StatusProcessorModule_ObjectIdentity = ObjectIdentity
statusProcessorModule = _StatusProcessorModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 2)
)


class _StatusProcessorModuleStatusLed_Type(Integer32):
    """Custom type statusProcessorModuleStatusLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("off", 1),
          ("on", 2))
    )


_StatusProcessorModuleStatusLed_Type.__name__ = "Integer32"
_StatusProcessorModuleStatusLed_Object = MibScalar
statusProcessorModuleStatusLed = _StatusProcessorModuleStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 2, 1),
    _StatusProcessorModuleStatusLed_Type()
)
statusProcessorModuleStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusProcessorModuleStatusLed.setStatus("mandatory")


class _StatusProcessorModuleFaultLed_Type(Integer32):
    """Custom type statusProcessorModuleFaultLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("off", 1),
          ("on", 2))
    )


_StatusProcessorModuleFaultLed_Type.__name__ = "Integer32"
_StatusProcessorModuleFaultLed_Object = MibScalar
statusProcessorModuleFaultLed = _StatusProcessorModuleFaultLed_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 2, 2),
    _StatusProcessorModuleFaultLed_Type()
)
statusProcessorModuleFaultLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusProcessorModuleFaultLed.setStatus("mandatory")
_StatusFeatureModule_ObjectIdentity = ObjectIdentity
statusFeatureModule = _StatusFeatureModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 3)
)


class _StatusFeatureModuleOperStatus_Type(Integer32):
    """Custom type statusFeatureModuleOperStatus based on Integer32"""
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
        *(("inService", 1),
          ("outOfService", 2),
          ("testing", 3),
          ("unknown", 4))
    )


_StatusFeatureModuleOperStatus_Type.__name__ = "Integer32"
_StatusFeatureModuleOperStatus_Object = MibScalar
statusFeatureModuleOperStatus = _StatusFeatureModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 3, 1),
    _StatusFeatureModuleOperStatus_Type()
)
statusFeatureModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFeatureModuleOperStatus.setStatus("mandatory")


class _StatusFeatureModuleStatusLed_Type(Integer32):
    """Custom type statusFeatureModuleStatusLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("off", 1),
          ("on", 2))
    )


_StatusFeatureModuleStatusLed_Type.__name__ = "Integer32"
_StatusFeatureModuleStatusLed_Object = MibScalar
statusFeatureModuleStatusLed = _StatusFeatureModuleStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 3, 2),
    _StatusFeatureModuleStatusLed_Type()
)
statusFeatureModuleStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFeatureModuleStatusLed.setStatus("mandatory")
_StatusXModule_ObjectIdentity = ObjectIdentity
statusXModule = _StatusXModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4)
)
_StatusXModuleTable_Object = MibTable
statusXModuleTable = _StatusXModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1)
)
if mibBuilder.loadTexts:
    statusXModuleTable.setStatus("mandatory")
_StatusXModuleEntry_Object = MibTableRow
statusXModuleEntry = _StatusXModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1)
)
statusXModuleEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "statusXModuleSlotIndex"),
)
if mibBuilder.loadTexts:
    statusXModuleEntry.setStatus("mandatory")


class _StatusXModuleSlotIndex_Type(Integer32):
    """Custom type statusXModuleSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_StatusXModuleSlotIndex_Type.__name__ = "Integer32"
_StatusXModuleSlotIndex_Object = MibTableColumn
statusXModuleSlotIndex = _StatusXModuleSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 1),
    _StatusXModuleSlotIndex_Type()
)
statusXModuleSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleSlotIndex.setStatus("mandatory")


class _StatusXModuleOperStatus_Type(Integer32):
    """Custom type statusXModuleOperStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabledByManagement", 8),
          ("disabledChanged", 6),
          ("disabledReplaced", 7),
          ("failed", 4),
          ("inService", 2),
          ("lost", 5),
          ("slave", 3),
          ("unknown", 1))
    )


_StatusXModuleOperStatus_Type.__name__ = "Integer32"
_StatusXModuleOperStatus_Object = MibTableColumn
statusXModuleOperStatus = _StatusXModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 2),
    _StatusXModuleOperStatus_Type()
)
statusXModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleOperStatus.setStatus("mandatory")


class _StatusXModuleNoOfSlotsUsed_Type(Integer32):
    """Custom type statusXModuleNoOfSlotsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_StatusXModuleNoOfSlotsUsed_Type.__name__ = "Integer32"
_StatusXModuleNoOfSlotsUsed_Object = MibTableColumn
statusXModuleNoOfSlotsUsed = _StatusXModuleNoOfSlotsUsed_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 3),
    _StatusXModuleNoOfSlotsUsed_Type()
)
statusXModuleNoOfSlotsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleNoOfSlotsUsed.setStatus("mandatory")


class _StatusXModuleIPort1SlotIndex_Type(Integer32):
    """Custom type statusXModuleIPort1SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_StatusXModuleIPort1SlotIndex_Type.__name__ = "Integer32"
_StatusXModuleIPort1SlotIndex_Object = MibTableColumn
statusXModuleIPort1SlotIndex = _StatusXModuleIPort1SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 4),
    _StatusXModuleIPort1SlotIndex_Type()
)
statusXModuleIPort1SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleIPort1SlotIndex.setStatus("mandatory")


class _StatusXModuleIPort1RIndex_Type(Integer32):
    """Custom type statusXModuleIPort1RIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_StatusXModuleIPort1RIndex_Type.__name__ = "Integer32"
_StatusXModuleIPort1RIndex_Object = MibTableColumn
statusXModuleIPort1RIndex = _StatusXModuleIPort1RIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 5),
    _StatusXModuleIPort1RIndex_Type()
)
statusXModuleIPort1RIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleIPort1RIndex.setStatus("mandatory")


class _StatusXModuleIPort2SlotIndex_Type(Integer32):
    """Custom type statusXModuleIPort2SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_StatusXModuleIPort2SlotIndex_Type.__name__ = "Integer32"
_StatusXModuleIPort2SlotIndex_Object = MibTableColumn
statusXModuleIPort2SlotIndex = _StatusXModuleIPort2SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 6),
    _StatusXModuleIPort2SlotIndex_Type()
)
statusXModuleIPort2SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleIPort2SlotIndex.setStatus("mandatory")


class _StatusXModuleIPort2RIndex_Type(Integer32):
    """Custom type statusXModuleIPort2RIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_StatusXModuleIPort2RIndex_Type.__name__ = "Integer32"
_StatusXModuleIPort2RIndex_Object = MibTableColumn
statusXModuleIPort2RIndex = _StatusXModuleIPort2RIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 7),
    _StatusXModuleIPort2RIndex_Type()
)
statusXModuleIPort2RIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleIPort2RIndex.setStatus("mandatory")


class _StatusXModuleIPort3SlotIndex_Type(Integer32):
    """Custom type statusXModuleIPort3SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_StatusXModuleIPort3SlotIndex_Type.__name__ = "Integer32"
_StatusXModuleIPort3SlotIndex_Object = MibTableColumn
statusXModuleIPort3SlotIndex = _StatusXModuleIPort3SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 8),
    _StatusXModuleIPort3SlotIndex_Type()
)
statusXModuleIPort3SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleIPort3SlotIndex.setStatus("mandatory")


class _StatusXModuleIPort3RIndex_Type(Integer32):
    """Custom type statusXModuleIPort3RIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_StatusXModuleIPort3RIndex_Type.__name__ = "Integer32"
_StatusXModuleIPort3RIndex_Object = MibTableColumn
statusXModuleIPort3RIndex = _StatusXModuleIPort3RIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 9),
    _StatusXModuleIPort3RIndex_Type()
)
statusXModuleIPort3RIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleIPort3RIndex.setStatus("mandatory")


class _StatusXModuleIPort4SlotIndex_Type(Integer32):
    """Custom type statusXModuleIPort4SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_StatusXModuleIPort4SlotIndex_Type.__name__ = "Integer32"
_StatusXModuleIPort4SlotIndex_Object = MibTableColumn
statusXModuleIPort4SlotIndex = _StatusXModuleIPort4SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 10),
    _StatusXModuleIPort4SlotIndex_Type()
)
statusXModuleIPort4SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleIPort4SlotIndex.setStatus("mandatory")


class _StatusXModuleIPort4RIndex_Type(Integer32):
    """Custom type statusXModuleIPort4RIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_StatusXModuleIPort4RIndex_Type.__name__ = "Integer32"
_StatusXModuleIPort4RIndex_Object = MibTableColumn
statusXModuleIPort4RIndex = _StatusXModuleIPort4RIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 4, 1, 1, 11),
    _StatusXModuleIPort4RIndex_Type()
)
statusXModuleIPort4RIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusXModuleIPort4RIndex.setStatus("mandatory")
_StatusEPort_ObjectIdentity = ObjectIdentity
statusEPort = _StatusEPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6)
)
_StatusEPortTable_Object = MibTable
statusEPortTable = _StatusEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1)
)
if mibBuilder.loadTexts:
    statusEPortTable.setStatus("mandatory")
_StatusEPortEntry_Object = MibTableRow
statusEPortEntry = _StatusEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1)
)
statusEPortEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "statusEPortIfIndex"),
)
if mibBuilder.loadTexts:
    statusEPortEntry.setStatus("mandatory")
_StatusEPortIfIndex_Type = Integer32
_StatusEPortIfIndex_Object = MibTableColumn
statusEPortIfIndex = _StatusEPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 1),
    _StatusEPortIfIndex_Type()
)
statusEPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortIfIndex.setStatus("mandatory")


class _StatusEPortXModuleIndex_Type(Integer32):
    """Custom type statusEPortXModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_StatusEPortXModuleIndex_Type.__name__ = "Integer32"
_StatusEPortXModuleIndex_Object = MibTableColumn
statusEPortXModuleIndex = _StatusEPortXModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 2),
    _StatusEPortXModuleIndex_Type()
)
statusEPortXModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortXModuleIndex.setStatus("mandatory")


class _StatusEPortRIndex_Type(Integer32):
    """Custom type statusEPortRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_StatusEPortRIndex_Type.__name__ = "Integer32"
_StatusEPortRIndex_Object = MibTableColumn
statusEPortRIndex = _StatusEPortRIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 3),
    _StatusEPortRIndex_Type()
)
statusEPortRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortRIndex.setStatus("mandatory")


class _StatusEPortOperStatus_Type(Integer32):
    """Custom type statusEPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_StatusEPortOperStatus_Type.__name__ = "Integer32"
_StatusEPortOperStatus_Object = MibTableColumn
statusEPortOperStatus = _StatusEPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 4),
    _StatusEPortOperStatus_Type()
)
statusEPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortOperStatus.setStatus("mandatory")


class _StatusEPortPhyState_Type(Integer32):
    """Custom type statusEPortPhyState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("offlineDisabled", 1),
          ("offlineRestart", 2),
          ("onlineAutoDisable", 7),
          ("onlineNoRxSync", 6),
          ("onlineOk", 3),
          ("onlineSignalLoss", 5),
          ("onlineTesting", 8),
          ("onlineTransPhyFault", 4))
    )


_StatusEPortPhyState_Type.__name__ = "Integer32"
_StatusEPortPhyState_Object = MibTableColumn
statusEPortPhyState = _StatusEPortPhyState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 5),
    _StatusEPortPhyState_Type()
)
statusEPortPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortPhyState.setStatus("mandatory")


class _StatusEPortType_Type(Integer32):
    """Custom type statusEPortType based on Integer32"""
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
        *(("ds3", 8),
          ("mmf155", 3),
          ("mmf622", 5),
          ("none", 1),
          ("smf155", 6),
          ("smf622", 7),
          ("utp155", 4),
          ("utp25", 2),
          ("vpTunnel", 9))
    )


_StatusEPortType_Type.__name__ = "Integer32"
_StatusEPortType_Object = MibTableColumn
statusEPortType = _StatusEPortType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 6),
    _StatusEPortType_Type()
)
statusEPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortType.setStatus("mandatory")


class _StatusEPortRxSyncLedState_Type(Integer32):
    """Custom type statusEPortRxSyncLedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("off", 1),
          ("on", 2))
    )


_StatusEPortRxSyncLedState_Type.__name__ = "Integer32"
_StatusEPortRxSyncLedState_Object = MibTableColumn
statusEPortRxSyncLedState = _StatusEPortRxSyncLedState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 7),
    _StatusEPortRxSyncLedState_Type()
)
statusEPortRxSyncLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortRxSyncLedState.setStatus("mandatory")


class _StatusEPortSignalLossLedState_Type(Integer32):
    """Custom type statusEPortSignalLossLedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("off", 1),
          ("on", 2))
    )


_StatusEPortSignalLossLedState_Type.__name__ = "Integer32"
_StatusEPortSignalLossLedState_Object = MibTableColumn
statusEPortSignalLossLedState = _StatusEPortSignalLossLedState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 8),
    _StatusEPortSignalLossLedState_Type()
)
statusEPortSignalLossLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortSignalLossLedState.setStatus("mandatory")
_StatusEPortPhyPortIndex_Type = Integer32
_StatusEPortPhyPortIndex_Object = MibTableColumn
statusEPortPhyPortIndex = _StatusEPortPhyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 9),
    _StatusEPortPhyPortIndex_Type()
)
statusEPortPhyPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortPhyPortIndex.setStatus("mandatory")


class _StatusEPortLoopbackState_Type(Integer32):
    """Custom type statusEPortLoopbackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_StatusEPortLoopbackState_Type.__name__ = "Integer32"
_StatusEPortLoopbackState_Object = MibTableColumn
statusEPortLoopbackState = _StatusEPortLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 10),
    _StatusEPortLoopbackState_Type()
)
statusEPortLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortLoopbackState.setStatus("mandatory")
_StatusEPortLoopbackErrorCode_Type = OctetString
_StatusEPortLoopbackErrorCode_Object = MibTableColumn
statusEPortLoopbackErrorCode = _StatusEPortLoopbackErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 11),
    _StatusEPortLoopbackErrorCode_Type()
)
statusEPortLoopbackErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortLoopbackErrorCode.setStatus("mandatory")


class _StatusEPortIlmiState_Type(Integer32):
    """Custom type statusEPortIlmiState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cleanUp", 8),
          ("configuring", 4),
          ("establishing", 3),
          ("linkFailing", 2),
          ("registering", 6),
          ("retrieving", 5),
          ("stopped", 1),
          ("verifying", 7))
    )


_StatusEPortIlmiState_Type.__name__ = "Integer32"
_StatusEPortIlmiState_Object = MibTableColumn
statusEPortIlmiState = _StatusEPortIlmiState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 12),
    _StatusEPortIlmiState_Type()
)
statusEPortIlmiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortIlmiState.setStatus("mandatory")
_StatusEPortAdjInfoTransmissionType_Type = Integer32
_StatusEPortAdjInfoTransmissionType_Object = MibTableColumn
statusEPortAdjInfoTransmissionType = _StatusEPortAdjInfoTransmissionType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 13),
    _StatusEPortAdjInfoTransmissionType_Type()
)
statusEPortAdjInfoTransmissionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoTransmissionType.setStatus("mandatory")
_StatusEPortAdjInfoMediaType_Type = Integer32
_StatusEPortAdjInfoMediaType_Object = MibTableColumn
statusEPortAdjInfoMediaType = _StatusEPortAdjInfoMediaType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 14),
    _StatusEPortAdjInfoMediaType_Type()
)
statusEPortAdjInfoMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoMediaType.setStatus("mandatory")
_StatusEPortAdjInfoIfName_Type = DisplayString
_StatusEPortAdjInfoIfName_Object = MibTableColumn
statusEPortAdjInfoIfName = _StatusEPortAdjInfoIfName_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 15),
    _StatusEPortAdjInfoIfName_Type()
)
statusEPortAdjInfoIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoIfName.setStatus("mandatory")


class _StatusEPortAdjInfoSystemIdentifier_Type(OctetString):
    """Custom type statusEPortAdjInfoSystemIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_StatusEPortAdjInfoSystemIdentifier_Type.__name__ = "OctetString"
_StatusEPortAdjInfoSystemIdentifier_Object = MibTableColumn
statusEPortAdjInfoSystemIdentifier = _StatusEPortAdjInfoSystemIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 16),
    _StatusEPortAdjInfoSystemIdentifier_Type()
)
statusEPortAdjInfoSystemIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoSystemIdentifier.setStatus("mandatory")
_StatusEPortAdjInfoMaxVpcs_Type = Integer32
_StatusEPortAdjInfoMaxVpcs_Object = MibTableColumn
statusEPortAdjInfoMaxVpcs = _StatusEPortAdjInfoMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 17),
    _StatusEPortAdjInfoMaxVpcs_Type()
)
statusEPortAdjInfoMaxVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoMaxVpcs.setStatus("mandatory")
_StatusEPortAdjInfoMaxVccs_Type = Integer32
_StatusEPortAdjInfoMaxVccs_Object = MibTableColumn
statusEPortAdjInfoMaxVccs = _StatusEPortAdjInfoMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 18),
    _StatusEPortAdjInfoMaxVccs_Type()
)
statusEPortAdjInfoMaxVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoMaxVccs.setStatus("mandatory")
_StatusEPortAdjInfoMaxVpiBits_Type = Integer32
_StatusEPortAdjInfoMaxVpiBits_Object = MibTableColumn
statusEPortAdjInfoMaxVpiBits = _StatusEPortAdjInfoMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 19),
    _StatusEPortAdjInfoMaxVpiBits_Type()
)
statusEPortAdjInfoMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoMaxVpiBits.setStatus("mandatory")
_StatusEPortAdjInfoMaxVciBits_Type = Integer32
_StatusEPortAdjInfoMaxVciBits_Object = MibTableColumn
statusEPortAdjInfoMaxVciBits = _StatusEPortAdjInfoMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 20),
    _StatusEPortAdjInfoMaxVciBits_Type()
)
statusEPortAdjInfoMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoMaxVciBits.setStatus("mandatory")


class _StatusEPortAdjInfoUniType_Type(Integer32):
    """Custom type statusEPortAdjInfoUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_StatusEPortAdjInfoUniType_Type.__name__ = "Integer32"
_StatusEPortAdjInfoUniType_Object = MibTableColumn
statusEPortAdjInfoUniType = _StatusEPortAdjInfoUniType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 21),
    _StatusEPortAdjInfoUniType_Type()
)
statusEPortAdjInfoUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoUniType.setStatus("mandatory")


class _StatusEPortAdjInfoUniVersion_Type(Integer32):
    """Custom type statusEPortAdjInfoUniVersion based on Integer32"""
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
        *(("version2point0", 1),
          ("version3point0", 2),
          ("version3point1", 3),
          ("version4point0", 4))
    )


_StatusEPortAdjInfoUniVersion_Type.__name__ = "Integer32"
_StatusEPortAdjInfoUniVersion_Object = MibTableColumn
statusEPortAdjInfoUniVersion = _StatusEPortAdjInfoUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 22),
    _StatusEPortAdjInfoUniVersion_Type()
)
statusEPortAdjInfoUniVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoUniVersion.setStatus("mandatory")


class _StatusEPortAdjInfoDeviceType_Type(Integer32):
    """Custom type statusEPortAdjInfoDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("user", 1))
    )


_StatusEPortAdjInfoDeviceType_Type.__name__ = "Integer32"
_StatusEPortAdjInfoDeviceType_Object = MibTableColumn
statusEPortAdjInfoDeviceType = _StatusEPortAdjInfoDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 23),
    _StatusEPortAdjInfoDeviceType_Type()
)
statusEPortAdjInfoDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoDeviceType.setStatus("mandatory")


class _StatusEPortAdjInfoIlmiVersion_Type(Integer32):
    """Custom type statusEPortAdjInfoIlmiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("version4point0", 2))
    )


_StatusEPortAdjInfoIlmiVersion_Type.__name__ = "Integer32"
_StatusEPortAdjInfoIlmiVersion_Object = MibTableColumn
statusEPortAdjInfoIlmiVersion = _StatusEPortAdjInfoIlmiVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 24),
    _StatusEPortAdjInfoIlmiVersion_Type()
)
statusEPortAdjInfoIlmiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoIlmiVersion.setStatus("mandatory")


class _StatusEPortAdjInfoNniSigVersion_Type(Integer32):
    """Custom type statusEPortAdjInfoNniSigVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 2),
          ("pnniVersion1point0", 3),
          ("unsupported", 1))
    )


_StatusEPortAdjInfoNniSigVersion_Type.__name__ = "Integer32"
_StatusEPortAdjInfoNniSigVersion_Object = MibTableColumn
statusEPortAdjInfoNniSigVersion = _StatusEPortAdjInfoNniSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 25),
    _StatusEPortAdjInfoNniSigVersion_Type()
)
statusEPortAdjInfoNniSigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoNniSigVersion.setStatus("mandatory")
_StatusEPortAutoconfigMaxVpcs_Type = Integer32
_StatusEPortAutoconfigMaxVpcs_Object = MibTableColumn
statusEPortAutoconfigMaxVpcs = _StatusEPortAutoconfigMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 26),
    _StatusEPortAutoconfigMaxVpcs_Type()
)
statusEPortAutoconfigMaxVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAutoconfigMaxVpcs.setStatus("mandatory")
_StatusEPortAutoconfigMaxVccs_Type = Integer32
_StatusEPortAutoconfigMaxVccs_Object = MibTableColumn
statusEPortAutoconfigMaxVccs = _StatusEPortAutoconfigMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 27),
    _StatusEPortAutoconfigMaxVccs_Type()
)
statusEPortAutoconfigMaxVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAutoconfigMaxVccs.setStatus("mandatory")
_StatusEPortAutoconfigMaxVpiBits_Type = Integer32
_StatusEPortAutoconfigMaxVpiBits_Object = MibTableColumn
statusEPortAutoconfigMaxVpiBits = _StatusEPortAutoconfigMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 28),
    _StatusEPortAutoconfigMaxVpiBits_Type()
)
statusEPortAutoconfigMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAutoconfigMaxVpiBits.setStatus("mandatory")
_StatusEPortAutoconfigMaxVciBits_Type = Integer32
_StatusEPortAutoconfigMaxVciBits_Object = MibTableColumn
statusEPortAutoconfigMaxVciBits = _StatusEPortAutoconfigMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 29),
    _StatusEPortAutoconfigMaxVciBits_Type()
)
statusEPortAutoconfigMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAutoconfigMaxVciBits.setStatus("mandatory")


class _StatusEPortAutoconfigUniVersion_Type(Integer32):
    """Custom type statusEPortAutoconfigUniVersion based on Integer32"""
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
        *(("undefined", 1),
          ("version3point0", 2),
          ("version3point1", 3),
          ("version4point0", 4))
    )


_StatusEPortAutoconfigUniVersion_Type.__name__ = "Integer32"
_StatusEPortAutoconfigUniVersion_Object = MibTableColumn
statusEPortAutoconfigUniVersion = _StatusEPortAutoconfigUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 30),
    _StatusEPortAutoconfigUniVersion_Type()
)
statusEPortAutoconfigUniVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAutoconfigUniVersion.setStatus("mandatory")


class _StatusEPortAutoconfigDeviceType_Type(Integer32):
    """Custom type statusEPortAutoconfigDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("user", 1))
    )


_StatusEPortAutoconfigDeviceType_Type.__name__ = "Integer32"
_StatusEPortAutoconfigDeviceType_Object = MibTableColumn
statusEPortAutoconfigDeviceType = _StatusEPortAutoconfigDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 31),
    _StatusEPortAutoconfigDeviceType_Type()
)
statusEPortAutoconfigDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAutoconfigDeviceType.setStatus("mandatory")


class _StatusEPortAutoconfigDerivedInterfaceType_Type(Integer32):
    """Custom type statusEPortAutoconfigDerivedInterfaceType based on Integer32"""
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
        *(("privateNni", 4),
          ("privateUni", 3),
          ("publicUni", 2),
          ("undefined", 1))
    )


_StatusEPortAutoconfigDerivedInterfaceType_Type.__name__ = "Integer32"
_StatusEPortAutoconfigDerivedInterfaceType_Object = MibTableColumn
statusEPortAutoconfigDerivedInterfaceType = _StatusEPortAutoconfigDerivedInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 32),
    _StatusEPortAutoconfigDerivedInterfaceType_Type()
)
statusEPortAutoconfigDerivedInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAutoconfigDerivedInterfaceType.setStatus("mandatory")


class _StatusEPortAutoconfigMaxSvpcVpi_Type(Integer32):
    """Custom type statusEPortAutoconfigMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_StatusEPortAutoconfigMaxSvpcVpi_Type.__name__ = "Integer32"
_StatusEPortAutoconfigMaxSvpcVpi_Object = MibTableColumn
statusEPortAutoconfigMaxSvpcVpi = _StatusEPortAutoconfigMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 33),
    _StatusEPortAutoconfigMaxSvpcVpi_Type()
)
statusEPortAutoconfigMaxSvpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAutoconfigMaxSvpcVpi.setStatus("mandatory")


class _StatusEPortAutoconfigMaxSvccVpi_Type(Integer32):
    """Custom type statusEPortAutoconfigMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_StatusEPortAutoconfigMaxSvccVpi_Type.__name__ = "Integer32"
_StatusEPortAutoconfigMaxSvccVpi_Object = MibTableColumn
statusEPortAutoconfigMaxSvccVpi = _StatusEPortAutoconfigMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 34),
    _StatusEPortAutoconfigMaxSvccVpi_Type()
)
statusEPortAutoconfigMaxSvccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAutoconfigMaxSvccVpi.setStatus("mandatory")


class _StatusEPortAutoconfigMinSvccVci_Type(Integer32):
    """Custom type statusEPortAutoconfigMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_StatusEPortAutoconfigMinSvccVci_Type.__name__ = "Integer32"
_StatusEPortAutoconfigMinSvccVci_Object = MibTableColumn
statusEPortAutoconfigMinSvccVci = _StatusEPortAutoconfigMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 35),
    _StatusEPortAutoconfigMinSvccVci_Type()
)
statusEPortAutoconfigMinSvccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAutoconfigMinSvccVci.setStatus("mandatory")


class _StatusEPortAdjInfoMaxSvpcVpi_Type(Integer32):
    """Custom type statusEPortAdjInfoMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_StatusEPortAdjInfoMaxSvpcVpi_Type.__name__ = "Integer32"
_StatusEPortAdjInfoMaxSvpcVpi_Object = MibTableColumn
statusEPortAdjInfoMaxSvpcVpi = _StatusEPortAdjInfoMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 36),
    _StatusEPortAdjInfoMaxSvpcVpi_Type()
)
statusEPortAdjInfoMaxSvpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoMaxSvpcVpi.setStatus("mandatory")


class _StatusEPortAdjInfoMaxSvccVpi_Type(Integer32):
    """Custom type statusEPortAdjInfoMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_StatusEPortAdjInfoMaxSvccVpi_Type.__name__ = "Integer32"
_StatusEPortAdjInfoMaxSvccVpi_Object = MibTableColumn
statusEPortAdjInfoMaxSvccVpi = _StatusEPortAdjInfoMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 37),
    _StatusEPortAdjInfoMaxSvccVpi_Type()
)
statusEPortAdjInfoMaxSvccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoMaxSvccVpi.setStatus("mandatory")


class _StatusEPortAdjInfoMinSvccVci_Type(Integer32):
    """Custom type statusEPortAdjInfoMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_StatusEPortAdjInfoMinSvccVci_Type.__name__ = "Integer32"
_StatusEPortAdjInfoMinSvccVci_Object = MibTableColumn
statusEPortAdjInfoMinSvccVci = _StatusEPortAdjInfoMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 6, 1, 1, 38),
    _StatusEPortAdjInfoMinSvccVci_Type()
)
statusEPortAdjInfoMinSvccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEPortAdjInfoMinSvccVci.setStatus("mandatory")
_StatusVpcVcc_ObjectIdentity = ObjectIdentity
statusVpcVcc = _StatusVpcVcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7)
)
_VpcExtensionTable_Object = MibTable
vpcExtensionTable = _VpcExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 1)
)
if mibBuilder.loadTexts:
    vpcExtensionTable.setStatus("mandatory")
_VpcExtensionEntry_Object = MibTableRow
vpcExtensionEntry = _VpcExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 1, 1)
)
vpcExtensionEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "vpcExtensionIndex"),
)
if mibBuilder.loadTexts:
    vpcExtensionEntry.setStatus("mandatory")
_VpcExtensionIndex_Type = Integer32
_VpcExtensionIndex_Object = MibTableColumn
vpcExtensionIndex = _VpcExtensionIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 1, 1, 1),
    _VpcExtensionIndex_Type()
)
vpcExtensionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpcExtensionIndex.setStatus("mandatory")
_VpcExtensionVpCrossConnectIndex_Type = Integer32
_VpcExtensionVpCrossConnectIndex_Object = MibTableColumn
vpcExtensionVpCrossConnectIndex = _VpcExtensionVpCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 1, 1, 2),
    _VpcExtensionVpCrossConnectIndex_Type()
)
vpcExtensionVpCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpcExtensionVpCrossConnectIndex.setStatus("mandatory")
_VpcExtensionOrigAtmAddr_Type = AtmAddress
_VpcExtensionOrigAtmAddr_Object = MibTableColumn
vpcExtensionOrigAtmAddr = _VpcExtensionOrigAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 1, 1, 3),
    _VpcExtensionOrigAtmAddr_Type()
)
vpcExtensionOrigAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpcExtensionOrigAtmAddr.setStatus("mandatory")
_VpcExtensionTermAtmAddr_Type = AtmAddress
_VpcExtensionTermAtmAddr_Object = MibTableColumn
vpcExtensionTermAtmAddr = _VpcExtensionTermAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 1, 1, 4),
    _VpcExtensionTermAtmAddr_Type()
)
vpcExtensionTermAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpcExtensionTermAtmAddr.setStatus("mandatory")
_VpcExtensionCapabilities_Type = Integer32
_VpcExtensionCapabilities_Object = MibTableColumn
vpcExtensionCapabilities = _VpcExtensionCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 1, 1, 5),
    _VpcExtensionCapabilities_Type()
)
vpcExtensionCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpcExtensionCapabilities.setStatus("mandatory")
_VccExtensionTable_Object = MibTable
vccExtensionTable = _VccExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 2)
)
if mibBuilder.loadTexts:
    vccExtensionTable.setStatus("mandatory")
_VccExtensionEntry_Object = MibTableRow
vccExtensionEntry = _VccExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 2, 1)
)
vccExtensionEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "vccExtensionIndex"),
)
if mibBuilder.loadTexts:
    vccExtensionEntry.setStatus("mandatory")
_VccExtensionIndex_Type = Integer32
_VccExtensionIndex_Object = MibTableColumn
vccExtensionIndex = _VccExtensionIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 2, 1, 1),
    _VccExtensionIndex_Type()
)
vccExtensionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccExtensionIndex.setStatus("mandatory")
_VccExtensionVcCrossConnectIndex_Type = Integer32
_VccExtensionVcCrossConnectIndex_Object = MibTableColumn
vccExtensionVcCrossConnectIndex = _VccExtensionVcCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 2, 1, 2),
    _VccExtensionVcCrossConnectIndex_Type()
)
vccExtensionVcCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccExtensionVcCrossConnectIndex.setStatus("mandatory")
_VccExtensionOrigAtmAddr_Type = AtmAddress
_VccExtensionOrigAtmAddr_Object = MibTableColumn
vccExtensionOrigAtmAddr = _VccExtensionOrigAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 2, 1, 3),
    _VccExtensionOrigAtmAddr_Type()
)
vccExtensionOrigAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccExtensionOrigAtmAddr.setStatus("mandatory")
_VccExtensionTermAtmAddr_Type = AtmAddress
_VccExtensionTermAtmAddr_Object = MibTableColumn
vccExtensionTermAtmAddr = _VccExtensionTermAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 2, 1, 4),
    _VccExtensionTermAtmAddr_Type()
)
vccExtensionTermAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccExtensionTermAtmAddr.setStatus("mandatory")
_VccExtensionCapabilities_Type = Integer32
_VccExtensionCapabilities_Object = MibTableColumn
vccExtensionCapabilities = _VccExtensionCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 2, 1, 5),
    _VccExtensionCapabilities_Type()
)
vccExtensionCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccExtensionCapabilities.setStatus("mandatory")


class _VccExtensionEarlyPacketDiscard_Type(Integer32):
    """Custom type vccExtensionEarlyPacketDiscard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_VccExtensionEarlyPacketDiscard_Type.__name__ = "Integer32"
_VccExtensionEarlyPacketDiscard_Object = MibTableColumn
vccExtensionEarlyPacketDiscard = _VccExtensionEarlyPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 7, 2, 1, 6),
    _VccExtensionEarlyPacketDiscard_Type()
)
vccExtensionEarlyPacketDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccExtensionEarlyPacketDiscard.setStatus("mandatory")
_StatusFatalLog_ObjectIdentity = ObjectIdentity
statusFatalLog = _StatusFatalLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8)
)
_StatusFatalStatUsed_Type = Integer32
_StatusFatalStatUsed_Object = MibScalar
statusFatalStatUsed = _StatusFatalStatUsed_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 1),
    _StatusFatalStatUsed_Type()
)
statusFatalStatUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalStatUsed.setStatus("mandatory")
_StatusFatalStatFree_Type = Integer32
_StatusFatalStatFree_Object = MibScalar
statusFatalStatFree = _StatusFatalStatFree_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 2),
    _StatusFatalStatFree_Type()
)
statusFatalStatFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalStatFree.setStatus("mandatory")


class _StatusFatalStatOverflow_Type(Integer32):
    """Custom type statusFatalStatOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_StatusFatalStatOverflow_Type.__name__ = "Integer32"
_StatusFatalStatOverflow_Object = MibScalar
statusFatalStatOverflow = _StatusFatalStatOverflow_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 3),
    _StatusFatalStatOverflow_Type()
)
statusFatalStatOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalStatOverflow.setStatus("mandatory")
_StatusFatalStatMaxDumpLength_Type = Integer32
_StatusFatalStatMaxDumpLength_Object = MibScalar
statusFatalStatMaxDumpLength = _StatusFatalStatMaxDumpLength_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 4),
    _StatusFatalStatMaxDumpLength_Type()
)
statusFatalStatMaxDumpLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalStatMaxDumpLength.setStatus("mandatory")
_StatusFatalTable_Object = MibTable
statusFatalTable = _StatusFatalTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5)
)
if mibBuilder.loadTexts:
    statusFatalTable.setStatus("mandatory")
_StatusFatalEntry_Object = MibTableRow
statusFatalEntry = _StatusFatalEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5, 1)
)
statusFatalEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "statusFatalIndex"),
)
if mibBuilder.loadTexts:
    statusFatalEntry.setStatus("mandatory")
_StatusFatalIndex_Type = Integer32
_StatusFatalIndex_Object = MibTableColumn
statusFatalIndex = _StatusFatalIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5, 1, 1),
    _StatusFatalIndex_Type()
)
statusFatalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalIndex.setStatus("mandatory")
_StatusFatalSerial_Type = Integer32
_StatusFatalSerial_Object = MibTableColumn
statusFatalSerial = _StatusFatalSerial_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5, 1, 2),
    _StatusFatalSerial_Type()
)
statusFatalSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalSerial.setStatus("mandatory")
_StatusFatalTimestamp_Type = Integer32
_StatusFatalTimestamp_Object = MibTableColumn
statusFatalTimestamp = _StatusFatalTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5, 1, 3),
    _StatusFatalTimestamp_Type()
)
statusFatalTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalTimestamp.setStatus("mandatory")
_StatusFatalTimeString_Type = DisplayString
_StatusFatalTimeString_Object = MibTableColumn
statusFatalTimeString = _StatusFatalTimeString_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5, 1, 4),
    _StatusFatalTimeString_Type()
)
statusFatalTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalTimeString.setStatus("mandatory")
_StatusFatalSource_Type = DisplayString
_StatusFatalSource_Object = MibTableColumn
statusFatalSource = _StatusFatalSource_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5, 1, 5),
    _StatusFatalSource_Type()
)
statusFatalSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalSource.setStatus("mandatory")
_StatusFatalLine_Type = Integer32
_StatusFatalLine_Object = MibTableColumn
statusFatalLine = _StatusFatalLine_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5, 1, 6),
    _StatusFatalLine_Type()
)
statusFatalLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalLine.setStatus("mandatory")
_StatusFatalOriginalDumpSize_Type = Integer32
_StatusFatalOriginalDumpSize_Object = MibTableColumn
statusFatalOriginalDumpSize = _StatusFatalOriginalDumpSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5, 1, 7),
    _StatusFatalOriginalDumpSize_Type()
)
statusFatalOriginalDumpSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalOriginalDumpSize.setStatus("mandatory")
_StatusFatalDumpSize_Type = Integer32
_StatusFatalDumpSize_Object = MibTableColumn
statusFatalDumpSize = _StatusFatalDumpSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5, 1, 8),
    _StatusFatalDumpSize_Type()
)
statusFatalDumpSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalDumpSize.setStatus("mandatory")
_StatusFatalDump_Type = OctetString
_StatusFatalDump_Object = MibTableColumn
statusFatalDump = _StatusFatalDump_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 3, 8, 5, 1, 9),
    _StatusFatalDump_Type()
)
statusFatalDump.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFatalDump.setStatus("mandatory")
_CrossfireAtmStatistics_ObjectIdentity = ObjectIdentity
crossfireAtmStatistics = _CrossfireAtmStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4)
)
_StatisticsGlobal_ObjectIdentity = ObjectIdentity
statisticsGlobal = _StatisticsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1)
)


class _StatsGlobalCongestionState_Type(Integer32):
    """Custom type statsGlobalCongestionState based on Integer32"""
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
        *(("high", 4),
          ("highDecreasing", 2),
          ("normal", 1),
          ("normalIncreasing", 3))
    )


_StatsGlobalCongestionState_Type.__name__ = "Integer32"
_StatsGlobalCongestionState_Object = MibScalar
statsGlobalCongestionState = _StatsGlobalCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1, 1),
    _StatsGlobalCongestionState_Type()
)
statsGlobalCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsGlobalCongestionState.setStatus("mandatory")
_StatsGlobalCongestionDiscardCellRate_Type = Gauge32
_StatsGlobalCongestionDiscardCellRate_Object = MibScalar
statsGlobalCongestionDiscardCellRate = _StatsGlobalCongestionDiscardCellRate_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1, 2),
    _StatsGlobalCongestionDiscardCellRate_Type()
)
statsGlobalCongestionDiscardCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsGlobalCongestionDiscardCellRate.setStatus("mandatory")
_StatsGlobalCongestionDiscardCellCounter_Type = Counter32
_StatsGlobalCongestionDiscardCellCounter_Object = MibScalar
statsGlobalCongestionDiscardCellCounter = _StatsGlobalCongestionDiscardCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1, 3),
    _StatsGlobalCongestionDiscardCellCounter_Type()
)
statsGlobalCongestionDiscardCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsGlobalCongestionDiscardCellCounter.setStatus("mandatory")


class _StatsGlobalCongestionDiscardCellLatch_Type(Integer32):
    """Custom type statsGlobalCongestionDiscardCellLatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StatsGlobalCongestionDiscardCellLatch_Type.__name__ = "Integer32"
_StatsGlobalCongestionDiscardCellLatch_Object = MibScalar
statsGlobalCongestionDiscardCellLatch = _StatsGlobalCongestionDiscardCellLatch_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1, 4),
    _StatsGlobalCongestionDiscardCellLatch_Type()
)
statsGlobalCongestionDiscardCellLatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsGlobalCongestionDiscardCellLatch.setStatus("mandatory")
_StatsGlobalCongestionDiscardCellLatchTime_Type = TimeTicks
_StatsGlobalCongestionDiscardCellLatchTime_Object = MibScalar
statsGlobalCongestionDiscardCellLatchTime = _StatsGlobalCongestionDiscardCellLatchTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1, 5),
    _StatsGlobalCongestionDiscardCellLatchTime_Type()
)
statsGlobalCongestionDiscardCellLatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsGlobalCongestionDiscardCellLatchTime.setStatus("mandatory")


class _StatsInvalidCellRateState_Type(Integer32):
    """Custom type statsInvalidCellRateState based on Integer32"""
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
        *(("high", 4),
          ("highDecreasing", 2),
          ("normal", 1),
          ("normalIncreasing", 3))
    )


_StatsInvalidCellRateState_Type.__name__ = "Integer32"
_StatsInvalidCellRateState_Object = MibScalar
statsInvalidCellRateState = _StatsInvalidCellRateState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1, 6),
    _StatsInvalidCellRateState_Type()
)
statsInvalidCellRateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInvalidCellRateState.setStatus("mandatory")
_StatsInvalidCellRate_Type = Gauge32
_StatsInvalidCellRate_Object = MibScalar
statsInvalidCellRate = _StatsInvalidCellRate_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1, 7),
    _StatsInvalidCellRate_Type()
)
statsInvalidCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInvalidCellRate.setStatus("mandatory")
_StatsInvalidCellCounter_Type = Counter32
_StatsInvalidCellCounter_Object = MibScalar
statsInvalidCellCounter = _StatsInvalidCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1, 8),
    _StatsInvalidCellCounter_Type()
)
statsInvalidCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInvalidCellCounter.setStatus("mandatory")


class _StatsInvalidCellLatch_Type(Integer32):
    """Custom type statsInvalidCellLatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StatsInvalidCellLatch_Type.__name__ = "Integer32"
_StatsInvalidCellLatch_Object = MibScalar
statsInvalidCellLatch = _StatsInvalidCellLatch_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1, 9),
    _StatsInvalidCellLatch_Type()
)
statsInvalidCellLatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsInvalidCellLatch.setStatus("mandatory")
_StatsInvalidCellLatchTime_Type = TimeTicks
_StatsInvalidCellLatchTime_Object = MibScalar
statsInvalidCellLatchTime = _StatsInvalidCellLatchTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 1, 10),
    _StatsInvalidCellLatchTime_Type()
)
statsInvalidCellLatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInvalidCellLatchTime.setStatus("mandatory")
_StatisticsCpuPort_ObjectIdentity = ObjectIdentity
statisticsCpuPort = _StatisticsCpuPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 2)
)


class _StatsCpuPortCongestionState_Type(Integer32):
    """Custom type statsCpuPortCongestionState based on Integer32"""
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
        *(("high", 4),
          ("highDecreasing", 2),
          ("normal", 1),
          ("normalIncreasing", 3))
    )


_StatsCpuPortCongestionState_Type.__name__ = "Integer32"
_StatsCpuPortCongestionState_Object = MibScalar
statsCpuPortCongestionState = _StatsCpuPortCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 2, 1),
    _StatsCpuPortCongestionState_Type()
)
statsCpuPortCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsCpuPortCongestionState.setStatus("mandatory")
_StatsCpuPortDiscardCellRate_Type = Gauge32
_StatsCpuPortDiscardCellRate_Object = MibScalar
statsCpuPortDiscardCellRate = _StatsCpuPortDiscardCellRate_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 2, 2),
    _StatsCpuPortDiscardCellRate_Type()
)
statsCpuPortDiscardCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsCpuPortDiscardCellRate.setStatus("mandatory")
_StatsCpuPortDiscardCellCounter_Type = Counter32
_StatsCpuPortDiscardCellCounter_Object = MibScalar
statsCpuPortDiscardCellCounter = _StatsCpuPortDiscardCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 2, 3),
    _StatsCpuPortDiscardCellCounter_Type()
)
statsCpuPortDiscardCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsCpuPortDiscardCellCounter.setStatus("mandatory")


class _StatsCpuPortDiscardCellLatch_Type(Integer32):
    """Custom type statsCpuPortDiscardCellLatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StatsCpuPortDiscardCellLatch_Type.__name__ = "Integer32"
_StatsCpuPortDiscardCellLatch_Object = MibScalar
statsCpuPortDiscardCellLatch = _StatsCpuPortDiscardCellLatch_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 2, 4),
    _StatsCpuPortDiscardCellLatch_Type()
)
statsCpuPortDiscardCellLatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsCpuPortDiscardCellLatch.setStatus("mandatory")
_StatsCpuPortDiscardCellLatchTime_Type = TimeTicks
_StatsCpuPortDiscardCellLatchTime_Object = MibScalar
statsCpuPortDiscardCellLatchTime = _StatsCpuPortDiscardCellLatchTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 2, 5),
    _StatsCpuPortDiscardCellLatchTime_Type()
)
statsCpuPortDiscardCellLatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsCpuPortDiscardCellLatchTime.setStatus("mandatory")
_StatisticsEPort_ObjectIdentity = ObjectIdentity
statisticsEPort = _StatisticsEPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 3)
)
_StatsEportTable_Object = MibTable
statsEportTable = _StatsEportTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    statsEportTable.setStatus("mandatory")
_StatsEportEntry_Object = MibTableRow
statsEportEntry = _StatsEportEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 3, 1, 1)
)
statsEportEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "statsEPortIfIndex"),
)
if mibBuilder.loadTexts:
    statsEportEntry.setStatus("mandatory")
_StatsEPortIfIndex_Type = Integer32
_StatsEPortIfIndex_Object = MibTableColumn
statsEPortIfIndex = _StatsEPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 3, 1, 1, 1),
    _StatsEPortIfIndex_Type()
)
statsEPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsEPortIfIndex.setStatus("mandatory")


class _StatsEPortHecErrorRateConditionState_Type(Integer32):
    """Custom type statsEPortHecErrorRateConditionState based on Integer32"""
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
        *(("high", 4),
          ("highDecreasing", 2),
          ("normal", 1),
          ("normalIncreasing", 3))
    )


_StatsEPortHecErrorRateConditionState_Type.__name__ = "Integer32"
_StatsEPortHecErrorRateConditionState_Object = MibTableColumn
statsEPortHecErrorRateConditionState = _StatsEPortHecErrorRateConditionState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 3, 1, 1, 2),
    _StatsEPortHecErrorRateConditionState_Type()
)
statsEPortHecErrorRateConditionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsEPortHecErrorRateConditionState.setStatus("mandatory")
_StatsEPortRxHecErrorCellRate_Type = Gauge32
_StatsEPortRxHecErrorCellRate_Object = MibTableColumn
statsEPortRxHecErrorCellRate = _StatsEPortRxHecErrorCellRate_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 3, 1, 1, 3),
    _StatsEPortRxHecErrorCellRate_Type()
)
statsEPortRxHecErrorCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsEPortRxHecErrorCellRate.setStatus("mandatory")
_StatsEPortRxHecErrorCellCounter_Type = Counter32
_StatsEPortRxHecErrorCellCounter_Object = MibTableColumn
statsEPortRxHecErrorCellCounter = _StatsEPortRxHecErrorCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 3, 1, 1, 4),
    _StatsEPortRxHecErrorCellCounter_Type()
)
statsEPortRxHecErrorCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsEPortRxHecErrorCellCounter.setStatus("mandatory")


class _StatsEPortRxHecErrorCellLatch_Type(Integer32):
    """Custom type statsEPortRxHecErrorCellLatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StatsEPortRxHecErrorCellLatch_Type.__name__ = "Integer32"
_StatsEPortRxHecErrorCellLatch_Object = MibTableColumn
statsEPortRxHecErrorCellLatch = _StatsEPortRxHecErrorCellLatch_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 3, 1, 1, 5),
    _StatsEPortRxHecErrorCellLatch_Type()
)
statsEPortRxHecErrorCellLatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsEPortRxHecErrorCellLatch.setStatus("mandatory")
_StatsEPortRxHecErrorCellLatchTime_Type = TimeTicks
_StatsEPortRxHecErrorCellLatchTime_Object = MibTableColumn
statsEPortRxHecErrorCellLatchTime = _StatsEPortRxHecErrorCellLatchTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 3, 1, 1, 6),
    _StatsEPortRxHecErrorCellLatchTime_Type()
)
statsEPortRxHecErrorCellLatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsEPortRxHecErrorCellLatchTime.setStatus("mandatory")
_StatisticsIPort_ObjectIdentity = ObjectIdentity
statisticsIPort = _StatisticsIPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4)
)
_StatsIPortTable_Object = MibTable
statsIPortTable = _StatsIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 1)
)
if mibBuilder.loadTexts:
    statsIPortTable.setStatus("mandatory")
_StatsIPortEntry_Object = MibTableRow
statsIPortEntry = _StatsIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 1, 1)
)
statsIPortEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "statsIPortSlotIndex"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "statsIPortRIndex"),
)
if mibBuilder.loadTexts:
    statsIPortEntry.setStatus("mandatory")


class _StatsIPortSlotIndex_Type(Integer32):
    """Custom type statsIPortSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_StatsIPortSlotIndex_Type.__name__ = "Integer32"
_StatsIPortSlotIndex_Object = MibTableColumn
statsIPortSlotIndex = _StatsIPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 1, 1, 1),
    _StatsIPortSlotIndex_Type()
)
statsIPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsIPortSlotIndex.setStatus("mandatory")


class _StatsIPortRIndex_Type(Integer32):
    """Custom type statsIPortRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_StatsIPortRIndex_Type.__name__ = "Integer32"
_StatsIPortRIndex_Object = MibTableColumn
statsIPortRIndex = _StatsIPortRIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 1, 1, 2),
    _StatsIPortRIndex_Type()
)
statsIPortRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsIPortRIndex.setStatus("mandatory")
_StatsIPortRxCellRate_Type = Gauge32
_StatsIPortRxCellRate_Object = MibTableColumn
statsIPortRxCellRate = _StatsIPortRxCellRate_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 1, 1, 3),
    _StatsIPortRxCellRate_Type()
)
statsIPortRxCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsIPortRxCellRate.setStatus("mandatory")
_StatsIPortTxCellRate_Type = Gauge32
_StatsIPortTxCellRate_Object = MibTableColumn
statsIPortTxCellRate = _StatsIPortTxCellRate_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 1, 1, 4),
    _StatsIPortTxCellRate_Type()
)
statsIPortTxCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsIPortTxCellRate.setStatus("mandatory")
_StatsIPortTxParityErrorCellCounter_Type = Counter32
_StatsIPortTxParityErrorCellCounter_Object = MibTableColumn
statsIPortTxParityErrorCellCounter = _StatsIPortTxParityErrorCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 1, 1, 5),
    _StatsIPortTxParityErrorCellCounter_Type()
)
statsIPortTxParityErrorCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsIPortTxParityErrorCellCounter.setStatus("mandatory")
_StatsQueueCongestionTable_Object = MibTable
statsQueueCongestionTable = _StatsQueueCongestionTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 2)
)
if mibBuilder.loadTexts:
    statsQueueCongestionTable.setStatus("mandatory")
_StatsQueueCongestionEntry_Object = MibTableRow
statsQueueCongestionEntry = _StatsQueueCongestionEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 2, 1)
)
statsQueueCongestionEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "statsQueueCongestionSlotIndex"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "statsQueueCongestionIPortRIndex"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "statsQueueCongestionQueueIndex"),
)
if mibBuilder.loadTexts:
    statsQueueCongestionEntry.setStatus("mandatory")


class _StatsQueueCongestionSlotIndex_Type(Integer32):
    """Custom type statsQueueCongestionSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_StatsQueueCongestionSlotIndex_Type.__name__ = "Integer32"
_StatsQueueCongestionSlotIndex_Object = MibTableColumn
statsQueueCongestionSlotIndex = _StatsQueueCongestionSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 2, 1, 1),
    _StatsQueueCongestionSlotIndex_Type()
)
statsQueueCongestionSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsQueueCongestionSlotIndex.setStatus("mandatory")


class _StatsQueueCongestionIPortRIndex_Type(Integer32):
    """Custom type statsQueueCongestionIPortRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_StatsQueueCongestionIPortRIndex_Type.__name__ = "Integer32"
_StatsQueueCongestionIPortRIndex_Object = MibTableColumn
statsQueueCongestionIPortRIndex = _StatsQueueCongestionIPortRIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 2, 1, 2),
    _StatsQueueCongestionIPortRIndex_Type()
)
statsQueueCongestionIPortRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsQueueCongestionIPortRIndex.setStatus("mandatory")


class _StatsQueueCongestionQueueIndex_Type(Integer32):
    """Custom type statsQueueCongestionQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_StatsQueueCongestionQueueIndex_Type.__name__ = "Integer32"
_StatsQueueCongestionQueueIndex_Object = MibTableColumn
statsQueueCongestionQueueIndex = _StatsQueueCongestionQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 2, 1, 3),
    _StatsQueueCongestionQueueIndex_Type()
)
statsQueueCongestionQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsQueueCongestionQueueIndex.setStatus("mandatory")


class _StatsQueueCongestionConditionState_Type(Integer32):
    """Custom type statsQueueCongestionConditionState based on Integer32"""
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
        *(("high", 4),
          ("highDecreasing", 2),
          ("normal", 1),
          ("normalIncreasing", 3))
    )


_StatsQueueCongestionConditionState_Type.__name__ = "Integer32"
_StatsQueueCongestionConditionState_Object = MibTableColumn
statsQueueCongestionConditionState = _StatsQueueCongestionConditionState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 2, 1, 4),
    _StatsQueueCongestionConditionState_Type()
)
statsQueueCongestionConditionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsQueueCongestionConditionState.setStatus("mandatory")
_StatsQueueCongestionCellsInQueueGauge_Type = Gauge32
_StatsQueueCongestionCellsInQueueGauge_Object = MibTableColumn
statsQueueCongestionCellsInQueueGauge = _StatsQueueCongestionCellsInQueueGauge_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 2, 1, 5),
    _StatsQueueCongestionCellsInQueueGauge_Type()
)
statsQueueCongestionCellsInQueueGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsQueueCongestionCellsInQueueGauge.setStatus("mandatory")
_StatsQueueCongestionCellsInQueueLatch_Type = Integer32
_StatsQueueCongestionCellsInQueueLatch_Object = MibTableColumn
statsQueueCongestionCellsInQueueLatch = _StatsQueueCongestionCellsInQueueLatch_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 2, 1, 6),
    _StatsQueueCongestionCellsInQueueLatch_Type()
)
statsQueueCongestionCellsInQueueLatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsQueueCongestionCellsInQueueLatch.setStatus("mandatory")
_StatsQueueCongestionCellsInQueueLatchTime_Type = TimeTicks
_StatsQueueCongestionCellsInQueueLatchTime_Object = MibTableColumn
statsQueueCongestionCellsInQueueLatchTime = _StatsQueueCongestionCellsInQueueLatchTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 4, 4, 2, 1, 7),
    _StatsQueueCongestionCellsInQueueLatchTime_Type()
)
statsQueueCongestionCellsInQueueLatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsQueueCongestionCellsInQueueLatchTime.setStatus("mandatory")
_CrossfireAtmTrapControl_ObjectIdentity = ObjectIdentity
crossfireAtmTrapControl = _CrossfireAtmTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5)
)


class _FhTrapFrequencyCntrlFrequency_Type(Integer32):
    """Custom type fhTrapFrequencyCntrlFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_FhTrapFrequencyCntrlFrequency_Type.__name__ = "Integer32"
_FhTrapFrequencyCntrlFrequency_Object = MibScalar
fhTrapFrequencyCntrlFrequency = _FhTrapFrequencyCntrlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 1),
    _FhTrapFrequencyCntrlFrequency_Type()
)
fhTrapFrequencyCntrlFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fhTrapFrequencyCntrlFrequency.setStatus("mandatory")


class _FhTrapFrequencyCntrlMaxTraps_Type(Integer32):
    """Custom type fhTrapFrequencyCntrlMaxTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FhTrapFrequencyCntrlMaxTraps_Type.__name__ = "Integer32"
_FhTrapFrequencyCntrlMaxTraps_Object = MibScalar
fhTrapFrequencyCntrlMaxTraps = _FhTrapFrequencyCntrlMaxTraps_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 2),
    _FhTrapFrequencyCntrlMaxTraps_Type()
)
fhTrapFrequencyCntrlMaxTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fhTrapFrequencyCntrlMaxTraps.setStatus("mandatory")
_FhTrapDashboardControlTable_Object = MibTable
fhTrapDashboardControlTable = _FhTrapDashboardControlTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 3)
)
if mibBuilder.loadTexts:
    fhTrapDashboardControlTable.setStatus("mandatory")
_FhTrapDashboardControlEntry_Object = MibTableRow
fhTrapDashboardControlEntry = _FhTrapDashboardControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 3, 1)
)
fhTrapDashboardControlEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "fhTrapDashboardControlTrapTypeIndex"),
)
if mibBuilder.loadTexts:
    fhTrapDashboardControlEntry.setStatus("mandatory")


class _FhTrapDashboardControlTrapTypeIndex_Type(Integer32):
    """Custom type fhTrapDashboardControlTrapTypeIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cpuPortCongestion", 3),
          ("ePortHecErrorRate", 5),
          ("fanMonitor", 8),
          ("globalCongestion", 1),
          ("globalInvalidCellRate", 2),
          ("iPortCongestion", 4),
          ("psuMonitor", 7),
          ("temperatureWarning", 6))
    )


_FhTrapDashboardControlTrapTypeIndex_Type.__name__ = "Integer32"
_FhTrapDashboardControlTrapTypeIndex_Object = MibTableColumn
fhTrapDashboardControlTrapTypeIndex = _FhTrapDashboardControlTrapTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 3, 1, 1),
    _FhTrapDashboardControlTrapTypeIndex_Type()
)
fhTrapDashboardControlTrapTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fhTrapDashboardControlTrapTypeIndex.setStatus("mandatory")


class _FhTrapDashboardControlFrequencyMode_Type(Integer32):
    """Custom type fhTrapDashboardControlFrequencyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forever", 2),
          ("oneShot", 1),
          ("upToMax", 3))
    )


_FhTrapDashboardControlFrequencyMode_Type.__name__ = "Integer32"
_FhTrapDashboardControlFrequencyMode_Object = MibTableColumn
fhTrapDashboardControlFrequencyMode = _FhTrapDashboardControlFrequencyMode_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 3, 1, 2),
    _FhTrapDashboardControlFrequencyMode_Type()
)
fhTrapDashboardControlFrequencyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fhTrapDashboardControlFrequencyMode.setStatus("mandatory")
_FhTrapDashboardControlThresholdLow_Type = Integer32
_FhTrapDashboardControlThresholdLow_Object = MibTableColumn
fhTrapDashboardControlThresholdLow = _FhTrapDashboardControlThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 3, 1, 3),
    _FhTrapDashboardControlThresholdLow_Type()
)
fhTrapDashboardControlThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fhTrapDashboardControlThresholdLow.setStatus("mandatory")
_FhTrapDashboardControlThresholdHigh_Type = Integer32
_FhTrapDashboardControlThresholdHigh_Object = MibTableColumn
fhTrapDashboardControlThresholdHigh = _FhTrapDashboardControlThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 3, 1, 4),
    _FhTrapDashboardControlThresholdHigh_Type()
)
fhTrapDashboardControlThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fhTrapDashboardControlThresholdHigh.setStatus("mandatory")


class _FhTrapDashboardControlSamplingInterval_Type(Integer32):
    """Custom type fhTrapDashboardControlSamplingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FhTrapDashboardControlSamplingInterval_Type.__name__ = "Integer32"
_FhTrapDashboardControlSamplingInterval_Object = MibTableColumn
fhTrapDashboardControlSamplingInterval = _FhTrapDashboardControlSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 3, 1, 5),
    _FhTrapDashboardControlSamplingInterval_Type()
)
fhTrapDashboardControlSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fhTrapDashboardControlSamplingInterval.setStatus("mandatory")


class _FhTrapDashboardControlNoSamples_Type(Integer32):
    """Custom type fhTrapDashboardControlNoSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FhTrapDashboardControlNoSamples_Type.__name__ = "Integer32"
_FhTrapDashboardControlNoSamples_Object = MibTableColumn
fhTrapDashboardControlNoSamples = _FhTrapDashboardControlNoSamples_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 3, 1, 6),
    _FhTrapDashboardControlNoSamples_Type()
)
fhTrapDashboardControlNoSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fhTrapDashboardControlNoSamples.setStatus("mandatory")
_TemperatureCriticalTrapThreshold_Type = Integer32
_TemperatureCriticalTrapThreshold_Object = MibScalar
temperatureCriticalTrapThreshold = _TemperatureCriticalTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 5, 4),
    _TemperatureCriticalTrapThreshold_Type()
)
temperatureCriticalTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureCriticalTrapThreshold.setStatus("mandatory")
_CrossfireAtmTest_ObjectIdentity = ObjectIdentity
crossfireAtmTest = _CrossfireAtmTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 6)
)
_Crossfirexlx_ObjectIdentity = ObjectIdentity
crossfirexlx = _Crossfirexlx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7)
)
_OcCNNI_ObjectIdentity = ObjectIdentity
ocCNNI = _OcCNNI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3)
)
_OcCNNIMonSimple_Object = MibTable
ocCNNIMonSimple = _OcCNNIMonSimple_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 1)
)
if mibBuilder.loadTexts:
    ocCNNIMonSimple.setStatus("optional")
_OcCNNIMonSEntry_Object = MibTableRow
ocCNNIMonSEntry = _OcCNNIMonSEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 1, 1)
)
ocCNNIMonSEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIApplID"),
)
if mibBuilder.loadTexts:
    ocCNNIMonSEntry.setStatus("optional")


class _OcCNNIRoutingTableChanged_Type(Integer32):
    """Custom type ocCNNIRoutingTableChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OcCNNIRoutingTableChanged_Type.__name__ = "Integer32"
_OcCNNIRoutingTableChanged_Object = MibTableColumn
ocCNNIRoutingTableChanged = _OcCNNIRoutingTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 1, 1, 1),
    _OcCNNIRoutingTableChanged_Type()
)
ocCNNIRoutingTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIRoutingTableChanged.setStatus("optional")


class _OcCNNINeighborTableChanged_Type(Integer32):
    """Custom type ocCNNINeighborTableChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OcCNNINeighborTableChanged_Type.__name__ = "Integer32"
_OcCNNINeighborTableChanged_Object = MibTableColumn
ocCNNINeighborTableChanged = _OcCNNINeighborTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 1, 1, 2),
    _OcCNNINeighborTableChanged_Type()
)
ocCNNINeighborTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNINeighborTableChanged.setStatus("optional")
_OcCNNILineStatus_Type = OctetString
_OcCNNILineStatus_Object = MibTableColumn
ocCNNILineStatus = _OcCNNILineStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 1, 1, 3),
    _OcCNNILineStatus_Type()
)
ocCNNILineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNILineStatus.setStatus("optional")
_OcCNNIMACAddress_Type = OctetString
_OcCNNIMACAddress_Object = MibTableColumn
ocCNNIMACAddress = _OcCNNIMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 1, 1, 4),
    _OcCNNIMACAddress_Type()
)
ocCNNIMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIMACAddress.setStatus("optional")


class _OcCNNIMode_Type(Integer32):
    """Custom type ocCNNIMode based on Integer32"""
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


_OcCNNIMode_Type.__name__ = "Integer32"
_OcCNNIMode_Object = MibTableColumn
ocCNNIMode = _OcCNNIMode_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 1, 1, 5),
    _OcCNNIMode_Type()
)
ocCNNIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIMode.setStatus("optional")
_OcCNNIProtocolVersion_Type = Integer32
_OcCNNIProtocolVersion_Object = MibTableColumn
ocCNNIProtocolVersion = _OcCNNIProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 1, 1, 6),
    _OcCNNIProtocolVersion_Type()
)
ocCNNIProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIProtocolVersion.setStatus("optional")
_OcCNNIApplID_Type = Integer32
_OcCNNIApplID_Object = MibTableColumn
ocCNNIApplID = _OcCNNIApplID_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 1, 1, 7),
    _OcCNNIApplID_Type()
)
ocCNNIApplID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIApplID.setStatus("optional")
_OcCNNIMonTables_ObjectIdentity = ObjectIdentity
ocCNNIMonTables = _OcCNNIMonTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2)
)
_OcCNNIRoutingTable_Object = MibTable
ocCNNIRoutingTable = _OcCNNIRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ocCNNIRoutingTable.setStatus("optional")
_OcCNNIRoutingTableEntry_Object = MibTableRow
ocCNNIRoutingTableEntry = _OcCNNIRoutingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 1, 1)
)
ocCNNIRoutingTableEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIApplID"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIAddress"),
)
if mibBuilder.loadTexts:
    ocCNNIRoutingTableEntry.setStatus("optional")
_OcCNNIAddress_Type = OctetString
_OcCNNIAddress_Object = MibTableColumn
ocCNNIAddress = _OcCNNIAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 1, 1, 1),
    _OcCNNIAddress_Type()
)
ocCNNIAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddress.setStatus("optional")
_OcCNNIRoutingTableData_Type = OctetString
_OcCNNIRoutingTableData_Object = MibTableColumn
ocCNNIRoutingTableData = _OcCNNIRoutingTableData_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 1, 1, 2),
    _OcCNNIRoutingTableData_Type()
)
ocCNNIRoutingTableData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIRoutingTableData.setStatus("optional")
_OcCNNIAddressAlias_Type = OctetString
_OcCNNIAddressAlias_Object = MibTableColumn
ocCNNIAddressAlias = _OcCNNIAddressAlias_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 1, 1, 3),
    _OcCNNIAddressAlias_Type()
)
ocCNNIAddressAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddressAlias.setStatus("optional")
_OcCNNINeighborTable_Object = MibTable
ocCNNINeighborTable = _OcCNNINeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ocCNNINeighborTable.setStatus("optional")
_OcCNNINeighborTableEntry_Object = MibTableRow
ocCNNINeighborTableEntry = _OcCNNINeighborTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 2, 1)
)
ocCNNINeighborTableEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIApplID"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIPort"),
)
if mibBuilder.loadTexts:
    ocCNNINeighborTableEntry.setStatus("optional")
_OcCNNIPort_Type = Integer32
_OcCNNIPort_Object = MibTableColumn
ocCNNIPort = _OcCNNIPort_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 2, 1, 1),
    _OcCNNIPort_Type()
)
ocCNNIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIPort.setStatus("optional")
_OcCNNINeighborTableData_Type = OctetString
_OcCNNINeighborTableData_Object = MibTableColumn
ocCNNINeighborTableData = _OcCNNINeighborTableData_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 2, 1, 2),
    _OcCNNINeighborTableData_Type()
)
ocCNNINeighborTableData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNINeighborTableData.setStatus("optional")
_OcCNNITrapClientTable_Object = MibTable
ocCNNITrapClientTable = _OcCNNITrapClientTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ocCNNITrapClientTable.setStatus("optional")
_OcCNNITrapClientTableEntry_Object = MibTableRow
ocCNNITrapClientTableEntry = _OcCNNITrapClientTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 3, 1)
)
ocCNNITrapClientTableEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIApplID"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNITrapClientAddress"),
)
if mibBuilder.loadTexts:
    ocCNNITrapClientTableEntry.setStatus("optional")
_OcCNNITrapClientIndex_Type = OctetString
_OcCNNITrapClientIndex_Object = MibTableColumn
ocCNNITrapClientIndex = _OcCNNITrapClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 3, 1, 1),
    _OcCNNITrapClientIndex_Type()
)
ocCNNITrapClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNITrapClientIndex.setStatus("optional")
_OcCNNITrapClientAddress_Type = IpAddress
_OcCNNITrapClientAddress_Object = MibTableColumn
ocCNNITrapClientAddress = _OcCNNITrapClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 3, 1, 2),
    _OcCNNITrapClientAddress_Type()
)
ocCNNITrapClientAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNITrapClientAddress.setStatus("optional")
_OcCNNITrapClientCommName_Type = OctetString
_OcCNNITrapClientCommName_Object = MibTableColumn
ocCNNITrapClientCommName = _OcCNNITrapClientCommName_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 2, 3, 1, 3),
    _OcCNNITrapClientCommName_Type()
)
ocCNNITrapClientCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNITrapClientCommName.setStatus("optional")
_OcCNNIConfig_ObjectIdentity = ObjectIdentity
ocCNNIConfig = _OcCNNIConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 3)
)


class _OcCNNIConfigMethod_Type(Integer32):
    """Custom type ocCNNIConfigMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("best", 1),
          ("first", 0))
    )


_OcCNNIConfigMethod_Type.__name__ = "Integer32"
_OcCNNIConfigMethod_Object = MibScalar
ocCNNIConfigMethod = _OcCNNIConfigMethod_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 3, 1),
    _OcCNNIConfigMethod_Type()
)
ocCNNIConfigMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIConfigMethod.setStatus("optional")
_OcCNNIConfigAlgorithm_Type = Integer32
_OcCNNIConfigAlgorithm_Object = MibScalar
ocCNNIConfigAlgorithm = _OcCNNIConfigAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 3, 2),
    _OcCNNIConfigAlgorithm_Type()
)
ocCNNIConfigAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIConfigAlgorithm.setStatus("optional")
_OcCNNIPortConfig_Object = MibTable
ocCNNIPortConfig = _OcCNNIPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 4)
)
if mibBuilder.loadTexts:
    ocCNNIPortConfig.setStatus("optional")
_OcCNNIPortEntry_Object = MibTableRow
ocCNNIPortEntry = _OcCNNIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 4, 1)
)
ocCNNIPortEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIPort"),
)
if mibBuilder.loadTexts:
    ocCNNIPortEntry.setStatus("optional")


class _OcCNNIPortProtocol_Type(Integer32):
    """Custom type ocCNNIPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnni", 0),
          ("none", 2),
          ("pnni", 1))
    )


_OcCNNIPortProtocol_Type.__name__ = "Integer32"
_OcCNNIPortProtocol_Object = MibTableColumn
ocCNNIPortProtocol = _OcCNNIPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 4, 1, 1),
    _OcCNNIPortProtocol_Type()
)
ocCNNIPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIPortProtocol.setStatus("optional")


class _OcCNNIPortBorder_Type(Integer32):
    """Custom type ocCNNIPortBorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OcCNNIPortBorder_Type.__name__ = "Integer32"
_OcCNNIPortBorder_Object = MibTableColumn
ocCNNIPortBorder = _OcCNNIPortBorder_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 4, 1, 2),
    _OcCNNIPortBorder_Type()
)
ocCNNIPortBorder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIPortBorder.setStatus("optional")


class _OcCNNIPortAutoreroute_Type(Integer32):
    """Custom type ocCNNIPortAutoreroute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OcCNNIPortAutoreroute_Type.__name__ = "Integer32"
_OcCNNIPortAutoreroute_Object = MibTableColumn
ocCNNIPortAutoreroute = _OcCNNIPortAutoreroute_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 4, 1, 3),
    _OcCNNIPortAutoreroute_Type()
)
ocCNNIPortAutoreroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIPortAutoreroute.setStatus("optional")


class _OcCNNIPortReroute_Type(Integer32):
    """Custom type ocCNNIPortReroute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OcCNNIPortReroute_Type.__name__ = "Integer32"
_OcCNNIPortReroute_Object = MibTableColumn
ocCNNIPortReroute = _OcCNNIPortReroute_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 4, 1, 4),
    _OcCNNIPortReroute_Type()
)
ocCNNIPortReroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIPortReroute.setStatus("optional")


class _OcCNNIPortAssign_Type(Integer32):
    """Custom type ocCNNIPortAssign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OcCNNIPortAssign_Type.__name__ = "Integer32"
_OcCNNIPortAssign_Object = MibTableColumn
ocCNNIPortAssign = _OcCNNIPortAssign_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 4, 1, 5),
    _OcCNNIPortAssign_Type()
)
ocCNNIPortAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIPortAssign.setStatus("optional")
_OcCNNIGlobalStats_ObjectIdentity = ObjectIdentity
ocCNNIGlobalStats = _OcCNNIGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 5)
)
_OcCNNIGlobalStatsTotal_Type = Counter32
_OcCNNIGlobalStatsTotal_Object = MibScalar
ocCNNIGlobalStatsTotal = _OcCNNIGlobalStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 5, 1),
    _OcCNNIGlobalStatsTotal_Type()
)
ocCNNIGlobalStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIGlobalStatsTotal.setStatus("optional")
_OcCNNIGlobalStatsCreated_Type = Counter32
_OcCNNIGlobalStatsCreated_Object = MibScalar
ocCNNIGlobalStatsCreated = _OcCNNIGlobalStatsCreated_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 5, 2),
    _OcCNNIGlobalStatsCreated_Type()
)
ocCNNIGlobalStatsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIGlobalStatsCreated.setStatus("optional")
_OcCNNIGlobalStatsOneWay_Type = Counter32
_OcCNNIGlobalStatsOneWay_Object = MibScalar
ocCNNIGlobalStatsOneWay = _OcCNNIGlobalStatsOneWay_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 5, 3),
    _OcCNNIGlobalStatsOneWay_Type()
)
ocCNNIGlobalStatsOneWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIGlobalStatsOneWay.setStatus("optional")
_OcCNNIGlobalStatsConnected_Type = Counter32
_OcCNNIGlobalStatsConnected_Object = MibScalar
ocCNNIGlobalStatsConnected = _OcCNNIGlobalStatsConnected_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 5, 4),
    _OcCNNIGlobalStatsConnected_Type()
)
ocCNNIGlobalStatsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIGlobalStatsConnected.setStatus("optional")
_OcCNNIGlobalStatsBrokenLeaf_Type = Counter32
_OcCNNIGlobalStatsBrokenLeaf_Object = MibScalar
ocCNNIGlobalStatsBrokenLeaf = _OcCNNIGlobalStatsBrokenLeaf_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 5, 5),
    _OcCNNIGlobalStatsBrokenLeaf_Type()
)
ocCNNIGlobalStatsBrokenLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIGlobalStatsBrokenLeaf.setStatus("optional")
_OcCNNIGlobalStatsBrokenRoot_Type = Counter32
_OcCNNIGlobalStatsBrokenRoot_Object = MibScalar
ocCNNIGlobalStatsBrokenRoot = _OcCNNIGlobalStatsBrokenRoot_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 5, 6),
    _OcCNNIGlobalStatsBrokenRoot_Type()
)
ocCNNIGlobalStatsBrokenRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIGlobalStatsBrokenRoot.setStatus("optional")
_OcCNNIGlobalStatsRerouteWaiting_Type = Counter32
_OcCNNIGlobalStatsRerouteWaiting_Object = MibScalar
ocCNNIGlobalStatsRerouteWaiting = _OcCNNIGlobalStatsRerouteWaiting_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 5, 7),
    _OcCNNIGlobalStatsRerouteWaiting_Type()
)
ocCNNIGlobalStatsRerouteWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIGlobalStatsRerouteWaiting.setStatus("optional")
_OcCNNIAddrStats_Object = MibTable
ocCNNIAddrStats = _OcCNNIAddrStats_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6)
)
if mibBuilder.loadTexts:
    ocCNNIAddrStats.setStatus("optional")
_OcCNNIAddrStatsEntry_Object = MibTableRow
ocCNNIAddrStatsEntry = _OcCNNIAddrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1)
)
ocCNNIAddrStatsEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIAddress"),
)
if mibBuilder.loadTexts:
    ocCNNIAddrStatsEntry.setStatus("optional")
_OcCNNIAddrStatsToTotal_Type = Counter32
_OcCNNIAddrStatsToTotal_Object = MibTableColumn
ocCNNIAddrStatsToTotal = _OcCNNIAddrStatsToTotal_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 1),
    _OcCNNIAddrStatsToTotal_Type()
)
ocCNNIAddrStatsToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsToTotal.setStatus("optional")
_OcCNNIAddrStatsToCreated_Type = Counter32
_OcCNNIAddrStatsToCreated_Object = MibTableColumn
ocCNNIAddrStatsToCreated = _OcCNNIAddrStatsToCreated_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 2),
    _OcCNNIAddrStatsToCreated_Type()
)
ocCNNIAddrStatsToCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsToCreated.setStatus("optional")
_OcCNNIAddrStatsToOneWay_Type = Counter32
_OcCNNIAddrStatsToOneWay_Object = MibTableColumn
ocCNNIAddrStatsToOneWay = _OcCNNIAddrStatsToOneWay_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 3),
    _OcCNNIAddrStatsToOneWay_Type()
)
ocCNNIAddrStatsToOneWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsToOneWay.setStatus("optional")
_OcCNNIAddrStatsToConnected_Type = Counter32
_OcCNNIAddrStatsToConnected_Object = MibTableColumn
ocCNNIAddrStatsToConnected = _OcCNNIAddrStatsToConnected_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 4),
    _OcCNNIAddrStatsToConnected_Type()
)
ocCNNIAddrStatsToConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsToConnected.setStatus("optional")
_OcCNNIAddrStatsToBrokenLeaf_Type = Counter32
_OcCNNIAddrStatsToBrokenLeaf_Object = MibTableColumn
ocCNNIAddrStatsToBrokenLeaf = _OcCNNIAddrStatsToBrokenLeaf_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 5),
    _OcCNNIAddrStatsToBrokenLeaf_Type()
)
ocCNNIAddrStatsToBrokenLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsToBrokenLeaf.setStatus("optional")
_OcCNNIAddrStatsToBrokenRoot_Type = Counter32
_OcCNNIAddrStatsToBrokenRoot_Object = MibTableColumn
ocCNNIAddrStatsToBrokenRoot = _OcCNNIAddrStatsToBrokenRoot_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 6),
    _OcCNNIAddrStatsToBrokenRoot_Type()
)
ocCNNIAddrStatsToBrokenRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsToBrokenRoot.setStatus("optional")
_OcCNNIAddrStatsToRerouteWaiting_Type = Counter32
_OcCNNIAddrStatsToRerouteWaiting_Object = MibTableColumn
ocCNNIAddrStatsToRerouteWaiting = _OcCNNIAddrStatsToRerouteWaiting_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 7),
    _OcCNNIAddrStatsToRerouteWaiting_Type()
)
ocCNNIAddrStatsToRerouteWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsToRerouteWaiting.setStatus("optional")
_OcCNNIAddrStatsFromTotal_Type = Counter32
_OcCNNIAddrStatsFromTotal_Object = MibTableColumn
ocCNNIAddrStatsFromTotal = _OcCNNIAddrStatsFromTotal_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 8),
    _OcCNNIAddrStatsFromTotal_Type()
)
ocCNNIAddrStatsFromTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsFromTotal.setStatus("optional")
_OcCNNIAddrStatsFromCreated_Type = Counter32
_OcCNNIAddrStatsFromCreated_Object = MibTableColumn
ocCNNIAddrStatsFromCreated = _OcCNNIAddrStatsFromCreated_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 9),
    _OcCNNIAddrStatsFromCreated_Type()
)
ocCNNIAddrStatsFromCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsFromCreated.setStatus("optional")
_OcCNNIAddrStatsFromOneWay_Type = Counter32
_OcCNNIAddrStatsFromOneWay_Object = MibTableColumn
ocCNNIAddrStatsFromOneWay = _OcCNNIAddrStatsFromOneWay_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 10),
    _OcCNNIAddrStatsFromOneWay_Type()
)
ocCNNIAddrStatsFromOneWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsFromOneWay.setStatus("optional")
_OcCNNIAddrStatsFromConnected_Type = Counter32
_OcCNNIAddrStatsFromConnected_Object = MibTableColumn
ocCNNIAddrStatsFromConnected = _OcCNNIAddrStatsFromConnected_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 11),
    _OcCNNIAddrStatsFromConnected_Type()
)
ocCNNIAddrStatsFromConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsFromConnected.setStatus("optional")
_OcCNNIAddrStatsFromBrokenLeaf_Type = Counter32
_OcCNNIAddrStatsFromBrokenLeaf_Object = MibTableColumn
ocCNNIAddrStatsFromBrokenLeaf = _OcCNNIAddrStatsFromBrokenLeaf_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 12),
    _OcCNNIAddrStatsFromBrokenLeaf_Type()
)
ocCNNIAddrStatsFromBrokenLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsFromBrokenLeaf.setStatus("optional")
_OcCNNIAddrStatsFromBrokenRoot_Type = Counter32
_OcCNNIAddrStatsFromBrokenRoot_Object = MibTableColumn
ocCNNIAddrStatsFromBrokenRoot = _OcCNNIAddrStatsFromBrokenRoot_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 13),
    _OcCNNIAddrStatsFromBrokenRoot_Type()
)
ocCNNIAddrStatsFromBrokenRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsFromBrokenRoot.setStatus("optional")
_OcCNNIAddrStatsFromRerouteWaiting_Type = Counter32
_OcCNNIAddrStatsFromRerouteWaiting_Object = MibTableColumn
ocCNNIAddrStatsFromRerouteWaiting = _OcCNNIAddrStatsFromRerouteWaiting_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 6, 1, 14),
    _OcCNNIAddrStatsFromRerouteWaiting_Type()
)
ocCNNIAddrStatsFromRerouteWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIAddrStatsFromRerouteWaiting.setStatus("optional")
_OcCNNIAliasTable_Object = MibTable
ocCNNIAliasTable = _OcCNNIAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 7)
)
if mibBuilder.loadTexts:
    ocCNNIAliasTable.setStatus("optional")
_OcCNNIAliasTableEntry_Object = MibTableRow
ocCNNIAliasTableEntry = _OcCNNIAliasTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 7, 1)
)
ocCNNIAliasTableEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIAddress"),
)
if mibBuilder.loadTexts:
    ocCNNIAliasTableEntry.setStatus("optional")
_OcCNNIAlias_Type = OctetString
_OcCNNIAlias_Object = MibTableColumn
ocCNNIAlias = _OcCNNIAlias_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 7, 1, 1),
    _OcCNNIAlias_Type()
)
ocCNNIAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIAlias.setStatus("optional")
_OcCNNIConnDB_ObjectIdentity = ObjectIdentity
ocCNNIConnDB = _OcCNNIConnDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8)
)
_OcCNNIFilterAssignID_Type = Integer32
_OcCNNIFilterAssignID_Object = MibScalar
ocCNNIFilterAssignID = _OcCNNIFilterAssignID_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 1),
    _OcCNNIFilterAssignID_Type()
)
ocCNNIFilterAssignID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIFilterAssignID.setStatus("optional")
_OcCNNIFilterTable_Object = MibTable
ocCNNIFilterTable = _OcCNNIFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2)
)
if mibBuilder.loadTexts:
    ocCNNIFilterTable.setStatus("optional")
_OcCNNIFilterTableEntry_Object = MibTableRow
ocCNNIFilterTableEntry = _OcCNNIFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1)
)
ocCNNIFilterTableEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIFilterID"),
)
if mibBuilder.loadTexts:
    ocCNNIFilterTableEntry.setStatus("optional")
_OcCNNIFilterID_Type = Integer32
_OcCNNIFilterID_Object = MibTableColumn
ocCNNIFilterID = _OcCNNIFilterID_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 1),
    _OcCNNIFilterID_Type()
)
ocCNNIFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNIFilterID.setStatus("optional")


class _OcCNNIFilterTypePres_Type(Integer32):
    """Custom type ocCNNIFilterTypePres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 0),
          ("present", 1))
    )


_OcCNNIFilterTypePres_Type.__name__ = "Integer32"
_OcCNNIFilterTypePres_Object = MibTableColumn
ocCNNIFilterTypePres = _OcCNNIFilterTypePres_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 2),
    _OcCNNIFilterTypePres_Type()
)
ocCNNIFilterTypePres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterTypePres.setStatus("optional")


class _OcCNNIFilterTypeData_Type(Integer32):
    """Custom type ocCNNIFilterTypeData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pointtomulitpoint", 1),
          ("pointtopoint", 0))
    )


_OcCNNIFilterTypeData_Type.__name__ = "Integer32"
_OcCNNIFilterTypeData_Object = MibTableColumn
ocCNNIFilterTypeData = _OcCNNIFilterTypeData_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 3),
    _OcCNNIFilterTypeData_Type()
)
ocCNNIFilterTypeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterTypeData.setStatus("optional")


class _OcCNNIFilterInPortPres_Type(Integer32):
    """Custom type ocCNNIFilterInPortPres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 0),
          ("present", 1))
    )


_OcCNNIFilterInPortPres_Type.__name__ = "Integer32"
_OcCNNIFilterInPortPres_Object = MibTableColumn
ocCNNIFilterInPortPres = _OcCNNIFilterInPortPres_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 4),
    _OcCNNIFilterInPortPres_Type()
)
ocCNNIFilterInPortPres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterInPortPres.setStatus("optional")
_OcCNNIFilterInPortData_Type = Integer32
_OcCNNIFilterInPortData_Object = MibTableColumn
ocCNNIFilterInPortData = _OcCNNIFilterInPortData_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 5),
    _OcCNNIFilterInPortData_Type()
)
ocCNNIFilterInPortData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterInPortData.setStatus("optional")


class _OcCNNIFilterOutPortPres_Type(Integer32):
    """Custom type ocCNNIFilterOutPortPres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 0),
          ("present", 1))
    )


_OcCNNIFilterOutPortPres_Type.__name__ = "Integer32"
_OcCNNIFilterOutPortPres_Object = MibTableColumn
ocCNNIFilterOutPortPres = _OcCNNIFilterOutPortPres_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 6),
    _OcCNNIFilterOutPortPres_Type()
)
ocCNNIFilterOutPortPres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterOutPortPres.setStatus("optional")
_OcCNNIFilterOutPortData_Type = Integer32
_OcCNNIFilterOutPortData_Object = MibTableColumn
ocCNNIFilterOutPortData = _OcCNNIFilterOutPortData_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 7),
    _OcCNNIFilterOutPortData_Type()
)
ocCNNIFilterOutPortData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterOutPortData.setStatus("optional")


class _OcCNNIFilterCgPtyPres_Type(Integer32):
    """Custom type ocCNNIFilterCgPtyPres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 0),
          ("present", 1))
    )


_OcCNNIFilterCgPtyPres_Type.__name__ = "Integer32"
_OcCNNIFilterCgPtyPres_Object = MibTableColumn
ocCNNIFilterCgPtyPres = _OcCNNIFilterCgPtyPres_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 8),
    _OcCNNIFilterCgPtyPres_Type()
)
ocCNNIFilterCgPtyPres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterCgPtyPres.setStatus("optional")
_OcCNNIFilterCgPtyData_Type = OctetString
_OcCNNIFilterCgPtyData_Object = MibTableColumn
ocCNNIFilterCgPtyData = _OcCNNIFilterCgPtyData_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 9),
    _OcCNNIFilterCgPtyData_Type()
)
ocCNNIFilterCgPtyData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterCgPtyData.setStatus("optional")


class _OcCNNIFilterCdPtyPres_Type(Integer32):
    """Custom type ocCNNIFilterCdPtyPres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 0),
          ("present", 1))
    )


_OcCNNIFilterCdPtyPres_Type.__name__ = "Integer32"
_OcCNNIFilterCdPtyPres_Object = MibTableColumn
ocCNNIFilterCdPtyPres = _OcCNNIFilterCdPtyPres_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 10),
    _OcCNNIFilterCdPtyPres_Type()
)
ocCNNIFilterCdPtyPres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterCdPtyPres.setStatus("optional")
_OcCNNIFilterCdPtyData_Type = OctetString
_OcCNNIFilterCdPtyData_Object = MibTableColumn
ocCNNIFilterCdPtyData = _OcCNNIFilterCdPtyData_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 11),
    _OcCNNIFilterCdPtyData_Type()
)
ocCNNIFilterCdPtyData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterCdPtyData.setStatus("optional")


class _OcCNNIFilterStatePres_Type(Integer32):
    """Custom type ocCNNIFilterStatePres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 0),
          ("present", 1))
    )


_OcCNNIFilterStatePres_Type.__name__ = "Integer32"
_OcCNNIFilterStatePres_Object = MibTableColumn
ocCNNIFilterStatePres = _OcCNNIFilterStatePres_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 12),
    _OcCNNIFilterStatePres_Type()
)
ocCNNIFilterStatePres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterStatePres.setStatus("optional")


class _OcCNNIFilterStateData_Type(Integer32):
    """Custom type ocCNNIFilterStateData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("brokenleaf", 4),
          ("brokenroot", 3),
          ("connected", 2),
          ("created", 0),
          ("oneway", 1),
          ("reroutewaiting", 5))
    )


_OcCNNIFilterStateData_Type.__name__ = "Integer32"
_OcCNNIFilterStateData_Object = MibTableColumn
ocCNNIFilterStateData = _OcCNNIFilterStateData_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 2, 1, 13),
    _OcCNNIFilterStateData_Type()
)
ocCNNIFilterStateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocCNNIFilterStateData.setStatus("optional")
_OcCNNISessTable_Object = MibTable
ocCNNISessTable = _OcCNNISessTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 3)
)
if mibBuilder.loadTexts:
    ocCNNISessTable.setStatus("optional")
_OcCNNISessTableEntry_Object = MibTableRow
ocCNNISessTableEntry = _OcCNNISessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 3, 1)
)
ocCNNISessTableEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNIFilterID"),
    (0, "Olicom-crossfireAtmSwitch-MIB", "ocCNNISessID"),
)
if mibBuilder.loadTexts:
    ocCNNISessTableEntry.setStatus("optional")
_OcCNNISessID_Type = Integer32
_OcCNNISessID_Object = MibTableColumn
ocCNNISessID = _OcCNNISessID_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 3, 1, 1),
    _OcCNNISessID_Type()
)
ocCNNISessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNISessID.setStatus("optional")


class _OcCNNISessDataType_Type(Integer32):
    """Custom type ocCNNISessDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pointtomulitpoint", 1),
          ("pointtopoint", 0))
    )


_OcCNNISessDataType_Type.__name__ = "Integer32"
_OcCNNISessDataType_Object = MibTableColumn
ocCNNISessDataType = _OcCNNISessDataType_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 3, 1, 2),
    _OcCNNISessDataType_Type()
)
ocCNNISessDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNISessDataType.setStatus("optional")
_OcCNNISessDataInPort_Type = Integer32
_OcCNNISessDataInPort_Object = MibTableColumn
ocCNNISessDataInPort = _OcCNNISessDataInPort_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 3, 1, 3),
    _OcCNNISessDataInPort_Type()
)
ocCNNISessDataInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNISessDataInPort.setStatus("optional")
_OcCNNISessDataOutPort_Type = Integer32
_OcCNNISessDataOutPort_Object = MibTableColumn
ocCNNISessDataOutPort = _OcCNNISessDataOutPort_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 3, 1, 4),
    _OcCNNISessDataOutPort_Type()
)
ocCNNISessDataOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNISessDataOutPort.setStatus("optional")
_OcCNNISessDataCgPty_Type = OctetString
_OcCNNISessDataCgPty_Object = MibTableColumn
ocCNNISessDataCgPty = _OcCNNISessDataCgPty_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 3, 1, 5),
    _OcCNNISessDataCgPty_Type()
)
ocCNNISessDataCgPty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNISessDataCgPty.setStatus("optional")
_OcCNNISessDataCdPty_Type = OctetString
_OcCNNISessDataCdPty_Object = MibTableColumn
ocCNNISessDataCdPty = _OcCNNISessDataCdPty_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 3, 1, 6),
    _OcCNNISessDataCdPty_Type()
)
ocCNNISessDataCdPty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNISessDataCdPty.setStatus("optional")


class _OcCNNISessDataState_Type(Integer32):
    """Custom type ocCNNISessDataState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("brokenleaf", 4),
          ("brokenroot", 3),
          ("connected", 2),
          ("created", 0),
          ("oneway", 1),
          ("reroutewaiting", 5))
    )


_OcCNNISessDataState_Type.__name__ = "Integer32"
_OcCNNISessDataState_Object = MibTableColumn
ocCNNISessDataState = _OcCNNISessDataState_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 3, 8, 3, 1, 7),
    _OcCNNISessDataState_Type()
)
ocCNNISessDataState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocCNNISessDataState.setStatus("optional")
_OcDsx3_ObjectIdentity = ObjectIdentity
ocDsx3 = _OcDsx3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4)
)
_OcDsx3MIBObjs_ObjectIdentity = ObjectIdentity
ocDsx3MIBObjs = _OcDsx3MIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1)
)
_OcDsx3ConfigTable_Object = MibTable
ocDsx3ConfigTable = _OcDsx3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ocDsx3ConfigTable.setStatus("mandatory")
_OcDsx3ConfigEntry_Object = MibTableRow
ocDsx3ConfigEntry = _OcDsx3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 1, 1)
)
ocDsx3ConfigEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "dsx3LineIndex"),
)
if mibBuilder.loadTexts:
    ocDsx3ConfigEntry.setStatus("mandatory")


class _OcDsx3Xor55_Type(Integer32):
    """Custom type ocDsx3Xor55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OcDsx3Xor55_Type.__name__ = "Integer32"
_OcDsx3Xor55_Object = MibTableColumn
ocDsx3Xor55 = _OcDsx3Xor55_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 1, 1, 1),
    _OcDsx3Xor55_Type()
)
ocDsx3Xor55.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocDsx3Xor55.setStatus("mandatory")


class _OcDsx3Scrambling_Type(Integer32):
    """Custom type ocDsx3Scrambling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OcDsx3Scrambling_Type.__name__ = "Integer32"
_OcDsx3Scrambling_Object = MibTableColumn
ocDsx3Scrambling = _OcDsx3Scrambling_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 1, 1, 2),
    _OcDsx3Scrambling_Type()
)
ocDsx3Scrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocDsx3Scrambling.setStatus("mandatory")


class _OcDsx3Delineation_Type(Integer32):
    """Custom type ocDsx3Delineation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hec", 1),
          ("plcp", 2))
    )


_OcDsx3Delineation_Type.__name__ = "Integer32"
_OcDsx3Delineation_Object = MibTableColumn
ocDsx3Delineation = _OcDsx3Delineation_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 1, 1, 3),
    _OcDsx3Delineation_Type()
)
ocDsx3Delineation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocDsx3Delineation.setStatus("mandatory")


class _OcDsx3HcsPassThru_Type(Integer32):
    """Custom type ocDsx3HcsPassThru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OcDsx3HcsPassThru_Type.__name__ = "Integer32"
_OcDsx3HcsPassThru_Object = MibTableColumn
ocDsx3HcsPassThru = _OcDsx3HcsPassThru_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 1, 1, 4),
    _OcDsx3HcsPassThru_Type()
)
ocDsx3HcsPassThru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocDsx3HcsPassThru.setStatus("mandatory")


class _OcDsx3Ext8kRefClk_Type(Integer32):
    """Custom type ocDsx3Ext8kRefClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled-master", 1),
          ("slave", 3))
    )


_OcDsx3Ext8kRefClk_Type.__name__ = "Integer32"
_OcDsx3Ext8kRefClk_Object = MibTableColumn
ocDsx3Ext8kRefClk = _OcDsx3Ext8kRefClk_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 1, 1, 5),
    _OcDsx3Ext8kRefClk_Type()
)
ocDsx3Ext8kRefClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocDsx3Ext8kRefClk.setStatus("mandatory")


class _OcDsx3ShortCable_Type(Integer32):
    """Custom type ocDsx3ShortCable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OcDsx3ShortCable_Type.__name__ = "Integer32"
_OcDsx3ShortCable_Object = MibTableColumn
ocDsx3ShortCable = _OcDsx3ShortCable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 1, 1, 6),
    _OcDsx3ShortCable_Type()
)
ocDsx3ShortCable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocDsx3ShortCable.setStatus("mandatory")


class _OcDsx3CntHcsCorrectedErrs_Type(Integer32):
    """Custom type ocDsx3CntHcsCorrectedErrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OcDsx3CntHcsCorrectedErrs_Type.__name__ = "Integer32"
_OcDsx3CntHcsCorrectedErrs_Object = MibTableColumn
ocDsx3CntHcsCorrectedErrs = _OcDsx3CntHcsCorrectedErrs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 1, 1, 7),
    _OcDsx3CntHcsCorrectedErrs_Type()
)
ocDsx3CntHcsCorrectedErrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocDsx3CntHcsCorrectedErrs.setStatus("mandatory")
_OcDsx3SuniPdhTable_Object = MibTable
ocDsx3SuniPdhTable = _OcDsx3SuniPdhTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2)
)
if mibBuilder.loadTexts:
    ocDsx3SuniPdhTable.setStatus("mandatory")
_OcDsx3SuniPdhEntry_Object = MibTableRow
ocDsx3SuniPdhEntry = _OcDsx3SuniPdhEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1)
)
ocDsx3SuniPdhEntry.setIndexNames(
    (0, "Olicom-crossfireAtmSwitch-MIB", "dsx3LineIndex"),
)
if mibBuilder.loadTexts:
    ocDsx3SuniPdhEntry.setStatus("mandatory")
_OcDsx3SuniPmonLcv_Type = Integer32
_OcDsx3SuniPmonLcv_Object = MibTableColumn
ocDsx3SuniPmonLcv = _OcDsx3SuniPmonLcv_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 1),
    _OcDsx3SuniPmonLcv_Type()
)
ocDsx3SuniPmonLcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniPmonLcv.setStatus("mandatory")
_OcDsx3SuniPmonFerr_Type = Integer32
_OcDsx3SuniPmonFerr_Object = MibTableColumn
ocDsx3SuniPmonFerr = _OcDsx3SuniPmonFerr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 2),
    _OcDsx3SuniPmonFerr_Type()
)
ocDsx3SuniPmonFerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniPmonFerr.setStatus("mandatory")
_OcDsx3SuniPmonExzs_Type = Integer32
_OcDsx3SuniPmonExzs_Object = MibTableColumn
ocDsx3SuniPmonExzs = _OcDsx3SuniPmonExzs_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 3),
    _OcDsx3SuniPmonExzs_Type()
)
ocDsx3SuniPmonExzs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniPmonExzs.setStatus("mandatory")
_OcDsx3SuniPmonPeec_Type = Integer32
_OcDsx3SuniPmonPeec_Object = MibTableColumn
ocDsx3SuniPmonPeec = _OcDsx3SuniPmonPeec_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 4),
    _OcDsx3SuniPmonPeec_Type()
)
ocDsx3SuniPmonPeec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniPmonPeec.setStatus("mandatory")
_OcDsx3SuniPmonPpec_Type = Integer32
_OcDsx3SuniPmonPpec_Object = MibTableColumn
ocDsx3SuniPmonPpec = _OcDsx3SuniPmonPpec_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 5),
    _OcDsx3SuniPmonPpec_Type()
)
ocDsx3SuniPmonPpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniPmonPpec.setStatus("mandatory")
_OcDsx3SuniPmonFebeErr_Type = Integer32
_OcDsx3SuniPmonFebeErr_Object = MibTableColumn
ocDsx3SuniPmonFebeErr = _OcDsx3SuniPmonFebeErr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 6),
    _OcDsx3SuniPmonFebeErr_Type()
)
ocDsx3SuniPmonFebeErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniPmonFebeErr.setStatus("mandatory")
_OcDsx3SuniB1Bip8Err_Type = Integer32
_OcDsx3SuniB1Bip8Err_Object = MibTableColumn
ocDsx3SuniB1Bip8Err = _OcDsx3SuniB1Bip8Err_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 7),
    _OcDsx3SuniB1Bip8Err_Type()
)
ocDsx3SuniB1Bip8Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniB1Bip8Err.setStatus("mandatory")
_OcDsx3SuniCppmFrameErr_Type = Integer32
_OcDsx3SuniCppmFrameErr_Object = MibTableColumn
ocDsx3SuniCppmFrameErr = _OcDsx3SuniCppmFrameErr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 8),
    _OcDsx3SuniCppmFrameErr_Type()
)
ocDsx3SuniCppmFrameErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniCppmFrameErr.setStatus("mandatory")
_OcDsx3SuniCppmFebeErr_Type = Integer32
_OcDsx3SuniCppmFebeErr_Object = MibTableColumn
ocDsx3SuniCppmFebeErr = _OcDsx3SuniCppmFebeErr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 9),
    _OcDsx3SuniCppmFebeErr_Type()
)
ocDsx3SuniCppmFebeErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniCppmFebeErr.setStatus("mandatory")
_OcDsx3SuniCppmHcsErr_Type = Integer32
_OcDsx3SuniCppmHcsErr_Object = MibTableColumn
ocDsx3SuniCppmHcsErr = _OcDsx3SuniCppmHcsErr_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 10),
    _OcDsx3SuniCppmHcsErr_Type()
)
ocDsx3SuniCppmHcsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniCppmHcsErr.setStatus("mandatory")
_OcDsx3SuniCppmRcvCells_Type = Integer32
_OcDsx3SuniCppmRcvCells_Object = MibTableColumn
ocDsx3SuniCppmRcvCells = _OcDsx3SuniCppmRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 11),
    _OcDsx3SuniCppmRcvCells_Type()
)
ocDsx3SuniCppmRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniCppmRcvCells.setStatus("mandatory")
_OcDsx3SuniCppmXmtCells_Type = Integer32
_OcDsx3SuniCppmXmtCells_Object = MibTableColumn
ocDsx3SuniCppmXmtCells = _OcDsx3SuniCppmXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 12),
    _OcDsx3SuniCppmXmtCells_Type()
)
ocDsx3SuniCppmXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniCppmXmtCells.setStatus("mandatory")
_OcDsx3SuniCppmIdleCells_Type = Integer32
_OcDsx3SuniCppmIdleCells_Object = MibTableColumn
ocDsx3SuniCppmIdleCells = _OcDsx3SuniCppmIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 13),
    _OcDsx3SuniCppmIdleCells_Type()
)
ocDsx3SuniCppmIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniCppmIdleCells.setStatus("mandatory")
_OcDsx3SuniCppmMegaRcvCells_Type = Integer32
_OcDsx3SuniCppmMegaRcvCells_Object = MibTableColumn
ocDsx3SuniCppmMegaRcvCells = _OcDsx3SuniCppmMegaRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 14),
    _OcDsx3SuniCppmMegaRcvCells_Type()
)
ocDsx3SuniCppmMegaRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniCppmMegaRcvCells.setStatus("mandatory")
_OcDsx3SuniCppmMegaXmtCells_Type = Integer32
_OcDsx3SuniCppmMegaXmtCells_Object = MibTableColumn
ocDsx3SuniCppmMegaXmtCells = _OcDsx3SuniCppmMegaXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 15),
    _OcDsx3SuniCppmMegaXmtCells_Type()
)
ocDsx3SuniCppmMegaXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniCppmMegaXmtCells.setStatus("mandatory")
_OcDsx3SuniCppmMegaIdleCells_Type = Integer32
_OcDsx3SuniCppmMegaIdleCells_Object = MibTableColumn
ocDsx3SuniCppmMegaIdleCells = _OcDsx3SuniCppmMegaIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 7, 4, 1, 2, 1, 16),
    _OcDsx3SuniCppmMegaIdleCells_Type()
)
ocDsx3SuniCppmMegaIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocDsx3SuniCppmMegaIdleCells.setStatus("mandatory")

# Managed Objects groups


# Notification objects

restart = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 1)
)
restart.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "termRestartInfoRestartTime"),
        ("Olicom-crossfireAtmSwitch-MIB", "termRestartInfoRestartReason"),
        ("Olicom-crossfireAtmSwitch-MIB", "termRestartInfoTerminationReason"),
        ("Olicom-crossfireAtmSwitch-MIB", "termRestartInfoBbsram"))
)
if mibBuilder.loadTexts:
    restart.setStatus(
        ""
    )

globalCongestionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 3)
)
globalCongestionTrap.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statsGlobalCongestionState"),
        ("Olicom-crossfireAtmSwitch-MIB", "statsGlobalCongestionDiscardCellRate"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    globalCongestionTrap.setStatus(
        ""
    )

globalInvalidCellRateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 4)
)
globalInvalidCellRateTrap.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statsInvalidCellRateState"),
        ("Olicom-crossfireAtmSwitch-MIB", "statsInvalidCellRate"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    globalInvalidCellRateTrap.setStatus(
        ""
    )

cpuPortCongestionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 5)
)
cpuPortCongestionTrap.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statsCpuPortCongestionState"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    cpuPortCongestionTrap.setStatus(
        ""
    )

queueCongestionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 6)
)
queueCongestionTrap.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statsQueueCongestionSlotIndex"),
        ("Olicom-crossfireAtmSwitch-MIB", "statsQueueCongestionIPortRIndex"),
        ("Olicom-crossfireAtmSwitch-MIB", "statsQueueCongestionQueueIndex"),
        ("Olicom-crossfireAtmSwitch-MIB", "statsQueueCongestionConditionState"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    queueCongestionTrap.setStatus(
        ""
    )

ePortHecErrorRateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 7)
)
ePortHecErrorRateTrap.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statsEPortIfIndex"),
        ("Olicom-crossfireAtmSwitch-MIB", "statusEPortXModuleIndex"),
        ("Olicom-crossfireAtmSwitch-MIB", "statusEPortRIndex"),
        ("Olicom-crossfireAtmSwitch-MIB", "statsEPortHecErrorRateConditionState"),
        ("Olicom-crossfireAtmSwitch-MIB", "statsEPortRxHecErrorCellRate"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    ePortHecErrorRateTrap.setStatus(
        ""
    )

iPortTxParityErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 8)
)
iPortTxParityErrorTrap.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statsIPortSlotIndex"),
        ("Olicom-crossfireAtmSwitch-MIB", "statsIPortRIndex"),
        ("Olicom-crossfireAtmSwitch-MIB", "statsIPortTxParityErrorCellCounter"))
)
if mibBuilder.loadTexts:
    iPortTxParityErrorTrap.setStatus(
        ""
    )

ePortAutoDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 9)
)
ePortAutoDisabled.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statusEPortIfIndex"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    ePortAutoDisabled.setStatus(
        ""
    )

featureModuleStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 10)
)
featureModuleStatusChange.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statusFeatureModuleOperStatus"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    featureModuleStatusChange.setStatus(
        ""
    )

xModuleStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 11)
)
xModuleStatusChange.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statusXModuleSlotIndex"),
        ("Olicom-crossfireAtmSwitch-MIB", "statusXModuleOperStatus"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    xModuleStatusChange.setStatus(
        ""
    )

temperatureWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 12)
)
temperatureWarningTrap.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statusCurrentTemperatureConditionState"),
        ("Olicom-crossfireAtmSwitch-MIB", "statusCurrentTemperatureGauge"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    temperatureWarningTrap.setStatus(
        ""
    )

fanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 13)
)
fanFailureTrap.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statusFanOperStatus"),
        ("Olicom-crossfireAtmSwitch-MIB", "statusCurrentTemperatureGauge"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    fanFailureTrap.setStatus(
        ""
    )

psuFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 14)
)
psuFailureTrap.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statusPsuIndex"),
        ("Olicom-crossfireAtmSwitch-MIB", "statusPsuOperStatus"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    psuFailureTrap.setStatus(
        ""
    )

temperatureCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 15)
)
temperatureCriticalTrap.setObjects(
      *(("Olicom-crossfireAtmSwitch-MIB", "statusCurrentTemperatureConditionState"),
        ("Olicom-crossfireAtmSwitch-MIB", "statusCurrentTemperatureGauge"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    temperatureCriticalTrap.setStatus(
        ""
    )

oamFlowNoResponseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 2, 6, 0, 16)
)
oamFlowNoResponseTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("Olicom-MIB", "controlTime"))
)
if mibBuilder.loadTexts:
    oamFlowNoResponseTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Olicom-crossfireAtmSwitch-MIB",
    **{"AtmAddress": AtmAddress,
       "olicom": olicom,
       "ocmibs": ocmibs,
       "ocmibsCrossfireAtmMIB": ocmibsCrossfireAtmMIB,
       "restart": restart,
       "globalCongestionTrap": globalCongestionTrap,
       "globalInvalidCellRateTrap": globalInvalidCellRateTrap,
       "cpuPortCongestionTrap": cpuPortCongestionTrap,
       "queueCongestionTrap": queueCongestionTrap,
       "ePortHecErrorRateTrap": ePortHecErrorRateTrap,
       "iPortTxParityErrorTrap": iPortTxParityErrorTrap,
       "ePortAutoDisabled": ePortAutoDisabled,
       "featureModuleStatusChange": featureModuleStatusChange,
       "xModuleStatusChange": xModuleStatusChange,
       "temperatureWarningTrap": temperatureWarningTrap,
       "fanFailureTrap": fanFailureTrap,
       "psuFailureTrap": psuFailureTrap,
       "temperatureCriticalTrap": temperatureCriticalTrap,
       "oamFlowNoResponseTrap": oamFlowNoResponseTrap,
       "crossfireAtmInfo": crossfireAtmInfo,
       "infoProcessorModule": infoProcessorModule,
       "infoProcessorModuleHwProductId": infoProcessorModuleHwProductId,
       "infoProcessorModuleHwVersion": infoProcessorModuleHwVersion,
       "infoProcessorModuleHwEcoLevel": infoProcessorModuleHwEcoLevel,
       "infoProcessorModuleHwSerialNumber": infoProcessorModuleHwSerialNumber,
       "infoProcessorModuleHwOptionTable": infoProcessorModuleHwOptionTable,
       "infoProcessorModuleHwOptionEntry": infoProcessorModuleHwOptionEntry,
       "infoProcessorModuleHwOptionNo": infoProcessorModuleHwOptionNo,
       "infoProcessorModuleHwOption": infoProcessorModuleHwOption,
       "infoFeatureModule": infoFeatureModule,
       "infoFeatureModuleHwProductId": infoFeatureModuleHwProductId,
       "infoFeatureModuleHwVersion": infoFeatureModuleHwVersion,
       "infoFeatureModuleHwEcoLevel": infoFeatureModuleHwEcoLevel,
       "infoFeatureModuleHwSerialNumber": infoFeatureModuleHwSerialNumber,
       "infoFeatureModuleHwOptionTable": infoFeatureModuleHwOptionTable,
       "infoFeatureModuleHwOptionEntry": infoFeatureModuleHwOptionEntry,
       "infoFeatureModuleHwOptionNo": infoFeatureModuleHwOptionNo,
       "infoFeatureModuleHwOption": infoFeatureModuleHwOption,
       "infoXModule": infoXModule,
       "infoXModuleTable": infoXModuleTable,
       "infoXModuleEntry": infoXModuleEntry,
       "infoXModuleSlotIndex": infoXModuleSlotIndex,
       "infoXModuleHwProductId": infoXModuleHwProductId,
       "infoXModuleHwVersion": infoXModuleHwVersion,
       "infoXModuleHwEcoLevel": infoXModuleHwEcoLevel,
       "infoXModuleHwSerialNumber": infoXModuleHwSerialNumber,
       "infoXModuleHwOptionTable": infoXModuleHwOptionTable,
       "infoXModuleHwOptionEntry": infoXModuleHwOptionEntry,
       "infoXModuleHwOptionSlotIndex": infoXModuleHwOptionSlotIndex,
       "infoXModuleHwOptionNo": infoXModuleHwOptionNo,
       "infoXModuleHwOption": infoXModuleHwOption,
       "infoIfIndex": infoIfIndex,
       "infoIfIndexLan": infoIfIndexLan,
       "infoIfIndexSlip": infoIfIndexSlip,
       "infoIfIndexElan": infoIfIndexElan,
       "infoIfIndexClassicalIp": infoIfIndexClassicalIp,
       "infoIfIndexRfc1483Bridged": infoIfIndexRfc1483Bridged,
       "infoIfIndexRfc1483Routed": infoIfIndexRfc1483Routed,
       "infoIfIndexAtmNode": infoIfIndexAtmNode,
       "termRestartInfo": termRestartInfo,
       "termRestartInfoRestartTime": termRestartInfoRestartTime,
       "termRestartInfoSwSection1StatusWord": termRestartInfoSwSection1StatusWord,
       "termRestartInfoSwSection2StatusWord": termRestartInfoSwSection2StatusWord,
       "termRestartInfoSwImageLoaded": termRestartInfoSwImageLoaded,
       "termRestartInfoFutureTestMode": termRestartInfoFutureTestMode,
       "termRestartInfoBootpExecuted": termRestartInfoBootpExecuted,
       "termRestartInfoReloadTime": termRestartInfoReloadTime,
       "termRestartInfoBootpReason": termRestartInfoBootpReason,
       "termRestartInfoServerIpAddress": termRestartInfoServerIpAddress,
       "termRestartInfoServerMacAddress": termRestartInfoServerMacAddress,
       "termRestartInfoFileName": termRestartInfoFileName,
       "termRestartInfoBbsramTerminationTimestamp": termRestartInfoBbsramTerminationTimestamp,
       "termRestartInfoTerminationReason": termRestartInfoTerminationReason,
       "termRestartInfoRestartReason": termRestartInfoRestartReason,
       "termRestartInfoHwReconfigState": termRestartInfoHwReconfigState,
       "termRestartInfoBbsram": termRestartInfoBbsram,
       "crossfireAtmConfiguration": crossfireAtmConfiguration,
       "configAddressing": configAddressing,
       "configSwitchAddrPrefixType": configSwitchAddrPrefixType,
       "configSwitchAddrPrefixSize": configSwitchAddrPrefixSize,
       "configSwitchAddrAtmPrefix": configSwitchAddrAtmPrefix,
       "configSwitchAddrAtmAddress": configSwitchAddrAtmAddress,
       "configClocking": configClocking,
       "configNetworkClockSource": configNetworkClockSource,
       "configNetworkClockEPortIndex": configNetworkClockEPortIndex,
       "configLane": configLane,
       "configLaneControlAdminStatus": configLaneControlAdminStatus,
       "configLaneControlLecsAdminStatus": configLaneControlLecsAdminStatus,
       "configLaneControlLesBusAdminStatus": configLaneControlLesBusAdminStatus,
       "configMonitoring": configMonitoring,
       "configMonitorEPortAdminStatus": configMonitorEPortAdminStatus,
       "configMonitorEPortIPortSlotIndex": configMonitorEPortIPortSlotIndex,
       "configMonitorEPortIPortRIndex": configMonitorEPortIPortRIndex,
       "configMonitorEPortDirection": configMonitorEPortDirection,
       "configTm": configTm,
       "configTmControlMode": configTmControlMode,
       "configTmControlEarlyPacketDiscardAdminStatus": configTmControlEarlyPacketDiscardAdminStatus,
       "configTmControlVbrTrafficAllocation": configTmControlVbrTrafficAllocation,
       "configTmControlErTuningAlpha": configTmControlErTuningAlpha,
       "configTmControlErTuningBeta": configTmControlErTuningBeta,
       "configTmControlErTuningGamma": configTmControlErTuningGamma,
       "configTmControlErTuningDelta": configTmControlErTuningDelta,
       "configTmControlErTuningLambda": configTmControlErTuningLambda,
       "configTmControlErTuningTau": configTmControlErTuningTau,
       "configTmControlErTuningPhi": configTmControlErTuningPhi,
       "configTmControlErTuningPsi": configTmControlErTuningPsi,
       "configTmServiceClassMapTable": configTmServiceClassMapTable,
       "configTmServiceClassMapEntry": configTmServiceClassMapEntry,
       "configTmServiceClassMapServiceClass": configTmServiceClassMapServiceClass,
       "configTmServiceClassMapSchedulingQueue": configTmServiceClassMapSchedulingQueue,
       "configTrafficDescr": configTrafficDescr,
       "trafficDescriptorTableNextIndex": trafficDescriptorTableNextIndex,
       "trafficDescriptorTable": trafficDescriptorTable,
       "trafficDescriptorEntry": trafficDescriptorEntry,
       "trafficDescriptorIndex": trafficDescriptorIndex,
       "trafficDescriptorCreationMode": trafficDescriptorCreationMode,
       "trafficDescriptorServiceClass": trafficDescriptorServiceClass,
       "trafficDescriptorPcr01": trafficDescriptorPcr01,
       "trafficDescriptorPcr0": trafficDescriptorPcr0,
       "trafficDescriptorScr01": trafficDescriptorScr01,
       "trafficDescriptorScr0": trafficDescriptorScr0,
       "trafficDescriptorMbs01": trafficDescriptorMbs01,
       "trafficDescriptorMbs0": trafficDescriptorMbs0,
       "trafficDescriptorTaggingFlag": trafficDescriptorTaggingFlag,
       "trafficDescriptorFrameDiscardFlag": trafficDescriptorFrameDiscardFlag,
       "trafficDescriptorBestEffortFlag": trafficDescriptorBestEffortFlag,
       "trafficDescriptorMcr": trafficDescriptorMcr,
       "trafficDescriptorAbrIcr": trafficDescriptorAbrIcr,
       "trafficDescriptorAbrTbe": trafficDescriptorAbrTbe,
       "trafficDescriptorAbrFrtt": trafficDescriptorAbrFrtt,
       "trafficDescriptorAbrRif": trafficDescriptorAbrRif,
       "trafficDescriptorAbrRdf": trafficDescriptorAbrRdf,
       "trafficDescriptorAbrNrm": trafficDescriptorAbrNrm,
       "trafficDescriptorAbrTrm": trafficDescriptorAbrTrm,
       "trafficDescriptorAbrCdf": trafficDescriptorAbrCdf,
       "trafficDescriptorAbrAdtf": trafficDescriptorAbrAdtf,
       "trafficDescriptorTrafficType": trafficDescriptorTrafficType,
       "trafficDescriptorRowStatus": trafficDescriptorRowStatus,
       "trafficDescriptorCtd": trafficDescriptorCtd,
       "trafficDescriptorCdv": trafficDescriptorCdv,
       "trafficDescriptorLogClr": trafficDescriptorLogClr,
       "configServiceReg": configServiceReg,
       "configIlmiServiceRegistryTable": configIlmiServiceRegistryTable,
       "configIlmiServiceRegistryEntry": configIlmiServiceRegistryEntry,
       "configIlmiServiceRegistryAddressIndex": configIlmiServiceRegistryAddressIndex,
       "configIlmiServiceRegistryServiceId": configIlmiServiceRegistryServiceId,
       "configIlmiServiceRegistryAtmAddress": configIlmiServiceRegistryAtmAddress,
       "configIlmiServiceRegistryParm1": configIlmiServiceRegistryParm1,
       "configIlmiServiceRegistryRowStatus": configIlmiServiceRegistryRowStatus,
       "configSar": configSar,
       "configSarMuxFillThreshold": configSarMuxFillThreshold,
       "configSarMuxSarVpi": configSarMuxSarVpi,
       "configSarEmptyCellHandling": configSarEmptyCellHandling,
       "configXModule": configXModule,
       "configXModuleTable": configXModuleTable,
       "configXModuleEntry": configXModuleEntry,
       "configXModuleSlotIndex": configXModuleSlotIndex,
       "configXModuleAdminStatus": configXModuleAdminStatus,
       "configFeatureModule": configFeatureModule,
       "configFeatureModuleAdminStatus": configFeatureModuleAdminStatus,
       "configCommonEPort": configCommonEPort,
       "configCommonEPortIlmiAdminStatus": configCommonEPortIlmiAdminStatus,
       "configCommonEPortAddrRegistrationAdminStatus": configCommonEPortAddrRegistrationAdminStatus,
       "configCommonEPortMaxVpcs": configCommonEPortMaxVpcs,
       "configCommonEPortMaxVccs": configCommonEPortMaxVccs,
       "configCommonEPortMaxVpiBits": configCommonEPortMaxVpiBits,
       "configCommonEPortMaxVciBits": configCommonEPortMaxVciBits,
       "configCommonEPortUniType": configCommonEPortUniType,
       "configCommonEPortUniVersion": configCommonEPortUniVersion,
       "configCommonEPortDeviceType": configCommonEPortDeviceType,
       "configCommonEPortIlmiVersion": configCommonEPortIlmiVersion,
       "configCommonEPortNniSigVersion": configCommonEPortNniSigVersion,
       "configCommonEPortSignallingVpi": configCommonEPortSignallingVpi,
       "configCommonEPortSignallingVci": configCommonEPortSignallingVci,
       "configCommonEPortIlmiVpi": configCommonEPortIlmiVpi,
       "configCommonEPortIlmiVci": configCommonEPortIlmiVci,
       "configCommonEPortLecsVpi": configCommonEPortLecsVpi,
       "configCommonEPortLecsVci": configCommonEPortLecsVci,
       "configCommonEPortPnniVpi": configCommonEPortPnniVpi,
       "configCommonEPortPnniVci": configCommonEPortPnniVci,
       "configCommonEPortAbrBandwidthAllocation": configCommonEPortAbrBandwidthAllocation,
       "configCommonEPortVbrRtBandwidthAllocation": configCommonEPortVbrRtBandwidthAllocation,
       "configCommonEPortVbrNrtBandwidthAllocation": configCommonEPortVbrNrtBandwidthAllocation,
       "configCommonEPortCbrBandwidthAllocation": configCommonEPortCbrBandwidthAllocation,
       "configStaticEPortIlmiPollFrequency": configStaticEPortIlmiPollFrequency,
       "configStaticEPortIlmiPollRetries": configStaticEPortIlmiPollRetries,
       "configStaticEPortMaxTransientPhyFailureTime": configStaticEPortMaxTransientPhyFailureTime,
       "configStaticEPortMaxPhyFailuresPerMinute": configStaticEPortMaxPhyFailuresPerMinute,
       "configCommonEPortLinkDelay": configCommonEPortLinkDelay,
       "configCommonEPortTransientPhyOffTime": configCommonEPortTransientPhyOffTime,
       "configCommonEPortTransientPhyWindowTime": configCommonEPortTransientPhyWindowTime,
       "configCommonEPortTransientPhyDisconnectCount": configCommonEPortTransientPhyDisconnectCount,
       "configCommonEPortTransientPhyDisconnectTimer": configCommonEPortTransientPhyDisconnectTimer,
       "configCommonEPortDefaultSigVersion": configCommonEPortDefaultSigVersion,
       "configCommonEPortMaxSvpcVpi": configCommonEPortMaxSvpcVpi,
       "configCommonEPortMaxSvccVpi": configCommonEPortMaxSvccVpi,
       "configCommonEPortMinSvccVci": configCommonEPortMinSvccVci,
       "configEPort": configEPort,
       "configEPortScratchPadScratchPadStatus": configEPortScratchPadScratchPadStatus,
       "configEPortScratchPadEPortIndex": configEPortScratchPadEPortIndex,
       "configEPortScratchPadIpAddress": configEPortScratchPadIpAddress,
       "configEPortScratchPadActionStatus": configEPortScratchPadActionStatus,
       "configEPortScratchPadHwConfigTxClocking": configEPortScratchPadHwConfigTxClocking,
       "configEPortScratchPadHwConfigSonetSdh": configEPortScratchPadHwConfigSonetSdh,
       "configEPortScratchPadUseCommonEPortConfig": configEPortScratchPadUseCommonEPortConfig,
       "configEPortScratchPadLoopback": configEPortScratchPadLoopback,
       "configEPortScratchPadIlmiConfigIlmiAdminStatus": configEPortScratchPadIlmiConfigIlmiAdminStatus,
       "configEPortScratchPadIlmiConfigAddrRegistrationAdminStatus": configEPortScratchPadIlmiConfigAddrRegistrationAdminStatus,
       "configEPortScratchPadIlmiConfigMaxVpcs": configEPortScratchPadIlmiConfigMaxVpcs,
       "configEPortScratchPadIlmiConfigMaxVccs": configEPortScratchPadIlmiConfigMaxVccs,
       "configEPortScratchPadIlmiConfigMaxVpiBits": configEPortScratchPadIlmiConfigMaxVpiBits,
       "configEPortScratchPadIlmiConfigMaxVciBits": configEPortScratchPadIlmiConfigMaxVciBits,
       "configEPortScratchPadIlmiConfigUniType": configEPortScratchPadIlmiConfigUniType,
       "configEPortScratchPadIlmiConfigUniVersion": configEPortScratchPadIlmiConfigUniVersion,
       "configEPortScratchPadIlmiConfigDeviceType": configEPortScratchPadIlmiConfigDeviceType,
       "configEPortScratchPadIlmiConfigIlmiVersion": configEPortScratchPadIlmiConfigIlmiVersion,
       "configEPortScratchPadIlmiConfigNniSigVersion": configEPortScratchPadIlmiConfigNniSigVersion,
       "configEPortScratchPadIlmiConfigSignallingVpi": configEPortScratchPadIlmiConfigSignallingVpi,
       "configEPortScratchPadIlmiConfigSignallingVci": configEPortScratchPadIlmiConfigSignallingVci,
       "configEPortScratchPadIlmiConfigIlmiVpi": configEPortScratchPadIlmiConfigIlmiVpi,
       "configEPortScratchPadIlmiConfigIlmiVci": configEPortScratchPadIlmiConfigIlmiVci,
       "configEPortScratchPadIlmiConfigLecsVpi": configEPortScratchPadIlmiConfigLecsVpi,
       "configEPortScratchPadIlmiConfigLecsVci": configEPortScratchPadIlmiConfigLecsVci,
       "configEPortScratchPadIlmiConfigPnniVpi": configEPortScratchPadIlmiConfigPnniVpi,
       "configEPortScratchPadIlmiConfigPnniVci": configEPortScratchPadIlmiConfigPnniVci,
       "configEPortScratchPadAbrBandwidthAllocation": configEPortScratchPadAbrBandwidthAllocation,
       "configEPortScratchPadVbrRtBandwidthAllocation": configEPortScratchPadVbrRtBandwidthAllocation,
       "configEPortScratchPadVbrNrtBandwidthAllocation": configEPortScratchPadVbrNrtBandwidthAllocation,
       "configEPortScratchPadCbrBandwidthAllocation": configEPortScratchPadCbrBandwidthAllocation,
       "configEPortScratchPadLinkDelay": configEPortScratchPadLinkDelay,
       "configEPortScratchPadTransientPhyOffTime": configEPortScratchPadTransientPhyOffTime,
       "configEPortScratchPadTransientPhyWindowTime": configEPortScratchPadTransientPhyWindowTime,
       "configEPortScratchPadTransientPhyDisconnectCount": configEPortScratchPadTransientPhyDisconnectCount,
       "configEPortScratchPadTransientPhyDisconnectTimer": configEPortScratchPadTransientPhyDisconnectTimer,
       "configEPortScratchPadBandwidthLimit": configEPortScratchPadBandwidthLimit,
       "configEPortTable": configEPortTable,
       "configEPortEntry": configEPortEntry,
       "configEPortIfIndex": configEPortIfIndex,
       "configEPortHwConfigTxClocking": configEPortHwConfigTxClocking,
       "configEPortHwConfigSonetSdh": configEPortHwConfigSonetSdh,
       "configEPortUseCommonEPortConfig": configEPortUseCommonEPortConfig,
       "configEPortLoopback": configEPortLoopback,
       "configEPortIlmiConfigIlmiAdminStatus": configEPortIlmiConfigIlmiAdminStatus,
       "configEPortIlmiConfigAddrRegistrationAdminStatus": configEPortIlmiConfigAddrRegistrationAdminStatus,
       "configEPortIlmiConfigMaxVpcs": configEPortIlmiConfigMaxVpcs,
       "configEPortIlmiConfigMaxVccs": configEPortIlmiConfigMaxVccs,
       "configEPortIlmiConfigMaxVpiBits": configEPortIlmiConfigMaxVpiBits,
       "configEPortIlmiConfigMaxVciBits": configEPortIlmiConfigMaxVciBits,
       "configEPortIlmiConfigUniType": configEPortIlmiConfigUniType,
       "configEPortIlmiConfigUniVersion": configEPortIlmiConfigUniVersion,
       "configEPortIlmiConfigDeviceType": configEPortIlmiConfigDeviceType,
       "configEPortIlmiConfigIlmiVersion": configEPortIlmiConfigIlmiVersion,
       "configEPortIlmiConfigNniSigVersion": configEPortIlmiConfigNniSigVersion,
       "configEPortIlmiConfigSignallingVpi": configEPortIlmiConfigSignallingVpi,
       "configEPortIlmiConfigSignallingVci": configEPortIlmiConfigSignallingVci,
       "configEPortIlmiConfigIlmiVpi": configEPortIlmiConfigIlmiVpi,
       "configEPortIlmiConfigIlmiVci": configEPortIlmiConfigIlmiVci,
       "configEPortIlmiConfigLecsVpi": configEPortIlmiConfigLecsVpi,
       "configEPortIlmiConfigLecsVci": configEPortIlmiConfigLecsVci,
       "configEPortIlmiConfigPnniVpi": configEPortIlmiConfigPnniVpi,
       "configEPortIlmiConfigPnniVci": configEPortIlmiConfigPnniVci,
       "configEPortAbrBandwidthAllocation": configEPortAbrBandwidthAllocation,
       "configEPortVbrRtBandwidthAllocation": configEPortVbrRtBandwidthAllocation,
       "configEPortVbrNrtBandwidthAllocation": configEPortVbrNrtBandwidthAllocation,
       "configEPortCbrBandwidthAllocation": configEPortCbrBandwidthAllocation,
       "configEPortLinkDelay": configEPortLinkDelay,
       "configEPortTransientPhyOffTime": configEPortTransientPhyOffTime,
       "configEPortTransientPhyWindowTime": configEPortTransientPhyWindowTime,
       "configEPortTransientPhyDisconnectCount": configEPortTransientPhyDisconnectCount,
       "configEPortTransientPhyDisconnectTimer": configEPortTransientPhyDisconnectTimer,
       "configEPortBandwidthLimit": configEPortBandwidthLimit,
       "configEPortDefaultSigVersion": configEPortDefaultSigVersion,
       "configEPortIlmiConfigMaxSvpcVpi": configEPortIlmiConfigMaxSvpcVpi,
       "configEPortIlmiConfigMaxSvccVpi": configEPortIlmiConfigMaxSvccVpi,
       "configEPortIlmiConfigMinSvccVci": configEPortIlmiConfigMinSvccVci,
       "configEPortScratchPadDefaultSigVersion": configEPortScratchPadDefaultSigVersion,
       "configEPortScratchPadIlmiConfigMaxSvpcVpi": configEPortScratchPadIlmiConfigMaxSvpcVpi,
       "configEPortScratchPadIlmiConfigMaxSvccVpi": configEPortScratchPadIlmiConfigMaxSvccVpi,
       "configEPortScratchPadIlmiConfigMinSvccVci": configEPortScratchPadIlmiConfigMinSvccVci,
       "configCpuQ": configCpuQ,
       "configCpuPortCpuQueueSize": configCpuPortCpuQueueSize,
       "configCpuPortResetQueueSize": configCpuPortResetQueueSize,
       "configCommonIPort": configCommonIPort,
       "configCommonIPortQueueTable": configCommonIPortQueueTable,
       "configCommonIPortQueueEntry": configCommonIPortQueueEntry,
       "configCommonIPortQueueIndex": configCommonIPortQueueIndex,
       "configCommonIPortEfciTaggingAdminStatus": configCommonIPortEfciTaggingAdminStatus,
       "configCommonIPortClpDiscardAdminStatus": configCommonIPortClpDiscardAdminStatus,
       "configCommonIPortEfciTaggingThreshold": configCommonIPortEfciTaggingThreshold,
       "configCommonIPortClpDiscardThreshold": configCommonIPortClpDiscardThreshold,
       "configCommonIPortQueueSize": configCommonIPortQueueSize,
       "configCommonIPortLogClr": configCommonIPortLogClr,
       "configCommonIPortCdv": configCommonIPortCdv,
       "configIPort": configIPort,
       "configIPortScratchPadScratchPadStatus": configIPortScratchPadScratchPadStatus,
       "configIPortScratchPadSlotIndex": configIPortScratchPadSlotIndex,
       "configIPortScratchPadIPortRIndex": configIPortScratchPadIPortRIndex,
       "configIPortScratchPadIpAddress": configIPortScratchPadIpAddress,
       "configIPortScratchPadActionStatus": configIPortScratchPadActionStatus,
       "configIPortScratchPadUseCommonIPortConfig": configIPortScratchPadUseCommonIPortConfig,
       "configIPortScratchPadQueueTable": configIPortScratchPadQueueTable,
       "configIPortScratchPadQueueEntry": configIPortScratchPadQueueEntry,
       "configIPortScratchPadQueueQueueIndex": configIPortScratchPadQueueQueueIndex,
       "configIPortScratchPadQueueEfciTaggingAdminStatus": configIPortScratchPadQueueEfciTaggingAdminStatus,
       "configIPortScratchPadQueueClpDiscardAdminStatus": configIPortScratchPadQueueClpDiscardAdminStatus,
       "configIPortScratchPadQueueEfciTaggingThreshold": configIPortScratchPadQueueEfciTaggingThreshold,
       "configIPortScratchPadQueueClpDiscardThreshold": configIPortScratchPadQueueClpDiscardThreshold,
       "configIPortScratchPadQueueSize": configIPortScratchPadQueueSize,
       "configIPortScratchPadQueueLogClr": configIPortScratchPadQueueLogClr,
       "configIPortScratchPadQueueCdv": configIPortScratchPadQueueCdv,
       "configIPortTable": configIPortTable,
       "configIPortEntry": configIPortEntry,
       "configIPortSlotIndex": configIPortSlotIndex,
       "configIPortRIndex": configIPortRIndex,
       "configIPortUseCommonIPortConfig": configIPortUseCommonIPortConfig,
       "configIPortQueueTable": configIPortQueueTable,
       "configIPortQueueEntry": configIPortQueueEntry,
       "configIPortQueueSlotIndex": configIPortQueueSlotIndex,
       "configIPortQueueRIndex": configIPortQueueRIndex,
       "configIPortQueueQueueIndex": configIPortQueueQueueIndex,
       "configIPortQueueEfciTaggingAdminStatus": configIPortQueueEfciTaggingAdminStatus,
       "configIPortQueueClpDiscardAdminStatus": configIPortQueueClpDiscardAdminStatus,
       "configIPortQueueEfciTaggingThreshold": configIPortQueueEfciTaggingThreshold,
       "configIPortQueueClpDiscardThreshold": configIPortQueueClpDiscardThreshold,
       "configIPortQueueSize": configIPortQueueSize,
       "configIPortQueueLogClr": configIPortQueueLogClr,
       "configIPortQueueCdv": configIPortQueueCdv,
       "configPvpPvc": configPvpPvc,
       "pvpSetupTableNextIndex": pvpSetupTableNextIndex,
       "pvpSetupTable": pvpSetupTable,
       "pvpSetupEntry": pvpSetupEntry,
       "pvpSetupIndex": pvpSetupIndex,
       "pvpSetupApplication": pvpSetupApplication,
       "pvpSetupLowEPortIndex": pvpSetupLowEPortIndex,
       "pvpSetupLowVpi": pvpSetupLowVpi,
       "pvpSetupHighEPortIndex": pvpSetupHighEPortIndex,
       "pvpSetupHighVpi": pvpSetupHighVpi,
       "pvpSetupVpCrossConnectIndex": pvpSetupVpCrossConnectIndex,
       "pvpSetupL2HTrafficDescriptorIndex": pvpSetupL2HTrafficDescriptorIndex,
       "pvpSetupH2LTrafficDescriptorIndex": pvpSetupH2LTrafficDescriptorIndex,
       "pvpSetupRowStatus": pvpSetupRowStatus,
       "pvcSetupTableNextIndex": pvcSetupTableNextIndex,
       "pvcSetupTable": pvcSetupTable,
       "pvcSetupEntry": pvcSetupEntry,
       "pvcSetupIndex": pvcSetupIndex,
       "pvcSetupApplication": pvcSetupApplication,
       "pvcSetupLowEPortIndex": pvcSetupLowEPortIndex,
       "pvcSetupLowVpi": pvcSetupLowVpi,
       "pvcSetupLowVci": pvcSetupLowVci,
       "pvcSetupHighEPortIndex": pvcSetupHighEPortIndex,
       "pvcSetupHighVpi": pvcSetupHighVpi,
       "pvcSetupHighVci": pvcSetupHighVci,
       "pvcSetupVcCrossConnectIndex": pvcSetupVcCrossConnectIndex,
       "pvcSetupL2HTrafficDescriptorIndex": pvcSetupL2HTrafficDescriptorIndex,
       "pvcSetupH2LTrafficDescriptorIndex": pvcSetupH2LTrafficDescriptorIndex,
       "pvcSetupRowStatus": pvcSetupRowStatus,
       "configSvpSvc": configSvpSvc,
       "svpSetupTableNextIndex": svpSetupTableNextIndex,
       "svpSetupTable": svpSetupTable,
       "svpSetupEntry": svpSetupEntry,
       "svpSetupIndex": svpSetupIndex,
       "svpSetupApplication": svpSetupApplication,
       "svpSetupEPortIndex": svpSetupEPortIndex,
       "svpSetupPreferredVpi": svpSetupPreferredVpi,
       "svpSetupTermAtmAddr": svpSetupTermAtmAddr,
       "svpSetupVpCrossConnectIndex": svpSetupVpCrossConnectIndex,
       "svpSetupTxTrafficDescriptorIndex": svpSetupTxTrafficDescriptorIndex,
       "svpSetupRxTrafficDescriptorIndex": svpSetupRxTrafficDescriptorIndex,
       "svpSetupRowStatus": svpSetupRowStatus,
       "svcSetupTableNextIndex": svcSetupTableNextIndex,
       "svcSetupTable": svcSetupTable,
       "svcSetupEntry": svcSetupEntry,
       "svcSetupIndex": svcSetupIndex,
       "svcSetupApplication": svcSetupApplication,
       "svcSetupTermAtmAddr": svcSetupTermAtmAddr,
       "svcSetupVcCrossConnectIndex": svcSetupVcCrossConnectIndex,
       "svcSetupTxTrafficDescriptorIndex": svcSetupTxTrafficDescriptorIndex,
       "svcSetupRxTrafficDescriptorIndex": svcSetupRxTrafficDescriptorIndex,
       "svcSetupRowStatus": svcSetupRowStatus,
       "configCommonSignalling": configCommonSignalling,
       "configCommonSignallingMaxTunnels": configCommonSignallingMaxTunnels,
       "configCommonSignallingMaxSaps": configCommonSignallingMaxSaps,
       "configCommonSignallingMaxPvcs": configCommonSignallingMaxPvcs,
       "configCommonSignallingMaxSvcs": configCommonSignallingMaxSvcs,
       "configCommonSignallingMaxConManStevs": configCommonSignallingMaxConManStevs,
       "configCommonSignallingMaxSigProtStevs": configCommonSignallingMaxSigProtStevs,
       "configCommonSignallingT301": configCommonSignallingT301,
       "configCommonSignallingT302": configCommonSignallingT302,
       "configCommonSignallingT303": configCommonSignallingT303,
       "configCommonSignallingT304": configCommonSignallingT304,
       "configCommonSignallingT306": configCommonSignallingT306,
       "configCommonSignallingT308": configCommonSignallingT308,
       "configCommonSignallingT309": configCommonSignallingT309,
       "configCommonSignallingT310": configCommonSignallingT310,
       "configCommonSignallingT313": configCommonSignallingT313,
       "configCommonSignallingT316": configCommonSignallingT316,
       "configCommonSignallingT317": configCommonSignallingT317,
       "configCommonSignallingT322": configCommonSignallingT322,
       "configCommonSignallingT331": configCommonSignallingT331,
       "configCommonSignallingT333": configCommonSignallingT333,
       "configCommonSignallingT397": configCommonSignallingT397,
       "configCommonSignallingT398": configCommonSignallingT398,
       "configCommonSignallingT399": configCommonSignallingT399,
       "configCommonSignallingPtmpMaxLeafs": configCommonSignallingPtmpMaxLeafs,
       "configCommonSignallingPtmpMaxLeafOperations": configCommonSignallingPtmpMaxLeafOperations,
       "configCommonSignallingPtmpMaxLeafsDropByClear": configCommonSignallingPtmpMaxLeafsDropByClear,
       "configCommonSignallingPtmpMaxP2mpSvcs": configCommonSignallingPtmpMaxP2mpSvcs,
       "configCommonSscopMaxSaps": configCommonSscopMaxSaps,
       "configCommonSscopMaxLinks": configCommonSscopMaxLinks,
       "configCommonSscopMaxRcvWinSize": configCommonSscopMaxRcvWinSize,
       "configCommonSscopMaxCc": configCommonSscopMaxCc,
       "configCommonSscopMaxPd": configCommonSscopMaxPd,
       "configCommonSscopMaxStat": configCommonSscopMaxStat,
       "configCommonSscopTimerPoll": configCommonSscopTimerPoll,
       "configCommonSscopTimerNoResponse": configCommonSscopTimerNoResponse,
       "configCommonSscopTimerKeepAlive": configCommonSscopTimerKeepAlive,
       "configCommonSscopTimerIdle": configCommonSscopTimerIdle,
       "configCommonSscopTimerCc": configCommonSscopTimerCc,
       "configCommonSscopMaxSduSize": configCommonSscopMaxSduSize,
       "configCommonSscopMaxUuSize": configCommonSscopMaxUuSize,
       "configIisp": configIisp,
       "configNextHopRoutingTableNextIndex": configNextHopRoutingTableNextIndex,
       "configNextHopRoutingTable": configNextHopRoutingTable,
       "configNextHopRoutingEntry": configNextHopRoutingEntry,
       "configNextHopRoutingIndex": configNextHopRoutingIndex,
       "configNextHopRoutingAtmAddress": configNextHopRoutingAtmAddress,
       "configNextHopRoutingAddressLength": configNextHopRoutingAddressLength,
       "configNextHopRoutingEPort": configNextHopRoutingEPort,
       "configNextHopRoutingSignallingType": configNextHopRoutingSignallingType,
       "configNextHopRoutingRowStatus": configNextHopRoutingRowStatus,
       "configIpArp": configIpArp,
       "atmIpArpTable": atmIpArpTable,
       "atmIpArpEntry": atmIpArpEntry,
       "atmIpArpServerIndex": atmIpArpServerIndex,
       "atmIpArpIpAddress": atmIpArpIpAddress,
       "atmIpArpAtmAddress": atmIpArpAtmAddress,
       "atmIpArpType": atmIpArpType,
       "configIpArpServerTableNextIndex": configIpArpServerTableNextIndex,
       "configIpArpServerTable": configIpArpServerTable,
       "configIpArpServerEntry": configIpArpServerEntry,
       "configIpArpServerIndex": configIpArpServerIndex,
       "configIpArpServerAtmAddressSpec": configIpArpServerAtmAddressSpec,
       "configIpArpServerAtmAddressMask": configIpArpServerAtmAddressMask,
       "configIpArpServerAtmAddressActual": configIpArpServerAtmAddressActual,
       "configIpArpServerIpSubnetAddress": configIpArpServerIpSubnetAddress,
       "configIpArpServerIpSubnetMask": configIpArpServerIpSubnetMask,
       "configIpArpServerAdminStatus": configIpArpServerAdminStatus,
       "configIpArpServerOperStatus": configIpArpServerOperStatus,
       "configIpArpServerRowStatus": configIpArpServerRowStatus,
       "configClipArpServer": configClipArpServer,
       "configQosClass": configQosClass,
       "qosClassTable": qosClassTable,
       "qosClassEntry": qosClassEntry,
       "qosClassClass": qosClassClass,
       "qosClassCtd": qosClassCtd,
       "qosClassCdv": qosClassCdv,
       "qosClassLogClr": qosClassLogClr,
       "configSerial": configSerial,
       "configSerialObmSlip": configSerialObmSlip,
       "configOam": configOam,
       "ifMIBObjects": ifMIBObjects,
       "ifTestTable": ifTestTable,
       "ifTestEntry": ifTestEntry,
       "ifTestId": ifTestId,
       "ifTestStatus": ifTestStatus,
       "ifTestType": ifTestType,
       "ifTestResult": ifTestResult,
       "ifTestCode": ifTestCode,
       "ifTestOwner": ifTestOwner,
       "atmTESTMIBObjects": atmTESTMIBObjects,
       "atmLoopbackTestGroup": atmLoopbackTestGroup,
       "atmLoopbackTestTypes": atmLoopbackTestTypes,
       "atmLoopbackVpE2e": atmLoopbackVpE2e,
       "atmLoopbackVcE2e": atmLoopbackVcE2e,
       "atmLoopbackVpSegment": atmLoopbackVpSegment,
       "atmLoopbackVcSegment": atmLoopbackVcSegment,
       "configTest": configTest,
       "controlDeleteCode": controlDeleteCode,
       "controlDeleteConfig": controlDeleteConfig,
       "configPriorityBuffer": configPriorityBuffer,
       "configPriorityBufferTable": configPriorityBufferTable,
       "configPriorityBufferEntry": configPriorityBufferEntry,
       "configPriorityBufferIndex": configPriorityBufferIndex,
       "configPriorityBufferSize": configPriorityBufferSize,
       "crossfireAtmStatus": crossfireAtmStatus,
       "statusBasicHw": statusBasicHw,
       "statusHwChassisCurrentXModules": statusHwChassisCurrentXModules,
       "statusHwChassisCurrentEPorts": statusHwChassisCurrentEPorts,
       "statusHwChassisUpsOperState": statusHwChassisUpsOperState,
       "statusHwChassisSwitchingSystemSize": statusHwChassisSwitchingSystemSize,
       "statusHwChassisCellBufferSize": statusHwChassisCellBufferSize,
       "statusCurrentTemperatureConditionState": statusCurrentTemperatureConditionState,
       "statusCurrentTemperatureGauge": statusCurrentTemperatureGauge,
       "statusCurrentTemperatureLatch": statusCurrentTemperatureLatch,
       "statusCurrentTemperatureLatchTime": statusCurrentTemperatureLatchTime,
       "statusFanOperStatus": statusFanOperStatus,
       "statusPsuStatusTable": statusPsuStatusTable,
       "statusPsuStatusEntry": statusPsuStatusEntry,
       "statusPsuIndex": statusPsuIndex,
       "statusPsuOperStatus": statusPsuOperStatus,
       "statusProcessorModule": statusProcessorModule,
       "statusProcessorModuleStatusLed": statusProcessorModuleStatusLed,
       "statusProcessorModuleFaultLed": statusProcessorModuleFaultLed,
       "statusFeatureModule": statusFeatureModule,
       "statusFeatureModuleOperStatus": statusFeatureModuleOperStatus,
       "statusFeatureModuleStatusLed": statusFeatureModuleStatusLed,
       "statusXModule": statusXModule,
       "statusXModuleTable": statusXModuleTable,
       "statusXModuleEntry": statusXModuleEntry,
       "statusXModuleSlotIndex": statusXModuleSlotIndex,
       "statusXModuleOperStatus": statusXModuleOperStatus,
       "statusXModuleNoOfSlotsUsed": statusXModuleNoOfSlotsUsed,
       "statusXModuleIPort1SlotIndex": statusXModuleIPort1SlotIndex,
       "statusXModuleIPort1RIndex": statusXModuleIPort1RIndex,
       "statusXModuleIPort2SlotIndex": statusXModuleIPort2SlotIndex,
       "statusXModuleIPort2RIndex": statusXModuleIPort2RIndex,
       "statusXModuleIPort3SlotIndex": statusXModuleIPort3SlotIndex,
       "statusXModuleIPort3RIndex": statusXModuleIPort3RIndex,
       "statusXModuleIPort4SlotIndex": statusXModuleIPort4SlotIndex,
       "statusXModuleIPort4RIndex": statusXModuleIPort4RIndex,
       "statusEPort": statusEPort,
       "statusEPortTable": statusEPortTable,
       "statusEPortEntry": statusEPortEntry,
       "statusEPortIfIndex": statusEPortIfIndex,
       "statusEPortXModuleIndex": statusEPortXModuleIndex,
       "statusEPortRIndex": statusEPortRIndex,
       "statusEPortOperStatus": statusEPortOperStatus,
       "statusEPortPhyState": statusEPortPhyState,
       "statusEPortType": statusEPortType,
       "statusEPortRxSyncLedState": statusEPortRxSyncLedState,
       "statusEPortSignalLossLedState": statusEPortSignalLossLedState,
       "statusEPortPhyPortIndex": statusEPortPhyPortIndex,
       "statusEPortLoopbackState": statusEPortLoopbackState,
       "statusEPortLoopbackErrorCode": statusEPortLoopbackErrorCode,
       "statusEPortIlmiState": statusEPortIlmiState,
       "statusEPortAdjInfoTransmissionType": statusEPortAdjInfoTransmissionType,
       "statusEPortAdjInfoMediaType": statusEPortAdjInfoMediaType,
       "statusEPortAdjInfoIfName": statusEPortAdjInfoIfName,
       "statusEPortAdjInfoSystemIdentifier": statusEPortAdjInfoSystemIdentifier,
       "statusEPortAdjInfoMaxVpcs": statusEPortAdjInfoMaxVpcs,
       "statusEPortAdjInfoMaxVccs": statusEPortAdjInfoMaxVccs,
       "statusEPortAdjInfoMaxVpiBits": statusEPortAdjInfoMaxVpiBits,
       "statusEPortAdjInfoMaxVciBits": statusEPortAdjInfoMaxVciBits,
       "statusEPortAdjInfoUniType": statusEPortAdjInfoUniType,
       "statusEPortAdjInfoUniVersion": statusEPortAdjInfoUniVersion,
       "statusEPortAdjInfoDeviceType": statusEPortAdjInfoDeviceType,
       "statusEPortAdjInfoIlmiVersion": statusEPortAdjInfoIlmiVersion,
       "statusEPortAdjInfoNniSigVersion": statusEPortAdjInfoNniSigVersion,
       "statusEPortAutoconfigMaxVpcs": statusEPortAutoconfigMaxVpcs,
       "statusEPortAutoconfigMaxVccs": statusEPortAutoconfigMaxVccs,
       "statusEPortAutoconfigMaxVpiBits": statusEPortAutoconfigMaxVpiBits,
       "statusEPortAutoconfigMaxVciBits": statusEPortAutoconfigMaxVciBits,
       "statusEPortAutoconfigUniVersion": statusEPortAutoconfigUniVersion,
       "statusEPortAutoconfigDeviceType": statusEPortAutoconfigDeviceType,
       "statusEPortAutoconfigDerivedInterfaceType": statusEPortAutoconfigDerivedInterfaceType,
       "statusEPortAutoconfigMaxSvpcVpi": statusEPortAutoconfigMaxSvpcVpi,
       "statusEPortAutoconfigMaxSvccVpi": statusEPortAutoconfigMaxSvccVpi,
       "statusEPortAutoconfigMinSvccVci": statusEPortAutoconfigMinSvccVci,
       "statusEPortAdjInfoMaxSvpcVpi": statusEPortAdjInfoMaxSvpcVpi,
       "statusEPortAdjInfoMaxSvccVpi": statusEPortAdjInfoMaxSvccVpi,
       "statusEPortAdjInfoMinSvccVci": statusEPortAdjInfoMinSvccVci,
       "statusVpcVcc": statusVpcVcc,
       "vpcExtensionTable": vpcExtensionTable,
       "vpcExtensionEntry": vpcExtensionEntry,
       "vpcExtensionIndex": vpcExtensionIndex,
       "vpcExtensionVpCrossConnectIndex": vpcExtensionVpCrossConnectIndex,
       "vpcExtensionOrigAtmAddr": vpcExtensionOrigAtmAddr,
       "vpcExtensionTermAtmAddr": vpcExtensionTermAtmAddr,
       "vpcExtensionCapabilities": vpcExtensionCapabilities,
       "vccExtensionTable": vccExtensionTable,
       "vccExtensionEntry": vccExtensionEntry,
       "vccExtensionIndex": vccExtensionIndex,
       "vccExtensionVcCrossConnectIndex": vccExtensionVcCrossConnectIndex,
       "vccExtensionOrigAtmAddr": vccExtensionOrigAtmAddr,
       "vccExtensionTermAtmAddr": vccExtensionTermAtmAddr,
       "vccExtensionCapabilities": vccExtensionCapabilities,
       "vccExtensionEarlyPacketDiscard": vccExtensionEarlyPacketDiscard,
       "statusFatalLog": statusFatalLog,
       "statusFatalStatUsed": statusFatalStatUsed,
       "statusFatalStatFree": statusFatalStatFree,
       "statusFatalStatOverflow": statusFatalStatOverflow,
       "statusFatalStatMaxDumpLength": statusFatalStatMaxDumpLength,
       "statusFatalTable": statusFatalTable,
       "statusFatalEntry": statusFatalEntry,
       "statusFatalIndex": statusFatalIndex,
       "statusFatalSerial": statusFatalSerial,
       "statusFatalTimestamp": statusFatalTimestamp,
       "statusFatalTimeString": statusFatalTimeString,
       "statusFatalSource": statusFatalSource,
       "statusFatalLine": statusFatalLine,
       "statusFatalOriginalDumpSize": statusFatalOriginalDumpSize,
       "statusFatalDumpSize": statusFatalDumpSize,
       "statusFatalDump": statusFatalDump,
       "crossfireAtmStatistics": crossfireAtmStatistics,
       "statisticsGlobal": statisticsGlobal,
       "statsGlobalCongestionState": statsGlobalCongestionState,
       "statsGlobalCongestionDiscardCellRate": statsGlobalCongestionDiscardCellRate,
       "statsGlobalCongestionDiscardCellCounter": statsGlobalCongestionDiscardCellCounter,
       "statsGlobalCongestionDiscardCellLatch": statsGlobalCongestionDiscardCellLatch,
       "statsGlobalCongestionDiscardCellLatchTime": statsGlobalCongestionDiscardCellLatchTime,
       "statsInvalidCellRateState": statsInvalidCellRateState,
       "statsInvalidCellRate": statsInvalidCellRate,
       "statsInvalidCellCounter": statsInvalidCellCounter,
       "statsInvalidCellLatch": statsInvalidCellLatch,
       "statsInvalidCellLatchTime": statsInvalidCellLatchTime,
       "statisticsCpuPort": statisticsCpuPort,
       "statsCpuPortCongestionState": statsCpuPortCongestionState,
       "statsCpuPortDiscardCellRate": statsCpuPortDiscardCellRate,
       "statsCpuPortDiscardCellCounter": statsCpuPortDiscardCellCounter,
       "statsCpuPortDiscardCellLatch": statsCpuPortDiscardCellLatch,
       "statsCpuPortDiscardCellLatchTime": statsCpuPortDiscardCellLatchTime,
       "statisticsEPort": statisticsEPort,
       "statsEportTable": statsEportTable,
       "statsEportEntry": statsEportEntry,
       "statsEPortIfIndex": statsEPortIfIndex,
       "statsEPortHecErrorRateConditionState": statsEPortHecErrorRateConditionState,
       "statsEPortRxHecErrorCellRate": statsEPortRxHecErrorCellRate,
       "statsEPortRxHecErrorCellCounter": statsEPortRxHecErrorCellCounter,
       "statsEPortRxHecErrorCellLatch": statsEPortRxHecErrorCellLatch,
       "statsEPortRxHecErrorCellLatchTime": statsEPortRxHecErrorCellLatchTime,
       "statisticsIPort": statisticsIPort,
       "statsIPortTable": statsIPortTable,
       "statsIPortEntry": statsIPortEntry,
       "statsIPortSlotIndex": statsIPortSlotIndex,
       "statsIPortRIndex": statsIPortRIndex,
       "statsIPortRxCellRate": statsIPortRxCellRate,
       "statsIPortTxCellRate": statsIPortTxCellRate,
       "statsIPortTxParityErrorCellCounter": statsIPortTxParityErrorCellCounter,
       "statsQueueCongestionTable": statsQueueCongestionTable,
       "statsQueueCongestionEntry": statsQueueCongestionEntry,
       "statsQueueCongestionSlotIndex": statsQueueCongestionSlotIndex,
       "statsQueueCongestionIPortRIndex": statsQueueCongestionIPortRIndex,
       "statsQueueCongestionQueueIndex": statsQueueCongestionQueueIndex,
       "statsQueueCongestionConditionState": statsQueueCongestionConditionState,
       "statsQueueCongestionCellsInQueueGauge": statsQueueCongestionCellsInQueueGauge,
       "statsQueueCongestionCellsInQueueLatch": statsQueueCongestionCellsInQueueLatch,
       "statsQueueCongestionCellsInQueueLatchTime": statsQueueCongestionCellsInQueueLatchTime,
       "crossfireAtmTrapControl": crossfireAtmTrapControl,
       "fhTrapFrequencyCntrlFrequency": fhTrapFrequencyCntrlFrequency,
       "fhTrapFrequencyCntrlMaxTraps": fhTrapFrequencyCntrlMaxTraps,
       "fhTrapDashboardControlTable": fhTrapDashboardControlTable,
       "fhTrapDashboardControlEntry": fhTrapDashboardControlEntry,
       "fhTrapDashboardControlTrapTypeIndex": fhTrapDashboardControlTrapTypeIndex,
       "fhTrapDashboardControlFrequencyMode": fhTrapDashboardControlFrequencyMode,
       "fhTrapDashboardControlThresholdLow": fhTrapDashboardControlThresholdLow,
       "fhTrapDashboardControlThresholdHigh": fhTrapDashboardControlThresholdHigh,
       "fhTrapDashboardControlSamplingInterval": fhTrapDashboardControlSamplingInterval,
       "fhTrapDashboardControlNoSamples": fhTrapDashboardControlNoSamples,
       "temperatureCriticalTrapThreshold": temperatureCriticalTrapThreshold,
       "crossfireAtmTest": crossfireAtmTest,
       "crossfirexlx": crossfirexlx,
       "ocCNNI": ocCNNI,
       "ocCNNIMonSimple": ocCNNIMonSimple,
       "ocCNNIMonSEntry": ocCNNIMonSEntry,
       "ocCNNIRoutingTableChanged": ocCNNIRoutingTableChanged,
       "ocCNNINeighborTableChanged": ocCNNINeighborTableChanged,
       "ocCNNILineStatus": ocCNNILineStatus,
       "ocCNNIMACAddress": ocCNNIMACAddress,
       "ocCNNIMode": ocCNNIMode,
       "ocCNNIProtocolVersion": ocCNNIProtocolVersion,
       "ocCNNIApplID": ocCNNIApplID,
       "ocCNNIMonTables": ocCNNIMonTables,
       "ocCNNIRoutingTable": ocCNNIRoutingTable,
       "ocCNNIRoutingTableEntry": ocCNNIRoutingTableEntry,
       "ocCNNIAddress": ocCNNIAddress,
       "ocCNNIRoutingTableData": ocCNNIRoutingTableData,
       "ocCNNIAddressAlias": ocCNNIAddressAlias,
       "ocCNNINeighborTable": ocCNNINeighborTable,
       "ocCNNINeighborTableEntry": ocCNNINeighborTableEntry,
       "ocCNNIPort": ocCNNIPort,
       "ocCNNINeighborTableData": ocCNNINeighborTableData,
       "ocCNNITrapClientTable": ocCNNITrapClientTable,
       "ocCNNITrapClientTableEntry": ocCNNITrapClientTableEntry,
       "ocCNNITrapClientIndex": ocCNNITrapClientIndex,
       "ocCNNITrapClientAddress": ocCNNITrapClientAddress,
       "ocCNNITrapClientCommName": ocCNNITrapClientCommName,
       "ocCNNIConfig": ocCNNIConfig,
       "ocCNNIConfigMethod": ocCNNIConfigMethod,
       "ocCNNIConfigAlgorithm": ocCNNIConfigAlgorithm,
       "ocCNNIPortConfig": ocCNNIPortConfig,
       "ocCNNIPortEntry": ocCNNIPortEntry,
       "ocCNNIPortProtocol": ocCNNIPortProtocol,
       "ocCNNIPortBorder": ocCNNIPortBorder,
       "ocCNNIPortAutoreroute": ocCNNIPortAutoreroute,
       "ocCNNIPortReroute": ocCNNIPortReroute,
       "ocCNNIPortAssign": ocCNNIPortAssign,
       "ocCNNIGlobalStats": ocCNNIGlobalStats,
       "ocCNNIGlobalStatsTotal": ocCNNIGlobalStatsTotal,
       "ocCNNIGlobalStatsCreated": ocCNNIGlobalStatsCreated,
       "ocCNNIGlobalStatsOneWay": ocCNNIGlobalStatsOneWay,
       "ocCNNIGlobalStatsConnected": ocCNNIGlobalStatsConnected,
       "ocCNNIGlobalStatsBrokenLeaf": ocCNNIGlobalStatsBrokenLeaf,
       "ocCNNIGlobalStatsBrokenRoot": ocCNNIGlobalStatsBrokenRoot,
       "ocCNNIGlobalStatsRerouteWaiting": ocCNNIGlobalStatsRerouteWaiting,
       "ocCNNIAddrStats": ocCNNIAddrStats,
       "ocCNNIAddrStatsEntry": ocCNNIAddrStatsEntry,
       "ocCNNIAddrStatsToTotal": ocCNNIAddrStatsToTotal,
       "ocCNNIAddrStatsToCreated": ocCNNIAddrStatsToCreated,
       "ocCNNIAddrStatsToOneWay": ocCNNIAddrStatsToOneWay,
       "ocCNNIAddrStatsToConnected": ocCNNIAddrStatsToConnected,
       "ocCNNIAddrStatsToBrokenLeaf": ocCNNIAddrStatsToBrokenLeaf,
       "ocCNNIAddrStatsToBrokenRoot": ocCNNIAddrStatsToBrokenRoot,
       "ocCNNIAddrStatsToRerouteWaiting": ocCNNIAddrStatsToRerouteWaiting,
       "ocCNNIAddrStatsFromTotal": ocCNNIAddrStatsFromTotal,
       "ocCNNIAddrStatsFromCreated": ocCNNIAddrStatsFromCreated,
       "ocCNNIAddrStatsFromOneWay": ocCNNIAddrStatsFromOneWay,
       "ocCNNIAddrStatsFromConnected": ocCNNIAddrStatsFromConnected,
       "ocCNNIAddrStatsFromBrokenLeaf": ocCNNIAddrStatsFromBrokenLeaf,
       "ocCNNIAddrStatsFromBrokenRoot": ocCNNIAddrStatsFromBrokenRoot,
       "ocCNNIAddrStatsFromRerouteWaiting": ocCNNIAddrStatsFromRerouteWaiting,
       "ocCNNIAliasTable": ocCNNIAliasTable,
       "ocCNNIAliasTableEntry": ocCNNIAliasTableEntry,
       "ocCNNIAlias": ocCNNIAlias,
       "ocCNNIConnDB": ocCNNIConnDB,
       "ocCNNIFilterAssignID": ocCNNIFilterAssignID,
       "ocCNNIFilterTable": ocCNNIFilterTable,
       "ocCNNIFilterTableEntry": ocCNNIFilterTableEntry,
       "ocCNNIFilterID": ocCNNIFilterID,
       "ocCNNIFilterTypePres": ocCNNIFilterTypePres,
       "ocCNNIFilterTypeData": ocCNNIFilterTypeData,
       "ocCNNIFilterInPortPres": ocCNNIFilterInPortPres,
       "ocCNNIFilterInPortData": ocCNNIFilterInPortData,
       "ocCNNIFilterOutPortPres": ocCNNIFilterOutPortPres,
       "ocCNNIFilterOutPortData": ocCNNIFilterOutPortData,
       "ocCNNIFilterCgPtyPres": ocCNNIFilterCgPtyPres,
       "ocCNNIFilterCgPtyData": ocCNNIFilterCgPtyData,
       "ocCNNIFilterCdPtyPres": ocCNNIFilterCdPtyPres,
       "ocCNNIFilterCdPtyData": ocCNNIFilterCdPtyData,
       "ocCNNIFilterStatePres": ocCNNIFilterStatePres,
       "ocCNNIFilterStateData": ocCNNIFilterStateData,
       "ocCNNISessTable": ocCNNISessTable,
       "ocCNNISessTableEntry": ocCNNISessTableEntry,
       "ocCNNISessID": ocCNNISessID,
       "ocCNNISessDataType": ocCNNISessDataType,
       "ocCNNISessDataInPort": ocCNNISessDataInPort,
       "ocCNNISessDataOutPort": ocCNNISessDataOutPort,
       "ocCNNISessDataCgPty": ocCNNISessDataCgPty,
       "ocCNNISessDataCdPty": ocCNNISessDataCdPty,
       "ocCNNISessDataState": ocCNNISessDataState,
       "ocDsx3": ocDsx3,
       "ocDsx3MIBObjs": ocDsx3MIBObjs,
       "ocDsx3ConfigTable": ocDsx3ConfigTable,
       "ocDsx3ConfigEntry": ocDsx3ConfigEntry,
       "ocDsx3Xor55": ocDsx3Xor55,
       "ocDsx3Scrambling": ocDsx3Scrambling,
       "ocDsx3Delineation": ocDsx3Delineation,
       "ocDsx3HcsPassThru": ocDsx3HcsPassThru,
       "ocDsx3Ext8kRefClk": ocDsx3Ext8kRefClk,
       "ocDsx3ShortCable": ocDsx3ShortCable,
       "ocDsx3CntHcsCorrectedErrs": ocDsx3CntHcsCorrectedErrs,
       "ocDsx3SuniPdhTable": ocDsx3SuniPdhTable,
       "ocDsx3SuniPdhEntry": ocDsx3SuniPdhEntry,
       "ocDsx3SuniPmonLcv": ocDsx3SuniPmonLcv,
       "ocDsx3SuniPmonFerr": ocDsx3SuniPmonFerr,
       "ocDsx3SuniPmonExzs": ocDsx3SuniPmonExzs,
       "ocDsx3SuniPmonPeec": ocDsx3SuniPmonPeec,
       "ocDsx3SuniPmonPpec": ocDsx3SuniPmonPpec,
       "ocDsx3SuniPmonFebeErr": ocDsx3SuniPmonFebeErr,
       "ocDsx3SuniB1Bip8Err": ocDsx3SuniB1Bip8Err,
       "ocDsx3SuniCppmFrameErr": ocDsx3SuniCppmFrameErr,
       "ocDsx3SuniCppmFebeErr": ocDsx3SuniCppmFebeErr,
       "ocDsx3SuniCppmHcsErr": ocDsx3SuniCppmHcsErr,
       "ocDsx3SuniCppmRcvCells": ocDsx3SuniCppmRcvCells,
       "ocDsx3SuniCppmXmtCells": ocDsx3SuniCppmXmtCells,
       "ocDsx3SuniCppmIdleCells": ocDsx3SuniCppmIdleCells,
       "ocDsx3SuniCppmMegaRcvCells": ocDsx3SuniCppmMegaRcvCells,
       "ocDsx3SuniCppmMegaXmtCells": ocDsx3SuniCppmMegaXmtCells,
       "ocDsx3SuniCppmMegaIdleCells": ocDsx3SuniCppmMegaIdleCells}
)
