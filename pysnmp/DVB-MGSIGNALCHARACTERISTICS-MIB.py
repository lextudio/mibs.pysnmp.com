# SNMP MIB module (DVB-MGSIGNALCHARACTERISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DVB-MGSIGNALCHARACTERISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:53 2024
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

(DeliverySystemType,
 FloatingPoint,
 InputNumber,
 Modulation,
 PIDPlusOne,
 RateStatus,
 ServiceId) = mibBuilder.importSymbols(
    "DVB-MGTR101290-MIB",
    "DeliverySystemType",
    "FloatingPoint",
    "InputNumber",
    "Modulation",
    "PIDPlusOne",
    "RateStatus",
    "ServiceId")

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

mgSignalCharacteristics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CASystemID(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )



class EncryptionState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 2),
          ("unencrypted", 1),
          ("unknown", 3))
    )



class GuardInterval(Integer32, TextualConvention):
    status = "current"
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
        *(("guard1over16", 2),
          ("guard1over32", 1),
          ("guard1over4", 4),
          ("guard1over8", 3))
    )



class InnerCodeRate(Integer32, TextualConvention):
    status = "current"
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
        *(("rate1over2", 2),
          ("rate2over3", 3),
          ("rate3over4", 4),
          ("rate5over6", 5),
          ("rate7over8", 6),
          ("rateNone", 1))
    )



class NetworkID(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )



class PID(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )



class ReadableString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TerrestrialTransmissionMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("carriers2k", 1),
          ("carriers8k", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Dvb_ObjectIdentity = ObjectIdentity
dvb = _Dvb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696)
)
_Mg_ObjectIdentity = ObjectIdentity
mg = _Mg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3)
)
_MgSignalCharacteristicsObjects_ObjectIdentity = ObjectIdentity
mgSignalCharacteristicsObjects = _MgSignalCharacteristicsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1)
)
_MgTSStructure_ObjectIdentity = ObjectIdentity
mgTSStructure = _MgTSStructure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1)
)
_MgTSStructureTrap_ObjectIdentity = ObjectIdentity
mgTSStructureTrap = _MgTSStructureTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1)
)
_StructureTrapPrefix_ObjectIdentity = ObjectIdentity
structureTrapPrefix = _StructureTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1, 0)
)
_StructureTrapControlTable_Object = MibTable
structureTrapControlTable = _StructureTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    structureTrapControlTable.setStatus("current")
_StructureTrapControlEntry_Object = MibTableRow
structureTrapControlEntry = _StructureTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1, 1, 1)
)
structureTrapControlEntry.setIndexNames(
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "structureTrapControlInputNumber"),
)
if mibBuilder.loadTexts:
    structureTrapControlEntry.setStatus("current")
_StructureTrapControlInputNumber_Type = InputNumber
_StructureTrapControlInputNumber_Object = MibTableColumn
structureTrapControlInputNumber = _StructureTrapControlInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1, 1, 1, 1),
    _StructureTrapControlInputNumber_Type()
)
structureTrapControlInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    structureTrapControlInputNumber.setStatus("current")
_StructureTrapControlOID_Type = ObjectIdentifier
_StructureTrapControlOID_Object = MibTableColumn
structureTrapControlOID = _StructureTrapControlOID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1, 1, 1, 2),
    _StructureTrapControlOID_Type()
)
structureTrapControlOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    structureTrapControlOID.setStatus("current")
_StructureTrapControlChangeTime_Type = DateAndTime
_StructureTrapControlChangeTime_Object = MibTableColumn
structureTrapControlChangeTime = _StructureTrapControlChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1, 1, 1, 3),
    _StructureTrapControlChangeTime_Type()
)
structureTrapControlChangeTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    structureTrapControlChangeTime.setStatus("current")
_StructureTrapControlRateStatus_Type = RateStatus
_StructureTrapControlRateStatus_Object = MibTableColumn
structureTrapControlRateStatus = _StructureTrapControlRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1, 1, 1, 4),
    _StructureTrapControlRateStatus_Type()
)
structureTrapControlRateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    structureTrapControlRateStatus.setStatus("current")


class _StructureTrapControlPeriod_Type(Unsigned32):
    """Custom type structureTrapControlPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_StructureTrapControlPeriod_Type.__name__ = "Unsigned32"
_StructureTrapControlPeriod_Object = MibTableColumn
structureTrapControlPeriod = _StructureTrapControlPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1, 1, 1, 5),
    _StructureTrapControlPeriod_Type()
)
structureTrapControlPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    structureTrapControlPeriod.setStatus("current")
if mibBuilder.loadTexts:
    structureTrapControlPeriod.setUnits("millisecond")
_StructureTrapInput_Type = InputNumber
_StructureTrapInput_Object = MibScalar
structureTrapInput = _StructureTrapInput_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1, 2),
    _StructureTrapInput_Type()
)
structureTrapInput.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    structureTrapInput.setStatus("current")
_MgTSTable_Object = MibTable
mgTSTable = _MgTSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mgTSTable.setStatus("current")
_MgTSEntry_Object = MibTableRow
mgTSEntry = _MgTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 2, 1)
)
mgTSEntry.setIndexNames(
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgTSInputNumber"),
)
if mibBuilder.loadTexts:
    mgTSEntry.setStatus("current")
_MgTSInputNumber_Type = InputNumber
_MgTSInputNumber_Object = MibTableColumn
mgTSInputNumber = _MgTSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 2, 1, 1),
    _MgTSInputNumber_Type()
)
mgTSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgTSInputNumber.setStatus("current")


class _MgTSId_Type(Integer32):
    """Custom type mgTSId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MgTSId_Type.__name__ = "Integer32"
_MgTSId_Object = MibTableColumn
mgTSId = _MgTSId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 2, 1, 2),
    _MgTSId_Type()
)
mgTSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgTSId.setStatus("current")
_MgTSOriginalNetworkID_Type = NetworkID
_MgTSOriginalNetworkID_Object = MibTableColumn
mgTSOriginalNetworkID = _MgTSOriginalNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 2, 1, 3),
    _MgTSOriginalNetworkID_Type()
)
mgTSOriginalNetworkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgTSOriginalNetworkID.setStatus("current")
_MgTSNetworkID_Type = NetworkID
_MgTSNetworkID_Object = MibTableColumn
mgTSNetworkID = _MgTSNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 2, 1, 4),
    _MgTSNetworkID_Type()
)
mgTSNetworkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgTSNetworkID.setStatus("current")
_MgTSNetworkName_Type = ReadableString
_MgTSNetworkName_Object = MibTableColumn
mgTSNetworkName = _MgTSNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 2, 1, 5),
    _MgTSNetworkName_Type()
)
mgTSNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgTSNetworkName.setStatus("current")
_MgServiceTable_Object = MibTable
mgServiceTable = _MgServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mgServiceTable.setStatus("current")
_MgServiceEntry_Object = MibTableRow
mgServiceEntry = _MgServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3, 1)
)
mgServiceEntry.setIndexNames(
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServiceNumber"),
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServiceInputNumber"),
)
if mibBuilder.loadTexts:
    mgServiceEntry.setStatus("current")
_MgServiceInputNumber_Type = InputNumber
_MgServiceInputNumber_Object = MibTableColumn
mgServiceInputNumber = _MgServiceInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3, 1, 1),
    _MgServiceInputNumber_Type()
)
mgServiceInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgServiceInputNumber.setStatus("current")
_MgServiceNumber_Type = ServiceId
_MgServiceNumber_Object = MibTableColumn
mgServiceNumber = _MgServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3, 1, 2),
    _MgServiceNumber_Type()
)
mgServiceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgServiceNumber.setStatus("current")


class _MgServiceType_Type(Integer32):
    """Custom type mgServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_MgServiceType_Type.__name__ = "Integer32"
_MgServiceType_Object = MibTableColumn
mgServiceType = _MgServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3, 1, 3),
    _MgServiceType_Type()
)
mgServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServiceType.setStatus("current")
_MgServiceName_Type = ReadableString
_MgServiceName_Object = MibTableColumn
mgServiceName = _MgServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3, 1, 4),
    _MgServiceName_Type()
)
mgServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServiceName.setStatus("current")
_MgServiceProviderName_Type = ReadableString
_MgServiceProviderName_Object = MibTableColumn
mgServiceProviderName = _MgServiceProviderName_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3, 1, 5),
    _MgServiceProviderName_Type()
)
mgServiceProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServiceProviderName.setStatus("current")
_MgServicePMTPID_Type = PID
_MgServicePMTPID_Object = MibTableColumn
mgServicePMTPID = _MgServicePMTPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3, 1, 6),
    _MgServicePMTPID_Type()
)
mgServicePMTPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServicePMTPID.setStatus("current")
_MgServicePCRPID_Type = PID
_MgServicePCRPID_Object = MibTableColumn
mgServicePCRPID = _MgServicePCRPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3, 1, 7),
    _MgServicePCRPID_Type()
)
mgServicePCRPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServicePCRPID.setStatus("current")
_MgServiceCondAccess_Type = EncryptionState
_MgServiceCondAccess_Object = MibTableColumn
mgServiceCondAccess = _MgServiceCondAccess_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3, 1, 8),
    _MgServiceCondAccess_Type()
)
mgServiceCondAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServiceCondAccess.setStatus("current")
_MgServiceEITComponentDescriptor_Type = ReadableString
_MgServiceEITComponentDescriptor_Object = MibTableColumn
mgServiceEITComponentDescriptor = _MgServiceEITComponentDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 3, 1, 9),
    _MgServiceEITComponentDescriptor_Type()
)
mgServiceEITComponentDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServiceEITComponentDescriptor.setStatus("current")
_MgPIDTable_Object = MibTable
mgPIDTable = _MgPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mgPIDTable.setStatus("current")
_MgPIDEntry_Object = MibTableRow
mgPIDEntry = _MgPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 4, 1)
)
mgPIDEntry.setIndexNames(
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgPIDServiceNumber"),
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgPIDNumber"),
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgPIDInputNumber"),
)
if mibBuilder.loadTexts:
    mgPIDEntry.setStatus("current")
_MgPIDInputNumber_Type = InputNumber
_MgPIDInputNumber_Object = MibTableColumn
mgPIDInputNumber = _MgPIDInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 4, 1, 1),
    _MgPIDInputNumber_Type()
)
mgPIDInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgPIDInputNumber.setStatus("current")
_MgPIDServiceNumber_Type = ServiceId
_MgPIDServiceNumber_Object = MibTableColumn
mgPIDServiceNumber = _MgPIDServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 4, 1, 2),
    _MgPIDServiceNumber_Type()
)
mgPIDServiceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgPIDServiceNumber.setStatus("current")
_MgPIDNumber_Type = PIDPlusOne
_MgPIDNumber_Object = MibTableColumn
mgPIDNumber = _MgPIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 4, 1, 3),
    _MgPIDNumber_Type()
)
mgPIDNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgPIDNumber.setStatus("current")


class _MgPIDType_Type(Integer32):
    """Custom type mgPIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MgPIDType_Type.__name__ = "Integer32"
_MgPIDType_Object = MibTableColumn
mgPIDType = _MgPIDType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 4, 1, 4),
    _MgPIDType_Type()
)
mgPIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgPIDType.setStatus("current")
_MgPIDCondAccess_Type = EncryptionState
_MgPIDCondAccess_Object = MibTableColumn
mgPIDCondAccess = _MgPIDCondAccess_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 4, 1, 5),
    _MgPIDCondAccess_Type()
)
mgPIDCondAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgPIDCondAccess.setStatus("current")
_MgEMMTable_Object = MibTable
mgEMMTable = _MgEMMTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mgEMMTable.setStatus("current")
_MgEMMEntry_Object = MibTableRow
mgEMMEntry = _MgEMMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 5, 1)
)
mgEMMEntry.setIndexNames(
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgEMMInputNumber"),
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgEMMCaPID"),
)
if mibBuilder.loadTexts:
    mgEMMEntry.setStatus("current")
_MgEMMInputNumber_Type = InputNumber
_MgEMMInputNumber_Object = MibTableColumn
mgEMMInputNumber = _MgEMMInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 5, 1, 1),
    _MgEMMInputNumber_Type()
)
mgEMMInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgEMMInputNumber.setStatus("current")
_MgEMMCaPID_Type = PIDPlusOne
_MgEMMCaPID_Object = MibTableColumn
mgEMMCaPID = _MgEMMCaPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 5, 1, 2),
    _MgEMMCaPID_Type()
)
mgEMMCaPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgEMMCaPID.setStatus("current")
_MgEMMCASystemID_Type = CASystemID
_MgEMMCASystemID_Object = MibTableColumn
mgEMMCASystemID = _MgEMMCASystemID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 5, 1, 3),
    _MgEMMCASystemID_Type()
)
mgEMMCASystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgEMMCASystemID.setStatus("current")
_MgServiceECMTable_Object = MibTable
mgServiceECMTable = _MgServiceECMTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mgServiceECMTable.setStatus("current")
_MgServiceECMEntry_Object = MibTableRow
mgServiceECMEntry = _MgServiceECMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 6, 1)
)
mgServiceECMEntry.setIndexNames(
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServiceECMInputNumber"),
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServiceECMServiceNumber"),
)
if mibBuilder.loadTexts:
    mgServiceECMEntry.setStatus("current")
_MgServiceECMInputNumber_Type = InputNumber
_MgServiceECMInputNumber_Object = MibTableColumn
mgServiceECMInputNumber = _MgServiceECMInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 6, 1, 1),
    _MgServiceECMInputNumber_Type()
)
mgServiceECMInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgServiceECMInputNumber.setStatus("current")
_MgServiceECMServiceNumber_Type = ServiceId
_MgServiceECMServiceNumber_Object = MibTableColumn
mgServiceECMServiceNumber = _MgServiceECMServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 6, 1, 2),
    _MgServiceECMServiceNumber_Type()
)
mgServiceECMServiceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgServiceECMServiceNumber.setStatus("current")
_MgServiceECMCaPID_Type = PIDPlusOne
_MgServiceECMCaPID_Object = MibTableColumn
mgServiceECMCaPID = _MgServiceECMCaPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 6, 1, 3),
    _MgServiceECMCaPID_Type()
)
mgServiceECMCaPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgServiceECMCaPID.setStatus("current")
_MgServiceECMCASystemID_Type = CASystemID
_MgServiceECMCASystemID_Object = MibTableColumn
mgServiceECMCASystemID = _MgServiceECMCASystemID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 6, 1, 4),
    _MgServiceECMCASystemID_Type()
)
mgServiceECMCASystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServiceECMCASystemID.setStatus("current")
_MgPIDECMTable_Object = MibTable
mgPIDECMTable = _MgPIDECMTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mgPIDECMTable.setStatus("current")
_MgPIDECMEntry_Object = MibTableRow
mgPIDECMEntry = _MgPIDECMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 7, 1)
)
mgPIDECMEntry.setIndexNames(
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgPIDECMInputNumber"),
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgPIDECMServiceNumber"),
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgPIDECMPID"),
)
if mibBuilder.loadTexts:
    mgPIDECMEntry.setStatus("current")
_MgPIDECMInputNumber_Type = InputNumber
_MgPIDECMInputNumber_Object = MibTableColumn
mgPIDECMInputNumber = _MgPIDECMInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 7, 1, 1),
    _MgPIDECMInputNumber_Type()
)
mgPIDECMInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgPIDECMInputNumber.setStatus("current")
_MgPIDECMServiceNumber_Type = ServiceId
_MgPIDECMServiceNumber_Object = MibTableColumn
mgPIDECMServiceNumber = _MgPIDECMServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 7, 1, 2),
    _MgPIDECMServiceNumber_Type()
)
mgPIDECMServiceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgPIDECMServiceNumber.setStatus("current")
_MgPIDECMPID_Type = PIDPlusOne
_MgPIDECMPID_Object = MibTableColumn
mgPIDECMPID = _MgPIDECMPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 7, 1, 3),
    _MgPIDECMPID_Type()
)
mgPIDECMPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgPIDECMPID.setStatus("current")
_MgPIDECMCaPID_Type = PIDPlusOne
_MgPIDECMCaPID_Object = MibTableColumn
mgPIDECMCaPID = _MgPIDECMCaPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 7, 1, 4),
    _MgPIDECMCaPID_Type()
)
mgPIDECMCaPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgPIDECMCaPID.setStatus("current")
_MgPIDECMCASystemID_Type = CASystemID
_MgPIDECMCASystemID_Object = MibTableColumn
mgPIDECMCASystemID = _MgPIDECMCASystemID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 7, 1, 5),
    _MgPIDECMCASystemID_Type()
)
mgPIDECMCASystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgPIDECMCASystemID.setStatus("current")
_MgNITDeliverySystemTable_Object = MibTable
mgNITDeliverySystemTable = _MgNITDeliverySystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    mgNITDeliverySystemTable.setStatus("current")
_MgNITDeliverySystemEntry_Object = MibTableRow
mgNITDeliverySystemEntry = _MgNITDeliverySystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1)
)
mgNITDeliverySystemEntry.setIndexNames(
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSInputNumber"),
)
if mibBuilder.loadTexts:
    mgNITDeliverySystemEntry.setStatus("current")
_MgNITDSInputNumber_Type = InputNumber
_MgNITDSInputNumber_Object = MibTableColumn
mgNITDSInputNumber = _MgNITDSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 1),
    _MgNITDSInputNumber_Type()
)
mgNITDSInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgNITDSInputNumber.setStatus("current")
_MgNITDSSystemType_Type = DeliverySystemType
_MgNITDSSystemType_Object = MibTableColumn
mgNITDSSystemType = _MgNITDSSystemType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 2),
    _MgNITDSSystemType_Type()
)
mgNITDSSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSSystemType.setStatus("current")
_MgNITDSFrequency_Type = FloatingPoint
_MgNITDSFrequency_Object = MibTableColumn
mgNITDSFrequency = _MgNITDSFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 3),
    _MgNITDSFrequency_Type()
)
mgNITDSFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSFrequency.setStatus("current")
if mibBuilder.loadTexts:
    mgNITDSFrequency.setUnits("MHz")


class _MgNITDSFecOuter_Type(Integer32):
    """Custom type mgNITDSFecOuter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MgNITDSFecOuter_Type.__name__ = "Integer32"
_MgNITDSFecOuter_Object = MibTableColumn
mgNITDSFecOuter = _MgNITDSFecOuter_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 4),
    _MgNITDSFecOuter_Type()
)
mgNITDSFecOuter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSFecOuter.setStatus("current")


class _MgNITDSCableModulation_Type(Integer32):
    """Custom type mgNITDSCableModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MgNITDSCableModulation_Type.__name__ = "Integer32"
_MgNITDSCableModulation_Object = MibTableColumn
mgNITDSCableModulation = _MgNITDSCableModulation_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 5),
    _MgNITDSCableModulation_Type()
)
mgNITDSCableModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSCableModulation.setStatus("current")
_MgNITDSSymbolRate_Type = Unsigned32
_MgNITDSSymbolRate_Object = MibTableColumn
mgNITDSSymbolRate = _MgNITDSSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 6),
    _MgNITDSSymbolRate_Type()
)
mgNITDSSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    mgNITDSSymbolRate.setUnits("symbol/s")


class _MgNITDSFecInner_Type(Integer32):
    """Custom type mgNITDSFecInner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MgNITDSFecInner_Type.__name__ = "Integer32"
_MgNITDSFecInner_Object = MibTableColumn
mgNITDSFecInner = _MgNITDSFecInner_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 7),
    _MgNITDSFecInner_Type()
)
mgNITDSFecInner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSFecInner.setStatus("current")
_MgNITDSOrbitalPosition_Type = FloatingPoint
_MgNITDSOrbitalPosition_Object = MibTableColumn
mgNITDSOrbitalPosition = _MgNITDSOrbitalPosition_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 8),
    _MgNITDSOrbitalPosition_Type()
)
mgNITDSOrbitalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSOrbitalPosition.setStatus("current")
if mibBuilder.loadTexts:
    mgNITDSOrbitalPosition.setUnits("degree")


class _MgNITDSWestEastFlag_Type(Integer32):
    """Custom type mgNITDSWestEastFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("west", 0))
    )


_MgNITDSWestEastFlag_Type.__name__ = "Integer32"
_MgNITDSWestEastFlag_Object = MibTableColumn
mgNITDSWestEastFlag = _MgNITDSWestEastFlag_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 9),
    _MgNITDSWestEastFlag_Type()
)
mgNITDSWestEastFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSWestEastFlag.setStatus("current")


class _MgNITDSPolarization_Type(Integer32):
    """Custom type mgNITDSPolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MgNITDSPolarization_Type.__name__ = "Integer32"
_MgNITDSPolarization_Object = MibTableColumn
mgNITDSPolarization = _MgNITDSPolarization_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 10),
    _MgNITDSPolarization_Type()
)
mgNITDSPolarization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSPolarization.setStatus("current")


class _MgNITDSSatelliteModulation_Type(Integer32):
    """Custom type mgNITDSSatelliteModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MgNITDSSatelliteModulation_Type.__name__ = "Integer32"
_MgNITDSSatelliteModulation_Object = MibTableColumn
mgNITDSSatelliteModulation = _MgNITDSSatelliteModulation_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 11),
    _MgNITDSSatelliteModulation_Type()
)
mgNITDSSatelliteModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSSatelliteModulation.setStatus("current")


class _MgNITDSBandwidth_Type(Integer32):
    """Custom type mgNITDSBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgNITDSBandwidth_Type.__name__ = "Integer32"
_MgNITDSBandwidth_Object = MibTableColumn
mgNITDSBandwidth = _MgNITDSBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 12),
    _MgNITDSBandwidth_Type()
)
mgNITDSBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSBandwidth.setStatus("current")


class _MgNITDSConstellation_Type(Integer32):
    """Custom type mgNITDSConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MgNITDSConstellation_Type.__name__ = "Integer32"
_MgNITDSConstellation_Object = MibTableColumn
mgNITDSConstellation = _MgNITDSConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 13),
    _MgNITDSConstellation_Type()
)
mgNITDSConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSConstellation.setStatus("current")


class _MgNITDSHierarchyInformation_Type(Integer32):
    """Custom type mgNITDSHierarchyInformation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgNITDSHierarchyInformation_Type.__name__ = "Integer32"
_MgNITDSHierarchyInformation_Object = MibTableColumn
mgNITDSHierarchyInformation = _MgNITDSHierarchyInformation_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 14),
    _MgNITDSHierarchyInformation_Type()
)
mgNITDSHierarchyInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSHierarchyInformation.setStatus("current")


class _MgNITDSCodeRateHPStream_Type(Integer32):
    """Custom type mgNITDSCodeRateHPStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgNITDSCodeRateHPStream_Type.__name__ = "Integer32"
_MgNITDSCodeRateHPStream_Object = MibTableColumn
mgNITDSCodeRateHPStream = _MgNITDSCodeRateHPStream_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 15),
    _MgNITDSCodeRateHPStream_Type()
)
mgNITDSCodeRateHPStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSCodeRateHPStream.setStatus("current")


class _MgNITDSCodeRateLPStream_Type(Integer32):
    """Custom type mgNITDSCodeRateLPStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgNITDSCodeRateLPStream_Type.__name__ = "Integer32"
_MgNITDSCodeRateLPStream_Object = MibTableColumn
mgNITDSCodeRateLPStream = _MgNITDSCodeRateLPStream_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 16),
    _MgNITDSCodeRateLPStream_Type()
)
mgNITDSCodeRateLPStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSCodeRateLPStream.setStatus("current")


class _MgNITDSGuardInterval_Type(Integer32):
    """Custom type mgNITDSGuardInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MgNITDSGuardInterval_Type.__name__ = "Integer32"
_MgNITDSGuardInterval_Object = MibTableColumn
mgNITDSGuardInterval = _MgNITDSGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 17),
    _MgNITDSGuardInterval_Type()
)
mgNITDSGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSGuardInterval.setStatus("current")


class _MgNITDSTransmissionMode_Type(Integer32):
    """Custom type mgNITDSTransmissionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MgNITDSTransmissionMode_Type.__name__ = "Integer32"
_MgNITDSTransmissionMode_Object = MibTableColumn
mgNITDSTransmissionMode = _MgNITDSTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 18),
    _MgNITDSTransmissionMode_Type()
)
mgNITDSTransmissionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSTransmissionMode.setStatus("current")


class _MgNITDSOtherFrequencyFlag_Type(Integer32):
    """Custom type mgNITDSOtherFrequencyFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MgNITDSOtherFrequencyFlag_Type.__name__ = "Integer32"
_MgNITDSOtherFrequencyFlag_Object = MibTableColumn
mgNITDSOtherFrequencyFlag = _MgNITDSOtherFrequencyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 8, 1, 19),
    _MgNITDSOtherFrequencyFlag_Type()
)
mgNITDSOtherFrequencyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNITDSOtherFrequencyFlag.setStatus("current")
_MgRFCharacteristics_ObjectIdentity = ObjectIdentity
mgRFCharacteristics = _MgRFCharacteristics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2)
)
_MgRFCharacteristicsTrap_ObjectIdentity = ObjectIdentity
mgRFCharacteristicsTrap = _MgRFCharacteristicsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1)
)
_RfTrapPrefix_ObjectIdentity = ObjectIdentity
rfTrapPrefix = _RfTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1, 0)
)
_RfCharacteristicsTrapControlTable_Object = MibTable
rfCharacteristicsTrapControlTable = _RfCharacteristicsTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rfCharacteristicsTrapControlTable.setStatus("current")
_RfCharacteristicsTrapControlEntry_Object = MibTableRow
rfCharacteristicsTrapControlEntry = _RfCharacteristicsTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1, 1, 1)
)
rfCharacteristicsTrapControlEntry.setIndexNames(
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "rfCharacteristicsTrapControlInputNumber"),
)
if mibBuilder.loadTexts:
    rfCharacteristicsTrapControlEntry.setStatus("current")
_RfCharacteristicsTrapControlInputNumber_Type = InputNumber
_RfCharacteristicsTrapControlInputNumber_Object = MibTableColumn
rfCharacteristicsTrapControlInputNumber = _RfCharacteristicsTrapControlInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1, 1, 1, 1),
    _RfCharacteristicsTrapControlInputNumber_Type()
)
rfCharacteristicsTrapControlInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfCharacteristicsTrapControlInputNumber.setStatus("current")
_RfCharacteristicsTrapControlOID_Type = ObjectIdentifier
_RfCharacteristicsTrapControlOID_Object = MibTableColumn
rfCharacteristicsTrapControlOID = _RfCharacteristicsTrapControlOID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1, 1, 1, 2),
    _RfCharacteristicsTrapControlOID_Type()
)
rfCharacteristicsTrapControlOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rfCharacteristicsTrapControlOID.setStatus("current")
_RfCharacteristicsTrapControlChangeTime_Type = DateAndTime
_RfCharacteristicsTrapControlChangeTime_Object = MibTableColumn
rfCharacteristicsTrapControlChangeTime = _RfCharacteristicsTrapControlChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1, 1, 1, 3),
    _RfCharacteristicsTrapControlChangeTime_Type()
)
rfCharacteristicsTrapControlChangeTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rfCharacteristicsTrapControlChangeTime.setStatus("current")
_RfCharacteristicsTrapControlRateStatus_Type = RateStatus
_RfCharacteristicsTrapControlRateStatus_Object = MibTableColumn
rfCharacteristicsTrapControlRateStatus = _RfCharacteristicsTrapControlRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1, 1, 1, 4),
    _RfCharacteristicsTrapControlRateStatus_Type()
)
rfCharacteristicsTrapControlRateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfCharacteristicsTrapControlRateStatus.setStatus("current")


class _RfCharacteristicsTrapControlPeriod_Type(Unsigned32):
    """Custom type rfCharacteristicsTrapControlPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_RfCharacteristicsTrapControlPeriod_Type.__name__ = "Unsigned32"
_RfCharacteristicsTrapControlPeriod_Object = MibTableColumn
rfCharacteristicsTrapControlPeriod = _RfCharacteristicsTrapControlPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1, 1, 1, 5),
    _RfCharacteristicsTrapControlPeriod_Type()
)
rfCharacteristicsTrapControlPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfCharacteristicsTrapControlPeriod.setStatus("current")
if mibBuilder.loadTexts:
    rfCharacteristicsTrapControlPeriod.setUnits("millisecond")
_RfCharacteristicsTrapInput_Type = InputNumber
_RfCharacteristicsTrapInput_Object = MibScalar
rfCharacteristicsTrapInput = _RfCharacteristicsTrapInput_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1, 2),
    _RfCharacteristicsTrapInput_Type()
)
rfCharacteristicsTrapInput.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rfCharacteristicsTrapInput.setStatus("current")
_MgRFCharacteristicsTable_Object = MibTable
mgRFCharacteristicsTable = _MgRFCharacteristicsTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mgRFCharacteristicsTable.setStatus("current")
_MgRFCharacteristicsEntry_Object = MibTableRow
mgRFCharacteristicsEntry = _MgRFCharacteristicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1)
)
mgRFCharacteristicsEntry.setIndexNames(
    (0, "DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFInputNumber"),
)
if mibBuilder.loadTexts:
    mgRFCharacteristicsEntry.setStatus("current")
_MgRFInputNumber_Type = InputNumber
_MgRFInputNumber_Object = MibTableColumn
mgRFInputNumber = _MgRFInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 1),
    _MgRFInputNumber_Type()
)
mgRFInputNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgRFInputNumber.setStatus("current")
_MgRFSystemType_Type = DeliverySystemType
_MgRFSystemType_Object = MibTableColumn
mgRFSystemType = _MgRFSystemType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 2),
    _MgRFSystemType_Type()
)
mgRFSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRFSystemType.setStatus("current")
_MgRFCentreFrequency_Type = FloatingPoint
_MgRFCentreFrequency_Object = MibTableColumn
mgRFCentreFrequency = _MgRFCentreFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 3),
    _MgRFCentreFrequency_Type()
)
mgRFCentreFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRFCentreFrequency.setStatus("current")
if mibBuilder.loadTexts:
    mgRFCentreFrequency.setUnits("MHz")
_MgRFModulation_Type = Modulation
_MgRFModulation_Object = MibTableColumn
mgRFModulation = _MgRFModulation_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 4),
    _MgRFModulation_Type()
)
mgRFModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRFModulation.setStatus("current")
_MgRFFecInner_Type = InnerCodeRate
_MgRFFecInner_Object = MibTableColumn
mgRFFecInner = _MgRFFecInner_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 5),
    _MgRFFecInner_Type()
)
mgRFFecInner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRFFecInner.setStatus("current")
_MgRFFecInnerLP_Type = InnerCodeRate
_MgRFFecInnerLP_Object = MibTableColumn
mgRFFecInnerLP = _MgRFFecInnerLP_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 6),
    _MgRFFecInnerLP_Type()
)
mgRFFecInnerLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRFFecInnerLP.setStatus("current")
_MgRFSymbolRate_Type = FloatingPoint
_MgRFSymbolRate_Object = MibTableColumn
mgRFSymbolRate = _MgRFSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 7),
    _MgRFSymbolRate_Type()
)
mgRFSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRFSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    mgRFSymbolRate.setUnits("Msymbol/s")
_MgRFBandwidth_Type = FloatingPoint
_MgRFBandwidth_Object = MibTableColumn
mgRFBandwidth = _MgRFBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 8),
    _MgRFBandwidth_Type()
)
mgRFBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRFBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mgRFBandwidth.setUnits("MHz")
_MgRFTransmissionMode_Type = TerrestrialTransmissionMode
_MgRFTransmissionMode_Object = MibTableColumn
mgRFTransmissionMode = _MgRFTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 9),
    _MgRFTransmissionMode_Type()
)
mgRFTransmissionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRFTransmissionMode.setStatus("current")
_MgRFIsHierarchical_Type = TruthValue
_MgRFIsHierarchical_Object = MibTableColumn
mgRFIsHierarchical = _MgRFIsHierarchical_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 10),
    _MgRFIsHierarchical_Type()
)
mgRFIsHierarchical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRFIsHierarchical.setStatus("current")
_MgRFGuardInterval_Type = GuardInterval
_MgRFGuardInterval_Object = MibTableColumn
mgRFGuardInterval = _MgRFGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 2, 1, 11),
    _MgRFGuardInterval_Type()
)
mgRFGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRFGuardInterval.setStatus("current")
_MgSignalCharacteristicsConformance_ObjectIdentity = ObjectIdentity
mgSignalCharacteristicsConformance = _MgSignalCharacteristicsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 2)
)
_MgSignalCharacteristicsCompliances_ObjectIdentity = ObjectIdentity
mgSignalCharacteristicsCompliances = _MgSignalCharacteristicsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 2, 1)
)
_MgSignalCharacteristicsGroups_ObjectIdentity = ObjectIdentity
mgSignalCharacteristicsGroups = _MgSignalCharacteristicsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 2, 3)
)

# Managed Objects groups

mgSCTransportStreamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 2, 3, 1)
)
mgSCTransportStreamGroup.setObjects(
      *(("DVB-MGSIGNALCHARACTERISTICS-MIB", "structureTrapControlOID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "structureTrapControlChangeTime"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "structureTrapControlRateStatus"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "structureTrapControlPeriod"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "structureTrapInput"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgTSId"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgTSOriginalNetworkID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgTSNetworkID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgTSNetworkName"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServiceType"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServiceName"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServiceProviderName"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServicePMTPID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServicePCRPID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServiceCondAccess"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServiceEITComponentDescriptor"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgPIDType"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgPIDCondAccess"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgEMMCASystemID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgServiceECMCASystemID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgPIDECMCASystemID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSSystemType"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSFrequency"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSFecOuter"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSCableModulation"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSSymbolRate"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSFecInner"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSOrbitalPosition"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSWestEastFlag"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSPolarization"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSSatelliteModulation"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSBandwidth"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSConstellation"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSHierarchyInformation"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSCodeRateHPStream"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSCodeRateLPStream"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSGuardInterval"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSTransmissionMode"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgNITDSOtherFrequencyFlag"))
)
if mibBuilder.loadTexts:
    mgSCTransportStreamGroup.setStatus("current")

mgSCRadioFrequencyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 2, 3, 2)
)
mgSCRadioFrequencyGroup.setObjects(
      *(("DVB-MGSIGNALCHARACTERISTICS-MIB", "rfCharacteristicsTrapControlOID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "rfCharacteristicsTrapControlChangeTime"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "rfCharacteristicsTrapControlRateStatus"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "rfCharacteristicsTrapControlPeriod"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "rfCharacteristicsTrapInput"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFSystemType"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFCentreFrequency"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFModulation"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFFecInner"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFFecInnerLP"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFSymbolRate"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFBandwidth"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFTransmissionMode"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFIsHierarchical"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "mgRFGuardInterval"))
)
if mibBuilder.loadTexts:
    mgSCRadioFrequencyGroup.setStatus("current")


# Notification objects

tsStructureChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 1, 1, 0, 1)
)
tsStructureChangeTrap.setObjects(
      *(("DVB-MGSIGNALCHARACTERISTICS-MIB", "structureTrapInput"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "structureTrapControlOID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "structureTrapControlChangeTime"))
)
if mibBuilder.loadTexts:
    tsStructureChangeTrap.setStatus(
        "current"
    )

rfCharacteristicsChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 1, 2, 1, 0, 1)
)
rfCharacteristicsChangeTrap.setObjects(
      *(("DVB-MGSIGNALCHARACTERISTICS-MIB", "rfCharacteristicsTrapInput"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "rfCharacteristicsTrapControlOID"),
        ("DVB-MGSIGNALCHARACTERISTICS-MIB", "rfCharacteristicsTrapControlChangeTime"))
)
if mibBuilder.loadTexts:
    rfCharacteristicsChangeTrap.setStatus(
        "current"
    )


# Notifications groups

mgSCTransportStreamTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 2, 3, 3)
)
mgSCTransportStreamTrapGroup.setObjects(
    ("DVB-MGSIGNALCHARACTERISTICS-MIB", "tsStructureChangeTrap")
)
if mibBuilder.loadTexts:
    mgSCTransportStreamTrapGroup.setStatus(
        "current"
    )

mgSCRadioFrequencyTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 2, 3, 4)
)
mgSCRadioFrequencyTrapGroup.setObjects(
    ("DVB-MGSIGNALCHARACTERISTICS-MIB", "rfCharacteristicsChangeTrap")
)
if mibBuilder.loadTexts:
    mgSCRadioFrequencyTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mgSCTransportStreamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mgSCTransportStreamCompliance.setStatus(
        "current"
    )

mgSCRadioFrequencyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2696, 3, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mgSCRadioFrequencyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DVB-MGSIGNALCHARACTERISTICS-MIB",
    **{"CASystemID": CASystemID,
       "EncryptionState": EncryptionState,
       "GuardInterval": GuardInterval,
       "InnerCodeRate": InnerCodeRate,
       "NetworkID": NetworkID,
       "PID": PID,
       "ReadableString": ReadableString,
       "TerrestrialTransmissionMode": TerrestrialTransmissionMode,
       "dvb": dvb,
       "mg": mg,
       "mgSignalCharacteristics": mgSignalCharacteristics,
       "mgSignalCharacteristicsObjects": mgSignalCharacteristicsObjects,
       "mgTSStructure": mgTSStructure,
       "mgTSStructureTrap": mgTSStructureTrap,
       "structureTrapPrefix": structureTrapPrefix,
       "tsStructureChangeTrap": tsStructureChangeTrap,
       "structureTrapControlTable": structureTrapControlTable,
       "structureTrapControlEntry": structureTrapControlEntry,
       "structureTrapControlInputNumber": structureTrapControlInputNumber,
       "structureTrapControlOID": structureTrapControlOID,
       "structureTrapControlChangeTime": structureTrapControlChangeTime,
       "structureTrapControlRateStatus": structureTrapControlRateStatus,
       "structureTrapControlPeriod": structureTrapControlPeriod,
       "structureTrapInput": structureTrapInput,
       "mgTSTable": mgTSTable,
       "mgTSEntry": mgTSEntry,
       "mgTSInputNumber": mgTSInputNumber,
       "mgTSId": mgTSId,
       "mgTSOriginalNetworkID": mgTSOriginalNetworkID,
       "mgTSNetworkID": mgTSNetworkID,
       "mgTSNetworkName": mgTSNetworkName,
       "mgServiceTable": mgServiceTable,
       "mgServiceEntry": mgServiceEntry,
       "mgServiceInputNumber": mgServiceInputNumber,
       "mgServiceNumber": mgServiceNumber,
       "mgServiceType": mgServiceType,
       "mgServiceName": mgServiceName,
       "mgServiceProviderName": mgServiceProviderName,
       "mgServicePMTPID": mgServicePMTPID,
       "mgServicePCRPID": mgServicePCRPID,
       "mgServiceCondAccess": mgServiceCondAccess,
       "mgServiceEITComponentDescriptor": mgServiceEITComponentDescriptor,
       "mgPIDTable": mgPIDTable,
       "mgPIDEntry": mgPIDEntry,
       "mgPIDInputNumber": mgPIDInputNumber,
       "mgPIDServiceNumber": mgPIDServiceNumber,
       "mgPIDNumber": mgPIDNumber,
       "mgPIDType": mgPIDType,
       "mgPIDCondAccess": mgPIDCondAccess,
       "mgEMMTable": mgEMMTable,
       "mgEMMEntry": mgEMMEntry,
       "mgEMMInputNumber": mgEMMInputNumber,
       "mgEMMCaPID": mgEMMCaPID,
       "mgEMMCASystemID": mgEMMCASystemID,
       "mgServiceECMTable": mgServiceECMTable,
       "mgServiceECMEntry": mgServiceECMEntry,
       "mgServiceECMInputNumber": mgServiceECMInputNumber,
       "mgServiceECMServiceNumber": mgServiceECMServiceNumber,
       "mgServiceECMCaPID": mgServiceECMCaPID,
       "mgServiceECMCASystemID": mgServiceECMCASystemID,
       "mgPIDECMTable": mgPIDECMTable,
       "mgPIDECMEntry": mgPIDECMEntry,
       "mgPIDECMInputNumber": mgPIDECMInputNumber,
       "mgPIDECMServiceNumber": mgPIDECMServiceNumber,
       "mgPIDECMPID": mgPIDECMPID,
       "mgPIDECMCaPID": mgPIDECMCaPID,
       "mgPIDECMCASystemID": mgPIDECMCASystemID,
       "mgNITDeliverySystemTable": mgNITDeliverySystemTable,
       "mgNITDeliverySystemEntry": mgNITDeliverySystemEntry,
       "mgNITDSInputNumber": mgNITDSInputNumber,
       "mgNITDSSystemType": mgNITDSSystemType,
       "mgNITDSFrequency": mgNITDSFrequency,
       "mgNITDSFecOuter": mgNITDSFecOuter,
       "mgNITDSCableModulation": mgNITDSCableModulation,
       "mgNITDSSymbolRate": mgNITDSSymbolRate,
       "mgNITDSFecInner": mgNITDSFecInner,
       "mgNITDSOrbitalPosition": mgNITDSOrbitalPosition,
       "mgNITDSWestEastFlag": mgNITDSWestEastFlag,
       "mgNITDSPolarization": mgNITDSPolarization,
       "mgNITDSSatelliteModulation": mgNITDSSatelliteModulation,
       "mgNITDSBandwidth": mgNITDSBandwidth,
       "mgNITDSConstellation": mgNITDSConstellation,
       "mgNITDSHierarchyInformation": mgNITDSHierarchyInformation,
       "mgNITDSCodeRateHPStream": mgNITDSCodeRateHPStream,
       "mgNITDSCodeRateLPStream": mgNITDSCodeRateLPStream,
       "mgNITDSGuardInterval": mgNITDSGuardInterval,
       "mgNITDSTransmissionMode": mgNITDSTransmissionMode,
       "mgNITDSOtherFrequencyFlag": mgNITDSOtherFrequencyFlag,
       "mgRFCharacteristics": mgRFCharacteristics,
       "mgRFCharacteristicsTrap": mgRFCharacteristicsTrap,
       "rfTrapPrefix": rfTrapPrefix,
       "rfCharacteristicsChangeTrap": rfCharacteristicsChangeTrap,
       "rfCharacteristicsTrapControlTable": rfCharacteristicsTrapControlTable,
       "rfCharacteristicsTrapControlEntry": rfCharacteristicsTrapControlEntry,
       "rfCharacteristicsTrapControlInputNumber": rfCharacteristicsTrapControlInputNumber,
       "rfCharacteristicsTrapControlOID": rfCharacteristicsTrapControlOID,
       "rfCharacteristicsTrapControlChangeTime": rfCharacteristicsTrapControlChangeTime,
       "rfCharacteristicsTrapControlRateStatus": rfCharacteristicsTrapControlRateStatus,
       "rfCharacteristicsTrapControlPeriod": rfCharacteristicsTrapControlPeriod,
       "rfCharacteristicsTrapInput": rfCharacteristicsTrapInput,
       "mgRFCharacteristicsTable": mgRFCharacteristicsTable,
       "mgRFCharacteristicsEntry": mgRFCharacteristicsEntry,
       "mgRFInputNumber": mgRFInputNumber,
       "mgRFSystemType": mgRFSystemType,
       "mgRFCentreFrequency": mgRFCentreFrequency,
       "mgRFModulation": mgRFModulation,
       "mgRFFecInner": mgRFFecInner,
       "mgRFFecInnerLP": mgRFFecInnerLP,
       "mgRFSymbolRate": mgRFSymbolRate,
       "mgRFBandwidth": mgRFBandwidth,
       "mgRFTransmissionMode": mgRFTransmissionMode,
       "mgRFIsHierarchical": mgRFIsHierarchical,
       "mgRFGuardInterval": mgRFGuardInterval,
       "mgSignalCharacteristicsConformance": mgSignalCharacteristicsConformance,
       "mgSignalCharacteristicsCompliances": mgSignalCharacteristicsCompliances,
       "mgSCTransportStreamCompliance": mgSCTransportStreamCompliance,
       "mgSCRadioFrequencyCompliance": mgSCRadioFrequencyCompliance,
       "mgSignalCharacteristicsGroups": mgSignalCharacteristicsGroups,
       "mgSCTransportStreamGroup": mgSCTransportStreamGroup,
       "mgSCRadioFrequencyGroup": mgSCRadioFrequencyGroup,
       "mgSCTransportStreamTrapGroup": mgSCTransportStreamTrapGroup,
       "mgSCRadioFrequencyTrapGroup": mgSCRadioFrequencyTrapGroup}
)
