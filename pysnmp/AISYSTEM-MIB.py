# SNMP MIB module (AISYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:09 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 8)
)
aiSystem.setRevisions(
        ("2001-08-15 10:00",
         "2001-06-28 15:00",
         "2001-05-22 20:00",
         "1999-10-25 00:00",
         "1998-10-30 00:00")
)


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



class AIIHwIntType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("analogIn", 21),
          ("discreteIn", 4),
          ("discreteOut", 5),
          ("ethernetPort10", 6),
          ("ethernetPort10-100", 8),
          ("ethernetPort100", 7),
          ("ethernetPort1000", 18),
          ("fan", 17),
          ("fiber1310", 20),
          ("fiber850", 19),
          ("hubbedEthernetPort10", 9),
          ("hubbedEthernetPort10-100", 11),
          ("hubbedEthernetPort100", 10),
          ("hubbedFiber1310", 13),
          ("hubbedFiber1550", 14),
          ("luxChannel10G", 27),
          ("modem56K", 12),
          ("noHwIfType", 0),
          ("power", 16),
          ("serialAsync", 3),
          ("serialAsyncnoDSR", 30),
          ("serialSync", 2),
          ("serialSyncAsync", 1),
          ("serialSyncAsyncnoDSR", 29),
          ("switchedEthernetPort10", 22),
          ("switchedEthernetPort10-100", 24),
          ("switchedEthernetPort100", 23),
          ("switchedEthernetPort1000", 28),
          ("switchedFiber1310", 25),
          ("switchedFiber1550", 26),
          ("temperatureProbe", 15))
    )



class AIIConnType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("aui", 7),
          ("coax", 6),
          ("copperGBIC", 11),
          ("db25", 3),
          ("db9", 2),
          ("gbic", 12),
          ("noConnType", 0),
          ("propConnType", 1),
          ("rj11", 4),
          ("rj45", 5),
          ("sc", 8),
          ("scsi2", 10),
          ("sfp", 13),
          ("vhdci", 9))
    )



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSystemSendsStatusTraps_Type = TruthValue
_AiSystemSendsStatusTraps_Object = MibScalar
aiSystemSendsStatusTraps = _AiSystemSendsStatusTraps_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 1),
    _AiSystemSendsStatusTraps_Type()
)
aiSystemSendsStatusTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSystemSendsStatusTraps.setStatus("current")


class _AiSystemLastTrapSequenceNum_Type(Integer32):
    """Custom type aiSystemLastTrapSequenceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiSystemLastTrapSequenceNum_Type.__name__ = "Integer32"
_AiSystemLastTrapSequenceNum_Object = MibScalar
aiSystemLastTrapSequenceNum = _AiSystemLastTrapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 2),
    _AiSystemLastTrapSequenceNum_Type()
)
aiSystemLastTrapSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSystemLastTrapSequenceNum.setStatus("current")
_AiSystemLastTrapMsg_Type = DisplayString
_AiSystemLastTrapMsg_Object = MibScalar
aiSystemLastTrapMsg = _AiSystemLastTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 3),
    _AiSystemLastTrapMsg_Type()
)
aiSystemLastTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSystemLastTrapMsg.setStatus("current")
_AiSystemDisc_ObjectIdentity = ObjectIdentity
aiSystemDisc = _AiSystemDisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 8, 4)
)


class _AiSystemDiscVersion_Type(Integer32):
    """Custom type aiSystemDiscVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AiSystemDiscVersion_Type.__name__ = "Integer32"
_AiSystemDiscVersion_Object = MibScalar
aiSystemDiscVersion = _AiSystemDiscVersion_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 1),
    _AiSystemDiscVersion_Type()
)
aiSystemDiscVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSystemDiscVersion.setStatus("current")
_AiSystemDiscLastChanged_Type = DateAndTime
_AiSystemDiscLastChanged_Object = MibScalar
aiSystemDiscLastChanged = _AiSystemDiscLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 2),
    _AiSystemDiscLastChanged_Type()
)
aiSystemDiscLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSystemDiscLastChanged.setStatus("current")
_AiSysDiscModuleTable_Object = MibTable
aiSysDiscModuleTable = _AiSysDiscModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 3)
)
if mibBuilder.loadTexts:
    aiSysDiscModuleTable.setStatus("current")
_AiSysModuleTableEntry_Object = MibTableRow
aiSysModuleTableEntry = _AiSysModuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 3, 1)
)
aiSysModuleTableEntry.setIndexNames(
    (1, "AISYSTEM-MIB", "aiSysMTIndex"),
)
if mibBuilder.loadTexts:
    aiSysModuleTableEntry.setStatus("current")
_AiSysMTIndex_Type = ObjectIdentifier
_AiSysMTIndex_Object = MibTableColumn
aiSysMTIndex = _AiSysMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 3, 1, 1),
    _AiSysMTIndex_Type()
)
aiSysMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysMTIndex.setStatus("current")
_AiSysMTProductName_Type = DisplayString
_AiSysMTProductName_Object = MibTableColumn
aiSysMTProductName = _AiSysMTProductName_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 3, 1, 2),
    _AiSysMTProductName_Type()
)
aiSysMTProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysMTProductName.setStatus("current")
_AiSysMTSerialNumber_Type = DisplayString
_AiSysMTSerialNumber_Object = MibTableColumn
aiSysMTSerialNumber = _AiSysMTSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 3, 1, 3),
    _AiSysMTSerialNumber_Type()
)
aiSysMTSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysMTSerialNumber.setStatus("current")
_AiSysMTManufDate_Type = DisplayString
_AiSysMTManufDate_Object = MibTableColumn
aiSysMTManufDate = _AiSysMTManufDate_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 3, 1, 4),
    _AiSysMTManufDate_Type()
)
aiSysMTManufDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysMTManufDate.setStatus("current")
_AiSysDiscStatumTable_Object = MibTable
aiSysDiscStatumTable = _AiSysDiscStatumTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 4)
)
if mibBuilder.loadTexts:
    aiSysDiscStatumTable.setStatus("current")
_AiSysStatumTableEntry_Object = MibTableRow
aiSysStatumTableEntry = _AiSysStatumTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 4, 1)
)
aiSysStatumTableEntry.setIndexNames(
    (1, "AISYSTEM-MIB", "aiSysSTIndex"),
)
if mibBuilder.loadTexts:
    aiSysStatumTableEntry.setStatus("current")
_AiSysSTIndex_Type = ObjectIdentifier
_AiSysSTIndex_Object = MibTableColumn
aiSysSTIndex = _AiSysSTIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 4, 1, 1),
    _AiSysSTIndex_Type()
)
aiSysSTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysSTIndex.setStatus("current")
_AiSysSTLabel_Type = DisplayString
_AiSysSTLabel_Object = MibTableColumn
aiSysSTLabel = _AiSysSTLabel_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 4, 1, 2),
    _AiSysSTLabel_Type()
)
aiSysSTLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysSTLabel.setStatus("current")
_AiSysSTFaceplateModule_Type = ObjectIdentifier
_AiSysSTFaceplateModule_Object = MibTableColumn
aiSysSTFaceplateModule = _AiSysSTFaceplateModule_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 4, 1, 3),
    _AiSysSTFaceplateModule_Type()
)
aiSysSTFaceplateModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysSTFaceplateModule.setStatus("current")


class _AiSysSTFaceplateOpening_Type(Integer32):
    """Custom type aiSysSTFaceplateOpening based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AiSysSTFaceplateOpening_Type.__name__ = "Integer32"
_AiSysSTFaceplateOpening_Object = MibTableColumn
aiSysSTFaceplateOpening = _AiSysSTFaceplateOpening_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 4, 1, 4),
    _AiSysSTFaceplateOpening_Type()
)
aiSysSTFaceplateOpening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysSTFaceplateOpening.setStatus("current")


class _AiSysSTOpeningIndex_Type(Integer32):
    """Custom type aiSysSTOpeningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AiSysSTOpeningIndex_Type.__name__ = "Integer32"
_AiSysSTOpeningIndex_Object = MibTableColumn
aiSysSTOpeningIndex = _AiSysSTOpeningIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 4, 1, 5),
    _AiSysSTOpeningIndex_Type()
)
aiSysSTOpeningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysSTOpeningIndex.setStatus("current")
_AiSysSTHwIntType_Type = AIIHwIntType
_AiSysSTHwIntType_Object = MibTableColumn
aiSysSTHwIntType = _AiSysSTHwIntType_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 4, 1, 6),
    _AiSysSTHwIntType_Type()
)
aiSysSTHwIntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysSTHwIntType.setStatus("current")
_AiSysSTConnType_Type = AIIConnType
_AiSysSTConnType_Object = MibTableColumn
aiSysSTConnType = _AiSysSTConnType_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 4, 1, 7),
    _AiSysSTConnType_Type()
)
aiSysSTConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysSTConnType.setStatus("current")


class _AiSysSTMonTabIndex_Type(Integer32):
    """Custom type aiSysSTMonTabIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AiSysSTMonTabIndex_Type.__name__ = "Integer32"
_AiSysSTMonTabIndex_Object = MibTableColumn
aiSysSTMonTabIndex = _AiSysSTMonTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 4, 4, 1, 8),
    _AiSysSTMonTabIndex_Type()
)
aiSysSTMonTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSysSTMonTabIndex.setStatus("current")
_AiSystemManagerTable_Object = MibTable
aiSystemManagerTable = _AiSystemManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 5)
)
if mibBuilder.loadTexts:
    aiSystemManagerTable.setStatus("current")
_AiSystemManagerTableEntry_Object = MibTableRow
aiSystemManagerTableEntry = _AiSystemManagerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 5, 1)
)
aiSystemManagerTableEntry.setIndexNames(
    (0, "AISYSTEM-MIB", "aisysManagerIndex"),
)
if mibBuilder.loadTexts:
    aiSystemManagerTableEntry.setStatus("current")
_AisysManagerIndex_Type = PositiveInteger
_AisysManagerIndex_Object = MibTableColumn
aisysManagerIndex = _AisysManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 5, 1, 1),
    _AisysManagerIndex_Type()
)
aisysManagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aisysManagerIndex.setStatus("current")
_AisysManagerAddress_Type = IpAddress
_AisysManagerAddress_Object = MibTableColumn
aisysManagerAddress = _AisysManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 5, 1, 2),
    _AisysManagerAddress_Type()
)
aisysManagerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aisysManagerAddress.setStatus("current")


class _AiSystemCmdReboot_Type(Integer32):
    """Custom type aiSystemCmdReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 2),
          ("up", 1))
    )


_AiSystemCmdReboot_Type.__name__ = "Integer32"
_AiSystemCmdReboot_Object = MibScalar
aiSystemCmdReboot = _AiSystemCmdReboot_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 6),
    _AiSystemCmdReboot_Type()
)
aiSystemCmdReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSystemCmdReboot.setStatus("current")


class _AiSystemStatusLastConfig_Type(OctetString):
    """Custom type aiSystemStatusLastConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AiSystemStatusLastConfig_Type.__name__ = "OctetString"
_AiSystemStatusLastConfig_Object = MibScalar
aiSystemStatusLastConfig = _AiSystemStatusLastConfig_Object(
    (1, 3, 6, 1, 4, 1, 539, 8, 7),
    _AiSystemStatusLastConfig_Type()
)
aiSystemStatusLastConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSystemStatusLastConfig.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISYSTEM-MIB",
    **{"PositiveInteger": PositiveInteger,
       "AIIHwIntType": AIIHwIntType,
       "AIIConnType": AIIConnType,
       "aii": aii,
       "aiSystem": aiSystem,
       "aiSystemSendsStatusTraps": aiSystemSendsStatusTraps,
       "aiSystemLastTrapSequenceNum": aiSystemLastTrapSequenceNum,
       "aiSystemLastTrapMsg": aiSystemLastTrapMsg,
       "aiSystemDisc": aiSystemDisc,
       "aiSystemDiscVersion": aiSystemDiscVersion,
       "aiSystemDiscLastChanged": aiSystemDiscLastChanged,
       "aiSysDiscModuleTable": aiSysDiscModuleTable,
       "aiSysModuleTableEntry": aiSysModuleTableEntry,
       "aiSysMTIndex": aiSysMTIndex,
       "aiSysMTProductName": aiSysMTProductName,
       "aiSysMTSerialNumber": aiSysMTSerialNumber,
       "aiSysMTManufDate": aiSysMTManufDate,
       "aiSysDiscStatumTable": aiSysDiscStatumTable,
       "aiSysStatumTableEntry": aiSysStatumTableEntry,
       "aiSysSTIndex": aiSysSTIndex,
       "aiSysSTLabel": aiSysSTLabel,
       "aiSysSTFaceplateModule": aiSysSTFaceplateModule,
       "aiSysSTFaceplateOpening": aiSysSTFaceplateOpening,
       "aiSysSTOpeningIndex": aiSysSTOpeningIndex,
       "aiSysSTHwIntType": aiSysSTHwIntType,
       "aiSysSTConnType": aiSysSTConnType,
       "aiSysSTMonTabIndex": aiSysSTMonTabIndex,
       "aiSystemManagerTable": aiSystemManagerTable,
       "aiSystemManagerTableEntry": aiSystemManagerTableEntry,
       "aisysManagerIndex": aisysManagerIndex,
       "aisysManagerAddress": aisysManagerAddress,
       "aiSystemCmdReboot": aiSystemCmdReboot,
       "aiSystemStatusLastConfig": aiSystemStatusLastConfig}
)
