# SNMP MIB module (TRAPEZE-NETWORKS-AP-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-AP-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:26 2024
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

(TrpzApAttachType,
 TrpzApFingerprint,
 TrpzApNum,
 TrpzApPortOrDapNum,
 TrpzApSerialNum,
 TrpzApState,
 TrpzChannelNum,
 TrpzPowerLevel,
 TrpzRadioChannelWidth,
 TrpzRadioConfigState,
 TrpzRadioEnable,
 TrpzRadioMimoState,
 TrpzRadioMode,
 TrpzRadioNum,
 TrpzRadioRate,
 TrpzRadioRateEx,
 TrpzRadioType) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-AP-TC",
    "TrpzApAttachType",
    "TrpzApFingerprint",
    "TrpzApNum",
    "TrpzApPortOrDapNum",
    "TrpzApSerialNum",
    "TrpzApState",
    "TrpzChannelNum",
    "TrpzPowerLevel",
    "TrpzRadioChannelWidth",
    "TrpzRadioConfigState",
    "TrpzRadioEnable",
    "TrpzRadioMimoState",
    "TrpzRadioMode",
    "TrpzRadioNum",
    "TrpzRadioRate",
    "TrpzRadioRateEx",
    "TrpzRadioType")

(TrpzPhysPortNumberOrZero,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-BASIC-TC",
    "TrpzPhysPortNumberOrZero")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzApStatusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5)
)
trpzApStatusMib.setRevisions(
        ("2012-02-10 02:30",
         "2011-01-07 02:21",
         "2011-01-05 02:20",
         "2009-11-02 01:53",
         "2009-09-10 01:50",
         "2009-02-13 01:41",
         "2008-12-01 01:15",
         "2008-11-04 01:11",
         "2008-05-22 01:07",
         "2008-05-09 01:04",
         "2008-02-14 01:03",
         "2007-12-07 01:00",
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



class TrpzRadioOpRateSetSingleValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class TrpzRadioOpRateSetMandatory(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )



class TrpzRadioOpRateSetDisabled(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )



# MIB Managed Objects in the order of their OIDs

_TrpzApStatusObjects_ObjectIdentity = ObjectIdentity
trpzApStatusObjects = _TrpzApStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1)
)
_TrpzApStatDataObjects_ObjectIdentity = ObjectIdentity
trpzApStatDataObjects = _TrpzApStatDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1)
)
_TrpzApStatNumAps_Type = Unsigned32
_TrpzApStatNumAps_Object = MibScalar
trpzApStatNumAps = _TrpzApStatNumAps_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 1),
    _TrpzApStatNumAps_Type()
)
trpzApStatNumAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatNumAps.setStatus("current")
_TrpzApStatApStatusTable_Object = MibTable
trpzApStatApStatusTable = _TrpzApStatApStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    trpzApStatApStatusTable.setStatus("current")
_TrpzApStatApStatusEntry_Object = MibTableRow
trpzApStatApStatusEntry = _TrpzApStatApStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1)
)
trpzApStatApStatusEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusSerialNum"),
)
if mibBuilder.loadTexts:
    trpzApStatApStatusEntry.setStatus("current")
_TrpzApStatApStatusSerialNum_Type = TrpzApSerialNum
_TrpzApStatApStatusSerialNum_Object = MibTableColumn
trpzApStatApStatusSerialNum = _TrpzApStatApStatusSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 1),
    _TrpzApStatApStatusSerialNum_Type()
)
trpzApStatApStatusSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatApStatusSerialNum.setStatus("current")
_TrpzApStatApStatusBaseMac_Type = MacAddress
_TrpzApStatApStatusBaseMac_Object = MibTableColumn
trpzApStatApStatusBaseMac = _TrpzApStatApStatusBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 2),
    _TrpzApStatApStatusBaseMac_Type()
)
trpzApStatApStatusBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusBaseMac.setStatus("current")
_TrpzApStatApStatusAttachType_Type = TrpzApAttachType
_TrpzApStatApStatusAttachType_Object = MibTableColumn
trpzApStatApStatusAttachType = _TrpzApStatApStatusAttachType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 3),
    _TrpzApStatApStatusAttachType_Type()
)
trpzApStatApStatusAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusAttachType.setStatus("current")
_TrpzApStatApStatusPortOrDapNum_Type = TrpzApPortOrDapNum
_TrpzApStatApStatusPortOrDapNum_Object = MibTableColumn
trpzApStatApStatusPortOrDapNum = _TrpzApStatApStatusPortOrDapNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 4),
    _TrpzApStatApStatusPortOrDapNum_Type()
)
trpzApStatApStatusPortOrDapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusPortOrDapNum.setStatus("obsolete")
_TrpzApStatApStatusApState_Type = TrpzApState
_TrpzApStatApStatusApState_Object = MibTableColumn
trpzApStatApStatusApState = _TrpzApStatApStatusApState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 5),
    _TrpzApStatApStatusApState_Type()
)
trpzApStatApStatusApState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusApState.setStatus("current")
_TrpzApStatApStatusModel_Type = DisplayString
_TrpzApStatApStatusModel_Object = MibTableColumn
trpzApStatApStatusModel = _TrpzApStatApStatusModel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 6),
    _TrpzApStatApStatusModel_Type()
)
trpzApStatApStatusModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusModel.setStatus("current")
_TrpzApStatApStatusFingerprint_Type = TrpzApFingerprint
_TrpzApStatApStatusFingerprint_Object = MibTableColumn
trpzApStatApStatusFingerprint = _TrpzApStatApStatusFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 7),
    _TrpzApStatApStatusFingerprint_Type()
)
trpzApStatApStatusFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusFingerprint.setStatus("current")
_TrpzApStatApStatusApName_Type = DisplayString
_TrpzApStatApStatusApName_Object = MibTableColumn
trpzApStatApStatusApName = _TrpzApStatApStatusApName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 8),
    _TrpzApStatApStatusApName_Type()
)
trpzApStatApStatusApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusApName.setStatus("current")
_TrpzApStatApStatusVlan_Type = DisplayString
_TrpzApStatApStatusVlan_Object = MibTableColumn
trpzApStatApStatusVlan = _TrpzApStatApStatusVlan_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 9),
    _TrpzApStatApStatusVlan_Type()
)
trpzApStatApStatusVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusVlan.setStatus("current")
_TrpzApStatApStatusIpAddress_Type = IpAddress
_TrpzApStatApStatusIpAddress_Object = MibTableColumn
trpzApStatApStatusIpAddress = _TrpzApStatApStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 10),
    _TrpzApStatApStatusIpAddress_Type()
)
trpzApStatApStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusIpAddress.setStatus("current")
_TrpzApStatApStatusUptimeSecs_Type = Unsigned32
_TrpzApStatApStatusUptimeSecs_Object = MibTableColumn
trpzApStatApStatusUptimeSecs = _TrpzApStatApStatusUptimeSecs_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 11),
    _TrpzApStatApStatusUptimeSecs_Type()
)
trpzApStatApStatusUptimeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusUptimeSecs.setStatus("current")
_TrpzApStatApStatusCpuInfo_Type = DisplayString
_TrpzApStatApStatusCpuInfo_Object = MibTableColumn
trpzApStatApStatusCpuInfo = _TrpzApStatApStatusCpuInfo_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 12),
    _TrpzApStatApStatusCpuInfo_Type()
)
trpzApStatApStatusCpuInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusCpuInfo.setStatus("current")
_TrpzApStatApStatusManufacturerId_Type = DisplayString
_TrpzApStatApStatusManufacturerId_Object = MibTableColumn
trpzApStatApStatusManufacturerId = _TrpzApStatApStatusManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 13),
    _TrpzApStatApStatusManufacturerId_Type()
)
trpzApStatApStatusManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusManufacturerId.setStatus("current")
_TrpzApStatApStatusRamBytes_Type = Unsigned32
_TrpzApStatApStatusRamBytes_Object = MibTableColumn
trpzApStatApStatusRamBytes = _TrpzApStatApStatusRamBytes_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 14),
    _TrpzApStatApStatusRamBytes_Type()
)
trpzApStatApStatusRamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusRamBytes.setStatus("current")
_TrpzApStatApStatusHardwareRev_Type = DisplayString
_TrpzApStatApStatusHardwareRev_Object = MibTableColumn
trpzApStatApStatusHardwareRev = _TrpzApStatApStatusHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 15),
    _TrpzApStatApStatusHardwareRev_Type()
)
trpzApStatApStatusHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusHardwareRev.setStatus("current")
_TrpzApStatApStatusClientSessions_Type = Unsigned32
_TrpzApStatApStatusClientSessions_Object = MibTableColumn
trpzApStatApStatusClientSessions = _TrpzApStatApStatusClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 16),
    _TrpzApStatApStatusClientSessions_Type()
)
trpzApStatApStatusClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusClientSessions.setStatus("current")
_TrpzApStatApStatusSoftwareVer_Type = DisplayString
_TrpzApStatApStatusSoftwareVer_Object = MibTableColumn
trpzApStatApStatusSoftwareVer = _TrpzApStatApStatusSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 17),
    _TrpzApStatApStatusSoftwareVer_Type()
)
trpzApStatApStatusSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusSoftwareVer.setStatus("current")
_TrpzApStatApStatusBootVer_Type = DisplayString
_TrpzApStatApStatusBootVer_Object = MibTableColumn
trpzApStatApStatusBootVer = _TrpzApStatApStatusBootVer_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 18),
    _TrpzApStatApStatusBootVer_Type()
)
trpzApStatApStatusBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusBootVer.setStatus("current")
_TrpzApStatApStatusApNum_Type = TrpzApNum
_TrpzApStatApStatusApNum_Object = MibTableColumn
trpzApStatApStatusApNum = _TrpzApStatApStatusApNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 19),
    _TrpzApStatApStatusApNum_Type()
)
trpzApStatApStatusApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusApNum.setStatus("current")
_TrpzApStatApStatusPhysPortNum_Type = TrpzPhysPortNumberOrZero
_TrpzApStatApStatusPhysPortNum_Object = MibTableColumn
trpzApStatApStatusPhysPortNum = _TrpzApStatApStatusPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 20),
    _TrpzApStatApStatusPhysPortNum_Type()
)
trpzApStatApStatusPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusPhysPortNum.setStatus("current")
_TrpzApStatApStatusIpNetmask_Type = IpAddress
_TrpzApStatApStatusIpNetmask_Object = MibTableColumn
trpzApStatApStatusIpNetmask = _TrpzApStatApStatusIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 21),
    _TrpzApStatApStatusIpNetmask_Type()
)
trpzApStatApStatusIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusIpNetmask.setStatus("current")
_TrpzApStatApStatusWiredIfNumber_Type = Unsigned32
_TrpzApStatApStatusWiredIfNumber_Object = MibTableColumn
trpzApStatApStatusWiredIfNumber = _TrpzApStatApStatusWiredIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 2, 1, 22),
    _TrpzApStatApStatusWiredIfNumber_Type()
)
trpzApStatApStatusWiredIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusWiredIfNumber.setStatus("current")
_TrpzApStatApStatusMacTable_Object = MibTable
trpzApStatApStatusMacTable = _TrpzApStatApStatusMacTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    trpzApStatApStatusMacTable.setStatus("current")
_TrpzApStatApStatusMacEntry_Object = MibTableRow
trpzApStatApStatusMacEntry = _TrpzApStatApStatusMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1)
)
trpzApStatApStatusMacEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacBaseMac"),
)
if mibBuilder.loadTexts:
    trpzApStatApStatusMacEntry.setStatus("current")
_TrpzApStatApStatusMacBaseMac_Type = MacAddress
_TrpzApStatApStatusMacBaseMac_Object = MibTableColumn
trpzApStatApStatusMacBaseMac = _TrpzApStatApStatusMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 1),
    _TrpzApStatApStatusMacBaseMac_Type()
)
trpzApStatApStatusMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacBaseMac.setStatus("current")
_TrpzApStatApStatusMacSerialNum_Type = TrpzApSerialNum
_TrpzApStatApStatusMacSerialNum_Object = MibTableColumn
trpzApStatApStatusMacSerialNum = _TrpzApStatApStatusMacSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 2),
    _TrpzApStatApStatusMacSerialNum_Type()
)
trpzApStatApStatusMacSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacSerialNum.setStatus("current")
_TrpzApStatApStatusMacAttachType_Type = TrpzApAttachType
_TrpzApStatApStatusMacAttachType_Object = MibTableColumn
trpzApStatApStatusMacAttachType = _TrpzApStatApStatusMacAttachType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 3),
    _TrpzApStatApStatusMacAttachType_Type()
)
trpzApStatApStatusMacAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacAttachType.setStatus("current")
_TrpzApStatApStatusMacPortOrDapNum_Type = TrpzApPortOrDapNum
_TrpzApStatApStatusMacPortOrDapNum_Object = MibTableColumn
trpzApStatApStatusMacPortOrDapNum = _TrpzApStatApStatusMacPortOrDapNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 4),
    _TrpzApStatApStatusMacPortOrDapNum_Type()
)
trpzApStatApStatusMacPortOrDapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacPortOrDapNum.setStatus("obsolete")
_TrpzApStatApStatusMacApState_Type = TrpzApState
_TrpzApStatApStatusMacApState_Object = MibTableColumn
trpzApStatApStatusMacApState = _TrpzApStatApStatusMacApState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 5),
    _TrpzApStatApStatusMacApState_Type()
)
trpzApStatApStatusMacApState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacApState.setStatus("current")
_TrpzApStatApStatusMacModel_Type = DisplayString
_TrpzApStatApStatusMacModel_Object = MibTableColumn
trpzApStatApStatusMacModel = _TrpzApStatApStatusMacModel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 6),
    _TrpzApStatApStatusMacModel_Type()
)
trpzApStatApStatusMacModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacModel.setStatus("current")
_TrpzApStatApStatusMacFingerprint_Type = TrpzApFingerprint
_TrpzApStatApStatusMacFingerprint_Object = MibTableColumn
trpzApStatApStatusMacFingerprint = _TrpzApStatApStatusMacFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 7),
    _TrpzApStatApStatusMacFingerprint_Type()
)
trpzApStatApStatusMacFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacFingerprint.setStatus("current")
_TrpzApStatApStatusMacApName_Type = DisplayString
_TrpzApStatApStatusMacApName_Object = MibTableColumn
trpzApStatApStatusMacApName = _TrpzApStatApStatusMacApName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 8),
    _TrpzApStatApStatusMacApName_Type()
)
trpzApStatApStatusMacApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacApName.setStatus("current")
_TrpzApStatApStatusMacVlan_Type = DisplayString
_TrpzApStatApStatusMacVlan_Object = MibTableColumn
trpzApStatApStatusMacVlan = _TrpzApStatApStatusMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 9),
    _TrpzApStatApStatusMacVlan_Type()
)
trpzApStatApStatusMacVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacVlan.setStatus("current")
_TrpzApStatApStatusMacIpAddress_Type = IpAddress
_TrpzApStatApStatusMacIpAddress_Object = MibTableColumn
trpzApStatApStatusMacIpAddress = _TrpzApStatApStatusMacIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 10),
    _TrpzApStatApStatusMacIpAddress_Type()
)
trpzApStatApStatusMacIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacIpAddress.setStatus("current")
_TrpzApStatApStatusMacUptimeSecs_Type = Unsigned32
_TrpzApStatApStatusMacUptimeSecs_Object = MibTableColumn
trpzApStatApStatusMacUptimeSecs = _TrpzApStatApStatusMacUptimeSecs_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 11),
    _TrpzApStatApStatusMacUptimeSecs_Type()
)
trpzApStatApStatusMacUptimeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacUptimeSecs.setStatus("current")
_TrpzApStatApStatusMacCpuInfo_Type = DisplayString
_TrpzApStatApStatusMacCpuInfo_Object = MibTableColumn
trpzApStatApStatusMacCpuInfo = _TrpzApStatApStatusMacCpuInfo_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 12),
    _TrpzApStatApStatusMacCpuInfo_Type()
)
trpzApStatApStatusMacCpuInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacCpuInfo.setStatus("current")
_TrpzApStatApStatusMacManufacturerId_Type = DisplayString
_TrpzApStatApStatusMacManufacturerId_Object = MibTableColumn
trpzApStatApStatusMacManufacturerId = _TrpzApStatApStatusMacManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 13),
    _TrpzApStatApStatusMacManufacturerId_Type()
)
trpzApStatApStatusMacManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacManufacturerId.setStatus("current")
_TrpzApStatApStatusMacRamBytes_Type = Unsigned32
_TrpzApStatApStatusMacRamBytes_Object = MibTableColumn
trpzApStatApStatusMacRamBytes = _TrpzApStatApStatusMacRamBytes_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 14),
    _TrpzApStatApStatusMacRamBytes_Type()
)
trpzApStatApStatusMacRamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacRamBytes.setStatus("current")
_TrpzApStatApStatusMacHardwareRev_Type = DisplayString
_TrpzApStatApStatusMacHardwareRev_Object = MibTableColumn
trpzApStatApStatusMacHardwareRev = _TrpzApStatApStatusMacHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 15),
    _TrpzApStatApStatusMacHardwareRev_Type()
)
trpzApStatApStatusMacHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacHardwareRev.setStatus("current")
_TrpzApStatApStatusMacClientSessions_Type = Unsigned32
_TrpzApStatApStatusMacClientSessions_Object = MibTableColumn
trpzApStatApStatusMacClientSessions = _TrpzApStatApStatusMacClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 16),
    _TrpzApStatApStatusMacClientSessions_Type()
)
trpzApStatApStatusMacClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacClientSessions.setStatus("current")
_TrpzApStatApStatusMacSoftwareVer_Type = DisplayString
_TrpzApStatApStatusMacSoftwareVer_Object = MibTableColumn
trpzApStatApStatusMacSoftwareVer = _TrpzApStatApStatusMacSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 17),
    _TrpzApStatApStatusMacSoftwareVer_Type()
)
trpzApStatApStatusMacSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacSoftwareVer.setStatus("current")
_TrpzApStatApStatusMacBootVer_Type = DisplayString
_TrpzApStatApStatusMacBootVer_Object = MibTableColumn
trpzApStatApStatusMacBootVer = _TrpzApStatApStatusMacBootVer_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 18),
    _TrpzApStatApStatusMacBootVer_Type()
)
trpzApStatApStatusMacBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacBootVer.setStatus("current")
_TrpzApStatApStatusMacApNum_Type = TrpzApNum
_TrpzApStatApStatusMacApNum_Object = MibTableColumn
trpzApStatApStatusMacApNum = _TrpzApStatApStatusMacApNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 19),
    _TrpzApStatApStatusMacApNum_Type()
)
trpzApStatApStatusMacApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacApNum.setStatus("current")
_TrpzApStatApStatusMacPhysPortNum_Type = TrpzPhysPortNumberOrZero
_TrpzApStatApStatusMacPhysPortNum_Object = MibTableColumn
trpzApStatApStatusMacPhysPortNum = _TrpzApStatApStatusMacPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 20),
    _TrpzApStatApStatusMacPhysPortNum_Type()
)
trpzApStatApStatusMacPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacPhysPortNum.setStatus("current")
_TrpzApStatApStatusMacIpNetmask_Type = IpAddress
_TrpzApStatApStatusMacIpNetmask_Object = MibTableColumn
trpzApStatApStatusMacIpNetmask = _TrpzApStatApStatusMacIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 21),
    _TrpzApStatApStatusMacIpNetmask_Type()
)
trpzApStatApStatusMacIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacIpNetmask.setStatus("current")
_TrpzApStatApStatusMacWiredIfNumber_Type = Unsigned32
_TrpzApStatApStatusMacWiredIfNumber_Object = MibTableColumn
trpzApStatApStatusMacWiredIfNumber = _TrpzApStatApStatusMacWiredIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 3, 1, 22),
    _TrpzApStatApStatusMacWiredIfNumber_Type()
)
trpzApStatApStatusMacWiredIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatApStatusMacWiredIfNumber.setStatus("current")
_TrpzApStatRadioStatusTable_Object = MibTable
trpzApStatRadioStatusTable = _TrpzApStatRadioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    trpzApStatRadioStatusTable.setStatus("current")
_TrpzApStatRadioStatusEntry_Object = MibTableRow
trpzApStatRadioStatusEntry = _TrpzApStatRadioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1)
)
trpzApStatRadioStatusEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusApSerialNum"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioNum"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioStatusEntry.setStatus("current")
_TrpzApStatRadioStatusApSerialNum_Type = TrpzApSerialNum
_TrpzApStatRadioStatusApSerialNum_Object = MibTableColumn
trpzApStatRadioStatusApSerialNum = _TrpzApStatRadioStatusApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 1),
    _TrpzApStatRadioStatusApSerialNum_Type()
)
trpzApStatRadioStatusApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusApSerialNum.setStatus("current")
_TrpzApStatRadioStatusRadioNum_Type = TrpzRadioNum
_TrpzApStatRadioStatusRadioNum_Object = MibTableColumn
trpzApStatRadioStatusRadioNum = _TrpzApStatRadioStatusRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 2),
    _TrpzApStatRadioStatusRadioNum_Type()
)
trpzApStatRadioStatusRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusRadioNum.setStatus("current")
_TrpzApStatRadioStatusBaseMac_Type = MacAddress
_TrpzApStatRadioStatusBaseMac_Object = MibTableColumn
trpzApStatRadioStatusBaseMac = _TrpzApStatRadioStatusBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 3),
    _TrpzApStatRadioStatusBaseMac_Type()
)
trpzApStatRadioStatusBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusBaseMac.setStatus("current")
_TrpzApStatRadioStatusEnable_Type = TrpzRadioEnable
_TrpzApStatRadioStatusEnable_Object = MibTableColumn
trpzApStatRadioStatusEnable = _TrpzApStatRadioStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 4),
    _TrpzApStatRadioStatusEnable_Type()
)
trpzApStatRadioStatusEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusEnable.setStatus("obsolete")
_TrpzApStatRadioStatusRadioConfigState_Type = TrpzRadioConfigState
_TrpzApStatRadioStatusRadioConfigState_Object = MibTableColumn
trpzApStatRadioStatusRadioConfigState = _TrpzApStatRadioStatusRadioConfigState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 5),
    _TrpzApStatRadioStatusRadioConfigState_Type()
)
trpzApStatRadioStatusRadioConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusRadioConfigState.setStatus("current")
_TrpzApStatRadioStatusCurrentPowerLevel_Type = TrpzPowerLevel
_TrpzApStatRadioStatusCurrentPowerLevel_Object = MibTableColumn
trpzApStatRadioStatusCurrentPowerLevel = _TrpzApStatRadioStatusCurrentPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 6),
    _TrpzApStatRadioStatusCurrentPowerLevel_Type()
)
trpzApStatRadioStatusCurrentPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusCurrentPowerLevel.setStatus("current")
_TrpzApStatRadioStatusCurrentChannelNum_Type = TrpzChannelNum
_TrpzApStatRadioStatusCurrentChannelNum_Object = MibTableColumn
trpzApStatRadioStatusCurrentChannelNum = _TrpzApStatRadioStatusCurrentChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 7),
    _TrpzApStatRadioStatusCurrentChannelNum_Type()
)
trpzApStatRadioStatusCurrentChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusCurrentChannelNum.setStatus("current")
_TrpzApStatRadioStatusClientSessions_Type = Unsigned32
_TrpzApStatRadioStatusClientSessions_Object = MibTableColumn
trpzApStatRadioStatusClientSessions = _TrpzApStatRadioStatusClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 8),
    _TrpzApStatRadioStatusClientSessions_Type()
)
trpzApStatRadioStatusClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusClientSessions.setStatus("current")
_TrpzApStatRadioStatusMaxPowerLevel_Type = TrpzPowerLevel
_TrpzApStatRadioStatusMaxPowerLevel_Object = MibTableColumn
trpzApStatRadioStatusMaxPowerLevel = _TrpzApStatRadioStatusMaxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 9),
    _TrpzApStatRadioStatusMaxPowerLevel_Type()
)
trpzApStatRadioStatusMaxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMaxPowerLevel.setStatus("current")
_TrpzApStatRadioStatusRadioPhyType_Type = TrpzRadioType
_TrpzApStatRadioStatusRadioPhyType_Object = MibTableColumn
trpzApStatRadioStatusRadioPhyType = _TrpzApStatRadioStatusRadioPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 10),
    _TrpzApStatRadioStatusRadioPhyType_Type()
)
trpzApStatRadioStatusRadioPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusRadioPhyType.setStatus("current")
_TrpzApStatRadioStatusRadioMode_Type = TrpzRadioMode
_TrpzApStatRadioStatusRadioMode_Object = MibTableColumn
trpzApStatRadioStatusRadioMode = _TrpzApStatRadioStatusRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 11),
    _TrpzApStatRadioStatusRadioMode_Type()
)
trpzApStatRadioStatusRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusRadioMode.setStatus("current")
_TrpzApStatRadioStatusRadioChannelWidth_Type = TrpzRadioChannelWidth
_TrpzApStatRadioStatusRadioChannelWidth_Object = MibTableColumn
trpzApStatRadioStatusRadioChannelWidth = _TrpzApStatRadioStatusRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 12),
    _TrpzApStatRadioStatusRadioChannelWidth_Type()
)
trpzApStatRadioStatusRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusRadioChannelWidth.setStatus("current")
_TrpzApStatRadioStatusRadioMimoState_Type = TrpzRadioMimoState
_TrpzApStatRadioStatusRadioMimoState_Object = MibTableColumn
trpzApStatRadioStatusRadioMimoState = _TrpzApStatRadioStatusRadioMimoState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 13),
    _TrpzApStatRadioStatusRadioMimoState_Type()
)
trpzApStatRadioStatusRadioMimoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusRadioMimoState.setStatus("obsolete")
_TrpzApStatRadioStatusMinPowerLevel_Type = TrpzPowerLevel
_TrpzApStatRadioStatusMinPowerLevel_Object = MibTableColumn
trpzApStatRadioStatusMinPowerLevel = _TrpzApStatRadioStatusMinPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 14),
    _TrpzApStatRadioStatusMinPowerLevel_Type()
)
trpzApStatRadioStatusMinPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMinPowerLevel.setStatus("current")
_TrpzApStatRadioStatusRadioMimoRxChains_Type = Unsigned32
_TrpzApStatRadioStatusRadioMimoRxChains_Object = MibTableColumn
trpzApStatRadioStatusRadioMimoRxChains = _TrpzApStatRadioStatusRadioMimoRxChains_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 15),
    _TrpzApStatRadioStatusRadioMimoRxChains_Type()
)
trpzApStatRadioStatusRadioMimoRxChains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusRadioMimoRxChains.setStatus("current")
_TrpzApStatRadioStatusRadioMimoTxChains_Type = Unsigned32
_TrpzApStatRadioStatusRadioMimoTxChains_Object = MibTableColumn
trpzApStatRadioStatusRadioMimoTxChains = _TrpzApStatRadioStatusRadioMimoTxChains_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 16),
    _TrpzApStatRadioStatusRadioMimoTxChains_Type()
)
trpzApStatRadioStatusRadioMimoTxChains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusRadioMimoTxChains.setStatus("current")
_TrpzApStatRadioStatusSpectralDataCollect_Type = TruthValue
_TrpzApStatRadioStatusSpectralDataCollect_Object = MibTableColumn
trpzApStatRadioStatusSpectralDataCollect = _TrpzApStatRadioStatusSpectralDataCollect_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 4, 1, 17),
    _TrpzApStatRadioStatusSpectralDataCollect_Type()
)
trpzApStatRadioStatusSpectralDataCollect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusSpectralDataCollect.setStatus("current")
_TrpzApStatRadioStatusMacTable_Object = MibTable
trpzApStatRadioStatusMacTable = _TrpzApStatRadioStatusMacTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacTable.setStatus("current")
_TrpzApStatRadioStatusMacEntry_Object = MibTableRow
trpzApStatRadioStatusMacEntry = _TrpzApStatRadioStatusMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1)
)
trpzApStatRadioStatusMacEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacBaseMac"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacEntry.setStatus("current")
_TrpzApStatRadioStatusMacBaseMac_Type = MacAddress
_TrpzApStatRadioStatusMacBaseMac_Object = MibTableColumn
trpzApStatRadioStatusMacBaseMac = _TrpzApStatRadioStatusMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 1),
    _TrpzApStatRadioStatusMacBaseMac_Type()
)
trpzApStatRadioStatusMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacBaseMac.setStatus("current")
_TrpzApStatRadioStatusMacApSerialNum_Type = TrpzApSerialNum
_TrpzApStatRadioStatusMacApSerialNum_Object = MibTableColumn
trpzApStatRadioStatusMacApSerialNum = _TrpzApStatRadioStatusMacApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 2),
    _TrpzApStatRadioStatusMacApSerialNum_Type()
)
trpzApStatRadioStatusMacApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacApSerialNum.setStatus("current")
_TrpzApStatRadioStatusMacRadioNum_Type = TrpzRadioNum
_TrpzApStatRadioStatusMacRadioNum_Object = MibTableColumn
trpzApStatRadioStatusMacRadioNum = _TrpzApStatRadioStatusMacRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 3),
    _TrpzApStatRadioStatusMacRadioNum_Type()
)
trpzApStatRadioStatusMacRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacRadioNum.setStatus("current")
_TrpzApStatRadioStatusMacEnable_Type = TrpzRadioEnable
_TrpzApStatRadioStatusMacEnable_Object = MibTableColumn
trpzApStatRadioStatusMacEnable = _TrpzApStatRadioStatusMacEnable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 4),
    _TrpzApStatRadioStatusMacEnable_Type()
)
trpzApStatRadioStatusMacEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacEnable.setStatus("obsolete")
_TrpzApStatRadioStatusMacRadioConfigState_Type = TrpzRadioConfigState
_TrpzApStatRadioStatusMacRadioConfigState_Object = MibTableColumn
trpzApStatRadioStatusMacRadioConfigState = _TrpzApStatRadioStatusMacRadioConfigState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 5),
    _TrpzApStatRadioStatusMacRadioConfigState_Type()
)
trpzApStatRadioStatusMacRadioConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacRadioConfigState.setStatus("current")
_TrpzApStatRadioStatusMacCurrentPowerLevel_Type = TrpzPowerLevel
_TrpzApStatRadioStatusMacCurrentPowerLevel_Object = MibTableColumn
trpzApStatRadioStatusMacCurrentPowerLevel = _TrpzApStatRadioStatusMacCurrentPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 6),
    _TrpzApStatRadioStatusMacCurrentPowerLevel_Type()
)
trpzApStatRadioStatusMacCurrentPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacCurrentPowerLevel.setStatus("current")
_TrpzApStatRadioStatusMacCurrentChannelNum_Type = TrpzChannelNum
_TrpzApStatRadioStatusMacCurrentChannelNum_Object = MibTableColumn
trpzApStatRadioStatusMacCurrentChannelNum = _TrpzApStatRadioStatusMacCurrentChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 7),
    _TrpzApStatRadioStatusMacCurrentChannelNum_Type()
)
trpzApStatRadioStatusMacCurrentChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacCurrentChannelNum.setStatus("current")
_TrpzApStatRadioStatusMacClientSessions_Type = Unsigned32
_TrpzApStatRadioStatusMacClientSessions_Object = MibTableColumn
trpzApStatRadioStatusMacClientSessions = _TrpzApStatRadioStatusMacClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 8),
    _TrpzApStatRadioStatusMacClientSessions_Type()
)
trpzApStatRadioStatusMacClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacClientSessions.setStatus("current")
_TrpzApStatRadioStatusMacMaxPowerLevel_Type = TrpzPowerLevel
_TrpzApStatRadioStatusMacMaxPowerLevel_Object = MibTableColumn
trpzApStatRadioStatusMacMaxPowerLevel = _TrpzApStatRadioStatusMacMaxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 9),
    _TrpzApStatRadioStatusMacMaxPowerLevel_Type()
)
trpzApStatRadioStatusMacMaxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacMaxPowerLevel.setStatus("current")
_TrpzApStatRadioStatusMacRadioPhyType_Type = TrpzRadioType
_TrpzApStatRadioStatusMacRadioPhyType_Object = MibTableColumn
trpzApStatRadioStatusMacRadioPhyType = _TrpzApStatRadioStatusMacRadioPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 10),
    _TrpzApStatRadioStatusMacRadioPhyType_Type()
)
trpzApStatRadioStatusMacRadioPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacRadioPhyType.setStatus("current")
_TrpzApStatRadioStatusMacRadioMode_Type = TrpzRadioMode
_TrpzApStatRadioStatusMacRadioMode_Object = MibTableColumn
trpzApStatRadioStatusMacRadioMode = _TrpzApStatRadioStatusMacRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 11),
    _TrpzApStatRadioStatusMacRadioMode_Type()
)
trpzApStatRadioStatusMacRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacRadioMode.setStatus("current")
_TrpzApStatRadioStatusMacRadioChannelWidth_Type = TrpzRadioChannelWidth
_TrpzApStatRadioStatusMacRadioChannelWidth_Object = MibTableColumn
trpzApStatRadioStatusMacRadioChannelWidth = _TrpzApStatRadioStatusMacRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 12),
    _TrpzApStatRadioStatusMacRadioChannelWidth_Type()
)
trpzApStatRadioStatusMacRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacRadioChannelWidth.setStatus("current")
_TrpzApStatRadioStatusMacRadioMimoState_Type = TrpzRadioMimoState
_TrpzApStatRadioStatusMacRadioMimoState_Object = MibTableColumn
trpzApStatRadioStatusMacRadioMimoState = _TrpzApStatRadioStatusMacRadioMimoState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 13),
    _TrpzApStatRadioStatusMacRadioMimoState_Type()
)
trpzApStatRadioStatusMacRadioMimoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacRadioMimoState.setStatus("obsolete")
_TrpzApStatRadioStatusMacMinPowerLevel_Type = TrpzPowerLevel
_TrpzApStatRadioStatusMacMinPowerLevel_Object = MibTableColumn
trpzApStatRadioStatusMacMinPowerLevel = _TrpzApStatRadioStatusMacMinPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 14),
    _TrpzApStatRadioStatusMacMinPowerLevel_Type()
)
trpzApStatRadioStatusMacMinPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacMinPowerLevel.setStatus("current")
_TrpzApStatRadioStatusMacRadioMimoRxChains_Type = Unsigned32
_TrpzApStatRadioStatusMacRadioMimoRxChains_Object = MibTableColumn
trpzApStatRadioStatusMacRadioMimoRxChains = _TrpzApStatRadioStatusMacRadioMimoRxChains_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 15),
    _TrpzApStatRadioStatusMacRadioMimoRxChains_Type()
)
trpzApStatRadioStatusMacRadioMimoRxChains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacRadioMimoRxChains.setStatus("current")
_TrpzApStatRadioStatusMacRadioMimoTxChains_Type = Unsigned32
_TrpzApStatRadioStatusMacRadioMimoTxChains_Object = MibTableColumn
trpzApStatRadioStatusMacRadioMimoTxChains = _TrpzApStatRadioStatusMacRadioMimoTxChains_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 16),
    _TrpzApStatRadioStatusMacRadioMimoTxChains_Type()
)
trpzApStatRadioStatusMacRadioMimoTxChains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacRadioMimoTxChains.setStatus("current")
_TrpzApStatRadioStatusMacSpectralDataCollect_Type = TruthValue
_TrpzApStatRadioStatusMacSpectralDataCollect_Object = MibTableColumn
trpzApStatRadioStatusMacSpectralDataCollect = _TrpzApStatRadioStatusMacSpectralDataCollect_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 5, 1, 17),
    _TrpzApStatRadioStatusMacSpectralDataCollect_Type()
)
trpzApStatRadioStatusMacSpectralDataCollect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioStatusMacSpectralDataCollect.setStatus("current")
_TrpzApStatRadioServiceTable_Object = MibTable
trpzApStatRadioServiceTable = _TrpzApStatRadioServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    trpzApStatRadioServiceTable.setStatus("current")
_TrpzApStatRadioServiceEntry_Object = MibTableRow
trpzApStatRadioServiceEntry = _TrpzApStatRadioServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 6, 1)
)
trpzApStatRadioServiceEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServApSerialNum"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServRadioNum"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServSsid"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioServiceEntry.setStatus("current")
_TrpzApStatRadioServApSerialNum_Type = TrpzApSerialNum
_TrpzApStatRadioServApSerialNum_Object = MibTableColumn
trpzApStatRadioServApSerialNum = _TrpzApStatRadioServApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 6, 1, 1),
    _TrpzApStatRadioServApSerialNum_Type()
)
trpzApStatRadioServApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioServApSerialNum.setStatus("current")
_TrpzApStatRadioServRadioNum_Type = TrpzRadioNum
_TrpzApStatRadioServRadioNum_Object = MibTableColumn
trpzApStatRadioServRadioNum = _TrpzApStatRadioServRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 6, 1, 2),
    _TrpzApStatRadioServRadioNum_Type()
)
trpzApStatRadioServRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioServRadioNum.setStatus("current")


class _TrpzApStatRadioServSsid_Type(DisplayString):
    """Custom type trpzApStatRadioServSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzApStatRadioServSsid_Type.__name__ = "DisplayString"
_TrpzApStatRadioServSsid_Object = MibTableColumn
trpzApStatRadioServSsid = _TrpzApStatRadioServSsid_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 6, 1, 3),
    _TrpzApStatRadioServSsid_Type()
)
trpzApStatRadioServSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioServSsid.setStatus("current")
_TrpzApStatRadioServBssid_Type = MacAddress
_TrpzApStatRadioServBssid_Object = MibTableColumn
trpzApStatRadioServBssid = _TrpzApStatRadioServBssid_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 6, 1, 4),
    _TrpzApStatRadioServBssid_Type()
)
trpzApStatRadioServBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioServBssid.setStatus("current")
_TrpzApStatRadioServServiceProfileName_Type = DisplayString
_TrpzApStatRadioServServiceProfileName_Object = MibTableColumn
trpzApStatRadioServServiceProfileName = _TrpzApStatRadioServServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 6, 1, 5),
    _TrpzApStatRadioServServiceProfileName_Type()
)
trpzApStatRadioServServiceProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioServServiceProfileName.setStatus("current")
_TrpzApStatRadioServiceMacTable_Object = MibTable
trpzApStatRadioServiceMacTable = _TrpzApStatRadioServiceMacTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    trpzApStatRadioServiceMacTable.setStatus("current")
_TrpzApStatRadioServiceMacEntry_Object = MibTableRow
trpzApStatRadioServiceMacEntry = _TrpzApStatRadioServiceMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 7, 1)
)
trpzApStatRadioServiceMacEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServMacBssid"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioServiceMacEntry.setStatus("current")
_TrpzApStatRadioServMacBssid_Type = MacAddress
_TrpzApStatRadioServMacBssid_Object = MibTableColumn
trpzApStatRadioServMacBssid = _TrpzApStatRadioServMacBssid_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 7, 1, 1),
    _TrpzApStatRadioServMacBssid_Type()
)
trpzApStatRadioServMacBssid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioServMacBssid.setStatus("current")
_TrpzApStatRadioServMacApSerialNum_Type = TrpzApSerialNum
_TrpzApStatRadioServMacApSerialNum_Object = MibTableColumn
trpzApStatRadioServMacApSerialNum = _TrpzApStatRadioServMacApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 7, 1, 2),
    _TrpzApStatRadioServMacApSerialNum_Type()
)
trpzApStatRadioServMacApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioServMacApSerialNum.setStatus("current")
_TrpzApStatRadioServMacRadioNum_Type = TrpzRadioNum
_TrpzApStatRadioServMacRadioNum_Object = MibTableColumn
trpzApStatRadioServMacRadioNum = _TrpzApStatRadioServMacRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 7, 1, 3),
    _TrpzApStatRadioServMacRadioNum_Type()
)
trpzApStatRadioServMacRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioServMacRadioNum.setStatus("current")


class _TrpzApStatRadioServMacSsid_Type(DisplayString):
    """Custom type trpzApStatRadioServMacSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzApStatRadioServMacSsid_Type.__name__ = "DisplayString"
_TrpzApStatRadioServMacSsid_Object = MibTableColumn
trpzApStatRadioServMacSsid = _TrpzApStatRadioServMacSsid_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 7, 1, 4),
    _TrpzApStatRadioServMacSsid_Type()
)
trpzApStatRadioServMacSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioServMacSsid.setStatus("current")
_TrpzApStatRadioServMacServiceProfileName_Type = DisplayString
_TrpzApStatRadioServMacServiceProfileName_Object = MibTableColumn
trpzApStatRadioServMacServiceProfileName = _TrpzApStatRadioServMacServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 7, 1, 5),
    _TrpzApStatRadioServMacServiceProfileName_Type()
)
trpzApStatRadioServMacServiceProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioServMacServiceProfileName.setStatus("current")
_TrpzApStatRadioServiceOpRateSetTable_Object = MibTable
trpzApStatRadioServiceOpRateSetTable = _TrpzApStatRadioServiceOpRateSetTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    trpzApStatRadioServiceOpRateSetTable.setStatus("current")
_TrpzApStatRadioServiceOpRateSetEntry_Object = MibTableRow
trpzApStatRadioServiceOpRateSetEntry = _TrpzApStatRadioServiceOpRateSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 8, 1)
)
trpzApStatRadioServiceOpRateSetEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetApSerialNum"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetRadioNum"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetSsid"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioServiceOpRateSetEntry.setStatus("current")
_TrpzApStatRadioSORSetApSerialNum_Type = TrpzApSerialNum
_TrpzApStatRadioSORSetApSerialNum_Object = MibTableColumn
trpzApStatRadioSORSetApSerialNum = _TrpzApStatRadioSORSetApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 8, 1, 1),
    _TrpzApStatRadioSORSetApSerialNum_Type()
)
trpzApStatRadioSORSetApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetApSerialNum.setStatus("current")
_TrpzApStatRadioSORSetRadioNum_Type = TrpzRadioNum
_TrpzApStatRadioSORSetRadioNum_Object = MibTableColumn
trpzApStatRadioSORSetRadioNum = _TrpzApStatRadioSORSetRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 8, 1, 2),
    _TrpzApStatRadioSORSetRadioNum_Type()
)
trpzApStatRadioSORSetRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetRadioNum.setStatus("current")


class _TrpzApStatRadioSORSetSsid_Type(DisplayString):
    """Custom type trpzApStatRadioSORSetSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzApStatRadioSORSetSsid_Type.__name__ = "DisplayString"
_TrpzApStatRadioSORSetSsid_Object = MibTableColumn
trpzApStatRadioSORSetSsid = _TrpzApStatRadioSORSetSsid_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 8, 1, 3),
    _TrpzApStatRadioSORSetSsid_Type()
)
trpzApStatRadioSORSetSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetSsid.setStatus("current")
_TrpzApStatRadioSORSetMandatory_Type = TrpzRadioOpRateSetMandatory
_TrpzApStatRadioSORSetMandatory_Object = MibTableColumn
trpzApStatRadioSORSetMandatory = _TrpzApStatRadioSORSetMandatory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 8, 1, 4),
    _TrpzApStatRadioSORSetMandatory_Type()
)
trpzApStatRadioSORSetMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetMandatory.setStatus("current")
_TrpzApStatRadioSORSetDisabled_Type = TrpzRadioOpRateSetDisabled
_TrpzApStatRadioSORSetDisabled_Object = MibTableColumn
trpzApStatRadioSORSetDisabled = _TrpzApStatRadioSORSetDisabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 8, 1, 5),
    _TrpzApStatRadioSORSetDisabled_Type()
)
trpzApStatRadioSORSetDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetDisabled.setStatus("current")
_TrpzApStatRadioSORSetBeacon_Type = TrpzRadioOpRateSetSingleValue
_TrpzApStatRadioSORSetBeacon_Object = MibTableColumn
trpzApStatRadioSORSetBeacon = _TrpzApStatRadioSORSetBeacon_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 8, 1, 6),
    _TrpzApStatRadioSORSetBeacon_Type()
)
trpzApStatRadioSORSetBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetBeacon.setStatus("current")
_TrpzApStatRadioSORSetMulticast_Type = TrpzRadioOpRateSetSingleValue
_TrpzApStatRadioSORSetMulticast_Object = MibTableColumn
trpzApStatRadioSORSetMulticast = _TrpzApStatRadioSORSetMulticast_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 8, 1, 7),
    _TrpzApStatRadioSORSetMulticast_Type()
)
trpzApStatRadioSORSetMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetMulticast.setStatus("current")
_TrpzApStatRadioServiceOpRateSetMacTable_Object = MibTable
trpzApStatRadioServiceOpRateSetMacTable = _TrpzApStatRadioServiceOpRateSetMacTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    trpzApStatRadioServiceOpRateSetMacTable.setStatus("current")
_TrpzApStatRadioServiceOpRateSetMacEntry_Object = MibTableRow
trpzApStatRadioServiceOpRateSetMacEntry = _TrpzApStatRadioServiceOpRateSetMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 9, 1)
)
trpzApStatRadioServiceOpRateSetMacEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetMacBssid"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioServiceOpRateSetMacEntry.setStatus("current")
_TrpzApStatRadioSORSetMacBssid_Type = MacAddress
_TrpzApStatRadioSORSetMacBssid_Object = MibTableColumn
trpzApStatRadioSORSetMacBssid = _TrpzApStatRadioSORSetMacBssid_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 9, 1, 1),
    _TrpzApStatRadioSORSetMacBssid_Type()
)
trpzApStatRadioSORSetMacBssid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetMacBssid.setStatus("current")
_TrpzApStatRadioSORSetMacMandatory_Type = TrpzRadioOpRateSetMandatory
_TrpzApStatRadioSORSetMacMandatory_Object = MibTableColumn
trpzApStatRadioSORSetMacMandatory = _TrpzApStatRadioSORSetMacMandatory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 9, 1, 2),
    _TrpzApStatRadioSORSetMacMandatory_Type()
)
trpzApStatRadioSORSetMacMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetMacMandatory.setStatus("current")
_TrpzApStatRadioSORSetMacDisabled_Type = TrpzRadioOpRateSetDisabled
_TrpzApStatRadioSORSetMacDisabled_Object = MibTableColumn
trpzApStatRadioSORSetMacDisabled = _TrpzApStatRadioSORSetMacDisabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 9, 1, 3),
    _TrpzApStatRadioSORSetMacDisabled_Type()
)
trpzApStatRadioSORSetMacDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetMacDisabled.setStatus("current")
_TrpzApStatRadioSORSetMacBeacon_Type = TrpzRadioOpRateSetSingleValue
_TrpzApStatRadioSORSetMacBeacon_Object = MibTableColumn
trpzApStatRadioSORSetMacBeacon = _TrpzApStatRadioSORSetMacBeacon_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 9, 1, 4),
    _TrpzApStatRadioSORSetMacBeacon_Type()
)
trpzApStatRadioSORSetMacBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetMacBeacon.setStatus("current")
_TrpzApStatRadioSORSetMacMulticast_Type = TrpzRadioOpRateSetSingleValue
_TrpzApStatRadioSORSetMacMulticast_Object = MibTableColumn
trpzApStatRadioSORSetMacMulticast = _TrpzApStatRadioSORSetMacMulticast_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 9, 1, 5),
    _TrpzApStatRadioSORSetMacMulticast_Type()
)
trpzApStatRadioSORSetMacMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioSORSetMacMulticast.setStatus("current")
_TrpzApStatRadioOpStatisticsTable_Object = MibTable
trpzApStatRadioOpStatisticsTable = _TrpzApStatRadioOpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10)
)
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatisticsTable.setStatus("current")
_TrpzApStatRadioOpStatisticsEntry_Object = MibTableRow
trpzApStatRadioOpStatisticsEntry = _TrpzApStatRadioOpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1)
)
trpzApStatRadioOpStatisticsEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsApSerialNum"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsRadioNum"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatisticsEntry.setStatus("current")
_TrpzApStatRadioOpStatsApSerialNum_Type = TrpzApSerialNum
_TrpzApStatRadioOpStatsApSerialNum_Object = MibTableColumn
trpzApStatRadioOpStatsApSerialNum = _TrpzApStatRadioOpStatsApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 1),
    _TrpzApStatRadioOpStatsApSerialNum_Type()
)
trpzApStatRadioOpStatsApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsApSerialNum.setStatus("current")
_TrpzApStatRadioOpStatsRadioNum_Type = TrpzRadioNum
_TrpzApStatRadioOpStatsRadioNum_Object = MibTableColumn
trpzApStatRadioOpStatsRadioNum = _TrpzApStatRadioOpStatsRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 2),
    _TrpzApStatRadioOpStatsRadioNum_Type()
)
trpzApStatRadioOpStatsRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsRadioNum.setStatus("current")
_TrpzApStatRadioOpStatsTxUniPkt_Type = Counter64
_TrpzApStatRadioOpStatsTxUniPkt_Object = MibTableColumn
trpzApStatRadioOpStatsTxUniPkt = _TrpzApStatRadioOpStatsTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 3),
    _TrpzApStatRadioOpStatsTxUniPkt_Type()
)
trpzApStatRadioOpStatsTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsTxUniPkt.setStatus("current")
_TrpzApStatRadioOpStatsTxUniOctet_Type = Counter64
_TrpzApStatRadioOpStatsTxUniOctet_Object = MibTableColumn
trpzApStatRadioOpStatsTxUniOctet = _TrpzApStatRadioOpStatsTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 4),
    _TrpzApStatRadioOpStatsTxUniOctet_Type()
)
trpzApStatRadioOpStatsTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsTxUniOctet.setStatus("current")
_TrpzApStatRadioOpStatsTxMultiPkt_Type = Counter64
_TrpzApStatRadioOpStatsTxMultiPkt_Object = MibTableColumn
trpzApStatRadioOpStatsTxMultiPkt = _TrpzApStatRadioOpStatsTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 5),
    _TrpzApStatRadioOpStatsTxMultiPkt_Type()
)
trpzApStatRadioOpStatsTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsTxMultiPkt.setStatus("current")
_TrpzApStatRadioOpStatsTxMultiOctet_Type = Counter64
_TrpzApStatRadioOpStatsTxMultiOctet_Object = MibTableColumn
trpzApStatRadioOpStatsTxMultiOctet = _TrpzApStatRadioOpStatsTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 6),
    _TrpzApStatRadioOpStatsTxMultiOctet_Type()
)
trpzApStatRadioOpStatsTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsTxMultiOctet.setStatus("current")
_TrpzApStatRadioOpStatsRxPkt_Type = Counter64
_TrpzApStatRadioOpStatsRxPkt_Object = MibTableColumn
trpzApStatRadioOpStatsRxPkt = _TrpzApStatRadioOpStatsRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 7),
    _TrpzApStatRadioOpStatsRxPkt_Type()
)
trpzApStatRadioOpStatsRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsRxPkt.setStatus("current")
_TrpzApStatRadioOpStatsRxOctet_Type = Counter64
_TrpzApStatRadioOpStatsRxOctet_Object = MibTableColumn
trpzApStatRadioOpStatsRxOctet = _TrpzApStatRadioOpStatsRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 8),
    _TrpzApStatRadioOpStatsRxOctet_Type()
)
trpzApStatRadioOpStatsRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsRxOctet.setStatus("current")
_TrpzApStatRadioOpStatsUndcrptPkt_Type = Counter64
_TrpzApStatRadioOpStatsUndcrptPkt_Object = MibTableColumn
trpzApStatRadioOpStatsUndcrptPkt = _TrpzApStatRadioOpStatsUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 9),
    _TrpzApStatRadioOpStatsUndcrptPkt_Type()
)
trpzApStatRadioOpStatsUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsUndcrptPkt.setStatus("current")
_TrpzApStatRadioOpStatsUndcrptOctet_Type = Counter64
_TrpzApStatRadioOpStatsUndcrptOctet_Object = MibTableColumn
trpzApStatRadioOpStatsUndcrptOctet = _TrpzApStatRadioOpStatsUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 10),
    _TrpzApStatRadioOpStatsUndcrptOctet_Type()
)
trpzApStatRadioOpStatsUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsUndcrptOctet.setStatus("current")
_TrpzApStatRadioOpStatsPhyErr_Type = Counter64
_TrpzApStatRadioOpStatsPhyErr_Object = MibTableColumn
trpzApStatRadioOpStatsPhyErr = _TrpzApStatRadioOpStatsPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 11),
    _TrpzApStatRadioOpStatsPhyErr_Type()
)
trpzApStatRadioOpStatsPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsPhyErr.setStatus("current")
_TrpzApStatRadioOpStatsResetCount_Type = Counter32
_TrpzApStatRadioOpStatsResetCount_Object = MibTableColumn
trpzApStatRadioOpStatsResetCount = _TrpzApStatRadioOpStatsResetCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 12),
    _TrpzApStatRadioOpStatsResetCount_Type()
)
trpzApStatRadioOpStatsResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsResetCount.setStatus("current")
_TrpzApStatRadioOpStatsAutoTuneChannelChangeCount_Type = Counter32
_TrpzApStatRadioOpStatsAutoTuneChannelChangeCount_Object = MibTableColumn
trpzApStatRadioOpStatsAutoTuneChannelChangeCount = _TrpzApStatRadioOpStatsAutoTuneChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 13),
    _TrpzApStatRadioOpStatsAutoTuneChannelChangeCount_Type()
)
trpzApStatRadioOpStatsAutoTuneChannelChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsAutoTuneChannelChangeCount.setStatus("current")
_TrpzApStatRadioOpStatsTxRetriesCount_Type = Counter32
_TrpzApStatRadioOpStatsTxRetriesCount_Object = MibTableColumn
trpzApStatRadioOpStatsTxRetriesCount = _TrpzApStatRadioOpStatsTxRetriesCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 14),
    _TrpzApStatRadioOpStatsTxRetriesCount_Type()
)
trpzApStatRadioOpStatsTxRetriesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsTxRetriesCount.setStatus("current")
_TrpzApStatRadioOpStatsUserSessions_Type = Gauge32
_TrpzApStatRadioOpStatsUserSessions_Object = MibTableColumn
trpzApStatRadioOpStatsUserSessions = _TrpzApStatRadioOpStatsUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 15),
    _TrpzApStatRadioOpStatsUserSessions_Type()
)
trpzApStatRadioOpStatsUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsUserSessions.setStatus("current")
_TrpzApStatRadioOpStatsNoiseFloor_Type = Integer32
_TrpzApStatRadioOpStatsNoiseFloor_Object = MibTableColumn
trpzApStatRadioOpStatsNoiseFloor = _TrpzApStatRadioOpStatsNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 16),
    _TrpzApStatRadioOpStatsNoiseFloor_Type()
)
trpzApStatRadioOpStatsNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsNoiseFloor.setStatus("current")
_TrpzApStatRadioOpStatsClientAssociations_Type = Counter32
_TrpzApStatRadioOpStatsClientAssociations_Object = MibTableColumn
trpzApStatRadioOpStatsClientAssociations = _TrpzApStatRadioOpStatsClientAssociations_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 17),
    _TrpzApStatRadioOpStatsClientAssociations_Type()
)
trpzApStatRadioOpStatsClientAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsClientAssociations.setStatus("current")
_TrpzApStatRadioOpStatsClientFailedAssociations_Type = Counter32
_TrpzApStatRadioOpStatsClientFailedAssociations_Object = MibTableColumn
trpzApStatRadioOpStatsClientFailedAssociations = _TrpzApStatRadioOpStatsClientFailedAssociations_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 18),
    _TrpzApStatRadioOpStatsClientFailedAssociations_Type()
)
trpzApStatRadioOpStatsClientFailedAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsClientFailedAssociations.setStatus("current")
_TrpzApStatRadioOpStatsClientReAssociations_Type = Counter32
_TrpzApStatRadioOpStatsClientReAssociations_Object = MibTableColumn
trpzApStatRadioOpStatsClientReAssociations = _TrpzApStatRadioOpStatsClientReAssociations_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 19),
    _TrpzApStatRadioOpStatsClientReAssociations_Type()
)
trpzApStatRadioOpStatsClientReAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsClientReAssociations.setStatus("current")
_TrpzApStatRadioOpStatsSignalingPkt_Type = Counter64
_TrpzApStatRadioOpStatsSignalingPkt_Object = MibTableColumn
trpzApStatRadioOpStatsSignalingPkt = _TrpzApStatRadioOpStatsSignalingPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 20),
    _TrpzApStatRadioOpStatsSignalingPkt_Type()
)
trpzApStatRadioOpStatsSignalingPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsSignalingPkt.setStatus("current")
_TrpzApStatRadioOpStatsReTransmitOctet_Type = Counter64
_TrpzApStatRadioOpStatsReTransmitOctet_Object = MibTableColumn
trpzApStatRadioOpStatsReTransmitOctet = _TrpzApStatRadioOpStatsReTransmitOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 21),
    _TrpzApStatRadioOpStatsReTransmitOctet_Type()
)
trpzApStatRadioOpStatsReTransmitOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsReTransmitOctet.setStatus("current")
_TrpzApStatRadioOpStatsRefusedConnectionCount_Type = Counter32
_TrpzApStatRadioOpStatsRefusedConnectionCount_Object = MibTableColumn
trpzApStatRadioOpStatsRefusedConnectionCount = _TrpzApStatRadioOpStatsRefusedConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 22),
    _TrpzApStatRadioOpStatsRefusedConnectionCount_Type()
)
trpzApStatRadioOpStatsRefusedConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsRefusedConnectionCount.setStatus("current")
_TrpzApStatRadioOpStatsRxDataPkt_Type = Counter64
_TrpzApStatRadioOpStatsRxDataPkt_Object = MibTableColumn
trpzApStatRadioOpStatsRxDataPkt = _TrpzApStatRadioOpStatsRxDataPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 23),
    _TrpzApStatRadioOpStatsRxDataPkt_Type()
)
trpzApStatRadioOpStatsRxDataPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsRxDataPkt.setStatus("current")
_TrpzApStatRadioOpStatsRxAuthPkt_Type = Counter64
_TrpzApStatRadioOpStatsRxAuthPkt_Object = MibTableColumn
trpzApStatRadioOpStatsRxAuthPkt = _TrpzApStatRadioOpStatsRxAuthPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 24),
    _TrpzApStatRadioOpStatsRxAuthPkt_Type()
)
trpzApStatRadioOpStatsRxAuthPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsRxAuthPkt.setStatus("current")
_TrpzApStatRadioOpStatsRxAssocPkt_Type = Counter64
_TrpzApStatRadioOpStatsRxAssocPkt_Object = MibTableColumn
trpzApStatRadioOpStatsRxAssocPkt = _TrpzApStatRadioOpStatsRxAssocPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 25),
    _TrpzApStatRadioOpStatsRxAssocPkt_Type()
)
trpzApStatRadioOpStatsRxAssocPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsRxAssocPkt.setStatus("current")
_TrpzApStatRadioOpStatsTxDataPkt_Type = Counter64
_TrpzApStatRadioOpStatsTxDataPkt_Object = MibTableColumn
trpzApStatRadioOpStatsTxDataPkt = _TrpzApStatRadioOpStatsTxDataPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 26),
    _TrpzApStatRadioOpStatsTxDataPkt_Type()
)
trpzApStatRadioOpStatsTxDataPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsTxDataPkt.setStatus("current")
_TrpzApStatRadioOpStatsTxAuthRespPkt_Type = Counter64
_TrpzApStatRadioOpStatsTxAuthRespPkt_Object = MibTableColumn
trpzApStatRadioOpStatsTxAuthRespPkt = _TrpzApStatRadioOpStatsTxAuthRespPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 27),
    _TrpzApStatRadioOpStatsTxAuthRespPkt_Type()
)
trpzApStatRadioOpStatsTxAuthRespPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsTxAuthRespPkt.setStatus("current")
_TrpzApStatRadioOpStatsTxAssocRespPkt_Type = Counter64
_TrpzApStatRadioOpStatsTxAssocRespPkt_Object = MibTableColumn
trpzApStatRadioOpStatsTxAssocRespPkt = _TrpzApStatRadioOpStatsTxAssocRespPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 10, 1, 28),
    _TrpzApStatRadioOpStatsTxAssocRespPkt_Type()
)
trpzApStatRadioOpStatsTxAssocRespPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsTxAssocRespPkt.setStatus("current")
_TrpzApStatRadioOpStatisticsMacTable_Object = MibTable
trpzApStatRadioOpStatisticsMacTable = _TrpzApStatRadioOpStatisticsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11)
)
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatisticsMacTable.setStatus("current")
_TrpzApStatRadioOpStatisticsMacEntry_Object = MibTableRow
trpzApStatRadioOpStatisticsMacEntry = _TrpzApStatRadioOpStatisticsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1)
)
trpzApStatRadioOpStatisticsMacEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacBaseMac"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatisticsMacEntry.setStatus("current")
_TrpzApStatRadioOpStatsMacBaseMac_Type = MacAddress
_TrpzApStatRadioOpStatsMacBaseMac_Object = MibTableColumn
trpzApStatRadioOpStatsMacBaseMac = _TrpzApStatRadioOpStatsMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 1),
    _TrpzApStatRadioOpStatsMacBaseMac_Type()
)
trpzApStatRadioOpStatsMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacBaseMac.setStatus("current")
_TrpzApStatRadioOpStatsMacTxUniPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacTxUniPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacTxUniPkt = _TrpzApStatRadioOpStatsMacTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 2),
    _TrpzApStatRadioOpStatsMacTxUniPkt_Type()
)
trpzApStatRadioOpStatsMacTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacTxUniPkt.setStatus("current")
_TrpzApStatRadioOpStatsMacTxUniOctet_Type = Counter64
_TrpzApStatRadioOpStatsMacTxUniOctet_Object = MibTableColumn
trpzApStatRadioOpStatsMacTxUniOctet = _TrpzApStatRadioOpStatsMacTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 3),
    _TrpzApStatRadioOpStatsMacTxUniOctet_Type()
)
trpzApStatRadioOpStatsMacTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacTxUniOctet.setStatus("current")
_TrpzApStatRadioOpStatsMacTxMultiPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacTxMultiPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacTxMultiPkt = _TrpzApStatRadioOpStatsMacTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 4),
    _TrpzApStatRadioOpStatsMacTxMultiPkt_Type()
)
trpzApStatRadioOpStatsMacTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacTxMultiPkt.setStatus("current")
_TrpzApStatRadioOpStatsMacTxMultiOctet_Type = Counter64
_TrpzApStatRadioOpStatsMacTxMultiOctet_Object = MibTableColumn
trpzApStatRadioOpStatsMacTxMultiOctet = _TrpzApStatRadioOpStatsMacTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 5),
    _TrpzApStatRadioOpStatsMacTxMultiOctet_Type()
)
trpzApStatRadioOpStatsMacTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacTxMultiOctet.setStatus("current")
_TrpzApStatRadioOpStatsMacRxPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacRxPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacRxPkt = _TrpzApStatRadioOpStatsMacRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 6),
    _TrpzApStatRadioOpStatsMacRxPkt_Type()
)
trpzApStatRadioOpStatsMacRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacRxPkt.setStatus("current")
_TrpzApStatRadioOpStatsMacRxOctet_Type = Counter64
_TrpzApStatRadioOpStatsMacRxOctet_Object = MibTableColumn
trpzApStatRadioOpStatsMacRxOctet = _TrpzApStatRadioOpStatsMacRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 7),
    _TrpzApStatRadioOpStatsMacRxOctet_Type()
)
trpzApStatRadioOpStatsMacRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacRxOctet.setStatus("current")
_TrpzApStatRadioOpStatsMacUndcrptPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacUndcrptPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacUndcrptPkt = _TrpzApStatRadioOpStatsMacUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 8),
    _TrpzApStatRadioOpStatsMacUndcrptPkt_Type()
)
trpzApStatRadioOpStatsMacUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacUndcrptPkt.setStatus("current")
_TrpzApStatRadioOpStatsMacUndcrptOctet_Type = Counter64
_TrpzApStatRadioOpStatsMacUndcrptOctet_Object = MibTableColumn
trpzApStatRadioOpStatsMacUndcrptOctet = _TrpzApStatRadioOpStatsMacUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 9),
    _TrpzApStatRadioOpStatsMacUndcrptOctet_Type()
)
trpzApStatRadioOpStatsMacUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacUndcrptOctet.setStatus("current")
_TrpzApStatRadioOpStatsMacPhyErr_Type = Counter64
_TrpzApStatRadioOpStatsMacPhyErr_Object = MibTableColumn
trpzApStatRadioOpStatsMacPhyErr = _TrpzApStatRadioOpStatsMacPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 10),
    _TrpzApStatRadioOpStatsMacPhyErr_Type()
)
trpzApStatRadioOpStatsMacPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacPhyErr.setStatus("current")
_TrpzApStatRadioOpStatsMacResetCount_Type = Counter32
_TrpzApStatRadioOpStatsMacResetCount_Object = MibTableColumn
trpzApStatRadioOpStatsMacResetCount = _TrpzApStatRadioOpStatsMacResetCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 11),
    _TrpzApStatRadioOpStatsMacResetCount_Type()
)
trpzApStatRadioOpStatsMacResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacResetCount.setStatus("current")
_TrpzApStatRadioOpStatsMacAutoTuneChannelChangeCount_Type = Counter32
_TrpzApStatRadioOpStatsMacAutoTuneChannelChangeCount_Object = MibTableColumn
trpzApStatRadioOpStatsMacAutoTuneChannelChangeCount = _TrpzApStatRadioOpStatsMacAutoTuneChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 12),
    _TrpzApStatRadioOpStatsMacAutoTuneChannelChangeCount_Type()
)
trpzApStatRadioOpStatsMacAutoTuneChannelChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacAutoTuneChannelChangeCount.setStatus("current")
_TrpzApStatRadioOpStatsMacTxRetriesCount_Type = Counter32
_TrpzApStatRadioOpStatsMacTxRetriesCount_Object = MibTableColumn
trpzApStatRadioOpStatsMacTxRetriesCount = _TrpzApStatRadioOpStatsMacTxRetriesCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 13),
    _TrpzApStatRadioOpStatsMacTxRetriesCount_Type()
)
trpzApStatRadioOpStatsMacTxRetriesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacTxRetriesCount.setStatus("current")
_TrpzApStatRadioOpStatsMacUserSessions_Type = Gauge32
_TrpzApStatRadioOpStatsMacUserSessions_Object = MibTableColumn
trpzApStatRadioOpStatsMacUserSessions = _TrpzApStatRadioOpStatsMacUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 14),
    _TrpzApStatRadioOpStatsMacUserSessions_Type()
)
trpzApStatRadioOpStatsMacUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacUserSessions.setStatus("current")
_TrpzApStatRadioOpStatsMacNoiseFloor_Type = Integer32
_TrpzApStatRadioOpStatsMacNoiseFloor_Object = MibTableColumn
trpzApStatRadioOpStatsMacNoiseFloor = _TrpzApStatRadioOpStatsMacNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 15),
    _TrpzApStatRadioOpStatsMacNoiseFloor_Type()
)
trpzApStatRadioOpStatsMacNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacNoiseFloor.setStatus("current")
_TrpzApStatRadioOpStatsMacClientAssociations_Type = Counter32
_TrpzApStatRadioOpStatsMacClientAssociations_Object = MibTableColumn
trpzApStatRadioOpStatsMacClientAssociations = _TrpzApStatRadioOpStatsMacClientAssociations_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 16),
    _TrpzApStatRadioOpStatsMacClientAssociations_Type()
)
trpzApStatRadioOpStatsMacClientAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacClientAssociations.setStatus("current")
_TrpzApStatRadioOpStatsMacClientFailedAssociations_Type = Counter32
_TrpzApStatRadioOpStatsMacClientFailedAssociations_Object = MibTableColumn
trpzApStatRadioOpStatsMacClientFailedAssociations = _TrpzApStatRadioOpStatsMacClientFailedAssociations_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 17),
    _TrpzApStatRadioOpStatsMacClientFailedAssociations_Type()
)
trpzApStatRadioOpStatsMacClientFailedAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacClientFailedAssociations.setStatus("current")
_TrpzApStatRadioOpStatsMacClientReAssociations_Type = Counter32
_TrpzApStatRadioOpStatsMacClientReAssociations_Object = MibTableColumn
trpzApStatRadioOpStatsMacClientReAssociations = _TrpzApStatRadioOpStatsMacClientReAssociations_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 18),
    _TrpzApStatRadioOpStatsMacClientReAssociations_Type()
)
trpzApStatRadioOpStatsMacClientReAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacClientReAssociations.setStatus("current")
_TrpzApStatRadioOpStatsMacSignalingPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacSignalingPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacSignalingPkt = _TrpzApStatRadioOpStatsMacSignalingPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 19),
    _TrpzApStatRadioOpStatsMacSignalingPkt_Type()
)
trpzApStatRadioOpStatsMacSignalingPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacSignalingPkt.setStatus("current")
_TrpzApStatRadioOpStatsMacReTransmitOctet_Type = Counter64
_TrpzApStatRadioOpStatsMacReTransmitOctet_Object = MibTableColumn
trpzApStatRadioOpStatsMacReTransmitOctet = _TrpzApStatRadioOpStatsMacReTransmitOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 20),
    _TrpzApStatRadioOpStatsMacReTransmitOctet_Type()
)
trpzApStatRadioOpStatsMacReTransmitOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacReTransmitOctet.setStatus("current")
_TrpzApStatRadioOpStatsMacRefusedConnectionCount_Type = Counter32
_TrpzApStatRadioOpStatsMacRefusedConnectionCount_Object = MibTableColumn
trpzApStatRadioOpStatsMacRefusedConnectionCount = _TrpzApStatRadioOpStatsMacRefusedConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 21),
    _TrpzApStatRadioOpStatsMacRefusedConnectionCount_Type()
)
trpzApStatRadioOpStatsMacRefusedConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacRefusedConnectionCount.setStatus("current")
_TrpzApStatRadioOpStatsMacRxDataPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacRxDataPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacRxDataPkt = _TrpzApStatRadioOpStatsMacRxDataPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 22),
    _TrpzApStatRadioOpStatsMacRxDataPkt_Type()
)
trpzApStatRadioOpStatsMacRxDataPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacRxDataPkt.setStatus("current")
_TrpzApStatRadioOpStatsMacRxAuthPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacRxAuthPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacRxAuthPkt = _TrpzApStatRadioOpStatsMacRxAuthPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 23),
    _TrpzApStatRadioOpStatsMacRxAuthPkt_Type()
)
trpzApStatRadioOpStatsMacRxAuthPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacRxAuthPkt.setStatus("current")
_TrpzApStatRadioOpStatsMacRxAssocPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacRxAssocPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacRxAssocPkt = _TrpzApStatRadioOpStatsMacRxAssocPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 24),
    _TrpzApStatRadioOpStatsMacRxAssocPkt_Type()
)
trpzApStatRadioOpStatsMacRxAssocPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacRxAssocPkt.setStatus("current")
_TrpzApStatRadioOpStatsMacTxDataPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacTxDataPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacTxDataPkt = _TrpzApStatRadioOpStatsMacTxDataPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 25),
    _TrpzApStatRadioOpStatsMacTxDataPkt_Type()
)
trpzApStatRadioOpStatsMacTxDataPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacTxDataPkt.setStatus("current")
_TrpzApStatRadioOpStatsMacTxAuthRespPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacTxAuthRespPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacTxAuthRespPkt = _TrpzApStatRadioOpStatsMacTxAuthRespPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 26),
    _TrpzApStatRadioOpStatsMacTxAuthRespPkt_Type()
)
trpzApStatRadioOpStatsMacTxAuthRespPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacTxAuthRespPkt.setStatus("current")
_TrpzApStatRadioOpStatsMacTxAssocRespPkt_Type = Counter64
_TrpzApStatRadioOpStatsMacTxAssocRespPkt_Object = MibTableColumn
trpzApStatRadioOpStatsMacTxAssocRespPkt = _TrpzApStatRadioOpStatsMacTxAssocRespPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 11, 1, 27),
    _TrpzApStatRadioOpStatsMacTxAssocRespPkt_Type()
)
trpzApStatRadioOpStatsMacTxAssocRespPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioOpStatsMacTxAssocRespPkt.setStatus("current")
_TrpzApStatRadioRateOpStatisticsTable_Object = MibTable
trpzApStatRadioRateOpStatisticsTable = _TrpzApStatRadioRateOpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatisticsTable.setStatus("current")
_TrpzApStatRadioRateOpStatisticsEntry_Object = MibTableRow
trpzApStatRadioRateOpStatisticsEntry = _TrpzApStatRadioRateOpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1)
)
trpzApStatRadioRateOpStatisticsEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsApSerialNum"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsRadioNum"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsRate"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatisticsEntry.setStatus("current")
_TrpzApStatRadioRateOpStatsApSerialNum_Type = TrpzApSerialNum
_TrpzApStatRadioRateOpStatsApSerialNum_Object = MibTableColumn
trpzApStatRadioRateOpStatsApSerialNum = _TrpzApStatRadioRateOpStatsApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 1),
    _TrpzApStatRadioRateOpStatsApSerialNum_Type()
)
trpzApStatRadioRateOpStatsApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsApSerialNum.setStatus("current")
_TrpzApStatRadioRateOpStatsRadioNum_Type = TrpzRadioNum
_TrpzApStatRadioRateOpStatsRadioNum_Object = MibTableColumn
trpzApStatRadioRateOpStatsRadioNum = _TrpzApStatRadioRateOpStatsRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 2),
    _TrpzApStatRadioRateOpStatsRadioNum_Type()
)
trpzApStatRadioRateOpStatsRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsRadioNum.setStatus("current")
_TrpzApStatRadioRateOpStatsRate_Type = TrpzRadioRate
_TrpzApStatRadioRateOpStatsRate_Object = MibTableColumn
trpzApStatRadioRateOpStatsRate = _TrpzApStatRadioRateOpStatsRate_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 3),
    _TrpzApStatRadioRateOpStatsRate_Type()
)
trpzApStatRadioRateOpStatsRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsRate.setStatus("current")
_TrpzApStatRadioRateOpStatsTxUniPkt_Type = Counter64
_TrpzApStatRadioRateOpStatsTxUniPkt_Object = MibTableColumn
trpzApStatRadioRateOpStatsTxUniPkt = _TrpzApStatRadioRateOpStatsTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 4),
    _TrpzApStatRadioRateOpStatsTxUniPkt_Type()
)
trpzApStatRadioRateOpStatsTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsTxUniPkt.setStatus("current")
_TrpzApStatRadioRateOpStatsTxUniOctet_Type = Counter64
_TrpzApStatRadioRateOpStatsTxUniOctet_Object = MibTableColumn
trpzApStatRadioRateOpStatsTxUniOctet = _TrpzApStatRadioRateOpStatsTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 5),
    _TrpzApStatRadioRateOpStatsTxUniOctet_Type()
)
trpzApStatRadioRateOpStatsTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsTxUniOctet.setStatus("current")
_TrpzApStatRadioRateOpStatsTxMultiPkt_Type = Counter64
_TrpzApStatRadioRateOpStatsTxMultiPkt_Object = MibTableColumn
trpzApStatRadioRateOpStatsTxMultiPkt = _TrpzApStatRadioRateOpStatsTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 6),
    _TrpzApStatRadioRateOpStatsTxMultiPkt_Type()
)
trpzApStatRadioRateOpStatsTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsTxMultiPkt.setStatus("current")
_TrpzApStatRadioRateOpStatsTxMultiOctet_Type = Counter64
_TrpzApStatRadioRateOpStatsTxMultiOctet_Object = MibTableColumn
trpzApStatRadioRateOpStatsTxMultiOctet = _TrpzApStatRadioRateOpStatsTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 7),
    _TrpzApStatRadioRateOpStatsTxMultiOctet_Type()
)
trpzApStatRadioRateOpStatsTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsTxMultiOctet.setStatus("current")
_TrpzApStatRadioRateOpStatsRxPkt_Type = Counter64
_TrpzApStatRadioRateOpStatsRxPkt_Object = MibTableColumn
trpzApStatRadioRateOpStatsRxPkt = _TrpzApStatRadioRateOpStatsRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 8),
    _TrpzApStatRadioRateOpStatsRxPkt_Type()
)
trpzApStatRadioRateOpStatsRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsRxPkt.setStatus("current")
_TrpzApStatRadioRateOpStatsRxOctet_Type = Counter64
_TrpzApStatRadioRateOpStatsRxOctet_Object = MibTableColumn
trpzApStatRadioRateOpStatsRxOctet = _TrpzApStatRadioRateOpStatsRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 9),
    _TrpzApStatRadioRateOpStatsRxOctet_Type()
)
trpzApStatRadioRateOpStatsRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsRxOctet.setStatus("current")
_TrpzApStatRadioRateOpStatsUndcrptPkt_Type = Counter64
_TrpzApStatRadioRateOpStatsUndcrptPkt_Object = MibTableColumn
trpzApStatRadioRateOpStatsUndcrptPkt = _TrpzApStatRadioRateOpStatsUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 10),
    _TrpzApStatRadioRateOpStatsUndcrptPkt_Type()
)
trpzApStatRadioRateOpStatsUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsUndcrptPkt.setStatus("current")
_TrpzApStatRadioRateOpStatsUndcrptOctet_Type = Counter64
_TrpzApStatRadioRateOpStatsUndcrptOctet_Object = MibTableColumn
trpzApStatRadioRateOpStatsUndcrptOctet = _TrpzApStatRadioRateOpStatsUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 11),
    _TrpzApStatRadioRateOpStatsUndcrptOctet_Type()
)
trpzApStatRadioRateOpStatsUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsUndcrptOctet.setStatus("current")
_TrpzApStatRadioRateOpStatsPhyErr_Type = Counter64
_TrpzApStatRadioRateOpStatsPhyErr_Object = MibTableColumn
trpzApStatRadioRateOpStatsPhyErr = _TrpzApStatRadioRateOpStatsPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 12, 1, 12),
    _TrpzApStatRadioRateOpStatsPhyErr_Type()
)
trpzApStatRadioRateOpStatsPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsPhyErr.setStatus("current")
_TrpzApStatRadioRateOpStatisticsMacTable_Object = MibTable
trpzApStatRadioRateOpStatisticsMacTable = _TrpzApStatRadioRateOpStatisticsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13)
)
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatisticsMacTable.setStatus("current")
_TrpzApStatRadioRateOpStatisticsMacEntry_Object = MibTableRow
trpzApStatRadioRateOpStatisticsMacEntry = _TrpzApStatRadioRateOpStatisticsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1)
)
trpzApStatRadioRateOpStatisticsMacEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacBaseMac"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacRate"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatisticsMacEntry.setStatus("current")
_TrpzApStatRadioRateOpStatsMacBaseMac_Type = MacAddress
_TrpzApStatRadioRateOpStatsMacBaseMac_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacBaseMac = _TrpzApStatRadioRateOpStatsMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 1),
    _TrpzApStatRadioRateOpStatsMacBaseMac_Type()
)
trpzApStatRadioRateOpStatsMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacBaseMac.setStatus("current")
_TrpzApStatRadioRateOpStatsMacRate_Type = TrpzRadioRate
_TrpzApStatRadioRateOpStatsMacRate_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacRate = _TrpzApStatRadioRateOpStatsMacRate_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 2),
    _TrpzApStatRadioRateOpStatsMacRate_Type()
)
trpzApStatRadioRateOpStatsMacRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacRate.setStatus("current")
_TrpzApStatRadioRateOpStatsMacTxUniPkt_Type = Counter64
_TrpzApStatRadioRateOpStatsMacTxUniPkt_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacTxUniPkt = _TrpzApStatRadioRateOpStatsMacTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 3),
    _TrpzApStatRadioRateOpStatsMacTxUniPkt_Type()
)
trpzApStatRadioRateOpStatsMacTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacTxUniPkt.setStatus("current")
_TrpzApStatRadioRateOpStatsMacTxUniOctet_Type = Counter64
_TrpzApStatRadioRateOpStatsMacTxUniOctet_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacTxUniOctet = _TrpzApStatRadioRateOpStatsMacTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 4),
    _TrpzApStatRadioRateOpStatsMacTxUniOctet_Type()
)
trpzApStatRadioRateOpStatsMacTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacTxUniOctet.setStatus("current")
_TrpzApStatRadioRateOpStatsMacTxMultiPkt_Type = Counter64
_TrpzApStatRadioRateOpStatsMacTxMultiPkt_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacTxMultiPkt = _TrpzApStatRadioRateOpStatsMacTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 5),
    _TrpzApStatRadioRateOpStatsMacTxMultiPkt_Type()
)
trpzApStatRadioRateOpStatsMacTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacTxMultiPkt.setStatus("current")
_TrpzApStatRadioRateOpStatsMacTxMultiOctet_Type = Counter64
_TrpzApStatRadioRateOpStatsMacTxMultiOctet_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacTxMultiOctet = _TrpzApStatRadioRateOpStatsMacTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 6),
    _TrpzApStatRadioRateOpStatsMacTxMultiOctet_Type()
)
trpzApStatRadioRateOpStatsMacTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacTxMultiOctet.setStatus("current")
_TrpzApStatRadioRateOpStatsMacRxPkt_Type = Counter64
_TrpzApStatRadioRateOpStatsMacRxPkt_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacRxPkt = _TrpzApStatRadioRateOpStatsMacRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 7),
    _TrpzApStatRadioRateOpStatsMacRxPkt_Type()
)
trpzApStatRadioRateOpStatsMacRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacRxPkt.setStatus("current")
_TrpzApStatRadioRateOpStatsMacRxOctet_Type = Counter64
_TrpzApStatRadioRateOpStatsMacRxOctet_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacRxOctet = _TrpzApStatRadioRateOpStatsMacRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 8),
    _TrpzApStatRadioRateOpStatsMacRxOctet_Type()
)
trpzApStatRadioRateOpStatsMacRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacRxOctet.setStatus("current")
_TrpzApStatRadioRateOpStatsMacUndcrptPkt_Type = Counter64
_TrpzApStatRadioRateOpStatsMacUndcrptPkt_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacUndcrptPkt = _TrpzApStatRadioRateOpStatsMacUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 9),
    _TrpzApStatRadioRateOpStatsMacUndcrptPkt_Type()
)
trpzApStatRadioRateOpStatsMacUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacUndcrptPkt.setStatus("current")
_TrpzApStatRadioRateOpStatsMacUndcrptOctet_Type = Counter64
_TrpzApStatRadioRateOpStatsMacUndcrptOctet_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacUndcrptOctet = _TrpzApStatRadioRateOpStatsMacUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 10),
    _TrpzApStatRadioRateOpStatsMacUndcrptOctet_Type()
)
trpzApStatRadioRateOpStatsMacUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacUndcrptOctet.setStatus("current")
_TrpzApStatRadioRateOpStatsMacPhyErr_Type = Counter64
_TrpzApStatRadioRateOpStatsMacPhyErr_Object = MibTableColumn
trpzApStatRadioRateOpStatsMacPhyErr = _TrpzApStatRadioRateOpStatsMacPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 13, 1, 11),
    _TrpzApStatRadioRateOpStatsMacPhyErr_Type()
)
trpzApStatRadioRateOpStatsMacPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateOpStatsMacPhyErr.setStatus("current")
_TrpzApStatRadioRateExOpStatisticsTable_Object = MibTable
trpzApStatRadioRateExOpStatisticsTable = _TrpzApStatRadioRateExOpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14)
)
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatisticsTable.setStatus("current")
_TrpzApStatRadioRateExOpStatisticsEntry_Object = MibTableRow
trpzApStatRadioRateExOpStatisticsEntry = _TrpzApStatRadioRateExOpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1)
)
trpzApStatRadioRateExOpStatisticsEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsApSerialNum"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsRadioNum"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsRateEx"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatisticsEntry.setStatus("current")
_TrpzApStatRadioRateExOpStatsApSerialNum_Type = TrpzApSerialNum
_TrpzApStatRadioRateExOpStatsApSerialNum_Object = MibTableColumn
trpzApStatRadioRateExOpStatsApSerialNum = _TrpzApStatRadioRateExOpStatsApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 1),
    _TrpzApStatRadioRateExOpStatsApSerialNum_Type()
)
trpzApStatRadioRateExOpStatsApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsApSerialNum.setStatus("current")
_TrpzApStatRadioRateExOpStatsRadioNum_Type = TrpzRadioNum
_TrpzApStatRadioRateExOpStatsRadioNum_Object = MibTableColumn
trpzApStatRadioRateExOpStatsRadioNum = _TrpzApStatRadioRateExOpStatsRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 2),
    _TrpzApStatRadioRateExOpStatsRadioNum_Type()
)
trpzApStatRadioRateExOpStatsRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsRadioNum.setStatus("current")
_TrpzApStatRadioRateExOpStatsRateEx_Type = TrpzRadioRateEx
_TrpzApStatRadioRateExOpStatsRateEx_Object = MibTableColumn
trpzApStatRadioRateExOpStatsRateEx = _TrpzApStatRadioRateExOpStatsRateEx_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 3),
    _TrpzApStatRadioRateExOpStatsRateEx_Type()
)
trpzApStatRadioRateExOpStatsRateEx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsRateEx.setStatus("current")
_TrpzApStatRadioRateExOpStatsTxUniPkt_Type = Counter64
_TrpzApStatRadioRateExOpStatsTxUniPkt_Object = MibTableColumn
trpzApStatRadioRateExOpStatsTxUniPkt = _TrpzApStatRadioRateExOpStatsTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 4),
    _TrpzApStatRadioRateExOpStatsTxUniPkt_Type()
)
trpzApStatRadioRateExOpStatsTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsTxUniPkt.setStatus("current")
_TrpzApStatRadioRateExOpStatsTxUniOctet_Type = Counter64
_TrpzApStatRadioRateExOpStatsTxUniOctet_Object = MibTableColumn
trpzApStatRadioRateExOpStatsTxUniOctet = _TrpzApStatRadioRateExOpStatsTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 5),
    _TrpzApStatRadioRateExOpStatsTxUniOctet_Type()
)
trpzApStatRadioRateExOpStatsTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsTxUniOctet.setStatus("current")
_TrpzApStatRadioRateExOpStatsTxMultiPkt_Type = Counter64
_TrpzApStatRadioRateExOpStatsTxMultiPkt_Object = MibTableColumn
trpzApStatRadioRateExOpStatsTxMultiPkt = _TrpzApStatRadioRateExOpStatsTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 6),
    _TrpzApStatRadioRateExOpStatsTxMultiPkt_Type()
)
trpzApStatRadioRateExOpStatsTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsTxMultiPkt.setStatus("current")
_TrpzApStatRadioRateExOpStatsTxMultiOctet_Type = Counter64
_TrpzApStatRadioRateExOpStatsTxMultiOctet_Object = MibTableColumn
trpzApStatRadioRateExOpStatsTxMultiOctet = _TrpzApStatRadioRateExOpStatsTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 7),
    _TrpzApStatRadioRateExOpStatsTxMultiOctet_Type()
)
trpzApStatRadioRateExOpStatsTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsTxMultiOctet.setStatus("current")
_TrpzApStatRadioRateExOpStatsRxPkt_Type = Counter64
_TrpzApStatRadioRateExOpStatsRxPkt_Object = MibTableColumn
trpzApStatRadioRateExOpStatsRxPkt = _TrpzApStatRadioRateExOpStatsRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 8),
    _TrpzApStatRadioRateExOpStatsRxPkt_Type()
)
trpzApStatRadioRateExOpStatsRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsRxPkt.setStatus("current")
_TrpzApStatRadioRateExOpStatsRxOctet_Type = Counter64
_TrpzApStatRadioRateExOpStatsRxOctet_Object = MibTableColumn
trpzApStatRadioRateExOpStatsRxOctet = _TrpzApStatRadioRateExOpStatsRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 9),
    _TrpzApStatRadioRateExOpStatsRxOctet_Type()
)
trpzApStatRadioRateExOpStatsRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsRxOctet.setStatus("current")
_TrpzApStatRadioRateExOpStatsUndcrptPkt_Type = Counter64
_TrpzApStatRadioRateExOpStatsUndcrptPkt_Object = MibTableColumn
trpzApStatRadioRateExOpStatsUndcrptPkt = _TrpzApStatRadioRateExOpStatsUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 10),
    _TrpzApStatRadioRateExOpStatsUndcrptPkt_Type()
)
trpzApStatRadioRateExOpStatsUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsUndcrptPkt.setStatus("current")
_TrpzApStatRadioRateExOpStatsUndcrptOctet_Type = Counter64
_TrpzApStatRadioRateExOpStatsUndcrptOctet_Object = MibTableColumn
trpzApStatRadioRateExOpStatsUndcrptOctet = _TrpzApStatRadioRateExOpStatsUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 11),
    _TrpzApStatRadioRateExOpStatsUndcrptOctet_Type()
)
trpzApStatRadioRateExOpStatsUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsUndcrptOctet.setStatus("current")
_TrpzApStatRadioRateExOpStatsPhyErr_Type = Counter64
_TrpzApStatRadioRateExOpStatsPhyErr_Object = MibTableColumn
trpzApStatRadioRateExOpStatsPhyErr = _TrpzApStatRadioRateExOpStatsPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 14, 1, 12),
    _TrpzApStatRadioRateExOpStatsPhyErr_Type()
)
trpzApStatRadioRateExOpStatsPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsPhyErr.setStatus("current")
_TrpzApStatRadioRateExOpStatisticsMacTable_Object = MibTable
trpzApStatRadioRateExOpStatisticsMacTable = _TrpzApStatRadioRateExOpStatisticsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15)
)
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatisticsMacTable.setStatus("current")
_TrpzApStatRadioRateExOpStatisticsMacEntry_Object = MibTableRow
trpzApStatRadioRateExOpStatisticsMacEntry = _TrpzApStatRadioRateExOpStatisticsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1)
)
trpzApStatRadioRateExOpStatisticsMacEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacBaseMac"),
    (0, "TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacRateEx"),
)
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatisticsMacEntry.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacBaseMac_Type = MacAddress
_TrpzApStatRadioRateExOpStatsMacBaseMac_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacBaseMac = _TrpzApStatRadioRateExOpStatsMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 1),
    _TrpzApStatRadioRateExOpStatsMacBaseMac_Type()
)
trpzApStatRadioRateExOpStatsMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacBaseMac.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacRateEx_Type = TrpzRadioRateEx
_TrpzApStatRadioRateExOpStatsMacRateEx_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacRateEx = _TrpzApStatRadioRateExOpStatsMacRateEx_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 2),
    _TrpzApStatRadioRateExOpStatsMacRateEx_Type()
)
trpzApStatRadioRateExOpStatsMacRateEx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacRateEx.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacTxUniPkt_Type = Counter64
_TrpzApStatRadioRateExOpStatsMacTxUniPkt_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacTxUniPkt = _TrpzApStatRadioRateExOpStatsMacTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 3),
    _TrpzApStatRadioRateExOpStatsMacTxUniPkt_Type()
)
trpzApStatRadioRateExOpStatsMacTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacTxUniPkt.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacTxUniOctet_Type = Counter64
_TrpzApStatRadioRateExOpStatsMacTxUniOctet_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacTxUniOctet = _TrpzApStatRadioRateExOpStatsMacTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 4),
    _TrpzApStatRadioRateExOpStatsMacTxUniOctet_Type()
)
trpzApStatRadioRateExOpStatsMacTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacTxUniOctet.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacTxMultiPkt_Type = Counter64
_TrpzApStatRadioRateExOpStatsMacTxMultiPkt_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacTxMultiPkt = _TrpzApStatRadioRateExOpStatsMacTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 5),
    _TrpzApStatRadioRateExOpStatsMacTxMultiPkt_Type()
)
trpzApStatRadioRateExOpStatsMacTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacTxMultiPkt.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacTxMultiOctet_Type = Counter64
_TrpzApStatRadioRateExOpStatsMacTxMultiOctet_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacTxMultiOctet = _TrpzApStatRadioRateExOpStatsMacTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 6),
    _TrpzApStatRadioRateExOpStatsMacTxMultiOctet_Type()
)
trpzApStatRadioRateExOpStatsMacTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacTxMultiOctet.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacRxPkt_Type = Counter64
_TrpzApStatRadioRateExOpStatsMacRxPkt_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacRxPkt = _TrpzApStatRadioRateExOpStatsMacRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 7),
    _TrpzApStatRadioRateExOpStatsMacRxPkt_Type()
)
trpzApStatRadioRateExOpStatsMacRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacRxPkt.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacRxOctet_Type = Counter64
_TrpzApStatRadioRateExOpStatsMacRxOctet_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacRxOctet = _TrpzApStatRadioRateExOpStatsMacRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 8),
    _TrpzApStatRadioRateExOpStatsMacRxOctet_Type()
)
trpzApStatRadioRateExOpStatsMacRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacRxOctet.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacUndcrptPkt_Type = Counter64
_TrpzApStatRadioRateExOpStatsMacUndcrptPkt_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacUndcrptPkt = _TrpzApStatRadioRateExOpStatsMacUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 9),
    _TrpzApStatRadioRateExOpStatsMacUndcrptPkt_Type()
)
trpzApStatRadioRateExOpStatsMacUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacUndcrptPkt.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacUndcrptOctet_Type = Counter64
_TrpzApStatRadioRateExOpStatsMacUndcrptOctet_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacUndcrptOctet = _TrpzApStatRadioRateExOpStatsMacUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 10),
    _TrpzApStatRadioRateExOpStatsMacUndcrptOctet_Type()
)
trpzApStatRadioRateExOpStatsMacUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacUndcrptOctet.setStatus("current")
_TrpzApStatRadioRateExOpStatsMacPhyErr_Type = Counter64
_TrpzApStatRadioRateExOpStatsMacPhyErr_Object = MibTableColumn
trpzApStatRadioRateExOpStatsMacPhyErr = _TrpzApStatRadioRateExOpStatsMacPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 1, 15, 1, 11),
    _TrpzApStatRadioRateExOpStatsMacPhyErr_Type()
)
trpzApStatRadioRateExOpStatsMacPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApStatRadioRateExOpStatsMacPhyErr.setStatus("current")
_TrpzApStatusConformance_ObjectIdentity = ObjectIdentity
trpzApStatusConformance = _TrpzApStatusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2)
)
_TrpzApStatusCompliances_ObjectIdentity = ObjectIdentity
trpzApStatusCompliances = _TrpzApStatusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 1)
)
_TrpzApStatusGroups_ObjectIdentity = ObjectIdentity
trpzApStatusGroups = _TrpzApStatusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2)
)

# Managed Objects groups

trpzApStatusCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 1)
)
trpzApStatusCommonGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatNumAps"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusBaseMac"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusAttachType"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusPortOrDapNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusApState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusModel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusFingerprint"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusApName"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusVlan"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusIpAddress"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusUptimeSecs"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusCpuInfo"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusManufacturerId"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusRamBytes"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusHardwareRev"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacSerialNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacAttachType"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacPortOrDapNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacApState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacModel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacFingerprint"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacApName"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacVlan"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacIpAddress"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacUptimeSecs"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacCpuInfo"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacManufacturerId"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacRamBytes"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacHardwareRev"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusBaseMac"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusEnable"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioConfigState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusCurrentPowerLevel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusCurrentChannelNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacApSerialNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacEnable"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioConfigState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacCurrentPowerLevel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacCurrentChannelNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServBssid"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServServiceProfileName"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServMacApSerialNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServMacRadioNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServMacSsid"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServMacServiceProfileName"))
)
if mibBuilder.loadTexts:
    trpzApStatusCommonGroup.setStatus("obsolete")

trpzApStatusScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 2)
)
trpzApStatusScalarsGroup.setObjects(
    ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatNumAps")
)
if mibBuilder.loadTexts:
    trpzApStatusScalarsGroup.setStatus("current")

trpzApStatusApStatusTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 3)
)
trpzApStatusApStatusTablesGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusBaseMac"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusAttachType"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusPortOrDapNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusApState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusModel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusFingerprint"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusApName"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusVlan"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusIpAddress"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusUptimeSecs"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusCpuInfo"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusManufacturerId"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusRamBytes"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusHardwareRev"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusClientSessions"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacSerialNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacAttachType"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacPortOrDapNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacApState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacModel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacFingerprint"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacApName"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacVlan"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacIpAddress"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacUptimeSecs"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacCpuInfo"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacManufacturerId"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacRamBytes"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacHardwareRev"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacClientSessions"))
)
if mibBuilder.loadTexts:
    trpzApStatusApStatusTablesGroup.setStatus("obsolete")

trpzApStatusRadioStatusTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 4)
)
trpzApStatusRadioStatusTablesGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusBaseMac"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusEnable"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioConfigState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusCurrentPowerLevel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusCurrentChannelNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacApSerialNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacEnable"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioConfigState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacCurrentPowerLevel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacCurrentChannelNum"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioStatusTablesGroup.setStatus("obsolete")

trpzApStatusRadioServiceTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 5)
)
trpzApStatusRadioServiceTablesGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServBssid"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServServiceProfileName"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServMacApSerialNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServMacRadioNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServMacSsid"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioServMacServiceProfileName"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioServiceTablesGroup.setStatus("current")

trpzApStatusRadioServiceOpRateSetTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 6)
)
trpzApStatusRadioServiceOpRateSetTablesGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetMandatory"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetDisabled"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetBeacon"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetMulticast"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetMacMandatory"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetMacDisabled"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetMacBeacon"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioSORSetMacMulticast"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioServiceOpRateSetTablesGroup.setStatus("current")

trpzApStatusRadioOpStatisticsTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 7)
)
trpzApStatusRadioOpStatisticsTablesGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsTxUniPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsTxUniOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsTxMultiPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsTxMultiOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsRxPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsRxOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsUndcrptPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsUndcrptOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsPhyErr"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsResetCount"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsAutoTuneChannelChangeCount"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsTxRetriesCount"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsUserSessions"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsNoiseFloor"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacTxUniPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacTxUniOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacTxMultiPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacTxMultiOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacRxPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacRxOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacUndcrptPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacUndcrptOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacPhyErr"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacResetCount"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacAutoTuneChannelChangeCount"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacTxRetriesCount"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacUserSessions"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacNoiseFloor"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioOpStatisticsTablesGroup.setStatus("current")

trpzApStatusRadioOpStatisticsPerRateTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 8)
)
trpzApStatusRadioOpStatisticsPerRateTablesGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsTxUniPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsTxUniOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsTxMultiPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsTxMultiOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsRxPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsRxOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsUndcrptPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsUndcrptOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsPhyErr"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacTxUniPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacTxUniOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacTxMultiPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacTxMultiOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacRxPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacRxOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacUndcrptPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacUndcrptOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateOpStatsMacPhyErr"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioOpStatisticsPerRateTablesGroup.setStatus("current")

trpzApStatusApStatusVersionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 9)
)
trpzApStatusApStatusVersionsGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusSoftwareVer"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusBootVer"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacSoftwareVer"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacBootVer"))
)
if mibBuilder.loadTexts:
    trpzApStatusApStatusVersionsGroup.setStatus("current")

trpzApStatusApStatusTablesGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 10)
)
trpzApStatusApStatusTablesGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusBaseMac"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusAttachType"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusApState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusModel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusFingerprint"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusApName"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusVlan"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusIpAddress"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusUptimeSecs"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusCpuInfo"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusManufacturerId"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusRamBytes"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusHardwareRev"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusClientSessions"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusApNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacSerialNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacAttachType"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacApState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacModel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacFingerprint"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacApName"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacVlan"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacIpAddress"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacUptimeSecs"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacCpuInfo"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacManufacturerId"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacRamBytes"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacHardwareRev"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacClientSessions"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacApNum"))
)
if mibBuilder.loadTexts:
    trpzApStatusApStatusTablesGroupRev2.setStatus("current")

trpzApStatusRadioStatusMaxPowerPhyTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 11)
)
trpzApStatusRadioStatusMaxPowerPhyTypeGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMaxPowerLevel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioPhyType"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacMaxPowerLevel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioPhyType"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioStatusMaxPowerPhyTypeGroup.setStatus("current")

trpzApStatusRadioStatusTablesGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 12)
)
trpzApStatusRadioStatusTablesGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusBaseMac"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioConfigState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusCurrentPowerLevel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusCurrentChannelNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusClientSessions"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioMode"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacApSerialNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioConfigState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacCurrentPowerLevel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacCurrentChannelNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacClientSessions"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioMode"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioStatusTablesGroupRev2.setStatus("current")

trpzApStatusRadioStatusWideMimoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 13)
)
trpzApStatusRadioStatusWideMimoGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioChannelWidth"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioMimoState"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioChannelWidth"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioMimoState"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioStatusWideMimoGroup.setStatus("obsolete")

trpzApStatusRadioOpStatisticsPerRateExTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 14)
)
trpzApStatusRadioOpStatisticsPerRateExTablesGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsTxUniPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsTxUniOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsTxMultiPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsTxMultiOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsRxPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsRxOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsUndcrptPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsUndcrptOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsPhyErr"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacTxUniPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacTxUniOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacTxMultiPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacTxMultiOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacRxPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacRxOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacUndcrptPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacUndcrptOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioRateExOpStatsMacPhyErr"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioOpStatisticsPerRateExTablesGroup.setStatus("current")

trpzApStatusApStatusPhysPortNumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 15)
)
trpzApStatusApStatusPhysPortNumGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusPhysPortNum"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacPhysPortNum"))
)
if mibBuilder.loadTexts:
    trpzApStatusApStatusPhysPortNumGroup.setStatus("current")

trpzApStatusApStatusConnectivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 16)
)
trpzApStatusApStatusConnectivityGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusIpNetmask"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusWiredIfNumber"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacIpNetmask"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatApStatusMacWiredIfNumber"))
)
if mibBuilder.loadTexts:
    trpzApStatusApStatusConnectivityGroup.setStatus("current")

trpzApStatusRadioStatusAntennaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 17)
)
trpzApStatusRadioStatusAntennaGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMinPowerLevel"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacMinPowerLevel"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioStatusAntennaGroup.setStatus("current")

trpzApStatusRadioOpStatisticsClientAssocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 18)
)
trpzApStatusRadioOpStatisticsClientAssocGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsClientAssociations"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsClientFailedAssociations"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsClientReAssociations"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacClientAssociations"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacClientFailedAssociations"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacClientReAssociations"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioOpStatisticsClientAssocGroup.setStatus("current")

trpzApStatusRadioOpStatisticsSignErrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 19)
)
trpzApStatusRadioOpStatisticsSignErrGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsSignalingPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsReTransmitOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsRefusedConnectionCount"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacSignalingPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacReTransmitOctet"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacRefusedConnectionCount"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioOpStatisticsSignErrGroup.setStatus("current")

trpzApStatusRadioStatusWideMimoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 20)
)
trpzApStatusRadioStatusWideMimoGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioChannelWidth"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioMimoRxChains"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusRadioMimoTxChains"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioChannelWidth"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioMimoRxChains"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacRadioMimoTxChains"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioStatusWideMimoGroupRev2.setStatus("current")

trpzApStatusRadioOpStatisticsPktDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 21)
)
trpzApStatusRadioOpStatisticsPktDetailGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsRxDataPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsRxAuthPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsRxAssocPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsTxDataPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsTxAuthRespPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsTxAssocRespPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacRxDataPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacRxAuthPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacRxAssocPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacTxDataPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacTxAuthRespPkt"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioOpStatsMacTxAssocRespPkt"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioOpStatisticsPktDetailGroup.setStatus("current")

trpzApStatusRadioStatusSpectralDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 2, 22)
)
trpzApStatusRadioStatusSpectralDataGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusSpectralDataCollect"),
        ("TRAPEZE-NETWORKS-AP-STATUS-MIB", "trpzApStatRadioStatusMacSpectralDataCollect"))
)
if mibBuilder.loadTexts:
    trpzApStatusRadioStatusSpectralDataGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzApStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzApStatusCompliance.setStatus(
        "obsolete"
    )

trpzApStatusComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    trpzApStatusComplianceRev2.setStatus(
        "obsolete"
    )

trpzApStatusComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    trpzApStatusComplianceRev3.setStatus(
        "obsolete"
    )

trpzApStatusComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    trpzApStatusComplianceRev4.setStatus(
        "obsolete"
    )

trpzApStatusComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    trpzApStatusComplianceRev5.setStatus(
        "obsolete"
    )

trpzApStatusComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    trpzApStatusComplianceRev6.setStatus(
        "deprecated"
    )

trpzApStatusComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 5, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    trpzApStatusComplianceRev7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-AP-STATUS-MIB",
    **{"TrpzRadioOpRateSetSingleValue": TrpzRadioOpRateSetSingleValue,
       "TrpzRadioOpRateSetMandatory": TrpzRadioOpRateSetMandatory,
       "TrpzRadioOpRateSetDisabled": TrpzRadioOpRateSetDisabled,
       "trpzApStatusMib": trpzApStatusMib,
       "trpzApStatusObjects": trpzApStatusObjects,
       "trpzApStatDataObjects": trpzApStatDataObjects,
       "trpzApStatNumAps": trpzApStatNumAps,
       "trpzApStatApStatusTable": trpzApStatApStatusTable,
       "trpzApStatApStatusEntry": trpzApStatApStatusEntry,
       "trpzApStatApStatusSerialNum": trpzApStatApStatusSerialNum,
       "trpzApStatApStatusBaseMac": trpzApStatApStatusBaseMac,
       "trpzApStatApStatusAttachType": trpzApStatApStatusAttachType,
       "trpzApStatApStatusPortOrDapNum": trpzApStatApStatusPortOrDapNum,
       "trpzApStatApStatusApState": trpzApStatApStatusApState,
       "trpzApStatApStatusModel": trpzApStatApStatusModel,
       "trpzApStatApStatusFingerprint": trpzApStatApStatusFingerprint,
       "trpzApStatApStatusApName": trpzApStatApStatusApName,
       "trpzApStatApStatusVlan": trpzApStatApStatusVlan,
       "trpzApStatApStatusIpAddress": trpzApStatApStatusIpAddress,
       "trpzApStatApStatusUptimeSecs": trpzApStatApStatusUptimeSecs,
       "trpzApStatApStatusCpuInfo": trpzApStatApStatusCpuInfo,
       "trpzApStatApStatusManufacturerId": trpzApStatApStatusManufacturerId,
       "trpzApStatApStatusRamBytes": trpzApStatApStatusRamBytes,
       "trpzApStatApStatusHardwareRev": trpzApStatApStatusHardwareRev,
       "trpzApStatApStatusClientSessions": trpzApStatApStatusClientSessions,
       "trpzApStatApStatusSoftwareVer": trpzApStatApStatusSoftwareVer,
       "trpzApStatApStatusBootVer": trpzApStatApStatusBootVer,
       "trpzApStatApStatusApNum": trpzApStatApStatusApNum,
       "trpzApStatApStatusPhysPortNum": trpzApStatApStatusPhysPortNum,
       "trpzApStatApStatusIpNetmask": trpzApStatApStatusIpNetmask,
       "trpzApStatApStatusWiredIfNumber": trpzApStatApStatusWiredIfNumber,
       "trpzApStatApStatusMacTable": trpzApStatApStatusMacTable,
       "trpzApStatApStatusMacEntry": trpzApStatApStatusMacEntry,
       "trpzApStatApStatusMacBaseMac": trpzApStatApStatusMacBaseMac,
       "trpzApStatApStatusMacSerialNum": trpzApStatApStatusMacSerialNum,
       "trpzApStatApStatusMacAttachType": trpzApStatApStatusMacAttachType,
       "trpzApStatApStatusMacPortOrDapNum": trpzApStatApStatusMacPortOrDapNum,
       "trpzApStatApStatusMacApState": trpzApStatApStatusMacApState,
       "trpzApStatApStatusMacModel": trpzApStatApStatusMacModel,
       "trpzApStatApStatusMacFingerprint": trpzApStatApStatusMacFingerprint,
       "trpzApStatApStatusMacApName": trpzApStatApStatusMacApName,
       "trpzApStatApStatusMacVlan": trpzApStatApStatusMacVlan,
       "trpzApStatApStatusMacIpAddress": trpzApStatApStatusMacIpAddress,
       "trpzApStatApStatusMacUptimeSecs": trpzApStatApStatusMacUptimeSecs,
       "trpzApStatApStatusMacCpuInfo": trpzApStatApStatusMacCpuInfo,
       "trpzApStatApStatusMacManufacturerId": trpzApStatApStatusMacManufacturerId,
       "trpzApStatApStatusMacRamBytes": trpzApStatApStatusMacRamBytes,
       "trpzApStatApStatusMacHardwareRev": trpzApStatApStatusMacHardwareRev,
       "trpzApStatApStatusMacClientSessions": trpzApStatApStatusMacClientSessions,
       "trpzApStatApStatusMacSoftwareVer": trpzApStatApStatusMacSoftwareVer,
       "trpzApStatApStatusMacBootVer": trpzApStatApStatusMacBootVer,
       "trpzApStatApStatusMacApNum": trpzApStatApStatusMacApNum,
       "trpzApStatApStatusMacPhysPortNum": trpzApStatApStatusMacPhysPortNum,
       "trpzApStatApStatusMacIpNetmask": trpzApStatApStatusMacIpNetmask,
       "trpzApStatApStatusMacWiredIfNumber": trpzApStatApStatusMacWiredIfNumber,
       "trpzApStatRadioStatusTable": trpzApStatRadioStatusTable,
       "trpzApStatRadioStatusEntry": trpzApStatRadioStatusEntry,
       "trpzApStatRadioStatusApSerialNum": trpzApStatRadioStatusApSerialNum,
       "trpzApStatRadioStatusRadioNum": trpzApStatRadioStatusRadioNum,
       "trpzApStatRadioStatusBaseMac": trpzApStatRadioStatusBaseMac,
       "trpzApStatRadioStatusEnable": trpzApStatRadioStatusEnable,
       "trpzApStatRadioStatusRadioConfigState": trpzApStatRadioStatusRadioConfigState,
       "trpzApStatRadioStatusCurrentPowerLevel": trpzApStatRadioStatusCurrentPowerLevel,
       "trpzApStatRadioStatusCurrentChannelNum": trpzApStatRadioStatusCurrentChannelNum,
       "trpzApStatRadioStatusClientSessions": trpzApStatRadioStatusClientSessions,
       "trpzApStatRadioStatusMaxPowerLevel": trpzApStatRadioStatusMaxPowerLevel,
       "trpzApStatRadioStatusRadioPhyType": trpzApStatRadioStatusRadioPhyType,
       "trpzApStatRadioStatusRadioMode": trpzApStatRadioStatusRadioMode,
       "trpzApStatRadioStatusRadioChannelWidth": trpzApStatRadioStatusRadioChannelWidth,
       "trpzApStatRadioStatusRadioMimoState": trpzApStatRadioStatusRadioMimoState,
       "trpzApStatRadioStatusMinPowerLevel": trpzApStatRadioStatusMinPowerLevel,
       "trpzApStatRadioStatusRadioMimoRxChains": trpzApStatRadioStatusRadioMimoRxChains,
       "trpzApStatRadioStatusRadioMimoTxChains": trpzApStatRadioStatusRadioMimoTxChains,
       "trpzApStatRadioStatusSpectralDataCollect": trpzApStatRadioStatusSpectralDataCollect,
       "trpzApStatRadioStatusMacTable": trpzApStatRadioStatusMacTable,
       "trpzApStatRadioStatusMacEntry": trpzApStatRadioStatusMacEntry,
       "trpzApStatRadioStatusMacBaseMac": trpzApStatRadioStatusMacBaseMac,
       "trpzApStatRadioStatusMacApSerialNum": trpzApStatRadioStatusMacApSerialNum,
       "trpzApStatRadioStatusMacRadioNum": trpzApStatRadioStatusMacRadioNum,
       "trpzApStatRadioStatusMacEnable": trpzApStatRadioStatusMacEnable,
       "trpzApStatRadioStatusMacRadioConfigState": trpzApStatRadioStatusMacRadioConfigState,
       "trpzApStatRadioStatusMacCurrentPowerLevel": trpzApStatRadioStatusMacCurrentPowerLevel,
       "trpzApStatRadioStatusMacCurrentChannelNum": trpzApStatRadioStatusMacCurrentChannelNum,
       "trpzApStatRadioStatusMacClientSessions": trpzApStatRadioStatusMacClientSessions,
       "trpzApStatRadioStatusMacMaxPowerLevel": trpzApStatRadioStatusMacMaxPowerLevel,
       "trpzApStatRadioStatusMacRadioPhyType": trpzApStatRadioStatusMacRadioPhyType,
       "trpzApStatRadioStatusMacRadioMode": trpzApStatRadioStatusMacRadioMode,
       "trpzApStatRadioStatusMacRadioChannelWidth": trpzApStatRadioStatusMacRadioChannelWidth,
       "trpzApStatRadioStatusMacRadioMimoState": trpzApStatRadioStatusMacRadioMimoState,
       "trpzApStatRadioStatusMacMinPowerLevel": trpzApStatRadioStatusMacMinPowerLevel,
       "trpzApStatRadioStatusMacRadioMimoRxChains": trpzApStatRadioStatusMacRadioMimoRxChains,
       "trpzApStatRadioStatusMacRadioMimoTxChains": trpzApStatRadioStatusMacRadioMimoTxChains,
       "trpzApStatRadioStatusMacSpectralDataCollect": trpzApStatRadioStatusMacSpectralDataCollect,
       "trpzApStatRadioServiceTable": trpzApStatRadioServiceTable,
       "trpzApStatRadioServiceEntry": trpzApStatRadioServiceEntry,
       "trpzApStatRadioServApSerialNum": trpzApStatRadioServApSerialNum,
       "trpzApStatRadioServRadioNum": trpzApStatRadioServRadioNum,
       "trpzApStatRadioServSsid": trpzApStatRadioServSsid,
       "trpzApStatRadioServBssid": trpzApStatRadioServBssid,
       "trpzApStatRadioServServiceProfileName": trpzApStatRadioServServiceProfileName,
       "trpzApStatRadioServiceMacTable": trpzApStatRadioServiceMacTable,
       "trpzApStatRadioServiceMacEntry": trpzApStatRadioServiceMacEntry,
       "trpzApStatRadioServMacBssid": trpzApStatRadioServMacBssid,
       "trpzApStatRadioServMacApSerialNum": trpzApStatRadioServMacApSerialNum,
       "trpzApStatRadioServMacRadioNum": trpzApStatRadioServMacRadioNum,
       "trpzApStatRadioServMacSsid": trpzApStatRadioServMacSsid,
       "trpzApStatRadioServMacServiceProfileName": trpzApStatRadioServMacServiceProfileName,
       "trpzApStatRadioServiceOpRateSetTable": trpzApStatRadioServiceOpRateSetTable,
       "trpzApStatRadioServiceOpRateSetEntry": trpzApStatRadioServiceOpRateSetEntry,
       "trpzApStatRadioSORSetApSerialNum": trpzApStatRadioSORSetApSerialNum,
       "trpzApStatRadioSORSetRadioNum": trpzApStatRadioSORSetRadioNum,
       "trpzApStatRadioSORSetSsid": trpzApStatRadioSORSetSsid,
       "trpzApStatRadioSORSetMandatory": trpzApStatRadioSORSetMandatory,
       "trpzApStatRadioSORSetDisabled": trpzApStatRadioSORSetDisabled,
       "trpzApStatRadioSORSetBeacon": trpzApStatRadioSORSetBeacon,
       "trpzApStatRadioSORSetMulticast": trpzApStatRadioSORSetMulticast,
       "trpzApStatRadioServiceOpRateSetMacTable": trpzApStatRadioServiceOpRateSetMacTable,
       "trpzApStatRadioServiceOpRateSetMacEntry": trpzApStatRadioServiceOpRateSetMacEntry,
       "trpzApStatRadioSORSetMacBssid": trpzApStatRadioSORSetMacBssid,
       "trpzApStatRadioSORSetMacMandatory": trpzApStatRadioSORSetMacMandatory,
       "trpzApStatRadioSORSetMacDisabled": trpzApStatRadioSORSetMacDisabled,
       "trpzApStatRadioSORSetMacBeacon": trpzApStatRadioSORSetMacBeacon,
       "trpzApStatRadioSORSetMacMulticast": trpzApStatRadioSORSetMacMulticast,
       "trpzApStatRadioOpStatisticsTable": trpzApStatRadioOpStatisticsTable,
       "trpzApStatRadioOpStatisticsEntry": trpzApStatRadioOpStatisticsEntry,
       "trpzApStatRadioOpStatsApSerialNum": trpzApStatRadioOpStatsApSerialNum,
       "trpzApStatRadioOpStatsRadioNum": trpzApStatRadioOpStatsRadioNum,
       "trpzApStatRadioOpStatsTxUniPkt": trpzApStatRadioOpStatsTxUniPkt,
       "trpzApStatRadioOpStatsTxUniOctet": trpzApStatRadioOpStatsTxUniOctet,
       "trpzApStatRadioOpStatsTxMultiPkt": trpzApStatRadioOpStatsTxMultiPkt,
       "trpzApStatRadioOpStatsTxMultiOctet": trpzApStatRadioOpStatsTxMultiOctet,
       "trpzApStatRadioOpStatsRxPkt": trpzApStatRadioOpStatsRxPkt,
       "trpzApStatRadioOpStatsRxOctet": trpzApStatRadioOpStatsRxOctet,
       "trpzApStatRadioOpStatsUndcrptPkt": trpzApStatRadioOpStatsUndcrptPkt,
       "trpzApStatRadioOpStatsUndcrptOctet": trpzApStatRadioOpStatsUndcrptOctet,
       "trpzApStatRadioOpStatsPhyErr": trpzApStatRadioOpStatsPhyErr,
       "trpzApStatRadioOpStatsResetCount": trpzApStatRadioOpStatsResetCount,
       "trpzApStatRadioOpStatsAutoTuneChannelChangeCount": trpzApStatRadioOpStatsAutoTuneChannelChangeCount,
       "trpzApStatRadioOpStatsTxRetriesCount": trpzApStatRadioOpStatsTxRetriesCount,
       "trpzApStatRadioOpStatsUserSessions": trpzApStatRadioOpStatsUserSessions,
       "trpzApStatRadioOpStatsNoiseFloor": trpzApStatRadioOpStatsNoiseFloor,
       "trpzApStatRadioOpStatsClientAssociations": trpzApStatRadioOpStatsClientAssociations,
       "trpzApStatRadioOpStatsClientFailedAssociations": trpzApStatRadioOpStatsClientFailedAssociations,
       "trpzApStatRadioOpStatsClientReAssociations": trpzApStatRadioOpStatsClientReAssociations,
       "trpzApStatRadioOpStatsSignalingPkt": trpzApStatRadioOpStatsSignalingPkt,
       "trpzApStatRadioOpStatsReTransmitOctet": trpzApStatRadioOpStatsReTransmitOctet,
       "trpzApStatRadioOpStatsRefusedConnectionCount": trpzApStatRadioOpStatsRefusedConnectionCount,
       "trpzApStatRadioOpStatsRxDataPkt": trpzApStatRadioOpStatsRxDataPkt,
       "trpzApStatRadioOpStatsRxAuthPkt": trpzApStatRadioOpStatsRxAuthPkt,
       "trpzApStatRadioOpStatsRxAssocPkt": trpzApStatRadioOpStatsRxAssocPkt,
       "trpzApStatRadioOpStatsTxDataPkt": trpzApStatRadioOpStatsTxDataPkt,
       "trpzApStatRadioOpStatsTxAuthRespPkt": trpzApStatRadioOpStatsTxAuthRespPkt,
       "trpzApStatRadioOpStatsTxAssocRespPkt": trpzApStatRadioOpStatsTxAssocRespPkt,
       "trpzApStatRadioOpStatisticsMacTable": trpzApStatRadioOpStatisticsMacTable,
       "trpzApStatRadioOpStatisticsMacEntry": trpzApStatRadioOpStatisticsMacEntry,
       "trpzApStatRadioOpStatsMacBaseMac": trpzApStatRadioOpStatsMacBaseMac,
       "trpzApStatRadioOpStatsMacTxUniPkt": trpzApStatRadioOpStatsMacTxUniPkt,
       "trpzApStatRadioOpStatsMacTxUniOctet": trpzApStatRadioOpStatsMacTxUniOctet,
       "trpzApStatRadioOpStatsMacTxMultiPkt": trpzApStatRadioOpStatsMacTxMultiPkt,
       "trpzApStatRadioOpStatsMacTxMultiOctet": trpzApStatRadioOpStatsMacTxMultiOctet,
       "trpzApStatRadioOpStatsMacRxPkt": trpzApStatRadioOpStatsMacRxPkt,
       "trpzApStatRadioOpStatsMacRxOctet": trpzApStatRadioOpStatsMacRxOctet,
       "trpzApStatRadioOpStatsMacUndcrptPkt": trpzApStatRadioOpStatsMacUndcrptPkt,
       "trpzApStatRadioOpStatsMacUndcrptOctet": trpzApStatRadioOpStatsMacUndcrptOctet,
       "trpzApStatRadioOpStatsMacPhyErr": trpzApStatRadioOpStatsMacPhyErr,
       "trpzApStatRadioOpStatsMacResetCount": trpzApStatRadioOpStatsMacResetCount,
       "trpzApStatRadioOpStatsMacAutoTuneChannelChangeCount": trpzApStatRadioOpStatsMacAutoTuneChannelChangeCount,
       "trpzApStatRadioOpStatsMacTxRetriesCount": trpzApStatRadioOpStatsMacTxRetriesCount,
       "trpzApStatRadioOpStatsMacUserSessions": trpzApStatRadioOpStatsMacUserSessions,
       "trpzApStatRadioOpStatsMacNoiseFloor": trpzApStatRadioOpStatsMacNoiseFloor,
       "trpzApStatRadioOpStatsMacClientAssociations": trpzApStatRadioOpStatsMacClientAssociations,
       "trpzApStatRadioOpStatsMacClientFailedAssociations": trpzApStatRadioOpStatsMacClientFailedAssociations,
       "trpzApStatRadioOpStatsMacClientReAssociations": trpzApStatRadioOpStatsMacClientReAssociations,
       "trpzApStatRadioOpStatsMacSignalingPkt": trpzApStatRadioOpStatsMacSignalingPkt,
       "trpzApStatRadioOpStatsMacReTransmitOctet": trpzApStatRadioOpStatsMacReTransmitOctet,
       "trpzApStatRadioOpStatsMacRefusedConnectionCount": trpzApStatRadioOpStatsMacRefusedConnectionCount,
       "trpzApStatRadioOpStatsMacRxDataPkt": trpzApStatRadioOpStatsMacRxDataPkt,
       "trpzApStatRadioOpStatsMacRxAuthPkt": trpzApStatRadioOpStatsMacRxAuthPkt,
       "trpzApStatRadioOpStatsMacRxAssocPkt": trpzApStatRadioOpStatsMacRxAssocPkt,
       "trpzApStatRadioOpStatsMacTxDataPkt": trpzApStatRadioOpStatsMacTxDataPkt,
       "trpzApStatRadioOpStatsMacTxAuthRespPkt": trpzApStatRadioOpStatsMacTxAuthRespPkt,
       "trpzApStatRadioOpStatsMacTxAssocRespPkt": trpzApStatRadioOpStatsMacTxAssocRespPkt,
       "trpzApStatRadioRateOpStatisticsTable": trpzApStatRadioRateOpStatisticsTable,
       "trpzApStatRadioRateOpStatisticsEntry": trpzApStatRadioRateOpStatisticsEntry,
       "trpzApStatRadioRateOpStatsApSerialNum": trpzApStatRadioRateOpStatsApSerialNum,
       "trpzApStatRadioRateOpStatsRadioNum": trpzApStatRadioRateOpStatsRadioNum,
       "trpzApStatRadioRateOpStatsRate": trpzApStatRadioRateOpStatsRate,
       "trpzApStatRadioRateOpStatsTxUniPkt": trpzApStatRadioRateOpStatsTxUniPkt,
       "trpzApStatRadioRateOpStatsTxUniOctet": trpzApStatRadioRateOpStatsTxUniOctet,
       "trpzApStatRadioRateOpStatsTxMultiPkt": trpzApStatRadioRateOpStatsTxMultiPkt,
       "trpzApStatRadioRateOpStatsTxMultiOctet": trpzApStatRadioRateOpStatsTxMultiOctet,
       "trpzApStatRadioRateOpStatsRxPkt": trpzApStatRadioRateOpStatsRxPkt,
       "trpzApStatRadioRateOpStatsRxOctet": trpzApStatRadioRateOpStatsRxOctet,
       "trpzApStatRadioRateOpStatsUndcrptPkt": trpzApStatRadioRateOpStatsUndcrptPkt,
       "trpzApStatRadioRateOpStatsUndcrptOctet": trpzApStatRadioRateOpStatsUndcrptOctet,
       "trpzApStatRadioRateOpStatsPhyErr": trpzApStatRadioRateOpStatsPhyErr,
       "trpzApStatRadioRateOpStatisticsMacTable": trpzApStatRadioRateOpStatisticsMacTable,
       "trpzApStatRadioRateOpStatisticsMacEntry": trpzApStatRadioRateOpStatisticsMacEntry,
       "trpzApStatRadioRateOpStatsMacBaseMac": trpzApStatRadioRateOpStatsMacBaseMac,
       "trpzApStatRadioRateOpStatsMacRate": trpzApStatRadioRateOpStatsMacRate,
       "trpzApStatRadioRateOpStatsMacTxUniPkt": trpzApStatRadioRateOpStatsMacTxUniPkt,
       "trpzApStatRadioRateOpStatsMacTxUniOctet": trpzApStatRadioRateOpStatsMacTxUniOctet,
       "trpzApStatRadioRateOpStatsMacTxMultiPkt": trpzApStatRadioRateOpStatsMacTxMultiPkt,
       "trpzApStatRadioRateOpStatsMacTxMultiOctet": trpzApStatRadioRateOpStatsMacTxMultiOctet,
       "trpzApStatRadioRateOpStatsMacRxPkt": trpzApStatRadioRateOpStatsMacRxPkt,
       "trpzApStatRadioRateOpStatsMacRxOctet": trpzApStatRadioRateOpStatsMacRxOctet,
       "trpzApStatRadioRateOpStatsMacUndcrptPkt": trpzApStatRadioRateOpStatsMacUndcrptPkt,
       "trpzApStatRadioRateOpStatsMacUndcrptOctet": trpzApStatRadioRateOpStatsMacUndcrptOctet,
       "trpzApStatRadioRateOpStatsMacPhyErr": trpzApStatRadioRateOpStatsMacPhyErr,
       "trpzApStatRadioRateExOpStatisticsTable": trpzApStatRadioRateExOpStatisticsTable,
       "trpzApStatRadioRateExOpStatisticsEntry": trpzApStatRadioRateExOpStatisticsEntry,
       "trpzApStatRadioRateExOpStatsApSerialNum": trpzApStatRadioRateExOpStatsApSerialNum,
       "trpzApStatRadioRateExOpStatsRadioNum": trpzApStatRadioRateExOpStatsRadioNum,
       "trpzApStatRadioRateExOpStatsRateEx": trpzApStatRadioRateExOpStatsRateEx,
       "trpzApStatRadioRateExOpStatsTxUniPkt": trpzApStatRadioRateExOpStatsTxUniPkt,
       "trpzApStatRadioRateExOpStatsTxUniOctet": trpzApStatRadioRateExOpStatsTxUniOctet,
       "trpzApStatRadioRateExOpStatsTxMultiPkt": trpzApStatRadioRateExOpStatsTxMultiPkt,
       "trpzApStatRadioRateExOpStatsTxMultiOctet": trpzApStatRadioRateExOpStatsTxMultiOctet,
       "trpzApStatRadioRateExOpStatsRxPkt": trpzApStatRadioRateExOpStatsRxPkt,
       "trpzApStatRadioRateExOpStatsRxOctet": trpzApStatRadioRateExOpStatsRxOctet,
       "trpzApStatRadioRateExOpStatsUndcrptPkt": trpzApStatRadioRateExOpStatsUndcrptPkt,
       "trpzApStatRadioRateExOpStatsUndcrptOctet": trpzApStatRadioRateExOpStatsUndcrptOctet,
       "trpzApStatRadioRateExOpStatsPhyErr": trpzApStatRadioRateExOpStatsPhyErr,
       "trpzApStatRadioRateExOpStatisticsMacTable": trpzApStatRadioRateExOpStatisticsMacTable,
       "trpzApStatRadioRateExOpStatisticsMacEntry": trpzApStatRadioRateExOpStatisticsMacEntry,
       "trpzApStatRadioRateExOpStatsMacBaseMac": trpzApStatRadioRateExOpStatsMacBaseMac,
       "trpzApStatRadioRateExOpStatsMacRateEx": trpzApStatRadioRateExOpStatsMacRateEx,
       "trpzApStatRadioRateExOpStatsMacTxUniPkt": trpzApStatRadioRateExOpStatsMacTxUniPkt,
       "trpzApStatRadioRateExOpStatsMacTxUniOctet": trpzApStatRadioRateExOpStatsMacTxUniOctet,
       "trpzApStatRadioRateExOpStatsMacTxMultiPkt": trpzApStatRadioRateExOpStatsMacTxMultiPkt,
       "trpzApStatRadioRateExOpStatsMacTxMultiOctet": trpzApStatRadioRateExOpStatsMacTxMultiOctet,
       "trpzApStatRadioRateExOpStatsMacRxPkt": trpzApStatRadioRateExOpStatsMacRxPkt,
       "trpzApStatRadioRateExOpStatsMacRxOctet": trpzApStatRadioRateExOpStatsMacRxOctet,
       "trpzApStatRadioRateExOpStatsMacUndcrptPkt": trpzApStatRadioRateExOpStatsMacUndcrptPkt,
       "trpzApStatRadioRateExOpStatsMacUndcrptOctet": trpzApStatRadioRateExOpStatsMacUndcrptOctet,
       "trpzApStatRadioRateExOpStatsMacPhyErr": trpzApStatRadioRateExOpStatsMacPhyErr,
       "trpzApStatusConformance": trpzApStatusConformance,
       "trpzApStatusCompliances": trpzApStatusCompliances,
       "trpzApStatusCompliance": trpzApStatusCompliance,
       "trpzApStatusComplianceRev2": trpzApStatusComplianceRev2,
       "trpzApStatusComplianceRev3": trpzApStatusComplianceRev3,
       "trpzApStatusComplianceRev4": trpzApStatusComplianceRev4,
       "trpzApStatusComplianceRev5": trpzApStatusComplianceRev5,
       "trpzApStatusComplianceRev6": trpzApStatusComplianceRev6,
       "trpzApStatusComplianceRev7": trpzApStatusComplianceRev7,
       "trpzApStatusGroups": trpzApStatusGroups,
       "trpzApStatusCommonGroup": trpzApStatusCommonGroup,
       "trpzApStatusScalarsGroup": trpzApStatusScalarsGroup,
       "trpzApStatusApStatusTablesGroup": trpzApStatusApStatusTablesGroup,
       "trpzApStatusRadioStatusTablesGroup": trpzApStatusRadioStatusTablesGroup,
       "trpzApStatusRadioServiceTablesGroup": trpzApStatusRadioServiceTablesGroup,
       "trpzApStatusRadioServiceOpRateSetTablesGroup": trpzApStatusRadioServiceOpRateSetTablesGroup,
       "trpzApStatusRadioOpStatisticsTablesGroup": trpzApStatusRadioOpStatisticsTablesGroup,
       "trpzApStatusRadioOpStatisticsPerRateTablesGroup": trpzApStatusRadioOpStatisticsPerRateTablesGroup,
       "trpzApStatusApStatusVersionsGroup": trpzApStatusApStatusVersionsGroup,
       "trpzApStatusApStatusTablesGroupRev2": trpzApStatusApStatusTablesGroupRev2,
       "trpzApStatusRadioStatusMaxPowerPhyTypeGroup": trpzApStatusRadioStatusMaxPowerPhyTypeGroup,
       "trpzApStatusRadioStatusTablesGroupRev2": trpzApStatusRadioStatusTablesGroupRev2,
       "trpzApStatusRadioStatusWideMimoGroup": trpzApStatusRadioStatusWideMimoGroup,
       "trpzApStatusRadioOpStatisticsPerRateExTablesGroup": trpzApStatusRadioOpStatisticsPerRateExTablesGroup,
       "trpzApStatusApStatusPhysPortNumGroup": trpzApStatusApStatusPhysPortNumGroup,
       "trpzApStatusApStatusConnectivityGroup": trpzApStatusApStatusConnectivityGroup,
       "trpzApStatusRadioStatusAntennaGroup": trpzApStatusRadioStatusAntennaGroup,
       "trpzApStatusRadioOpStatisticsClientAssocGroup": trpzApStatusRadioOpStatisticsClientAssocGroup,
       "trpzApStatusRadioOpStatisticsSignErrGroup": trpzApStatusRadioOpStatisticsSignErrGroup,
       "trpzApStatusRadioStatusWideMimoGroupRev2": trpzApStatusRadioStatusWideMimoGroupRev2,
       "trpzApStatusRadioOpStatisticsPktDetailGroup": trpzApStatusRadioOpStatisticsPktDetailGroup,
       "trpzApStatusRadioStatusSpectralDataGroup": trpzApStatusRadioStatusSpectralDataGroup}
)
