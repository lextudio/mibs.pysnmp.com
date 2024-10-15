# SNMP MIB module (SW-STRCTURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-STRCTURE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:57 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Marconi_ObjectIdentity = ObjectIdentity
marconi = _Marconi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_External_ObjectIdentity = ObjectIdentity
external = _External_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20)
)
_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1)
)
_Dlinkcommon_ObjectIdentity = ObjectIdentity
dlinkcommon = _Dlinkcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1)
)
_Golf_ObjectIdentity = ObjectIdentity
golf = _Golf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2)
)
_Golfproducts_ObjectIdentity = ObjectIdentity
golfproducts = _Golfproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1)
)
_Es2000_ObjectIdentity = ObjectIdentity
es2000 = _Es2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3)
)
_Golfcommon_ObjectIdentity = ObjectIdentity
golfcommon = _Golfcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2)
)
_Marconi_mgmt_ObjectIdentity = ObjectIdentity
marconi_mgmt = _Marconi_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)
)
_Es2000Mgmt_ObjectIdentity = ObjectIdentity
es2000Mgmt = _Es2000Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28)
)
_SwStructure_ObjectIdentity = ObjectIdentity
swStructure = _SwStructure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1)
)
_SwStructInfo_ObjectIdentity = ObjectIdentity
swStructInfo = _SwStructInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1)
)
_SwStructDevType_Type = ObjectIdentifier
_SwStructDevType_Object = MibScalar
swStructDevType = _SwStructDevType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 1),
    _SwStructDevType_Type()
)
swStructDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevType.setStatus("mandatory")


class _SwStructDevDescr_Type(DisplayString):
    """Custom type swStructDevDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwStructDevDescr_Type.__name__ = "DisplayString"
_SwStructDevDescr_Object = MibScalar
swStructDevDescr = _SwStructDevDescr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 2),
    _SwStructDevDescr_Type()
)
swStructDevDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevDescr.setStatus("mandatory")
_SwStructDevPortEncodingFactor_Type = Integer32
_SwStructDevPortEncodingFactor_Object = MibScalar
swStructDevPortEncodingFactor = _SwStructDevPortEncodingFactor_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 3),
    _SwStructDevPortEncodingFactor_Type()
)
swStructDevPortEncodingFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevPortEncodingFactor.setStatus("mandatory")


class _SwStructDevLedInfo_Type(OctetString):
    """Custom type swStructDevLedInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SwStructDevLedInfo_Type.__name__ = "OctetString"
_SwStructDevLedInfo_Object = MibScalar
swStructDevLedInfo = _SwStructDevLedInfo_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 4),
    _SwStructDevLedInfo_Type()
)
swStructDevLedInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevLedInfo.setStatus("mandatory")
_SwStructDevMaxModuleNum_Type = Integer32
_SwStructDevMaxModuleNum_Object = MibScalar
swStructDevMaxModuleNum = _SwStructDevMaxModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 5),
    _SwStructDevMaxModuleNum_Type()
)
swStructDevMaxModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevMaxModuleNum.setStatus("mandatory")
_SwStructDevMaxPortNum_Type = Integer32
_SwStructDevMaxPortNum_Object = MibScalar
swStructDevMaxPortNum = _SwStructDevMaxPortNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 6),
    _SwStructDevMaxPortNum_Type()
)
swStructDevMaxPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevMaxPortNum.setStatus("mandatory")
_SwStructDevNumOfPortInUse_Type = Integer32
_SwStructDevNumOfPortInUse_Object = MibScalar
swStructDevNumOfPortInUse = _SwStructDevNumOfPortInUse_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 7),
    _SwStructDevNumOfPortInUse_Type()
)
swStructDevNumOfPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevNumOfPortInUse.setStatus("mandatory")


class _SwStructDevOperStatus_Type(Integer32):
    """Custom type swStructDevOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("fatalErr", 10),
          ("nonFatalErr", 9),
          ("normal", 5),
          ("notAvail", 2),
          ("other", 1),
          ("removed", 3))
    )


_SwStructDevOperStatus_Type.__name__ = "Integer32"
_SwStructDevOperStatus_Object = MibScalar
swStructDevOperStatus = _SwStructDevOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 8),
    _SwStructDevOperStatus_Type()
)
swStructDevOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevOperStatus.setStatus("mandatory")
_SwStructDevLastChange_Type = Integer32
_SwStructDevLastChange_Object = MibScalar
swStructDevLastChange = _SwStructDevLastChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 9),
    _SwStructDevLastChange_Type()
)
swStructDevLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevLastChange.setStatus("mandatory")
_SwStructModuleTable_Object = MibTable
swStructModuleTable = _SwStructModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2)
)
if mibBuilder.loadTexts:
    swStructModuleTable.setStatus("mandatory")
_SwStructModuleEntry_Object = MibTableRow
swStructModuleEntry = _SwStructModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1)
)
swStructModuleEntry.setIndexNames(
    (0, "SW-STRCTURE-MIB", "swStructModuleUnitIndex"),
    (0, "SW-STRCTURE-MIB", "swStructModuleIndex"),
)
if mibBuilder.loadTexts:
    swStructModuleEntry.setStatus("mandatory")
_SwStructModuleUnitIndex_Type = Integer32
_SwStructModuleUnitIndex_Object = MibTableColumn
swStructModuleUnitIndex = _SwStructModuleUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 1),
    _SwStructModuleUnitIndex_Type()
)
swStructModuleUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleUnitIndex.setStatus("mandatory")
_SwStructModuleIndex_Type = Integer32
_SwStructModuleIndex_Object = MibTableColumn
swStructModuleIndex = _SwStructModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 2),
    _SwStructModuleIndex_Type()
)
swStructModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleIndex.setStatus("mandatory")
_SwStructModuleType_Type = ObjectIdentifier
_SwStructModuleType_Object = MibTableColumn
swStructModuleType = _SwStructModuleType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 3),
    _SwStructModuleType_Type()
)
swStructModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleType.setStatus("mandatory")


class _SwStructModuleDescr_Type(DisplayString):
    """Custom type swStructModuleDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwStructModuleDescr_Type.__name__ = "DisplayString"
_SwStructModuleDescr_Object = MibTableColumn
swStructModuleDescr = _SwStructModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 4),
    _SwStructModuleDescr_Type()
)
swStructModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleDescr.setStatus("mandatory")
_SwStructModuleVersion_Type = Integer32
_SwStructModuleVersion_Object = MibTableColumn
swStructModuleVersion = _SwStructModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 5),
    _SwStructModuleVersion_Type()
)
swStructModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleVersion.setStatus("mandatory")
_SwStructModuleMaxPortNum_Type = Integer32
_SwStructModuleMaxPortNum_Object = MibTableColumn
swStructModuleMaxPortNum = _SwStructModuleMaxPortNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 6),
    _SwStructModuleMaxPortNum_Type()
)
swStructModuleMaxPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleMaxPortNum.setStatus("mandatory")
_SwStructModuleEncodingOffset_Type = Integer32
_SwStructModuleEncodingOffset_Object = MibTableColumn
swStructModuleEncodingOffset = _SwStructModuleEncodingOffset_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 7),
    _SwStructModuleEncodingOffset_Type()
)
swStructModuleEncodingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleEncodingOffset.setStatus("mandatory")


class _SwStructModuleLEDInfo_Type(OctetString):
    """Custom type swStructModuleLEDInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SwStructModuleLEDInfo_Type.__name__ = "OctetString"
_SwStructModuleLEDInfo_Object = MibTableColumn
swStructModuleLEDInfo = _SwStructModuleLEDInfo_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 8),
    _SwStructModuleLEDInfo_Type()
)
swStructModuleLEDInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleLEDInfo.setStatus("mandatory")


class _SwStructModuleOperStatus_Type(Integer32):
    """Custom type swStructModuleOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("fatalErr", 10),
          ("nonFatalErr", 9),
          ("normal", 5),
          ("notAvail", 2),
          ("other", 1),
          ("removed", 3))
    )


_SwStructModuleOperStatus_Type.__name__ = "Integer32"
_SwStructModuleOperStatus_Object = MibTableColumn
swStructModuleOperStatus = _SwStructModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 9),
    _SwStructModuleOperStatus_Type()
)
swStructModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleOperStatus.setStatus("mandatory")
_SwStructModuleLastChange_Type = Integer32
_SwStructModuleLastChange_Object = MibTableColumn
swStructModuleLastChange = _SwStructModuleLastChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 10),
    _SwStructModuleLastChange_Type()
)
swStructModuleLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleLastChange.setStatus("mandatory")
_SwStructPowerTable_Object = MibTable
swStructPowerTable = _SwStructPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3)
)
if mibBuilder.loadTexts:
    swStructPowerTable.setStatus("mandatory")
_SwStructPowerEntry_Object = MibTableRow
swStructPowerEntry = _SwStructPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1)
)
swStructPowerEntry.setIndexNames(
    (0, "SW-STRCTURE-MIB", "swStructPowerIndex"),
)
if mibBuilder.loadTexts:
    swStructPowerEntry.setStatus("mandatory")
_SwStructPowerIndex_Type = Integer32
_SwStructPowerIndex_Object = MibTableColumn
swStructPowerIndex = _SwStructPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 1),
    _SwStructPowerIndex_Type()
)
swStructPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerIndex.setStatus("mandatory")


class _SwStructPowerInfo_Type(DisplayString):
    """Custom type swStructPowerInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwStructPowerInfo_Type.__name__ = "DisplayString"
_SwStructPowerInfo_Object = MibTableColumn
swStructPowerInfo = _SwStructPowerInfo_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 2),
    _SwStructPowerInfo_Type()
)
swStructPowerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerInfo.setStatus("mandatory")
_SwStructPowerTemperature_Type = Integer32
_SwStructPowerTemperature_Object = MibTableColumn
swStructPowerTemperature = _SwStructPowerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 3),
    _SwStructPowerTemperature_Type()
)
swStructPowerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerTemperature.setStatus("mandatory")


class _SwStructPowerVolt_Type(DisplayString):
    """Custom type swStructPowerVolt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SwStructPowerVolt_Type.__name__ = "DisplayString"
_SwStructPowerVolt_Object = MibTableColumn
swStructPowerVolt = _SwStructPowerVolt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 4),
    _SwStructPowerVolt_Type()
)
swStructPowerVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerVolt.setStatus("mandatory")
_SwStructPowerAmp_Type = Integer32
_SwStructPowerAmp_Object = MibTableColumn
swStructPowerAmp = _SwStructPowerAmp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 5),
    _SwStructPowerAmp_Type()
)
swStructPowerAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerAmp.setStatus("mandatory")


class _SwStructPowerFan1Status_Type(Integer32):
    """Custom type swStructPowerFan1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fanFail", 2),
          ("fanOk", 1),
          ("other", 3))
    )


_SwStructPowerFan1Status_Type.__name__ = "Integer32"
_SwStructPowerFan1Status_Object = MibTableColumn
swStructPowerFan1Status = _SwStructPowerFan1Status_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 6),
    _SwStructPowerFan1Status_Type()
)
swStructPowerFan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerFan1Status.setStatus("mandatory")


class _SwStructPowerFan2Status_Type(Integer32):
    """Custom type swStructPowerFan2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fanFail", 2),
          ("fanOk", 1),
          ("other", 3))
    )


_SwStructPowerFan2Status_Type.__name__ = "Integer32"
_SwStructPowerFan2Status_Object = MibTableColumn
swStructPowerFan2Status = _SwStructPowerFan2Status_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 7),
    _SwStructPowerFan2Status_Type()
)
swStructPowerFan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerFan2Status.setStatus("mandatory")


class _SwStructPowerStatus_Type(Integer32):
    """Custom type swStructPowerStatus based on Integer32"""
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
        *(("acFailPsFail", 1),
          ("acPresentPsFail", 2),
          ("other", 4),
          ("psGood", 3))
    )


_SwStructPowerStatus_Type.__name__ = "Integer32"
_SwStructPowerStatus_Object = MibTableColumn
swStructPowerStatus = _SwStructPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 8),
    _SwStructPowerStatus_Type()
)
swStructPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerStatus.setStatus("mandatory")
_SwStructSystemFanTable_Object = MibTable
swStructSystemFanTable = _SwStructSystemFanTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 4)
)
if mibBuilder.loadTexts:
    swStructSystemFanTable.setStatus("mandatory")
_SwStructSystemFanEntry_Object = MibTableRow
swStructSystemFanEntry = _SwStructSystemFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 4, 1)
)
swStructSystemFanEntry.setIndexNames(
    (0, "SW-STRCTURE-MIB", "swStructSystemFanIndex"),
)
if mibBuilder.loadTexts:
    swStructSystemFanEntry.setStatus("mandatory")
_SwStructSystemFanIndex_Type = Integer32
_SwStructSystemFanIndex_Object = MibTableColumn
swStructSystemFanIndex = _SwStructSystemFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 4, 1, 1),
    _SwStructSystemFanIndex_Type()
)
swStructSystemFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructSystemFanIndex.setStatus("mandatory")


class _SwStructSystemFanStatus_Type(Integer32):
    """Custom type swStructSystemFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fanFail", 2),
          ("fanOk", 1),
          ("other", 3))
    )


_SwStructSystemFanStatus_Type.__name__ = "Integer32"
_SwStructSystemFanStatus_Object = MibTableColumn
swStructSystemFanStatus = _SwStructSystemFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 4, 1, 2),
    _SwStructSystemFanStatus_Type()
)
swStructSystemFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructSystemFanStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

powerTemperatureWarnning = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 5)
)
powerTemperatureWarnning.setObjects(
    ("SW-STRCTURE-MIB", "swStructPowerIndex")
)
if mibBuilder.loadTexts:
    powerTemperatureWarnning.setStatus(
        ""
    )

powerVoltWarnning = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 6)
)
powerVoltWarnning.setObjects(
    ("SW-STRCTURE-MIB", "swStructPowerIndex")
)
if mibBuilder.loadTexts:
    powerVoltWarnning.setStatus(
        ""
    )

powerCurrentWarnning = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 7)
)
powerCurrentWarnning.setObjects(
    ("SW-STRCTURE-MIB", "swStructPowerIndex")
)
if mibBuilder.loadTexts:
    powerCurrentWarnning.setStatus(
        ""
    )

powerFan1Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 8)
)
powerFan1Fail.setObjects(
    ("SW-STRCTURE-MIB", "swStructPowerIndex")
)
if mibBuilder.loadTexts:
    powerFan1Fail.setStatus(
        ""
    )

powerFan2Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 9)
)
powerFan2Fail.setObjects(
    ("SW-STRCTURE-MIB", "swStructPowerIndex")
)
if mibBuilder.loadTexts:
    powerFan2Fail.setStatus(
        ""
    )

systemFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 10)
)
systemFanFail.setObjects(
    ("SW-STRCTURE-MIB", "swStructSystemFanIndex")
)
if mibBuilder.loadTexts:
    systemFanFail.setStatus(
        ""
    )

powerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 11)
)
powerRemoved.setObjects(
    ("SW-STRCTURE-MIB", "swStructPowerIndex")
)
if mibBuilder.loadTexts:
    powerRemoved.setStatus(
        ""
    )

powerInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 12)
)
powerInserted.setObjects(
    ("SW-STRCTURE-MIB", "swStructPowerIndex")
)
if mibBuilder.loadTexts:
    powerInserted.setStatus(
        ""
    )

powerBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3, 0, 13)
)
powerBad.setObjects(
    ("SW-STRCTURE-MIB", "swStructPowerIndex")
)
if mibBuilder.loadTexts:
    powerBad.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-STRCTURE-MIB",
    **{"marconi": marconi,
       "systems": systems,
       "external": external,
       "dlink": dlink,
       "dlinkcommon": dlinkcommon,
       "golf": golf,
       "golfproducts": golfproducts,
       "es2000": es2000,
       "powerTemperatureWarnning": powerTemperatureWarnning,
       "powerVoltWarnning": powerVoltWarnning,
       "powerCurrentWarnning": powerCurrentWarnning,
       "powerFan1Fail": powerFan1Fail,
       "powerFan2Fail": powerFan2Fail,
       "systemFanFail": systemFanFail,
       "powerRemoved": powerRemoved,
       "powerInserted": powerInserted,
       "powerBad": powerBad,
       "golfcommon": golfcommon,
       "marconi-mgmt": marconi_mgmt,
       "es2000Mgmt": es2000Mgmt,
       "swStructure": swStructure,
       "swStructInfo": swStructInfo,
       "swStructDevType": swStructDevType,
       "swStructDevDescr": swStructDevDescr,
       "swStructDevPortEncodingFactor": swStructDevPortEncodingFactor,
       "swStructDevLedInfo": swStructDevLedInfo,
       "swStructDevMaxModuleNum": swStructDevMaxModuleNum,
       "swStructDevMaxPortNum": swStructDevMaxPortNum,
       "swStructDevNumOfPortInUse": swStructDevNumOfPortInUse,
       "swStructDevOperStatus": swStructDevOperStatus,
       "swStructDevLastChange": swStructDevLastChange,
       "swStructModuleTable": swStructModuleTable,
       "swStructModuleEntry": swStructModuleEntry,
       "swStructModuleUnitIndex": swStructModuleUnitIndex,
       "swStructModuleIndex": swStructModuleIndex,
       "swStructModuleType": swStructModuleType,
       "swStructModuleDescr": swStructModuleDescr,
       "swStructModuleVersion": swStructModuleVersion,
       "swStructModuleMaxPortNum": swStructModuleMaxPortNum,
       "swStructModuleEncodingOffset": swStructModuleEncodingOffset,
       "swStructModuleLEDInfo": swStructModuleLEDInfo,
       "swStructModuleOperStatus": swStructModuleOperStatus,
       "swStructModuleLastChange": swStructModuleLastChange,
       "swStructPowerTable": swStructPowerTable,
       "swStructPowerEntry": swStructPowerEntry,
       "swStructPowerIndex": swStructPowerIndex,
       "swStructPowerInfo": swStructPowerInfo,
       "swStructPowerTemperature": swStructPowerTemperature,
       "swStructPowerVolt": swStructPowerVolt,
       "swStructPowerAmp": swStructPowerAmp,
       "swStructPowerFan1Status": swStructPowerFan1Status,
       "swStructPowerFan2Status": swStructPowerFan2Status,
       "swStructPowerStatus": swStructPowerStatus,
       "swStructSystemFanTable": swStructSystemFanTable,
       "swStructSystemFanEntry": swStructSystemFanEntry,
       "swStructSystemFanIndex": swStructSystemFanIndex,
       "swStructSystemFanStatus": swStructSystemFanStatus}
)
