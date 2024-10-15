# SNMP MIB module (SIEMENS-PN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SIEMENS-PN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:16 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

hicomMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1)
)


# Types definitions



class DiscoveryStates(Integer32):
    """Custom type DiscoveryStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              11,
              12,
              13,
              14,
              15,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("done", 1),
          ("errdelBusy", 23),
          ("errdelDone", 21),
          ("errdelError", 22),
          ("errdelFinerr", 25),
          ("errdelFinok", 24),
          ("error", 2),
          ("finerr", 5),
          ("finok", 4),
          ("kill", 6),
          ("masterBusy", 13),
          ("masterDone", 11),
          ("masterError", 12),
          ("masterFinerr", 15),
          ("masterFinok", 14))
    )





class DiscoveryModes(Integer32):
    """Custom type DiscoveryModes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("man", 1),
          ("undef", 9))
    )





class AlarmFilterStates(Integer32):
    """Custom type AlarmFilterStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 2),
          ("filterOn", 1))
    )





class AlarmPriorities(Integer32):
    """Custom type AlarmPriorities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("device", 3),
          ("major", 2),
          ("minor", 1))
    )





class TrunkTypes(Integer32):
    """Custom type TrunkTypes based on Integer32"""
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
        *(("analog", 2),
          ("digital", 3),
          ("special", 4),
          ("undef", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SiemensUnits_ObjectIdentity = ObjectIdentity
siemensUnits = _SiemensUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7)
)
_Pn_ObjectIdentity = ObjectIdentity
pn = _Pn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2)
)
_HicomControl_ObjectIdentity = ObjectIdentity
hicomControl = _HicomControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 0)
)
_HicomProxyName_Type = DisplayString
_HicomProxyName_Object = MibScalar
hicomProxyName = _HicomProxyName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 0, 1),
    _HicomProxyName_Type()
)
hicomProxyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomProxyName.setStatus("current")
_HicomAgentVersion_Type = DisplayString
_HicomAgentVersion_Object = MibScalar
hicomAgentVersion = _HicomAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 0, 2),
    _HicomAgentVersion_Type()
)
hicomAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAgentVersion.setStatus("current")
_HicomMIBVersion_Type = DisplayString
_HicomMIBVersion_Object = MibScalar
hicomMIBVersion = _HicomMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 0, 3),
    _HicomMIBVersion_Type()
)
hicomMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomMIBVersion.setStatus("current")
_HicomSystem_ObjectIdentity = ObjectIdentity
hicomSystem = _HicomSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1)
)
_HicomNumHicoms_Type = Integer32
_HicomNumHicoms_Object = MibScalar
hicomNumHicoms = _HicomNumHicoms_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 1),
    _HicomNumHicoms_Type()
)
hicomNumHicoms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomNumHicoms.setStatus("current")
_HicomSystemChanges_Type = Counter32
_HicomSystemChanges_Object = MibScalar
hicomSystemChanges = _HicomSystemChanges_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 2),
    _HicomSystemChanges_Type()
)
hicomSystemChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSystemChanges.setStatus("current")
_HicomSysTable_Object = MibTable
hicomSysTable = _HicomSysTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hicomSysTable.setStatus("current")
_HicomSysEntry_Object = MibTableRow
hicomSysEntry = _HicomSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1)
)
hicomSysEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomSysPabxId"),
)
if mibBuilder.loadTexts:
    hicomSysEntry.setStatus("current")
_HicomSysPabxId_Type = Integer32
_HicomSysPabxId_Object = MibTableColumn
hicomSysPabxId = _HicomSysPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 1),
    _HicomSysPabxId_Type()
)
hicomSysPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysPabxId.setStatus("current")
_HicomSysConNo_Type = DisplayString
_HicomSysConNo_Object = MibTableColumn
hicomSysConNo = _HicomSysConNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 2),
    _HicomSysConNo_Type()
)
hicomSysConNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysConNo.setStatus("current")
_HicomSysEstabl_Type = Integer32
_HicomSysEstabl_Object = MibTableColumn
hicomSysEstabl = _HicomSysEstabl_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 3),
    _HicomSysEstabl_Type()
)
hicomSysEstabl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysEstabl.setStatus("current")
_HicomSysPosNo_Type = DisplayString
_HicomSysPosNo_Object = MibTableColumn
hicomSysPosNo = _HicomSysPosNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 4),
    _HicomSysPosNo_Type()
)
hicomSysPosNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysPosNo.setStatus("current")
_HicomSysMnemonic_Type = DisplayString
_HicomSysMnemonic_Object = MibTableColumn
hicomSysMnemonic = _HicomSysMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 5),
    _HicomSysMnemonic_Type()
)
hicomSysMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysMnemonic.setStatus("current")
_HicomSysCustName_Type = DisplayString
_HicomSysCustName_Object = MibTableColumn
hicomSysCustName = _HicomSysCustName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 6),
    _HicomSysCustName_Type()
)
hicomSysCustName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysCustName.setStatus("current")
_HicomSysCbCode_Type = DisplayString
_HicomSysCbCode_Object = MibTableColumn
hicomSysCbCode = _HicomSysCbCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 7),
    _HicomSysCbCode_Type()
)
hicomSysCbCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysCbCode.setStatus("current")
_HicomSysTelNo_Type = DisplayString
_HicomSysTelNo_Object = MibTableColumn
hicomSysTelNo = _HicomSysTelNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 8),
    _HicomSysTelNo_Type()
)
hicomSysTelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysTelNo.setStatus("current")
_HicomSysCutOver_Type = DisplayString
_HicomSysCutOver_Object = MibTableColumn
hicomSysCutOver = _HicomSysCutOver_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 9),
    _HicomSysCutOver_Type()
)
hicomSysCutOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysCutOver.setStatus("current")
_HicomSysClnr_Type = DisplayString
_HicomSysClnr_Object = MibTableColumn
hicomSysClnr = _HicomSysClnr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 11),
    _HicomSysClnr_Type()
)
hicomSysClnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysClnr.setStatus("current")
_HicomSysPabxNo_Type = DisplayString
_HicomSysPabxNo_Object = MibTableColumn
hicomSysPabxNo = _HicomSysPabxNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 12),
    _HicomSysPabxNo_Type()
)
hicomSysPabxNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysPabxNo.setStatus("current")
_HicomSysLocation_Type = DisplayString
_HicomSysLocation_Object = MibTableColumn
hicomSysLocation = _HicomSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 13),
    _HicomSysLocation_Type()
)
hicomSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysLocation.setStatus("current")
_HicomSysRemark_Type = DisplayString
_HicomSysRemark_Object = MibTableColumn
hicomSysRemark = _HicomSysRemark_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 14),
    _HicomSysRemark_Type()
)
hicomSysRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysRemark.setStatus("current")
_HicomSysSwLic_Type = DisplayString
_HicomSysSwLic_Object = MibTableColumn
hicomSysSwLic = _HicomSysSwLic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 15),
    _HicomSysSwLic_Type()
)
hicomSysSwLic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysSwLic.setStatus("current")
_HicomSysSysType_Type = DisplayString
_HicomSysSysType_Object = MibTableColumn
hicomSysSysType = _HicomSysSysType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 16),
    _HicomSysSysType_Type()
)
hicomSysSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysSysType.setStatus("current")
_HicomSysApsPa_Type = DisplayString
_HicomSysApsPa_Object = MibTableColumn
hicomSysApsPa = _HicomSysApsPa_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 17),
    _HicomSysApsPa_Type()
)
hicomSysApsPa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysApsPa.setStatus("current")
_HicomSysTimeStamp_Type = Integer32
_HicomSysTimeStamp_Object = MibTableColumn
hicomSysTimeStamp = _HicomSysTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 26),
    _HicomSysTimeStamp_Type()
)
hicomSysTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysTimeStamp.setStatus("current")
_HicomSysDescription_Type = DisplayString
_HicomSysDescription_Object = MibTableColumn
hicomSysDescription = _HicomSysDescription_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 34),
    _HicomSysDescription_Type()
)
hicomSysDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysDescription.setStatus("current")
_HicomSysVersion_Type = DisplayString
_HicomSysVersion_Object = MibTableColumn
hicomSysVersion = _HicomSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 39),
    _HicomSysVersion_Type()
)
hicomSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysVersion.setStatus("current")
_HicomSysCustomerSpecific_Type = DisplayString
_HicomSysCustomerSpecific_Object = MibTableColumn
hicomSysCustomerSpecific = _HicomSysCustomerSpecific_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 44),
    _HicomSysCustomerSpecific_Type()
)
hicomSysCustomerSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysCustomerSpecific.setStatus("current")
_HicomSysStreetAddress_Type = DisplayString
_HicomSysStreetAddress_Object = MibTableColumn
hicomSysStreetAddress = _HicomSysStreetAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 45),
    _HicomSysStreetAddress_Type()
)
hicomSysStreetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysStreetAddress.setStatus("current")
_HicomSysLineType_Type = DisplayString
_HicomSysLineType_Object = MibTableColumn
hicomSysLineType = _HicomSysLineType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 46),
    _HicomSysLineType_Type()
)
hicomSysLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysLineType.setStatus("current")
_HicomSysProduct_Type = DisplayString
_HicomSysProduct_Object = MibTableColumn
hicomSysProduct = _HicomSysProduct_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 48),
    _HicomSysProduct_Type()
)
hicomSysProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysProduct.setStatus("current")
_HicomSysCustomerContact_Type = DisplayString
_HicomSysCustomerContact_Object = MibTableColumn
hicomSysCustomerContact = _HicomSysCustomerContact_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 49),
    _HicomSysCustomerContact_Type()
)
hicomSysCustomerContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysCustomerContact.setStatus("current")
_HicomSysServiceDistrict_Type = DisplayString
_HicomSysServiceDistrict_Object = MibTableColumn
hicomSysServiceDistrict = _HicomSysServiceDistrict_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 50),
    _HicomSysServiceDistrict_Type()
)
hicomSysServiceDistrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysServiceDistrict.setStatus("current")
_HicomSysCustomerContract_Type = DisplayString
_HicomSysCustomerContract_Object = MibTableColumn
hicomSysCustomerContract = _HicomSysCustomerContract_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 51),
    _HicomSysCustomerContract_Type()
)
hicomSysCustomerContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysCustomerContract.setStatus("current")
_HicomSysTimeOfLastFm_Type = Integer32
_HicomSysTimeOfLastFm_Object = MibTableColumn
hicomSysTimeOfLastFm = _HicomSysTimeOfLastFm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 53),
    _HicomSysTimeOfLastFm_Type()
)
hicomSysTimeOfLastFm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysTimeOfLastFm.setStatus("current")
_HicomSysHicomSwVersion_Type = DisplayString
_HicomSysHicomSwVersion_Object = MibTableColumn
hicomSysHicomSwVersion = _HicomSysHicomSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 55),
    _HicomSysHicomSwVersion_Type()
)
hicomSysHicomSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysHicomSwVersion.setStatus("current")
_HicomSysEndWarranty_Type = DisplayString
_HicomSysEndWarranty_Object = MibTableColumn
hicomSysEndWarranty = _HicomSysEndWarranty_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 58),
    _HicomSysEndWarranty_Type()
)
hicomSysEndWarranty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysEndWarranty.setStatus("current")
_HicomSysBatteryType_Type = DisplayString
_HicomSysBatteryType_Object = MibTableColumn
hicomSysBatteryType = _HicomSysBatteryType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 61),
    _HicomSysBatteryType_Type()
)
hicomSysBatteryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysBatteryType.setStatus("current")
_HicomSysBatteryCapac_Type = DisplayString
_HicomSysBatteryCapac_Object = MibTableColumn
hicomSysBatteryCapac = _HicomSysBatteryCapac_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 62),
    _HicomSysBatteryCapac_Type()
)
hicomSysBatteryCapac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysBatteryCapac.setStatus("current")
_HicomSysInterface_Type = DisplayString
_HicomSysInterface_Object = MibTableColumn
hicomSysInterface = _HicomSysInterface_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 63),
    _HicomSysInterface_Type()
)
hicomSysInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysInterface.setStatus("current")
_HicomSysSystemRoomTel_Type = DisplayString
_HicomSysSystemRoomTel_Object = MibTableColumn
hicomSysSystemRoomTel = _HicomSysSystemRoomTel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 64),
    _HicomSysSystemRoomTel_Type()
)
hicomSysSystemRoomTel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysSystemRoomTel.setStatus("current")
_HicomSysNoType_Type = DisplayString
_HicomSysNoType_Object = MibTableColumn
hicomSysNoType = _HicomSysNoType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 71),
    _HicomSysNoType_Type()
)
hicomSysNoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysNoType.setStatus("current")
_HicomSysCustServer_Type = DisplayString
_HicomSysCustServer_Object = MibTableColumn
hicomSysCustServer = _HicomSysCustServer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 72),
    _HicomSysCustServer_Type()
)
hicomSysCustServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysCustServer.setStatus("current")
_HicomSysCustNoid_Type = DisplayString
_HicomSysCustNoid_Object = MibTableColumn
hicomSysCustNoid = _HicomSysCustNoid_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 73),
    _HicomSysCustNoid_Type()
)
hicomSysCustNoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysCustNoid.setStatus("current")
_HicomSysNoName_Type = DisplayString
_HicomSysNoName_Object = MibTableColumn
hicomSysNoName = _HicomSysNoName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 74),
    _HicomSysNoName_Type()
)
hicomSysNoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysNoName.setStatus("current")
_HicomSysRemarkCd_Type = DisplayString
_HicomSysRemarkCd_Object = MibTableColumn
hicomSysRemarkCd = _HicomSysRemarkCd_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 75),
    _HicomSysRemarkCd_Type()
)
hicomSysRemarkCd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysRemarkCd.setStatus("current")
_HicomSysHSystemRelease_Type = DisplayString
_HicomSysHSystemRelease_Object = MibTableColumn
hicomSysHSystemRelease = _HicomSysHSystemRelease_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 76),
    _HicomSysHSystemRelease_Type()
)
hicomSysHSystemRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysHSystemRelease.setStatus("current")
_HicomSysHcmAmolang_Type = DisplayString
_HicomSysHcmAmolang_Object = MibTableColumn
hicomSysHcmAmolang = _HicomSysHcmAmolang_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 77),
    _HicomSysHcmAmolang_Type()
)
hicomSysHcmAmolang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysHcmAmolang.setStatus("current")
_HicomSysRemarkCon_Type = DisplayString
_HicomSysRemarkCon_Object = MibTableColumn
hicomSysRemarkCon = _HicomSysRemarkCon_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 78),
    _HicomSysRemarkCon_Type()
)
hicomSysRemarkCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysRemarkCon.setStatus("current")
_HicomSysIpAddress_Type = DisplayString
_HicomSysIpAddress_Object = MibTableColumn
hicomSysIpAddress = _HicomSysIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 79),
    _HicomSysIpAddress_Type()
)
hicomSysIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysIpAddress.setStatus("current")
_HicomSysRemarkCom_Type = DisplayString
_HicomSysRemarkCom_Object = MibTableColumn
hicomSysRemarkCom = _HicomSysRemarkCom_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 80),
    _HicomSysRemarkCom_Type()
)
hicomSysRemarkCom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysRemarkCom.setStatus("current")
_HicomSysMsvProgNum_Type = Integer32
_HicomSysMsvProgNum_Object = MibTableColumn
hicomSysMsvProgNum = _HicomSysMsvProgNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 81),
    _HicomSysMsvProgNum_Type()
)
hicomSysMsvProgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysMsvProgNum.setStatus("current")
_HicomSysMsvRegNum_Type = Integer32
_HicomSysMsvRegNum_Object = MibTableColumn
hicomSysMsvRegNum = _HicomSysMsvRegNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 82),
    _HicomSysMsvRegNum_Type()
)
hicomSysMsvRegNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysMsvRegNum.setStatus("current")
_HicomSysHcEquipNr1_Type = DisplayString
_HicomSysHcEquipNr1_Object = MibTableColumn
hicomSysHcEquipNr1 = _HicomSysHcEquipNr1_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 83),
    _HicomSysHcEquipNr1_Type()
)
hicomSysHcEquipNr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysHcEquipNr1.setStatus("current")
_HicomSysHcEquipNr2_Type = DisplayString
_HicomSysHcEquipNr2_Object = MibTableColumn
hicomSysHcEquipNr2 = _HicomSysHcEquipNr2_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 84),
    _HicomSysHcEquipNr2_Type()
)
hicomSysHcEquipNr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysHcEquipNr2.setStatus("current")
_HicomSysDaUrl_Type = DisplayString
_HicomSysDaUrl_Object = MibTableColumn
hicomSysDaUrl = _HicomSysDaUrl_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 85),
    _HicomSysDaUrl_Type()
)
hicomSysDaUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysDaUrl.setStatus("current")
_HicomSysHcmCorrState_Type = DisplayString
_HicomSysHcmCorrState_Object = MibTableColumn
hicomSysHcmCorrState = _HicomSysHcmCorrState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 86),
    _HicomSysHcmCorrState_Type()
)
hicomSysHcmCorrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysHcmCorrState.setStatus("current")


class _HicomSysNodeNo_Type(Integer32):
    """Custom type hicomSysNodeNo based on Integer32"""
    defaultValue = 0


_HicomSysNodeNo_Object = MibTableColumn
hicomSysNodeNo = _HicomSysNodeNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 100),
    _HicomSysNodeNo_Type()
)
hicomSysNodeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysNodeNo.setStatus("current")


class _HicomSysLang_Type(Integer32):
    """Custom type hicomSysLang based on Integer32"""
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
        *(("english", 3),
          ("german", 2),
          ("undef", 1))
    )


_HicomSysLang_Type.__name__ = "Integer32"
_HicomSysLang_Object = MibTableColumn
hicomSysLang = _HicomSysLang_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 101),
    _HicomSysLang_Type()
)
hicomSysLang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysLang.setStatus("current")


class _HicomSysMgrNetId_Type(OctetString):
    """Custom type hicomSysMgrNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HicomSysMgrNetId_Type.__name__ = "OctetString"
_HicomSysMgrNetId_Object = MibTableColumn
hicomSysMgrNetId = _HicomSysMgrNetId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 102),
    _HicomSysMgrNetId_Type()
)
hicomSysMgrNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSysMgrNetId.setStatus("current")


class _HicomSysMgrSubNetId_Type(OctetString):
    """Custom type hicomSysMgrSubNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HicomSysMgrSubNetId_Type.__name__ = "OctetString"
_HicomSysMgrSubNetId_Object = MibTableColumn
hicomSysMgrSubNetId = _HicomSysMgrSubNetId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 103),
    _HicomSysMgrSubNetId_Type()
)
hicomSysMgrSubNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSysMgrSubNetId.setStatus("current")


class _HicomSysMgrPhysNetId_Type(OctetString):
    """Custom type hicomSysMgrPhysNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HicomSysMgrPhysNetId_Type.__name__ = "OctetString"
_HicomSysMgrPhysNetId_Object = MibTableColumn
hicomSysMgrPhysNetId = _HicomSysMgrPhysNetId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 104),
    _HicomSysMgrPhysNetId_Type()
)
hicomSysMgrPhysNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSysMgrPhysNetId.setStatus("current")
_HicomSysMgrFlags_Type = Integer32
_HicomSysMgrFlags_Object = MibTableColumn
hicomSysMgrFlags = _HicomSysMgrFlags_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 105),
    _HicomSysMgrFlags_Type()
)
hicomSysMgrFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSysMgrFlags.setStatus("current")


class _HicomSysDiscTimeOutEvnt_Type(Integer32):
    """Custom type hicomSysDiscTimeOutEvnt based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 65535),
    )


_HicomSysDiscTimeOutEvnt_Type.__name__ = "Integer32"
_HicomSysDiscTimeOutEvnt_Object = MibTableColumn
hicomSysDiscTimeOutEvnt = _HicomSysDiscTimeOutEvnt_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 106),
    _HicomSysDiscTimeOutEvnt_Type()
)
hicomSysDiscTimeOutEvnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSysDiscTimeOutEvnt.setStatus("current")


class _HicomSysDiscAgedData_Type(Integer32):
    """Custom type hicomSysDiscAgedData based on Integer32"""
    defaultValue = 168

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(168, 65535),
    )


_HicomSysDiscAgedData_Type.__name__ = "Integer32"
_HicomSysDiscAgedData_Object = MibTableColumn
hicomSysDiscAgedData = _HicomSysDiscAgedData_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 107),
    _HicomSysDiscAgedData_Type()
)
hicomSysDiscAgedData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSysDiscAgedData.setStatus("current")


class _HicomSysDiscComType_Type(Integer32):
    """Custom type hicomSysDiscComType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addBatchJob", 1),
          ("online", 2))
    )


_HicomSysDiscComType_Type.__name__ = "Integer32"
_HicomSysDiscComType_Object = MibTableColumn
hicomSysDiscComType = _HicomSysDiscComType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 108),
    _HicomSysDiscComType_Type()
)
hicomSysDiscComType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSysDiscComType.setStatus("current")
_HicomSysAgentFlags_Type = Integer32
_HicomSysAgentFlags_Object = MibTableColumn
hicomSysAgentFlags = _HicomSysAgentFlags_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 3, 1, 109),
    _HicomSysAgentFlags_Type()
)
hicomSysAgentFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSysAgentFlags.setStatus("current")
_HicomSysSubagentLastMsgNo_Type = Integer32
_HicomSysSubagentLastMsgNo_Object = MibScalar
hicomSysSubagentLastMsgNo = _HicomSysSubagentLastMsgNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 4),
    _HicomSysSubagentLastMsgNo_Type()
)
hicomSysSubagentLastMsgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysSubagentLastMsgNo.setStatus("current")
_HicomSysSubagentLastMsgText_Type = DisplayString
_HicomSysSubagentLastMsgText_Object = MibScalar
hicomSysSubagentLastMsgText = _HicomSysSubagentLastMsgText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 5),
    _HicomSysSubagentLastMsgText_Type()
)
hicomSysSubagentLastMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSysSubagentLastMsgText.setStatus("current")
_HicomForeignSysTable_Object = MibTable
hicomForeignSysTable = _HicomForeignSysTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hicomForeignSysTable.setStatus("current")
_HicomForeignSysEntry_Object = MibTableRow
hicomForeignSysEntry = _HicomForeignSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 6, 1)
)
hicomForeignSysEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomForSysPhysNetId"),
    (0, "SIEMENS-PN-MIB", "hicomForSysNodeNo"),
)
if mibBuilder.loadTexts:
    hicomForeignSysEntry.setStatus("current")


class _HicomForSysPhysNetId_Type(OctetString):
    """Custom type hicomForSysPhysNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HicomForSysPhysNetId_Type.__name__ = "OctetString"
_HicomForSysPhysNetId_Object = MibTableColumn
hicomForSysPhysNetId = _HicomForSysPhysNetId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 6, 1, 1),
    _HicomForSysPhysNetId_Type()
)
hicomForSysPhysNetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomForSysPhysNetId.setStatus("current")
_HicomForSysNodeNo_Type = Integer32
_HicomForSysNodeNo_Object = MibTableColumn
hicomForSysNodeNo = _HicomForSysNodeNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 6, 1, 2),
    _HicomForSysNodeNo_Type()
)
hicomForSysNodeNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomForSysNodeNo.setStatus("current")


class _HicomForSysName_Type(OctetString):
    """Custom type hicomForSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HicomForSysName_Type.__name__ = "OctetString"
_HicomForSysName_Object = MibTableColumn
hicomForSysName = _HicomForSysName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 6, 1, 3),
    _HicomForSysName_Type()
)
hicomForSysName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hicomForSysName.setStatus("current")


class _HicomForSysNetId_Type(OctetString):
    """Custom type hicomForSysNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HicomForSysNetId_Type.__name__ = "OctetString"
_HicomForSysNetId_Object = MibTableColumn
hicomForSysNetId = _HicomForSysNetId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 6, 1, 4),
    _HicomForSysNetId_Type()
)
hicomForSysNetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hicomForSysNetId.setStatus("current")


class _HicomForSysSubNetId_Type(OctetString):
    """Custom type hicomForSysSubNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HicomForSysSubNetId_Type.__name__ = "OctetString"
_HicomForSysSubNetId_Object = MibTableColumn
hicomForSysSubNetId = _HicomForSysSubNetId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 6, 1, 5),
    _HicomForSysSubNetId_Type()
)
hicomForSysSubNetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hicomForSysSubNetId.setStatus("current")


class _HicomForSysProvNetId_Type(OctetString):
    """Custom type hicomForSysProvNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HicomForSysProvNetId_Type.__name__ = "OctetString"
_HicomForSysProvNetId_Object = MibTableColumn
hicomForSysProvNetId = _HicomForSysProvNetId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 6, 1, 6),
    _HicomForSysProvNetId_Type()
)
hicomForSysProvNetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hicomForSysProvNetId.setStatus("current")


class _HicomForSysProvSubNetId_Type(OctetString):
    """Custom type hicomForSysProvSubNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HicomForSysProvSubNetId_Type.__name__ = "OctetString"
_HicomForSysProvSubNetId_Object = MibTableColumn
hicomForSysProvSubNetId = _HicomForSysProvSubNetId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 6, 1, 7),
    _HicomForSysProvSubNetId_Type()
)
hicomForSysProvSubNetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hicomForSysProvSubNetId.setStatus("current")
_HicomForSysRowStat_Type = RowStatus
_HicomForSysRowStat_Object = MibTableColumn
hicomForSysRowStat = _HicomForSysRowStat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 1, 6, 1, 8),
    _HicomForSysRowStat_Type()
)
hicomForSysRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hicomForSysRowStat.setStatus("current")
_HicomAlarms_ObjectIdentity = ObjectIdentity
hicomAlarms = _HicomAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2)
)
_HicomAlarmsChanges_Type = Counter32
_HicomAlarmsChanges_Object = MibScalar
hicomAlarmsChanges = _HicomAlarmsChanges_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 1),
    _HicomAlarmsChanges_Type()
)
hicomAlarmsChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlarmsChanges.setStatus("current")
_HicomAlTable_Object = MibTable
hicomAlTable = _HicomAlTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hicomAlTable.setStatus("current")
_HicomAlEntry_Object = MibTableRow
hicomAlEntry = _HicomAlEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1)
)
hicomAlEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomAlFilter"),
    (0, "SIEMENS-PN-MIB", "hicomAlStatus"),
    (0, "SIEMENS-PN-MIB", "hicomAlPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomAlGroup"),
    (0, "SIEMENS-PN-MIB", "hicomAlSubId"),
    (0, "SIEMENS-PN-MIB", "hicomAlPriority"),
    (0, "SIEMENS-PN-MIB", "hicomAlAbsMod"),
)
if mibBuilder.loadTexts:
    hicomAlEntry.setStatus("current")
_HicomAlFilter_Type = AlarmFilterStates
_HicomAlFilter_Object = MibTableColumn
hicomAlFilter = _HicomAlFilter_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 1),
    _HicomAlFilter_Type()
)
hicomAlFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlFilter.setStatus("current")


class _HicomAlStatus_Type(Integer32):
    """Custom type hicomAlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("set", 2))
    )


_HicomAlStatus_Type.__name__ = "Integer32"
_HicomAlStatus_Object = MibTableColumn
hicomAlStatus = _HicomAlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 2),
    _HicomAlStatus_Type()
)
hicomAlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlStatus.setStatus("current")
_HicomAlPabxId_Type = Integer32
_HicomAlPabxId_Object = MibTableColumn
hicomAlPabxId = _HicomAlPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 3),
    _HicomAlPabxId_Type()
)
hicomAlPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlPabxId.setStatus("current")
_HicomAlGroup_Type = Integer32
_HicomAlGroup_Object = MibTableColumn
hicomAlGroup = _HicomAlGroup_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 4),
    _HicomAlGroup_Type()
)
hicomAlGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlGroup.setStatus("current")
_HicomAlSubId_Type = Integer32
_HicomAlSubId_Object = MibTableColumn
hicomAlSubId = _HicomAlSubId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 5),
    _HicomAlSubId_Type()
)
hicomAlSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlSubId.setStatus("current")
_HicomAlPriority_Type = AlarmPriorities
_HicomAlPriority_Object = MibTableColumn
hicomAlPriority = _HicomAlPriority_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 6),
    _HicomAlPriority_Type()
)
hicomAlPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlPriority.setStatus("current")
_HicomAlAbsMod_Type = DisplayString
_HicomAlAbsMod_Object = MibTableColumn
hicomAlAbsMod = _HicomAlAbsMod_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 7),
    _HicomAlAbsMod_Type()
)
hicomAlAbsMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlAbsMod.setStatus("current")
_HicomAlTimDat_Type = Integer32
_HicomAlTimDat_Object = MibTableColumn
hicomAlTimDat = _HicomAlTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 8),
    _HicomAlTimDat_Type()
)
hicomAlTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlTimDat.setStatus("current")
_HicomAlName_Type = DisplayString
_HicomAlName_Object = MibTableColumn
hicomAlName = _HicomAlName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 9),
    _HicomAlName_Type()
)
hicomAlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlName.setStatus("current")


class _HicomAlReset_Type(Integer32):
    """Custom type hicomAlReset based on Integer32"""
    defaultValue = 1

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
        *(("busy", 3),
          ("error", 2),
          ("finerr", 5),
          ("finok", 4),
          ("init", 1))
    )


_HicomAlReset_Type.__name__ = "Integer32"
_HicomAlReset_Object = MibTableColumn
hicomAlReset = _HicomAlReset_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 10),
    _HicomAlReset_Type()
)
hicomAlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomAlReset.setStatus("current")
_HicomAlTimOldDat_Type = Integer32
_HicomAlTimOldDat_Object = MibTableColumn
hicomAlTimOldDat = _HicomAlTimOldDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 11),
    _HicomAlTimOldDat_Type()
)
hicomAlTimOldDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlTimOldDat.setStatus("current")
_HicomAlArrivalTimDat_Type = Integer32
_HicomAlArrivalTimDat_Object = MibTableColumn
hicomAlArrivalTimDat = _HicomAlArrivalTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 2, 1, 12),
    _HicomAlArrivalTimDat_Type()
)
hicomAlArrivalTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlArrivalTimDat.setStatus("current")
_HicomAlFiltConfTable_Object = MibTable
hicomAlFiltConfTable = _HicomAlFiltConfTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hicomAlFiltConfTable.setStatus("current")
_HicomAlFiltConfEntry_Object = MibTableRow
hicomAlFiltConfEntry = _HicomAlFiltConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 3, 1)
)
hicomAlFiltConfEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomAlFiltConfPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomAlFiltConfGroup"),
    (0, "SIEMENS-PN-MIB", "hicomAlFiltConfSubId"),
    (0, "SIEMENS-PN-MIB", "hicomAlFiltConfPriority"),
)
if mibBuilder.loadTexts:
    hicomAlFiltConfEntry.setStatus("current")
_HicomAlFiltConfPabxId_Type = Integer32
_HicomAlFiltConfPabxId_Object = MibTableColumn
hicomAlFiltConfPabxId = _HicomAlFiltConfPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 3, 1, 1),
    _HicomAlFiltConfPabxId_Type()
)
hicomAlFiltConfPabxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomAlFiltConfPabxId.setStatus("current")
_HicomAlFiltConfGroup_Type = Integer32
_HicomAlFiltConfGroup_Object = MibTableColumn
hicomAlFiltConfGroup = _HicomAlFiltConfGroup_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 3, 1, 2),
    _HicomAlFiltConfGroup_Type()
)
hicomAlFiltConfGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomAlFiltConfGroup.setStatus("current")
_HicomAlFiltConfSubId_Type = Integer32
_HicomAlFiltConfSubId_Object = MibTableColumn
hicomAlFiltConfSubId = _HicomAlFiltConfSubId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 3, 1, 3),
    _HicomAlFiltConfSubId_Type()
)
hicomAlFiltConfSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomAlFiltConfSubId.setStatus("current")
_HicomAlFiltConfPriority_Type = AlarmPriorities
_HicomAlFiltConfPriority_Object = MibTableColumn
hicomAlFiltConfPriority = _HicomAlFiltConfPriority_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 3, 1, 4),
    _HicomAlFiltConfPriority_Type()
)
hicomAlFiltConfPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomAlFiltConfPriority.setStatus("current")
_HicomAlFiltConfSwitch_Type = AlarmFilterStates
_HicomAlFiltConfSwitch_Object = MibTableColumn
hicomAlFiltConfSwitch = _HicomAlFiltConfSwitch_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 3, 1, 5),
    _HicomAlFiltConfSwitch_Type()
)
hicomAlFiltConfSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hicomAlFiltConfSwitch.setStatus("current")
_HicomAlFiltConfRowStat_Type = RowStatus
_HicomAlFiltConfRowStat_Object = MibTableColumn
hicomAlFiltConfRowStat = _HicomAlFiltConfRowStat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 3, 1, 6),
    _HicomAlFiltConfRowStat_Type()
)
hicomAlFiltConfRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hicomAlFiltConfRowStat.setStatus("current")
_HicomAlarmSubagentLastMsgNo_Type = Integer32
_HicomAlarmSubagentLastMsgNo_Object = MibScalar
hicomAlarmSubagentLastMsgNo = _HicomAlarmSubagentLastMsgNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 4),
    _HicomAlarmSubagentLastMsgNo_Type()
)
hicomAlarmSubagentLastMsgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlarmSubagentLastMsgNo.setStatus("current")
_HicomAlarmSubagentLastMsgText_Type = DisplayString
_HicomAlarmSubagentLastMsgText_Object = MibScalar
hicomAlarmSubagentLastMsgText = _HicomAlarmSubagentLastMsgText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 5),
    _HicomAlarmSubagentLastMsgText_Type()
)
hicomAlarmSubagentLastMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlarmSubagentLastMsgText.setStatus("current")
_HicomAlMirrorUploadTable_Object = MibTable
hicomAlMirrorUploadTable = _HicomAlMirrorUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hicomAlMirrorUploadTable.setStatus("current")
_HicomAlMirrorUploadEntry_Object = MibTableRow
hicomAlMirrorUploadEntry = _HicomAlMirrorUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 6, 1)
)
hicomAlMirrorUploadEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomAlMirrorUploadPabxId"),
)
if mibBuilder.loadTexts:
    hicomAlMirrorUploadEntry.setStatus("current")
_HicomAlMirrorUploadPabxId_Type = Integer32
_HicomAlMirrorUploadPabxId_Object = MibTableColumn
hicomAlMirrorUploadPabxId = _HicomAlMirrorUploadPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 6, 1, 1),
    _HicomAlMirrorUploadPabxId_Type()
)
hicomAlMirrorUploadPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlMirrorUploadPabxId.setStatus("current")
_HicomAlMirrorUploadMnemonic_Type = DisplayString
_HicomAlMirrorUploadMnemonic_Object = MibTableColumn
hicomAlMirrorUploadMnemonic = _HicomAlMirrorUploadMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 6, 1, 2),
    _HicomAlMirrorUploadMnemonic_Type()
)
hicomAlMirrorUploadMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlMirrorUploadMnemonic.setStatus("current")


class _HicomAlMirrorUploadState_Type(Integer32):
    """Custom type hicomAlMirrorUploadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("done", 1),
          ("error", 2))
    )


_HicomAlMirrorUploadState_Type.__name__ = "Integer32"
_HicomAlMirrorUploadState_Object = MibTableColumn
hicomAlMirrorUploadState = _HicomAlMirrorUploadState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 6, 1, 3),
    _HicomAlMirrorUploadState_Type()
)
hicomAlMirrorUploadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomAlMirrorUploadState.setStatus("current")
_HicomAlMirrorUploadStartTimDat_Type = DisplayString
_HicomAlMirrorUploadStartTimDat_Object = MibTableColumn
hicomAlMirrorUploadStartTimDat = _HicomAlMirrorUploadStartTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 6, 1, 4),
    _HicomAlMirrorUploadStartTimDat_Type()
)
hicomAlMirrorUploadStartTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlMirrorUploadStartTimDat.setStatus("current")
_HicomAlMirrorUploadErrorTimDat_Type = DisplayString
_HicomAlMirrorUploadErrorTimDat_Object = MibTableColumn
hicomAlMirrorUploadErrorTimDat = _HicomAlMirrorUploadErrorTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 2, 6, 1, 5),
    _HicomAlMirrorUploadErrorTimDat_Type()
)
hicomAlMirrorUploadErrorTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlMirrorUploadErrorTimDat.setStatus("current")
_HicomErrors_ObjectIdentity = ObjectIdentity
hicomErrors = _HicomErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3)
)
_HicomErrorTable_Object = MibTable
hicomErrorTable = _HicomErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hicomErrorTable.setStatus("current")
_HicomErrorEntry_Object = MibTableRow
hicomErrorEntry = _HicomErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1)
)
hicomErrorEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomErrorPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomErrorAlGroup"),
    (0, "SIEMENS-PN-MIB", "hicomErrorAlSubId"),
    (0, "SIEMENS-PN-MIB", "hicomErrorSerialNo"),
)
if mibBuilder.loadTexts:
    hicomErrorEntry.setStatus("current")
_HicomErrorPabxId_Type = Integer32
_HicomErrorPabxId_Object = MibTableColumn
hicomErrorPabxId = _HicomErrorPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 1),
    _HicomErrorPabxId_Type()
)
hicomErrorPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorPabxId.setStatus("current")
_HicomErrorAlGroup_Type = Integer32
_HicomErrorAlGroup_Object = MibTableColumn
hicomErrorAlGroup = _HicomErrorAlGroup_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 2),
    _HicomErrorAlGroup_Type()
)
hicomErrorAlGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorAlGroup.setStatus("current")
_HicomErrorAlSubId_Type = Integer32
_HicomErrorAlSubId_Object = MibTableColumn
hicomErrorAlSubId = _HicomErrorAlSubId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 3),
    _HicomErrorAlSubId_Type()
)
hicomErrorAlSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorAlSubId.setStatus("current")
_HicomErrorSerialNo_Type = Integer32
_HicomErrorSerialNo_Object = MibTableColumn
hicomErrorSerialNo = _HicomErrorSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 4),
    _HicomErrorSerialNo_Type()
)
hicomErrorSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorSerialNo.setStatus("current")
_HicomErrorMsgId_Type = DisplayString
_HicomErrorMsgId_Object = MibTableColumn
hicomErrorMsgId = _HicomErrorMsgId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 5),
    _HicomErrorMsgId_Type()
)
hicomErrorMsgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorMsgId.setStatus("current")
_HicomErrorPriority_Type = DisplayString
_HicomErrorPriority_Object = MibTableColumn
hicomErrorPriority = _HicomErrorPriority_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 6),
    _HicomErrorPriority_Type()
)
hicomErrorPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorPriority.setStatus("current")
_HicomErrorAction_Type = DisplayString
_HicomErrorAction_Object = MibTableColumn
hicomErrorAction = _HicomErrorAction_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 7),
    _HicomErrorAction_Type()
)
hicomErrorAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorAction.setStatus("current")
_HicomErrorAbsMod_Type = DisplayString
_HicomErrorAbsMod_Object = MibTableColumn
hicomErrorAbsMod = _HicomErrorAbsMod_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 8),
    _HicomErrorAbsMod_Type()
)
hicomErrorAbsMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorAbsMod.setStatus("current")
_HicomErrorEvent_Type = DisplayString
_HicomErrorEvent_Object = MibTableColumn
hicomErrorEvent = _HicomErrorEvent_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 9),
    _HicomErrorEvent_Type()
)
hicomErrorEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorEvent.setStatus("current")
_HicomErrorSubevent_Type = DisplayString
_HicomErrorSubevent_Object = MibTableColumn
hicomErrorSubevent = _HicomErrorSubevent_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 10),
    _HicomErrorSubevent_Type()
)
hicomErrorSubevent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorSubevent.setStatus("current")
_HicomErrorCardRef_Type = DisplayString
_HicomErrorCardRef_Object = MibTableColumn
hicomErrorCardRef = _HicomErrorCardRef_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 11),
    _HicomErrorCardRef_Type()
)
hicomErrorCardRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorCardRef.setStatus("current")
_HicomErrorBoardVersion_Type = DisplayString
_HicomErrorBoardVersion_Object = MibTableColumn
hicomErrorBoardVersion = _HicomErrorBoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 12),
    _HicomErrorBoardVersion_Type()
)
hicomErrorBoardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorBoardVersion.setStatus("current")
_HicomErrorFwType_Type = DisplayString
_HicomErrorFwType_Object = MibTableColumn
hicomErrorFwType = _HicomErrorFwType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 13),
    _HicomErrorFwType_Type()
)
hicomErrorFwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorFwType.setStatus("current")
_HicomErrorTimDat_Type = Integer32
_HicomErrorTimDat_Object = MibTableColumn
hicomErrorTimDat = _HicomErrorTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 14),
    _HicomErrorTimDat_Type()
)
hicomErrorTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorTimDat.setStatus("current")
_HicomErrorOrigText_Type = DisplayString
_HicomErrorOrigText_Object = MibTableColumn
hicomErrorOrigText = _HicomErrorOrigText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 3, 1, 1, 15),
    _HicomErrorOrigText_Type()
)
hicomErrorOrigText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrorOrigText.setStatus("current")
_HicomAlConf_ObjectIdentity = ObjectIdentity
hicomAlConf = _HicomAlConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4)
)
_HicomAlConfig_ObjectIdentity = ObjectIdentity
hicomAlConfig = _HicomAlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1)
)
_HicomAlConfTable_Object = MibTable
hicomAlConfTable = _HicomAlConfTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hicomAlConfTable.setStatus("current")
_HicomAlConfEntry_Object = MibTableRow
hicomAlConfEntry = _HicomAlConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1)
)
hicomAlConfEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomAlConfPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfAlGroup"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfAlSubId"),
)
if mibBuilder.loadTexts:
    hicomAlConfEntry.setStatus("current")
_HicomAlConfPabxId_Type = Integer32
_HicomAlConfPabxId_Object = MibTableColumn
hicomAlConfPabxId = _HicomAlConfPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1, 1),
    _HicomAlConfPabxId_Type()
)
hicomAlConfPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfPabxId.setStatus("current")
_HicomAlConfAlGroup_Type = Integer32
_HicomAlConfAlGroup_Object = MibTableColumn
hicomAlConfAlGroup = _HicomAlConfAlGroup_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1, 2),
    _HicomAlConfAlGroup_Type()
)
hicomAlConfAlGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfAlGroup.setStatus("current")
_HicomAlConfAlSubId_Type = Integer32
_HicomAlConfAlSubId_Object = MibTableColumn
hicomAlConfAlSubId = _HicomAlConfAlSubId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1, 3),
    _HicomAlConfAlSubId_Type()
)
hicomAlConfAlSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfAlSubId.setStatus("current")
_HicomAlConfName_Type = DisplayString
_HicomAlConfName_Object = MibTableColumn
hicomAlConfName = _HicomAlConfName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1, 4),
    _HicomAlConfName_Type()
)
hicomAlConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfName.setStatus("current")
_HicomAlConfThreshold1_Type = Integer32
_HicomAlConfThreshold1_Object = MibTableColumn
hicomAlConfThreshold1 = _HicomAlConfThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1, 5),
    _HicomAlConfThreshold1_Type()
)
hicomAlConfThreshold1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfThreshold1.setStatus("current")
_HicomAlConfThreshold2_Type = Integer32
_HicomAlConfThreshold2_Object = MibTableColumn
hicomAlConfThreshold2 = _HicomAlConfThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1, 6),
    _HicomAlConfThreshold2_Type()
)
hicomAlConfThreshold2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfThreshold2.setStatus("current")
_HicomAlConfTime1_Type = Integer32
_HicomAlConfTime1_Object = MibTableColumn
hicomAlConfTime1 = _HicomAlConfTime1_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1, 7),
    _HicomAlConfTime1_Type()
)
hicomAlConfTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfTime1.setStatus("current")
_HicomAlConfTime2_Type = Integer32
_HicomAlConfTime2_Object = MibTableColumn
hicomAlConfTime2 = _HicomAlConfTime2_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1, 8),
    _HicomAlConfTime2_Type()
)
hicomAlConfTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfTime2.setStatus("current")
_HicomAlConfTimeH_Type = Integer32
_HicomAlConfTimeH_Object = MibTableColumn
hicomAlConfTimeH = _HicomAlConfTimeH_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1, 9),
    _HicomAlConfTimeH_Type()
)
hicomAlConfTimeH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfTimeH.setStatus("current")
_HicomAlConfBase_Type = Integer32
_HicomAlConfBase_Object = MibTableColumn
hicomAlConfBase = _HicomAlConfBase_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 1, 1, 10),
    _HicomAlConfBase_Type()
)
hicomAlConfBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfBase.setStatus("current")
_HicomAlConfPersonTable_Object = MibTable
hicomAlConfPersonTable = _HicomAlConfPersonTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hicomAlConfPersonTable.setStatus("current")
_HicomAlConfPersonEntry_Object = MibTableRow
hicomAlConfPersonEntry = _HicomAlConfPersonEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 2, 1)
)
hicomAlConfPersonEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomAlConfPersonPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfPersonAlGroup"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfPersonAlSubId"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfPersonExtNo"),
)
if mibBuilder.loadTexts:
    hicomAlConfPersonEntry.setStatus("current")
_HicomAlConfPersonPabxId_Type = Integer32
_HicomAlConfPersonPabxId_Object = MibTableColumn
hicomAlConfPersonPabxId = _HicomAlConfPersonPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 2, 1, 1),
    _HicomAlConfPersonPabxId_Type()
)
hicomAlConfPersonPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfPersonPabxId.setStatus("current")
_HicomAlConfPersonAlGroup_Type = Integer32
_HicomAlConfPersonAlGroup_Object = MibTableColumn
hicomAlConfPersonAlGroup = _HicomAlConfPersonAlGroup_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 2, 1, 2),
    _HicomAlConfPersonAlGroup_Type()
)
hicomAlConfPersonAlGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfPersonAlGroup.setStatus("current")
_HicomAlConfPersonAlSubId_Type = Integer32
_HicomAlConfPersonAlSubId_Object = MibTableColumn
hicomAlConfPersonAlSubId = _HicomAlConfPersonAlSubId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 2, 1, 3),
    _HicomAlConfPersonAlSubId_Type()
)
hicomAlConfPersonAlSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfPersonAlSubId.setStatus("current")
_HicomAlConfPersonExtNo_Type = DisplayString
_HicomAlConfPersonExtNo_Object = MibTableColumn
hicomAlConfPersonExtNo = _HicomAlConfPersonExtNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 2, 1, 4),
    _HicomAlConfPersonExtNo_Type()
)
hicomAlConfPersonExtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfPersonExtNo.setStatus("current")
_HicomAlConfTargetTable_Object = MibTable
hicomAlConfTargetTable = _HicomAlConfTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hicomAlConfTargetTable.setStatus("current")
_HicomAlConfTargetEntry_Object = MibTableRow
hicomAlConfTargetEntry = _HicomAlConfTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 3, 1)
)
hicomAlConfTargetEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomAlConfTargetPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfTargetAlGroup"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfTargetAlSubId"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfTargetLtg"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfTargetLtu"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfTargetSlot"),
    (0, "SIEMENS-PN-MIB", "hicomAlConfTargetTrunkNo"),
)
if mibBuilder.loadTexts:
    hicomAlConfTargetEntry.setStatus("current")
_HicomAlConfTargetPabxId_Type = Integer32
_HicomAlConfTargetPabxId_Object = MibTableColumn
hicomAlConfTargetPabxId = _HicomAlConfTargetPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 3, 1, 1),
    _HicomAlConfTargetPabxId_Type()
)
hicomAlConfTargetPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfTargetPabxId.setStatus("current")
_HicomAlConfTargetAlGroup_Type = Integer32
_HicomAlConfTargetAlGroup_Object = MibTableColumn
hicomAlConfTargetAlGroup = _HicomAlConfTargetAlGroup_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 3, 1, 2),
    _HicomAlConfTargetAlGroup_Type()
)
hicomAlConfTargetAlGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfTargetAlGroup.setStatus("current")
_HicomAlConfTargetAlSubId_Type = Integer32
_HicomAlConfTargetAlSubId_Object = MibTableColumn
hicomAlConfTargetAlSubId = _HicomAlConfTargetAlSubId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 3, 1, 3),
    _HicomAlConfTargetAlSubId_Type()
)
hicomAlConfTargetAlSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfTargetAlSubId.setStatus("current")
_HicomAlConfTargetLtg_Type = Integer32
_HicomAlConfTargetLtg_Object = MibTableColumn
hicomAlConfTargetLtg = _HicomAlConfTargetLtg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 3, 1, 4),
    _HicomAlConfTargetLtg_Type()
)
hicomAlConfTargetLtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfTargetLtg.setStatus("current")
_HicomAlConfTargetLtu_Type = Integer32
_HicomAlConfTargetLtu_Object = MibTableColumn
hicomAlConfTargetLtu = _HicomAlConfTargetLtu_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 3, 1, 5),
    _HicomAlConfTargetLtu_Type()
)
hicomAlConfTargetLtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfTargetLtu.setStatus("current")
_HicomAlConfTargetSlot_Type = Integer32
_HicomAlConfTargetSlot_Object = MibTableColumn
hicomAlConfTargetSlot = _HicomAlConfTargetSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 3, 1, 6),
    _HicomAlConfTargetSlot_Type()
)
hicomAlConfTargetSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfTargetSlot.setStatus("current")
_HicomAlConfTargetTrunkNo_Type = Integer32
_HicomAlConfTargetTrunkNo_Object = MibTableColumn
hicomAlConfTargetTrunkNo = _HicomAlConfTargetTrunkNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 1, 3, 1, 7),
    _HicomAlConfTargetTrunkNo_Type()
)
hicomAlConfTargetTrunkNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfTargetTrunkNo.setStatus("current")
_HicomErrAlConfInfo_ObjectIdentity = ObjectIdentity
hicomErrAlConfInfo = _HicomErrAlConfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 2)
)
_HicomErrAlConfSubagentLastMsgNo_Type = Integer32
_HicomErrAlConfSubagentLastMsgNo_Object = MibScalar
hicomErrAlConfSubagentLastMsgNo = _HicomErrAlConfSubagentLastMsgNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 2, 1),
    _HicomErrAlConfSubagentLastMsgNo_Type()
)
hicomErrAlConfSubagentLastMsgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrAlConfSubagentLastMsgNo.setStatus("current")
_HicomErrAlConfSubagentLastMsgText_Type = DisplayString
_HicomErrAlConfSubagentLastMsgText_Object = MibScalar
hicomErrAlConfSubagentLastMsgText = _HicomErrAlConfSubagentLastMsgText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 2, 2),
    _HicomErrAlConfSubagentLastMsgText_Type()
)
hicomErrAlConfSubagentLastMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomErrAlConfSubagentLastMsgText.setStatus("current")
_HicomErrAlConfResultData_Type = Integer32
_HicomErrAlConfResultData_Object = MibScalar
hicomErrAlConfResultData = _HicomErrAlConfResultData_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 2, 3),
    _HicomErrAlConfResultData_Type()
)
hicomErrAlConfResultData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomErrAlConfResultData.setStatus("current")
_HicomAlConfDiscovery_ObjectIdentity = ObjectIdentity
hicomAlConfDiscovery = _HicomAlConfDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 3)
)
_HicomAlConfChanges_Type = Counter32
_HicomAlConfChanges_Object = MibScalar
hicomAlConfChanges = _HicomAlConfChanges_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 3, 1),
    _HicomAlConfChanges_Type()
)
hicomAlConfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfChanges.setStatus("current")
_HicomAlConfDiscovTable_Object = MibTable
hicomAlConfDiscovTable = _HicomAlConfDiscovTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    hicomAlConfDiscovTable.setStatus("current")
_HicomAlConfDiscovEntry_Object = MibTableRow
hicomAlConfDiscovEntry = _HicomAlConfDiscovEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 3, 2, 1)
)
hicomAlConfDiscovEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomAlConfDiscovPabxId"),
)
if mibBuilder.loadTexts:
    hicomAlConfDiscovEntry.setStatus("current")
_HicomAlConfDiscovPabxId_Type = Integer32
_HicomAlConfDiscovPabxId_Object = MibTableColumn
hicomAlConfDiscovPabxId = _HicomAlConfDiscovPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 3, 2, 1, 1),
    _HicomAlConfDiscovPabxId_Type()
)
hicomAlConfDiscovPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfDiscovPabxId.setStatus("current")
_HicomAlConfDiscovPabxMnemonic_Type = DisplayString
_HicomAlConfDiscovPabxMnemonic_Object = MibTableColumn
hicomAlConfDiscovPabxMnemonic = _HicomAlConfDiscovPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 3, 2, 1, 2),
    _HicomAlConfDiscovPabxMnemonic_Type()
)
hicomAlConfDiscovPabxMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfDiscovPabxMnemonic.setStatus("current")
_HicomAlConfDiscovStatus_Type = DiscoveryStates
_HicomAlConfDiscovStatus_Object = MibTableColumn
hicomAlConfDiscovStatus = _HicomAlConfDiscovStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 3, 2, 1, 3),
    _HicomAlConfDiscovStatus_Type()
)
hicomAlConfDiscovStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomAlConfDiscovStatus.setStatus("current")
_HicomAlConfDiscovMode_Type = DiscoveryModes
_HicomAlConfDiscovMode_Object = MibTableColumn
hicomAlConfDiscovMode = _HicomAlConfDiscovMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 3, 2, 1, 4),
    _HicomAlConfDiscovMode_Type()
)
hicomAlConfDiscovMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomAlConfDiscovMode.setStatus("current")
_HicomAlConfDiscovTimDat_Type = DisplayString
_HicomAlConfDiscovTimDat_Object = MibTableColumn
hicomAlConfDiscovTimDat = _HicomAlConfDiscovTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 3, 2, 1, 5),
    _HicomAlConfDiscovTimDat_Type()
)
hicomAlConfDiscovTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfDiscovTimDat.setStatus("current")
_HicomAlConfDiscovErrTimDat_Type = DisplayString
_HicomAlConfDiscovErrTimDat_Object = MibTableColumn
hicomAlConfDiscovErrTimDat = _HicomAlConfDiscovErrTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 4, 3, 2, 1, 6),
    _HicomAlConfDiscovErrTimDat_Type()
)
hicomAlConfDiscovErrTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomAlConfDiscovErrTimDat.setStatus("current")
_HicomSoft_ObjectIdentity = ObjectIdentity
hicomSoft = _HicomSoft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5)
)
_HicomSoftAps_ObjectIdentity = ObjectIdentity
hicomSoftAps = _HicomSoftAps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1)
)
_HicomSoftApsTable_Object = MibTable
hicomSoftApsTable = _HicomSoftApsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hicomSoftApsTable.setStatus("current")
_HicomSoftApsEntry_Object = MibTableRow
hicomSoftApsEntry = _HicomSoftApsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 1, 1)
)
hicomSoftApsEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomSoftApsPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomSoftApsID"),
)
if mibBuilder.loadTexts:
    hicomSoftApsEntry.setStatus("current")
_HicomSoftApsPabxId_Type = Integer32
_HicomSoftApsPabxId_Object = MibTableColumn
hicomSoftApsPabxId = _HicomSoftApsPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 1, 1, 1),
    _HicomSoftApsPabxId_Type()
)
hicomSoftApsPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftApsPabxId.setStatus("current")
_HicomSoftApsID_Type = OctetString
_HicomSoftApsID_Object = MibTableColumn
hicomSoftApsID = _HicomSoftApsID_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 1, 1, 2),
    _HicomSoftApsID_Type()
)
hicomSoftApsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftApsID.setStatus("current")
_HicomSoftApsPartNo_Type = DisplayString
_HicomSoftApsPartNo_Object = MibTableColumn
hicomSoftApsPartNo = _HicomSoftApsPartNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 1, 1, 3),
    _HicomSoftApsPartNo_Type()
)
hicomSoftApsPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftApsPartNo.setStatus("current")
_HicomSoftPatchTable_Object = MibTable
hicomSoftPatchTable = _HicomSoftPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hicomSoftPatchTable.setStatus("current")
_HicomSoftPatchEntry_Object = MibTableRow
hicomSoftPatchEntry = _HicomSoftPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 2, 1)
)
hicomSoftPatchEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomSoftPatchPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomSoftPatchNo"),
)
if mibBuilder.loadTexts:
    hicomSoftPatchEntry.setStatus("current")
_HicomSoftPatchPabxId_Type = Integer32
_HicomSoftPatchPabxId_Object = MibTableColumn
hicomSoftPatchPabxId = _HicomSoftPatchPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 2, 1, 1),
    _HicomSoftPatchPabxId_Type()
)
hicomSoftPatchPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftPatchPabxId.setStatus("current")
_HicomSoftPatchNo_Type = OctetString
_HicomSoftPatchNo_Object = MibTableColumn
hicomSoftPatchNo = _HicomSoftPatchNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 2, 1, 2),
    _HicomSoftPatchNo_Type()
)
hicomSoftPatchNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftPatchNo.setStatus("current")
_HicomSoftPatchHWMod_Type = DisplayString
_HicomSoftPatchHWMod_Object = MibTableColumn
hicomSoftPatchHWMod = _HicomSoftPatchHWMod_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 2, 1, 3),
    _HicomSoftPatchHWMod_Type()
)
hicomSoftPatchHWMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftPatchHWMod.setStatus("current")
_HicomSoftPatchActType_Type = DisplayString
_HicomSoftPatchActType_Object = MibTableColumn
hicomSoftPatchActType = _HicomSoftPatchActType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 2, 1, 4),
    _HicomSoftPatchActType_Type()
)
hicomSoftPatchActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftPatchActType.setStatus("current")
_HicomSoftPatchGroup_Type = DisplayString
_HicomSoftPatchGroup_Object = MibTableColumn
hicomSoftPatchGroup = _HicomSoftPatchGroup_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 1, 2, 1, 5),
    _HicomSoftPatchGroup_Type()
)
hicomSoftPatchGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftPatchGroup.setStatus("current")
_HicomSoftInfo_ObjectIdentity = ObjectIdentity
hicomSoftInfo = _HicomSoftInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 2)
)
_HicomSoftSubagentLastMsgNo_Type = Integer32
_HicomSoftSubagentLastMsgNo_Object = MibScalar
hicomSoftSubagentLastMsgNo = _HicomSoftSubagentLastMsgNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 2, 1),
    _HicomSoftSubagentLastMsgNo_Type()
)
hicomSoftSubagentLastMsgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftSubagentLastMsgNo.setStatus("current")
_HicomSoftSubagentLastMsgText_Type = OctetString
_HicomSoftSubagentLastMsgText_Object = MibScalar
hicomSoftSubagentLastMsgText = _HicomSoftSubagentLastMsgText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 2, 2),
    _HicomSoftSubagentLastMsgText_Type()
)
hicomSoftSubagentLastMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftSubagentLastMsgText.setStatus("current")
_HicomSoftResultData_Type = Integer32
_HicomSoftResultData_Object = MibScalar
hicomSoftResultData = _HicomSoftResultData_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 2, 3),
    _HicomSoftResultData_Type()
)
hicomSoftResultData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSoftResultData.setStatus("current")
_HicomSoftDiscovery_ObjectIdentity = ObjectIdentity
hicomSoftDiscovery = _HicomSoftDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 3)
)
_HicomSoftChanges_Type = Counter32
_HicomSoftChanges_Object = MibScalar
hicomSoftChanges = _HicomSoftChanges_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 3, 1),
    _HicomSoftChanges_Type()
)
hicomSoftChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftChanges.setStatus("current")
_HicomSoftDiscovTable_Object = MibTable
hicomSoftDiscovTable = _HicomSoftDiscovTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    hicomSoftDiscovTable.setStatus("current")
_HicomSoftDiscovEntry_Object = MibTableRow
hicomSoftDiscovEntry = _HicomSoftDiscovEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 3, 2, 1)
)
hicomSoftDiscovEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomSoftDiscovPabxId"),
)
if mibBuilder.loadTexts:
    hicomSoftDiscovEntry.setStatus("current")
_HicomSoftDiscovPabxId_Type = Integer32
_HicomSoftDiscovPabxId_Object = MibTableColumn
hicomSoftDiscovPabxId = _HicomSoftDiscovPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 3, 2, 1, 1),
    _HicomSoftDiscovPabxId_Type()
)
hicomSoftDiscovPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftDiscovPabxId.setStatus("current")
_HicomSoftDiscovPabxMnemonic_Type = DisplayString
_HicomSoftDiscovPabxMnemonic_Object = MibTableColumn
hicomSoftDiscovPabxMnemonic = _HicomSoftDiscovPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 3, 2, 1, 2),
    _HicomSoftDiscovPabxMnemonic_Type()
)
hicomSoftDiscovPabxMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftDiscovPabxMnemonic.setStatus("current")
_HicomSoftDiscovStatus_Type = DiscoveryStates
_HicomSoftDiscovStatus_Object = MibTableColumn
hicomSoftDiscovStatus = _HicomSoftDiscovStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 3, 2, 1, 3),
    _HicomSoftDiscovStatus_Type()
)
hicomSoftDiscovStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSoftDiscovStatus.setStatus("current")
_HicomSoftDiscovMode_Type = DiscoveryModes
_HicomSoftDiscovMode_Object = MibTableColumn
hicomSoftDiscovMode = _HicomSoftDiscovMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 3, 2, 1, 4),
    _HicomSoftDiscovMode_Type()
)
hicomSoftDiscovMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSoftDiscovMode.setStatus("current")
_HicomSoftDiscovTimDat_Type = DisplayString
_HicomSoftDiscovTimDat_Object = MibTableColumn
hicomSoftDiscovTimDat = _HicomSoftDiscovTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 3, 2, 1, 5),
    _HicomSoftDiscovTimDat_Type()
)
hicomSoftDiscovTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftDiscovTimDat.setStatus("current")
_HicomSoftDiscovErrTimDat_Type = DisplayString
_HicomSoftDiscovErrTimDat_Object = MibTableColumn
hicomSoftDiscovErrTimDat = _HicomSoftDiscovErrTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 5, 3, 2, 1, 6),
    _HicomSoftDiscovErrTimDat_Type()
)
hicomSoftDiscovErrTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSoftDiscovErrTimDat.setStatus("current")
_HicomHard_ObjectIdentity = ObjectIdentity
hicomHard = _HicomHard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6)
)
_HicomCabinets_ObjectIdentity = ObjectIdentity
hicomCabinets = _HicomCabinets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1)
)
_HicomCabTable_Object = MibTable
hicomCabTable = _HicomCabTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hicomCabTable.setStatus("current")
_HicomCabEntry_Object = MibTableRow
hicomCabEntry = _HicomCabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 1, 1)
)
hicomCabEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomCabPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomCabAddr"),
)
if mibBuilder.loadTexts:
    hicomCabEntry.setStatus("current")
_HicomCabPabxId_Type = Integer32
_HicomCabPabxId_Object = MibTableColumn
hicomCabPabxId = _HicomCabPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 1, 1, 1),
    _HicomCabPabxId_Type()
)
hicomCabPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCabPabxId.setStatus("current")
_HicomCabAddr_Type = OctetString
_HicomCabAddr_Object = MibTableColumn
hicomCabAddr = _HicomCabAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 1, 1, 2),
    _HicomCabAddr_Type()
)
hicomCabAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCabAddr.setStatus("current")
_HicomCabType_Type = DisplayString
_HicomCabType_Object = MibTableColumn
hicomCabType = _HicomCabType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 1, 1, 3),
    _HicomCabType_Type()
)
hicomCabType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCabType.setStatus("current")
_HicomCabPartNo_Type = DisplayString
_HicomCabPartNo_Object = MibTableColumn
hicomCabPartNo = _HicomCabPartNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 1, 1, 4),
    _HicomCabPartNo_Type()
)
hicomCabPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCabPartNo.setStatus("current")
_HicomCabNumShelves_Type = Integer32
_HicomCabNumShelves_Object = MibTableColumn
hicomCabNumShelves = _HicomCabNumShelves_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 1, 1, 5),
    _HicomCabNumShelves_Type()
)
hicomCabNumShelves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCabNumShelves.setStatus("current")
_HicomFrameTable_Object = MibTable
hicomFrameTable = _HicomFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    hicomFrameTable.setStatus("current")
_HicomFrameEntry_Object = MibTableRow
hicomFrameEntry = _HicomFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1)
)
hicomFrameEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomFramePabxId"),
    (0, "SIEMENS-PN-MIB", "hicomFrameCabAddr"),
    (0, "SIEMENS-PN-MIB", "hicomFrameMntLevel"),
)
if mibBuilder.loadTexts:
    hicomFrameEntry.setStatus("current")
_HicomFramePabxId_Type = Integer32
_HicomFramePabxId_Object = MibTableColumn
hicomFramePabxId = _HicomFramePabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1, 1),
    _HicomFramePabxId_Type()
)
hicomFramePabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomFramePabxId.setStatus("current")
_HicomFrameCabAddr_Type = OctetString
_HicomFrameCabAddr_Object = MibTableColumn
hicomFrameCabAddr = _HicomFrameCabAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1, 2),
    _HicomFrameCabAddr_Type()
)
hicomFrameCabAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomFrameCabAddr.setStatus("current")
_HicomFrameMntLevel_Type = Integer32
_HicomFrameMntLevel_Object = MibTableColumn
hicomFrameMntLevel = _HicomFrameMntLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1, 3),
    _HicomFrameMntLevel_Type()
)
hicomFrameMntLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomFrameMntLevel.setStatus("current")
_HicomFrameType_Type = DisplayString
_HicomFrameType_Object = MibTableColumn
hicomFrameType = _HicomFrameType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1, 4),
    _HicomFrameType_Type()
)
hicomFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomFrameType.setStatus("current")
_HicomFramePartNo_Type = DisplayString
_HicomFramePartNo_Object = MibTableColumn
hicomFramePartNo = _HicomFramePartNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1, 5),
    _HicomFramePartNo_Type()
)
hicomFramePartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomFramePartNo.setStatus("current")
_HicomFramePID1_Type = DisplayString
_HicomFramePID1_Object = MibTableColumn
hicomFramePID1 = _HicomFramePID1_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1, 6),
    _HicomFramePID1_Type()
)
hicomFramePID1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomFramePID1.setStatus("current")
_HicomFramePID2_Type = DisplayString
_HicomFramePID2_Object = MibTableColumn
hicomFramePID2 = _HicomFramePID2_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1, 7),
    _HicomFramePID2_Type()
)
hicomFramePID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomFramePID2.setStatus("current")
_HicomFramePID3_Type = DisplayString
_HicomFramePID3_Object = MibTableColumn
hicomFramePID3 = _HicomFramePID3_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1, 8),
    _HicomFramePID3_Type()
)
hicomFramePID3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomFramePID3.setStatus("current")
_HicomFrameLTU_Type = Integer32
_HicomFrameLTU_Object = MibTableColumn
hicomFrameLTU = _HicomFrameLTU_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1, 9),
    _HicomFrameLTU_Type()
)
hicomFrameLTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomFrameLTU.setStatus("current")
_HicomFrameIpAddr_Type = DisplayString
_HicomFrameIpAddr_Object = MibTableColumn
hicomFrameIpAddr = _HicomFrameIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 1, 2, 1, 10),
    _HicomFrameIpAddr_Type()
)
hicomFrameIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomFrameIpAddr.setStatus("current")
_HicomPeripherals_ObjectIdentity = ObjectIdentity
hicomPeripherals = _HicomPeripherals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 2)
)
_HicomPeriphTable_Object = MibTable
hicomPeriphTable = _HicomPeriphTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hicomPeriphTable.setStatus("current")
_HicomPeriphEntry_Object = MibTableRow
hicomPeriphEntry = _HicomPeriphEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 2, 1, 1)
)
hicomPeriphEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomPeriphPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomPeriphContrID"),
    (0, "SIEMENS-PN-MIB", "hicomPeriphModule"),
)
if mibBuilder.loadTexts:
    hicomPeriphEntry.setStatus("current")
_HicomPeriphPabxId_Type = Integer32
_HicomPeriphPabxId_Object = MibTableColumn
hicomPeriphPabxId = _HicomPeriphPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 2, 1, 1, 1),
    _HicomPeriphPabxId_Type()
)
hicomPeriphPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomPeriphPabxId.setStatus("current")
_HicomPeriphContrID_Type = Integer32
_HicomPeriphContrID_Object = MibTableColumn
hicomPeriphContrID = _HicomPeriphContrID_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 2, 1, 1, 2),
    _HicomPeriphContrID_Type()
)
hicomPeriphContrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomPeriphContrID.setStatus("current")
_HicomPeriphModule_Type = OctetString
_HicomPeriphModule_Object = MibTableColumn
hicomPeriphModule = _HicomPeriphModule_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 2, 1, 1, 3),
    _HicomPeriphModule_Type()
)
hicomPeriphModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomPeriphModule.setStatus("current")
_HicomPeriphType_Type = DisplayString
_HicomPeriphType_Object = MibTableColumn
hicomPeriphType = _HicomPeriphType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 2, 1, 1, 4),
    _HicomPeriphType_Type()
)
hicomPeriphType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomPeriphType.setStatus("current")
_HicomPeriphSSNo_Type = DisplayString
_HicomPeriphSSNo_Object = MibTableColumn
hicomPeriphSSNo = _HicomPeriphSSNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 2, 1, 1, 5),
    _HicomPeriphSSNo_Type()
)
hicomPeriphSSNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomPeriphSSNo.setStatus("current")
_HicomPeriphSize_Type = Integer32
_HicomPeriphSize_Object = MibTableColumn
hicomPeriphSize = _HicomPeriphSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 2, 1, 1, 6),
    _HicomPeriphSize_Type()
)
hicomPeriphSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomPeriphSize.setStatus("current")
_HicomPeriphGran_Type = Integer32
_HicomPeriphGran_Object = MibTableColumn
hicomPeriphGran = _HicomPeriphGran_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 2, 1, 1, 7),
    _HicomPeriphGran_Type()
)
hicomPeriphGran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomPeriphGran.setStatus("current")
_HicomBoards_ObjectIdentity = ObjectIdentity
hicomBoards = _HicomBoards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3)
)
_HicomCDSMTable_Object = MibTable
hicomCDSMTable = _HicomCDSMTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    hicomCDSMTable.setStatus("current")
_HicomCDSMEntry_Object = MibTableRow
hicomCDSMEntry = _HicomCDSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 1, 1)
)
hicomCDSMEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomCDSMPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomCDSMCabAddr"),
    (0, "SIEMENS-PN-MIB", "hicomCDSMMntLevel"),
    (0, "SIEMENS-PN-MIB", "hicomCDSMSlotAddr"),
)
if mibBuilder.loadTexts:
    hicomCDSMEntry.setStatus("current")
_HicomCDSMPabxId_Type = Integer32
_HicomCDSMPabxId_Object = MibTableColumn
hicomCDSMPabxId = _HicomCDSMPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 1, 1, 1),
    _HicomCDSMPabxId_Type()
)
hicomCDSMPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSMPabxId.setStatus("current")
_HicomCDSMCabAddr_Type = OctetString
_HicomCDSMCabAddr_Object = MibTableColumn
hicomCDSMCabAddr = _HicomCDSMCabAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 1, 1, 2),
    _HicomCDSMCabAddr_Type()
)
hicomCDSMCabAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSMCabAddr.setStatus("current")
_HicomCDSMMntLevel_Type = Integer32
_HicomCDSMMntLevel_Object = MibTableColumn
hicomCDSMMntLevel = _HicomCDSMMntLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 1, 1, 3),
    _HicomCDSMMntLevel_Type()
)
hicomCDSMMntLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSMMntLevel.setStatus("current")
_HicomCDSMSlotAddr_Type = Integer32
_HicomCDSMSlotAddr_Object = MibTableColumn
hicomCDSMSlotAddr = _HicomCDSMSlotAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 1, 1, 4),
    _HicomCDSMSlotAddr_Type()
)
hicomCDSMSlotAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSMSlotAddr.setStatus("current")
_HicomCDSMPartNo_Type = DisplayString
_HicomCDSMPartNo_Object = MibTableColumn
hicomCDSMPartNo = _HicomCDSMPartNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 1, 1, 5),
    _HicomCDSMPartNo_Type()
)
hicomCDSMPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSMPartNo.setStatus("current")
_HicomCDSMCode_Type = DisplayString
_HicomCDSMCode_Object = MibTableColumn
hicomCDSMCode = _HicomCDSMCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 1, 1, 6),
    _HicomCDSMCode_Type()
)
hicomCDSMCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSMCode.setStatus("current")
_HicomCDSMVers_Type = Integer32
_HicomCDSMVers_Object = MibTableColumn
hicomCDSMVers = _HicomCDSMVers_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 1, 1, 7),
    _HicomCDSMVers_Type()
)
hicomCDSMVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSMVers.setStatus("current")
_HicomCDSMFirmware_Type = DisplayString
_HicomCDSMFirmware_Object = MibTableColumn
hicomCDSMFirmware = _HicomCDSMFirmware_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 1, 1, 8),
    _HicomCDSMFirmware_Type()
)
hicomCDSMFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSMFirmware.setStatus("current")
_HicomCDSUTable_Object = MibTable
hicomCDSUTable = _HicomCDSUTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    hicomCDSUTable.setStatus("current")
_HicomCDSUEntry_Object = MibTableRow
hicomCDSUEntry = _HicomCDSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 2, 1)
)
hicomCDSUEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomCDSUPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomCDSUCabAddr"),
    (0, "SIEMENS-PN-MIB", "hicomCDSUMntLevel"),
    (0, "SIEMENS-PN-MIB", "hicomCDSUSlotAddr"),
)
if mibBuilder.loadTexts:
    hicomCDSUEntry.setStatus("current")
_HicomCDSUPabxId_Type = Integer32
_HicomCDSUPabxId_Object = MibTableColumn
hicomCDSUPabxId = _HicomCDSUPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 2, 1, 1),
    _HicomCDSUPabxId_Type()
)
hicomCDSUPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSUPabxId.setStatus("current")
_HicomCDSUCabAddr_Type = OctetString
_HicomCDSUCabAddr_Object = MibTableColumn
hicomCDSUCabAddr = _HicomCDSUCabAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 2, 1, 2),
    _HicomCDSUCabAddr_Type()
)
hicomCDSUCabAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSUCabAddr.setStatus("current")
_HicomCDSUMntLevel_Type = Integer32
_HicomCDSUMntLevel_Object = MibTableColumn
hicomCDSUMntLevel = _HicomCDSUMntLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 2, 1, 3),
    _HicomCDSUMntLevel_Type()
)
hicomCDSUMntLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSUMntLevel.setStatus("current")
_HicomCDSUSlotAddr_Type = Integer32
_HicomCDSUSlotAddr_Object = MibTableColumn
hicomCDSUSlotAddr = _HicomCDSUSlotAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 2, 1, 4),
    _HicomCDSUSlotAddr_Type()
)
hicomCDSUSlotAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSUSlotAddr.setStatus("current")
_HicomCDSUPartNo_Type = DisplayString
_HicomCDSUPartNo_Object = MibTableColumn
hicomCDSUPartNo = _HicomCDSUPartNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 2, 1, 5),
    _HicomCDSUPartNo_Type()
)
hicomCDSUPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSUPartNo.setStatus("current")
_HicomCDSUCode_Type = DisplayString
_HicomCDSUCode_Object = MibTableColumn
hicomCDSUCode = _HicomCDSUCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 2, 1, 6),
    _HicomCDSUCode_Type()
)
hicomCDSUCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSUCode.setStatus("current")
_HicomCDSUVers_Type = Integer32
_HicomCDSUVers_Object = MibTableColumn
hicomCDSUVers = _HicomCDSUVers_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 2, 1, 7),
    _HicomCDSUVers_Type()
)
hicomCDSUVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSUVers.setStatus("current")
_HicomCDSUFirmware_Type = DisplayString
_HicomCDSUFirmware_Object = MibTableColumn
hicomCDSUFirmware = _HicomCDSUFirmware_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 2, 1, 8),
    _HicomCDSUFirmware_Type()
)
hicomCDSUFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomCDSUFirmware.setStatus("current")
_HicomBCSMTable_Object = MibTable
hicomBCSMTable = _HicomBCSMTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    hicomBCSMTable.setStatus("current")
_HicomBCSMEntry_Object = MibTableRow
hicomBCSMEntry = _HicomBCSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3, 1)
)
hicomBCSMEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomBCSMPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomBCSMMod"),
    (0, "SIEMENS-PN-MIB", "hicomBCSMSlotAddr"),
)
if mibBuilder.loadTexts:
    hicomBCSMEntry.setStatus("current")
_HicomBCSMPabxId_Type = Integer32
_HicomBCSMPabxId_Object = MibTableColumn
hicomBCSMPabxId = _HicomBCSMPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3, 1, 1),
    _HicomBCSMPabxId_Type()
)
hicomBCSMPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSMPabxId.setStatus("current")
_HicomBCSMMod_Type = OctetString
_HicomBCSMMod_Object = MibTableColumn
hicomBCSMMod = _HicomBCSMMod_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3, 1, 2),
    _HicomBCSMMod_Type()
)
hicomBCSMMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSMMod.setStatus("current")
_HicomBCSMSlotAddr_Type = Integer32
_HicomBCSMSlotAddr_Object = MibTableColumn
hicomBCSMSlotAddr = _HicomBCSMSlotAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3, 1, 3),
    _HicomBCSMSlotAddr_Type()
)
hicomBCSMSlotAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSMSlotAddr.setStatus("current")
_HicomBCSMConfBoard_Type = DisplayString
_HicomBCSMConfBoard_Object = MibTableColumn
hicomBCSMConfBoard = _HicomBCSMConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3, 1, 4),
    _HicomBCSMConfBoard_Type()
)
hicomBCSMConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSMConfBoard.setStatus("current")
_HicomBCSMCode_Type = DisplayString
_HicomBCSMCode_Object = MibTableColumn
hicomBCSMCode = _HicomBCSMCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3, 1, 5),
    _HicomBCSMCode_Type()
)
hicomBCSMCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSMCode.setStatus("current")
_HicomBCSMInstBoard_Type = DisplayString
_HicomBCSMInstBoard_Object = MibTableColumn
hicomBCSMInstBoard = _HicomBCSMInstBoard_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3, 1, 6),
    _HicomBCSMInstBoard_Type()
)
hicomBCSMInstBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSMInstBoard.setStatus("current")
_HicomBCSMVers_Type = Integer32
_HicomBCSMVers_Object = MibTableColumn
hicomBCSMVers = _HicomBCSMVers_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3, 1, 7),
    _HicomBCSMVers_Type()
)
hicomBCSMVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSMVers.setStatus("current")
_HicomBCSMFirmware_Type = DisplayString
_HicomBCSMFirmware_Object = MibTableColumn
hicomBCSMFirmware = _HicomBCSMFirmware_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3, 1, 8),
    _HicomBCSMFirmware_Type()
)
hicomBCSMFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSMFirmware.setStatus("current")
_HicomBCSMStatus_Type = DisplayString
_HicomBCSMStatus_Object = MibTableColumn
hicomBCSMStatus = _HicomBCSMStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 3, 1, 9),
    _HicomBCSMStatus_Type()
)
hicomBCSMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSMStatus.setStatus("current")
_HicomBCSUTable_Object = MibTable
hicomBCSUTable = _HicomBCSUTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4)
)
if mibBuilder.loadTexts:
    hicomBCSUTable.setStatus("current")
_HicomBCSUEntry_Object = MibTableRow
hicomBCSUEntry = _HicomBCSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1)
)
hicomBCSUEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomBCSUPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomBCSULTG"),
    (0, "SIEMENS-PN-MIB", "hicomBCSULTU"),
    (0, "SIEMENS-PN-MIB", "hicomBCSUSlotAddr"),
)
if mibBuilder.loadTexts:
    hicomBCSUEntry.setStatus("current")
_HicomBCSUPabxId_Type = Integer32
_HicomBCSUPabxId_Object = MibTableColumn
hicomBCSUPabxId = _HicomBCSUPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1, 1),
    _HicomBCSUPabxId_Type()
)
hicomBCSUPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSUPabxId.setStatus("current")
_HicomBCSULTG_Type = Integer32
_HicomBCSULTG_Object = MibTableColumn
hicomBCSULTG = _HicomBCSULTG_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1, 2),
    _HicomBCSULTG_Type()
)
hicomBCSULTG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSULTG.setStatus("current")
_HicomBCSULTU_Type = Integer32
_HicomBCSULTU_Object = MibTableColumn
hicomBCSULTU = _HicomBCSULTU_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1, 3),
    _HicomBCSULTU_Type()
)
hicomBCSULTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSULTU.setStatus("current")
_HicomBCSUSlotAddr_Type = Integer32
_HicomBCSUSlotAddr_Object = MibTableColumn
hicomBCSUSlotAddr = _HicomBCSUSlotAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1, 4),
    _HicomBCSUSlotAddr_Type()
)
hicomBCSUSlotAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSUSlotAddr.setStatus("current")
_HicomBCSUConfBoard_Type = DisplayString
_HicomBCSUConfBoard_Object = MibTableColumn
hicomBCSUConfBoard = _HicomBCSUConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1, 5),
    _HicomBCSUConfBoard_Type()
)
hicomBCSUConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSUConfBoard.setStatus("current")
_HicomBCSUCode_Type = DisplayString
_HicomBCSUCode_Object = MibTableColumn
hicomBCSUCode = _HicomBCSUCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1, 6),
    _HicomBCSUCode_Type()
)
hicomBCSUCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSUCode.setStatus("current")
_HicomBCSUInstBoard_Type = DisplayString
_HicomBCSUInstBoard_Object = MibTableColumn
hicomBCSUInstBoard = _HicomBCSUInstBoard_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1, 7),
    _HicomBCSUInstBoard_Type()
)
hicomBCSUInstBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSUInstBoard.setStatus("current")
_HicomBCSUVers_Type = Integer32
_HicomBCSUVers_Object = MibTableColumn
hicomBCSUVers = _HicomBCSUVers_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1, 8),
    _HicomBCSUVers_Type()
)
hicomBCSUVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSUVers.setStatus("current")
_HicomBCSUFirmware_Type = DisplayString
_HicomBCSUFirmware_Object = MibTableColumn
hicomBCSUFirmware = _HicomBCSUFirmware_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1, 9),
    _HicomBCSUFirmware_Type()
)
hicomBCSUFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSUFirmware.setStatus("current")
_HicomBCSUStatus_Type = DisplayString
_HicomBCSUStatus_Object = MibTableColumn
hicomBCSUStatus = _HicomBCSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 3, 4, 1, 10),
    _HicomBCSUStatus_Type()
)
hicomBCSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomBCSUStatus.setStatus("current")
_HicomHWInfo_ObjectIdentity = ObjectIdentity
hicomHWInfo = _HicomHWInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 4)
)
_HicomHardSubagentLastMsgNo_Type = Integer32
_HicomHardSubagentLastMsgNo_Object = MibScalar
hicomHardSubagentLastMsgNo = _HicomHardSubagentLastMsgNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 4, 1),
    _HicomHardSubagentLastMsgNo_Type()
)
hicomHardSubagentLastMsgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomHardSubagentLastMsgNo.setStatus("current")
_HicomHardSubagentLastMsgText_Type = OctetString
_HicomHardSubagentLastMsgText_Object = MibScalar
hicomHardSubagentLastMsgText = _HicomHardSubagentLastMsgText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 4, 2),
    _HicomHardSubagentLastMsgText_Type()
)
hicomHardSubagentLastMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomHardSubagentLastMsgText.setStatus("current")
_HicomHardSubagentResultData_Type = Integer32
_HicomHardSubagentResultData_Object = MibScalar
hicomHardSubagentResultData = _HicomHardSubagentResultData_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 4, 3),
    _HicomHardSubagentResultData_Type()
)
hicomHardSubagentResultData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomHardSubagentResultData.setStatus("current")
_HicomHWDiscovery_ObjectIdentity = ObjectIdentity
hicomHWDiscovery = _HicomHWDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 5)
)
_HicomHWChanges_Type = Counter32
_HicomHWChanges_Object = MibScalar
hicomHWChanges = _HicomHWChanges_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 5, 1),
    _HicomHWChanges_Type()
)
hicomHWChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomHWChanges.setStatus("current")
_HicomHWDiscovTable_Object = MibTable
hicomHWDiscovTable = _HicomHWDiscovTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    hicomHWDiscovTable.setStatus("current")
_HicomHWDiscovEntry_Object = MibTableRow
hicomHWDiscovEntry = _HicomHWDiscovEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 5, 2, 1)
)
hicomHWDiscovEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomHWDiscovPabxId"),
)
if mibBuilder.loadTexts:
    hicomHWDiscovEntry.setStatus("current")
_HicomHWDiscovPabxId_Type = Integer32
_HicomHWDiscovPabxId_Object = MibTableColumn
hicomHWDiscovPabxId = _HicomHWDiscovPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 5, 2, 1, 1),
    _HicomHWDiscovPabxId_Type()
)
hicomHWDiscovPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomHWDiscovPabxId.setStatus("current")
_HicomHWDiscovPabxMnemonic_Type = DisplayString
_HicomHWDiscovPabxMnemonic_Object = MibTableColumn
hicomHWDiscovPabxMnemonic = _HicomHWDiscovPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 5, 2, 1, 2),
    _HicomHWDiscovPabxMnemonic_Type()
)
hicomHWDiscovPabxMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomHWDiscovPabxMnemonic.setStatus("current")
_HicomHWDiscovStatus_Type = DiscoveryStates
_HicomHWDiscovStatus_Object = MibTableColumn
hicomHWDiscovStatus = _HicomHWDiscovStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 5, 2, 1, 3),
    _HicomHWDiscovStatus_Type()
)
hicomHWDiscovStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomHWDiscovStatus.setStatus("current")
_HicomHWDiscovMode_Type = DiscoveryModes
_HicomHWDiscovMode_Object = MibTableColumn
hicomHWDiscovMode = _HicomHWDiscovMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 5, 2, 1, 4),
    _HicomHWDiscovMode_Type()
)
hicomHWDiscovMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomHWDiscovMode.setStatus("current")
_HicomHWDiscovTimDat_Type = DisplayString
_HicomHWDiscovTimDat_Object = MibTableColumn
hicomHWDiscovTimDat = _HicomHWDiscovTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 5, 2, 1, 5),
    _HicomHWDiscovTimDat_Type()
)
hicomHWDiscovTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomHWDiscovTimDat.setStatus("current")
_HicomHWDiscovErrTimDat_Type = DisplayString
_HicomHWDiscovErrTimDat_Object = MibTableColumn
hicomHWDiscovErrTimDat = _HicomHWDiscovErrTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 6, 5, 2, 1, 6),
    _HicomHWDiscovErrTimDat_Type()
)
hicomHWDiscovErrTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomHWDiscovErrTimDat.setStatus("current")
_HicomTopo_ObjectIdentity = ObjectIdentity
hicomTopo = _HicomTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7)
)
_HicomTrunkGrp_ObjectIdentity = ObjectIdentity
hicomTrunkGrp = _HicomTrunkGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1)
)
_HicomTrunkGrpTable_Object = MibTable
hicomTrunkGrpTable = _HicomTrunkGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hicomTrunkGrpTable.setStatus("current")
_HicomTrunkGrpEntry_Object = MibTableRow
hicomTrunkGrpEntry = _HicomTrunkGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1, 1)
)
hicomTrunkGrpEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomTrunkGrpPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomTrunkGrpNo"),
)
if mibBuilder.loadTexts:
    hicomTrunkGrpEntry.setStatus("current")
_HicomTrunkGrpPabxId_Type = Integer32
_HicomTrunkGrpPabxId_Object = MibTableColumn
hicomTrunkGrpPabxId = _HicomTrunkGrpPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1, 1, 1),
    _HicomTrunkGrpPabxId_Type()
)
hicomTrunkGrpPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkGrpPabxId.setStatus("current")
_HicomTrunkGrpNo_Type = Integer32
_HicomTrunkGrpNo_Object = MibTableColumn
hicomTrunkGrpNo = _HicomTrunkGrpNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1, 1, 2),
    _HicomTrunkGrpNo_Type()
)
hicomTrunkGrpNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkGrpNo.setStatus("current")


class _HicomTrunkGrpNNodeNo_Type(Integer32):
    """Custom type hicomTrunkGrpNNodeNo based on Integer32"""
    defaultValue = 0


_HicomTrunkGrpNNodeNo_Object = MibTableColumn
hicomTrunkGrpNNodeNo = _HicomTrunkGrpNNodeNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1, 1, 3),
    _HicomTrunkGrpNNodeNo_Type()
)
hicomTrunkGrpNNodeNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomTrunkGrpNNodeNo.setStatus("current")


class _HicomTrunkGrpVNodeNo_Type(Integer32):
    """Custom type hicomTrunkGrpVNodeNo based on Integer32"""
    defaultValue = 0


_HicomTrunkGrpVNodeNo_Object = MibTableColumn
hicomTrunkGrpVNodeNo = _HicomTrunkGrpVNodeNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1, 1, 4),
    _HicomTrunkGrpVNodeNo_Type()
)
hicomTrunkGrpVNodeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkGrpVNodeNo.setStatus("current")
_HicomTrunkGrpTrunkType_Type = TrunkTypes
_HicomTrunkGrpTrunkType_Object = MibTableColumn
hicomTrunkGrpTrunkType = _HicomTrunkGrpTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1, 1, 5),
    _HicomTrunkGrpTrunkType_Type()
)
hicomTrunkGrpTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkGrpTrunkType.setStatus("current")
_HicomTrunkGrpMaxNo_Type = Integer32
_HicomTrunkGrpMaxNo_Object = MibTableColumn
hicomTrunkGrpMaxNo = _HicomTrunkGrpMaxNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1, 1, 6),
    _HicomTrunkGrpMaxNo_Type()
)
hicomTrunkGrpMaxNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkGrpMaxNo.setStatus("current")
_HicomTrunkGrpName_Type = DisplayString
_HicomTrunkGrpName_Object = MibTableColumn
hicomTrunkGrpName = _HicomTrunkGrpName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1, 1, 7),
    _HicomTrunkGrpName_Type()
)
hicomTrunkGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkGrpName.setStatus("current")
_HicomTrunkGrpDevice_Type = DisplayString
_HicomTrunkGrpDevice_Object = MibTableColumn
hicomTrunkGrpDevice = _HicomTrunkGrpDevice_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1, 1, 8),
    _HicomTrunkGrpDevice_Type()
)
hicomTrunkGrpDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkGrpDevice.setStatus("current")
_HicomTrunkGrpAlarms_Type = OctetString
_HicomTrunkGrpAlarms_Object = MibTableColumn
hicomTrunkGrpAlarms = _HicomTrunkGrpAlarms_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 1, 1, 1, 9),
    _HicomTrunkGrpAlarms_Type()
)
hicomTrunkGrpAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkGrpAlarms.setStatus("current")
_HicomTrunk_ObjectIdentity = ObjectIdentity
hicomTrunk = _HicomTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2)
)
_HicomTrunkTable_Object = MibTable
hicomTrunkTable = _HicomTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hicomTrunkTable.setStatus("current")
_HicomTrunkEntry_Object = MibTableRow
hicomTrunkEntry = _HicomTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1)
)
hicomTrunkEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomTrunkPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomTrunkType"),
    (0, "SIEMENS-PN-MIB", "hicomTrunkTrunkGrpNo"),
    (0, "SIEMENS-PN-MIB", "hicomTrunkLtg"),
    (0, "SIEMENS-PN-MIB", "hicomTrunkLtu"),
    (0, "SIEMENS-PN-MIB", "hicomTrunkSlot"),
    (0, "SIEMENS-PN-MIB", "hicomTrunkNo"),
    (0, "SIEMENS-PN-MIB", "hicomTrunkChannelGrp"),
)
if mibBuilder.loadTexts:
    hicomTrunkEntry.setStatus("current")
_HicomTrunkPabxId_Type = Integer32
_HicomTrunkPabxId_Object = MibTableColumn
hicomTrunkPabxId = _HicomTrunkPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 1),
    _HicomTrunkPabxId_Type()
)
hicomTrunkPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkPabxId.setStatus("current")
_HicomTrunkType_Type = TrunkTypes
_HicomTrunkType_Object = MibTableColumn
hicomTrunkType = _HicomTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 2),
    _HicomTrunkType_Type()
)
hicomTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkType.setStatus("current")
_HicomTrunkTrunkGrpNo_Type = Integer32
_HicomTrunkTrunkGrpNo_Object = MibTableColumn
hicomTrunkTrunkGrpNo = _HicomTrunkTrunkGrpNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 3),
    _HicomTrunkTrunkGrpNo_Type()
)
hicomTrunkTrunkGrpNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkTrunkGrpNo.setStatus("current")
_HicomTrunkLtg_Type = Integer32
_HicomTrunkLtg_Object = MibTableColumn
hicomTrunkLtg = _HicomTrunkLtg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 4),
    _HicomTrunkLtg_Type()
)
hicomTrunkLtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkLtg.setStatus("current")
_HicomTrunkLtu_Type = Integer32
_HicomTrunkLtu_Object = MibTableColumn
hicomTrunkLtu = _HicomTrunkLtu_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 5),
    _HicomTrunkLtu_Type()
)
hicomTrunkLtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkLtu.setStatus("current")
_HicomTrunkSlot_Type = Integer32
_HicomTrunkSlot_Object = MibTableColumn
hicomTrunkSlot = _HicomTrunkSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 6),
    _HicomTrunkSlot_Type()
)
hicomTrunkSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkSlot.setStatus("current")
_HicomTrunkNo_Type = Integer32
_HicomTrunkNo_Object = MibTableColumn
hicomTrunkNo = _HicomTrunkNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 7),
    _HicomTrunkNo_Type()
)
hicomTrunkNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkNo.setStatus("current")
_HicomTrunkChannelGrp_Type = Integer32
_HicomTrunkChannelGrp_Object = MibTableColumn
hicomTrunkChannelGrp = _HicomTrunkChannelGrp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 8),
    _HicomTrunkChannelGrp_Type()
)
hicomTrunkChannelGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkChannelGrp.setStatus("current")
_HicomTrunkSNodeNo_Type = Integer32
_HicomTrunkSNodeNo_Object = MibTableColumn
hicomTrunkSNodeNo = _HicomTrunkSNodeNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 9),
    _HicomTrunkSNodeNo_Type()
)
hicomTrunkSNodeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkSNodeNo.setStatus("current")


class _HicomTrunkStatOp_Type(Integer32):
    """Custom type hicomTrunkStatOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_HicomTrunkStatOp_Type.__name__ = "Integer32"
_HicomTrunkStatOp_Object = MibTableColumn
hicomTrunkStatOp = _HicomTrunkStatOp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 10),
    _HicomTrunkStatOp_Type()
)
hicomTrunkStatOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkStatOp.setStatus("current")
_HicomTrunkAlSubId_Type = Integer32
_HicomTrunkAlSubId_Object = MibTableColumn
hicomTrunkAlSubId = _HicomTrunkAlSubId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 11),
    _HicomTrunkAlSubId_Type()
)
hicomTrunkAlSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkAlSubId.setStatus("current")
_HicomTrunkChannels_Type = OctetString
_HicomTrunkChannels_Object = MibTableColumn
hicomTrunkChannels = _HicomTrunkChannels_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 12),
    _HicomTrunkChannels_Type()
)
hicomTrunkChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkChannels.setStatus("current")
_HicomTrunkDevice_Type = DisplayString
_HicomTrunkDevice_Object = MibTableColumn
hicomTrunkDevice = _HicomTrunkDevice_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 13),
    _HicomTrunkDevice_Type()
)
hicomTrunkDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkDevice.setStatus("current")
_HicomTrunkName_Type = DisplayString
_HicomTrunkName_Object = MibTableColumn
hicomTrunkName = _HicomTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 2, 1, 1, 14),
    _HicomTrunkName_Type()
)
hicomTrunkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTrunkName.setStatus("current")
_HicomTopoInfo_ObjectIdentity = ObjectIdentity
hicomTopoInfo = _HicomTopoInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 3)
)
_HicomTopoSubagentLastMsgNo_Type = Integer32
_HicomTopoSubagentLastMsgNo_Object = MibScalar
hicomTopoSubagentLastMsgNo = _HicomTopoSubagentLastMsgNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 3, 1),
    _HicomTopoSubagentLastMsgNo_Type()
)
hicomTopoSubagentLastMsgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTopoSubagentLastMsgNo.setStatus("current")
_HicomTopoSubagentLastMsgText_Type = OctetString
_HicomTopoSubagentLastMsgText_Object = MibScalar
hicomTopoSubagentLastMsgText = _HicomTopoSubagentLastMsgText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 3, 2),
    _HicomTopoSubagentLastMsgText_Type()
)
hicomTopoSubagentLastMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTopoSubagentLastMsgText.setStatus("current")
_HicomTopoSubagentResultData_Type = Integer32
_HicomTopoSubagentResultData_Object = MibScalar
hicomTopoSubagentResultData = _HicomTopoSubagentResultData_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 3, 3),
    _HicomTopoSubagentResultData_Type()
)
hicomTopoSubagentResultData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomTopoSubagentResultData.setStatus("current")
_HicomTopoDiscovery_ObjectIdentity = ObjectIdentity
hicomTopoDiscovery = _HicomTopoDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 4)
)
_HicomTopoChanges_Type = Counter32
_HicomTopoChanges_Object = MibScalar
hicomTopoChanges = _HicomTopoChanges_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 4, 1),
    _HicomTopoChanges_Type()
)
hicomTopoChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTopoChanges.setStatus("current")
_HicomTopoDiscovTable_Object = MibTable
hicomTopoDiscovTable = _HicomTopoDiscovTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 4, 2)
)
if mibBuilder.loadTexts:
    hicomTopoDiscovTable.setStatus("current")
_HicomTopoDiscovEntry_Object = MibTableRow
hicomTopoDiscovEntry = _HicomTopoDiscovEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 4, 2, 1)
)
hicomTopoDiscovEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomTopoDiscovPabxId"),
)
if mibBuilder.loadTexts:
    hicomTopoDiscovEntry.setStatus("current")
_HicomTopoDiscovPabxId_Type = Integer32
_HicomTopoDiscovPabxId_Object = MibTableColumn
hicomTopoDiscovPabxId = _HicomTopoDiscovPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 4, 2, 1, 1),
    _HicomTopoDiscovPabxId_Type()
)
hicomTopoDiscovPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTopoDiscovPabxId.setStatus("current")
_HicomTopoDiscovPabxMnemonic_Type = DisplayString
_HicomTopoDiscovPabxMnemonic_Object = MibTableColumn
hicomTopoDiscovPabxMnemonic = _HicomTopoDiscovPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 4, 2, 1, 2),
    _HicomTopoDiscovPabxMnemonic_Type()
)
hicomTopoDiscovPabxMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTopoDiscovPabxMnemonic.setStatus("current")
_HicomTopoDiscovStatus_Type = DiscoveryStates
_HicomTopoDiscovStatus_Object = MibTableColumn
hicomTopoDiscovStatus = _HicomTopoDiscovStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 4, 2, 1, 3),
    _HicomTopoDiscovStatus_Type()
)
hicomTopoDiscovStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomTopoDiscovStatus.setStatus("current")
_HicomTopoDiscovMode_Type = DiscoveryModes
_HicomTopoDiscovMode_Object = MibTableColumn
hicomTopoDiscovMode = _HicomTopoDiscovMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 4, 2, 1, 4),
    _HicomTopoDiscovMode_Type()
)
hicomTopoDiscovMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomTopoDiscovMode.setStatus("current")
_HicomTopoDiscovTimDat_Type = DisplayString
_HicomTopoDiscovTimDat_Object = MibTableColumn
hicomTopoDiscovTimDat = _HicomTopoDiscovTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 4, 2, 1, 5),
    _HicomTopoDiscovTimDat_Type()
)
hicomTopoDiscovTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTopoDiscovTimDat.setStatus("current")
_HicomTopoDiscovErrTimDat_Type = DisplayString
_HicomTopoDiscovErrTimDat_Object = MibTableColumn
hicomTopoDiscovErrTimDat = _HicomTopoDiscovErrTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 4, 2, 1, 6),
    _HicomTopoDiscovErrTimDat_Type()
)
hicomTopoDiscovErrTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomTopoDiscovErrTimDat.setStatus("current")
_HicomKntop_ObjectIdentity = ObjectIdentity
hicomKntop = _HicomKntop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5)
)
_HicomKntopTable_Object = MibTable
hicomKntopTable = _HicomKntopTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1)
)
if mibBuilder.loadTexts:
    hicomKntopTable.setStatus("current")
_HicomKntopEntry_Object = MibTableRow
hicomKntopEntry = _HicomKntopEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1)
)
hicomKntopEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomKntopPabxId"),
    (0, "SIEMENS-PN-MIB", "hicomKntopLtg"),
    (0, "SIEMENS-PN-MIB", "hicomKntopLtu"),
    (0, "SIEMENS-PN-MIB", "hicomKntopSlot"),
    (0, "SIEMENS-PN-MIB", "hicomKntopSatznr"),
    (0, "SIEMENS-PN-MIB", "hicomKntopBKanalGrp"),
    (0, "SIEMENS-PN-MIB", "hicomKntopPNodeIndex"),
)
if mibBuilder.loadTexts:
    hicomKntopEntry.setStatus("current")
_HicomKntopPabxId_Type = Integer32
_HicomKntopPabxId_Object = MibTableColumn
hicomKntopPabxId = _HicomKntopPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 1),
    _HicomKntopPabxId_Type()
)
hicomKntopPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopPabxId.setStatus("current")
_HicomKntopLtg_Type = Integer32
_HicomKntopLtg_Object = MibTableColumn
hicomKntopLtg = _HicomKntopLtg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 2),
    _HicomKntopLtg_Type()
)
hicomKntopLtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopLtg.setStatus("current")
_HicomKntopLtu_Type = Integer32
_HicomKntopLtu_Object = MibTableColumn
hicomKntopLtu = _HicomKntopLtu_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 3),
    _HicomKntopLtu_Type()
)
hicomKntopLtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopLtu.setStatus("current")
_HicomKntopSlot_Type = Integer32
_HicomKntopSlot_Object = MibTableColumn
hicomKntopSlot = _HicomKntopSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 4),
    _HicomKntopSlot_Type()
)
hicomKntopSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopSlot.setStatus("current")
_HicomKntopSatznr_Type = Integer32
_HicomKntopSatznr_Object = MibTableColumn
hicomKntopSatznr = _HicomKntopSatznr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 5),
    _HicomKntopSatznr_Type()
)
hicomKntopSatznr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopSatznr.setStatus("current")
_HicomKntopBKanalGrp_Type = Integer32
_HicomKntopBKanalGrp_Object = MibTableColumn
hicomKntopBKanalGrp = _HicomKntopBKanalGrp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 6),
    _HicomKntopBKanalGrp_Type()
)
hicomKntopBKanalGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopBKanalGrp.setStatus("current")
_HicomKntopPNodeIndex_Type = Integer32
_HicomKntopPNodeIndex_Object = MibTableColumn
hicomKntopPNodeIndex = _HicomKntopPNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 7),
    _HicomKntopPNodeIndex_Type()
)
hicomKntopPNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopPNodeIndex.setStatus("current")
_HicomKntopPLtg_Type = Integer32
_HicomKntopPLtg_Object = MibTableColumn
hicomKntopPLtg = _HicomKntopPLtg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 8),
    _HicomKntopPLtg_Type()
)
hicomKntopPLtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopPLtg.setStatus("current")
_HicomKntopPLtu_Type = Integer32
_HicomKntopPLtu_Object = MibTableColumn
hicomKntopPLtu = _HicomKntopPLtu_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 9),
    _HicomKntopPLtu_Type()
)
hicomKntopPLtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopPLtu.setStatus("current")
_HicomKntopPSlot_Type = Integer32
_HicomKntopPSlot_Object = MibTableColumn
hicomKntopPSlot = _HicomKntopPSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 10),
    _HicomKntopPSlot_Type()
)
hicomKntopPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopPSlot.setStatus("current")
_HicomKntopPSatznr_Type = Integer32
_HicomKntopPSatznr_Object = MibTableColumn
hicomKntopPSatznr = _HicomKntopPSatznr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 11),
    _HicomKntopPSatznr_Type()
)
hicomKntopPSatznr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopPSatznr.setStatus("current")
_HicomKntopPBKanalGrp_Type = Integer32
_HicomKntopPBKanalGrp_Object = MibTableColumn
hicomKntopPBKanalGrp = _HicomKntopPBKanalGrp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 12),
    _HicomKntopPBKanalGrp_Type()
)
hicomKntopPBKanalGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopPBKanalGrp.setStatus("current")
_HicomKntopPNodeNo_Type = Integer32
_HicomKntopPNodeNo_Object = MibTableColumn
hicomKntopPNodeNo = _HicomKntopPNodeNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 13),
    _HicomKntopPNodeNo_Type()
)
hicomKntopPNodeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopPNodeNo.setStatus("current")
_HicomKntopBunr_Type = Integer32
_HicomKntopBunr_Object = MibTableColumn
hicomKntopBunr = _HicomKntopBunr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 7, 5, 1, 1, 14),
    _HicomKntopBunr_Type()
)
hicomKntopBunr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomKntopBunr.setStatus("current")
_HicomSQL_ObjectIdentity = ObjectIdentity
hicomSQL = _HicomSQL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8)
)
_HicomSQLsessionIdGenerator_Type = TestAndIncr
_HicomSQLsessionIdGenerator_Object = MibScalar
hicomSQLsessionIdGenerator = _HicomSQLsessionIdGenerator_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 1),
    _HicomSQLsessionIdGenerator_Type()
)
hicomSQLsessionIdGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSQLsessionIdGenerator.setStatus("current")
_HicomSQLsessionTable_Object = MibTable
hicomSQLsessionTable = _HicomSQLsessionTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    hicomSQLsessionTable.setStatus("current")
_HicomSQLsessionEntry_Object = MibTableRow
hicomSQLsessionEntry = _HicomSQLsessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 2, 1)
)
hicomSQLsessionEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomSQLsessionId"),
)
if mibBuilder.loadTexts:
    hicomSQLsessionEntry.setStatus("current")
_HicomSQLsessionId_Type = Integer32
_HicomSQLsessionId_Object = MibTableColumn
hicomSQLsessionId = _HicomSQLsessionId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 2, 1, 1),
    _HicomSQLsessionId_Type()
)
hicomSQLsessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSQLsessionId.setStatus("current")


class _HicomSQLsessionState_Type(Integer32):
    """Custom type hicomSQLsessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("error", 4),
          ("idle", 1),
          ("run", 2),
          ("valid", 5))
    )


_HicomSQLsessionState_Type.__name__ = "Integer32"
_HicomSQLsessionState_Object = MibTableColumn
hicomSQLsessionState = _HicomSQLsessionState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 2, 1, 2),
    _HicomSQLsessionState_Type()
)
hicomSQLsessionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSQLsessionState.setStatus("current")
_HicomSQLsessionStatement_Type = Integer32
_HicomSQLsessionStatement_Object = MibTableColumn
hicomSQLsessionStatement = _HicomSQLsessionStatement_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 2, 1, 3),
    _HicomSQLsessionStatement_Type()
)
hicomSQLsessionStatement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSQLsessionStatement.setStatus("current")
_HicomSQLsessionWhereClause_Type = DisplayString
_HicomSQLsessionWhereClause_Object = MibTableColumn
hicomSQLsessionWhereClause = _HicomSQLsessionWhereClause_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 2, 1, 4),
    _HicomSQLsessionWhereClause_Type()
)
hicomSQLsessionWhereClause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSQLsessionWhereClause.setStatus("current")


class _HicomSQLsessionTimeout_Type(Integer32):
    """Custom type hicomSQLsessionTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_HicomSQLsessionTimeout_Type.__name__ = "Integer32"
_HicomSQLsessionTimeout_Object = MibTableColumn
hicomSQLsessionTimeout = _HicomSQLsessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 2, 1, 5),
    _HicomSQLsessionTimeout_Type()
)
hicomSQLsessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomSQLsessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hicomSQLsessionTimeout.setUnits("seconds")


class _HicomSQLsessionResultSize_Type(Integer32):
    """Custom type hicomSQLsessionResultSize based on Integer32"""
    defaultValue = 0


_HicomSQLsessionResultSize_Object = MibTableColumn
hicomSQLsessionResultSize = _HicomSQLsessionResultSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 2, 1, 6),
    _HicomSQLsessionResultSize_Type()
)
hicomSQLsessionResultSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSQLsessionResultSize.setStatus("current")


class _HicomSQLsessionResultNoLines_Type(Integer32):
    """Custom type hicomSQLsessionResultNoLines based on Integer32"""
    defaultValue = 0


_HicomSQLsessionResultNoLines_Object = MibTableColumn
hicomSQLsessionResultNoLines = _HicomSQLsessionResultNoLines_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 2, 1, 7),
    _HicomSQLsessionResultNoLines_Type()
)
hicomSQLsessionResultNoLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSQLsessionResultNoLines.setStatus("current")
_HicomSQLresultTable_Object = MibTable
hicomSQLresultTable = _HicomSQLresultTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    hicomSQLresultTable.setStatus("current")
_HicomSQLresultEntry_Object = MibTableRow
hicomSQLresultEntry = _HicomSQLresultEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 3, 1)
)
hicomSQLresultEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomSQLresultId"),
    (0, "SIEMENS-PN-MIB", "hicomSQLresultBlockNo"),
)
if mibBuilder.loadTexts:
    hicomSQLresultEntry.setStatus("current")
_HicomSQLresultId_Type = Integer32
_HicomSQLresultId_Object = MibTableColumn
hicomSQLresultId = _HicomSQLresultId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 3, 1, 1),
    _HicomSQLresultId_Type()
)
hicomSQLresultId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSQLresultId.setStatus("current")
_HicomSQLresultBlockNo_Type = Integer32
_HicomSQLresultBlockNo_Object = MibTableColumn
hicomSQLresultBlockNo = _HicomSQLresultBlockNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 3, 1, 2),
    _HicomSQLresultBlockNo_Type()
)
hicomSQLresultBlockNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSQLresultBlockNo.setStatus("current")
_HicomSQLresultData_Type = DisplayString
_HicomSQLresultData_Object = MibTableColumn
hicomSQLresultData = _HicomSQLresultData_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 3, 1, 3),
    _HicomSQLresultData_Type()
)
hicomSQLresultData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSQLresultData.setStatus("current")
_HicomSQLinfo_ObjectIdentity = ObjectIdentity
hicomSQLinfo = _HicomSQLinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 4)
)
_HicomSQLSubagentLastMsgNo_Type = Integer32
_HicomSQLSubagentLastMsgNo_Object = MibScalar
hicomSQLSubagentLastMsgNo = _HicomSQLSubagentLastMsgNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 4, 1),
    _HicomSQLSubagentLastMsgNo_Type()
)
hicomSQLSubagentLastMsgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSQLSubagentLastMsgNo.setStatus("current")
_HicomSQLSubagentLastMsgText_Type = OctetString
_HicomSQLSubagentLastMsgText_Object = MibScalar
hicomSQLSubagentLastMsgText = _HicomSQLSubagentLastMsgText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 8, 4, 2),
    _HicomSQLSubagentLastMsgText_Type()
)
hicomSQLSubagentLastMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomSQLSubagentLastMsgText.setStatus("current")
_HicomDiscov_ObjectIdentity = ObjectIdentity
hicomDiscov = _HicomDiscov_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9)
)
_HicomDiscovTable_Object = MibTable
hicomDiscovTable = _HicomDiscovTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hicomDiscovTable.setStatus("current")
_HicomDiscovEntry_Object = MibTableRow
hicomDiscovEntry = _HicomDiscovEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 1, 1)
)
hicomDiscovEntry.setIndexNames(
    (0, "SIEMENS-PN-MIB", "hicomDiscovPabxId"),
)
if mibBuilder.loadTexts:
    hicomDiscovEntry.setStatus("current")
_HicomDiscovPabxId_Type = Integer32
_HicomDiscovPabxId_Object = MibTableColumn
hicomDiscovPabxId = _HicomDiscovPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 1, 1, 1),
    _HicomDiscovPabxId_Type()
)
hicomDiscovPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomDiscovPabxId.setStatus("current")
_HicomDiscovPabxMnemonic_Type = DisplayString
_HicomDiscovPabxMnemonic_Object = MibTableColumn
hicomDiscovPabxMnemonic = _HicomDiscovPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 1, 1, 2),
    _HicomDiscovPabxMnemonic_Type()
)
hicomDiscovPabxMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomDiscovPabxMnemonic.setStatus("current")
_HicomDiscovStatus_Type = DiscoveryStates
_HicomDiscovStatus_Object = MibTableColumn
hicomDiscovStatus = _HicomDiscovStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 1, 1, 3),
    _HicomDiscovStatus_Type()
)
hicomDiscovStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomDiscovStatus.setStatus("current")
_HicomDiscovMode_Type = DiscoveryModes
_HicomDiscovMode_Object = MibTableColumn
hicomDiscovMode = _HicomDiscovMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 1, 1, 4),
    _HicomDiscovMode_Type()
)
hicomDiscovMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicomDiscovMode.setStatus("current")
_HicomDiscovTimDat_Type = DisplayString
_HicomDiscovTimDat_Object = MibTableColumn
hicomDiscovTimDat = _HicomDiscovTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 1, 1, 5),
    _HicomDiscovTimDat_Type()
)
hicomDiscovTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomDiscovTimDat.setStatus("current")
_HicomDiscovErrTimDat_Type = DisplayString
_HicomDiscovErrTimDat_Object = MibTableColumn
hicomDiscovErrTimDat = _HicomDiscovErrTimDat_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 1, 1, 6),
    _HicomDiscovErrTimDat_Type()
)
hicomDiscovErrTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomDiscovErrTimDat.setStatus("current")
_HicomDiscInfo_ObjectIdentity = ObjectIdentity
hicomDiscInfo = _HicomDiscInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 2)
)
_HicomDiscSubagentLastMsgNo_Type = Integer32
_HicomDiscSubagentLastMsgNo_Object = MibScalar
hicomDiscSubagentLastMsgNo = _HicomDiscSubagentLastMsgNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 2, 1),
    _HicomDiscSubagentLastMsgNo_Type()
)
hicomDiscSubagentLastMsgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomDiscSubagentLastMsgNo.setStatus("current")
_HicomDiscSubagentLastMsgText_Type = OctetString
_HicomDiscSubagentLastMsgText_Object = MibScalar
hicomDiscSubagentLastMsgText = _HicomDiscSubagentLastMsgText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 9, 2, 2),
    _HicomDiscSubagentLastMsgText_Type()
)
hicomDiscSubagentLastMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hicomDiscSubagentLastMsgText.setStatus("current")
_HicomMibConformance_ObjectIdentity = ObjectIdentity
hicomMibConformance = _HicomMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20)
)
_HicomMibGroups_ObjectIdentity = ObjectIdentity
hicomMibGroups = _HicomMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1)
)
_HicomCntrlTree_ObjectIdentity = ObjectIdentity
hicomCntrlTree = _HicomCntrlTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 0)
)
_HicomSysTree_ObjectIdentity = ObjectIdentity
hicomSysTree = _HicomSysTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 1)
)
_HicomAlarmTree_ObjectIdentity = ObjectIdentity
hicomAlarmTree = _HicomAlarmTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 2)
)
_HicomErrorTree_ObjectIdentity = ObjectIdentity
hicomErrorTree = _HicomErrorTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 3)
)
_HicomAlConfTree_ObjectIdentity = ObjectIdentity
hicomAlConfTree = _HicomAlConfTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 4)
)
_HicomSoftTree_ObjectIdentity = ObjectIdentity
hicomSoftTree = _HicomSoftTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 5)
)
_HicomHardTree_ObjectIdentity = ObjectIdentity
hicomHardTree = _HicomHardTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 6)
)
_HicomTopoTree_ObjectIdentity = ObjectIdentity
hicomTopoTree = _HicomTopoTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 7)
)
_HicomSQLtree_ObjectIdentity = ObjectIdentity
hicomSQLtree = _HicomSQLtree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 8)
)
_HicomDiscovTree_ObjectIdentity = ObjectIdentity
hicomDiscovTree = _HicomDiscovTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 9)
)
_HicomTrapGroup_ObjectIdentity = ObjectIdentity
hicomTrapGroup = _HicomTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21)
)
_HicomTrapVariables_ObjectIdentity = ObjectIdentity
hicomTrapVariables = _HicomTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1)
)
_HicomSystemTrapVariables_ObjectIdentity = ObjectIdentity
hicomSystemTrapVariables = _HicomSystemTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 1)
)
_HicomAlarmTrapVariables_ObjectIdentity = ObjectIdentity
hicomAlarmTrapVariables = _HicomAlarmTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 2)
)
_HicomAlTrpSysPabxId_Type = Integer32
_HicomAlTrpSysPabxId_Object = MibScalar
hicomAlTrpSysPabxId = _HicomAlTrpSysPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 2, 1),
    _HicomAlTrpSysPabxId_Type()
)
hicomAlTrpSysPabxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomAlTrpSysPabxId.setStatus("current")
_HicomAlTrpSysMnemonic_Type = DisplayString
_HicomAlTrpSysMnemonic_Object = MibScalar
hicomAlTrpSysMnemonic = _HicomAlTrpSysMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 2, 2),
    _HicomAlTrpSysMnemonic_Type()
)
hicomAlTrpSysMnemonic.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomAlTrpSysMnemonic.setStatus("current")
_HicomErrorTrapVariables_ObjectIdentity = ObjectIdentity
hicomErrorTrapVariables = _HicomErrorTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 3)
)
_HicomErrTrpPabxId_Type = Integer32
_HicomErrTrpPabxId_Object = MibScalar
hicomErrTrpPabxId = _HicomErrTrpPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 3, 1),
    _HicomErrTrpPabxId_Type()
)
hicomErrTrpPabxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomErrTrpPabxId.setStatus("current")
_HicomErrTrpMnemonic_Type = DisplayString
_HicomErrTrpMnemonic_Object = MibScalar
hicomErrTrpMnemonic = _HicomErrTrpMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 3, 2),
    _HicomErrTrpMnemonic_Type()
)
hicomErrTrpMnemonic.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomErrTrpMnemonic.setStatus("current")
_HicomSWTrapVariables_ObjectIdentity = ObjectIdentity
hicomSWTrapVariables = _HicomSWTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 4)
)
_HicomSWTrpPabxId_Type = Integer32
_HicomSWTrpPabxId_Object = MibScalar
hicomSWTrpPabxId = _HicomSWTrpPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 4, 1),
    _HicomSWTrpPabxId_Type()
)
hicomSWTrpPabxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomSWTrpPabxId.setStatus("current")
_HicomSWTrpPabxMnemonic_Type = DisplayString
_HicomSWTrpPabxMnemonic_Object = MibScalar
hicomSWTrpPabxMnemonic = _HicomSWTrpPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 4, 2),
    _HicomSWTrpPabxMnemonic_Type()
)
hicomSWTrpPabxMnemonic.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomSWTrpPabxMnemonic.setStatus("current")
_HicomAlConfTrapVariables_ObjectIdentity = ObjectIdentity
hicomAlConfTrapVariables = _HicomAlConfTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 5)
)
_HicomHWTrapVariables_ObjectIdentity = ObjectIdentity
hicomHWTrapVariables = _HicomHWTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 6)
)
_HicomHWTrpPabxId_Type = Integer32
_HicomHWTrpPabxId_Object = MibScalar
hicomHWTrpPabxId = _HicomHWTrpPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 6, 1),
    _HicomHWTrpPabxId_Type()
)
hicomHWTrpPabxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomHWTrpPabxId.setStatus("current")
_HicomHWTrpPabxMnemonic_Type = DisplayString
_HicomHWTrpPabxMnemonic_Object = MibScalar
hicomHWTrpPabxMnemonic = _HicomHWTrpPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 6, 2),
    _HicomHWTrpPabxMnemonic_Type()
)
hicomHWTrpPabxMnemonic.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomHWTrpPabxMnemonic.setStatus("current")
_HicomTopoTrapVariables_ObjectIdentity = ObjectIdentity
hicomTopoTrapVariables = _HicomTopoTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 7)
)
_HicomTopoTrpPabxId_Type = Integer32
_HicomTopoTrpPabxId_Object = MibScalar
hicomTopoTrpPabxId = _HicomTopoTrpPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 7, 1),
    _HicomTopoTrpPabxId_Type()
)
hicomTopoTrpPabxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomTopoTrpPabxId.setStatus("current")
_HicomTopoTrpPabxMnemonic_Type = DisplayString
_HicomTopoTrpPabxMnemonic_Object = MibScalar
hicomTopoTrpPabxMnemonic = _HicomTopoTrpPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 7, 2),
    _HicomTopoTrpPabxMnemonic_Type()
)
hicomTopoTrpPabxMnemonic.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomTopoTrpPabxMnemonic.setStatus("current")
_HicomSQLTrapVariables_ObjectIdentity = ObjectIdentity
hicomSQLTrapVariables = _HicomSQLTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 8)
)
_HicomDiscTrapVariables_ObjectIdentity = ObjectIdentity
hicomDiscTrapVariables = _HicomDiscTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 9)
)
_HicomEDTrpPabxId_Type = Integer32
_HicomEDTrpPabxId_Object = MibScalar
hicomEDTrpPabxId = _HicomEDTrpPabxId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 9, 1),
    _HicomEDTrpPabxId_Type()
)
hicomEDTrpPabxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomEDTrpPabxId.setStatus("current")
_HicomEDTrpPabxMnemonic_Type = DisplayString
_HicomEDTrpPabxMnemonic_Object = MibScalar
hicomEDTrpPabxMnemonic = _HicomEDTrpPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 1, 9, 2),
    _HicomEDTrpPabxMnemonic_Type()
)
hicomEDTrpPabxMnemonic.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hicomEDTrpPabxMnemonic.setStatus("current")
_HicomTraps_ObjectIdentity = ObjectIdentity
hicomTraps = _HicomTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2)
)
_HicomSystemTraps_ObjectIdentity = ObjectIdentity
hicomSystemTraps = _HicomSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 1)
)
_HicomAlarmTraps_ObjectIdentity = ObjectIdentity
hicomAlarmTraps = _HicomAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2)
)
_HicomErrorTraps_ObjectIdentity = ObjectIdentity
hicomErrorTraps = _HicomErrorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 3)
)
_HicomAlConfTraps_ObjectIdentity = ObjectIdentity
hicomAlConfTraps = _HicomAlConfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 4)
)
_HicomSWTraps_ObjectIdentity = ObjectIdentity
hicomSWTraps = _HicomSWTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 5)
)
_HicomHWTraps_ObjectIdentity = ObjectIdentity
hicomHWTraps = _HicomHWTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 6)
)
_HicomTopoTraps_ObjectIdentity = ObjectIdentity
hicomTopoTraps = _HicomTopoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 7)
)
_HicomSQLTraps_ObjectIdentity = ObjectIdentity
hicomSQLTraps = _HicomSQLTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 8)
)
_HicomDiscTraps_ObjectIdentity = ObjectIdentity
hicomDiscTraps = _HicomDiscTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 9)
)

# Managed Objects groups

hicomControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 0, 1)
)
hicomControlGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomProxyName"),
        ("SIEMENS-PN-MIB", "hicomAgentVersion"),
        ("SIEMENS-PN-MIB", "hicomMIBVersion"))
)
if mibBuilder.loadTexts:
    hicomControlGroup.setStatus("current")

hicomSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 1, 1)
)
hicomSystemGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomNumHicoms"),
        ("SIEMENS-PN-MIB", "hicomSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomSysConNo"),
        ("SIEMENS-PN-MIB", "hicomSysEstabl"),
        ("SIEMENS-PN-MIB", "hicomSysPosNo"),
        ("SIEMENS-PN-MIB", "hicomSysMnemonic"),
        ("SIEMENS-PN-MIB", "hicomSysCustName"),
        ("SIEMENS-PN-MIB", "hicomSysCbCode"),
        ("SIEMENS-PN-MIB", "hicomSysTelNo"),
        ("SIEMENS-PN-MIB", "hicomSysCutOver"),
        ("SIEMENS-PN-MIB", "hicomSysClnr"),
        ("SIEMENS-PN-MIB", "hicomSysPabxNo"),
        ("SIEMENS-PN-MIB", "hicomSysLocation"),
        ("SIEMENS-PN-MIB", "hicomSysRemark"),
        ("SIEMENS-PN-MIB", "hicomSysSwLic"),
        ("SIEMENS-PN-MIB", "hicomSysSysType"),
        ("SIEMENS-PN-MIB", "hicomSysApsPa"),
        ("SIEMENS-PN-MIB", "hicomSysTimeStamp"),
        ("SIEMENS-PN-MIB", "hicomSysDescription"),
        ("SIEMENS-PN-MIB", "hicomSysVersion"),
        ("SIEMENS-PN-MIB", "hicomSysCustomerSpecific"),
        ("SIEMENS-PN-MIB", "hicomSysStreetAddress"),
        ("SIEMENS-PN-MIB", "hicomSysLineType"),
        ("SIEMENS-PN-MIB", "hicomSysProduct"),
        ("SIEMENS-PN-MIB", "hicomSysCustomerContact"),
        ("SIEMENS-PN-MIB", "hicomSysServiceDistrict"),
        ("SIEMENS-PN-MIB", "hicomSysCustomerContract"),
        ("SIEMENS-PN-MIB", "hicomSysTimeOfLastFm"),
        ("SIEMENS-PN-MIB", "hicomSysHicomSwVersion"),
        ("SIEMENS-PN-MIB", "hicomSysEndWarranty"),
        ("SIEMENS-PN-MIB", "hicomSysBatteryType"),
        ("SIEMENS-PN-MIB", "hicomSysBatteryCapac"),
        ("SIEMENS-PN-MIB", "hicomSysInterface"),
        ("SIEMENS-PN-MIB", "hicomSysSystemRoomTel"),
        ("SIEMENS-PN-MIB", "hicomSysNoType"),
        ("SIEMENS-PN-MIB", "hicomSysCustServer"),
        ("SIEMENS-PN-MIB", "hicomSysCustNoid"),
        ("SIEMENS-PN-MIB", "hicomSysNoName"),
        ("SIEMENS-PN-MIB", "hicomSysRemarkCd"),
        ("SIEMENS-PN-MIB", "hicomSysHSystemRelease"),
        ("SIEMENS-PN-MIB", "hicomSysHcmAmolang"),
        ("SIEMENS-PN-MIB", "hicomSysRemarkCon"),
        ("SIEMENS-PN-MIB", "hicomSysIpAddress"),
        ("SIEMENS-PN-MIB", "hicomSysRemarkCom"),
        ("SIEMENS-PN-MIB", "hicomSysMsvProgNum"),
        ("SIEMENS-PN-MIB", "hicomSysMsvRegNum"),
        ("SIEMENS-PN-MIB", "hicomSysHcEquipNr1"),
        ("SIEMENS-PN-MIB", "hicomSysHcEquipNr2"),
        ("SIEMENS-PN-MIB", "hicomSysDaUrl"),
        ("SIEMENS-PN-MIB", "hicomSysHcmCorrState"),
        ("SIEMENS-PN-MIB", "hicomSysNodeNo"),
        ("SIEMENS-PN-MIB", "hicomSysLang"),
        ("SIEMENS-PN-MIB", "hicomSysMgrNetId"),
        ("SIEMENS-PN-MIB", "hicomSysMgrSubNetId"),
        ("SIEMENS-PN-MIB", "hicomSysMgrPhysNetId"),
        ("SIEMENS-PN-MIB", "hicomSysMgrFlags"),
        ("SIEMENS-PN-MIB", "hicomSysDiscTimeOutEvnt"),
        ("SIEMENS-PN-MIB", "hicomSysDiscAgedData"),
        ("SIEMENS-PN-MIB", "hicomSysDiscComType"),
        ("SIEMENS-PN-MIB", "hicomSysAgentFlags"),
        ("SIEMENS-PN-MIB", "hicomSystemChanges"),
        ("SIEMENS-PN-MIB", "hicomSysSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSysSubagentLastMsgText"),
        ("SIEMENS-PN-MIB", "hicomForSysName"),
        ("SIEMENS-PN-MIB", "hicomForSysNetId"),
        ("SIEMENS-PN-MIB", "hicomForSysSubNetId"),
        ("SIEMENS-PN-MIB", "hicomForSysProvNetId"),
        ("SIEMENS-PN-MIB", "hicomForSysProvSubNetId"),
        ("SIEMENS-PN-MIB", "hicomForSysRowStat"))
)
if mibBuilder.loadTexts:
    hicomSystemGroup.setStatus("current")

hicomAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 2, 1)
)
hicomAlarmsGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlGroup"),
        ("SIEMENS-PN-MIB", "hicomAlSubId"),
        ("SIEMENS-PN-MIB", "hicomAlPriority"),
        ("SIEMENS-PN-MIB", "hicomAlAbsMod"),
        ("SIEMENS-PN-MIB", "hicomAlStatus"),
        ("SIEMENS-PN-MIB", "hicomAlTimDat"),
        ("SIEMENS-PN-MIB", "hicomAlName"),
        ("SIEMENS-PN-MIB", "hicomAlReset"),
        ("SIEMENS-PN-MIB", "hicomAlTimOldDat"),
        ("SIEMENS-PN-MIB", "hicomAlArrivalTimDat"),
        ("SIEMENS-PN-MIB", "hicomAlFilter"),
        ("SIEMENS-PN-MIB", "hicomAlarmsChanges"),
        ("SIEMENS-PN-MIB", "hicomAlFiltConfSwitch"),
        ("SIEMENS-PN-MIB", "hicomAlFiltConfRowStat"),
        ("SIEMENS-PN-MIB", "hicomAlarmSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomAlarmSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    hicomAlarmsGroup.setStatus("current")

hicomAlMirrorUploadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 2, 2)
)
hicomAlMirrorUploadGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlMirrorUploadPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlMirrorUploadMnemonic"),
        ("SIEMENS-PN-MIB", "hicomAlMirrorUploadState"),
        ("SIEMENS-PN-MIB", "hicomAlMirrorUploadStartTimDat"),
        ("SIEMENS-PN-MIB", "hicomAlMirrorUploadErrorTimDat"))
)
if mibBuilder.loadTexts:
    hicomAlMirrorUploadGroup.setStatus("current")

hicomErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 3, 1)
)
hicomErrorGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomErrorPabxId"),
        ("SIEMENS-PN-MIB", "hicomErrorSerialNo"),
        ("SIEMENS-PN-MIB", "hicomErrorMsgId"),
        ("SIEMENS-PN-MIB", "hicomErrorPriority"),
        ("SIEMENS-PN-MIB", "hicomErrorAction"),
        ("SIEMENS-PN-MIB", "hicomErrorAbsMod"),
        ("SIEMENS-PN-MIB", "hicomErrorEvent"),
        ("SIEMENS-PN-MIB", "hicomErrorSubevent"),
        ("SIEMENS-PN-MIB", "hicomErrorCardRef"),
        ("SIEMENS-PN-MIB", "hicomErrorBoardVersion"),
        ("SIEMENS-PN-MIB", "hicomErrorFwType"),
        ("SIEMENS-PN-MIB", "hicomErrorTimDat"),
        ("SIEMENS-PN-MIB", "hicomErrorAlGroup"),
        ("SIEMENS-PN-MIB", "hicomErrorAlSubId"),
        ("SIEMENS-PN-MIB", "hicomErrorOrigText"))
)
if mibBuilder.loadTexts:
    hicomErrorGroup.setStatus("current")

hicomAlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 4, 1)
)
hicomAlConfigGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlConfPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlConfAlGroup"),
        ("SIEMENS-PN-MIB", "hicomAlConfAlSubId"),
        ("SIEMENS-PN-MIB", "hicomAlConfName"),
        ("SIEMENS-PN-MIB", "hicomAlConfThreshold1"),
        ("SIEMENS-PN-MIB", "hicomAlConfThreshold2"),
        ("SIEMENS-PN-MIB", "hicomAlConfTime1"),
        ("SIEMENS-PN-MIB", "hicomAlConfTime2"),
        ("SIEMENS-PN-MIB", "hicomAlConfTimeH"),
        ("SIEMENS-PN-MIB", "hicomAlConfBase"),
        ("SIEMENS-PN-MIB", "hicomAlConfTargetPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlConfTargetAlGroup"),
        ("SIEMENS-PN-MIB", "hicomAlConfTargetAlSubId"),
        ("SIEMENS-PN-MIB", "hicomAlConfTargetLtg"),
        ("SIEMENS-PN-MIB", "hicomAlConfTargetLtu"),
        ("SIEMENS-PN-MIB", "hicomAlConfTargetSlot"),
        ("SIEMENS-PN-MIB", "hicomAlConfTargetTrunkNo"),
        ("SIEMENS-PN-MIB", "hicomAlConfPersonPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlConfPersonAlGroup"),
        ("SIEMENS-PN-MIB", "hicomAlConfPersonAlSubId"),
        ("SIEMENS-PN-MIB", "hicomAlConfPersonExtNo"))
)
if mibBuilder.loadTexts:
    hicomAlConfigGroup.setStatus("current")

hicomErrAlConfInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 4, 2)
)
hicomErrAlConfInfoGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomErrAlConfSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomErrAlConfSubagentLastMsgText"),
        ("SIEMENS-PN-MIB", "hicomErrAlConfResultData"))
)
if mibBuilder.loadTexts:
    hicomErrAlConfInfoGroup.setStatus("current")

hicomAlConfDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 4, 3)
)
hicomAlConfDiscoveryGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlConfChanges"),
        ("SIEMENS-PN-MIB", "hicomAlConfDiscovPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlConfDiscovPabxMnemonic"),
        ("SIEMENS-PN-MIB", "hicomAlConfDiscovStatus"),
        ("SIEMENS-PN-MIB", "hicomAlConfDiscovMode"),
        ("SIEMENS-PN-MIB", "hicomAlConfDiscovTimDat"),
        ("SIEMENS-PN-MIB", "hicomAlConfDiscovErrTimDat"))
)
if mibBuilder.loadTexts:
    hicomAlConfDiscoveryGroup.setStatus("current")

hicomSoftGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 5, 1)
)
hicomSoftGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSoftApsPabxId"),
        ("SIEMENS-PN-MIB", "hicomSoftApsID"),
        ("SIEMENS-PN-MIB", "hicomSoftPatchNo"),
        ("SIEMENS-PN-MIB", "hicomSoftApsPartNo"),
        ("SIEMENS-PN-MIB", "hicomSoftPatchHWMod"),
        ("SIEMENS-PN-MIB", "hicomSoftPatchActType"),
        ("SIEMENS-PN-MIB", "hicomSoftPatchGroup"),
        ("SIEMENS-PN-MIB", "hicomSoftPatchPabxId"))
)
if mibBuilder.loadTexts:
    hicomSoftGroup.setStatus("current")

hicomSoftInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 5, 2)
)
hicomSoftInfoGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSoftSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSoftSubagentLastMsgText"),
        ("SIEMENS-PN-MIB", "hicomSoftResultData"))
)
if mibBuilder.loadTexts:
    hicomSoftInfoGroup.setStatus("current")

hicomSoftDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 5, 3)
)
hicomSoftDiscoveryGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSoftChanges"),
        ("SIEMENS-PN-MIB", "hicomSoftDiscovPabxId"),
        ("SIEMENS-PN-MIB", "hicomSoftDiscovPabxMnemonic"),
        ("SIEMENS-PN-MIB", "hicomSoftDiscovStatus"),
        ("SIEMENS-PN-MIB", "hicomSoftDiscovMode"),
        ("SIEMENS-PN-MIB", "hicomSoftDiscovTimDat"),
        ("SIEMENS-PN-MIB", "hicomSoftDiscovErrTimDat"))
)
if mibBuilder.loadTexts:
    hicomSoftDiscoveryGroup.setStatus("current")

hicomCabinetsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 6, 1)
)
hicomCabinetsGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomCabPabxId"),
        ("SIEMENS-PN-MIB", "hicomCabAddr"),
        ("SIEMENS-PN-MIB", "hicomCabType"),
        ("SIEMENS-PN-MIB", "hicomCabPartNo"),
        ("SIEMENS-PN-MIB", "hicomCabNumShelves"),
        ("SIEMENS-PN-MIB", "hicomFramePabxId"),
        ("SIEMENS-PN-MIB", "hicomFrameCabAddr"),
        ("SIEMENS-PN-MIB", "hicomFrameMntLevel"),
        ("SIEMENS-PN-MIB", "hicomFrameType"),
        ("SIEMENS-PN-MIB", "hicomFramePartNo"),
        ("SIEMENS-PN-MIB", "hicomFramePID1"),
        ("SIEMENS-PN-MIB", "hicomFramePID2"),
        ("SIEMENS-PN-MIB", "hicomFramePID3"),
        ("SIEMENS-PN-MIB", "hicomFrameLTU"),
        ("SIEMENS-PN-MIB", "hicomFrameIpAddr"))
)
if mibBuilder.loadTexts:
    hicomCabinetsGroup.setStatus("current")

hicomPeriperalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 6, 2)
)
hicomPeriperalsGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomPeriphPabxId"),
        ("SIEMENS-PN-MIB", "hicomPeriphContrID"),
        ("SIEMENS-PN-MIB", "hicomPeriphModule"),
        ("SIEMENS-PN-MIB", "hicomPeriphType"),
        ("SIEMENS-PN-MIB", "hicomPeriphSSNo"),
        ("SIEMENS-PN-MIB", "hicomPeriphSize"),
        ("SIEMENS-PN-MIB", "hicomPeriphGran"))
)
if mibBuilder.loadTexts:
    hicomPeriperalsGroup.setStatus("current")

hicomBoardsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 6, 3)
)
hicomBoardsGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomCDSMPabxId"),
        ("SIEMENS-PN-MIB", "hicomCDSMCabAddr"),
        ("SIEMENS-PN-MIB", "hicomCDSMMntLevel"),
        ("SIEMENS-PN-MIB", "hicomCDSMSlotAddr"),
        ("SIEMENS-PN-MIB", "hicomCDSMPartNo"),
        ("SIEMENS-PN-MIB", "hicomCDSMCode"),
        ("SIEMENS-PN-MIB", "hicomCDSMVers"),
        ("SIEMENS-PN-MIB", "hicomCDSMFirmware"),
        ("SIEMENS-PN-MIB", "hicomCDSUPabxId"),
        ("SIEMENS-PN-MIB", "hicomCDSUCabAddr"),
        ("SIEMENS-PN-MIB", "hicomCDSUMntLevel"),
        ("SIEMENS-PN-MIB", "hicomCDSUSlotAddr"),
        ("SIEMENS-PN-MIB", "hicomCDSUPartNo"),
        ("SIEMENS-PN-MIB", "hicomCDSUCode"),
        ("SIEMENS-PN-MIB", "hicomCDSUVers"),
        ("SIEMENS-PN-MIB", "hicomCDSUFirmware"),
        ("SIEMENS-PN-MIB", "hicomBCSMPabxId"),
        ("SIEMENS-PN-MIB", "hicomBCSMMod"),
        ("SIEMENS-PN-MIB", "hicomBCSMSlotAddr"),
        ("SIEMENS-PN-MIB", "hicomBCSMConfBoard"),
        ("SIEMENS-PN-MIB", "hicomBCSMCode"),
        ("SIEMENS-PN-MIB", "hicomBCSMInstBoard"),
        ("SIEMENS-PN-MIB", "hicomBCSMVers"),
        ("SIEMENS-PN-MIB", "hicomBCSMFirmware"),
        ("SIEMENS-PN-MIB", "hicomBCSMStatus"),
        ("SIEMENS-PN-MIB", "hicomBCSUPabxId"),
        ("SIEMENS-PN-MIB", "hicomBCSULTG"),
        ("SIEMENS-PN-MIB", "hicomBCSULTU"),
        ("SIEMENS-PN-MIB", "hicomBCSUSlotAddr"),
        ("SIEMENS-PN-MIB", "hicomBCSUConfBoard"),
        ("SIEMENS-PN-MIB", "hicomBCSUCode"),
        ("SIEMENS-PN-MIB", "hicomBCSUInstBoard"),
        ("SIEMENS-PN-MIB", "hicomBCSUVers"),
        ("SIEMENS-PN-MIB", "hicomBCSUFirmware"),
        ("SIEMENS-PN-MIB", "hicomBCSUStatus"))
)
if mibBuilder.loadTexts:
    hicomBoardsGroup.setStatus("current")

hicomHWInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 6, 4)
)
hicomHWInfoGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomHardSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomHardSubagentLastMsgText"),
        ("SIEMENS-PN-MIB", "hicomHardSubagentResultData"))
)
if mibBuilder.loadTexts:
    hicomHWInfoGroup.setStatus("current")

hicomHWDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 6, 5)
)
hicomHWDiscoveryGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomHWChanges"),
        ("SIEMENS-PN-MIB", "hicomHWDiscovPabxId"),
        ("SIEMENS-PN-MIB", "hicomHWDiscovPabxMnemonic"),
        ("SIEMENS-PN-MIB", "hicomHWDiscovStatus"),
        ("SIEMENS-PN-MIB", "hicomHWDiscovMode"),
        ("SIEMENS-PN-MIB", "hicomHWDiscovTimDat"),
        ("SIEMENS-PN-MIB", "hicomHWDiscovErrTimDat"))
)
if mibBuilder.loadTexts:
    hicomHWDiscoveryGroup.setStatus("current")

hicomTrunkGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 7, 1)
)
hicomTrunkGrpGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomTrunkGrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomTrunkGrpTrunkType"),
        ("SIEMENS-PN-MIB", "hicomTrunkGrpNo"),
        ("SIEMENS-PN-MIB", "hicomTrunkGrpName"),
        ("SIEMENS-PN-MIB", "hicomTrunkGrpMaxNo"),
        ("SIEMENS-PN-MIB", "hicomTrunkGrpDevice"),
        ("SIEMENS-PN-MIB", "hicomTrunkGrpNNodeNo"),
        ("SIEMENS-PN-MIB", "hicomTrunkGrpVNodeNo"),
        ("SIEMENS-PN-MIB", "hicomTrunkGrpAlarms"))
)
if mibBuilder.loadTexts:
    hicomTrunkGrpGroup.setStatus("current")

hicomTrunkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 7, 2)
)
hicomTrunkGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomTrunkPabxId"),
        ("SIEMENS-PN-MIB", "hicomTrunkType"),
        ("SIEMENS-PN-MIB", "hicomTrunkTrunkGrpNo"),
        ("SIEMENS-PN-MIB", "hicomTrunkLtg"),
        ("SIEMENS-PN-MIB", "hicomTrunkLtu"),
        ("SIEMENS-PN-MIB", "hicomTrunkSlot"),
        ("SIEMENS-PN-MIB", "hicomTrunkNo"),
        ("SIEMENS-PN-MIB", "hicomTrunkChannelGrp"),
        ("SIEMENS-PN-MIB", "hicomTrunkChannels"),
        ("SIEMENS-PN-MIB", "hicomTrunkDevice"),
        ("SIEMENS-PN-MIB", "hicomTrunkName"),
        ("SIEMENS-PN-MIB", "hicomTrunkStatOp"),
        ("SIEMENS-PN-MIB", "hicomTrunkSNodeNo"),
        ("SIEMENS-PN-MIB", "hicomTrunkAlSubId"))
)
if mibBuilder.loadTexts:
    hicomTrunkGroup.setStatus("current")

hicomTopoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 7, 3)
)
hicomTopoInfoGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomTopoSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomTopoSubagentLastMsgText"),
        ("SIEMENS-PN-MIB", "hicomTopoSubagentResultData"))
)
if mibBuilder.loadTexts:
    hicomTopoInfoGroup.setStatus("current")

hicomTopoDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 7, 4)
)
hicomTopoDiscoveryGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomTopoChanges"),
        ("SIEMENS-PN-MIB", "hicomTopoDiscovPabxId"),
        ("SIEMENS-PN-MIB", "hicomTopoDiscovPabxMnemonic"),
        ("SIEMENS-PN-MIB", "hicomTopoDiscovStatus"),
        ("SIEMENS-PN-MIB", "hicomTopoDiscovMode"),
        ("SIEMENS-PN-MIB", "hicomTopoDiscovTimDat"),
        ("SIEMENS-PN-MIB", "hicomTopoDiscovErrTimDat"))
)
if mibBuilder.loadTexts:
    hicomTopoDiscoveryGroup.setStatus("current")

hicomKntopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 7, 5)
)
hicomKntopGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomKntopPabxId"),
        ("SIEMENS-PN-MIB", "hicomKntopLtg"),
        ("SIEMENS-PN-MIB", "hicomKntopLtu"),
        ("SIEMENS-PN-MIB", "hicomKntopSlot"),
        ("SIEMENS-PN-MIB", "hicomKntopSatznr"),
        ("SIEMENS-PN-MIB", "hicomKntopBKanalGrp"),
        ("SIEMENS-PN-MIB", "hicomKntopPNodeIndex"),
        ("SIEMENS-PN-MIB", "hicomKntopPLtg"),
        ("SIEMENS-PN-MIB", "hicomKntopPLtu"),
        ("SIEMENS-PN-MIB", "hicomKntopPSlot"),
        ("SIEMENS-PN-MIB", "hicomKntopPSatznr"),
        ("SIEMENS-PN-MIB", "hicomKntopPBKanalGrp"),
        ("SIEMENS-PN-MIB", "hicomKntopPNodeNo"),
        ("SIEMENS-PN-MIB", "hicomKntopBunr"))
)
if mibBuilder.loadTexts:
    hicomKntopGroup.setStatus("current")

hicomSQLsessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 8, 1)
)
hicomSQLsessionGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSQLsessionIdGenerator"),
        ("SIEMENS-PN-MIB", "hicomSQLsessionId"),
        ("SIEMENS-PN-MIB", "hicomSQLsessionState"),
        ("SIEMENS-PN-MIB", "hicomSQLsessionResultSize"),
        ("SIEMENS-PN-MIB", "hicomSQLsessionResultNoLines"),
        ("SIEMENS-PN-MIB", "hicomSQLsessionTimeout"),
        ("SIEMENS-PN-MIB", "hicomSQLsessionStatement"),
        ("SIEMENS-PN-MIB", "hicomSQLsessionWhereClause"))
)
if mibBuilder.loadTexts:
    hicomSQLsessionGroup.setStatus("current")

hicomSQLresultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 8, 2)
)
hicomSQLresultGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSQLresultId"),
        ("SIEMENS-PN-MIB", "hicomSQLresultBlockNo"),
        ("SIEMENS-PN-MIB", "hicomSQLresultData"))
)
if mibBuilder.loadTexts:
    hicomSQLresultGroup.setStatus("current")

hicomSQLinfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 8, 3)
)
hicomSQLinfoGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSQLSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSQLSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    hicomSQLinfoGroup.setStatus("current")

hicomDiscovGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 9, 1)
)
hicomDiscovGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomDiscovPabxId"),
        ("SIEMENS-PN-MIB", "hicomDiscovPabxMnemonic"),
        ("SIEMENS-PN-MIB", "hicomDiscovStatus"),
        ("SIEMENS-PN-MIB", "hicomDiscovMode"),
        ("SIEMENS-PN-MIB", "hicomDiscovTimDat"),
        ("SIEMENS-PN-MIB", "hicomDiscovErrTimDat"))
)
if mibBuilder.loadTexts:
    hicomDiscovGroup.setStatus("current")

hicomDiscInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 20, 1, 9, 2)
)
hicomDiscInfoGroup.setObjects(
      *(("SIEMENS-PN-MIB", "hicomDiscSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomDiscSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    hicomDiscInfoGroup.setStatus("current")


# Notification objects

internalMessageSystemSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 1, 0)
)
internalMessageSystemSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSysSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSysSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalMessageSystemSubagent.setStatus(
        "current"
    )

internalWarningSystemSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 1, 1)
)
internalWarningSystemSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSysSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSysSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalWarningSystemSubagent.setStatus(
        "current"
    )

internalErrorSystemSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 1, 2)
)
internalErrorSystemSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSysSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSysSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalErrorSystemSubagent.setStatus(
        "current"
    )

addHicom = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 1, 10)
)
addHicom.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomSysMnemonic"))
)
if mibBuilder.loadTexts:
    addHicom.setStatus(
        "current"
    )

deleteHicom = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 1, 11)
)
deleteHicom.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomSysMnemonic"))
)
if mibBuilder.loadTexts:
    deleteHicom.setStatus(
        "current"
    )

changeConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 1, 12)
)
changeConfig.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomSysMnemonic"))
)
if mibBuilder.loadTexts:
    changeConfig.setStatus(
        "deprecated"
    )

internalMessageAlarmSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 0)
)
internalMessageAlarmSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlarmSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomAlarmSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalMessageAlarmSubagent.setStatus(
        "current"
    )

internalWarningAlarmSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 1)
)
internalWarningAlarmSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlarmSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomAlarmSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalWarningAlarmSubagent.setStatus(
        "current"
    )

internalErrorAlarmSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 2)
)
internalErrorAlarmSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlarmSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomAlarmSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalErrorAlarmSubagent.setStatus(
        "current"
    )

hicomAlResetInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 20)
)
hicomAlResetInitFailed.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlTrpSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlTrpSysMnemonic"),
        ("SIEMENS-PN-MIB", "hicomAlReset"))
)
if mibBuilder.loadTexts:
    hicomAlResetInitFailed.setStatus(
        "current"
    )

hicomAlUploadMirrorFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 22)
)
hicomAlUploadMirrorFailed.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlTrpSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlTrpSysMnemonic"),
        ("SIEMENS-PN-MIB", "hicomAlMirrorUploadErrorTimDat"))
)
if mibBuilder.loadTexts:
    hicomAlUploadMirrorFailed.setStatus(
        "current"
    )

hicomAlarmOnMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 30)
)
hicomAlarmOnMajor.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlTrpSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlTrpSysMnemonic"),
        ("SIEMENS-PN-MIB", "hicomAlGroup"),
        ("SIEMENS-PN-MIB", "hicomAlSubId"),
        ("SIEMENS-PN-MIB", "hicomAlPriority"),
        ("SIEMENS-PN-MIB", "hicomAlAbsMod"),
        ("SIEMENS-PN-MIB", "hicomAlStatus"),
        ("SIEMENS-PN-MIB", "hicomAlTimDat"),
        ("SIEMENS-PN-MIB", "hicomAlName"))
)
if mibBuilder.loadTexts:
    hicomAlarmOnMajor.setStatus(
        "current"
    )

hicomAlarmOffMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 31)
)
hicomAlarmOffMajor.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlTrpSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlTrpSysMnemonic"),
        ("SIEMENS-PN-MIB", "hicomAlGroup"),
        ("SIEMENS-PN-MIB", "hicomAlSubId"),
        ("SIEMENS-PN-MIB", "hicomAlPriority"),
        ("SIEMENS-PN-MIB", "hicomAlAbsMod"),
        ("SIEMENS-PN-MIB", "hicomAlStatus"),
        ("SIEMENS-PN-MIB", "hicomAlTimDat"),
        ("SIEMENS-PN-MIB", "hicomAlName"))
)
if mibBuilder.loadTexts:
    hicomAlarmOffMajor.setStatus(
        "current"
    )

hicomAlarmOnMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 32)
)
hicomAlarmOnMinor.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlTrpSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlTrpSysMnemonic"),
        ("SIEMENS-PN-MIB", "hicomAlGroup"),
        ("SIEMENS-PN-MIB", "hicomAlSubId"),
        ("SIEMENS-PN-MIB", "hicomAlPriority"),
        ("SIEMENS-PN-MIB", "hicomAlAbsMod"),
        ("SIEMENS-PN-MIB", "hicomAlStatus"),
        ("SIEMENS-PN-MIB", "hicomAlTimDat"),
        ("SIEMENS-PN-MIB", "hicomAlName"))
)
if mibBuilder.loadTexts:
    hicomAlarmOnMinor.setStatus(
        "current"
    )

hicomAlarmOffMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 33)
)
hicomAlarmOffMinor.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlTrpSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlTrpSysMnemonic"),
        ("SIEMENS-PN-MIB", "hicomAlGroup"),
        ("SIEMENS-PN-MIB", "hicomAlSubId"),
        ("SIEMENS-PN-MIB", "hicomAlPriority"),
        ("SIEMENS-PN-MIB", "hicomAlAbsMod"),
        ("SIEMENS-PN-MIB", "hicomAlStatus"),
        ("SIEMENS-PN-MIB", "hicomAlTimDat"),
        ("SIEMENS-PN-MIB", "hicomAlName"))
)
if mibBuilder.loadTexts:
    hicomAlarmOffMinor.setStatus(
        "current"
    )

hicomAlarmOnDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 34)
)
hicomAlarmOnDevice.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlTrpSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlTrpSysMnemonic"),
        ("SIEMENS-PN-MIB", "hicomAlGroup"),
        ("SIEMENS-PN-MIB", "hicomAlSubId"),
        ("SIEMENS-PN-MIB", "hicomAlPriority"),
        ("SIEMENS-PN-MIB", "hicomAlAbsMod"),
        ("SIEMENS-PN-MIB", "hicomAlStatus"),
        ("SIEMENS-PN-MIB", "hicomAlTimDat"),
        ("SIEMENS-PN-MIB", "hicomAlName"))
)
if mibBuilder.loadTexts:
    hicomAlarmOnDevice.setStatus(
        "current"
    )

hicomAlarmOffDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 2, 35)
)
hicomAlarmOffDevice.setObjects(
      *(("SIEMENS-PN-MIB", "hicomAlTrpSysPabxId"),
        ("SIEMENS-PN-MIB", "hicomAlTrpSysMnemonic"),
        ("SIEMENS-PN-MIB", "hicomAlGroup"),
        ("SIEMENS-PN-MIB", "hicomAlSubId"),
        ("SIEMENS-PN-MIB", "hicomAlPriority"),
        ("SIEMENS-PN-MIB", "hicomAlAbsMod"),
        ("SIEMENS-PN-MIB", "hicomAlStatus"),
        ("SIEMENS-PN-MIB", "hicomAlTimDat"),
        ("SIEMENS-PN-MIB", "hicomAlName"))
)
if mibBuilder.loadTexts:
    hicomAlarmOffDevice.setStatus(
        "current"
    )

internalMessageErrAlConfSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 3, 0)
)
internalMessageErrAlConfSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomErrAlConfSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomErrAlConfSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalMessageErrAlConfSubagent.setStatus(
        "current"
    )

internalWarningErrAlConfSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 3, 1)
)
internalWarningErrAlConfSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomErrAlConfSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomErrAlConfSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalWarningErrAlConfSubagent.setStatus(
        "current"
    )

internalErrorErrAlConfSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 3, 2)
)
internalErrorErrAlConfSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomErrAlConfSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomErrAlConfSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalErrorErrAlConfSubagent.setStatus(
        "current"
    )

hicomAlConfDiscovSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 3, 10)
)
hicomAlConfDiscovSucc.setObjects(
      *(("SIEMENS-PN-MIB", "hicomErrTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomErrTrpMnemonic"))
)
if mibBuilder.loadTexts:
    hicomAlConfDiscovSucc.setStatus(
        "current"
    )

hicomAlConfDiscovErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 3, 11)
)
hicomAlConfDiscovErr.setObjects(
      *(("SIEMENS-PN-MIB", "hicomErrTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomErrTrpMnemonic"))
)
if mibBuilder.loadTexts:
    hicomAlConfDiscovErr.setStatus(
        "current"
    )

hicomAlConfDiscovBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 3, 19)
)
hicomAlConfDiscovBusy.setObjects(
      *(("SIEMENS-PN-MIB", "hicomErrTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomErrTrpMnemonic"))
)
if mibBuilder.loadTexts:
    hicomAlConfDiscovBusy.setStatus(
        "current"
    )

hicomErrorMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 3, 20)
)
hicomErrorMsg.setObjects(
      *(("SIEMENS-PN-MIB", "hicomErrorPabxId"),
        ("SIEMENS-PN-MIB", "hicomErrorAlGroup"),
        ("SIEMENS-PN-MIB", "hicomErrorAlSubId"),
        ("SIEMENS-PN-MIB", "hicomErrorSerialNo"),
        ("SIEMENS-PN-MIB", "hicomErrorMsgId"),
        ("SIEMENS-PN-MIB", "hicomErrorPriority"),
        ("SIEMENS-PN-MIB", "hicomErrorAction"),
        ("SIEMENS-PN-MIB", "hicomErrorAbsMod"),
        ("SIEMENS-PN-MIB", "hicomErrorEvent"),
        ("SIEMENS-PN-MIB", "hicomErrorSubevent"),
        ("SIEMENS-PN-MIB", "hicomErrorCardRef"),
        ("SIEMENS-PN-MIB", "hicomErrorBoardVersion"),
        ("SIEMENS-PN-MIB", "hicomErrorFwType"),
        ("SIEMENS-PN-MIB", "hicomErrorTimDat"),
        ("SIEMENS-PN-MIB", "hicomErrTrpMnemonic"))
)
if mibBuilder.loadTexts:
    hicomErrorMsg.setStatus(
        "current"
    )

internalMessageSWSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 5, 0)
)
internalMessageSWSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSoftSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSoftSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalMessageSWSubagent.setStatus(
        "current"
    )

internalWarningSWSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 5, 1)
)
internalWarningSWSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSoftSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSoftSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalWarningSWSubagent.setStatus(
        "current"
    )

internalErrorSWSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 5, 2)
)
internalErrorSWSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSoftSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSoftSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalErrorSWSubagent.setStatus(
        "current"
    )

hicomSoftDiscovSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 5, 10)
)
hicomSoftDiscovSucc.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSWTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomSWTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomSoftDiscovSucc.setStatus(
        "current"
    )

hicomSoftDiscovErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 5, 11)
)
hicomSoftDiscovErr.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSWTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomSWTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomSoftDiscovErr.setStatus(
        "current"
    )

hicomSoftDiscovBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 5, 19)
)
hicomSoftDiscovBusy.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSWTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomSWTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomSoftDiscovBusy.setStatus(
        "current"
    )

internalMessageHWSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 6, 0)
)
internalMessageHWSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomHardSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomHardSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalMessageHWSubagent.setStatus(
        "current"
    )

internalWarningHWSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 6, 1)
)
internalWarningHWSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomHardSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomHardSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalWarningHWSubagent.setStatus(
        "current"
    )

internalErrorHWSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 6, 2)
)
internalErrorHWSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomHardSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomHardSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalErrorHWSubagent.setStatus(
        "current"
    )

hicomHWDiscovSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 6, 10)
)
hicomHWDiscovSucc.setObjects(
      *(("SIEMENS-PN-MIB", "hicomHWTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomHWTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomHWDiscovSucc.setStatus(
        "current"
    )

hicomHWDiscovErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 6, 11)
)
hicomHWDiscovErr.setObjects(
      *(("SIEMENS-PN-MIB", "hicomHWTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomHWTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomHWDiscovErr.setStatus(
        "current"
    )

hicomHWDiscovBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 6, 19)
)
hicomHWDiscovBusy.setObjects(
      *(("SIEMENS-PN-MIB", "hicomHWTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomHWTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomHWDiscovBusy.setStatus(
        "current"
    )

internalMessageTopoSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 7, 0)
)
internalMessageTopoSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomTopoSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomTopoSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalMessageTopoSubagent.setStatus(
        "current"
    )

internalWarningTopoSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 7, 1)
)
internalWarningTopoSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomTopoSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomTopoSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalWarningTopoSubagent.setStatus(
        "current"
    )

internalErrorTopoSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 7, 2)
)
internalErrorTopoSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomTopoSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomTopoSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalErrorTopoSubagent.setStatus(
        "current"
    )

hicomTopoDiscovSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 7, 10)
)
hicomTopoDiscovSucc.setObjects(
      *(("SIEMENS-PN-MIB", "hicomTopoTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomTopoTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomTopoDiscovSucc.setStatus(
        "current"
    )

hicomTopoDiscovErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 7, 11)
)
hicomTopoDiscovErr.setObjects(
      *(("SIEMENS-PN-MIB", "hicomTopoTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomTopoTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomTopoDiscovErr.setStatus(
        "current"
    )

hicomTopoDiscovBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 7, 19)
)
hicomTopoDiscovBusy.setObjects(
      *(("SIEMENS-PN-MIB", "hicomTopoTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomTopoTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomTopoDiscovBusy.setStatus(
        "current"
    )

internalMessageSQLSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 8, 0)
)
internalMessageSQLSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSQLSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSQLSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalMessageSQLSubagent.setStatus(
        "current"
    )

internalWarningSQLSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 8, 1)
)
internalWarningSQLSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSQLSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSQLSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalWarningSQLSubagent.setStatus(
        "current"
    )

internalErrorSQLSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 8, 2)
)
internalErrorSQLSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSQLSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomSQLSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalErrorSQLSubagent.setStatus(
        "current"
    )

hicomSQLsessionFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 8, 20)
)
hicomSQLsessionFinished.setObjects(
      *(("SIEMENS-PN-MIB", "hicomSQLsessionId"),
        ("SIEMENS-PN-MIB", "hicomSQLsessionState"),
        ("SIEMENS-PN-MIB", "hicomSQLsessionResultSize"),
        ("SIEMENS-PN-MIB", "hicomSQLsessionResultNoLines"))
)
if mibBuilder.loadTexts:
    hicomSQLsessionFinished.setStatus(
        "current"
    )

internalMessageDiscSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 9, 0)
)
internalMessageDiscSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomDiscSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomDiscSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalMessageDiscSubagent.setStatus(
        "current"
    )

internalWarningDiscSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 9, 1)
)
internalWarningDiscSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomDiscSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomDiscSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalWarningDiscSubagent.setStatus(
        "current"
    )

internalErrorDiscSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 9, 2)
)
internalErrorDiscSubagent.setObjects(
      *(("SIEMENS-PN-MIB", "hicomDiscSubagentLastMsgNo"),
        ("SIEMENS-PN-MIB", "hicomDiscSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalErrorDiscSubagent.setStatus(
        "current"
    )

hicomErrDeleteSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 9, 10)
)
hicomErrDeleteSucc.setObjects(
      *(("SIEMENS-PN-MIB", "hicomEDTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomEDTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomErrDeleteSucc.setStatus(
        "current"
    )

hicomErrDeleteErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 9, 11)
)
hicomErrDeleteErr.setObjects(
      *(("SIEMENS-PN-MIB", "hicomEDTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomEDTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomErrDeleteErr.setStatus(
        "current"
    )

hicomErrDeleteBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 2, 1, 21, 2, 9, 19)
)
hicomErrDeleteBusy.setObjects(
      *(("SIEMENS-PN-MIB", "hicomEDTrpPabxId"),
        ("SIEMENS-PN-MIB", "hicomEDTrpPabxMnemonic"))
)
if mibBuilder.loadTexts:
    hicomErrDeleteBusy.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIEMENS-PN-MIB",
    **{"DiscoveryStates": DiscoveryStates,
       "DiscoveryModes": DiscoveryModes,
       "AlarmFilterStates": AlarmFilterStates,
       "AlarmPriorities": AlarmPriorities,
       "TrunkTypes": TrunkTypes,
       "sni": sni,
       "siemensUnits": siemensUnits,
       "pn": pn,
       "hicomMib": hicomMib,
       "hicomControl": hicomControl,
       "hicomProxyName": hicomProxyName,
       "hicomAgentVersion": hicomAgentVersion,
       "hicomMIBVersion": hicomMIBVersion,
       "hicomSystem": hicomSystem,
       "hicomNumHicoms": hicomNumHicoms,
       "hicomSystemChanges": hicomSystemChanges,
       "hicomSysTable": hicomSysTable,
       "hicomSysEntry": hicomSysEntry,
       "hicomSysPabxId": hicomSysPabxId,
       "hicomSysConNo": hicomSysConNo,
       "hicomSysEstabl": hicomSysEstabl,
       "hicomSysPosNo": hicomSysPosNo,
       "hicomSysMnemonic": hicomSysMnemonic,
       "hicomSysCustName": hicomSysCustName,
       "hicomSysCbCode": hicomSysCbCode,
       "hicomSysTelNo": hicomSysTelNo,
       "hicomSysCutOver": hicomSysCutOver,
       "hicomSysClnr": hicomSysClnr,
       "hicomSysPabxNo": hicomSysPabxNo,
       "hicomSysLocation": hicomSysLocation,
       "hicomSysRemark": hicomSysRemark,
       "hicomSysSwLic": hicomSysSwLic,
       "hicomSysSysType": hicomSysSysType,
       "hicomSysApsPa": hicomSysApsPa,
       "hicomSysTimeStamp": hicomSysTimeStamp,
       "hicomSysDescription": hicomSysDescription,
       "hicomSysVersion": hicomSysVersion,
       "hicomSysCustomerSpecific": hicomSysCustomerSpecific,
       "hicomSysStreetAddress": hicomSysStreetAddress,
       "hicomSysLineType": hicomSysLineType,
       "hicomSysProduct": hicomSysProduct,
       "hicomSysCustomerContact": hicomSysCustomerContact,
       "hicomSysServiceDistrict": hicomSysServiceDistrict,
       "hicomSysCustomerContract": hicomSysCustomerContract,
       "hicomSysTimeOfLastFm": hicomSysTimeOfLastFm,
       "hicomSysHicomSwVersion": hicomSysHicomSwVersion,
       "hicomSysEndWarranty": hicomSysEndWarranty,
       "hicomSysBatteryType": hicomSysBatteryType,
       "hicomSysBatteryCapac": hicomSysBatteryCapac,
       "hicomSysInterface": hicomSysInterface,
       "hicomSysSystemRoomTel": hicomSysSystemRoomTel,
       "hicomSysNoType": hicomSysNoType,
       "hicomSysCustServer": hicomSysCustServer,
       "hicomSysCustNoid": hicomSysCustNoid,
       "hicomSysNoName": hicomSysNoName,
       "hicomSysRemarkCd": hicomSysRemarkCd,
       "hicomSysHSystemRelease": hicomSysHSystemRelease,
       "hicomSysHcmAmolang": hicomSysHcmAmolang,
       "hicomSysRemarkCon": hicomSysRemarkCon,
       "hicomSysIpAddress": hicomSysIpAddress,
       "hicomSysRemarkCom": hicomSysRemarkCom,
       "hicomSysMsvProgNum": hicomSysMsvProgNum,
       "hicomSysMsvRegNum": hicomSysMsvRegNum,
       "hicomSysHcEquipNr1": hicomSysHcEquipNr1,
       "hicomSysHcEquipNr2": hicomSysHcEquipNr2,
       "hicomSysDaUrl": hicomSysDaUrl,
       "hicomSysHcmCorrState": hicomSysHcmCorrState,
       "hicomSysNodeNo": hicomSysNodeNo,
       "hicomSysLang": hicomSysLang,
       "hicomSysMgrNetId": hicomSysMgrNetId,
       "hicomSysMgrSubNetId": hicomSysMgrSubNetId,
       "hicomSysMgrPhysNetId": hicomSysMgrPhysNetId,
       "hicomSysMgrFlags": hicomSysMgrFlags,
       "hicomSysDiscTimeOutEvnt": hicomSysDiscTimeOutEvnt,
       "hicomSysDiscAgedData": hicomSysDiscAgedData,
       "hicomSysDiscComType": hicomSysDiscComType,
       "hicomSysAgentFlags": hicomSysAgentFlags,
       "hicomSysSubagentLastMsgNo": hicomSysSubagentLastMsgNo,
       "hicomSysSubagentLastMsgText": hicomSysSubagentLastMsgText,
       "hicomForeignSysTable": hicomForeignSysTable,
       "hicomForeignSysEntry": hicomForeignSysEntry,
       "hicomForSysPhysNetId": hicomForSysPhysNetId,
       "hicomForSysNodeNo": hicomForSysNodeNo,
       "hicomForSysName": hicomForSysName,
       "hicomForSysNetId": hicomForSysNetId,
       "hicomForSysSubNetId": hicomForSysSubNetId,
       "hicomForSysProvNetId": hicomForSysProvNetId,
       "hicomForSysProvSubNetId": hicomForSysProvSubNetId,
       "hicomForSysRowStat": hicomForSysRowStat,
       "hicomAlarms": hicomAlarms,
       "hicomAlarmsChanges": hicomAlarmsChanges,
       "hicomAlTable": hicomAlTable,
       "hicomAlEntry": hicomAlEntry,
       "hicomAlFilter": hicomAlFilter,
       "hicomAlStatus": hicomAlStatus,
       "hicomAlPabxId": hicomAlPabxId,
       "hicomAlGroup": hicomAlGroup,
       "hicomAlSubId": hicomAlSubId,
       "hicomAlPriority": hicomAlPriority,
       "hicomAlAbsMod": hicomAlAbsMod,
       "hicomAlTimDat": hicomAlTimDat,
       "hicomAlName": hicomAlName,
       "hicomAlReset": hicomAlReset,
       "hicomAlTimOldDat": hicomAlTimOldDat,
       "hicomAlArrivalTimDat": hicomAlArrivalTimDat,
       "hicomAlFiltConfTable": hicomAlFiltConfTable,
       "hicomAlFiltConfEntry": hicomAlFiltConfEntry,
       "hicomAlFiltConfPabxId": hicomAlFiltConfPabxId,
       "hicomAlFiltConfGroup": hicomAlFiltConfGroup,
       "hicomAlFiltConfSubId": hicomAlFiltConfSubId,
       "hicomAlFiltConfPriority": hicomAlFiltConfPriority,
       "hicomAlFiltConfSwitch": hicomAlFiltConfSwitch,
       "hicomAlFiltConfRowStat": hicomAlFiltConfRowStat,
       "hicomAlarmSubagentLastMsgNo": hicomAlarmSubagentLastMsgNo,
       "hicomAlarmSubagentLastMsgText": hicomAlarmSubagentLastMsgText,
       "hicomAlMirrorUploadTable": hicomAlMirrorUploadTable,
       "hicomAlMirrorUploadEntry": hicomAlMirrorUploadEntry,
       "hicomAlMirrorUploadPabxId": hicomAlMirrorUploadPabxId,
       "hicomAlMirrorUploadMnemonic": hicomAlMirrorUploadMnemonic,
       "hicomAlMirrorUploadState": hicomAlMirrorUploadState,
       "hicomAlMirrorUploadStartTimDat": hicomAlMirrorUploadStartTimDat,
       "hicomAlMirrorUploadErrorTimDat": hicomAlMirrorUploadErrorTimDat,
       "hicomErrors": hicomErrors,
       "hicomErrorTable": hicomErrorTable,
       "hicomErrorEntry": hicomErrorEntry,
       "hicomErrorPabxId": hicomErrorPabxId,
       "hicomErrorAlGroup": hicomErrorAlGroup,
       "hicomErrorAlSubId": hicomErrorAlSubId,
       "hicomErrorSerialNo": hicomErrorSerialNo,
       "hicomErrorMsgId": hicomErrorMsgId,
       "hicomErrorPriority": hicomErrorPriority,
       "hicomErrorAction": hicomErrorAction,
       "hicomErrorAbsMod": hicomErrorAbsMod,
       "hicomErrorEvent": hicomErrorEvent,
       "hicomErrorSubevent": hicomErrorSubevent,
       "hicomErrorCardRef": hicomErrorCardRef,
       "hicomErrorBoardVersion": hicomErrorBoardVersion,
       "hicomErrorFwType": hicomErrorFwType,
       "hicomErrorTimDat": hicomErrorTimDat,
       "hicomErrorOrigText": hicomErrorOrigText,
       "hicomAlConf": hicomAlConf,
       "hicomAlConfig": hicomAlConfig,
       "hicomAlConfTable": hicomAlConfTable,
       "hicomAlConfEntry": hicomAlConfEntry,
       "hicomAlConfPabxId": hicomAlConfPabxId,
       "hicomAlConfAlGroup": hicomAlConfAlGroup,
       "hicomAlConfAlSubId": hicomAlConfAlSubId,
       "hicomAlConfName": hicomAlConfName,
       "hicomAlConfThreshold1": hicomAlConfThreshold1,
       "hicomAlConfThreshold2": hicomAlConfThreshold2,
       "hicomAlConfTime1": hicomAlConfTime1,
       "hicomAlConfTime2": hicomAlConfTime2,
       "hicomAlConfTimeH": hicomAlConfTimeH,
       "hicomAlConfBase": hicomAlConfBase,
       "hicomAlConfPersonTable": hicomAlConfPersonTable,
       "hicomAlConfPersonEntry": hicomAlConfPersonEntry,
       "hicomAlConfPersonPabxId": hicomAlConfPersonPabxId,
       "hicomAlConfPersonAlGroup": hicomAlConfPersonAlGroup,
       "hicomAlConfPersonAlSubId": hicomAlConfPersonAlSubId,
       "hicomAlConfPersonExtNo": hicomAlConfPersonExtNo,
       "hicomAlConfTargetTable": hicomAlConfTargetTable,
       "hicomAlConfTargetEntry": hicomAlConfTargetEntry,
       "hicomAlConfTargetPabxId": hicomAlConfTargetPabxId,
       "hicomAlConfTargetAlGroup": hicomAlConfTargetAlGroup,
       "hicomAlConfTargetAlSubId": hicomAlConfTargetAlSubId,
       "hicomAlConfTargetLtg": hicomAlConfTargetLtg,
       "hicomAlConfTargetLtu": hicomAlConfTargetLtu,
       "hicomAlConfTargetSlot": hicomAlConfTargetSlot,
       "hicomAlConfTargetTrunkNo": hicomAlConfTargetTrunkNo,
       "hicomErrAlConfInfo": hicomErrAlConfInfo,
       "hicomErrAlConfSubagentLastMsgNo": hicomErrAlConfSubagentLastMsgNo,
       "hicomErrAlConfSubagentLastMsgText": hicomErrAlConfSubagentLastMsgText,
       "hicomErrAlConfResultData": hicomErrAlConfResultData,
       "hicomAlConfDiscovery": hicomAlConfDiscovery,
       "hicomAlConfChanges": hicomAlConfChanges,
       "hicomAlConfDiscovTable": hicomAlConfDiscovTable,
       "hicomAlConfDiscovEntry": hicomAlConfDiscovEntry,
       "hicomAlConfDiscovPabxId": hicomAlConfDiscovPabxId,
       "hicomAlConfDiscovPabxMnemonic": hicomAlConfDiscovPabxMnemonic,
       "hicomAlConfDiscovStatus": hicomAlConfDiscovStatus,
       "hicomAlConfDiscovMode": hicomAlConfDiscovMode,
       "hicomAlConfDiscovTimDat": hicomAlConfDiscovTimDat,
       "hicomAlConfDiscovErrTimDat": hicomAlConfDiscovErrTimDat,
       "hicomSoft": hicomSoft,
       "hicomSoftAps": hicomSoftAps,
       "hicomSoftApsTable": hicomSoftApsTable,
       "hicomSoftApsEntry": hicomSoftApsEntry,
       "hicomSoftApsPabxId": hicomSoftApsPabxId,
       "hicomSoftApsID": hicomSoftApsID,
       "hicomSoftApsPartNo": hicomSoftApsPartNo,
       "hicomSoftPatchTable": hicomSoftPatchTable,
       "hicomSoftPatchEntry": hicomSoftPatchEntry,
       "hicomSoftPatchPabxId": hicomSoftPatchPabxId,
       "hicomSoftPatchNo": hicomSoftPatchNo,
       "hicomSoftPatchHWMod": hicomSoftPatchHWMod,
       "hicomSoftPatchActType": hicomSoftPatchActType,
       "hicomSoftPatchGroup": hicomSoftPatchGroup,
       "hicomSoftInfo": hicomSoftInfo,
       "hicomSoftSubagentLastMsgNo": hicomSoftSubagentLastMsgNo,
       "hicomSoftSubagentLastMsgText": hicomSoftSubagentLastMsgText,
       "hicomSoftResultData": hicomSoftResultData,
       "hicomSoftDiscovery": hicomSoftDiscovery,
       "hicomSoftChanges": hicomSoftChanges,
       "hicomSoftDiscovTable": hicomSoftDiscovTable,
       "hicomSoftDiscovEntry": hicomSoftDiscovEntry,
       "hicomSoftDiscovPabxId": hicomSoftDiscovPabxId,
       "hicomSoftDiscovPabxMnemonic": hicomSoftDiscovPabxMnemonic,
       "hicomSoftDiscovStatus": hicomSoftDiscovStatus,
       "hicomSoftDiscovMode": hicomSoftDiscovMode,
       "hicomSoftDiscovTimDat": hicomSoftDiscovTimDat,
       "hicomSoftDiscovErrTimDat": hicomSoftDiscovErrTimDat,
       "hicomHard": hicomHard,
       "hicomCabinets": hicomCabinets,
       "hicomCabTable": hicomCabTable,
       "hicomCabEntry": hicomCabEntry,
       "hicomCabPabxId": hicomCabPabxId,
       "hicomCabAddr": hicomCabAddr,
       "hicomCabType": hicomCabType,
       "hicomCabPartNo": hicomCabPartNo,
       "hicomCabNumShelves": hicomCabNumShelves,
       "hicomFrameTable": hicomFrameTable,
       "hicomFrameEntry": hicomFrameEntry,
       "hicomFramePabxId": hicomFramePabxId,
       "hicomFrameCabAddr": hicomFrameCabAddr,
       "hicomFrameMntLevel": hicomFrameMntLevel,
       "hicomFrameType": hicomFrameType,
       "hicomFramePartNo": hicomFramePartNo,
       "hicomFramePID1": hicomFramePID1,
       "hicomFramePID2": hicomFramePID2,
       "hicomFramePID3": hicomFramePID3,
       "hicomFrameLTU": hicomFrameLTU,
       "hicomFrameIpAddr": hicomFrameIpAddr,
       "hicomPeripherals": hicomPeripherals,
       "hicomPeriphTable": hicomPeriphTable,
       "hicomPeriphEntry": hicomPeriphEntry,
       "hicomPeriphPabxId": hicomPeriphPabxId,
       "hicomPeriphContrID": hicomPeriphContrID,
       "hicomPeriphModule": hicomPeriphModule,
       "hicomPeriphType": hicomPeriphType,
       "hicomPeriphSSNo": hicomPeriphSSNo,
       "hicomPeriphSize": hicomPeriphSize,
       "hicomPeriphGran": hicomPeriphGran,
       "hicomBoards": hicomBoards,
       "hicomCDSMTable": hicomCDSMTable,
       "hicomCDSMEntry": hicomCDSMEntry,
       "hicomCDSMPabxId": hicomCDSMPabxId,
       "hicomCDSMCabAddr": hicomCDSMCabAddr,
       "hicomCDSMMntLevel": hicomCDSMMntLevel,
       "hicomCDSMSlotAddr": hicomCDSMSlotAddr,
       "hicomCDSMPartNo": hicomCDSMPartNo,
       "hicomCDSMCode": hicomCDSMCode,
       "hicomCDSMVers": hicomCDSMVers,
       "hicomCDSMFirmware": hicomCDSMFirmware,
       "hicomCDSUTable": hicomCDSUTable,
       "hicomCDSUEntry": hicomCDSUEntry,
       "hicomCDSUPabxId": hicomCDSUPabxId,
       "hicomCDSUCabAddr": hicomCDSUCabAddr,
       "hicomCDSUMntLevel": hicomCDSUMntLevel,
       "hicomCDSUSlotAddr": hicomCDSUSlotAddr,
       "hicomCDSUPartNo": hicomCDSUPartNo,
       "hicomCDSUCode": hicomCDSUCode,
       "hicomCDSUVers": hicomCDSUVers,
       "hicomCDSUFirmware": hicomCDSUFirmware,
       "hicomBCSMTable": hicomBCSMTable,
       "hicomBCSMEntry": hicomBCSMEntry,
       "hicomBCSMPabxId": hicomBCSMPabxId,
       "hicomBCSMMod": hicomBCSMMod,
       "hicomBCSMSlotAddr": hicomBCSMSlotAddr,
       "hicomBCSMConfBoard": hicomBCSMConfBoard,
       "hicomBCSMCode": hicomBCSMCode,
       "hicomBCSMInstBoard": hicomBCSMInstBoard,
       "hicomBCSMVers": hicomBCSMVers,
       "hicomBCSMFirmware": hicomBCSMFirmware,
       "hicomBCSMStatus": hicomBCSMStatus,
       "hicomBCSUTable": hicomBCSUTable,
       "hicomBCSUEntry": hicomBCSUEntry,
       "hicomBCSUPabxId": hicomBCSUPabxId,
       "hicomBCSULTG": hicomBCSULTG,
       "hicomBCSULTU": hicomBCSULTU,
       "hicomBCSUSlotAddr": hicomBCSUSlotAddr,
       "hicomBCSUConfBoard": hicomBCSUConfBoard,
       "hicomBCSUCode": hicomBCSUCode,
       "hicomBCSUInstBoard": hicomBCSUInstBoard,
       "hicomBCSUVers": hicomBCSUVers,
       "hicomBCSUFirmware": hicomBCSUFirmware,
       "hicomBCSUStatus": hicomBCSUStatus,
       "hicomHWInfo": hicomHWInfo,
       "hicomHardSubagentLastMsgNo": hicomHardSubagentLastMsgNo,
       "hicomHardSubagentLastMsgText": hicomHardSubagentLastMsgText,
       "hicomHardSubagentResultData": hicomHardSubagentResultData,
       "hicomHWDiscovery": hicomHWDiscovery,
       "hicomHWChanges": hicomHWChanges,
       "hicomHWDiscovTable": hicomHWDiscovTable,
       "hicomHWDiscovEntry": hicomHWDiscovEntry,
       "hicomHWDiscovPabxId": hicomHWDiscovPabxId,
       "hicomHWDiscovPabxMnemonic": hicomHWDiscovPabxMnemonic,
       "hicomHWDiscovStatus": hicomHWDiscovStatus,
       "hicomHWDiscovMode": hicomHWDiscovMode,
       "hicomHWDiscovTimDat": hicomHWDiscovTimDat,
       "hicomHWDiscovErrTimDat": hicomHWDiscovErrTimDat,
       "hicomTopo": hicomTopo,
       "hicomTrunkGrp": hicomTrunkGrp,
       "hicomTrunkGrpTable": hicomTrunkGrpTable,
       "hicomTrunkGrpEntry": hicomTrunkGrpEntry,
       "hicomTrunkGrpPabxId": hicomTrunkGrpPabxId,
       "hicomTrunkGrpNo": hicomTrunkGrpNo,
       "hicomTrunkGrpNNodeNo": hicomTrunkGrpNNodeNo,
       "hicomTrunkGrpVNodeNo": hicomTrunkGrpVNodeNo,
       "hicomTrunkGrpTrunkType": hicomTrunkGrpTrunkType,
       "hicomTrunkGrpMaxNo": hicomTrunkGrpMaxNo,
       "hicomTrunkGrpName": hicomTrunkGrpName,
       "hicomTrunkGrpDevice": hicomTrunkGrpDevice,
       "hicomTrunkGrpAlarms": hicomTrunkGrpAlarms,
       "hicomTrunk": hicomTrunk,
       "hicomTrunkTable": hicomTrunkTable,
       "hicomTrunkEntry": hicomTrunkEntry,
       "hicomTrunkPabxId": hicomTrunkPabxId,
       "hicomTrunkType": hicomTrunkType,
       "hicomTrunkTrunkGrpNo": hicomTrunkTrunkGrpNo,
       "hicomTrunkLtg": hicomTrunkLtg,
       "hicomTrunkLtu": hicomTrunkLtu,
       "hicomTrunkSlot": hicomTrunkSlot,
       "hicomTrunkNo": hicomTrunkNo,
       "hicomTrunkChannelGrp": hicomTrunkChannelGrp,
       "hicomTrunkSNodeNo": hicomTrunkSNodeNo,
       "hicomTrunkStatOp": hicomTrunkStatOp,
       "hicomTrunkAlSubId": hicomTrunkAlSubId,
       "hicomTrunkChannels": hicomTrunkChannels,
       "hicomTrunkDevice": hicomTrunkDevice,
       "hicomTrunkName": hicomTrunkName,
       "hicomTopoInfo": hicomTopoInfo,
       "hicomTopoSubagentLastMsgNo": hicomTopoSubagentLastMsgNo,
       "hicomTopoSubagentLastMsgText": hicomTopoSubagentLastMsgText,
       "hicomTopoSubagentResultData": hicomTopoSubagentResultData,
       "hicomTopoDiscovery": hicomTopoDiscovery,
       "hicomTopoChanges": hicomTopoChanges,
       "hicomTopoDiscovTable": hicomTopoDiscovTable,
       "hicomTopoDiscovEntry": hicomTopoDiscovEntry,
       "hicomTopoDiscovPabxId": hicomTopoDiscovPabxId,
       "hicomTopoDiscovPabxMnemonic": hicomTopoDiscovPabxMnemonic,
       "hicomTopoDiscovStatus": hicomTopoDiscovStatus,
       "hicomTopoDiscovMode": hicomTopoDiscovMode,
       "hicomTopoDiscovTimDat": hicomTopoDiscovTimDat,
       "hicomTopoDiscovErrTimDat": hicomTopoDiscovErrTimDat,
       "hicomKntop": hicomKntop,
       "hicomKntopTable": hicomKntopTable,
       "hicomKntopEntry": hicomKntopEntry,
       "hicomKntopPabxId": hicomKntopPabxId,
       "hicomKntopLtg": hicomKntopLtg,
       "hicomKntopLtu": hicomKntopLtu,
       "hicomKntopSlot": hicomKntopSlot,
       "hicomKntopSatznr": hicomKntopSatznr,
       "hicomKntopBKanalGrp": hicomKntopBKanalGrp,
       "hicomKntopPNodeIndex": hicomKntopPNodeIndex,
       "hicomKntopPLtg": hicomKntopPLtg,
       "hicomKntopPLtu": hicomKntopPLtu,
       "hicomKntopPSlot": hicomKntopPSlot,
       "hicomKntopPSatznr": hicomKntopPSatznr,
       "hicomKntopPBKanalGrp": hicomKntopPBKanalGrp,
       "hicomKntopPNodeNo": hicomKntopPNodeNo,
       "hicomKntopBunr": hicomKntopBunr,
       "hicomSQL": hicomSQL,
       "hicomSQLsessionIdGenerator": hicomSQLsessionIdGenerator,
       "hicomSQLsessionTable": hicomSQLsessionTable,
       "hicomSQLsessionEntry": hicomSQLsessionEntry,
       "hicomSQLsessionId": hicomSQLsessionId,
       "hicomSQLsessionState": hicomSQLsessionState,
       "hicomSQLsessionStatement": hicomSQLsessionStatement,
       "hicomSQLsessionWhereClause": hicomSQLsessionWhereClause,
       "hicomSQLsessionTimeout": hicomSQLsessionTimeout,
       "hicomSQLsessionResultSize": hicomSQLsessionResultSize,
       "hicomSQLsessionResultNoLines": hicomSQLsessionResultNoLines,
       "hicomSQLresultTable": hicomSQLresultTable,
       "hicomSQLresultEntry": hicomSQLresultEntry,
       "hicomSQLresultId": hicomSQLresultId,
       "hicomSQLresultBlockNo": hicomSQLresultBlockNo,
       "hicomSQLresultData": hicomSQLresultData,
       "hicomSQLinfo": hicomSQLinfo,
       "hicomSQLSubagentLastMsgNo": hicomSQLSubagentLastMsgNo,
       "hicomSQLSubagentLastMsgText": hicomSQLSubagentLastMsgText,
       "hicomDiscov": hicomDiscov,
       "hicomDiscovTable": hicomDiscovTable,
       "hicomDiscovEntry": hicomDiscovEntry,
       "hicomDiscovPabxId": hicomDiscovPabxId,
       "hicomDiscovPabxMnemonic": hicomDiscovPabxMnemonic,
       "hicomDiscovStatus": hicomDiscovStatus,
       "hicomDiscovMode": hicomDiscovMode,
       "hicomDiscovTimDat": hicomDiscovTimDat,
       "hicomDiscovErrTimDat": hicomDiscovErrTimDat,
       "hicomDiscInfo": hicomDiscInfo,
       "hicomDiscSubagentLastMsgNo": hicomDiscSubagentLastMsgNo,
       "hicomDiscSubagentLastMsgText": hicomDiscSubagentLastMsgText,
       "hicomMibConformance": hicomMibConformance,
       "hicomMibGroups": hicomMibGroups,
       "hicomCntrlTree": hicomCntrlTree,
       "hicomControlGroup": hicomControlGroup,
       "hicomSysTree": hicomSysTree,
       "hicomSystemGroup": hicomSystemGroup,
       "hicomAlarmTree": hicomAlarmTree,
       "hicomAlarmsGroup": hicomAlarmsGroup,
       "hicomAlMirrorUploadGroup": hicomAlMirrorUploadGroup,
       "hicomErrorTree": hicomErrorTree,
       "hicomErrorGroup": hicomErrorGroup,
       "hicomAlConfTree": hicomAlConfTree,
       "hicomAlConfigGroup": hicomAlConfigGroup,
       "hicomErrAlConfInfoGroup": hicomErrAlConfInfoGroup,
       "hicomAlConfDiscoveryGroup": hicomAlConfDiscoveryGroup,
       "hicomSoftTree": hicomSoftTree,
       "hicomSoftGroup": hicomSoftGroup,
       "hicomSoftInfoGroup": hicomSoftInfoGroup,
       "hicomSoftDiscoveryGroup": hicomSoftDiscoveryGroup,
       "hicomHardTree": hicomHardTree,
       "hicomCabinetsGroup": hicomCabinetsGroup,
       "hicomPeriperalsGroup": hicomPeriperalsGroup,
       "hicomBoardsGroup": hicomBoardsGroup,
       "hicomHWInfoGroup": hicomHWInfoGroup,
       "hicomHWDiscoveryGroup": hicomHWDiscoveryGroup,
       "hicomTopoTree": hicomTopoTree,
       "hicomTrunkGrpGroup": hicomTrunkGrpGroup,
       "hicomTrunkGroup": hicomTrunkGroup,
       "hicomTopoInfoGroup": hicomTopoInfoGroup,
       "hicomTopoDiscoveryGroup": hicomTopoDiscoveryGroup,
       "hicomKntopGroup": hicomKntopGroup,
       "hicomSQLtree": hicomSQLtree,
       "hicomSQLsessionGroup": hicomSQLsessionGroup,
       "hicomSQLresultGroup": hicomSQLresultGroup,
       "hicomSQLinfoGroup": hicomSQLinfoGroup,
       "hicomDiscovTree": hicomDiscovTree,
       "hicomDiscovGroup": hicomDiscovGroup,
       "hicomDiscInfoGroup": hicomDiscInfoGroup,
       "hicomTrapGroup": hicomTrapGroup,
       "hicomTrapVariables": hicomTrapVariables,
       "hicomSystemTrapVariables": hicomSystemTrapVariables,
       "hicomAlarmTrapVariables": hicomAlarmTrapVariables,
       "hicomAlTrpSysPabxId": hicomAlTrpSysPabxId,
       "hicomAlTrpSysMnemonic": hicomAlTrpSysMnemonic,
       "hicomErrorTrapVariables": hicomErrorTrapVariables,
       "hicomErrTrpPabxId": hicomErrTrpPabxId,
       "hicomErrTrpMnemonic": hicomErrTrpMnemonic,
       "hicomSWTrapVariables": hicomSWTrapVariables,
       "hicomSWTrpPabxId": hicomSWTrpPabxId,
       "hicomSWTrpPabxMnemonic": hicomSWTrpPabxMnemonic,
       "hicomAlConfTrapVariables": hicomAlConfTrapVariables,
       "hicomHWTrapVariables": hicomHWTrapVariables,
       "hicomHWTrpPabxId": hicomHWTrpPabxId,
       "hicomHWTrpPabxMnemonic": hicomHWTrpPabxMnemonic,
       "hicomTopoTrapVariables": hicomTopoTrapVariables,
       "hicomTopoTrpPabxId": hicomTopoTrpPabxId,
       "hicomTopoTrpPabxMnemonic": hicomTopoTrpPabxMnemonic,
       "hicomSQLTrapVariables": hicomSQLTrapVariables,
       "hicomDiscTrapVariables": hicomDiscTrapVariables,
       "hicomEDTrpPabxId": hicomEDTrpPabxId,
       "hicomEDTrpPabxMnemonic": hicomEDTrpPabxMnemonic,
       "hicomTraps": hicomTraps,
       "hicomSystemTraps": hicomSystemTraps,
       "internalMessageSystemSubagent": internalMessageSystemSubagent,
       "internalWarningSystemSubagent": internalWarningSystemSubagent,
       "internalErrorSystemSubagent": internalErrorSystemSubagent,
       "addHicom": addHicom,
       "deleteHicom": deleteHicom,
       "changeConfig": changeConfig,
       "hicomAlarmTraps": hicomAlarmTraps,
       "internalMessageAlarmSubagent": internalMessageAlarmSubagent,
       "internalWarningAlarmSubagent": internalWarningAlarmSubagent,
       "internalErrorAlarmSubagent": internalErrorAlarmSubagent,
       "hicomAlResetInitFailed": hicomAlResetInitFailed,
       "hicomAlUploadMirrorFailed": hicomAlUploadMirrorFailed,
       "hicomAlarmOnMajor": hicomAlarmOnMajor,
       "hicomAlarmOffMajor": hicomAlarmOffMajor,
       "hicomAlarmOnMinor": hicomAlarmOnMinor,
       "hicomAlarmOffMinor": hicomAlarmOffMinor,
       "hicomAlarmOnDevice": hicomAlarmOnDevice,
       "hicomAlarmOffDevice": hicomAlarmOffDevice,
       "hicomErrorTraps": hicomErrorTraps,
       "internalMessageErrAlConfSubagent": internalMessageErrAlConfSubagent,
       "internalWarningErrAlConfSubagent": internalWarningErrAlConfSubagent,
       "internalErrorErrAlConfSubagent": internalErrorErrAlConfSubagent,
       "hicomAlConfDiscovSucc": hicomAlConfDiscovSucc,
       "hicomAlConfDiscovErr": hicomAlConfDiscovErr,
       "hicomAlConfDiscovBusy": hicomAlConfDiscovBusy,
       "hicomErrorMsg": hicomErrorMsg,
       "hicomAlConfTraps": hicomAlConfTraps,
       "hicomSWTraps": hicomSWTraps,
       "internalMessageSWSubagent": internalMessageSWSubagent,
       "internalWarningSWSubagent": internalWarningSWSubagent,
       "internalErrorSWSubagent": internalErrorSWSubagent,
       "hicomSoftDiscovSucc": hicomSoftDiscovSucc,
       "hicomSoftDiscovErr": hicomSoftDiscovErr,
       "hicomSoftDiscovBusy": hicomSoftDiscovBusy,
       "hicomHWTraps": hicomHWTraps,
       "internalMessageHWSubagent": internalMessageHWSubagent,
       "internalWarningHWSubagent": internalWarningHWSubagent,
       "internalErrorHWSubagent": internalErrorHWSubagent,
       "hicomHWDiscovSucc": hicomHWDiscovSucc,
       "hicomHWDiscovErr": hicomHWDiscovErr,
       "hicomHWDiscovBusy": hicomHWDiscovBusy,
       "hicomTopoTraps": hicomTopoTraps,
       "internalMessageTopoSubagent": internalMessageTopoSubagent,
       "internalWarningTopoSubagent": internalWarningTopoSubagent,
       "internalErrorTopoSubagent": internalErrorTopoSubagent,
       "hicomTopoDiscovSucc": hicomTopoDiscovSucc,
       "hicomTopoDiscovErr": hicomTopoDiscovErr,
       "hicomTopoDiscovBusy": hicomTopoDiscovBusy,
       "hicomSQLTraps": hicomSQLTraps,
       "internalMessageSQLSubagent": internalMessageSQLSubagent,
       "internalWarningSQLSubagent": internalWarningSQLSubagent,
       "internalErrorSQLSubagent": internalErrorSQLSubagent,
       "hicomSQLsessionFinished": hicomSQLsessionFinished,
       "hicomDiscTraps": hicomDiscTraps,
       "internalMessageDiscSubagent": internalMessageDiscSubagent,
       "internalWarningDiscSubagent": internalWarningDiscSubagent,
       "internalErrorDiscSubagent": internalErrorDiscSubagent,
       "hicomErrDeleteSucc": hicomErrDeleteSucc,
       "hicomErrDeleteErr": hicomErrDeleteErr,
       "hicomErrDeleteBusy": hicomErrDeleteBusy}
)
