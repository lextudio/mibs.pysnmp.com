# SNMP MIB module (FCFABRIC-ELEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FCFABRIC-ELEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:24 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class MilliSeconds(Integer32):
    """Custom type MilliSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147383647),
    )





class MicroSeconds(Integer32):
    """Custom type MicroSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147383647),
    )





class FcNameId(OctetString):
    """Custom type FcNameId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class FabricName(FcNameId):
    """Custom type FabricName based on FcNameId"""




class FcPortName(FcNameId):
    """Custom type FcPortName based on FcNameId"""




class FcAddressId(OctetString):
    """Custom type FcAddressId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )





class FcRxDataFieldSize(Integer32):
    """Custom type FcRxDataFieldSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 2112),
    )





class FcBbCredit(Integer32):
    """Custom type FcBbCredit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )





class FcphVersion(Integer32):
    """Custom type FcphVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class FcStackedConnMode(Integer32):
    """Custom type FcStackedConnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lockedDown", 3),
          ("none", 1),
          ("transparent", 2))
    )





class FcCosCap(Integer32):
    """Custom type FcCosCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )





class Fc0BaudRate(Integer32):
    """Custom type Fc0BaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("double", 32),
          ("full", 16),
          ("half", 8),
          ("oneEighth", 2),
          ("other", 1),
          ("quadruple", 64),
          ("quarter", 4))
    )





class Fc0BaudRateCap(Integer32):
    """Custom type Fc0BaudRateCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )





class Fc0MediaCap(Integer32):
    """Custom type Fc0MediaCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class Fc0Medium(Integer32):
    """Custom type Fc0Medium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("lv", 256),
          ("m5", 4),
          ("m6", 8),
          ("mi", 32),
          ("sm", 2),
          ("stp", 64),
          ("tv", 16),
          ("tw", 128),
          ("unknown", 1))
    )





class Fc0TxType(Integer32):
    """Custom type Fc0TxType based on Integer32"""
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
        *(("electrical", 5),
          ("longWaveLED", 4),
          ("longWaveLaser", 2),
          ("shortWaveLaser", 3),
          ("shortWaveLaser-noOFC", 6),
          ("unknown", 1))
    )





class Fc0Distance(Integer32):
    """Custom type Fc0Distance based on Integer32"""
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
        *(("intermediate", 3),
          ("long", 2),
          ("short", 4),
          ("unknown", 1))
    )





class FcFeModuleCapacity(Integer32):
    """Custom type FcFeModuleCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )





class FcFeFxPortCapacity(Integer32):
    """Custom type FcFeFxPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )





class FcFeModuleIndex(Integer32):
    """Custom type FcFeModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )





class FcFeFxPortIndex(Integer32):
    """Custom type FcFeFxPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )





class FcFeNxPortIndex(Integer32):
    """Custom type FcFeNxPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )





class FcFxPortMode(Integer32):
    """Custom type FcFxPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fPort", 2),
          ("flPort", 3),
          ("unknown", 1))
    )





class FcBbCreditModel(Integer32):
    """Custom type FcBbCreditModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("regular", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FibreChannel_ObjectIdentity = ObjectIdentity
fibreChannel = _FibreChannel_ObjectIdentity(
    (1, 3, 6, 1, 3, 42)
)
_FcFabric_ObjectIdentity = ObjectIdentity
fcFabric = _FcFabric_ObjectIdentity(
    (1, 3, 6, 1, 3, 42, 2)
)
_FcFe_ObjectIdentity = ObjectIdentity
fcFe = _FcFe_ObjectIdentity(
    (1, 3, 6, 1, 3, 42, 2, 1)
)
_FcFeConfig_ObjectIdentity = ObjectIdentity
fcFeConfig = _FcFeConfig_ObjectIdentity(
    (1, 3, 6, 1, 3, 42, 2, 1, 1)
)
_FcFabricName_Type = FabricName
_FcFabricName_Object = MibScalar
fcFabricName = _FcFabricName_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 1),
    _FcFabricName_Type()
)
fcFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFabricName.setStatus("mandatory")
_FcElementName_Type = FcNameId
_FcElementName_Object = MibScalar
fcElementName = _FcElementName_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 2),
    _FcElementName_Type()
)
fcElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcElementName.setStatus("mandatory")
_FcFeModuleCapacity_Type = FcFeModuleCapacity
_FcFeModuleCapacity_Object = MibScalar
fcFeModuleCapacity = _FcFeModuleCapacity_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 3),
    _FcFeModuleCapacity_Type()
)
fcFeModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleCapacity.setStatus("mandatory")
_FcFeModuleTable_Object = MibTable
fcFeModuleTable = _FcFeModuleTable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fcFeModuleTable.setStatus("mandatory")
_FcFeModuleEntry_Object = MibTableRow
fcFeModuleEntry = _FcFeModuleEntry_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 4, 1)
)
fcFeModuleEntry.setIndexNames(
    (0, "FCFABRIC-ELEMENT-MIB", "fcFeModuleIndex"),
)
if mibBuilder.loadTexts:
    fcFeModuleEntry.setStatus("mandatory")
_FcFeModuleIndex_Type = FcFeModuleIndex
_FcFeModuleIndex_Object = MibTableColumn
fcFeModuleIndex = _FcFeModuleIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 4, 1, 1),
    _FcFeModuleIndex_Type()
)
fcFeModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleIndex.setStatus("mandatory")
_FcFeModuleDescr_Type = DisplayString
_FcFeModuleDescr_Object = MibTableColumn
fcFeModuleDescr = _FcFeModuleDescr_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 4, 1, 2),
    _FcFeModuleDescr_Type()
)
fcFeModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleDescr.setStatus("mandatory")
_FcFeModuleObjectID_Type = ObjectIdentifier
_FcFeModuleObjectID_Object = MibTableColumn
fcFeModuleObjectID = _FcFeModuleObjectID_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 4, 1, 3),
    _FcFeModuleObjectID_Type()
)
fcFeModuleObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleObjectID.setStatus("mandatory")


class _FcFeModuleOperStatus_Type(Integer32):
    """Custom type fcFeModuleOperStatus based on Integer32"""
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
        *(("faulty", 4),
          ("offline", 2),
          ("online", 1),
          ("testing", 3))
    )


_FcFeModuleOperStatus_Type.__name__ = "Integer32"
_FcFeModuleOperStatus_Object = MibTableColumn
fcFeModuleOperStatus = _FcFeModuleOperStatus_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 4, 1, 4),
    _FcFeModuleOperStatus_Type()
)
fcFeModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleOperStatus.setStatus("mandatory")
_FcFeModuleLastChange_Type = TimeTicks
_FcFeModuleLastChange_Object = MibTableColumn
fcFeModuleLastChange = _FcFeModuleLastChange_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 4, 1, 5),
    _FcFeModuleLastChange_Type()
)
fcFeModuleLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleLastChange.setStatus("mandatory")
_FcFeModuleFxPortCapacity_Type = FcFeFxPortCapacity
_FcFeModuleFxPortCapacity_Object = MibTableColumn
fcFeModuleFxPortCapacity = _FcFeModuleFxPortCapacity_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 4, 1, 6),
    _FcFeModuleFxPortCapacity_Type()
)
fcFeModuleFxPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleFxPortCapacity.setStatus("mandatory")
_FcFeModuleName_Type = FcNameId
_FcFeModuleName_Object = MibTableColumn
fcFeModuleName = _FcFeModuleName_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 4, 1, 7),
    _FcFeModuleName_Type()
)
fcFeModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleName.setStatus("mandatory")
_FcFxConfTable_Object = MibTable
fcFxConfTable = _FcFxConfTable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fcFxConfTable.setStatus("mandatory")
_FcFxConfEntry_Object = MibTableRow
fcFxConfEntry = _FcFxConfEntry_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1)
)
fcFxConfEntry.setIndexNames(
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxConfModuleIndex"),
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxConfFxPortIndex"),
)
if mibBuilder.loadTexts:
    fcFxConfEntry.setStatus("mandatory")
_FcFxConfModuleIndex_Type = FcFeModuleIndex
_FcFxConfModuleIndex_Object = MibTableColumn
fcFxConfModuleIndex = _FcFxConfModuleIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 1),
    _FcFxConfModuleIndex_Type()
)
fcFxConfModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxConfModuleIndex.setStatus("mandatory")
_FcFxConfFxPortIndex_Type = FcFeFxPortIndex
_FcFxConfFxPortIndex_Object = MibTableColumn
fcFxConfFxPortIndex = _FcFxConfFxPortIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 2),
    _FcFxConfFxPortIndex_Type()
)
fcFxConfFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxConfFxPortIndex.setStatus("mandatory")
_FcFxPortName_Type = FcPortName
_FcFxPortName_Object = MibTableColumn
fcFxPortName = _FcFxPortName_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 3),
    _FcFxPortName_Type()
)
fcFxPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortName.setStatus("mandatory")
_FcFxPortFcphVersionHigh_Type = FcphVersion
_FcFxPortFcphVersionHigh_Object = MibTableColumn
fcFxPortFcphVersionHigh = _FcFxPortFcphVersionHigh_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 4),
    _FcFxPortFcphVersionHigh_Type()
)
fcFxPortFcphVersionHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortFcphVersionHigh.setStatus("mandatory")
_FcFxPortFcphVersionLow_Type = FcphVersion
_FcFxPortFcphVersionLow_Object = MibTableColumn
fcFxPortFcphVersionLow = _FcFxPortFcphVersionLow_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 5),
    _FcFxPortFcphVersionLow_Type()
)
fcFxPortFcphVersionLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortFcphVersionLow.setStatus("mandatory")
_FcFxPortBbCredit_Type = FcBbCredit
_FcFxPortBbCredit_Object = MibTableColumn
fcFxPortBbCredit = _FcFxPortBbCredit_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 6),
    _FcFxPortBbCredit_Type()
)
fcFxPortBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortBbCredit.setStatus("mandatory")
_FcFxPortRxBufSize_Type = FcRxDataFieldSize
_FcFxPortRxBufSize_Object = MibTableColumn
fcFxPortRxBufSize = _FcFxPortRxBufSize_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 7),
    _FcFxPortRxBufSize_Type()
)
fcFxPortRxBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortRxBufSize.setStatus("mandatory")
_FcFxPortRatov_Type = MilliSeconds
_FcFxPortRatov_Object = MibTableColumn
fcFxPortRatov = _FcFxPortRatov_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 8),
    _FcFxPortRatov_Type()
)
fcFxPortRatov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortRatov.setStatus("mandatory")
_FcFxPortEdtov_Type = MilliSeconds
_FcFxPortEdtov_Object = MibTableColumn
fcFxPortEdtov = _FcFxPortEdtov_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 9),
    _FcFxPortEdtov_Type()
)
fcFxPortEdtov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortEdtov.setStatus("mandatory")
_FcFxPortCosSupported_Type = FcCosCap
_FcFxPortCosSupported_Object = MibTableColumn
fcFxPortCosSupported = _FcFxPortCosSupported_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 10),
    _FcFxPortCosSupported_Type()
)
fcFxPortCosSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCosSupported.setStatus("mandatory")


class _FcFxPortIntermixSupported_Type(Integer32):
    """Custom type fcFxPortIntermixSupported based on Integer32"""
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


_FcFxPortIntermixSupported_Type.__name__ = "Integer32"
_FcFxPortIntermixSupported_Object = MibTableColumn
fcFxPortIntermixSupported = _FcFxPortIntermixSupported_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 11),
    _FcFxPortIntermixSupported_Type()
)
fcFxPortIntermixSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortIntermixSupported.setStatus("mandatory")
_FcFxPortStackedConnMode_Type = FcStackedConnMode
_FcFxPortStackedConnMode_Object = MibTableColumn
fcFxPortStackedConnMode = _FcFxPortStackedConnMode_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 12),
    _FcFxPortStackedConnMode_Type()
)
fcFxPortStackedConnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortStackedConnMode.setStatus("mandatory")


class _FcFxPortClass2SeqDeliv_Type(Integer32):
    """Custom type fcFxPortClass2SeqDeliv based on Integer32"""
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


_FcFxPortClass2SeqDeliv_Type.__name__ = "Integer32"
_FcFxPortClass2SeqDeliv_Object = MibTableColumn
fcFxPortClass2SeqDeliv = _FcFxPortClass2SeqDeliv_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 13),
    _FcFxPortClass2SeqDeliv_Type()
)
fcFxPortClass2SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortClass2SeqDeliv.setStatus("mandatory")


class _FcFxPortClass3SeqDeliv_Type(Integer32):
    """Custom type fcFxPortClass3SeqDeliv based on Integer32"""
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


_FcFxPortClass3SeqDeliv_Type.__name__ = "Integer32"
_FcFxPortClass3SeqDeliv_Object = MibTableColumn
fcFxPortClass3SeqDeliv = _FcFxPortClass3SeqDeliv_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 14),
    _FcFxPortClass3SeqDeliv_Type()
)
fcFxPortClass3SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortClass3SeqDeliv.setStatus("mandatory")
_FcFxPortHoldTime_Type = MicroSeconds
_FcFxPortHoldTime_Object = MibTableColumn
fcFxPortHoldTime = _FcFxPortHoldTime_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 15),
    _FcFxPortHoldTime_Type()
)
fcFxPortHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortHoldTime.setStatus("mandatory")
_FcFxPortBaudRate_Type = Fc0BaudRate
_FcFxPortBaudRate_Object = MibTableColumn
fcFxPortBaudRate = _FcFxPortBaudRate_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 16),
    _FcFxPortBaudRate_Type()
)
fcFxPortBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortBaudRate.setStatus("deprecated")
_FcFxPortMedium_Type = Fc0Medium
_FcFxPortMedium_Object = MibTableColumn
fcFxPortMedium = _FcFxPortMedium_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 17),
    _FcFxPortMedium_Type()
)
fcFxPortMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortMedium.setStatus("deprecated")
_FcFxPortTxType_Type = Fc0TxType
_FcFxPortTxType_Object = MibTableColumn
fcFxPortTxType = _FcFxPortTxType_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 18),
    _FcFxPortTxType_Type()
)
fcFxPortTxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortTxType.setStatus("deprecated")
_FcFxPortDistance_Type = Fc0Distance
_FcFxPortDistance_Object = MibTableColumn
fcFxPortDistance = _FcFxPortDistance_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 1, 5, 1, 19),
    _FcFxPortDistance_Type()
)
fcFxPortDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortDistance.setStatus("deprecated")
_FcFeOp_ObjectIdentity = ObjectIdentity
fcFeOp = _FcFeOp_ObjectIdentity(
    (1, 3, 6, 1, 3, 42, 2, 1, 2)
)
_FcFxPortOperTable_Object = MibTable
fcFxPortOperTable = _FcFxPortOperTable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fcFxPortOperTable.setStatus("mandatory")
_FcFxPortOperEntry_Object = MibTableRow
fcFxPortOperEntry = _FcFxPortOperEntry_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 1, 1)
)
fcFxPortOperEntry.setIndexNames(
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortOperModuleIndex"),
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortOperFxPortIndex"),
)
if mibBuilder.loadTexts:
    fcFxPortOperEntry.setStatus("mandatory")
_FcFxPortOperModuleIndex_Type = FcFeModuleIndex
_FcFxPortOperModuleIndex_Object = MibTableColumn
fcFxPortOperModuleIndex = _FcFxPortOperModuleIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 1, 1, 1),
    _FcFxPortOperModuleIndex_Type()
)
fcFxPortOperModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortOperModuleIndex.setStatus("mandatory")
_FcFxPortOperFxPortIndex_Type = FcFeFxPortIndex
_FcFxPortOperFxPortIndex_Object = MibTableColumn
fcFxPortOperFxPortIndex = _FcFxPortOperFxPortIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 1, 1, 2),
    _FcFxPortOperFxPortIndex_Type()
)
fcFxPortOperFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortOperFxPortIndex.setStatus("mandatory")
_FcFxPortID_Type = FcAddressId
_FcFxPortID_Object = MibTableColumn
fcFxPortID = _FcFxPortID_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 1, 1, 3),
    _FcFxPortID_Type()
)
fcFxPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortID.setStatus("mandatory")
_FcFPortAttachedPortName_Type = FcPortName
_FcFPortAttachedPortName_Object = MibTableColumn
fcFPortAttachedPortName = _FcFPortAttachedPortName_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 1, 1, 4),
    _FcFPortAttachedPortName_Type()
)
fcFPortAttachedPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFPortAttachedPortName.setStatus("deprecated")
_FcFPortConnectedPort_Type = FcAddressId
_FcFPortConnectedPort_Object = MibTableColumn
fcFPortConnectedPort = _FcFPortConnectedPort_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 1, 1, 5),
    _FcFPortConnectedPort_Type()
)
fcFPortConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFPortConnectedPort.setStatus("deprecated")
_FcFxPortBbCreditAvailable_Type = Gauge32
_FcFxPortBbCreditAvailable_Object = MibTableColumn
fcFxPortBbCreditAvailable = _FcFxPortBbCreditAvailable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 1, 1, 6),
    _FcFxPortBbCreditAvailable_Type()
)
fcFxPortBbCreditAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortBbCreditAvailable.setStatus("mandatory")
_FcFxPortOperMode_Type = FcFxPortMode
_FcFxPortOperMode_Object = MibTableColumn
fcFxPortOperMode = _FcFxPortOperMode_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 1, 1, 7),
    _FcFxPortOperMode_Type()
)
fcFxPortOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortOperMode.setStatus("mandatory")
_FcFxPortAdminMode_Type = FcFxPortMode
_FcFxPortAdminMode_Object = MibTableColumn
fcFxPortAdminMode = _FcFxPortAdminMode_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 1, 1, 8),
    _FcFxPortAdminMode_Type()
)
fcFxPortAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortAdminMode.setStatus("mandatory")
_FcFxPortPhysTable_Object = MibTable
fcFxPortPhysTable = _FcFxPortPhysTable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fcFxPortPhysTable.setStatus("mandatory")
_FcFxPortPhysEntry_Object = MibTableRow
fcFxPortPhysEntry = _FcFxPortPhysEntry_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 3, 1)
)
fcFxPortPhysEntry.setIndexNames(
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortPhysModuleIndex"),
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortPhysFxPortIndex"),
)
if mibBuilder.loadTexts:
    fcFxPortPhysEntry.setStatus("mandatory")
_FcFxPortPhysModuleIndex_Type = FcFeModuleIndex
_FcFxPortPhysModuleIndex_Object = MibTableColumn
fcFxPortPhysModuleIndex = _FcFxPortPhysModuleIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 3, 1, 1),
    _FcFxPortPhysModuleIndex_Type()
)
fcFxPortPhysModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortPhysModuleIndex.setStatus("mandatory")
_FcFxPortPhysFxPortIndex_Type = FcFeFxPortIndex
_FcFxPortPhysFxPortIndex_Object = MibTableColumn
fcFxPortPhysFxPortIndex = _FcFxPortPhysFxPortIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 3, 1, 2),
    _FcFxPortPhysFxPortIndex_Type()
)
fcFxPortPhysFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortPhysFxPortIndex.setStatus("mandatory")


class _FcFxPortPhysAdminStatus_Type(Integer32):
    """Custom type fcFxPortPhysAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("testing", 3))
    )


_FcFxPortPhysAdminStatus_Type.__name__ = "Integer32"
_FcFxPortPhysAdminStatus_Object = MibTableColumn
fcFxPortPhysAdminStatus = _FcFxPortPhysAdminStatus_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 3, 1, 3),
    _FcFxPortPhysAdminStatus_Type()
)
fcFxPortPhysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcFxPortPhysAdminStatus.setStatus("mandatory")


class _FcFxPortPhysOperStatus_Type(Integer32):
    """Custom type fcFxPortPhysOperStatus based on Integer32"""
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
        *(("link-failure", 4),
          ("offline", 2),
          ("online", 1),
          ("testing", 3))
    )


_FcFxPortPhysOperStatus_Type.__name__ = "Integer32"
_FcFxPortPhysOperStatus_Object = MibTableColumn
fcFxPortPhysOperStatus = _FcFxPortPhysOperStatus_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 3, 1, 4),
    _FcFxPortPhysOperStatus_Type()
)
fcFxPortPhysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortPhysOperStatus.setStatus("mandatory")
_FcFxPortPhysLastChange_Type = TimeTicks
_FcFxPortPhysLastChange_Object = MibTableColumn
fcFxPortPhysLastChange = _FcFxPortPhysLastChange_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 3, 1, 5),
    _FcFxPortPhysLastChange_Type()
)
fcFxPortPhysLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortPhysLastChange.setStatus("mandatory")
_FcFxPortPhysRttov_Type = MilliSeconds
_FcFxPortPhysRttov_Object = MibTableColumn
fcFxPortPhysRttov = _FcFxPortPhysRttov_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 3, 1, 6),
    _FcFxPortPhysRttov_Type()
)
fcFxPortPhysRttov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortPhysRttov.setStatus("mandatory")
_FcFxlogiTable_Object = MibTable
fcFxlogiTable = _FcFxlogiTable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fcFxlogiTable.setStatus("mandatory")
_FcFxlogiEntry_Object = MibTableRow
fcFxlogiEntry = _FcFxlogiEntry_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1)
)
fcFxlogiEntry.setIndexNames(
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxlogiModuleIndex"),
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxlogiFxPortIndex"),
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxlogiNxPortIndex"),
)
if mibBuilder.loadTexts:
    fcFxlogiEntry.setStatus("mandatory")
_FcFxlogiModuleIndex_Type = FcFeModuleIndex
_FcFxlogiModuleIndex_Object = MibTableColumn
fcFxlogiModuleIndex = _FcFxlogiModuleIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 1),
    _FcFxlogiModuleIndex_Type()
)
fcFxlogiModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxlogiModuleIndex.setStatus("mandatory")
_FcFxlogiFxPortIndex_Type = FcFeFxPortIndex
_FcFxlogiFxPortIndex_Object = MibTableColumn
fcFxlogiFxPortIndex = _FcFxlogiFxPortIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 2),
    _FcFxlogiFxPortIndex_Type()
)
fcFxlogiFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxlogiFxPortIndex.setStatus("mandatory")
_FcFxlogiNxPortIndex_Type = FcFeNxPortIndex
_FcFxlogiNxPortIndex_Object = MibTableColumn
fcFxlogiNxPortIndex = _FcFxlogiNxPortIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 3),
    _FcFxlogiNxPortIndex_Type()
)
fcFxlogiNxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxlogiNxPortIndex.setStatus("mandatory")
_FcFxPortFcphVersionAgreed_Type = FcphVersion
_FcFxPortFcphVersionAgreed_Object = MibTableColumn
fcFxPortFcphVersionAgreed = _FcFxPortFcphVersionAgreed_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 4),
    _FcFxPortFcphVersionAgreed_Type()
)
fcFxPortFcphVersionAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortFcphVersionAgreed.setStatus("mandatory")
_FcFxPortNxPortBbCredit_Type = FcBbCredit
_FcFxPortNxPortBbCredit_Object = MibTableColumn
fcFxPortNxPortBbCredit = _FcFxPortNxPortBbCredit_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 5),
    _FcFxPortNxPortBbCredit_Type()
)
fcFxPortNxPortBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortNxPortBbCredit.setStatus("mandatory")
_FcFxPortNxPortRxDataFieldSize_Type = FcRxDataFieldSize
_FcFxPortNxPortRxDataFieldSize_Object = MibTableColumn
fcFxPortNxPortRxDataFieldSize = _FcFxPortNxPortRxDataFieldSize_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 6),
    _FcFxPortNxPortRxDataFieldSize_Type()
)
fcFxPortNxPortRxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortNxPortRxDataFieldSize.setStatus("mandatory")
_FcFxPortCosSuppAgreed_Type = FcCosCap
_FcFxPortCosSuppAgreed_Object = MibTableColumn
fcFxPortCosSuppAgreed = _FcFxPortCosSuppAgreed_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 7),
    _FcFxPortCosSuppAgreed_Type()
)
fcFxPortCosSuppAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCosSuppAgreed.setStatus("mandatory")


class _FcFxPortIntermixSuppAgreed_Type(Integer32):
    """Custom type fcFxPortIntermixSuppAgreed based on Integer32"""
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


_FcFxPortIntermixSuppAgreed_Type.__name__ = "Integer32"
_FcFxPortIntermixSuppAgreed_Object = MibTableColumn
fcFxPortIntermixSuppAgreed = _FcFxPortIntermixSuppAgreed_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 8),
    _FcFxPortIntermixSuppAgreed_Type()
)
fcFxPortIntermixSuppAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortIntermixSuppAgreed.setStatus("mandatory")
_FcFxPortStackedConnModeAgreed_Type = FcStackedConnMode
_FcFxPortStackedConnModeAgreed_Object = MibTableColumn
fcFxPortStackedConnModeAgreed = _FcFxPortStackedConnModeAgreed_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 9),
    _FcFxPortStackedConnModeAgreed_Type()
)
fcFxPortStackedConnModeAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortStackedConnModeAgreed.setStatus("mandatory")


class _FcFxPortClass2SeqDelivAgreed_Type(Integer32):
    """Custom type fcFxPortClass2SeqDelivAgreed based on Integer32"""
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


_FcFxPortClass2SeqDelivAgreed_Type.__name__ = "Integer32"
_FcFxPortClass2SeqDelivAgreed_Object = MibTableColumn
fcFxPortClass2SeqDelivAgreed = _FcFxPortClass2SeqDelivAgreed_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 10),
    _FcFxPortClass2SeqDelivAgreed_Type()
)
fcFxPortClass2SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortClass2SeqDelivAgreed.setStatus("mandatory")


class _FcFxPortClass3SeqDelivAgreed_Type(Integer32):
    """Custom type fcFxPortClass3SeqDelivAgreed based on Integer32"""
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


_FcFxPortClass3SeqDelivAgreed_Type.__name__ = "Integer32"
_FcFxPortClass3SeqDelivAgreed_Object = MibTableColumn
fcFxPortClass3SeqDelivAgreed = _FcFxPortClass3SeqDelivAgreed_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 11),
    _FcFxPortClass3SeqDelivAgreed_Type()
)
fcFxPortClass3SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortClass3SeqDelivAgreed.setStatus("mandatory")
_FcFxPortNxPortName_Type = FcPortName
_FcFxPortNxPortName_Object = MibTableColumn
fcFxPortNxPortName = _FcFxPortNxPortName_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 12),
    _FcFxPortNxPortName_Type()
)
fcFxPortNxPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortNxPortName.setStatus("mandatory")
_FcFxPortConnectedNxPort_Type = FcAddressId
_FcFxPortConnectedNxPort_Object = MibTableColumn
fcFxPortConnectedNxPort = _FcFxPortConnectedNxPort_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 13),
    _FcFxPortConnectedNxPort_Type()
)
fcFxPortConnectedNxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortConnectedNxPort.setStatus("mandatory")
_FcFxPortBbCreditModel_Type = FcBbCreditModel
_FcFxPortBbCreditModel_Object = MibTableColumn
fcFxPortBbCreditModel = _FcFxPortBbCreditModel_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 2, 4, 1, 14),
    _FcFxPortBbCreditModel_Type()
)
fcFxPortBbCreditModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortBbCreditModel.setStatus("mandatory")
_FcFeError_ObjectIdentity = ObjectIdentity
fcFeError = _FcFeError_ObjectIdentity(
    (1, 3, 6, 1, 3, 42, 2, 1, 3)
)
_FcFxPortErrorTable_Object = MibTable
fcFxPortErrorTable = _FcFxPortErrorTable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fcFxPortErrorTable.setStatus("mandatory")
_FcFxPortErrorEntry_Object = MibTableRow
fcFxPortErrorEntry = _FcFxPortErrorEntry_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1)
)
fcFxPortErrorEntry.setIndexNames(
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortErrorModuleIndex"),
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortErrorFxPortIndex"),
)
if mibBuilder.loadTexts:
    fcFxPortErrorEntry.setStatus("mandatory")
_FcFxPortErrorModuleIndex_Type = FcFeModuleIndex
_FcFxPortErrorModuleIndex_Object = MibTableColumn
fcFxPortErrorModuleIndex = _FcFxPortErrorModuleIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 1),
    _FcFxPortErrorModuleIndex_Type()
)
fcFxPortErrorModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortErrorModuleIndex.setStatus("mandatory")
_FcFxPortErrorFxPortIndex_Type = FcFeFxPortIndex
_FcFxPortErrorFxPortIndex_Object = MibTableColumn
fcFxPortErrorFxPortIndex = _FcFxPortErrorFxPortIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 2),
    _FcFxPortErrorFxPortIndex_Type()
)
fcFxPortErrorFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortErrorFxPortIndex.setStatus("mandatory")
_FcFxPortLinkFailures_Type = Counter32
_FcFxPortLinkFailures_Object = MibTableColumn
fcFxPortLinkFailures = _FcFxPortLinkFailures_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 3),
    _FcFxPortLinkFailures_Type()
)
fcFxPortLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortLinkFailures.setStatus("mandatory")
_FcFxPortSyncLosses_Type = Counter32
_FcFxPortSyncLosses_Object = MibTableColumn
fcFxPortSyncLosses = _FcFxPortSyncLosses_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 4),
    _FcFxPortSyncLosses_Type()
)
fcFxPortSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortSyncLosses.setStatus("mandatory")
_FcFxPortSigLosses_Type = Counter32
_FcFxPortSigLosses_Object = MibTableColumn
fcFxPortSigLosses = _FcFxPortSigLosses_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 5),
    _FcFxPortSigLosses_Type()
)
fcFxPortSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortSigLosses.setStatus("mandatory")
_FcFxPortPrimSeqProtoErrors_Type = Counter32
_FcFxPortPrimSeqProtoErrors_Object = MibTableColumn
fcFxPortPrimSeqProtoErrors = _FcFxPortPrimSeqProtoErrors_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 6),
    _FcFxPortPrimSeqProtoErrors_Type()
)
fcFxPortPrimSeqProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortPrimSeqProtoErrors.setStatus("mandatory")
_FcFxPortInvalidTxWords_Type = Counter32
_FcFxPortInvalidTxWords_Object = MibTableColumn
fcFxPortInvalidTxWords = _FcFxPortInvalidTxWords_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 7),
    _FcFxPortInvalidTxWords_Type()
)
fcFxPortInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortInvalidTxWords.setStatus("mandatory")
_FcFxPortInvalidCrcs_Type = Counter32
_FcFxPortInvalidCrcs_Object = MibTableColumn
fcFxPortInvalidCrcs = _FcFxPortInvalidCrcs_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 8),
    _FcFxPortInvalidCrcs_Type()
)
fcFxPortInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortInvalidCrcs.setStatus("mandatory")
_FcFxPortDelimiterErrors_Type = Counter32
_FcFxPortDelimiterErrors_Object = MibTableColumn
fcFxPortDelimiterErrors = _FcFxPortDelimiterErrors_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 9),
    _FcFxPortDelimiterErrors_Type()
)
fcFxPortDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortDelimiterErrors.setStatus("mandatory")
_FcFxPortAddressIdErrors_Type = Counter32
_FcFxPortAddressIdErrors_Object = MibTableColumn
fcFxPortAddressIdErrors = _FcFxPortAddressIdErrors_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 10),
    _FcFxPortAddressIdErrors_Type()
)
fcFxPortAddressIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortAddressIdErrors.setStatus("mandatory")
_FcFxPortLinkResetIns_Type = Counter32
_FcFxPortLinkResetIns_Object = MibTableColumn
fcFxPortLinkResetIns = _FcFxPortLinkResetIns_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 11),
    _FcFxPortLinkResetIns_Type()
)
fcFxPortLinkResetIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortLinkResetIns.setStatus("mandatory")
_FcFxPortLinkResetOuts_Type = Counter32
_FcFxPortLinkResetOuts_Object = MibTableColumn
fcFxPortLinkResetOuts = _FcFxPortLinkResetOuts_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 12),
    _FcFxPortLinkResetOuts_Type()
)
fcFxPortLinkResetOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortLinkResetOuts.setStatus("mandatory")
_FcFxPortOlsIns_Type = Counter32
_FcFxPortOlsIns_Object = MibTableColumn
fcFxPortOlsIns = _FcFxPortOlsIns_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 13),
    _FcFxPortOlsIns_Type()
)
fcFxPortOlsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortOlsIns.setStatus("mandatory")
_FcFxPortOlsOuts_Type = Counter32
_FcFxPortOlsOuts_Object = MibTableColumn
fcFxPortOlsOuts = _FcFxPortOlsOuts_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 3, 1, 1, 14),
    _FcFxPortOlsOuts_Type()
)
fcFxPortOlsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortOlsOuts.setStatus("mandatory")
_FcFeAcct_ObjectIdentity = ObjectIdentity
fcFeAcct = _FcFeAcct_ObjectIdentity(
    (1, 3, 6, 1, 3, 42, 2, 1, 4)
)
_FcFxPortC1AcctTable_Object = MibTable
fcFxPortC1AcctTable = _FcFxPortC1AcctTable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fcFxPortC1AcctTable.setStatus("mandatory")
_FcFxPortC1AcctEntry_Object = MibTableRow
fcFxPortC1AcctEntry = _FcFxPortC1AcctEntry_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1)
)
fcFxPortC1AcctEntry.setIndexNames(
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortC1AcctModuleIndex"),
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortC1AcctFxPortIndex"),
)
if mibBuilder.loadTexts:
    fcFxPortC1AcctEntry.setStatus("mandatory")
_FcFxPortC1AcctModuleIndex_Type = FcFeModuleIndex
_FcFxPortC1AcctModuleIndex_Object = MibTableColumn
fcFxPortC1AcctModuleIndex = _FcFxPortC1AcctModuleIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 1),
    _FcFxPortC1AcctModuleIndex_Type()
)
fcFxPortC1AcctModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1AcctModuleIndex.setStatus("mandatory")
_FcFxPortC1AcctFxPortIndex_Type = FcFeFxPortIndex
_FcFxPortC1AcctFxPortIndex_Object = MibTableColumn
fcFxPortC1AcctFxPortIndex = _FcFxPortC1AcctFxPortIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 2),
    _FcFxPortC1AcctFxPortIndex_Type()
)
fcFxPortC1AcctFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1AcctFxPortIndex.setStatus("mandatory")
_FcFxPortC1InConnections_Type = Counter32
_FcFxPortC1InConnections_Object = MibTableColumn
fcFxPortC1InConnections = _FcFxPortC1InConnections_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 3),
    _FcFxPortC1InConnections_Type()
)
fcFxPortC1InConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1InConnections.setStatus("mandatory")
_FcFxPortC1OutConnections_Type = Counter32
_FcFxPortC1OutConnections_Object = MibTableColumn
fcFxPortC1OutConnections = _FcFxPortC1OutConnections_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 4),
    _FcFxPortC1OutConnections_Type()
)
fcFxPortC1OutConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1OutConnections.setStatus("mandatory")
_FcFxPortC1FbsyFrames_Type = Counter32
_FcFxPortC1FbsyFrames_Object = MibTableColumn
fcFxPortC1FbsyFrames = _FcFxPortC1FbsyFrames_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 5),
    _FcFxPortC1FbsyFrames_Type()
)
fcFxPortC1FbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1FbsyFrames.setStatus("mandatory")
_FcFxPortC1FrjtFrames_Type = Counter32
_FcFxPortC1FrjtFrames_Object = MibTableColumn
fcFxPortC1FrjtFrames = _FcFxPortC1FrjtFrames_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 6),
    _FcFxPortC1FrjtFrames_Type()
)
fcFxPortC1FrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1FrjtFrames.setStatus("mandatory")
_FcFxPortC1ConnTime_Type = Counter32
_FcFxPortC1ConnTime_Object = MibTableColumn
fcFxPortC1ConnTime = _FcFxPortC1ConnTime_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 7),
    _FcFxPortC1ConnTime_Type()
)
fcFxPortC1ConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1ConnTime.setStatus("mandatory")
_FcFxPortC1InFrames_Type = Counter32
_FcFxPortC1InFrames_Object = MibTableColumn
fcFxPortC1InFrames = _FcFxPortC1InFrames_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 8),
    _FcFxPortC1InFrames_Type()
)
fcFxPortC1InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1InFrames.setStatus("mandatory")
_FcFxPortC1OutFrames_Type = Counter32
_FcFxPortC1OutFrames_Object = MibTableColumn
fcFxPortC1OutFrames = _FcFxPortC1OutFrames_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 9),
    _FcFxPortC1OutFrames_Type()
)
fcFxPortC1OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1OutFrames.setStatus("mandatory")
_FcFxPortC1InOctets_Type = Counter32
_FcFxPortC1InOctets_Object = MibTableColumn
fcFxPortC1InOctets = _FcFxPortC1InOctets_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 10),
    _FcFxPortC1InOctets_Type()
)
fcFxPortC1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1InOctets.setStatus("mandatory")
_FcFxPortC1OutOctets_Type = Counter32
_FcFxPortC1OutOctets_Object = MibTableColumn
fcFxPortC1OutOctets = _FcFxPortC1OutOctets_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 11),
    _FcFxPortC1OutOctets_Type()
)
fcFxPortC1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1OutOctets.setStatus("mandatory")
_FcFxPortC1Discards_Type = Counter32
_FcFxPortC1Discards_Object = MibTableColumn
fcFxPortC1Discards = _FcFxPortC1Discards_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 1, 1, 12),
    _FcFxPortC1Discards_Type()
)
fcFxPortC1Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1Discards.setStatus("mandatory")
_FcFxPortC2AcctTable_Object = MibTable
fcFxPortC2AcctTable = _FcFxPortC2AcctTable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fcFxPortC2AcctTable.setStatus("mandatory")
_FcFxPortC2AcctEntry_Object = MibTableRow
fcFxPortC2AcctEntry = _FcFxPortC2AcctEntry_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2, 1)
)
fcFxPortC2AcctEntry.setIndexNames(
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortC2AcctModuleIndex"),
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortC2AcctFxPortIndex"),
)
if mibBuilder.loadTexts:
    fcFxPortC2AcctEntry.setStatus("mandatory")
_FcFxPortC2AcctModuleIndex_Type = FcFeModuleIndex
_FcFxPortC2AcctModuleIndex_Object = MibTableColumn
fcFxPortC2AcctModuleIndex = _FcFxPortC2AcctModuleIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2, 1, 1),
    _FcFxPortC2AcctModuleIndex_Type()
)
fcFxPortC2AcctModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2AcctModuleIndex.setStatus("mandatory")
_FcFxPortC2AcctFxPortIndex_Type = FcFeFxPortIndex
_FcFxPortC2AcctFxPortIndex_Object = MibTableColumn
fcFxPortC2AcctFxPortIndex = _FcFxPortC2AcctFxPortIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2, 1, 2),
    _FcFxPortC2AcctFxPortIndex_Type()
)
fcFxPortC2AcctFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2AcctFxPortIndex.setStatus("mandatory")
_FcFxPortC2InFrames_Type = Counter32
_FcFxPortC2InFrames_Object = MibTableColumn
fcFxPortC2InFrames = _FcFxPortC2InFrames_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2, 1, 3),
    _FcFxPortC2InFrames_Type()
)
fcFxPortC2InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2InFrames.setStatus("mandatory")
_FcFxPortC2OutFrames_Type = Counter32
_FcFxPortC2OutFrames_Object = MibTableColumn
fcFxPortC2OutFrames = _FcFxPortC2OutFrames_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2, 1, 4),
    _FcFxPortC2OutFrames_Type()
)
fcFxPortC2OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2OutFrames.setStatus("mandatory")
_FcFxPortC2InOctets_Type = Counter32
_FcFxPortC2InOctets_Object = MibTableColumn
fcFxPortC2InOctets = _FcFxPortC2InOctets_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2, 1, 5),
    _FcFxPortC2InOctets_Type()
)
fcFxPortC2InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2InOctets.setStatus("mandatory")
_FcFxPortC2OutOctets_Type = Counter32
_FcFxPortC2OutOctets_Object = MibTableColumn
fcFxPortC2OutOctets = _FcFxPortC2OutOctets_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2, 1, 6),
    _FcFxPortC2OutOctets_Type()
)
fcFxPortC2OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2OutOctets.setStatus("mandatory")
_FcFxPortC2Discards_Type = Counter32
_FcFxPortC2Discards_Object = MibTableColumn
fcFxPortC2Discards = _FcFxPortC2Discards_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2, 1, 7),
    _FcFxPortC2Discards_Type()
)
fcFxPortC2Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2Discards.setStatus("mandatory")
_FcFxPortC2FbsyFrames_Type = Counter32
_FcFxPortC2FbsyFrames_Object = MibTableColumn
fcFxPortC2FbsyFrames = _FcFxPortC2FbsyFrames_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2, 1, 8),
    _FcFxPortC2FbsyFrames_Type()
)
fcFxPortC2FbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2FbsyFrames.setStatus("mandatory")
_FcFxPortC2FrjtFrames_Type = Counter32
_FcFxPortC2FrjtFrames_Object = MibTableColumn
fcFxPortC2FrjtFrames = _FcFxPortC2FrjtFrames_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 2, 1, 9),
    _FcFxPortC2FrjtFrames_Type()
)
fcFxPortC2FrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2FrjtFrames.setStatus("mandatory")
_FcFxPortC3AcctTable_Object = MibTable
fcFxPortC3AcctTable = _FcFxPortC3AcctTable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    fcFxPortC3AcctTable.setStatus("mandatory")
_FcFxPortC3AcctEntry_Object = MibTableRow
fcFxPortC3AcctEntry = _FcFxPortC3AcctEntry_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 3, 1)
)
fcFxPortC3AcctEntry.setIndexNames(
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortC3AcctModuleIndex"),
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortC3AcctFxPortIndex"),
)
if mibBuilder.loadTexts:
    fcFxPortC3AcctEntry.setStatus("mandatory")
_FcFxPortC3AcctModuleIndex_Type = FcFeModuleIndex
_FcFxPortC3AcctModuleIndex_Object = MibTableColumn
fcFxPortC3AcctModuleIndex = _FcFxPortC3AcctModuleIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 3, 1, 1),
    _FcFxPortC3AcctModuleIndex_Type()
)
fcFxPortC3AcctModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3AcctModuleIndex.setStatus("mandatory")
_FcFxPortC3AcctFxPortIndex_Type = FcFeFxPortIndex
_FcFxPortC3AcctFxPortIndex_Object = MibTableColumn
fcFxPortC3AcctFxPortIndex = _FcFxPortC3AcctFxPortIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 3, 1, 2),
    _FcFxPortC3AcctFxPortIndex_Type()
)
fcFxPortC3AcctFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3AcctFxPortIndex.setStatus("mandatory")
_FcFxPortC3InFrames_Type = Counter32
_FcFxPortC3InFrames_Object = MibTableColumn
fcFxPortC3InFrames = _FcFxPortC3InFrames_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 3, 1, 3),
    _FcFxPortC3InFrames_Type()
)
fcFxPortC3InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3InFrames.setStatus("mandatory")
_FcFxPortC3OutFrames_Type = Counter32
_FcFxPortC3OutFrames_Object = MibTableColumn
fcFxPortC3OutFrames = _FcFxPortC3OutFrames_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 3, 1, 4),
    _FcFxPortC3OutFrames_Type()
)
fcFxPortC3OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3OutFrames.setStatus("mandatory")
_FcFxPortC3InOctets_Type = Counter32
_FcFxPortC3InOctets_Object = MibTableColumn
fcFxPortC3InOctets = _FcFxPortC3InOctets_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 3, 1, 5),
    _FcFxPortC3InOctets_Type()
)
fcFxPortC3InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3InOctets.setStatus("mandatory")
_FcFxPortC3OutOctets_Type = Counter32
_FcFxPortC3OutOctets_Object = MibTableColumn
fcFxPortC3OutOctets = _FcFxPortC3OutOctets_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 3, 1, 6),
    _FcFxPortC3OutOctets_Type()
)
fcFxPortC3OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3OutOctets.setStatus("mandatory")
_FcFxPortC3Discards_Type = Counter32
_FcFxPortC3Discards_Object = MibTableColumn
fcFxPortC3Discards = _FcFxPortC3Discards_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 4, 3, 1, 7),
    _FcFxPortC3Discards_Type()
)
fcFxPortC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3Discards.setStatus("mandatory")
_FcFeCap_ObjectIdentity = ObjectIdentity
fcFeCap = _FcFeCap_ObjectIdentity(
    (1, 3, 6, 1, 3, 42, 2, 1, 5)
)
_FcFxPortCapTable_Object = MibTable
fcFxPortCapTable = _FcFxPortCapTable_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fcFxPortCapTable.setStatus("mandatory")
_FcFxPortCapEntry_Object = MibTableRow
fcFxPortCapEntry = _FcFxPortCapEntry_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1)
)
fcFxPortCapEntry.setIndexNames(
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortCapModuleIndex"),
    (0, "FCFABRIC-ELEMENT-MIB", "fcFxPortCapFxPortIndex"),
)
if mibBuilder.loadTexts:
    fcFxPortCapEntry.setStatus("mandatory")
_FcFxPortCapModuleIndex_Type = FcFeModuleIndex
_FcFxPortCapModuleIndex_Object = MibTableColumn
fcFxPortCapModuleIndex = _FcFxPortCapModuleIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 1),
    _FcFxPortCapModuleIndex_Type()
)
fcFxPortCapModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapModuleIndex.setStatus("mandatory")
_FcFxPortCapFxPortIndex_Type = FcFeFxPortIndex
_FcFxPortCapFxPortIndex_Object = MibTableColumn
fcFxPortCapFxPortIndex = _FcFxPortCapFxPortIndex_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 2),
    _FcFxPortCapFxPortIndex_Type()
)
fcFxPortCapFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapFxPortIndex.setStatus("mandatory")
_FcFxPortCapFcphVersionHigh_Type = FcphVersion
_FcFxPortCapFcphVersionHigh_Object = MibTableColumn
fcFxPortCapFcphVersionHigh = _FcFxPortCapFcphVersionHigh_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 3),
    _FcFxPortCapFcphVersionHigh_Type()
)
fcFxPortCapFcphVersionHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapFcphVersionHigh.setStatus("mandatory")
_FcFxPortCapFcphVersionLow_Type = FcphVersion
_FcFxPortCapFcphVersionLow_Object = MibTableColumn
fcFxPortCapFcphVersionLow = _FcFxPortCapFcphVersionLow_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 4),
    _FcFxPortCapFcphVersionLow_Type()
)
fcFxPortCapFcphVersionLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapFcphVersionLow.setStatus("mandatory")
_FcFxPortCapBbCreditMax_Type = FcBbCredit
_FcFxPortCapBbCreditMax_Object = MibTableColumn
fcFxPortCapBbCreditMax = _FcFxPortCapBbCreditMax_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 5),
    _FcFxPortCapBbCreditMax_Type()
)
fcFxPortCapBbCreditMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapBbCreditMax.setStatus("mandatory")
_FcFxPortCapBbCreditMin_Type = FcBbCredit
_FcFxPortCapBbCreditMin_Object = MibTableColumn
fcFxPortCapBbCreditMin = _FcFxPortCapBbCreditMin_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 6),
    _FcFxPortCapBbCreditMin_Type()
)
fcFxPortCapBbCreditMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapBbCreditMin.setStatus("mandatory")
_FcFxPortCapRxDataFieldSizeMax_Type = FcRxDataFieldSize
_FcFxPortCapRxDataFieldSizeMax_Object = MibTableColumn
fcFxPortCapRxDataFieldSizeMax = _FcFxPortCapRxDataFieldSizeMax_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 7),
    _FcFxPortCapRxDataFieldSizeMax_Type()
)
fcFxPortCapRxDataFieldSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapRxDataFieldSizeMax.setStatus("mandatory")
_FcFxPortCapRxDataFieldSizeMin_Type = FcRxDataFieldSize
_FcFxPortCapRxDataFieldSizeMin_Object = MibTableColumn
fcFxPortCapRxDataFieldSizeMin = _FcFxPortCapRxDataFieldSizeMin_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 8),
    _FcFxPortCapRxDataFieldSizeMin_Type()
)
fcFxPortCapRxDataFieldSizeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapRxDataFieldSizeMin.setStatus("mandatory")
_FcFxPortCapCos_Type = FcCosCap
_FcFxPortCapCos_Object = MibTableColumn
fcFxPortCapCos = _FcFxPortCapCos_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 9),
    _FcFxPortCapCos_Type()
)
fcFxPortCapCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapCos.setStatus("mandatory")


class _FcFxPortCapIntermix_Type(Integer32):
    """Custom type fcFxPortCapIntermix based on Integer32"""
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


_FcFxPortCapIntermix_Type.__name__ = "Integer32"
_FcFxPortCapIntermix_Object = MibTableColumn
fcFxPortCapIntermix = _FcFxPortCapIntermix_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 10),
    _FcFxPortCapIntermix_Type()
)
fcFxPortCapIntermix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapIntermix.setStatus("mandatory")
_FcFxPortCapStackedConnMode_Type = FcStackedConnMode
_FcFxPortCapStackedConnMode_Object = MibTableColumn
fcFxPortCapStackedConnMode = _FcFxPortCapStackedConnMode_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 11),
    _FcFxPortCapStackedConnMode_Type()
)
fcFxPortCapStackedConnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapStackedConnMode.setStatus("mandatory")


class _FcFxPortCapClass2SeqDeliv_Type(Integer32):
    """Custom type fcFxPortCapClass2SeqDeliv based on Integer32"""
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


_FcFxPortCapClass2SeqDeliv_Type.__name__ = "Integer32"
_FcFxPortCapClass2SeqDeliv_Object = MibTableColumn
fcFxPortCapClass2SeqDeliv = _FcFxPortCapClass2SeqDeliv_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 12),
    _FcFxPortCapClass2SeqDeliv_Type()
)
fcFxPortCapClass2SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapClass2SeqDeliv.setStatus("mandatory")


class _FcFxPortCapClass3SeqDeliv_Type(Integer32):
    """Custom type fcFxPortCapClass3SeqDeliv based on Integer32"""
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


_FcFxPortCapClass3SeqDeliv_Type.__name__ = "Integer32"
_FcFxPortCapClass3SeqDeliv_Object = MibTableColumn
fcFxPortCapClass3SeqDeliv = _FcFxPortCapClass3SeqDeliv_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 13),
    _FcFxPortCapClass3SeqDeliv_Type()
)
fcFxPortCapClass3SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapClass3SeqDeliv.setStatus("mandatory")
_FcFxPortCapHoldTimeMax_Type = MicroSeconds
_FcFxPortCapHoldTimeMax_Object = MibTableColumn
fcFxPortCapHoldTimeMax = _FcFxPortCapHoldTimeMax_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 14),
    _FcFxPortCapHoldTimeMax_Type()
)
fcFxPortCapHoldTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapHoldTimeMax.setStatus("mandatory")
_FcFxPortCapHoldTimeMin_Type = MicroSeconds
_FcFxPortCapHoldTimeMin_Object = MibTableColumn
fcFxPortCapHoldTimeMin = _FcFxPortCapHoldTimeMin_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 15),
    _FcFxPortCapHoldTimeMin_Type()
)
fcFxPortCapHoldTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapHoldTimeMin.setStatus("mandatory")
_FcFxPortCapBaudRates_Type = Fc0BaudRateCap
_FcFxPortCapBaudRates_Object = MibTableColumn
fcFxPortCapBaudRates = _FcFxPortCapBaudRates_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 16),
    _FcFxPortCapBaudRates_Type()
)
fcFxPortCapBaudRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapBaudRates.setStatus("deprecated")
_FcFxPortCapMedia_Type = Fc0MediaCap
_FcFxPortCapMedia_Object = MibTableColumn
fcFxPortCapMedia = _FcFxPortCapMedia_Object(
    (1, 3, 6, 1, 3, 42, 2, 1, 5, 1, 1, 17),
    _FcFxPortCapMedia_Type()
)
fcFxPortCapMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapMedia.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FCFABRIC-ELEMENT-MIB",
    **{"DisplayString": DisplayString,
       "MilliSeconds": MilliSeconds,
       "MicroSeconds": MicroSeconds,
       "FcNameId": FcNameId,
       "FabricName": FabricName,
       "FcPortName": FcPortName,
       "FcAddressId": FcAddressId,
       "FcRxDataFieldSize": FcRxDataFieldSize,
       "FcBbCredit": FcBbCredit,
       "FcphVersion": FcphVersion,
       "FcStackedConnMode": FcStackedConnMode,
       "FcCosCap": FcCosCap,
       "Fc0BaudRate": Fc0BaudRate,
       "Fc0BaudRateCap": Fc0BaudRateCap,
       "Fc0MediaCap": Fc0MediaCap,
       "Fc0Medium": Fc0Medium,
       "Fc0TxType": Fc0TxType,
       "Fc0Distance": Fc0Distance,
       "FcFeModuleCapacity": FcFeModuleCapacity,
       "FcFeFxPortCapacity": FcFeFxPortCapacity,
       "FcFeModuleIndex": FcFeModuleIndex,
       "FcFeFxPortIndex": FcFeFxPortIndex,
       "FcFeNxPortIndex": FcFeNxPortIndex,
       "FcFxPortMode": FcFxPortMode,
       "FcBbCreditModel": FcBbCreditModel,
       "fibreChannel": fibreChannel,
       "fcFabric": fcFabric,
       "fcFe": fcFe,
       "fcFeConfig": fcFeConfig,
       "fcFabricName": fcFabricName,
       "fcElementName": fcElementName,
       "fcFeModuleCapacity": fcFeModuleCapacity,
       "fcFeModuleTable": fcFeModuleTable,
       "fcFeModuleEntry": fcFeModuleEntry,
       "fcFeModuleIndex": fcFeModuleIndex,
       "fcFeModuleDescr": fcFeModuleDescr,
       "fcFeModuleObjectID": fcFeModuleObjectID,
       "fcFeModuleOperStatus": fcFeModuleOperStatus,
       "fcFeModuleLastChange": fcFeModuleLastChange,
       "fcFeModuleFxPortCapacity": fcFeModuleFxPortCapacity,
       "fcFeModuleName": fcFeModuleName,
       "fcFxConfTable": fcFxConfTable,
       "fcFxConfEntry": fcFxConfEntry,
       "fcFxConfModuleIndex": fcFxConfModuleIndex,
       "fcFxConfFxPortIndex": fcFxConfFxPortIndex,
       "fcFxPortName": fcFxPortName,
       "fcFxPortFcphVersionHigh": fcFxPortFcphVersionHigh,
       "fcFxPortFcphVersionLow": fcFxPortFcphVersionLow,
       "fcFxPortBbCredit": fcFxPortBbCredit,
       "fcFxPortRxBufSize": fcFxPortRxBufSize,
       "fcFxPortRatov": fcFxPortRatov,
       "fcFxPortEdtov": fcFxPortEdtov,
       "fcFxPortCosSupported": fcFxPortCosSupported,
       "fcFxPortIntermixSupported": fcFxPortIntermixSupported,
       "fcFxPortStackedConnMode": fcFxPortStackedConnMode,
       "fcFxPortClass2SeqDeliv": fcFxPortClass2SeqDeliv,
       "fcFxPortClass3SeqDeliv": fcFxPortClass3SeqDeliv,
       "fcFxPortHoldTime": fcFxPortHoldTime,
       "fcFxPortBaudRate": fcFxPortBaudRate,
       "fcFxPortMedium": fcFxPortMedium,
       "fcFxPortTxType": fcFxPortTxType,
       "fcFxPortDistance": fcFxPortDistance,
       "fcFeOp": fcFeOp,
       "fcFxPortOperTable": fcFxPortOperTable,
       "fcFxPortOperEntry": fcFxPortOperEntry,
       "fcFxPortOperModuleIndex": fcFxPortOperModuleIndex,
       "fcFxPortOperFxPortIndex": fcFxPortOperFxPortIndex,
       "fcFxPortID": fcFxPortID,
       "fcFPortAttachedPortName": fcFPortAttachedPortName,
       "fcFPortConnectedPort": fcFPortConnectedPort,
       "fcFxPortBbCreditAvailable": fcFxPortBbCreditAvailable,
       "fcFxPortOperMode": fcFxPortOperMode,
       "fcFxPortAdminMode": fcFxPortAdminMode,
       "fcFxPortPhysTable": fcFxPortPhysTable,
       "fcFxPortPhysEntry": fcFxPortPhysEntry,
       "fcFxPortPhysModuleIndex": fcFxPortPhysModuleIndex,
       "fcFxPortPhysFxPortIndex": fcFxPortPhysFxPortIndex,
       "fcFxPortPhysAdminStatus": fcFxPortPhysAdminStatus,
       "fcFxPortPhysOperStatus": fcFxPortPhysOperStatus,
       "fcFxPortPhysLastChange": fcFxPortPhysLastChange,
       "fcFxPortPhysRttov": fcFxPortPhysRttov,
       "fcFxlogiTable": fcFxlogiTable,
       "fcFxlogiEntry": fcFxlogiEntry,
       "fcFxlogiModuleIndex": fcFxlogiModuleIndex,
       "fcFxlogiFxPortIndex": fcFxlogiFxPortIndex,
       "fcFxlogiNxPortIndex": fcFxlogiNxPortIndex,
       "fcFxPortFcphVersionAgreed": fcFxPortFcphVersionAgreed,
       "fcFxPortNxPortBbCredit": fcFxPortNxPortBbCredit,
       "fcFxPortNxPortRxDataFieldSize": fcFxPortNxPortRxDataFieldSize,
       "fcFxPortCosSuppAgreed": fcFxPortCosSuppAgreed,
       "fcFxPortIntermixSuppAgreed": fcFxPortIntermixSuppAgreed,
       "fcFxPortStackedConnModeAgreed": fcFxPortStackedConnModeAgreed,
       "fcFxPortClass2SeqDelivAgreed": fcFxPortClass2SeqDelivAgreed,
       "fcFxPortClass3SeqDelivAgreed": fcFxPortClass3SeqDelivAgreed,
       "fcFxPortNxPortName": fcFxPortNxPortName,
       "fcFxPortConnectedNxPort": fcFxPortConnectedNxPort,
       "fcFxPortBbCreditModel": fcFxPortBbCreditModel,
       "fcFeError": fcFeError,
       "fcFxPortErrorTable": fcFxPortErrorTable,
       "fcFxPortErrorEntry": fcFxPortErrorEntry,
       "fcFxPortErrorModuleIndex": fcFxPortErrorModuleIndex,
       "fcFxPortErrorFxPortIndex": fcFxPortErrorFxPortIndex,
       "fcFxPortLinkFailures": fcFxPortLinkFailures,
       "fcFxPortSyncLosses": fcFxPortSyncLosses,
       "fcFxPortSigLosses": fcFxPortSigLosses,
       "fcFxPortPrimSeqProtoErrors": fcFxPortPrimSeqProtoErrors,
       "fcFxPortInvalidTxWords": fcFxPortInvalidTxWords,
       "fcFxPortInvalidCrcs": fcFxPortInvalidCrcs,
       "fcFxPortDelimiterErrors": fcFxPortDelimiterErrors,
       "fcFxPortAddressIdErrors": fcFxPortAddressIdErrors,
       "fcFxPortLinkResetIns": fcFxPortLinkResetIns,
       "fcFxPortLinkResetOuts": fcFxPortLinkResetOuts,
       "fcFxPortOlsIns": fcFxPortOlsIns,
       "fcFxPortOlsOuts": fcFxPortOlsOuts,
       "fcFeAcct": fcFeAcct,
       "fcFxPortC1AcctTable": fcFxPortC1AcctTable,
       "fcFxPortC1AcctEntry": fcFxPortC1AcctEntry,
       "fcFxPortC1AcctModuleIndex": fcFxPortC1AcctModuleIndex,
       "fcFxPortC1AcctFxPortIndex": fcFxPortC1AcctFxPortIndex,
       "fcFxPortC1InConnections": fcFxPortC1InConnections,
       "fcFxPortC1OutConnections": fcFxPortC1OutConnections,
       "fcFxPortC1FbsyFrames": fcFxPortC1FbsyFrames,
       "fcFxPortC1FrjtFrames": fcFxPortC1FrjtFrames,
       "fcFxPortC1ConnTime": fcFxPortC1ConnTime,
       "fcFxPortC1InFrames": fcFxPortC1InFrames,
       "fcFxPortC1OutFrames": fcFxPortC1OutFrames,
       "fcFxPortC1InOctets": fcFxPortC1InOctets,
       "fcFxPortC1OutOctets": fcFxPortC1OutOctets,
       "fcFxPortC1Discards": fcFxPortC1Discards,
       "fcFxPortC2AcctTable": fcFxPortC2AcctTable,
       "fcFxPortC2AcctEntry": fcFxPortC2AcctEntry,
       "fcFxPortC2AcctModuleIndex": fcFxPortC2AcctModuleIndex,
       "fcFxPortC2AcctFxPortIndex": fcFxPortC2AcctFxPortIndex,
       "fcFxPortC2InFrames": fcFxPortC2InFrames,
       "fcFxPortC2OutFrames": fcFxPortC2OutFrames,
       "fcFxPortC2InOctets": fcFxPortC2InOctets,
       "fcFxPortC2OutOctets": fcFxPortC2OutOctets,
       "fcFxPortC2Discards": fcFxPortC2Discards,
       "fcFxPortC2FbsyFrames": fcFxPortC2FbsyFrames,
       "fcFxPortC2FrjtFrames": fcFxPortC2FrjtFrames,
       "fcFxPortC3AcctTable": fcFxPortC3AcctTable,
       "fcFxPortC3AcctEntry": fcFxPortC3AcctEntry,
       "fcFxPortC3AcctModuleIndex": fcFxPortC3AcctModuleIndex,
       "fcFxPortC3AcctFxPortIndex": fcFxPortC3AcctFxPortIndex,
       "fcFxPortC3InFrames": fcFxPortC3InFrames,
       "fcFxPortC3OutFrames": fcFxPortC3OutFrames,
       "fcFxPortC3InOctets": fcFxPortC3InOctets,
       "fcFxPortC3OutOctets": fcFxPortC3OutOctets,
       "fcFxPortC3Discards": fcFxPortC3Discards,
       "fcFeCap": fcFeCap,
       "fcFxPortCapTable": fcFxPortCapTable,
       "fcFxPortCapEntry": fcFxPortCapEntry,
       "fcFxPortCapModuleIndex": fcFxPortCapModuleIndex,
       "fcFxPortCapFxPortIndex": fcFxPortCapFxPortIndex,
       "fcFxPortCapFcphVersionHigh": fcFxPortCapFcphVersionHigh,
       "fcFxPortCapFcphVersionLow": fcFxPortCapFcphVersionLow,
       "fcFxPortCapBbCreditMax": fcFxPortCapBbCreditMax,
       "fcFxPortCapBbCreditMin": fcFxPortCapBbCreditMin,
       "fcFxPortCapRxDataFieldSizeMax": fcFxPortCapRxDataFieldSizeMax,
       "fcFxPortCapRxDataFieldSizeMin": fcFxPortCapRxDataFieldSizeMin,
       "fcFxPortCapCos": fcFxPortCapCos,
       "fcFxPortCapIntermix": fcFxPortCapIntermix,
       "fcFxPortCapStackedConnMode": fcFxPortCapStackedConnMode,
       "fcFxPortCapClass2SeqDeliv": fcFxPortCapClass2SeqDeliv,
       "fcFxPortCapClass3SeqDeliv": fcFxPortCapClass3SeqDeliv,
       "fcFxPortCapHoldTimeMax": fcFxPortCapHoldTimeMax,
       "fcFxPortCapHoldTimeMin": fcFxPortCapHoldTimeMin,
       "fcFxPortCapBaudRates": fcFxPortCapBaudRates,
       "fcFxPortCapMedia": fcFxPortCapMedia}
)
