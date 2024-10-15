# SNMP MIB module (NTWS-AP-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-AP-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:52 2024
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

(NtwsApAttachType,
 NtwsApFingerprint,
 NtwsApNum,
 NtwsApPortOrDapNum,
 NtwsApSerialNum,
 NtwsApState,
 NtwsChannelNum,
 NtwsPowerLevel,
 NtwsRadioChannelWidth,
 NtwsRadioConfigState,
 NtwsRadioEnable,
 NtwsRadioMimoState,
 NtwsRadioMode,
 NtwsRadioNum,
 NtwsRadioRate,
 NtwsRadioRateEx,
 NtwsRadioType) = mibBuilder.importSymbols(
    "NTWS-AP-TC",
    "NtwsApAttachType",
    "NtwsApFingerprint",
    "NtwsApNum",
    "NtwsApPortOrDapNum",
    "NtwsApSerialNum",
    "NtwsApState",
    "NtwsChannelNum",
    "NtwsPowerLevel",
    "NtwsRadioChannelWidth",
    "NtwsRadioConfigState",
    "NtwsRadioEnable",
    "NtwsRadioMimoState",
    "NtwsRadioMode",
    "NtwsRadioNum",
    "NtwsRadioRate",
    "NtwsRadioRateEx",
    "NtwsRadioType")

(NtwsPhysPortNumberOrZero,) = mibBuilder.importSymbols(
    "NTWS-BASIC-TC",
    "NtwsPhysPortNumberOrZero")

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntwsApStatusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5)
)
ntwsApStatusMib.setRevisions(
        ("2009-09-10 01:50",
         "2009-02-13 01:41",
         "2008-12-01 01:15",
         "2008-11-04 01:11",
         "2008-05-22 01:07",
         "2008-05-09 01:04",
         "2008-02-14 01:03",
         "2007-12-07 01:00",
         "2007-09-25 00:52",
         "2007-07-06 00:51",
         "2007-07-05 00:50",
         "2006-09-27 00:43",
         "2006-07-28 00:35",
         "2006-07-28 00:34",
         "2006-06-26 00:20",
         "2006-06-21 00:18",
         "2006-05-10 00:17",
         "2006-03-30 00:16")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtwsRadioOpRateSetSingleValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class NtwsRadioOpRateSetMandatory(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )



class NtwsRadioOpRateSetDisabled(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )



# MIB Managed Objects in the order of their OIDs

_NtwsApStatusObjects_ObjectIdentity = ObjectIdentity
ntwsApStatusObjects = _NtwsApStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1)
)
_NtwsApStatDataObjects_ObjectIdentity = ObjectIdentity
ntwsApStatDataObjects = _NtwsApStatDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1)
)
_NtwsApStatNumAps_Type = Unsigned32
_NtwsApStatNumAps_Object = MibScalar
ntwsApStatNumAps = _NtwsApStatNumAps_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 1),
    _NtwsApStatNumAps_Type()
)
ntwsApStatNumAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatNumAps.setStatus("current")
_NtwsApStatApStatusTable_Object = MibTable
ntwsApStatApStatusTable = _NtwsApStatApStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ntwsApStatApStatusTable.setStatus("current")
_NtwsApStatApStatusEntry_Object = MibTableRow
ntwsApStatApStatusEntry = _NtwsApStatApStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1)
)
ntwsApStatApStatusEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatApStatusSerialNum"),
)
if mibBuilder.loadTexts:
    ntwsApStatApStatusEntry.setStatus("current")
_NtwsApStatApStatusSerialNum_Type = NtwsApSerialNum
_NtwsApStatApStatusSerialNum_Object = MibTableColumn
ntwsApStatApStatusSerialNum = _NtwsApStatApStatusSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 1),
    _NtwsApStatApStatusSerialNum_Type()
)
ntwsApStatApStatusSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatApStatusSerialNum.setStatus("current")
_NtwsApStatApStatusBaseMac_Type = MacAddress
_NtwsApStatApStatusBaseMac_Object = MibTableColumn
ntwsApStatApStatusBaseMac = _NtwsApStatApStatusBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 2),
    _NtwsApStatApStatusBaseMac_Type()
)
ntwsApStatApStatusBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusBaseMac.setStatus("current")
_NtwsApStatApStatusAttachType_Type = NtwsApAttachType
_NtwsApStatApStatusAttachType_Object = MibTableColumn
ntwsApStatApStatusAttachType = _NtwsApStatApStatusAttachType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 3),
    _NtwsApStatApStatusAttachType_Type()
)
ntwsApStatApStatusAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusAttachType.setStatus("current")
_NtwsApStatApStatusPortOrDapNum_Type = NtwsApPortOrDapNum
_NtwsApStatApStatusPortOrDapNum_Object = MibTableColumn
ntwsApStatApStatusPortOrDapNum = _NtwsApStatApStatusPortOrDapNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 4),
    _NtwsApStatApStatusPortOrDapNum_Type()
)
ntwsApStatApStatusPortOrDapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusPortOrDapNum.setStatus("obsolete")
_NtwsApStatApStatusApState_Type = NtwsApState
_NtwsApStatApStatusApState_Object = MibTableColumn
ntwsApStatApStatusApState = _NtwsApStatApStatusApState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 5),
    _NtwsApStatApStatusApState_Type()
)
ntwsApStatApStatusApState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusApState.setStatus("current")
_NtwsApStatApStatusModel_Type = DisplayString
_NtwsApStatApStatusModel_Object = MibTableColumn
ntwsApStatApStatusModel = _NtwsApStatApStatusModel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 6),
    _NtwsApStatApStatusModel_Type()
)
ntwsApStatApStatusModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusModel.setStatus("current")
_NtwsApStatApStatusFingerprint_Type = NtwsApFingerprint
_NtwsApStatApStatusFingerprint_Object = MibTableColumn
ntwsApStatApStatusFingerprint = _NtwsApStatApStatusFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 7),
    _NtwsApStatApStatusFingerprint_Type()
)
ntwsApStatApStatusFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusFingerprint.setStatus("current")
_NtwsApStatApStatusApName_Type = DisplayString
_NtwsApStatApStatusApName_Object = MibTableColumn
ntwsApStatApStatusApName = _NtwsApStatApStatusApName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 8),
    _NtwsApStatApStatusApName_Type()
)
ntwsApStatApStatusApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusApName.setStatus("current")
_NtwsApStatApStatusVlan_Type = DisplayString
_NtwsApStatApStatusVlan_Object = MibTableColumn
ntwsApStatApStatusVlan = _NtwsApStatApStatusVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 9),
    _NtwsApStatApStatusVlan_Type()
)
ntwsApStatApStatusVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusVlan.setStatus("current")
_NtwsApStatApStatusIpAddress_Type = IpAddress
_NtwsApStatApStatusIpAddress_Object = MibTableColumn
ntwsApStatApStatusIpAddress = _NtwsApStatApStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 10),
    _NtwsApStatApStatusIpAddress_Type()
)
ntwsApStatApStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusIpAddress.setStatus("current")
_NtwsApStatApStatusUptimeSecs_Type = Unsigned32
_NtwsApStatApStatusUptimeSecs_Object = MibTableColumn
ntwsApStatApStatusUptimeSecs = _NtwsApStatApStatusUptimeSecs_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 11),
    _NtwsApStatApStatusUptimeSecs_Type()
)
ntwsApStatApStatusUptimeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusUptimeSecs.setStatus("current")
_NtwsApStatApStatusCpuInfo_Type = DisplayString
_NtwsApStatApStatusCpuInfo_Object = MibTableColumn
ntwsApStatApStatusCpuInfo = _NtwsApStatApStatusCpuInfo_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 12),
    _NtwsApStatApStatusCpuInfo_Type()
)
ntwsApStatApStatusCpuInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusCpuInfo.setStatus("current")
_NtwsApStatApStatusManufacturerId_Type = DisplayString
_NtwsApStatApStatusManufacturerId_Object = MibTableColumn
ntwsApStatApStatusManufacturerId = _NtwsApStatApStatusManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 13),
    _NtwsApStatApStatusManufacturerId_Type()
)
ntwsApStatApStatusManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusManufacturerId.setStatus("current")
_NtwsApStatApStatusRamBytes_Type = Unsigned32
_NtwsApStatApStatusRamBytes_Object = MibTableColumn
ntwsApStatApStatusRamBytes = _NtwsApStatApStatusRamBytes_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 14),
    _NtwsApStatApStatusRamBytes_Type()
)
ntwsApStatApStatusRamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusRamBytes.setStatus("current")
_NtwsApStatApStatusHardwareRev_Type = DisplayString
_NtwsApStatApStatusHardwareRev_Object = MibTableColumn
ntwsApStatApStatusHardwareRev = _NtwsApStatApStatusHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 15),
    _NtwsApStatApStatusHardwareRev_Type()
)
ntwsApStatApStatusHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusHardwareRev.setStatus("current")
_NtwsApStatApStatusClientSessions_Type = Unsigned32
_NtwsApStatApStatusClientSessions_Object = MibTableColumn
ntwsApStatApStatusClientSessions = _NtwsApStatApStatusClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 16),
    _NtwsApStatApStatusClientSessions_Type()
)
ntwsApStatApStatusClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusClientSessions.setStatus("current")
_NtwsApStatApStatusSoftwareVer_Type = DisplayString
_NtwsApStatApStatusSoftwareVer_Object = MibTableColumn
ntwsApStatApStatusSoftwareVer = _NtwsApStatApStatusSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 17),
    _NtwsApStatApStatusSoftwareVer_Type()
)
ntwsApStatApStatusSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusSoftwareVer.setStatus("current")
_NtwsApStatApStatusBootVer_Type = DisplayString
_NtwsApStatApStatusBootVer_Object = MibTableColumn
ntwsApStatApStatusBootVer = _NtwsApStatApStatusBootVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 18),
    _NtwsApStatApStatusBootVer_Type()
)
ntwsApStatApStatusBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusBootVer.setStatus("current")
_NtwsApStatApStatusApNum_Type = NtwsApNum
_NtwsApStatApStatusApNum_Object = MibTableColumn
ntwsApStatApStatusApNum = _NtwsApStatApStatusApNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 19),
    _NtwsApStatApStatusApNum_Type()
)
ntwsApStatApStatusApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusApNum.setStatus("current")
_NtwsApStatApStatusPhysPortNum_Type = NtwsPhysPortNumberOrZero
_NtwsApStatApStatusPhysPortNum_Object = MibTableColumn
ntwsApStatApStatusPhysPortNum = _NtwsApStatApStatusPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 20),
    _NtwsApStatApStatusPhysPortNum_Type()
)
ntwsApStatApStatusPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusPhysPortNum.setStatus("current")
_NtwsApStatApStatusIpNetmask_Type = IpAddress
_NtwsApStatApStatusIpNetmask_Object = MibTableColumn
ntwsApStatApStatusIpNetmask = _NtwsApStatApStatusIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 21),
    _NtwsApStatApStatusIpNetmask_Type()
)
ntwsApStatApStatusIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusIpNetmask.setStatus("current")
_NtwsApStatApStatusWiredIfNumber_Type = Unsigned32
_NtwsApStatApStatusWiredIfNumber_Object = MibTableColumn
ntwsApStatApStatusWiredIfNumber = _NtwsApStatApStatusWiredIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 2, 1, 22),
    _NtwsApStatApStatusWiredIfNumber_Type()
)
ntwsApStatApStatusWiredIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusWiredIfNumber.setStatus("current")
_NtwsApStatApStatusMacTable_Object = MibTable
ntwsApStatApStatusMacTable = _NtwsApStatApStatusMacTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacTable.setStatus("current")
_NtwsApStatApStatusMacEntry_Object = MibTableRow
ntwsApStatApStatusMacEntry = _NtwsApStatApStatusMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1)
)
ntwsApStatApStatusMacEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacBaseMac"),
)
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacEntry.setStatus("current")
_NtwsApStatApStatusMacBaseMac_Type = MacAddress
_NtwsApStatApStatusMacBaseMac_Object = MibTableColumn
ntwsApStatApStatusMacBaseMac = _NtwsApStatApStatusMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 1),
    _NtwsApStatApStatusMacBaseMac_Type()
)
ntwsApStatApStatusMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacBaseMac.setStatus("current")
_NtwsApStatApStatusMacSerialNum_Type = NtwsApSerialNum
_NtwsApStatApStatusMacSerialNum_Object = MibTableColumn
ntwsApStatApStatusMacSerialNum = _NtwsApStatApStatusMacSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 2),
    _NtwsApStatApStatusMacSerialNum_Type()
)
ntwsApStatApStatusMacSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacSerialNum.setStatus("current")
_NtwsApStatApStatusMacAttachType_Type = NtwsApAttachType
_NtwsApStatApStatusMacAttachType_Object = MibTableColumn
ntwsApStatApStatusMacAttachType = _NtwsApStatApStatusMacAttachType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 3),
    _NtwsApStatApStatusMacAttachType_Type()
)
ntwsApStatApStatusMacAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacAttachType.setStatus("current")
_NtwsApStatApStatusMacPortOrDapNum_Type = NtwsApPortOrDapNum
_NtwsApStatApStatusMacPortOrDapNum_Object = MibTableColumn
ntwsApStatApStatusMacPortOrDapNum = _NtwsApStatApStatusMacPortOrDapNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 4),
    _NtwsApStatApStatusMacPortOrDapNum_Type()
)
ntwsApStatApStatusMacPortOrDapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacPortOrDapNum.setStatus("obsolete")
_NtwsApStatApStatusMacApState_Type = NtwsApState
_NtwsApStatApStatusMacApState_Object = MibTableColumn
ntwsApStatApStatusMacApState = _NtwsApStatApStatusMacApState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 5),
    _NtwsApStatApStatusMacApState_Type()
)
ntwsApStatApStatusMacApState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacApState.setStatus("current")
_NtwsApStatApStatusMacModel_Type = DisplayString
_NtwsApStatApStatusMacModel_Object = MibTableColumn
ntwsApStatApStatusMacModel = _NtwsApStatApStatusMacModel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 6),
    _NtwsApStatApStatusMacModel_Type()
)
ntwsApStatApStatusMacModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacModel.setStatus("current")
_NtwsApStatApStatusMacFingerprint_Type = NtwsApFingerprint
_NtwsApStatApStatusMacFingerprint_Object = MibTableColumn
ntwsApStatApStatusMacFingerprint = _NtwsApStatApStatusMacFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 7),
    _NtwsApStatApStatusMacFingerprint_Type()
)
ntwsApStatApStatusMacFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacFingerprint.setStatus("current")
_NtwsApStatApStatusMacApName_Type = DisplayString
_NtwsApStatApStatusMacApName_Object = MibTableColumn
ntwsApStatApStatusMacApName = _NtwsApStatApStatusMacApName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 8),
    _NtwsApStatApStatusMacApName_Type()
)
ntwsApStatApStatusMacApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacApName.setStatus("current")
_NtwsApStatApStatusMacVlan_Type = DisplayString
_NtwsApStatApStatusMacVlan_Object = MibTableColumn
ntwsApStatApStatusMacVlan = _NtwsApStatApStatusMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 9),
    _NtwsApStatApStatusMacVlan_Type()
)
ntwsApStatApStatusMacVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacVlan.setStatus("current")
_NtwsApStatApStatusMacIpAddress_Type = IpAddress
_NtwsApStatApStatusMacIpAddress_Object = MibTableColumn
ntwsApStatApStatusMacIpAddress = _NtwsApStatApStatusMacIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 10),
    _NtwsApStatApStatusMacIpAddress_Type()
)
ntwsApStatApStatusMacIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacIpAddress.setStatus("current")
_NtwsApStatApStatusMacUptimeSecs_Type = Unsigned32
_NtwsApStatApStatusMacUptimeSecs_Object = MibTableColumn
ntwsApStatApStatusMacUptimeSecs = _NtwsApStatApStatusMacUptimeSecs_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 11),
    _NtwsApStatApStatusMacUptimeSecs_Type()
)
ntwsApStatApStatusMacUptimeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacUptimeSecs.setStatus("current")
_NtwsApStatApStatusMacCpuInfo_Type = DisplayString
_NtwsApStatApStatusMacCpuInfo_Object = MibTableColumn
ntwsApStatApStatusMacCpuInfo = _NtwsApStatApStatusMacCpuInfo_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 12),
    _NtwsApStatApStatusMacCpuInfo_Type()
)
ntwsApStatApStatusMacCpuInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacCpuInfo.setStatus("current")
_NtwsApStatApStatusMacManufacturerId_Type = DisplayString
_NtwsApStatApStatusMacManufacturerId_Object = MibTableColumn
ntwsApStatApStatusMacManufacturerId = _NtwsApStatApStatusMacManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 13),
    _NtwsApStatApStatusMacManufacturerId_Type()
)
ntwsApStatApStatusMacManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacManufacturerId.setStatus("current")
_NtwsApStatApStatusMacRamBytes_Type = Unsigned32
_NtwsApStatApStatusMacRamBytes_Object = MibTableColumn
ntwsApStatApStatusMacRamBytes = _NtwsApStatApStatusMacRamBytes_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 14),
    _NtwsApStatApStatusMacRamBytes_Type()
)
ntwsApStatApStatusMacRamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacRamBytes.setStatus("current")
_NtwsApStatApStatusMacHardwareRev_Type = DisplayString
_NtwsApStatApStatusMacHardwareRev_Object = MibTableColumn
ntwsApStatApStatusMacHardwareRev = _NtwsApStatApStatusMacHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 15),
    _NtwsApStatApStatusMacHardwareRev_Type()
)
ntwsApStatApStatusMacHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacHardwareRev.setStatus("current")
_NtwsApStatApStatusMacClientSessions_Type = Unsigned32
_NtwsApStatApStatusMacClientSessions_Object = MibTableColumn
ntwsApStatApStatusMacClientSessions = _NtwsApStatApStatusMacClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 16),
    _NtwsApStatApStatusMacClientSessions_Type()
)
ntwsApStatApStatusMacClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacClientSessions.setStatus("current")
_NtwsApStatApStatusMacSoftwareVer_Type = DisplayString
_NtwsApStatApStatusMacSoftwareVer_Object = MibTableColumn
ntwsApStatApStatusMacSoftwareVer = _NtwsApStatApStatusMacSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 17),
    _NtwsApStatApStatusMacSoftwareVer_Type()
)
ntwsApStatApStatusMacSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacSoftwareVer.setStatus("current")
_NtwsApStatApStatusMacBootVer_Type = DisplayString
_NtwsApStatApStatusMacBootVer_Object = MibTableColumn
ntwsApStatApStatusMacBootVer = _NtwsApStatApStatusMacBootVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 18),
    _NtwsApStatApStatusMacBootVer_Type()
)
ntwsApStatApStatusMacBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacBootVer.setStatus("current")
_NtwsApStatApStatusMacApNum_Type = NtwsApNum
_NtwsApStatApStatusMacApNum_Object = MibTableColumn
ntwsApStatApStatusMacApNum = _NtwsApStatApStatusMacApNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 19),
    _NtwsApStatApStatusMacApNum_Type()
)
ntwsApStatApStatusMacApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacApNum.setStatus("current")
_NtwsApStatApStatusMacPhysPortNum_Type = NtwsPhysPortNumberOrZero
_NtwsApStatApStatusMacPhysPortNum_Object = MibTableColumn
ntwsApStatApStatusMacPhysPortNum = _NtwsApStatApStatusMacPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 20),
    _NtwsApStatApStatusMacPhysPortNum_Type()
)
ntwsApStatApStatusMacPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacPhysPortNum.setStatus("current")
_NtwsApStatApStatusMacIpNetmask_Type = IpAddress
_NtwsApStatApStatusMacIpNetmask_Object = MibTableColumn
ntwsApStatApStatusMacIpNetmask = _NtwsApStatApStatusMacIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 21),
    _NtwsApStatApStatusMacIpNetmask_Type()
)
ntwsApStatApStatusMacIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacIpNetmask.setStatus("current")
_NtwsApStatApStatusMacWiredIfNumber_Type = Unsigned32
_NtwsApStatApStatusMacWiredIfNumber_Object = MibTableColumn
ntwsApStatApStatusMacWiredIfNumber = _NtwsApStatApStatusMacWiredIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 3, 1, 22),
    _NtwsApStatApStatusMacWiredIfNumber_Type()
)
ntwsApStatApStatusMacWiredIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatApStatusMacWiredIfNumber.setStatus("current")
_NtwsApStatRadioStatusTable_Object = MibTable
ntwsApStatRadioStatusTable = _NtwsApStatRadioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusTable.setStatus("current")
_NtwsApStatRadioStatusEntry_Object = MibTableRow
ntwsApStatRadioStatusEntry = _NtwsApStatRadioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1)
)
ntwsApStatRadioStatusEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusApSerialNum"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusRadioNum"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusEntry.setStatus("current")
_NtwsApStatRadioStatusApSerialNum_Type = NtwsApSerialNum
_NtwsApStatRadioStatusApSerialNum_Object = MibTableColumn
ntwsApStatRadioStatusApSerialNum = _NtwsApStatRadioStatusApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 1),
    _NtwsApStatRadioStatusApSerialNum_Type()
)
ntwsApStatRadioStatusApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusApSerialNum.setStatus("current")
_NtwsApStatRadioStatusRadioNum_Type = NtwsRadioNum
_NtwsApStatRadioStatusRadioNum_Object = MibTableColumn
ntwsApStatRadioStatusRadioNum = _NtwsApStatRadioStatusRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 2),
    _NtwsApStatRadioStatusRadioNum_Type()
)
ntwsApStatRadioStatusRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusRadioNum.setStatus("current")
_NtwsApStatRadioStatusBaseMac_Type = MacAddress
_NtwsApStatRadioStatusBaseMac_Object = MibTableColumn
ntwsApStatRadioStatusBaseMac = _NtwsApStatRadioStatusBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 3),
    _NtwsApStatRadioStatusBaseMac_Type()
)
ntwsApStatRadioStatusBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusBaseMac.setStatus("current")
_NtwsApStatRadioStatusEnable_Type = NtwsRadioEnable
_NtwsApStatRadioStatusEnable_Object = MibTableColumn
ntwsApStatRadioStatusEnable = _NtwsApStatRadioStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 4),
    _NtwsApStatRadioStatusEnable_Type()
)
ntwsApStatRadioStatusEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusEnable.setStatus("obsolete")
_NtwsApStatRadioStatusRadioConfigState_Type = NtwsRadioConfigState
_NtwsApStatRadioStatusRadioConfigState_Object = MibTableColumn
ntwsApStatRadioStatusRadioConfigState = _NtwsApStatRadioStatusRadioConfigState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 5),
    _NtwsApStatRadioStatusRadioConfigState_Type()
)
ntwsApStatRadioStatusRadioConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusRadioConfigState.setStatus("current")
_NtwsApStatRadioStatusCurrentPowerLevel_Type = NtwsPowerLevel
_NtwsApStatRadioStatusCurrentPowerLevel_Object = MibTableColumn
ntwsApStatRadioStatusCurrentPowerLevel = _NtwsApStatRadioStatusCurrentPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 6),
    _NtwsApStatRadioStatusCurrentPowerLevel_Type()
)
ntwsApStatRadioStatusCurrentPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusCurrentPowerLevel.setStatus("current")
_NtwsApStatRadioStatusCurrentChannelNum_Type = NtwsChannelNum
_NtwsApStatRadioStatusCurrentChannelNum_Object = MibTableColumn
ntwsApStatRadioStatusCurrentChannelNum = _NtwsApStatRadioStatusCurrentChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 7),
    _NtwsApStatRadioStatusCurrentChannelNum_Type()
)
ntwsApStatRadioStatusCurrentChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusCurrentChannelNum.setStatus("current")
_NtwsApStatRadioStatusClientSessions_Type = Unsigned32
_NtwsApStatRadioStatusClientSessions_Object = MibTableColumn
ntwsApStatRadioStatusClientSessions = _NtwsApStatRadioStatusClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 8),
    _NtwsApStatRadioStatusClientSessions_Type()
)
ntwsApStatRadioStatusClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusClientSessions.setStatus("current")
_NtwsApStatRadioStatusMaxPowerLevel_Type = NtwsPowerLevel
_NtwsApStatRadioStatusMaxPowerLevel_Object = MibTableColumn
ntwsApStatRadioStatusMaxPowerLevel = _NtwsApStatRadioStatusMaxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 9),
    _NtwsApStatRadioStatusMaxPowerLevel_Type()
)
ntwsApStatRadioStatusMaxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMaxPowerLevel.setStatus("current")
_NtwsApStatRadioStatusRadioPhyType_Type = NtwsRadioType
_NtwsApStatRadioStatusRadioPhyType_Object = MibTableColumn
ntwsApStatRadioStatusRadioPhyType = _NtwsApStatRadioStatusRadioPhyType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 10),
    _NtwsApStatRadioStatusRadioPhyType_Type()
)
ntwsApStatRadioStatusRadioPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusRadioPhyType.setStatus("current")
_NtwsApStatRadioStatusRadioMode_Type = NtwsRadioMode
_NtwsApStatRadioStatusRadioMode_Object = MibTableColumn
ntwsApStatRadioStatusRadioMode = _NtwsApStatRadioStatusRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 11),
    _NtwsApStatRadioStatusRadioMode_Type()
)
ntwsApStatRadioStatusRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusRadioMode.setStatus("current")
_NtwsApStatRadioStatusRadioChannelWidth_Type = NtwsRadioChannelWidth
_NtwsApStatRadioStatusRadioChannelWidth_Object = MibTableColumn
ntwsApStatRadioStatusRadioChannelWidth = _NtwsApStatRadioStatusRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 12),
    _NtwsApStatRadioStatusRadioChannelWidth_Type()
)
ntwsApStatRadioStatusRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusRadioChannelWidth.setStatus("current")
_NtwsApStatRadioStatusRadioMimoState_Type = NtwsRadioMimoState
_NtwsApStatRadioStatusRadioMimoState_Object = MibTableColumn
ntwsApStatRadioStatusRadioMimoState = _NtwsApStatRadioStatusRadioMimoState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 13),
    _NtwsApStatRadioStatusRadioMimoState_Type()
)
ntwsApStatRadioStatusRadioMimoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusRadioMimoState.setStatus("current")
_NtwsApStatRadioStatusMinPowerLevel_Type = NtwsPowerLevel
_NtwsApStatRadioStatusMinPowerLevel_Object = MibTableColumn
ntwsApStatRadioStatusMinPowerLevel = _NtwsApStatRadioStatusMinPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 4, 1, 14),
    _NtwsApStatRadioStatusMinPowerLevel_Type()
)
ntwsApStatRadioStatusMinPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMinPowerLevel.setStatus("current")
_NtwsApStatRadioStatusMacTable_Object = MibTable
ntwsApStatRadioStatusMacTable = _NtwsApStatRadioStatusMacTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacTable.setStatus("current")
_NtwsApStatRadioStatusMacEntry_Object = MibTableRow
ntwsApStatRadioStatusMacEntry = _NtwsApStatRadioStatusMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1)
)
ntwsApStatRadioStatusMacEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacBaseMac"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacEntry.setStatus("current")
_NtwsApStatRadioStatusMacBaseMac_Type = MacAddress
_NtwsApStatRadioStatusMacBaseMac_Object = MibTableColumn
ntwsApStatRadioStatusMacBaseMac = _NtwsApStatRadioStatusMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 1),
    _NtwsApStatRadioStatusMacBaseMac_Type()
)
ntwsApStatRadioStatusMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacBaseMac.setStatus("current")
_NtwsApStatRadioStatusMacApSerialNum_Type = NtwsApSerialNum
_NtwsApStatRadioStatusMacApSerialNum_Object = MibTableColumn
ntwsApStatRadioStatusMacApSerialNum = _NtwsApStatRadioStatusMacApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 2),
    _NtwsApStatRadioStatusMacApSerialNum_Type()
)
ntwsApStatRadioStatusMacApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacApSerialNum.setStatus("current")
_NtwsApStatRadioStatusMacRadioNum_Type = NtwsRadioNum
_NtwsApStatRadioStatusMacRadioNum_Object = MibTableColumn
ntwsApStatRadioStatusMacRadioNum = _NtwsApStatRadioStatusMacRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 3),
    _NtwsApStatRadioStatusMacRadioNum_Type()
)
ntwsApStatRadioStatusMacRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacRadioNum.setStatus("current")
_NtwsApStatRadioStatusMacEnable_Type = NtwsRadioEnable
_NtwsApStatRadioStatusMacEnable_Object = MibTableColumn
ntwsApStatRadioStatusMacEnable = _NtwsApStatRadioStatusMacEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 4),
    _NtwsApStatRadioStatusMacEnable_Type()
)
ntwsApStatRadioStatusMacEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacEnable.setStatus("obsolete")
_NtwsApStatRadioStatusMacRadioConfigState_Type = NtwsRadioConfigState
_NtwsApStatRadioStatusMacRadioConfigState_Object = MibTableColumn
ntwsApStatRadioStatusMacRadioConfigState = _NtwsApStatRadioStatusMacRadioConfigState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 5),
    _NtwsApStatRadioStatusMacRadioConfigState_Type()
)
ntwsApStatRadioStatusMacRadioConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacRadioConfigState.setStatus("current")
_NtwsApStatRadioStatusMacCurrentPowerLevel_Type = NtwsPowerLevel
_NtwsApStatRadioStatusMacCurrentPowerLevel_Object = MibTableColumn
ntwsApStatRadioStatusMacCurrentPowerLevel = _NtwsApStatRadioStatusMacCurrentPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 6),
    _NtwsApStatRadioStatusMacCurrentPowerLevel_Type()
)
ntwsApStatRadioStatusMacCurrentPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacCurrentPowerLevel.setStatus("current")
_NtwsApStatRadioStatusMacCurrentChannelNum_Type = NtwsChannelNum
_NtwsApStatRadioStatusMacCurrentChannelNum_Object = MibTableColumn
ntwsApStatRadioStatusMacCurrentChannelNum = _NtwsApStatRadioStatusMacCurrentChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 7),
    _NtwsApStatRadioStatusMacCurrentChannelNum_Type()
)
ntwsApStatRadioStatusMacCurrentChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacCurrentChannelNum.setStatus("current")
_NtwsApStatRadioStatusMacClientSessions_Type = Unsigned32
_NtwsApStatRadioStatusMacClientSessions_Object = MibTableColumn
ntwsApStatRadioStatusMacClientSessions = _NtwsApStatRadioStatusMacClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 8),
    _NtwsApStatRadioStatusMacClientSessions_Type()
)
ntwsApStatRadioStatusMacClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacClientSessions.setStatus("current")
_NtwsApStatRadioStatusMacMaxPowerLevel_Type = NtwsPowerLevel
_NtwsApStatRadioStatusMacMaxPowerLevel_Object = MibTableColumn
ntwsApStatRadioStatusMacMaxPowerLevel = _NtwsApStatRadioStatusMacMaxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 9),
    _NtwsApStatRadioStatusMacMaxPowerLevel_Type()
)
ntwsApStatRadioStatusMacMaxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacMaxPowerLevel.setStatus("current")
_NtwsApStatRadioStatusMacRadioPhyType_Type = NtwsRadioType
_NtwsApStatRadioStatusMacRadioPhyType_Object = MibTableColumn
ntwsApStatRadioStatusMacRadioPhyType = _NtwsApStatRadioStatusMacRadioPhyType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 10),
    _NtwsApStatRadioStatusMacRadioPhyType_Type()
)
ntwsApStatRadioStatusMacRadioPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacRadioPhyType.setStatus("current")
_NtwsApStatRadioStatusMacRadioMode_Type = NtwsRadioMode
_NtwsApStatRadioStatusMacRadioMode_Object = MibTableColumn
ntwsApStatRadioStatusMacRadioMode = _NtwsApStatRadioStatusMacRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 11),
    _NtwsApStatRadioStatusMacRadioMode_Type()
)
ntwsApStatRadioStatusMacRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacRadioMode.setStatus("current")
_NtwsApStatRadioStatusMacRadioChannelWidth_Type = NtwsRadioChannelWidth
_NtwsApStatRadioStatusMacRadioChannelWidth_Object = MibTableColumn
ntwsApStatRadioStatusMacRadioChannelWidth = _NtwsApStatRadioStatusMacRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 12),
    _NtwsApStatRadioStatusMacRadioChannelWidth_Type()
)
ntwsApStatRadioStatusMacRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacRadioChannelWidth.setStatus("current")
_NtwsApStatRadioStatusMacRadioMimoState_Type = NtwsRadioMimoState
_NtwsApStatRadioStatusMacRadioMimoState_Object = MibTableColumn
ntwsApStatRadioStatusMacRadioMimoState = _NtwsApStatRadioStatusMacRadioMimoState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 13),
    _NtwsApStatRadioStatusMacRadioMimoState_Type()
)
ntwsApStatRadioStatusMacRadioMimoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacRadioMimoState.setStatus("current")
_NtwsApStatRadioStatusMacMinPowerLevel_Type = NtwsPowerLevel
_NtwsApStatRadioStatusMacMinPowerLevel_Object = MibTableColumn
ntwsApStatRadioStatusMacMinPowerLevel = _NtwsApStatRadioStatusMacMinPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 5, 1, 14),
    _NtwsApStatRadioStatusMacMinPowerLevel_Type()
)
ntwsApStatRadioStatusMacMinPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioStatusMacMinPowerLevel.setStatus("current")
_NtwsApStatRadioServiceTable_Object = MibTable
ntwsApStatRadioServiceTable = _NtwsApStatRadioServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioServiceTable.setStatus("current")
_NtwsApStatRadioServiceEntry_Object = MibTableRow
ntwsApStatRadioServiceEntry = _NtwsApStatRadioServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 6, 1)
)
ntwsApStatRadioServiceEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioServApSerialNum"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioServRadioNum"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioServSsid"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioServiceEntry.setStatus("current")
_NtwsApStatRadioServApSerialNum_Type = NtwsApSerialNum
_NtwsApStatRadioServApSerialNum_Object = MibTableColumn
ntwsApStatRadioServApSerialNum = _NtwsApStatRadioServApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 6, 1, 1),
    _NtwsApStatRadioServApSerialNum_Type()
)
ntwsApStatRadioServApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioServApSerialNum.setStatus("current")
_NtwsApStatRadioServRadioNum_Type = NtwsRadioNum
_NtwsApStatRadioServRadioNum_Object = MibTableColumn
ntwsApStatRadioServRadioNum = _NtwsApStatRadioServRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 6, 1, 2),
    _NtwsApStatRadioServRadioNum_Type()
)
ntwsApStatRadioServRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioServRadioNum.setStatus("current")


class _NtwsApStatRadioServSsid_Type(DisplayString):
    """Custom type ntwsApStatRadioServSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsApStatRadioServSsid_Type.__name__ = "DisplayString"
_NtwsApStatRadioServSsid_Object = MibTableColumn
ntwsApStatRadioServSsid = _NtwsApStatRadioServSsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 6, 1, 3),
    _NtwsApStatRadioServSsid_Type()
)
ntwsApStatRadioServSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioServSsid.setStatus("current")
_NtwsApStatRadioServBssid_Type = MacAddress
_NtwsApStatRadioServBssid_Object = MibTableColumn
ntwsApStatRadioServBssid = _NtwsApStatRadioServBssid_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 6, 1, 4),
    _NtwsApStatRadioServBssid_Type()
)
ntwsApStatRadioServBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioServBssid.setStatus("current")
_NtwsApStatRadioServServiceProfileName_Type = DisplayString
_NtwsApStatRadioServServiceProfileName_Object = MibTableColumn
ntwsApStatRadioServServiceProfileName = _NtwsApStatRadioServServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 6, 1, 5),
    _NtwsApStatRadioServServiceProfileName_Type()
)
ntwsApStatRadioServServiceProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioServServiceProfileName.setStatus("current")
_NtwsApStatRadioServiceMacTable_Object = MibTable
ntwsApStatRadioServiceMacTable = _NtwsApStatRadioServiceMacTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioServiceMacTable.setStatus("current")
_NtwsApStatRadioServiceMacEntry_Object = MibTableRow
ntwsApStatRadioServiceMacEntry = _NtwsApStatRadioServiceMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 7, 1)
)
ntwsApStatRadioServiceMacEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioServMacBssid"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioServiceMacEntry.setStatus("current")
_NtwsApStatRadioServMacBssid_Type = MacAddress
_NtwsApStatRadioServMacBssid_Object = MibTableColumn
ntwsApStatRadioServMacBssid = _NtwsApStatRadioServMacBssid_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 7, 1, 1),
    _NtwsApStatRadioServMacBssid_Type()
)
ntwsApStatRadioServMacBssid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioServMacBssid.setStatus("current")
_NtwsApStatRadioServMacApSerialNum_Type = NtwsApSerialNum
_NtwsApStatRadioServMacApSerialNum_Object = MibTableColumn
ntwsApStatRadioServMacApSerialNum = _NtwsApStatRadioServMacApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 7, 1, 2),
    _NtwsApStatRadioServMacApSerialNum_Type()
)
ntwsApStatRadioServMacApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioServMacApSerialNum.setStatus("current")
_NtwsApStatRadioServMacRadioNum_Type = NtwsRadioNum
_NtwsApStatRadioServMacRadioNum_Object = MibTableColumn
ntwsApStatRadioServMacRadioNum = _NtwsApStatRadioServMacRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 7, 1, 3),
    _NtwsApStatRadioServMacRadioNum_Type()
)
ntwsApStatRadioServMacRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioServMacRadioNum.setStatus("current")


class _NtwsApStatRadioServMacSsid_Type(DisplayString):
    """Custom type ntwsApStatRadioServMacSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsApStatRadioServMacSsid_Type.__name__ = "DisplayString"
_NtwsApStatRadioServMacSsid_Object = MibTableColumn
ntwsApStatRadioServMacSsid = _NtwsApStatRadioServMacSsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 7, 1, 4),
    _NtwsApStatRadioServMacSsid_Type()
)
ntwsApStatRadioServMacSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioServMacSsid.setStatus("current")
_NtwsApStatRadioServMacServiceProfileName_Type = DisplayString
_NtwsApStatRadioServMacServiceProfileName_Object = MibTableColumn
ntwsApStatRadioServMacServiceProfileName = _NtwsApStatRadioServMacServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 7, 1, 5),
    _NtwsApStatRadioServMacServiceProfileName_Type()
)
ntwsApStatRadioServMacServiceProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioServMacServiceProfileName.setStatus("current")
_NtwsApStatRadioServiceOpRateSetTable_Object = MibTable
ntwsApStatRadioServiceOpRateSetTable = _NtwsApStatRadioServiceOpRateSetTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioServiceOpRateSetTable.setStatus("current")
_NtwsApStatRadioServiceOpRateSetEntry_Object = MibTableRow
ntwsApStatRadioServiceOpRateSetEntry = _NtwsApStatRadioServiceOpRateSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 8, 1)
)
ntwsApStatRadioServiceOpRateSetEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetApSerialNum"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetRadioNum"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetSsid"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioServiceOpRateSetEntry.setStatus("current")
_NtwsApStatRadioSORSetApSerialNum_Type = NtwsApSerialNum
_NtwsApStatRadioSORSetApSerialNum_Object = MibTableColumn
ntwsApStatRadioSORSetApSerialNum = _NtwsApStatRadioSORSetApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 8, 1, 1),
    _NtwsApStatRadioSORSetApSerialNum_Type()
)
ntwsApStatRadioSORSetApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetApSerialNum.setStatus("current")
_NtwsApStatRadioSORSetRadioNum_Type = NtwsRadioNum
_NtwsApStatRadioSORSetRadioNum_Object = MibTableColumn
ntwsApStatRadioSORSetRadioNum = _NtwsApStatRadioSORSetRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 8, 1, 2),
    _NtwsApStatRadioSORSetRadioNum_Type()
)
ntwsApStatRadioSORSetRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetRadioNum.setStatus("current")


class _NtwsApStatRadioSORSetSsid_Type(DisplayString):
    """Custom type ntwsApStatRadioSORSetSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsApStatRadioSORSetSsid_Type.__name__ = "DisplayString"
_NtwsApStatRadioSORSetSsid_Object = MibTableColumn
ntwsApStatRadioSORSetSsid = _NtwsApStatRadioSORSetSsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 8, 1, 3),
    _NtwsApStatRadioSORSetSsid_Type()
)
ntwsApStatRadioSORSetSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetSsid.setStatus("current")
_NtwsApStatRadioSORSetMandatory_Type = NtwsRadioOpRateSetMandatory
_NtwsApStatRadioSORSetMandatory_Object = MibTableColumn
ntwsApStatRadioSORSetMandatory = _NtwsApStatRadioSORSetMandatory_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 8, 1, 4),
    _NtwsApStatRadioSORSetMandatory_Type()
)
ntwsApStatRadioSORSetMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetMandatory.setStatus("current")
_NtwsApStatRadioSORSetDisabled_Type = NtwsRadioOpRateSetDisabled
_NtwsApStatRadioSORSetDisabled_Object = MibTableColumn
ntwsApStatRadioSORSetDisabled = _NtwsApStatRadioSORSetDisabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 8, 1, 5),
    _NtwsApStatRadioSORSetDisabled_Type()
)
ntwsApStatRadioSORSetDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetDisabled.setStatus("current")
_NtwsApStatRadioSORSetBeacon_Type = NtwsRadioOpRateSetSingleValue
_NtwsApStatRadioSORSetBeacon_Object = MibTableColumn
ntwsApStatRadioSORSetBeacon = _NtwsApStatRadioSORSetBeacon_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 8, 1, 6),
    _NtwsApStatRadioSORSetBeacon_Type()
)
ntwsApStatRadioSORSetBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetBeacon.setStatus("current")
_NtwsApStatRadioSORSetMulticast_Type = NtwsRadioOpRateSetSingleValue
_NtwsApStatRadioSORSetMulticast_Object = MibTableColumn
ntwsApStatRadioSORSetMulticast = _NtwsApStatRadioSORSetMulticast_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 8, 1, 7),
    _NtwsApStatRadioSORSetMulticast_Type()
)
ntwsApStatRadioSORSetMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetMulticast.setStatus("current")
_NtwsApStatRadioServiceOpRateSetMacTable_Object = MibTable
ntwsApStatRadioServiceOpRateSetMacTable = _NtwsApStatRadioServiceOpRateSetMacTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioServiceOpRateSetMacTable.setStatus("current")
_NtwsApStatRadioServiceOpRateSetMacEntry_Object = MibTableRow
ntwsApStatRadioServiceOpRateSetMacEntry = _NtwsApStatRadioServiceOpRateSetMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 9, 1)
)
ntwsApStatRadioServiceOpRateSetMacEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetMacBssid"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioServiceOpRateSetMacEntry.setStatus("current")
_NtwsApStatRadioSORSetMacBssid_Type = MacAddress
_NtwsApStatRadioSORSetMacBssid_Object = MibTableColumn
ntwsApStatRadioSORSetMacBssid = _NtwsApStatRadioSORSetMacBssid_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 9, 1, 1),
    _NtwsApStatRadioSORSetMacBssid_Type()
)
ntwsApStatRadioSORSetMacBssid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetMacBssid.setStatus("current")
_NtwsApStatRadioSORSetMacMandatory_Type = NtwsRadioOpRateSetMandatory
_NtwsApStatRadioSORSetMacMandatory_Object = MibTableColumn
ntwsApStatRadioSORSetMacMandatory = _NtwsApStatRadioSORSetMacMandatory_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 9, 1, 2),
    _NtwsApStatRadioSORSetMacMandatory_Type()
)
ntwsApStatRadioSORSetMacMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetMacMandatory.setStatus("current")
_NtwsApStatRadioSORSetMacDisabled_Type = NtwsRadioOpRateSetDisabled
_NtwsApStatRadioSORSetMacDisabled_Object = MibTableColumn
ntwsApStatRadioSORSetMacDisabled = _NtwsApStatRadioSORSetMacDisabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 9, 1, 3),
    _NtwsApStatRadioSORSetMacDisabled_Type()
)
ntwsApStatRadioSORSetMacDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetMacDisabled.setStatus("current")
_NtwsApStatRadioSORSetMacBeacon_Type = NtwsRadioOpRateSetSingleValue
_NtwsApStatRadioSORSetMacBeacon_Object = MibTableColumn
ntwsApStatRadioSORSetMacBeacon = _NtwsApStatRadioSORSetMacBeacon_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 9, 1, 4),
    _NtwsApStatRadioSORSetMacBeacon_Type()
)
ntwsApStatRadioSORSetMacBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetMacBeacon.setStatus("current")
_NtwsApStatRadioSORSetMacMulticast_Type = NtwsRadioOpRateSetSingleValue
_NtwsApStatRadioSORSetMacMulticast_Object = MibTableColumn
ntwsApStatRadioSORSetMacMulticast = _NtwsApStatRadioSORSetMacMulticast_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 9, 1, 5),
    _NtwsApStatRadioSORSetMacMulticast_Type()
)
ntwsApStatRadioSORSetMacMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioSORSetMacMulticast.setStatus("current")
_NtwsApStatRadioOpStatisticsTable_Object = MibTable
ntwsApStatRadioOpStatisticsTable = _NtwsApStatRadioOpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatisticsTable.setStatus("current")
_NtwsApStatRadioOpStatisticsEntry_Object = MibTableRow
ntwsApStatRadioOpStatisticsEntry = _NtwsApStatRadioOpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1)
)
ntwsApStatRadioOpStatisticsEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsApSerialNum"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsRadioNum"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatisticsEntry.setStatus("current")
_NtwsApStatRadioOpStatsApSerialNum_Type = NtwsApSerialNum
_NtwsApStatRadioOpStatsApSerialNum_Object = MibTableColumn
ntwsApStatRadioOpStatsApSerialNum = _NtwsApStatRadioOpStatsApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 1),
    _NtwsApStatRadioOpStatsApSerialNum_Type()
)
ntwsApStatRadioOpStatsApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsApSerialNum.setStatus("current")
_NtwsApStatRadioOpStatsRadioNum_Type = NtwsRadioNum
_NtwsApStatRadioOpStatsRadioNum_Object = MibTableColumn
ntwsApStatRadioOpStatsRadioNum = _NtwsApStatRadioOpStatsRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 2),
    _NtwsApStatRadioOpStatsRadioNum_Type()
)
ntwsApStatRadioOpStatsRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsRadioNum.setStatus("current")
_NtwsApStatRadioOpStatsTxUniPkt_Type = Counter64
_NtwsApStatRadioOpStatsTxUniPkt_Object = MibTableColumn
ntwsApStatRadioOpStatsTxUniPkt = _NtwsApStatRadioOpStatsTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 3),
    _NtwsApStatRadioOpStatsTxUniPkt_Type()
)
ntwsApStatRadioOpStatsTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsTxUniPkt.setStatus("current")
_NtwsApStatRadioOpStatsTxUniOctet_Type = Counter64
_NtwsApStatRadioOpStatsTxUniOctet_Object = MibTableColumn
ntwsApStatRadioOpStatsTxUniOctet = _NtwsApStatRadioOpStatsTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 4),
    _NtwsApStatRadioOpStatsTxUniOctet_Type()
)
ntwsApStatRadioOpStatsTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsTxUniOctet.setStatus("current")
_NtwsApStatRadioOpStatsTxMultiPkt_Type = Counter64
_NtwsApStatRadioOpStatsTxMultiPkt_Object = MibTableColumn
ntwsApStatRadioOpStatsTxMultiPkt = _NtwsApStatRadioOpStatsTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 5),
    _NtwsApStatRadioOpStatsTxMultiPkt_Type()
)
ntwsApStatRadioOpStatsTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsTxMultiPkt.setStatus("current")
_NtwsApStatRadioOpStatsTxMultiOctet_Type = Counter64
_NtwsApStatRadioOpStatsTxMultiOctet_Object = MibTableColumn
ntwsApStatRadioOpStatsTxMultiOctet = _NtwsApStatRadioOpStatsTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 6),
    _NtwsApStatRadioOpStatsTxMultiOctet_Type()
)
ntwsApStatRadioOpStatsTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsTxMultiOctet.setStatus("current")
_NtwsApStatRadioOpStatsRxPkt_Type = Counter64
_NtwsApStatRadioOpStatsRxPkt_Object = MibTableColumn
ntwsApStatRadioOpStatsRxPkt = _NtwsApStatRadioOpStatsRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 7),
    _NtwsApStatRadioOpStatsRxPkt_Type()
)
ntwsApStatRadioOpStatsRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsRxPkt.setStatus("current")
_NtwsApStatRadioOpStatsRxOctet_Type = Counter64
_NtwsApStatRadioOpStatsRxOctet_Object = MibTableColumn
ntwsApStatRadioOpStatsRxOctet = _NtwsApStatRadioOpStatsRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 8),
    _NtwsApStatRadioOpStatsRxOctet_Type()
)
ntwsApStatRadioOpStatsRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsRxOctet.setStatus("current")
_NtwsApStatRadioOpStatsUndcrptPkt_Type = Counter64
_NtwsApStatRadioOpStatsUndcrptPkt_Object = MibTableColumn
ntwsApStatRadioOpStatsUndcrptPkt = _NtwsApStatRadioOpStatsUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 9),
    _NtwsApStatRadioOpStatsUndcrptPkt_Type()
)
ntwsApStatRadioOpStatsUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsUndcrptPkt.setStatus("current")
_NtwsApStatRadioOpStatsUndcrptOctet_Type = Counter64
_NtwsApStatRadioOpStatsUndcrptOctet_Object = MibTableColumn
ntwsApStatRadioOpStatsUndcrptOctet = _NtwsApStatRadioOpStatsUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 10),
    _NtwsApStatRadioOpStatsUndcrptOctet_Type()
)
ntwsApStatRadioOpStatsUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsUndcrptOctet.setStatus("current")
_NtwsApStatRadioOpStatsPhyErr_Type = Counter64
_NtwsApStatRadioOpStatsPhyErr_Object = MibTableColumn
ntwsApStatRadioOpStatsPhyErr = _NtwsApStatRadioOpStatsPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 11),
    _NtwsApStatRadioOpStatsPhyErr_Type()
)
ntwsApStatRadioOpStatsPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsPhyErr.setStatus("current")
_NtwsApStatRadioOpStatsResetCount_Type = Counter32
_NtwsApStatRadioOpStatsResetCount_Object = MibTableColumn
ntwsApStatRadioOpStatsResetCount = _NtwsApStatRadioOpStatsResetCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 12),
    _NtwsApStatRadioOpStatsResetCount_Type()
)
ntwsApStatRadioOpStatsResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsResetCount.setStatus("current")
_NtwsApStatRadioOpStatsAutoTuneChannelChangeCount_Type = Counter32
_NtwsApStatRadioOpStatsAutoTuneChannelChangeCount_Object = MibTableColumn
ntwsApStatRadioOpStatsAutoTuneChannelChangeCount = _NtwsApStatRadioOpStatsAutoTuneChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 13),
    _NtwsApStatRadioOpStatsAutoTuneChannelChangeCount_Type()
)
ntwsApStatRadioOpStatsAutoTuneChannelChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsAutoTuneChannelChangeCount.setStatus("current")
_NtwsApStatRadioOpStatsTxRetriesCount_Type = Counter32
_NtwsApStatRadioOpStatsTxRetriesCount_Object = MibTableColumn
ntwsApStatRadioOpStatsTxRetriesCount = _NtwsApStatRadioOpStatsTxRetriesCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 14),
    _NtwsApStatRadioOpStatsTxRetriesCount_Type()
)
ntwsApStatRadioOpStatsTxRetriesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsTxRetriesCount.setStatus("current")
_NtwsApStatRadioOpStatsUserSessions_Type = Gauge32
_NtwsApStatRadioOpStatsUserSessions_Object = MibTableColumn
ntwsApStatRadioOpStatsUserSessions = _NtwsApStatRadioOpStatsUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 15),
    _NtwsApStatRadioOpStatsUserSessions_Type()
)
ntwsApStatRadioOpStatsUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsUserSessions.setStatus("current")
_NtwsApStatRadioOpStatsNoiseFloor_Type = Integer32
_NtwsApStatRadioOpStatsNoiseFloor_Object = MibTableColumn
ntwsApStatRadioOpStatsNoiseFloor = _NtwsApStatRadioOpStatsNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 16),
    _NtwsApStatRadioOpStatsNoiseFloor_Type()
)
ntwsApStatRadioOpStatsNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsNoiseFloor.setStatus("current")
_NtwsApStatRadioOpStatsClientAssociations_Type = Counter32
_NtwsApStatRadioOpStatsClientAssociations_Object = MibTableColumn
ntwsApStatRadioOpStatsClientAssociations = _NtwsApStatRadioOpStatsClientAssociations_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 17),
    _NtwsApStatRadioOpStatsClientAssociations_Type()
)
ntwsApStatRadioOpStatsClientAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsClientAssociations.setStatus("current")
_NtwsApStatRadioOpStatsClientFailedAssociations_Type = Counter32
_NtwsApStatRadioOpStatsClientFailedAssociations_Object = MibTableColumn
ntwsApStatRadioOpStatsClientFailedAssociations = _NtwsApStatRadioOpStatsClientFailedAssociations_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 18),
    _NtwsApStatRadioOpStatsClientFailedAssociations_Type()
)
ntwsApStatRadioOpStatsClientFailedAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsClientFailedAssociations.setStatus("current")
_NtwsApStatRadioOpStatsClientReAssociations_Type = Counter32
_NtwsApStatRadioOpStatsClientReAssociations_Object = MibTableColumn
ntwsApStatRadioOpStatsClientReAssociations = _NtwsApStatRadioOpStatsClientReAssociations_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 19),
    _NtwsApStatRadioOpStatsClientReAssociations_Type()
)
ntwsApStatRadioOpStatsClientReAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsClientReAssociations.setStatus("current")
_NtwsApStatRadioOpStatsSignalingPkt_Type = Counter64
_NtwsApStatRadioOpStatsSignalingPkt_Object = MibTableColumn
ntwsApStatRadioOpStatsSignalingPkt = _NtwsApStatRadioOpStatsSignalingPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 20),
    _NtwsApStatRadioOpStatsSignalingPkt_Type()
)
ntwsApStatRadioOpStatsSignalingPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsSignalingPkt.setStatus("current")
_NtwsApStatRadioOpStatsReTransmitOctet_Type = Counter64
_NtwsApStatRadioOpStatsReTransmitOctet_Object = MibTableColumn
ntwsApStatRadioOpStatsReTransmitOctet = _NtwsApStatRadioOpStatsReTransmitOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 21),
    _NtwsApStatRadioOpStatsReTransmitOctet_Type()
)
ntwsApStatRadioOpStatsReTransmitOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsReTransmitOctet.setStatus("current")
_NtwsApStatRadioOpStatsRefusedConnectionCount_Type = Counter32
_NtwsApStatRadioOpStatsRefusedConnectionCount_Object = MibTableColumn
ntwsApStatRadioOpStatsRefusedConnectionCount = _NtwsApStatRadioOpStatsRefusedConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 10, 1, 22),
    _NtwsApStatRadioOpStatsRefusedConnectionCount_Type()
)
ntwsApStatRadioOpStatsRefusedConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsRefusedConnectionCount.setStatus("current")
_NtwsApStatRadioOpStatisticsMacTable_Object = MibTable
ntwsApStatRadioOpStatisticsMacTable = _NtwsApStatRadioOpStatisticsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatisticsMacTable.setStatus("current")
_NtwsApStatRadioOpStatisticsMacEntry_Object = MibTableRow
ntwsApStatRadioOpStatisticsMacEntry = _NtwsApStatRadioOpStatisticsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1)
)
ntwsApStatRadioOpStatisticsMacEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacBaseMac"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatisticsMacEntry.setStatus("current")
_NtwsApStatRadioOpStatsMacBaseMac_Type = MacAddress
_NtwsApStatRadioOpStatsMacBaseMac_Object = MibTableColumn
ntwsApStatRadioOpStatsMacBaseMac = _NtwsApStatRadioOpStatsMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 1),
    _NtwsApStatRadioOpStatsMacBaseMac_Type()
)
ntwsApStatRadioOpStatsMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacBaseMac.setStatus("current")
_NtwsApStatRadioOpStatsMacTxUniPkt_Type = Counter64
_NtwsApStatRadioOpStatsMacTxUniPkt_Object = MibTableColumn
ntwsApStatRadioOpStatsMacTxUniPkt = _NtwsApStatRadioOpStatsMacTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 2),
    _NtwsApStatRadioOpStatsMacTxUniPkt_Type()
)
ntwsApStatRadioOpStatsMacTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacTxUniPkt.setStatus("current")
_NtwsApStatRadioOpStatsMacTxUniOctet_Type = Counter64
_NtwsApStatRadioOpStatsMacTxUniOctet_Object = MibTableColumn
ntwsApStatRadioOpStatsMacTxUniOctet = _NtwsApStatRadioOpStatsMacTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 3),
    _NtwsApStatRadioOpStatsMacTxUniOctet_Type()
)
ntwsApStatRadioOpStatsMacTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacTxUniOctet.setStatus("current")
_NtwsApStatRadioOpStatsMacTxMultiPkt_Type = Counter64
_NtwsApStatRadioOpStatsMacTxMultiPkt_Object = MibTableColumn
ntwsApStatRadioOpStatsMacTxMultiPkt = _NtwsApStatRadioOpStatsMacTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 4),
    _NtwsApStatRadioOpStatsMacTxMultiPkt_Type()
)
ntwsApStatRadioOpStatsMacTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacTxMultiPkt.setStatus("current")
_NtwsApStatRadioOpStatsMacTxMultiOctet_Type = Counter64
_NtwsApStatRadioOpStatsMacTxMultiOctet_Object = MibTableColumn
ntwsApStatRadioOpStatsMacTxMultiOctet = _NtwsApStatRadioOpStatsMacTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 5),
    _NtwsApStatRadioOpStatsMacTxMultiOctet_Type()
)
ntwsApStatRadioOpStatsMacTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacTxMultiOctet.setStatus("current")
_NtwsApStatRadioOpStatsMacRxPkt_Type = Counter64
_NtwsApStatRadioOpStatsMacRxPkt_Object = MibTableColumn
ntwsApStatRadioOpStatsMacRxPkt = _NtwsApStatRadioOpStatsMacRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 6),
    _NtwsApStatRadioOpStatsMacRxPkt_Type()
)
ntwsApStatRadioOpStatsMacRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacRxPkt.setStatus("current")
_NtwsApStatRadioOpStatsMacRxOctet_Type = Counter64
_NtwsApStatRadioOpStatsMacRxOctet_Object = MibTableColumn
ntwsApStatRadioOpStatsMacRxOctet = _NtwsApStatRadioOpStatsMacRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 7),
    _NtwsApStatRadioOpStatsMacRxOctet_Type()
)
ntwsApStatRadioOpStatsMacRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacRxOctet.setStatus("current")
_NtwsApStatRadioOpStatsMacUndcrptPkt_Type = Counter64
_NtwsApStatRadioOpStatsMacUndcrptPkt_Object = MibTableColumn
ntwsApStatRadioOpStatsMacUndcrptPkt = _NtwsApStatRadioOpStatsMacUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 8),
    _NtwsApStatRadioOpStatsMacUndcrptPkt_Type()
)
ntwsApStatRadioOpStatsMacUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacUndcrptPkt.setStatus("current")
_NtwsApStatRadioOpStatsMacUndcrptOctet_Type = Counter64
_NtwsApStatRadioOpStatsMacUndcrptOctet_Object = MibTableColumn
ntwsApStatRadioOpStatsMacUndcrptOctet = _NtwsApStatRadioOpStatsMacUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 9),
    _NtwsApStatRadioOpStatsMacUndcrptOctet_Type()
)
ntwsApStatRadioOpStatsMacUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacUndcrptOctet.setStatus("current")
_NtwsApStatRadioOpStatsMacPhyErr_Type = Counter64
_NtwsApStatRadioOpStatsMacPhyErr_Object = MibTableColumn
ntwsApStatRadioOpStatsMacPhyErr = _NtwsApStatRadioOpStatsMacPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 10),
    _NtwsApStatRadioOpStatsMacPhyErr_Type()
)
ntwsApStatRadioOpStatsMacPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacPhyErr.setStatus("current")
_NtwsApStatRadioOpStatsMacResetCount_Type = Counter32
_NtwsApStatRadioOpStatsMacResetCount_Object = MibTableColumn
ntwsApStatRadioOpStatsMacResetCount = _NtwsApStatRadioOpStatsMacResetCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 11),
    _NtwsApStatRadioOpStatsMacResetCount_Type()
)
ntwsApStatRadioOpStatsMacResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacResetCount.setStatus("current")
_NtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount_Type = Counter32
_NtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount_Object = MibTableColumn
ntwsApStatRadioOpStatsMacAutoTuneChannelChangeCount = _NtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 12),
    _NtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount_Type()
)
ntwsApStatRadioOpStatsMacAutoTuneChannelChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacAutoTuneChannelChangeCount.setStatus("current")
_NtwsApStatRadioOpStatsMacTxRetriesCount_Type = Counter32
_NtwsApStatRadioOpStatsMacTxRetriesCount_Object = MibTableColumn
ntwsApStatRadioOpStatsMacTxRetriesCount = _NtwsApStatRadioOpStatsMacTxRetriesCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 13),
    _NtwsApStatRadioOpStatsMacTxRetriesCount_Type()
)
ntwsApStatRadioOpStatsMacTxRetriesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacTxRetriesCount.setStatus("current")
_NtwsApStatRadioOpStatsMacUserSessions_Type = Gauge32
_NtwsApStatRadioOpStatsMacUserSessions_Object = MibTableColumn
ntwsApStatRadioOpStatsMacUserSessions = _NtwsApStatRadioOpStatsMacUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 14),
    _NtwsApStatRadioOpStatsMacUserSessions_Type()
)
ntwsApStatRadioOpStatsMacUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacUserSessions.setStatus("current")
_NtwsApStatRadioOpStatsMacNoiseFloor_Type = Integer32
_NtwsApStatRadioOpStatsMacNoiseFloor_Object = MibTableColumn
ntwsApStatRadioOpStatsMacNoiseFloor = _NtwsApStatRadioOpStatsMacNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 15),
    _NtwsApStatRadioOpStatsMacNoiseFloor_Type()
)
ntwsApStatRadioOpStatsMacNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacNoiseFloor.setStatus("current")
_NtwsApStatRadioOpStatsMacClientAssociations_Type = Counter32
_NtwsApStatRadioOpStatsMacClientAssociations_Object = MibTableColumn
ntwsApStatRadioOpStatsMacClientAssociations = _NtwsApStatRadioOpStatsMacClientAssociations_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 16),
    _NtwsApStatRadioOpStatsMacClientAssociations_Type()
)
ntwsApStatRadioOpStatsMacClientAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacClientAssociations.setStatus("current")
_NtwsApStatRadioOpStatsMacClientFailedAssociations_Type = Counter32
_NtwsApStatRadioOpStatsMacClientFailedAssociations_Object = MibTableColumn
ntwsApStatRadioOpStatsMacClientFailedAssociations = _NtwsApStatRadioOpStatsMacClientFailedAssociations_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 17),
    _NtwsApStatRadioOpStatsMacClientFailedAssociations_Type()
)
ntwsApStatRadioOpStatsMacClientFailedAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacClientFailedAssociations.setStatus("current")
_NtwsApStatRadioOpStatsMacClientReAssociations_Type = Counter32
_NtwsApStatRadioOpStatsMacClientReAssociations_Object = MibTableColumn
ntwsApStatRadioOpStatsMacClientReAssociations = _NtwsApStatRadioOpStatsMacClientReAssociations_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 18),
    _NtwsApStatRadioOpStatsMacClientReAssociations_Type()
)
ntwsApStatRadioOpStatsMacClientReAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacClientReAssociations.setStatus("current")
_NtwsApStatRadioOpStatsMacSignalingPkt_Type = Counter64
_NtwsApStatRadioOpStatsMacSignalingPkt_Object = MibTableColumn
ntwsApStatRadioOpStatsMacSignalingPkt = _NtwsApStatRadioOpStatsMacSignalingPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 19),
    _NtwsApStatRadioOpStatsMacSignalingPkt_Type()
)
ntwsApStatRadioOpStatsMacSignalingPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacSignalingPkt.setStatus("current")
_NtwsApStatRadioOpStatsMacReTransmitOctet_Type = Counter64
_NtwsApStatRadioOpStatsMacReTransmitOctet_Object = MibTableColumn
ntwsApStatRadioOpStatsMacReTransmitOctet = _NtwsApStatRadioOpStatsMacReTransmitOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 20),
    _NtwsApStatRadioOpStatsMacReTransmitOctet_Type()
)
ntwsApStatRadioOpStatsMacReTransmitOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacReTransmitOctet.setStatus("current")
_NtwsApStatRadioOpStatsMacRefusedConnectionCount_Type = Counter32
_NtwsApStatRadioOpStatsMacRefusedConnectionCount_Object = MibTableColumn
ntwsApStatRadioOpStatsMacRefusedConnectionCount = _NtwsApStatRadioOpStatsMacRefusedConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 11, 1, 21),
    _NtwsApStatRadioOpStatsMacRefusedConnectionCount_Type()
)
ntwsApStatRadioOpStatsMacRefusedConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioOpStatsMacRefusedConnectionCount.setStatus("current")
_NtwsApStatRadioRateOpStatisticsTable_Object = MibTable
ntwsApStatRadioRateOpStatisticsTable = _NtwsApStatRadioRateOpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatisticsTable.setStatus("current")
_NtwsApStatRadioRateOpStatisticsEntry_Object = MibTableRow
ntwsApStatRadioRateOpStatisticsEntry = _NtwsApStatRadioRateOpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1)
)
ntwsApStatRadioRateOpStatisticsEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsApSerialNum"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsRadioNum"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsRate"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatisticsEntry.setStatus("current")
_NtwsApStatRadioRateOpStatsApSerialNum_Type = NtwsApSerialNum
_NtwsApStatRadioRateOpStatsApSerialNum_Object = MibTableColumn
ntwsApStatRadioRateOpStatsApSerialNum = _NtwsApStatRadioRateOpStatsApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 1),
    _NtwsApStatRadioRateOpStatsApSerialNum_Type()
)
ntwsApStatRadioRateOpStatsApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsApSerialNum.setStatus("current")
_NtwsApStatRadioRateOpStatsRadioNum_Type = NtwsRadioNum
_NtwsApStatRadioRateOpStatsRadioNum_Object = MibTableColumn
ntwsApStatRadioRateOpStatsRadioNum = _NtwsApStatRadioRateOpStatsRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 2),
    _NtwsApStatRadioRateOpStatsRadioNum_Type()
)
ntwsApStatRadioRateOpStatsRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsRadioNum.setStatus("current")
_NtwsApStatRadioRateOpStatsRate_Type = NtwsRadioRate
_NtwsApStatRadioRateOpStatsRate_Object = MibTableColumn
ntwsApStatRadioRateOpStatsRate = _NtwsApStatRadioRateOpStatsRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 3),
    _NtwsApStatRadioRateOpStatsRate_Type()
)
ntwsApStatRadioRateOpStatsRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsRate.setStatus("current")
_NtwsApStatRadioRateOpStatsTxUniPkt_Type = Counter64
_NtwsApStatRadioRateOpStatsTxUniPkt_Object = MibTableColumn
ntwsApStatRadioRateOpStatsTxUniPkt = _NtwsApStatRadioRateOpStatsTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 4),
    _NtwsApStatRadioRateOpStatsTxUniPkt_Type()
)
ntwsApStatRadioRateOpStatsTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsTxUniPkt.setStatus("current")
_NtwsApStatRadioRateOpStatsTxUniOctet_Type = Counter64
_NtwsApStatRadioRateOpStatsTxUniOctet_Object = MibTableColumn
ntwsApStatRadioRateOpStatsTxUniOctet = _NtwsApStatRadioRateOpStatsTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 5),
    _NtwsApStatRadioRateOpStatsTxUniOctet_Type()
)
ntwsApStatRadioRateOpStatsTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsTxUniOctet.setStatus("current")
_NtwsApStatRadioRateOpStatsTxMultiPkt_Type = Counter64
_NtwsApStatRadioRateOpStatsTxMultiPkt_Object = MibTableColumn
ntwsApStatRadioRateOpStatsTxMultiPkt = _NtwsApStatRadioRateOpStatsTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 6),
    _NtwsApStatRadioRateOpStatsTxMultiPkt_Type()
)
ntwsApStatRadioRateOpStatsTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsTxMultiPkt.setStatus("current")
_NtwsApStatRadioRateOpStatsTxMultiOctet_Type = Counter64
_NtwsApStatRadioRateOpStatsTxMultiOctet_Object = MibTableColumn
ntwsApStatRadioRateOpStatsTxMultiOctet = _NtwsApStatRadioRateOpStatsTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 7),
    _NtwsApStatRadioRateOpStatsTxMultiOctet_Type()
)
ntwsApStatRadioRateOpStatsTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsTxMultiOctet.setStatus("current")
_NtwsApStatRadioRateOpStatsRxPkt_Type = Counter64
_NtwsApStatRadioRateOpStatsRxPkt_Object = MibTableColumn
ntwsApStatRadioRateOpStatsRxPkt = _NtwsApStatRadioRateOpStatsRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 8),
    _NtwsApStatRadioRateOpStatsRxPkt_Type()
)
ntwsApStatRadioRateOpStatsRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsRxPkt.setStatus("current")
_NtwsApStatRadioRateOpStatsRxOctet_Type = Counter64
_NtwsApStatRadioRateOpStatsRxOctet_Object = MibTableColumn
ntwsApStatRadioRateOpStatsRxOctet = _NtwsApStatRadioRateOpStatsRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 9),
    _NtwsApStatRadioRateOpStatsRxOctet_Type()
)
ntwsApStatRadioRateOpStatsRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsRxOctet.setStatus("current")
_NtwsApStatRadioRateOpStatsUndcrptPkt_Type = Counter64
_NtwsApStatRadioRateOpStatsUndcrptPkt_Object = MibTableColumn
ntwsApStatRadioRateOpStatsUndcrptPkt = _NtwsApStatRadioRateOpStatsUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 10),
    _NtwsApStatRadioRateOpStatsUndcrptPkt_Type()
)
ntwsApStatRadioRateOpStatsUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsUndcrptPkt.setStatus("current")
_NtwsApStatRadioRateOpStatsUndcrptOctet_Type = Counter64
_NtwsApStatRadioRateOpStatsUndcrptOctet_Object = MibTableColumn
ntwsApStatRadioRateOpStatsUndcrptOctet = _NtwsApStatRadioRateOpStatsUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 11),
    _NtwsApStatRadioRateOpStatsUndcrptOctet_Type()
)
ntwsApStatRadioRateOpStatsUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsUndcrptOctet.setStatus("current")
_NtwsApStatRadioRateOpStatsPhyErr_Type = Counter64
_NtwsApStatRadioRateOpStatsPhyErr_Object = MibTableColumn
ntwsApStatRadioRateOpStatsPhyErr = _NtwsApStatRadioRateOpStatsPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 12, 1, 12),
    _NtwsApStatRadioRateOpStatsPhyErr_Type()
)
ntwsApStatRadioRateOpStatsPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsPhyErr.setStatus("current")
_NtwsApStatRadioRateOpStatisticsMacTable_Object = MibTable
ntwsApStatRadioRateOpStatisticsMacTable = _NtwsApStatRadioRateOpStatisticsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatisticsMacTable.setStatus("current")
_NtwsApStatRadioRateOpStatisticsMacEntry_Object = MibTableRow
ntwsApStatRadioRateOpStatisticsMacEntry = _NtwsApStatRadioRateOpStatisticsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1)
)
ntwsApStatRadioRateOpStatisticsMacEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacBaseMac"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacRate"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatisticsMacEntry.setStatus("current")
_NtwsApStatRadioRateOpStatsMacBaseMac_Type = MacAddress
_NtwsApStatRadioRateOpStatsMacBaseMac_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacBaseMac = _NtwsApStatRadioRateOpStatsMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 1),
    _NtwsApStatRadioRateOpStatsMacBaseMac_Type()
)
ntwsApStatRadioRateOpStatsMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacBaseMac.setStatus("current")
_NtwsApStatRadioRateOpStatsMacRate_Type = NtwsRadioRate
_NtwsApStatRadioRateOpStatsMacRate_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacRate = _NtwsApStatRadioRateOpStatsMacRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 2),
    _NtwsApStatRadioRateOpStatsMacRate_Type()
)
ntwsApStatRadioRateOpStatsMacRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacRate.setStatus("current")
_NtwsApStatRadioRateOpStatsMacTxUniPkt_Type = Counter64
_NtwsApStatRadioRateOpStatsMacTxUniPkt_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacTxUniPkt = _NtwsApStatRadioRateOpStatsMacTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 3),
    _NtwsApStatRadioRateOpStatsMacTxUniPkt_Type()
)
ntwsApStatRadioRateOpStatsMacTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacTxUniPkt.setStatus("current")
_NtwsApStatRadioRateOpStatsMacTxUniOctet_Type = Counter64
_NtwsApStatRadioRateOpStatsMacTxUniOctet_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacTxUniOctet = _NtwsApStatRadioRateOpStatsMacTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 4),
    _NtwsApStatRadioRateOpStatsMacTxUniOctet_Type()
)
ntwsApStatRadioRateOpStatsMacTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacTxUniOctet.setStatus("current")
_NtwsApStatRadioRateOpStatsMacTxMultiPkt_Type = Counter64
_NtwsApStatRadioRateOpStatsMacTxMultiPkt_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacTxMultiPkt = _NtwsApStatRadioRateOpStatsMacTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 5),
    _NtwsApStatRadioRateOpStatsMacTxMultiPkt_Type()
)
ntwsApStatRadioRateOpStatsMacTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacTxMultiPkt.setStatus("current")
_NtwsApStatRadioRateOpStatsMacTxMultiOctet_Type = Counter64
_NtwsApStatRadioRateOpStatsMacTxMultiOctet_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacTxMultiOctet = _NtwsApStatRadioRateOpStatsMacTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 6),
    _NtwsApStatRadioRateOpStatsMacTxMultiOctet_Type()
)
ntwsApStatRadioRateOpStatsMacTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacTxMultiOctet.setStatus("current")
_NtwsApStatRadioRateOpStatsMacRxPkt_Type = Counter64
_NtwsApStatRadioRateOpStatsMacRxPkt_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacRxPkt = _NtwsApStatRadioRateOpStatsMacRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 7),
    _NtwsApStatRadioRateOpStatsMacRxPkt_Type()
)
ntwsApStatRadioRateOpStatsMacRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacRxPkt.setStatus("current")
_NtwsApStatRadioRateOpStatsMacRxOctet_Type = Counter64
_NtwsApStatRadioRateOpStatsMacRxOctet_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacRxOctet = _NtwsApStatRadioRateOpStatsMacRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 8),
    _NtwsApStatRadioRateOpStatsMacRxOctet_Type()
)
ntwsApStatRadioRateOpStatsMacRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacRxOctet.setStatus("current")
_NtwsApStatRadioRateOpStatsMacUndcrptPkt_Type = Counter64
_NtwsApStatRadioRateOpStatsMacUndcrptPkt_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacUndcrptPkt = _NtwsApStatRadioRateOpStatsMacUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 9),
    _NtwsApStatRadioRateOpStatsMacUndcrptPkt_Type()
)
ntwsApStatRadioRateOpStatsMacUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacUndcrptPkt.setStatus("current")
_NtwsApStatRadioRateOpStatsMacUndcrptOctet_Type = Counter64
_NtwsApStatRadioRateOpStatsMacUndcrptOctet_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacUndcrptOctet = _NtwsApStatRadioRateOpStatsMacUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 10),
    _NtwsApStatRadioRateOpStatsMacUndcrptOctet_Type()
)
ntwsApStatRadioRateOpStatsMacUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacUndcrptOctet.setStatus("current")
_NtwsApStatRadioRateOpStatsMacPhyErr_Type = Counter64
_NtwsApStatRadioRateOpStatsMacPhyErr_Object = MibTableColumn
ntwsApStatRadioRateOpStatsMacPhyErr = _NtwsApStatRadioRateOpStatsMacPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 13, 1, 11),
    _NtwsApStatRadioRateOpStatsMacPhyErr_Type()
)
ntwsApStatRadioRateOpStatsMacPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateOpStatsMacPhyErr.setStatus("current")
_NtwsApStatRadioRateExOpStatisticsTable_Object = MibTable
ntwsApStatRadioRateExOpStatisticsTable = _NtwsApStatRadioRateExOpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatisticsTable.setStatus("current")
_NtwsApStatRadioRateExOpStatisticsEntry_Object = MibTableRow
ntwsApStatRadioRateExOpStatisticsEntry = _NtwsApStatRadioRateExOpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1)
)
ntwsApStatRadioRateExOpStatisticsEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsApSerialNum"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsRadioNum"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsRateEx"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatisticsEntry.setStatus("current")
_NtwsApStatRadioRateExOpStatsApSerialNum_Type = NtwsApSerialNum
_NtwsApStatRadioRateExOpStatsApSerialNum_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsApSerialNum = _NtwsApStatRadioRateExOpStatsApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 1),
    _NtwsApStatRadioRateExOpStatsApSerialNum_Type()
)
ntwsApStatRadioRateExOpStatsApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsApSerialNum.setStatus("current")
_NtwsApStatRadioRateExOpStatsRadioNum_Type = NtwsRadioNum
_NtwsApStatRadioRateExOpStatsRadioNum_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsRadioNum = _NtwsApStatRadioRateExOpStatsRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 2),
    _NtwsApStatRadioRateExOpStatsRadioNum_Type()
)
ntwsApStatRadioRateExOpStatsRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsRadioNum.setStatus("current")
_NtwsApStatRadioRateExOpStatsRateEx_Type = NtwsRadioRateEx
_NtwsApStatRadioRateExOpStatsRateEx_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsRateEx = _NtwsApStatRadioRateExOpStatsRateEx_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 3),
    _NtwsApStatRadioRateExOpStatsRateEx_Type()
)
ntwsApStatRadioRateExOpStatsRateEx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsRateEx.setStatus("current")
_NtwsApStatRadioRateExOpStatsTxUniPkt_Type = Counter64
_NtwsApStatRadioRateExOpStatsTxUniPkt_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsTxUniPkt = _NtwsApStatRadioRateExOpStatsTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 4),
    _NtwsApStatRadioRateExOpStatsTxUniPkt_Type()
)
ntwsApStatRadioRateExOpStatsTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsTxUniPkt.setStatus("current")
_NtwsApStatRadioRateExOpStatsTxUniOctet_Type = Counter64
_NtwsApStatRadioRateExOpStatsTxUniOctet_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsTxUniOctet = _NtwsApStatRadioRateExOpStatsTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 5),
    _NtwsApStatRadioRateExOpStatsTxUniOctet_Type()
)
ntwsApStatRadioRateExOpStatsTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsTxUniOctet.setStatus("current")
_NtwsApStatRadioRateExOpStatsTxMultiPkt_Type = Counter64
_NtwsApStatRadioRateExOpStatsTxMultiPkt_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsTxMultiPkt = _NtwsApStatRadioRateExOpStatsTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 6),
    _NtwsApStatRadioRateExOpStatsTxMultiPkt_Type()
)
ntwsApStatRadioRateExOpStatsTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsTxMultiPkt.setStatus("current")
_NtwsApStatRadioRateExOpStatsTxMultiOctet_Type = Counter64
_NtwsApStatRadioRateExOpStatsTxMultiOctet_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsTxMultiOctet = _NtwsApStatRadioRateExOpStatsTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 7),
    _NtwsApStatRadioRateExOpStatsTxMultiOctet_Type()
)
ntwsApStatRadioRateExOpStatsTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsTxMultiOctet.setStatus("current")
_NtwsApStatRadioRateExOpStatsRxPkt_Type = Counter64
_NtwsApStatRadioRateExOpStatsRxPkt_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsRxPkt = _NtwsApStatRadioRateExOpStatsRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 8),
    _NtwsApStatRadioRateExOpStatsRxPkt_Type()
)
ntwsApStatRadioRateExOpStatsRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsRxPkt.setStatus("current")
_NtwsApStatRadioRateExOpStatsRxOctet_Type = Counter64
_NtwsApStatRadioRateExOpStatsRxOctet_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsRxOctet = _NtwsApStatRadioRateExOpStatsRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 9),
    _NtwsApStatRadioRateExOpStatsRxOctet_Type()
)
ntwsApStatRadioRateExOpStatsRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsRxOctet.setStatus("current")
_NtwsApStatRadioRateExOpStatsUndcrptPkt_Type = Counter64
_NtwsApStatRadioRateExOpStatsUndcrptPkt_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsUndcrptPkt = _NtwsApStatRadioRateExOpStatsUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 10),
    _NtwsApStatRadioRateExOpStatsUndcrptPkt_Type()
)
ntwsApStatRadioRateExOpStatsUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsUndcrptPkt.setStatus("current")
_NtwsApStatRadioRateExOpStatsUndcrptOctet_Type = Counter64
_NtwsApStatRadioRateExOpStatsUndcrptOctet_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsUndcrptOctet = _NtwsApStatRadioRateExOpStatsUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 11),
    _NtwsApStatRadioRateExOpStatsUndcrptOctet_Type()
)
ntwsApStatRadioRateExOpStatsUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsUndcrptOctet.setStatus("current")
_NtwsApStatRadioRateExOpStatsPhyErr_Type = Counter64
_NtwsApStatRadioRateExOpStatsPhyErr_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsPhyErr = _NtwsApStatRadioRateExOpStatsPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 14, 1, 12),
    _NtwsApStatRadioRateExOpStatsPhyErr_Type()
)
ntwsApStatRadioRateExOpStatsPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsPhyErr.setStatus("current")
_NtwsApStatRadioRateExOpStatisticsMacTable_Object = MibTable
ntwsApStatRadioRateExOpStatisticsMacTable = _NtwsApStatRadioRateExOpStatisticsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15)
)
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatisticsMacTable.setStatus("current")
_NtwsApStatRadioRateExOpStatisticsMacEntry_Object = MibTableRow
ntwsApStatRadioRateExOpStatisticsMacEntry = _NtwsApStatRadioRateExOpStatisticsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1)
)
ntwsApStatRadioRateExOpStatisticsMacEntry.setIndexNames(
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacBaseMac"),
    (0, "NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacRateEx"),
)
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatisticsMacEntry.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacBaseMac_Type = MacAddress
_NtwsApStatRadioRateExOpStatsMacBaseMac_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacBaseMac = _NtwsApStatRadioRateExOpStatsMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 1),
    _NtwsApStatRadioRateExOpStatsMacBaseMac_Type()
)
ntwsApStatRadioRateExOpStatsMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacBaseMac.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacRateEx_Type = NtwsRadioRateEx
_NtwsApStatRadioRateExOpStatsMacRateEx_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacRateEx = _NtwsApStatRadioRateExOpStatsMacRateEx_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 2),
    _NtwsApStatRadioRateExOpStatsMacRateEx_Type()
)
ntwsApStatRadioRateExOpStatsMacRateEx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacRateEx.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacTxUniPkt_Type = Counter64
_NtwsApStatRadioRateExOpStatsMacTxUniPkt_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacTxUniPkt = _NtwsApStatRadioRateExOpStatsMacTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 3),
    _NtwsApStatRadioRateExOpStatsMacTxUniPkt_Type()
)
ntwsApStatRadioRateExOpStatsMacTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacTxUniPkt.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacTxUniOctet_Type = Counter64
_NtwsApStatRadioRateExOpStatsMacTxUniOctet_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacTxUniOctet = _NtwsApStatRadioRateExOpStatsMacTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 4),
    _NtwsApStatRadioRateExOpStatsMacTxUniOctet_Type()
)
ntwsApStatRadioRateExOpStatsMacTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacTxUniOctet.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacTxMultiPkt_Type = Counter64
_NtwsApStatRadioRateExOpStatsMacTxMultiPkt_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacTxMultiPkt = _NtwsApStatRadioRateExOpStatsMacTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 5),
    _NtwsApStatRadioRateExOpStatsMacTxMultiPkt_Type()
)
ntwsApStatRadioRateExOpStatsMacTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacTxMultiPkt.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacTxMultiOctet_Type = Counter64
_NtwsApStatRadioRateExOpStatsMacTxMultiOctet_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacTxMultiOctet = _NtwsApStatRadioRateExOpStatsMacTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 6),
    _NtwsApStatRadioRateExOpStatsMacTxMultiOctet_Type()
)
ntwsApStatRadioRateExOpStatsMacTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacTxMultiOctet.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacRxPkt_Type = Counter64
_NtwsApStatRadioRateExOpStatsMacRxPkt_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacRxPkt = _NtwsApStatRadioRateExOpStatsMacRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 7),
    _NtwsApStatRadioRateExOpStatsMacRxPkt_Type()
)
ntwsApStatRadioRateExOpStatsMacRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacRxPkt.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacRxOctet_Type = Counter64
_NtwsApStatRadioRateExOpStatsMacRxOctet_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacRxOctet = _NtwsApStatRadioRateExOpStatsMacRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 8),
    _NtwsApStatRadioRateExOpStatsMacRxOctet_Type()
)
ntwsApStatRadioRateExOpStatsMacRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacRxOctet.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacUndcrptPkt_Type = Counter64
_NtwsApStatRadioRateExOpStatsMacUndcrptPkt_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacUndcrptPkt = _NtwsApStatRadioRateExOpStatsMacUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 9),
    _NtwsApStatRadioRateExOpStatsMacUndcrptPkt_Type()
)
ntwsApStatRadioRateExOpStatsMacUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacUndcrptPkt.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacUndcrptOctet_Type = Counter64
_NtwsApStatRadioRateExOpStatsMacUndcrptOctet_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacUndcrptOctet = _NtwsApStatRadioRateExOpStatsMacUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 10),
    _NtwsApStatRadioRateExOpStatsMacUndcrptOctet_Type()
)
ntwsApStatRadioRateExOpStatsMacUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacUndcrptOctet.setStatus("current")
_NtwsApStatRadioRateExOpStatsMacPhyErr_Type = Counter64
_NtwsApStatRadioRateExOpStatsMacPhyErr_Object = MibTableColumn
ntwsApStatRadioRateExOpStatsMacPhyErr = _NtwsApStatRadioRateExOpStatsMacPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 1, 15, 1, 11),
    _NtwsApStatRadioRateExOpStatsMacPhyErr_Type()
)
ntwsApStatRadioRateExOpStatsMacPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApStatRadioRateExOpStatsMacPhyErr.setStatus("current")
_NtwsApStatusConformance_ObjectIdentity = ObjectIdentity
ntwsApStatusConformance = _NtwsApStatusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2)
)
_NtwsApStatusCompliances_ObjectIdentity = ObjectIdentity
ntwsApStatusCompliances = _NtwsApStatusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 1)
)
_NtwsApStatusGroups_ObjectIdentity = ObjectIdentity
ntwsApStatusGroups = _NtwsApStatusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2)
)

# Managed Objects groups

ntwsApStatusCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 1)
)
ntwsApStatusCommonGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatNumAps"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusBaseMac"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusAttachType"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusPortOrDapNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusApState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusModel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusFingerprint"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusApName"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusVlan"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusIpAddress"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusUptimeSecs"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusCpuInfo"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusManufacturerId"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusRamBytes"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusHardwareRev"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacSerialNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacAttachType"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacPortOrDapNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacApState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacModel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacFingerprint"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacApName"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacVlan"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacIpAddress"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacUptimeSecs"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacCpuInfo"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacManufacturerId"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacRamBytes"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacHardwareRev"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusBaseMac"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusEnable"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusRadioConfigState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusCurrentPowerLevel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusCurrentChannelNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacApSerialNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacRadioNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacEnable"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacRadioConfigState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacCurrentPowerLevel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacCurrentChannelNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServBssid"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServServiceProfileName"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServMacApSerialNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServMacRadioNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServMacSsid"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServMacServiceProfileName"))
)
if mibBuilder.loadTexts:
    ntwsApStatusCommonGroup.setStatus("obsolete")

ntwsApStatusScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 2)
)
ntwsApStatusScalarsGroup.setObjects(
    ("NTWS-AP-STATUS-MIB", "ntwsApStatNumAps")
)
if mibBuilder.loadTexts:
    ntwsApStatusScalarsGroup.setStatus("current")

ntwsApStatusApStatusTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 3)
)
ntwsApStatusApStatusTablesGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusBaseMac"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusAttachType"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusPortOrDapNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusApState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusModel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusFingerprint"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusApName"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusVlan"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusIpAddress"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusUptimeSecs"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusCpuInfo"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusManufacturerId"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusRamBytes"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusHardwareRev"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusClientSessions"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacSerialNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacAttachType"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacPortOrDapNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacApState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacModel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacFingerprint"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacApName"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacVlan"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacIpAddress"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacUptimeSecs"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacCpuInfo"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacManufacturerId"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacRamBytes"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacHardwareRev"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacClientSessions"))
)
if mibBuilder.loadTexts:
    ntwsApStatusApStatusTablesGroup.setStatus("obsolete")

ntwsApStatusRadioStatusTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 4)
)
ntwsApStatusRadioStatusTablesGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusBaseMac"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusEnable"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusRadioConfigState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusCurrentPowerLevel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusCurrentChannelNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacApSerialNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacRadioNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacEnable"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacRadioConfigState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacCurrentPowerLevel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacCurrentChannelNum"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioStatusTablesGroup.setStatus("obsolete")

ntwsApStatusRadioServiceTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 5)
)
ntwsApStatusRadioServiceTablesGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServBssid"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServServiceProfileName"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServMacApSerialNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServMacRadioNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServMacSsid"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioServMacServiceProfileName"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioServiceTablesGroup.setStatus("current")

ntwsApStatusRadioServiceOpRateSetTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 6)
)
ntwsApStatusRadioServiceOpRateSetTablesGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetMandatory"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetDisabled"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetBeacon"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetMulticast"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetMacMandatory"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetMacDisabled"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetMacBeacon"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioSORSetMacMulticast"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioServiceOpRateSetTablesGroup.setStatus("current")

ntwsApStatusRadioOpStatisticsTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 7)
)
ntwsApStatusRadioOpStatisticsTablesGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsTxUniPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsTxUniOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsTxMultiPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsTxMultiOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsRxPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsRxOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsUndcrptPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsUndcrptOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsPhyErr"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsResetCount"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsAutoTuneChannelChangeCount"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsTxRetriesCount"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsUserSessions"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsNoiseFloor"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacTxUniPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacTxUniOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacTxMultiPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacTxMultiOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacRxPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacRxOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacUndcrptPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacUndcrptOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacPhyErr"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacResetCount"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacAutoTuneChannelChangeCount"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacTxRetriesCount"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacUserSessions"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacNoiseFloor"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioOpStatisticsTablesGroup.setStatus("current")

ntwsApStatusRadioOpStatisticsPerRateTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 8)
)
ntwsApStatusRadioOpStatisticsPerRateTablesGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsTxUniPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsTxUniOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsTxMultiPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsTxMultiOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsRxPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsRxOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsUndcrptPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsUndcrptOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsPhyErr"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacTxUniPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacTxUniOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacTxMultiPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacTxMultiOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacRxPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacRxOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacUndcrptPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacUndcrptOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateOpStatsMacPhyErr"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioOpStatisticsPerRateTablesGroup.setStatus("current")

ntwsApStatusApStatusVersionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 9)
)
ntwsApStatusApStatusVersionsGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusSoftwareVer"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusBootVer"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacSoftwareVer"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacBootVer"))
)
if mibBuilder.loadTexts:
    ntwsApStatusApStatusVersionsGroup.setStatus("current")

ntwsApStatusApStatusTablesGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 10)
)
ntwsApStatusApStatusTablesGroupRev2.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusBaseMac"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusAttachType"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusApState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusModel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusFingerprint"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusApName"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusVlan"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusIpAddress"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusUptimeSecs"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusCpuInfo"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusManufacturerId"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusRamBytes"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusHardwareRev"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusClientSessions"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusApNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacSerialNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacAttachType"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacApState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacModel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacFingerprint"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacApName"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacVlan"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacIpAddress"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacUptimeSecs"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacCpuInfo"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacManufacturerId"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacRamBytes"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacHardwareRev"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacClientSessions"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacApNum"))
)
if mibBuilder.loadTexts:
    ntwsApStatusApStatusTablesGroupRev2.setStatus("current")

ntwsApStatusRadioStatusMaxPowerPhyTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 11)
)
ntwsApStatusRadioStatusMaxPowerPhyTypeGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMaxPowerLevel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusRadioPhyType"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacMaxPowerLevel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacRadioPhyType"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioStatusMaxPowerPhyTypeGroup.setStatus("current")

ntwsApStatusRadioStatusTablesGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 12)
)
ntwsApStatusRadioStatusTablesGroupRev2.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusBaseMac"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusRadioConfigState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusCurrentPowerLevel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusCurrentChannelNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusClientSessions"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusRadioMode"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacApSerialNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacRadioNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacRadioConfigState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacCurrentPowerLevel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacCurrentChannelNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacClientSessions"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacRadioMode"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioStatusTablesGroupRev2.setStatus("current")

ntwsApStatusRadioStatusWideMimoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 13)
)
ntwsApStatusRadioStatusWideMimoGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusRadioChannelWidth"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusRadioMimoState"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacRadioChannelWidth"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacRadioMimoState"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioStatusWideMimoGroup.setStatus("current")

ntwsApStatusRadioOpStatisticsPerRateExTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 14)
)
ntwsApStatusRadioOpStatisticsPerRateExTablesGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsTxUniPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsTxUniOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsTxMultiPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsTxMultiOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsRxPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsRxOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsUndcrptPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsUndcrptOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsPhyErr"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacTxUniPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacTxUniOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacTxMultiPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacTxMultiOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacRxPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacRxOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacUndcrptPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacUndcrptOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioRateExOpStatsMacPhyErr"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioOpStatisticsPerRateExTablesGroup.setStatus("current")

ntwsApStatusApStatusPhysPortNumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 15)
)
ntwsApStatusApStatusPhysPortNumGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusPhysPortNum"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacPhysPortNum"))
)
if mibBuilder.loadTexts:
    ntwsApStatusApStatusPhysPortNumGroup.setStatus("current")

ntwsApStatusApStatusConnectivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 16)
)
ntwsApStatusApStatusConnectivityGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusIpNetmask"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusWiredIfNumber"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacIpNetmask"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatApStatusMacWiredIfNumber"))
)
if mibBuilder.loadTexts:
    ntwsApStatusApStatusConnectivityGroup.setStatus("current")

ntwsApStatusRadioStatusAntennaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 17)
)
ntwsApStatusRadioStatusAntennaGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMinPowerLevel"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioStatusMacMinPowerLevel"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioStatusAntennaGroup.setStatus("current")

ntwsApStatusRadioOpStatisticsClientAssocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 18)
)
ntwsApStatusRadioOpStatisticsClientAssocGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsClientAssociations"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsClientFailedAssociations"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsClientReAssociations"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacClientAssociations"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacClientFailedAssociations"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacClientReAssociations"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioOpStatisticsClientAssocGroup.setStatus("current")

ntwsApStatusRadioOpStatisticsSignErrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 2, 19)
)
ntwsApStatusRadioOpStatisticsSignErrGroup.setObjects(
      *(("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsSignalingPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsReTransmitOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsRefusedConnectionCount"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacSignalingPkt"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacReTransmitOctet"),
        ("NTWS-AP-STATUS-MIB", "ntwsApStatRadioOpStatsMacRefusedConnectionCount"))
)
if mibBuilder.loadTexts:
    ntwsApStatusRadioOpStatisticsSignErrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntwsApStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsApStatusCompliance.setStatus(
        "obsolete"
    )

ntwsApStatusComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ntwsApStatusComplianceRev2.setStatus(
        "obsolete"
    )

ntwsApStatusComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ntwsApStatusComplianceRev3.setStatus(
        "obsolete"
    )

ntwsApStatusComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ntwsApStatusComplianceRev4.setStatus(
        "obsolete"
    )

ntwsApStatusComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 5, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ntwsApStatusComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-AP-STATUS-MIB",
    **{"NtwsRadioOpRateSetSingleValue": NtwsRadioOpRateSetSingleValue,
       "NtwsRadioOpRateSetMandatory": NtwsRadioOpRateSetMandatory,
       "NtwsRadioOpRateSetDisabled": NtwsRadioOpRateSetDisabled,
       "ntwsApStatusMib": ntwsApStatusMib,
       "ntwsApStatusObjects": ntwsApStatusObjects,
       "ntwsApStatDataObjects": ntwsApStatDataObjects,
       "ntwsApStatNumAps": ntwsApStatNumAps,
       "ntwsApStatApStatusTable": ntwsApStatApStatusTable,
       "ntwsApStatApStatusEntry": ntwsApStatApStatusEntry,
       "ntwsApStatApStatusSerialNum": ntwsApStatApStatusSerialNum,
       "ntwsApStatApStatusBaseMac": ntwsApStatApStatusBaseMac,
       "ntwsApStatApStatusAttachType": ntwsApStatApStatusAttachType,
       "ntwsApStatApStatusPortOrDapNum": ntwsApStatApStatusPortOrDapNum,
       "ntwsApStatApStatusApState": ntwsApStatApStatusApState,
       "ntwsApStatApStatusModel": ntwsApStatApStatusModel,
       "ntwsApStatApStatusFingerprint": ntwsApStatApStatusFingerprint,
       "ntwsApStatApStatusApName": ntwsApStatApStatusApName,
       "ntwsApStatApStatusVlan": ntwsApStatApStatusVlan,
       "ntwsApStatApStatusIpAddress": ntwsApStatApStatusIpAddress,
       "ntwsApStatApStatusUptimeSecs": ntwsApStatApStatusUptimeSecs,
       "ntwsApStatApStatusCpuInfo": ntwsApStatApStatusCpuInfo,
       "ntwsApStatApStatusManufacturerId": ntwsApStatApStatusManufacturerId,
       "ntwsApStatApStatusRamBytes": ntwsApStatApStatusRamBytes,
       "ntwsApStatApStatusHardwareRev": ntwsApStatApStatusHardwareRev,
       "ntwsApStatApStatusClientSessions": ntwsApStatApStatusClientSessions,
       "ntwsApStatApStatusSoftwareVer": ntwsApStatApStatusSoftwareVer,
       "ntwsApStatApStatusBootVer": ntwsApStatApStatusBootVer,
       "ntwsApStatApStatusApNum": ntwsApStatApStatusApNum,
       "ntwsApStatApStatusPhysPortNum": ntwsApStatApStatusPhysPortNum,
       "ntwsApStatApStatusIpNetmask": ntwsApStatApStatusIpNetmask,
       "ntwsApStatApStatusWiredIfNumber": ntwsApStatApStatusWiredIfNumber,
       "ntwsApStatApStatusMacTable": ntwsApStatApStatusMacTable,
       "ntwsApStatApStatusMacEntry": ntwsApStatApStatusMacEntry,
       "ntwsApStatApStatusMacBaseMac": ntwsApStatApStatusMacBaseMac,
       "ntwsApStatApStatusMacSerialNum": ntwsApStatApStatusMacSerialNum,
       "ntwsApStatApStatusMacAttachType": ntwsApStatApStatusMacAttachType,
       "ntwsApStatApStatusMacPortOrDapNum": ntwsApStatApStatusMacPortOrDapNum,
       "ntwsApStatApStatusMacApState": ntwsApStatApStatusMacApState,
       "ntwsApStatApStatusMacModel": ntwsApStatApStatusMacModel,
       "ntwsApStatApStatusMacFingerprint": ntwsApStatApStatusMacFingerprint,
       "ntwsApStatApStatusMacApName": ntwsApStatApStatusMacApName,
       "ntwsApStatApStatusMacVlan": ntwsApStatApStatusMacVlan,
       "ntwsApStatApStatusMacIpAddress": ntwsApStatApStatusMacIpAddress,
       "ntwsApStatApStatusMacUptimeSecs": ntwsApStatApStatusMacUptimeSecs,
       "ntwsApStatApStatusMacCpuInfo": ntwsApStatApStatusMacCpuInfo,
       "ntwsApStatApStatusMacManufacturerId": ntwsApStatApStatusMacManufacturerId,
       "ntwsApStatApStatusMacRamBytes": ntwsApStatApStatusMacRamBytes,
       "ntwsApStatApStatusMacHardwareRev": ntwsApStatApStatusMacHardwareRev,
       "ntwsApStatApStatusMacClientSessions": ntwsApStatApStatusMacClientSessions,
       "ntwsApStatApStatusMacSoftwareVer": ntwsApStatApStatusMacSoftwareVer,
       "ntwsApStatApStatusMacBootVer": ntwsApStatApStatusMacBootVer,
       "ntwsApStatApStatusMacApNum": ntwsApStatApStatusMacApNum,
       "ntwsApStatApStatusMacPhysPortNum": ntwsApStatApStatusMacPhysPortNum,
       "ntwsApStatApStatusMacIpNetmask": ntwsApStatApStatusMacIpNetmask,
       "ntwsApStatApStatusMacWiredIfNumber": ntwsApStatApStatusMacWiredIfNumber,
       "ntwsApStatRadioStatusTable": ntwsApStatRadioStatusTable,
       "ntwsApStatRadioStatusEntry": ntwsApStatRadioStatusEntry,
       "ntwsApStatRadioStatusApSerialNum": ntwsApStatRadioStatusApSerialNum,
       "ntwsApStatRadioStatusRadioNum": ntwsApStatRadioStatusRadioNum,
       "ntwsApStatRadioStatusBaseMac": ntwsApStatRadioStatusBaseMac,
       "ntwsApStatRadioStatusEnable": ntwsApStatRadioStatusEnable,
       "ntwsApStatRadioStatusRadioConfigState": ntwsApStatRadioStatusRadioConfigState,
       "ntwsApStatRadioStatusCurrentPowerLevel": ntwsApStatRadioStatusCurrentPowerLevel,
       "ntwsApStatRadioStatusCurrentChannelNum": ntwsApStatRadioStatusCurrentChannelNum,
       "ntwsApStatRadioStatusClientSessions": ntwsApStatRadioStatusClientSessions,
       "ntwsApStatRadioStatusMaxPowerLevel": ntwsApStatRadioStatusMaxPowerLevel,
       "ntwsApStatRadioStatusRadioPhyType": ntwsApStatRadioStatusRadioPhyType,
       "ntwsApStatRadioStatusRadioMode": ntwsApStatRadioStatusRadioMode,
       "ntwsApStatRadioStatusRadioChannelWidth": ntwsApStatRadioStatusRadioChannelWidth,
       "ntwsApStatRadioStatusRadioMimoState": ntwsApStatRadioStatusRadioMimoState,
       "ntwsApStatRadioStatusMinPowerLevel": ntwsApStatRadioStatusMinPowerLevel,
       "ntwsApStatRadioStatusMacTable": ntwsApStatRadioStatusMacTable,
       "ntwsApStatRadioStatusMacEntry": ntwsApStatRadioStatusMacEntry,
       "ntwsApStatRadioStatusMacBaseMac": ntwsApStatRadioStatusMacBaseMac,
       "ntwsApStatRadioStatusMacApSerialNum": ntwsApStatRadioStatusMacApSerialNum,
       "ntwsApStatRadioStatusMacRadioNum": ntwsApStatRadioStatusMacRadioNum,
       "ntwsApStatRadioStatusMacEnable": ntwsApStatRadioStatusMacEnable,
       "ntwsApStatRadioStatusMacRadioConfigState": ntwsApStatRadioStatusMacRadioConfigState,
       "ntwsApStatRadioStatusMacCurrentPowerLevel": ntwsApStatRadioStatusMacCurrentPowerLevel,
       "ntwsApStatRadioStatusMacCurrentChannelNum": ntwsApStatRadioStatusMacCurrentChannelNum,
       "ntwsApStatRadioStatusMacClientSessions": ntwsApStatRadioStatusMacClientSessions,
       "ntwsApStatRadioStatusMacMaxPowerLevel": ntwsApStatRadioStatusMacMaxPowerLevel,
       "ntwsApStatRadioStatusMacRadioPhyType": ntwsApStatRadioStatusMacRadioPhyType,
       "ntwsApStatRadioStatusMacRadioMode": ntwsApStatRadioStatusMacRadioMode,
       "ntwsApStatRadioStatusMacRadioChannelWidth": ntwsApStatRadioStatusMacRadioChannelWidth,
       "ntwsApStatRadioStatusMacRadioMimoState": ntwsApStatRadioStatusMacRadioMimoState,
       "ntwsApStatRadioStatusMacMinPowerLevel": ntwsApStatRadioStatusMacMinPowerLevel,
       "ntwsApStatRadioServiceTable": ntwsApStatRadioServiceTable,
       "ntwsApStatRadioServiceEntry": ntwsApStatRadioServiceEntry,
       "ntwsApStatRadioServApSerialNum": ntwsApStatRadioServApSerialNum,
       "ntwsApStatRadioServRadioNum": ntwsApStatRadioServRadioNum,
       "ntwsApStatRadioServSsid": ntwsApStatRadioServSsid,
       "ntwsApStatRadioServBssid": ntwsApStatRadioServBssid,
       "ntwsApStatRadioServServiceProfileName": ntwsApStatRadioServServiceProfileName,
       "ntwsApStatRadioServiceMacTable": ntwsApStatRadioServiceMacTable,
       "ntwsApStatRadioServiceMacEntry": ntwsApStatRadioServiceMacEntry,
       "ntwsApStatRadioServMacBssid": ntwsApStatRadioServMacBssid,
       "ntwsApStatRadioServMacApSerialNum": ntwsApStatRadioServMacApSerialNum,
       "ntwsApStatRadioServMacRadioNum": ntwsApStatRadioServMacRadioNum,
       "ntwsApStatRadioServMacSsid": ntwsApStatRadioServMacSsid,
       "ntwsApStatRadioServMacServiceProfileName": ntwsApStatRadioServMacServiceProfileName,
       "ntwsApStatRadioServiceOpRateSetTable": ntwsApStatRadioServiceOpRateSetTable,
       "ntwsApStatRadioServiceOpRateSetEntry": ntwsApStatRadioServiceOpRateSetEntry,
       "ntwsApStatRadioSORSetApSerialNum": ntwsApStatRadioSORSetApSerialNum,
       "ntwsApStatRadioSORSetRadioNum": ntwsApStatRadioSORSetRadioNum,
       "ntwsApStatRadioSORSetSsid": ntwsApStatRadioSORSetSsid,
       "ntwsApStatRadioSORSetMandatory": ntwsApStatRadioSORSetMandatory,
       "ntwsApStatRadioSORSetDisabled": ntwsApStatRadioSORSetDisabled,
       "ntwsApStatRadioSORSetBeacon": ntwsApStatRadioSORSetBeacon,
       "ntwsApStatRadioSORSetMulticast": ntwsApStatRadioSORSetMulticast,
       "ntwsApStatRadioServiceOpRateSetMacTable": ntwsApStatRadioServiceOpRateSetMacTable,
       "ntwsApStatRadioServiceOpRateSetMacEntry": ntwsApStatRadioServiceOpRateSetMacEntry,
       "ntwsApStatRadioSORSetMacBssid": ntwsApStatRadioSORSetMacBssid,
       "ntwsApStatRadioSORSetMacMandatory": ntwsApStatRadioSORSetMacMandatory,
       "ntwsApStatRadioSORSetMacDisabled": ntwsApStatRadioSORSetMacDisabled,
       "ntwsApStatRadioSORSetMacBeacon": ntwsApStatRadioSORSetMacBeacon,
       "ntwsApStatRadioSORSetMacMulticast": ntwsApStatRadioSORSetMacMulticast,
       "ntwsApStatRadioOpStatisticsTable": ntwsApStatRadioOpStatisticsTable,
       "ntwsApStatRadioOpStatisticsEntry": ntwsApStatRadioOpStatisticsEntry,
       "ntwsApStatRadioOpStatsApSerialNum": ntwsApStatRadioOpStatsApSerialNum,
       "ntwsApStatRadioOpStatsRadioNum": ntwsApStatRadioOpStatsRadioNum,
       "ntwsApStatRadioOpStatsTxUniPkt": ntwsApStatRadioOpStatsTxUniPkt,
       "ntwsApStatRadioOpStatsTxUniOctet": ntwsApStatRadioOpStatsTxUniOctet,
       "ntwsApStatRadioOpStatsTxMultiPkt": ntwsApStatRadioOpStatsTxMultiPkt,
       "ntwsApStatRadioOpStatsTxMultiOctet": ntwsApStatRadioOpStatsTxMultiOctet,
       "ntwsApStatRadioOpStatsRxPkt": ntwsApStatRadioOpStatsRxPkt,
       "ntwsApStatRadioOpStatsRxOctet": ntwsApStatRadioOpStatsRxOctet,
       "ntwsApStatRadioOpStatsUndcrptPkt": ntwsApStatRadioOpStatsUndcrptPkt,
       "ntwsApStatRadioOpStatsUndcrptOctet": ntwsApStatRadioOpStatsUndcrptOctet,
       "ntwsApStatRadioOpStatsPhyErr": ntwsApStatRadioOpStatsPhyErr,
       "ntwsApStatRadioOpStatsResetCount": ntwsApStatRadioOpStatsResetCount,
       "ntwsApStatRadioOpStatsAutoTuneChannelChangeCount": ntwsApStatRadioOpStatsAutoTuneChannelChangeCount,
       "ntwsApStatRadioOpStatsTxRetriesCount": ntwsApStatRadioOpStatsTxRetriesCount,
       "ntwsApStatRadioOpStatsUserSessions": ntwsApStatRadioOpStatsUserSessions,
       "ntwsApStatRadioOpStatsNoiseFloor": ntwsApStatRadioOpStatsNoiseFloor,
       "ntwsApStatRadioOpStatsClientAssociations": ntwsApStatRadioOpStatsClientAssociations,
       "ntwsApStatRadioOpStatsClientFailedAssociations": ntwsApStatRadioOpStatsClientFailedAssociations,
       "ntwsApStatRadioOpStatsClientReAssociations": ntwsApStatRadioOpStatsClientReAssociations,
       "ntwsApStatRadioOpStatsSignalingPkt": ntwsApStatRadioOpStatsSignalingPkt,
       "ntwsApStatRadioOpStatsReTransmitOctet": ntwsApStatRadioOpStatsReTransmitOctet,
       "ntwsApStatRadioOpStatsRefusedConnectionCount": ntwsApStatRadioOpStatsRefusedConnectionCount,
       "ntwsApStatRadioOpStatisticsMacTable": ntwsApStatRadioOpStatisticsMacTable,
       "ntwsApStatRadioOpStatisticsMacEntry": ntwsApStatRadioOpStatisticsMacEntry,
       "ntwsApStatRadioOpStatsMacBaseMac": ntwsApStatRadioOpStatsMacBaseMac,
       "ntwsApStatRadioOpStatsMacTxUniPkt": ntwsApStatRadioOpStatsMacTxUniPkt,
       "ntwsApStatRadioOpStatsMacTxUniOctet": ntwsApStatRadioOpStatsMacTxUniOctet,
       "ntwsApStatRadioOpStatsMacTxMultiPkt": ntwsApStatRadioOpStatsMacTxMultiPkt,
       "ntwsApStatRadioOpStatsMacTxMultiOctet": ntwsApStatRadioOpStatsMacTxMultiOctet,
       "ntwsApStatRadioOpStatsMacRxPkt": ntwsApStatRadioOpStatsMacRxPkt,
       "ntwsApStatRadioOpStatsMacRxOctet": ntwsApStatRadioOpStatsMacRxOctet,
       "ntwsApStatRadioOpStatsMacUndcrptPkt": ntwsApStatRadioOpStatsMacUndcrptPkt,
       "ntwsApStatRadioOpStatsMacUndcrptOctet": ntwsApStatRadioOpStatsMacUndcrptOctet,
       "ntwsApStatRadioOpStatsMacPhyErr": ntwsApStatRadioOpStatsMacPhyErr,
       "ntwsApStatRadioOpStatsMacResetCount": ntwsApStatRadioOpStatsMacResetCount,
       "ntwsApStatRadioOpStatsMacAutoTuneChannelChangeCount": ntwsApStatRadioOpStatsMacAutoTuneChannelChangeCount,
       "ntwsApStatRadioOpStatsMacTxRetriesCount": ntwsApStatRadioOpStatsMacTxRetriesCount,
       "ntwsApStatRadioOpStatsMacUserSessions": ntwsApStatRadioOpStatsMacUserSessions,
       "ntwsApStatRadioOpStatsMacNoiseFloor": ntwsApStatRadioOpStatsMacNoiseFloor,
       "ntwsApStatRadioOpStatsMacClientAssociations": ntwsApStatRadioOpStatsMacClientAssociations,
       "ntwsApStatRadioOpStatsMacClientFailedAssociations": ntwsApStatRadioOpStatsMacClientFailedAssociations,
       "ntwsApStatRadioOpStatsMacClientReAssociations": ntwsApStatRadioOpStatsMacClientReAssociations,
       "ntwsApStatRadioOpStatsMacSignalingPkt": ntwsApStatRadioOpStatsMacSignalingPkt,
       "ntwsApStatRadioOpStatsMacReTransmitOctet": ntwsApStatRadioOpStatsMacReTransmitOctet,
       "ntwsApStatRadioOpStatsMacRefusedConnectionCount": ntwsApStatRadioOpStatsMacRefusedConnectionCount,
       "ntwsApStatRadioRateOpStatisticsTable": ntwsApStatRadioRateOpStatisticsTable,
       "ntwsApStatRadioRateOpStatisticsEntry": ntwsApStatRadioRateOpStatisticsEntry,
       "ntwsApStatRadioRateOpStatsApSerialNum": ntwsApStatRadioRateOpStatsApSerialNum,
       "ntwsApStatRadioRateOpStatsRadioNum": ntwsApStatRadioRateOpStatsRadioNum,
       "ntwsApStatRadioRateOpStatsRate": ntwsApStatRadioRateOpStatsRate,
       "ntwsApStatRadioRateOpStatsTxUniPkt": ntwsApStatRadioRateOpStatsTxUniPkt,
       "ntwsApStatRadioRateOpStatsTxUniOctet": ntwsApStatRadioRateOpStatsTxUniOctet,
       "ntwsApStatRadioRateOpStatsTxMultiPkt": ntwsApStatRadioRateOpStatsTxMultiPkt,
       "ntwsApStatRadioRateOpStatsTxMultiOctet": ntwsApStatRadioRateOpStatsTxMultiOctet,
       "ntwsApStatRadioRateOpStatsRxPkt": ntwsApStatRadioRateOpStatsRxPkt,
       "ntwsApStatRadioRateOpStatsRxOctet": ntwsApStatRadioRateOpStatsRxOctet,
       "ntwsApStatRadioRateOpStatsUndcrptPkt": ntwsApStatRadioRateOpStatsUndcrptPkt,
       "ntwsApStatRadioRateOpStatsUndcrptOctet": ntwsApStatRadioRateOpStatsUndcrptOctet,
       "ntwsApStatRadioRateOpStatsPhyErr": ntwsApStatRadioRateOpStatsPhyErr,
       "ntwsApStatRadioRateOpStatisticsMacTable": ntwsApStatRadioRateOpStatisticsMacTable,
       "ntwsApStatRadioRateOpStatisticsMacEntry": ntwsApStatRadioRateOpStatisticsMacEntry,
       "ntwsApStatRadioRateOpStatsMacBaseMac": ntwsApStatRadioRateOpStatsMacBaseMac,
       "ntwsApStatRadioRateOpStatsMacRate": ntwsApStatRadioRateOpStatsMacRate,
       "ntwsApStatRadioRateOpStatsMacTxUniPkt": ntwsApStatRadioRateOpStatsMacTxUniPkt,
       "ntwsApStatRadioRateOpStatsMacTxUniOctet": ntwsApStatRadioRateOpStatsMacTxUniOctet,
       "ntwsApStatRadioRateOpStatsMacTxMultiPkt": ntwsApStatRadioRateOpStatsMacTxMultiPkt,
       "ntwsApStatRadioRateOpStatsMacTxMultiOctet": ntwsApStatRadioRateOpStatsMacTxMultiOctet,
       "ntwsApStatRadioRateOpStatsMacRxPkt": ntwsApStatRadioRateOpStatsMacRxPkt,
       "ntwsApStatRadioRateOpStatsMacRxOctet": ntwsApStatRadioRateOpStatsMacRxOctet,
       "ntwsApStatRadioRateOpStatsMacUndcrptPkt": ntwsApStatRadioRateOpStatsMacUndcrptPkt,
       "ntwsApStatRadioRateOpStatsMacUndcrptOctet": ntwsApStatRadioRateOpStatsMacUndcrptOctet,
       "ntwsApStatRadioRateOpStatsMacPhyErr": ntwsApStatRadioRateOpStatsMacPhyErr,
       "ntwsApStatRadioRateExOpStatisticsTable": ntwsApStatRadioRateExOpStatisticsTable,
       "ntwsApStatRadioRateExOpStatisticsEntry": ntwsApStatRadioRateExOpStatisticsEntry,
       "ntwsApStatRadioRateExOpStatsApSerialNum": ntwsApStatRadioRateExOpStatsApSerialNum,
       "ntwsApStatRadioRateExOpStatsRadioNum": ntwsApStatRadioRateExOpStatsRadioNum,
       "ntwsApStatRadioRateExOpStatsRateEx": ntwsApStatRadioRateExOpStatsRateEx,
       "ntwsApStatRadioRateExOpStatsTxUniPkt": ntwsApStatRadioRateExOpStatsTxUniPkt,
       "ntwsApStatRadioRateExOpStatsTxUniOctet": ntwsApStatRadioRateExOpStatsTxUniOctet,
       "ntwsApStatRadioRateExOpStatsTxMultiPkt": ntwsApStatRadioRateExOpStatsTxMultiPkt,
       "ntwsApStatRadioRateExOpStatsTxMultiOctet": ntwsApStatRadioRateExOpStatsTxMultiOctet,
       "ntwsApStatRadioRateExOpStatsRxPkt": ntwsApStatRadioRateExOpStatsRxPkt,
       "ntwsApStatRadioRateExOpStatsRxOctet": ntwsApStatRadioRateExOpStatsRxOctet,
       "ntwsApStatRadioRateExOpStatsUndcrptPkt": ntwsApStatRadioRateExOpStatsUndcrptPkt,
       "ntwsApStatRadioRateExOpStatsUndcrptOctet": ntwsApStatRadioRateExOpStatsUndcrptOctet,
       "ntwsApStatRadioRateExOpStatsPhyErr": ntwsApStatRadioRateExOpStatsPhyErr,
       "ntwsApStatRadioRateExOpStatisticsMacTable": ntwsApStatRadioRateExOpStatisticsMacTable,
       "ntwsApStatRadioRateExOpStatisticsMacEntry": ntwsApStatRadioRateExOpStatisticsMacEntry,
       "ntwsApStatRadioRateExOpStatsMacBaseMac": ntwsApStatRadioRateExOpStatsMacBaseMac,
       "ntwsApStatRadioRateExOpStatsMacRateEx": ntwsApStatRadioRateExOpStatsMacRateEx,
       "ntwsApStatRadioRateExOpStatsMacTxUniPkt": ntwsApStatRadioRateExOpStatsMacTxUniPkt,
       "ntwsApStatRadioRateExOpStatsMacTxUniOctet": ntwsApStatRadioRateExOpStatsMacTxUniOctet,
       "ntwsApStatRadioRateExOpStatsMacTxMultiPkt": ntwsApStatRadioRateExOpStatsMacTxMultiPkt,
       "ntwsApStatRadioRateExOpStatsMacTxMultiOctet": ntwsApStatRadioRateExOpStatsMacTxMultiOctet,
       "ntwsApStatRadioRateExOpStatsMacRxPkt": ntwsApStatRadioRateExOpStatsMacRxPkt,
       "ntwsApStatRadioRateExOpStatsMacRxOctet": ntwsApStatRadioRateExOpStatsMacRxOctet,
       "ntwsApStatRadioRateExOpStatsMacUndcrptPkt": ntwsApStatRadioRateExOpStatsMacUndcrptPkt,
       "ntwsApStatRadioRateExOpStatsMacUndcrptOctet": ntwsApStatRadioRateExOpStatsMacUndcrptOctet,
       "ntwsApStatRadioRateExOpStatsMacPhyErr": ntwsApStatRadioRateExOpStatsMacPhyErr,
       "ntwsApStatusConformance": ntwsApStatusConformance,
       "ntwsApStatusCompliances": ntwsApStatusCompliances,
       "ntwsApStatusCompliance": ntwsApStatusCompliance,
       "ntwsApStatusComplianceRev2": ntwsApStatusComplianceRev2,
       "ntwsApStatusComplianceRev3": ntwsApStatusComplianceRev3,
       "ntwsApStatusComplianceRev4": ntwsApStatusComplianceRev4,
       "ntwsApStatusComplianceRev5": ntwsApStatusComplianceRev5,
       "ntwsApStatusGroups": ntwsApStatusGroups,
       "ntwsApStatusCommonGroup": ntwsApStatusCommonGroup,
       "ntwsApStatusScalarsGroup": ntwsApStatusScalarsGroup,
       "ntwsApStatusApStatusTablesGroup": ntwsApStatusApStatusTablesGroup,
       "ntwsApStatusRadioStatusTablesGroup": ntwsApStatusRadioStatusTablesGroup,
       "ntwsApStatusRadioServiceTablesGroup": ntwsApStatusRadioServiceTablesGroup,
       "ntwsApStatusRadioServiceOpRateSetTablesGroup": ntwsApStatusRadioServiceOpRateSetTablesGroup,
       "ntwsApStatusRadioOpStatisticsTablesGroup": ntwsApStatusRadioOpStatisticsTablesGroup,
       "ntwsApStatusRadioOpStatisticsPerRateTablesGroup": ntwsApStatusRadioOpStatisticsPerRateTablesGroup,
       "ntwsApStatusApStatusVersionsGroup": ntwsApStatusApStatusVersionsGroup,
       "ntwsApStatusApStatusTablesGroupRev2": ntwsApStatusApStatusTablesGroupRev2,
       "ntwsApStatusRadioStatusMaxPowerPhyTypeGroup": ntwsApStatusRadioStatusMaxPowerPhyTypeGroup,
       "ntwsApStatusRadioStatusTablesGroupRev2": ntwsApStatusRadioStatusTablesGroupRev2,
       "ntwsApStatusRadioStatusWideMimoGroup": ntwsApStatusRadioStatusWideMimoGroup,
       "ntwsApStatusRadioOpStatisticsPerRateExTablesGroup": ntwsApStatusRadioOpStatisticsPerRateExTablesGroup,
       "ntwsApStatusApStatusPhysPortNumGroup": ntwsApStatusApStatusPhysPortNumGroup,
       "ntwsApStatusApStatusConnectivityGroup": ntwsApStatusApStatusConnectivityGroup,
       "ntwsApStatusRadioStatusAntennaGroup": ntwsApStatusRadioStatusAntennaGroup,
       "ntwsApStatusRadioOpStatisticsClientAssocGroup": ntwsApStatusRadioOpStatisticsClientAssocGroup,
       "ntwsApStatusRadioOpStatisticsSignErrGroup": ntwsApStatusRadioOpStatisticsSignErrGroup}
)
