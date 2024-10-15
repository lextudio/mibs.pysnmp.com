# SNMP MIB module (HUAWEI-ETHOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ETHOAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:47 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifDescr",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hwEthOamMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1)
)
hwEthOamMib.setRevisions(
        ("2015-04-24 00:00",
         "2015-03-03 00:00",
         "2015-01-15 00:00",
         "2015-01-06 00:00",
         "2014-12-26 00:00",
         "2014-12-10 00:00",
         "2014-10-08 00:00",
         "2014-09-15 00:00",
         "2014-08-12 00:00",
         "2014-06-26 00:00",
         "2014-06-03 00:00",
         "2014-05-06 00:00",
         "2014-04-26 00:00",
         "2014-04-09 00:00",
         "2013-12-04 00:00",
         "2013-10-07 00:00",
         "2013-04-01 10:45",
         "2013-02-06 11:02")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWDetectType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastDetect", 2),
          ("normalDetect", 1))
    )



class HWDot3Oui(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class HWTestMessageSendSpeed(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiveMbps", 2),
          ("oneMbps", 1))
    )



class HWTestMessageFinishedValue(Integer32, TextualConvention):
    status = "current"
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
        *(("failed", 4),
          ("finished", 3),
          ("ready", 1),
          ("stop", 5),
          ("testing", 2))
    )



class HWDot1agCfmRelayActionFieldValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("rlyFdb", 2),
          ("rlyHit", 1),
          ("rlyInvalid", 255),
          ("rlyMpdb", 3))
    )



class HWDot1agCfmIngressActionFieldValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ingBlocked", 3),
          ("ingDown", 2),
          ("ingInvalid", 255),
          ("ingOk", 1),
          ("ingVid", 4))
    )



class HWDot1agCfmEgressActionFieldValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("egrBlocked", 3),
          ("egrDown", 2),
          ("egrInvalid", 255),
          ("egrOK", 1),
          ("egrVid", 4))
    )



class HWDot1agCfmHighestDefectPri(Integer32, TextualConvention):
    status = "current"
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
        *(("defErrorCCM", 4),
          ("defMACstatus", 2),
          ("defRDICCM", 1),
          ("defRemoteCCM", 3),
          ("defXconCCM", 5),
          ("none", 0))
    )



class HWDot1agCfmMDLevel(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_HwEthOam_ObjectIdentity = ObjectIdentity
hwEthOam = _HwEthOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136)
)
_HwEthOam1ag_ObjectIdentity = ObjectIdentity
hwEthOam1ag = _HwEthOam1ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1)
)
_HwDot1agCfmEnabled_Type = EnabledStatus
_HwDot1agCfmEnabled_Object = MibScalar
hwDot1agCfmEnabled = _HwDot1agCfmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 1),
    _HwDot1agCfmEnabled_Type()
)
hwDot1agCfmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1agCfmEnabled.setStatus("current")


class _HwDot1agCfmVersion_Type(Integer32):
    """Custom type hwDot1agCfmVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("draft7", 1),
          ("standard", 2))
    )


_HwDot1agCfmVersion_Type.__name__ = "Integer32"
_HwDot1agCfmVersion_Object = MibScalar
hwDot1agCfmVersion = _HwDot1agCfmVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 2),
    _HwDot1agCfmVersion_Type()
)
hwDot1agCfmVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1agCfmVersion.setStatus("current")
_HwDot1agCfmMdObject_ObjectIdentity = ObjectIdentity
hwDot1agCfmMdObject = _HwDot1agCfmMdObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3)
)
_HwDot1agCfmMdTableNextIndex_Type = Unsigned32
_HwDot1agCfmMdTableNextIndex_Object = MibScalar
hwDot1agCfmMdTableNextIndex = _HwDot1agCfmMdTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 1),
    _HwDot1agCfmMdTableNextIndex_Type()
)
hwDot1agCfmMdTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMdTableNextIndex.setStatus("current")
_HwDot1agCfmMdTable_Object = MibTable
hwDot1agCfmMdTable = _HwDot1agCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwDot1agCfmMdTable.setStatus("current")
_HwDot1agCfmMdEntry_Object = MibTableRow
hwDot1agCfmMdEntry = _HwDot1agCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 2, 1)
)
hwDot1agCfmMdEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmMdEntry.setStatus("current")
_HwDot1agCfmMdIndex_Type = Unsigned32
_HwDot1agCfmMdIndex_Object = MibTableColumn
hwDot1agCfmMdIndex = _HwDot1agCfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 2, 1, 1),
    _HwDot1agCfmMdIndex_Type()
)
hwDot1agCfmMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmMdIndex.setStatus("current")


class _HwDot1agCfmMdFormat_Type(Integer32):
    """Custom type hwDot1agCfmMdFormat based on Integer32"""
    defaultValue = 4

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
        *(("dns", 2),
          ("macAddress", 3),
          ("noMdName", 1),
          ("string", 4))
    )


_HwDot1agCfmMdFormat_Type.__name__ = "Integer32"
_HwDot1agCfmMdFormat_Object = MibTableColumn
hwDot1agCfmMdFormat = _HwDot1agCfmMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 2, 1, 2),
    _HwDot1agCfmMdFormat_Type()
)
hwDot1agCfmMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMdFormat.setStatus("current")


class _HwDot1agCfmMdName_Type(OctetString):
    """Custom type hwDot1agCfmMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwDot1agCfmMdName_Type.__name__ = "OctetString"
_HwDot1agCfmMdName_Object = MibTableColumn
hwDot1agCfmMdName = _HwDot1agCfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 2, 1, 3),
    _HwDot1agCfmMdName_Type()
)
hwDot1agCfmMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMdName.setStatus("current")


class _HwDot1agCfmMdMdLevel_Type(HWDot1agCfmMDLevel):
    """Custom type hwDot1agCfmMdMdLevel based on HWDot1agCfmMDLevel"""
    defaultValue = 0


_HwDot1agCfmMdMdLevel_Object = MibTableColumn
hwDot1agCfmMdMdLevel = _HwDot1agCfmMdMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 2, 1, 4),
    _HwDot1agCfmMdMdLevel_Type()
)
hwDot1agCfmMdMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMdMdLevel.setStatus("current")


class _HwDot1agCfmMdMhfCreation_Type(Integer32):
    """Custom type hwDot1agCfmMdMhfCreation based on Integer32"""
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
        *(("defMHFdefault", 2),
          ("defMHFexplicit", 3),
          ("defMHFnone", 1))
    )


_HwDot1agCfmMdMhfCreation_Type.__name__ = "Integer32"
_HwDot1agCfmMdMhfCreation_Object = MibTableColumn
hwDot1agCfmMdMhfCreation = _HwDot1agCfmMdMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 2, 1, 5),
    _HwDot1agCfmMdMhfCreation_Type()
)
hwDot1agCfmMdMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMdMhfCreation.setStatus("current")


class _HwDot1agCfmMdMhfIdPermission_Type(Integer32):
    """Custom type hwDot1agCfmMdMhfIdPermission based on Integer32"""
    defaultValue = 5

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
        *(("sendIdChassis", 2),
          ("sendIdChassisManage", 4),
          ("sendIdDefer", 5),
          ("sendIdManage", 3),
          ("sendIdNone", 1))
    )


_HwDot1agCfmMdMhfIdPermission_Type.__name__ = "Integer32"
_HwDot1agCfmMdMhfIdPermission_Object = MibTableColumn
hwDot1agCfmMdMhfIdPermission = _HwDot1agCfmMdMhfIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 2, 1, 6),
    _HwDot1agCfmMdMhfIdPermission_Type()
)
hwDot1agCfmMdMhfIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMdMhfIdPermission.setStatus("current")


class _HwDot1agCfmMdFormatName_Type(OctetString):
    """Custom type hwDot1agCfmMdFormatName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 43),
    )


_HwDot1agCfmMdFormatName_Type.__name__ = "OctetString"
_HwDot1agCfmMdFormatName_Object = MibTableColumn
hwDot1agCfmMdFormatName = _HwDot1agCfmMdFormatName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 2, 1, 7),
    _HwDot1agCfmMdFormatName_Type()
)
hwDot1agCfmMdFormatName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMdFormatName.setStatus("current")
_HwDot1agCfmMdRowStatus_Type = RowStatus
_HwDot1agCfmMdRowStatus_Object = MibTableColumn
hwDot1agCfmMdRowStatus = _HwDot1agCfmMdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 3, 2, 1, 99),
    _HwDot1agCfmMdRowStatus_Type()
)
hwDot1agCfmMdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMdRowStatus.setStatus("current")
_HwDot1agCfmMaObject_ObjectIdentity = ObjectIdentity
hwDot1agCfmMaObject = _HwDot1agCfmMaObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4)
)
_HwDot1agCfmMaNextIndex_Type = Unsigned32
_HwDot1agCfmMaNextIndex_Object = MibScalar
hwDot1agCfmMaNextIndex = _HwDot1agCfmMaNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 1),
    _HwDot1agCfmMaNextIndex_Type()
)
hwDot1agCfmMaNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMaNextIndex.setStatus("current")
_HwDot1agCfmMaTable_Object = MibTable
hwDot1agCfmMaTable = _HwDot1agCfmMaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hwDot1agCfmMaTable.setStatus("current")
_HwDot1agCfmMaEntry_Object = MibTableRow
hwDot1agCfmMaEntry = _HwDot1agCfmMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1)
)
hwDot1agCfmMaEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmMaEntry.setStatus("current")
_HwDot1agCfmMaIndex_Type = Unsigned32
_HwDot1agCfmMaIndex_Object = MibTableColumn
hwDot1agCfmMaIndex = _HwDot1agCfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 1),
    _HwDot1agCfmMaIndex_Type()
)
hwDot1agCfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmMaIndex.setStatus("current")


class _HwDot1agCfmMaName_Type(OctetString):
    """Custom type hwDot1agCfmMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwDot1agCfmMaName_Type.__name__ = "OctetString"
_HwDot1agCfmMaName_Object = MibTableColumn
hwDot1agCfmMaName = _HwDot1agCfmMaName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 2),
    _HwDot1agCfmMaName_Type()
)
hwDot1agCfmMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaName.setStatus("current")


class _HwDot1agCfmMaMapType_Type(Integer32):
    """Custom type hwDot1agCfmMaMapType based on Integer32"""
    defaultValue = 4

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
        *(("mapCcc", 5),
          ("mapL2vc", 3),
          ("mapVlan", 1),
          ("mapVsi", 2),
          ("unbind", 4))
    )


_HwDot1agCfmMaMapType_Type.__name__ = "Integer32"
_HwDot1agCfmMaMapType_Object = MibTableColumn
hwDot1agCfmMaMapType = _HwDot1agCfmMaMapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 3),
    _HwDot1agCfmMaMapType_Type()
)
hwDot1agCfmMaMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaMapType.setStatus("current")
_HwDot1agCfmMaMapVlanValue_Type = VlanIdOrNone
_HwDot1agCfmMaMapVlanValue_Object = MibTableColumn
hwDot1agCfmMaMapVlanValue = _HwDot1agCfmMaMapVlanValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 4),
    _HwDot1agCfmMaMapVlanValue_Type()
)
hwDot1agCfmMaMapVlanValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaMapVlanValue.setStatus("current")


class _HwDot1agCfmMaMapVsiName_Type(OctetString):
    """Custom type hwDot1agCfmMaMapVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwDot1agCfmMaMapVsiName_Type.__name__ = "OctetString"
_HwDot1agCfmMaMapVsiName_Object = MibTableColumn
hwDot1agCfmMaMapVsiName = _HwDot1agCfmMaMapVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 5),
    _HwDot1agCfmMaMapVsiName_Type()
)
hwDot1agCfmMaMapVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaMapVsiName.setStatus("current")
_HwDot1agCfmMaMapL2vcValue_Type = Unsigned32
_HwDot1agCfmMaMapL2vcValue_Object = MibTableColumn
hwDot1agCfmMaMapL2vcValue = _HwDot1agCfmMaMapL2vcValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 6),
    _HwDot1agCfmMaMapL2vcValue_Type()
)
hwDot1agCfmMaMapL2vcValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaMapL2vcValue.setStatus("current")


class _HwDot1agCfmMaMapL2vcType_Type(Integer32):
    """Custom type hwDot1agCfmMaMapL2vcType based on Integer32"""
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
        *(("invalid", 1),
          ("l2vcRaw", 2),
          ("l2vcTagged", 3))
    )


_HwDot1agCfmMaMapL2vcType_Type.__name__ = "Integer32"
_HwDot1agCfmMaMapL2vcType_Object = MibTableColumn
hwDot1agCfmMaMapL2vcType = _HwDot1agCfmMaMapL2vcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 7),
    _HwDot1agCfmMaMapL2vcType_Type()
)
hwDot1agCfmMaMapL2vcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaMapL2vcType.setStatus("current")


class _HwDot1agCfmMaPktPriority_Type(Integer32):
    """Custom type hwDot1agCfmMaPktPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwDot1agCfmMaPktPriority_Type.__name__ = "Integer32"
_HwDot1agCfmMaPktPriority_Object = MibTableColumn
hwDot1agCfmMaPktPriority = _HwDot1agCfmMaPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 8),
    _HwDot1agCfmMaPktPriority_Type()
)
hwDot1agCfmMaPktPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaPktPriority.setStatus("current")


class _HwDot1agCfmMaCcmInterval_Type(Integer32):
    """Custom type hwDot1agCfmMaCcmInterval based on Integer32"""
    defaultValue = 6

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("interval100ms", 5),
          ("interval10min", 10),
          ("interval10ms", 1),
          ("interval10s", 7),
          ("interval1min", 9),
          ("interval1s", 6),
          ("interval20ms", 2),
          ("interval30ms", 3),
          ("interval3Dot3ms", 8),
          ("interval50ms", 4))
    )


_HwDot1agCfmMaCcmInterval_Type.__name__ = "Integer32"
_HwDot1agCfmMaCcmInterval_Object = MibTableColumn
hwDot1agCfmMaCcmInterval = _HwDot1agCfmMaCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 9),
    _HwDot1agCfmMaCcmInterval_Type()
)
hwDot1agCfmMaCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaCcmInterval.setStatus("current")


class _HwDot1agCfmMaRmepActiveTime_Type(Integer32):
    """Custom type hwDot1agCfmMaRmepActiveTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HwDot1agCfmMaRmepActiveTime_Type.__name__ = "Integer32"
_HwDot1agCfmMaRmepActiveTime_Object = MibTableColumn
hwDot1agCfmMaRmepActiveTime = _HwDot1agCfmMaRmepActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 10),
    _HwDot1agCfmMaRmepActiveTime_Type()
)
hwDot1agCfmMaRmepActiveTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaRmepActiveTime.setStatus("current")


class _HwDot1agCfmMaMepFngAlarmTime_Type(Integer32):
    """Custom type hwDot1agCfmMaMepFngAlarmTime based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_HwDot1agCfmMaMepFngAlarmTime_Type.__name__ = "Integer32"
_HwDot1agCfmMaMepFngAlarmTime_Object = MibTableColumn
hwDot1agCfmMaMepFngAlarmTime = _HwDot1agCfmMaMepFngAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 11),
    _HwDot1agCfmMaMepFngAlarmTime_Type()
)
hwDot1agCfmMaMepFngAlarmTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaMepFngAlarmTime.setStatus("current")


class _HwDot1agCfmMaMepFngResetTime_Type(Integer32):
    """Custom type hwDot1agCfmMaMepFngResetTime based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_HwDot1agCfmMaMepFngResetTime_Type.__name__ = "Integer32"
_HwDot1agCfmMaMepFngResetTime_Object = MibTableColumn
hwDot1agCfmMaMepFngResetTime = _HwDot1agCfmMaMepFngResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 12),
    _HwDot1agCfmMaMepFngResetTime_Type()
)
hwDot1agCfmMaMepFngResetTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaMepFngResetTime.setStatus("current")


class _HwDot1agCfmMaFormat_Type(Integer32):
    """Custom type hwDot1agCfmMaFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              32)
        )
    )
    namedValues = NamedValues(
        *(("iccBased", 32),
          ("string", 2))
    )


_HwDot1agCfmMaFormat_Type.__name__ = "Integer32"
_HwDot1agCfmMaFormat_Object = MibTableColumn
hwDot1agCfmMaFormat = _HwDot1agCfmMaFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 13),
    _HwDot1agCfmMaFormat_Type()
)
hwDot1agCfmMaFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaFormat.setStatus("current")


class _HwDot1agCfmMaFormatName_Type(OctetString):
    """Custom type hwDot1agCfmMaFormatName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwDot1agCfmMaFormatName_Type.__name__ = "OctetString"
_HwDot1agCfmMaFormatName_Object = MibTableColumn
hwDot1agCfmMaFormatName = _HwDot1agCfmMaFormatName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 14),
    _HwDot1agCfmMaFormatName_Type()
)
hwDot1agCfmMaFormatName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaFormatName.setStatus("current")


class _HwDot1agCfmMaMapCccName_Type(OctetString):
    """Custom type hwDot1agCfmMaMapCccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwDot1agCfmMaMapCccName_Type.__name__ = "OctetString"
_HwDot1agCfmMaMapCccName_Object = MibTableColumn
hwDot1agCfmMaMapCccName = _HwDot1agCfmMaMapCccName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 15),
    _HwDot1agCfmMaMapCccName_Type()
)
hwDot1agCfmMaMapCccName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaMapCccName.setStatus("current")
_HwDot1agCfmMaRowStatus_Type = RowStatus
_HwDot1agCfmMaRowStatus_Object = MibTableColumn
hwDot1agCfmMaRowStatus = _HwDot1agCfmMaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 4, 2, 1, 99),
    _HwDot1agCfmMaRowStatus_Type()
)
hwDot1agCfmMaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMaRowStatus.setStatus("current")
_HwDot1agCfmMepObject_ObjectIdentity = ObjectIdentity
hwDot1agCfmMepObject = _HwDot1agCfmMepObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5)
)
_HwDot1agCfmMepTable_Object = MibTable
hwDot1agCfmMepTable = _HwDot1agCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwDot1agCfmMepTable.setStatus("current")
_HwDot1agCfmMepEntry_Object = MibTableRow
hwDot1agCfmMepEntry = _HwDot1agCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1)
)
hwDot1agCfmMepEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmMepEntry.setStatus("current")


class _HwDot1agCfmMepIdentifier_Type(Integer32):
    """Custom type hwDot1agCfmMepIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_HwDot1agCfmMepIdentifier_Type.__name__ = "Integer32"
_HwDot1agCfmMepIdentifier_Object = MibTableColumn
hwDot1agCfmMepIdentifier = _HwDot1agCfmMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1, 1),
    _HwDot1agCfmMepIdentifier_Type()
)
hwDot1agCfmMepIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDot1agCfmMepIdentifier.setStatus("current")
_HwDot1agCfmMepIsVlanType_Type = TruthValue
_HwDot1agCfmMepIsVlanType_Object = MibTableColumn
hwDot1agCfmMepIsVlanType = _HwDot1agCfmMepIsVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1, 2),
    _HwDot1agCfmMepIsVlanType_Type()
)
hwDot1agCfmMepIsVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMepIsVlanType.setStatus("current")


class _HwDot1agCfmMepIfIndex_Type(InterfaceIndexOrZero):
    """Custom type hwDot1agCfmMepIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_HwDot1agCfmMepIfIndex_Object = MibTableColumn
hwDot1agCfmMepIfIndex = _HwDot1agCfmMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1, 3),
    _HwDot1agCfmMepIfIndex_Type()
)
hwDot1agCfmMepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMepIfIndex.setStatus("current")
_HwDot1agCfmMepDot1qVlan_Type = VlanIdOrNone
_HwDot1agCfmMepDot1qVlan_Object = MibTableColumn
hwDot1agCfmMepDot1qVlan = _HwDot1agCfmMepDot1qVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1, 4),
    _HwDot1agCfmMepDot1qVlan_Type()
)
hwDot1agCfmMepDot1qVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMepDot1qVlan.setStatus("current")
_HwDot1agCfmMepPeVlan_Type = VlanIdOrNone
_HwDot1agCfmMepPeVlan_Object = MibTableColumn
hwDot1agCfmMepPeVlan = _HwDot1agCfmMepPeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1, 5),
    _HwDot1agCfmMepPeVlan_Type()
)
hwDot1agCfmMepPeVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMepPeVlan.setStatus("current")
_HwDot1agCfmMepCeVlan_Type = VlanIdOrNone
_HwDot1agCfmMepCeVlan_Object = MibTableColumn
hwDot1agCfmMepCeVlan = _HwDot1agCfmMepCeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1, 6),
    _HwDot1agCfmMepCeVlan_Type()
)
hwDot1agCfmMepCeVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMepCeVlan.setStatus("current")


class _HwDot1agCfmMepDirection_Type(Integer32):
    """Custom type hwDot1agCfmMepDirection based on Integer32"""
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
        *(("dirInward", 2),
          ("dirOutward", 3),
          ("invalid", 1))
    )


_HwDot1agCfmMepDirection_Type.__name__ = "Integer32"
_HwDot1agCfmMepDirection_Object = MibTableColumn
hwDot1agCfmMepDirection = _HwDot1agCfmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1, 7),
    _HwDot1agCfmMepDirection_Type()
)
hwDot1agCfmMepDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMepDirection.setStatus("current")


class _HwDot1agCfmMepCcmSendEnabled_Type(EnabledStatus):
    """Custom type hwDot1agCfmMepCcmSendEnabled based on EnabledStatus"""


_HwDot1agCfmMepCcmSendEnabled_Object = MibTableColumn
hwDot1agCfmMepCcmSendEnabled = _HwDot1agCfmMepCcmSendEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1, 8),
    _HwDot1agCfmMepCcmSendEnabled_Type()
)
hwDot1agCfmMepCcmSendEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMepCcmSendEnabled.setStatus("current")
_HwDot1agCfmMepMacAddress_Type = MacAddress
_HwDot1agCfmMepMacAddress_Object = MibTableColumn
hwDot1agCfmMepMacAddress = _HwDot1agCfmMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1, 9),
    _HwDot1agCfmMepMacAddress_Type()
)
hwDot1agCfmMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMepMacAddress.setStatus("current")
_HwDot1agCfmMepRowStatus_Type = RowStatus
_HwDot1agCfmMepRowStatus_Object = MibTableColumn
hwDot1agCfmMepRowStatus = _HwDot1agCfmMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 5, 1, 1, 99),
    _HwDot1agCfmMepRowStatus_Type()
)
hwDot1agCfmMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMepRowStatus.setStatus("current")
_HwDot1agCfmRMepObject_ObjectIdentity = ObjectIdentity
hwDot1agCfmRMepObject = _HwDot1agCfmRMepObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 6)
)
_HwDot1agCfmRMepTable_Object = MibTable
hwDot1agCfmRMepTable = _HwDot1agCfmRMepTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hwDot1agCfmRMepTable.setStatus("current")
_HwDot1agCfmRMepEntry_Object = MibTableRow
hwDot1agCfmRMepEntry = _HwDot1agCfmRMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 6, 1, 1)
)
hwDot1agCfmRMepEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmRMepEntry.setStatus("current")


class _HwDot1agCfmRMepIdentifier_Type(Integer32):
    """Custom type hwDot1agCfmRMepIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_HwDot1agCfmRMepIdentifier_Type.__name__ = "Integer32"
_HwDot1agCfmRMepIdentifier_Object = MibTableColumn
hwDot1agCfmRMepIdentifier = _HwDot1agCfmRMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 6, 1, 1, 1),
    _HwDot1agCfmRMepIdentifier_Type()
)
hwDot1agCfmRMepIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDot1agCfmRMepIdentifier.setStatus("current")
_HwDot1agCfmRMepMacAddress_Type = MacAddress
_HwDot1agCfmRMepMacAddress_Object = MibTableColumn
hwDot1agCfmRMepMacAddress = _HwDot1agCfmRMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 6, 1, 1, 2),
    _HwDot1agCfmRMepMacAddress_Type()
)
hwDot1agCfmRMepMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmRMepMacAddress.setStatus("current")


class _HwDot1agCfmRMepCcmRecvEnabled_Type(EnabledStatus):
    """Custom type hwDot1agCfmRMepCcmRecvEnabled based on EnabledStatus"""


_HwDot1agCfmRMepCcmRecvEnabled_Object = MibTableColumn
hwDot1agCfmRMepCcmRecvEnabled = _HwDot1agCfmRMepCcmRecvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 6, 1, 1, 3),
    _HwDot1agCfmRMepCcmRecvEnabled_Type()
)
hwDot1agCfmRMepCcmRecvEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmRMepCcmRecvEnabled.setStatus("current")


class _HwDot1agCfmRMepStateIsUp_Type(Integer32):
    """Custom type hwDot1agCfmRMepStateIsUp based on Integer32"""
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
          ("invalid", 3),
          ("up", 1))
    )


_HwDot1agCfmRMepStateIsUp_Type.__name__ = "Integer32"
_HwDot1agCfmRMepStateIsUp_Object = MibTableColumn
hwDot1agCfmRMepStateIsUp = _HwDot1agCfmRMepStateIsUp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 6, 1, 1, 4),
    _HwDot1agCfmRMepStateIsUp_Type()
)
hwDot1agCfmRMepStateIsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmRMepStateIsUp.setStatus("current")
_HwDot1agCfmRMepHighestPrDefect_Type = HWDot1agCfmHighestDefectPri
_HwDot1agCfmRMepHighestPrDefect_Object = MibTableColumn
hwDot1agCfmRMepHighestPrDefect = _HwDot1agCfmRMepHighestPrDefect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 6, 1, 1, 5),
    _HwDot1agCfmRMepHighestPrDefect_Type()
)
hwDot1agCfmRMepHighestPrDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmRMepHighestPrDefect.setStatus("current")
_HwDot1agCfmRMepRowStatus_Type = RowStatus
_HwDot1agCfmRMepRowStatus_Object = MibTableColumn
hwDot1agCfmRMepRowStatus = _HwDot1agCfmRMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 6, 1, 1, 99),
    _HwDot1agCfmRMepRowStatus_Type()
)
hwDot1agCfmRMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmRMepRowStatus.setStatus("current")
_HwDot1agCfmMipObject_ObjectIdentity = ObjectIdentity
hwDot1agCfmMipObject = _HwDot1agCfmMipObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 7)
)
_HwDot1agCfmMipTable_Object = MibTable
hwDot1agCfmMipTable = _HwDot1agCfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hwDot1agCfmMipTable.setStatus("current")
_HwDot1agCfmMipEntry_Object = MibTableRow
hwDot1agCfmMipEntry = _HwDot1agCfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 7, 1, 1)
)
hwDot1agCfmMipEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMipIfIndex"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmMipEntry.setStatus("current")
_HwDot1agCfmMipIfIndex_Type = InterfaceIndex
_HwDot1agCfmMipIfIndex_Object = MibTableColumn
hwDot1agCfmMipIfIndex = _HwDot1agCfmMipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 7, 1, 1, 1),
    _HwDot1agCfmMipIfIndex_Type()
)
hwDot1agCfmMipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmMipIfIndex.setStatus("current")
_HwDot1agCfmMipLevel_Type = HWDot1agCfmMDLevel
_HwDot1agCfmMipLevel_Object = MibTableColumn
hwDot1agCfmMipLevel = _HwDot1agCfmMipLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 7, 1, 1, 2),
    _HwDot1agCfmMipLevel_Type()
)
hwDot1agCfmMipLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMipLevel.setStatus("current")
_HwDot1agCfmMipIfMacAddress_Type = MacAddress
_HwDot1agCfmMipIfMacAddress_Object = MibTableColumn
hwDot1agCfmMipIfMacAddress = _HwDot1agCfmMipIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 7, 1, 1, 3),
    _HwDot1agCfmMipIfMacAddress_Type()
)
hwDot1agCfmMipIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMipIfMacAddress.setStatus("current")
_HwDot1agCfmMacPingObject_ObjectIdentity = ObjectIdentity
hwDot1agCfmMacPingObject = _HwDot1agCfmMacPingObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8)
)
_HwDot1agCfmMacPingTable_Object = MibTable
hwDot1agCfmMacPingTable = _HwDot1agCfmMacPingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingTable.setStatus("current")
_HwDot1agCfmMacPingEntry_Object = MibTableRow
hwDot1agCfmMacPingEntry = _HwDot1agCfmMacPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1)
)
hwDot1agCfmMacPingEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingIndex"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingEntry.setStatus("current")
_HwDot1agCfmMacPingIndex_Type = Unsigned32
_HwDot1agCfmMacPingIndex_Object = MibTableColumn
hwDot1agCfmMacPingIndex = _HwDot1agCfmMacPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 1),
    _HwDot1agCfmMacPingIndex_Type()
)
hwDot1agCfmMacPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingIndex.setStatus("current")


class _HwDot1agCfmMacPingState_Type(EnabledStatus):
    """Custom type hwDot1agCfmMacPingState based on EnabledStatus"""


_HwDot1agCfmMacPingState_Object = MibTableColumn
hwDot1agCfmMacPingState = _HwDot1agCfmMacPingState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 2),
    _HwDot1agCfmMacPingState_Type()
)
hwDot1agCfmMacPingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingState.setStatus("current")


class _HwDot1agCfmMacPingMdName_Type(OctetString):
    """Custom type hwDot1agCfmMacPingMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwDot1agCfmMacPingMdName_Type.__name__ = "OctetString"
_HwDot1agCfmMacPingMdName_Object = MibTableColumn
hwDot1agCfmMacPingMdName = _HwDot1agCfmMacPingMdName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 3),
    _HwDot1agCfmMacPingMdName_Type()
)
hwDot1agCfmMacPingMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingMdName.setStatus("current")


class _HwDot1agCfmMacPingMaName_Type(OctetString):
    """Custom type hwDot1agCfmMacPingMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwDot1agCfmMacPingMaName_Type.__name__ = "OctetString"
_HwDot1agCfmMacPingMaName_Object = MibTableColumn
hwDot1agCfmMacPingMaName = _HwDot1agCfmMacPingMaName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 4),
    _HwDot1agCfmMacPingMaName_Type()
)
hwDot1agCfmMacPingMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingMaName.setStatus("current")


class _HwDot1agCfmMacPingMepId_Type(Integer32):
    """Custom type hwDot1agCfmMacPingMepId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwDot1agCfmMacPingMepId_Type.__name__ = "Integer32"
_HwDot1agCfmMacPingMepId_Object = MibTableColumn
hwDot1agCfmMacPingMepId = _HwDot1agCfmMacPingMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 5),
    _HwDot1agCfmMacPingMepId_Type()
)
hwDot1agCfmMacPingMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingMepId.setStatus("current")
_HwDot1agCfmMacPingDestIsMepId_Type = TruthValue
_HwDot1agCfmMacPingDestIsMepId_Object = MibTableColumn
hwDot1agCfmMacPingDestIsMepId = _HwDot1agCfmMacPingDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 6),
    _HwDot1agCfmMacPingDestIsMepId_Type()
)
hwDot1agCfmMacPingDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingDestIsMepId.setStatus("current")


class _HwDot1agCfmMacPingDestMepId_Type(Integer32):
    """Custom type hwDot1agCfmMacPingDestMepId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwDot1agCfmMacPingDestMepId_Type.__name__ = "Integer32"
_HwDot1agCfmMacPingDestMepId_Object = MibTableColumn
hwDot1agCfmMacPingDestMepId = _HwDot1agCfmMacPingDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 7),
    _HwDot1agCfmMacPingDestMepId_Type()
)
hwDot1agCfmMacPingDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingDestMepId.setStatus("current")
_HwDot1agCfmMacPingMacAddress_Type = MacAddress
_HwDot1agCfmMacPingMacAddress_Object = MibTableColumn
hwDot1agCfmMacPingMacAddress = _HwDot1agCfmMacPingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 8),
    _HwDot1agCfmMacPingMacAddress_Type()
)
hwDot1agCfmMacPingMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingMacAddress.setStatus("current")


class _HwDot1agCfmMacPingOutIfIndex_Type(InterfaceIndexOrZero):
    """Custom type hwDot1agCfmMacPingOutIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_HwDot1agCfmMacPingOutIfIndex_Object = MibTableColumn
hwDot1agCfmMacPingOutIfIndex = _HwDot1agCfmMacPingOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 9),
    _HwDot1agCfmMacPingOutIfIndex_Type()
)
hwDot1agCfmMacPingOutIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingOutIfIndex.setStatus("current")


class _HwDot1agCfmMacPingTimeOut_Type(Unsigned32):
    """Custom type hwDot1agCfmMacPingTimeOut based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwDot1agCfmMacPingTimeOut_Type.__name__ = "Unsigned32"
_HwDot1agCfmMacPingTimeOut_Object = MibTableColumn
hwDot1agCfmMacPingTimeOut = _HwDot1agCfmMacPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 10),
    _HwDot1agCfmMacPingTimeOut_Type()
)
hwDot1agCfmMacPingTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingTimeOut.setStatus("current")


class _HwDot1agCfmMacPingCount_Type(Unsigned32):
    """Custom type hwDot1agCfmMacPingCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwDot1agCfmMacPingCount_Type.__name__ = "Unsigned32"
_HwDot1agCfmMacPingCount_Object = MibTableColumn
hwDot1agCfmMacPingCount = _HwDot1agCfmMacPingCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 11),
    _HwDot1agCfmMacPingCount_Type()
)
hwDot1agCfmMacPingCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingCount.setStatus("current")


class _HwDot1agCfmMacPingPacketSize_Type(Integer32):
    """Custom type hwDot1agCfmMacPingPacketSize based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9500),
    )


_HwDot1agCfmMacPingPacketSize_Type.__name__ = "Integer32"
_HwDot1agCfmMacPingPacketSize_Object = MibTableColumn
hwDot1agCfmMacPingPacketSize = _HwDot1agCfmMacPingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 12),
    _HwDot1agCfmMacPingPacketSize_Type()
)
hwDot1agCfmMacPingPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingPacketSize.setStatus("current")


class _HwDot1agCfmMacPingPriority_Type(Integer32):
    """Custom type hwDot1agCfmMacPingPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwDot1agCfmMacPingPriority_Type.__name__ = "Integer32"
_HwDot1agCfmMacPingPriority_Object = MibTableColumn
hwDot1agCfmMacPingPriority = _HwDot1agCfmMacPingPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 13),
    _HwDot1agCfmMacPingPriority_Type()
)
hwDot1agCfmMacPingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingPriority.setStatus("current")
_HwDot1agCfmMacPingSendPacketNum_Type = Counter32
_HwDot1agCfmMacPingSendPacketNum_Object = MibTableColumn
hwDot1agCfmMacPingSendPacketNum = _HwDot1agCfmMacPingSendPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 14),
    _HwDot1agCfmMacPingSendPacketNum_Type()
)
hwDot1agCfmMacPingSendPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingSendPacketNum.setStatus("current")
_HwDot1agCfmMacPingRecvPacketNum_Type = Counter32
_HwDot1agCfmMacPingRecvPacketNum_Object = MibTableColumn
hwDot1agCfmMacPingRecvPacketNum = _HwDot1agCfmMacPingRecvPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 15),
    _HwDot1agCfmMacPingRecvPacketNum_Type()
)
hwDot1agCfmMacPingRecvPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingRecvPacketNum.setStatus("current")


class _HwDot1agCfmMacPingPacketLossRatio_Type(Unsigned32):
    """Custom type hwDot1agCfmMacPingPacketLossRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwDot1agCfmMacPingPacketLossRatio_Type.__name__ = "Unsigned32"
_HwDot1agCfmMacPingPacketLossRatio_Object = MibTableColumn
hwDot1agCfmMacPingPacketLossRatio = _HwDot1agCfmMacPingPacketLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 16),
    _HwDot1agCfmMacPingPacketLossRatio_Type()
)
hwDot1agCfmMacPingPacketLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingPacketLossRatio.setStatus("current")
_HwDot1agCfmMacPingRecvTimeDelayMin_Type = Unsigned32
_HwDot1agCfmMacPingRecvTimeDelayMin_Object = MibTableColumn
hwDot1agCfmMacPingRecvTimeDelayMin = _HwDot1agCfmMacPingRecvTimeDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 17),
    _HwDot1agCfmMacPingRecvTimeDelayMin_Type()
)
hwDot1agCfmMacPingRecvTimeDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingRecvTimeDelayMin.setStatus("current")
_HwDot1agCfmMacPingRecvTimeDelayMax_Type = Unsigned32
_HwDot1agCfmMacPingRecvTimeDelayMax_Object = MibTableColumn
hwDot1agCfmMacPingRecvTimeDelayMax = _HwDot1agCfmMacPingRecvTimeDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 18),
    _HwDot1agCfmMacPingRecvTimeDelayMax_Type()
)
hwDot1agCfmMacPingRecvTimeDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingRecvTimeDelayMax.setStatus("current")
_HwDot1agCfmMacPingRecvTimeDelayAvg_Type = Unsigned32
_HwDot1agCfmMacPingRecvTimeDelayAvg_Object = MibTableColumn
hwDot1agCfmMacPingRecvTimeDelayAvg = _HwDot1agCfmMacPingRecvTimeDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 19),
    _HwDot1agCfmMacPingRecvTimeDelayAvg_Type()
)
hwDot1agCfmMacPingRecvTimeDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingRecvTimeDelayAvg.setStatus("current")
_HwDot1agCfmMacPingRowStatus_Type = RowStatus
_HwDot1agCfmMacPingRowStatus_Object = MibTableColumn
hwDot1agCfmMacPingRowStatus = _HwDot1agCfmMacPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 8, 1, 1, 99),
    _HwDot1agCfmMacPingRowStatus_Type()
)
hwDot1agCfmMacPingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingRowStatus.setStatus("current")
_HwDot1agCfmMacTraceObjects_ObjectIdentity = ObjectIdentity
hwDot1agCfmMacTraceObjects = _HwDot1agCfmMacTraceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9)
)
_HwDot1agCfmMacTraceTable_Object = MibTable
hwDot1agCfmMacTraceTable = _HwDot1agCfmMacTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceTable.setStatus("current")
_HwDot1agCfmMacTraceEntry_Object = MibTableRow
hwDot1agCfmMacTraceEntry = _HwDot1agCfmMacTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1)
)
hwDot1agCfmMacTraceEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceIndex"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceEntry.setStatus("current")
_HwDot1agCfmMacTraceIndex_Type = Unsigned32
_HwDot1agCfmMacTraceIndex_Object = MibTableColumn
hwDot1agCfmMacTraceIndex = _HwDot1agCfmMacTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 1),
    _HwDot1agCfmMacTraceIndex_Type()
)
hwDot1agCfmMacTraceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceIndex.setStatus("current")


class _HwDot1agCfmMacTraceState_Type(EnabledStatus):
    """Custom type hwDot1agCfmMacTraceState based on EnabledStatus"""


_HwDot1agCfmMacTraceState_Object = MibTableColumn
hwDot1agCfmMacTraceState = _HwDot1agCfmMacTraceState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 2),
    _HwDot1agCfmMacTraceState_Type()
)
hwDot1agCfmMacTraceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceState.setStatus("current")


class _HwDot1agCfmMacTraceMdName_Type(OctetString):
    """Custom type hwDot1agCfmMacTraceMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwDot1agCfmMacTraceMdName_Type.__name__ = "OctetString"
_HwDot1agCfmMacTraceMdName_Object = MibTableColumn
hwDot1agCfmMacTraceMdName = _HwDot1agCfmMacTraceMdName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 3),
    _HwDot1agCfmMacTraceMdName_Type()
)
hwDot1agCfmMacTraceMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceMdName.setStatus("current")


class _HwDot1agCfmMacTraceMaName_Type(OctetString):
    """Custom type hwDot1agCfmMacTraceMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwDot1agCfmMacTraceMaName_Type.__name__ = "OctetString"
_HwDot1agCfmMacTraceMaName_Object = MibTableColumn
hwDot1agCfmMacTraceMaName = _HwDot1agCfmMacTraceMaName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 4),
    _HwDot1agCfmMacTraceMaName_Type()
)
hwDot1agCfmMacTraceMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceMaName.setStatus("current")


class _HwDot1agCfmMacTraceMepId_Type(Integer32):
    """Custom type hwDot1agCfmMacTraceMepId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwDot1agCfmMacTraceMepId_Type.__name__ = "Integer32"
_HwDot1agCfmMacTraceMepId_Object = MibTableColumn
hwDot1agCfmMacTraceMepId = _HwDot1agCfmMacTraceMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 5),
    _HwDot1agCfmMacTraceMepId_Type()
)
hwDot1agCfmMacTraceMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceMepId.setStatus("current")
_HwDot1agCfmMacTraceDestIsMepId_Type = TruthValue
_HwDot1agCfmMacTraceDestIsMepId_Object = MibTableColumn
hwDot1agCfmMacTraceDestIsMepId = _HwDot1agCfmMacTraceDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 6),
    _HwDot1agCfmMacTraceDestIsMepId_Type()
)
hwDot1agCfmMacTraceDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceDestIsMepId.setStatus("current")


class _HwDot1agCfmMacTraceDestMepId_Type(Integer32):
    """Custom type hwDot1agCfmMacTraceDestMepId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwDot1agCfmMacTraceDestMepId_Type.__name__ = "Integer32"
_HwDot1agCfmMacTraceDestMepId_Object = MibTableColumn
hwDot1agCfmMacTraceDestMepId = _HwDot1agCfmMacTraceDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 7),
    _HwDot1agCfmMacTraceDestMepId_Type()
)
hwDot1agCfmMacTraceDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceDestMepId.setStatus("current")
_HwDot1agCfmMacTraceMacAddress_Type = MacAddress
_HwDot1agCfmMacTraceMacAddress_Object = MibTableColumn
hwDot1agCfmMacTraceMacAddress = _HwDot1agCfmMacTraceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 8),
    _HwDot1agCfmMacTraceMacAddress_Type()
)
hwDot1agCfmMacTraceMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceMacAddress.setStatus("current")


class _HwDot1agCfmMacTraceOutIfIndex_Type(InterfaceIndexOrZero):
    """Custom type hwDot1agCfmMacTraceOutIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_HwDot1agCfmMacTraceOutIfIndex_Object = MibTableColumn
hwDot1agCfmMacTraceOutIfIndex = _HwDot1agCfmMacTraceOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 9),
    _HwDot1agCfmMacTraceOutIfIndex_Type()
)
hwDot1agCfmMacTraceOutIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceOutIfIndex.setStatus("current")


class _HwDot1agCfmMacTraceTimeOut_Type(Unsigned32):
    """Custom type hwDot1agCfmMacTraceTimeOut based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwDot1agCfmMacTraceTimeOut_Type.__name__ = "Unsigned32"
_HwDot1agCfmMacTraceTimeOut_Object = MibTableColumn
hwDot1agCfmMacTraceTimeOut = _HwDot1agCfmMacTraceTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 10),
    _HwDot1agCfmMacTraceTimeOut_Type()
)
hwDot1agCfmMacTraceTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceTimeOut.setStatus("current")


class _HwDot1agCfmMacTraceTTL_Type(Unsigned32):
    """Custom type hwDot1agCfmMacTraceTTL based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwDot1agCfmMacTraceTTL_Type.__name__ = "Unsigned32"
_HwDot1agCfmMacTraceTTL_Object = MibTableColumn
hwDot1agCfmMacTraceTTL = _HwDot1agCfmMacTraceTTL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 11),
    _HwDot1agCfmMacTraceTTL_Type()
)
hwDot1agCfmMacTraceTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceTTL.setStatus("current")
_HwDot1agCfmMacTraceSendSeqNumber_Type = Unsigned32
_HwDot1agCfmMacTraceSendSeqNumber_Object = MibTableColumn
hwDot1agCfmMacTraceSendSeqNumber = _HwDot1agCfmMacTraceSendSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 12),
    _HwDot1agCfmMacTraceSendSeqNumber_Type()
)
hwDot1agCfmMacTraceSendSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceSendSeqNumber.setStatus("current")


class _HwDot1agCfmMacTraceResult_Type(Integer32):
    """Custom type hwDot1agCfmMacTraceResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("invalid", 1),
          ("successful", 2))
    )


_HwDot1agCfmMacTraceResult_Type.__name__ = "Integer32"
_HwDot1agCfmMacTraceResult_Object = MibTableColumn
hwDot1agCfmMacTraceResult = _HwDot1agCfmMacTraceResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 13),
    _HwDot1agCfmMacTraceResult_Type()
)
hwDot1agCfmMacTraceResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceResult.setStatus("current")
_HwDot1agCfmMacTraceRowStatus_Type = RowStatus
_HwDot1agCfmMacTraceRowStatus_Object = MibTableColumn
hwDot1agCfmMacTraceRowStatus = _HwDot1agCfmMacTraceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 1, 1, 99),
    _HwDot1agCfmMacTraceRowStatus_Type()
)
hwDot1agCfmMacTraceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceRowStatus.setStatus("current")
_HwDot1agCfmMacTraceReplyTable_Object = MibTable
hwDot1agCfmMacTraceReplyTable = _HwDot1agCfmMacTraceReplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyTable.setStatus("current")
_HwDot1agCfmMacTraceReplyEntry_Object = MibTableRow
hwDot1agCfmMacTraceReplyEntry = _HwDot1agCfmMacTraceReplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1)
)
hwDot1agCfmMacTraceReplyEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplySeqNumber"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyRecvOrder"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyEntry.setStatus("current")
_HwDot1agCfmMacTraceReplySeqNumber_Type = Unsigned32
_HwDot1agCfmMacTraceReplySeqNumber_Object = MibTableColumn
hwDot1agCfmMacTraceReplySeqNumber = _HwDot1agCfmMacTraceReplySeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 1),
    _HwDot1agCfmMacTraceReplySeqNumber_Type()
)
hwDot1agCfmMacTraceReplySeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplySeqNumber.setStatus("current")
_HwDot1agCfmMacTraceReplyRecvOrder_Type = Unsigned32
_HwDot1agCfmMacTraceReplyRecvOrder_Object = MibTableColumn
hwDot1agCfmMacTraceReplyRecvOrder = _HwDot1agCfmMacTraceReplyRecvOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 2),
    _HwDot1agCfmMacTraceReplyRecvOrder_Type()
)
hwDot1agCfmMacTraceReplyRecvOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyRecvOrder.setStatus("current")


class _HwDot1agCfmMacTraceReplyTTL_Type(Unsigned32):
    """Custom type hwDot1agCfmMacTraceReplyTTL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwDot1agCfmMacTraceReplyTTL_Type.__name__ = "Unsigned32"
_HwDot1agCfmMacTraceReplyTTL_Object = MibTableColumn
hwDot1agCfmMacTraceReplyTTL = _HwDot1agCfmMacTraceReplyTTL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 3),
    _HwDot1agCfmMacTraceReplyTTL_Type()
)
hwDot1agCfmMacTraceReplyTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyTTL.setStatus("current")
_HwDot1agCfmMacTraceReplyForwarded_Type = TruthValue
_HwDot1agCfmMacTraceReplyForwarded_Object = MibTableColumn
hwDot1agCfmMacTraceReplyForwarded = _HwDot1agCfmMacTraceReplyForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 4),
    _HwDot1agCfmMacTraceReplyForwarded_Type()
)
hwDot1agCfmMacTraceReplyForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyForwarded.setStatus("current")
_HwDot1agCfmMacTraceReplyTerminalMep_Type = TruthValue
_HwDot1agCfmMacTraceReplyTerminalMep_Object = MibTableColumn
hwDot1agCfmMacTraceReplyTerminalMep = _HwDot1agCfmMacTraceReplyTerminalMep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 5),
    _HwDot1agCfmMacTraceReplyTerminalMep_Type()
)
hwDot1agCfmMacTraceReplyTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyTerminalMep.setStatus("current")
_HwDot1agCfmMacTraceReplyRelayAction_Type = HWDot1agCfmRelayActionFieldValue
_HwDot1agCfmMacTraceReplyRelayAction_Object = MibTableColumn
hwDot1agCfmMacTraceReplyRelayAction = _HwDot1agCfmMacTraceReplyRelayAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 6),
    _HwDot1agCfmMacTraceReplyRelayAction_Type()
)
hwDot1agCfmMacTraceReplyRelayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyRelayAction.setStatus("current")
_HwDot1agCfmMacTraceReplyIngressAction_Type = HWDot1agCfmIngressActionFieldValue
_HwDot1agCfmMacTraceReplyIngressAction_Object = MibTableColumn
hwDot1agCfmMacTraceReplyIngressAction = _HwDot1agCfmMacTraceReplyIngressAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 7),
    _HwDot1agCfmMacTraceReplyIngressAction_Type()
)
hwDot1agCfmMacTraceReplyIngressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyIngressAction.setStatus("current")
_HwDot1agCfmMacTraceReplyIngressMac_Type = MacAddress
_HwDot1agCfmMacTraceReplyIngressMac_Object = MibTableColumn
hwDot1agCfmMacTraceReplyIngressMac = _HwDot1agCfmMacTraceReplyIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 8),
    _HwDot1agCfmMacTraceReplyIngressMac_Type()
)
hwDot1agCfmMacTraceReplyIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyIngressMac.setStatus("current")
_HwDot1agCfmMacTraceReplyIngressIfName_Type = OctetString
_HwDot1agCfmMacTraceReplyIngressIfName_Object = MibTableColumn
hwDot1agCfmMacTraceReplyIngressIfName = _HwDot1agCfmMacTraceReplyIngressIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 9),
    _HwDot1agCfmMacTraceReplyIngressIfName_Type()
)
hwDot1agCfmMacTraceReplyIngressIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyIngressIfName.setStatus("current")
_HwDot1agCfmMacTraceReplyEgressAction_Type = HWDot1agCfmEgressActionFieldValue
_HwDot1agCfmMacTraceReplyEgressAction_Object = MibTableColumn
hwDot1agCfmMacTraceReplyEgressAction = _HwDot1agCfmMacTraceReplyEgressAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 10),
    _HwDot1agCfmMacTraceReplyEgressAction_Type()
)
hwDot1agCfmMacTraceReplyEgressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyEgressAction.setStatus("current")
_HwDot1agCfmMacTraceReplyEgressMac_Type = MacAddress
_HwDot1agCfmMacTraceReplyEgressMac_Object = MibTableColumn
hwDot1agCfmMacTraceReplyEgressMac = _HwDot1agCfmMacTraceReplyEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 11),
    _HwDot1agCfmMacTraceReplyEgressMac_Type()
)
hwDot1agCfmMacTraceReplyEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyEgressMac.setStatus("current")
_HwDot1agCfmMacTraceReplyEgressIfName_Type = OctetString
_HwDot1agCfmMacTraceReplyEgressIfName_Object = MibTableColumn
hwDot1agCfmMacTraceReplyEgressIfName = _HwDot1agCfmMacTraceReplyEgressIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 9, 2, 1, 12),
    _HwDot1agCfmMacTraceReplyEgressIfName_Type()
)
hwDot1agCfmMacTraceReplyEgressIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyEgressIfName.setStatus("current")
_HwDot1agCfmQueryObject_ObjectIdentity = ObjectIdentity
hwDot1agCfmQueryObject = _HwDot1agCfmQueryObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 10)
)
_HwDot1agCfmQueryMdIndexTable_Object = MibTable
hwDot1agCfmQueryMdIndexTable = _HwDot1agCfmQueryMdIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    hwDot1agCfmQueryMdIndexTable.setStatus("current")
_HwDot1agCfmQueryMdIndexEntry_Object = MibTableRow
hwDot1agCfmQueryMdIndexEntry = _HwDot1agCfmQueryMdIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 10, 1, 1)
)
hwDot1agCfmQueryMdIndexEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmQueryMdName"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmQueryMdIndexEntry.setStatus("current")


class _HwDot1agCfmQueryMdName_Type(OctetString):
    """Custom type hwDot1agCfmQueryMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwDot1agCfmQueryMdName_Type.__name__ = "OctetString"
_HwDot1agCfmQueryMdName_Object = MibTableColumn
hwDot1agCfmQueryMdName = _HwDot1agCfmQueryMdName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 10, 1, 1, 1),
    _HwDot1agCfmQueryMdName_Type()
)
hwDot1agCfmQueryMdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmQueryMdName.setStatus("current")
_HwDot1agCfmQueryMdIndex_Type = Unsigned32
_HwDot1agCfmQueryMdIndex_Object = MibTableColumn
hwDot1agCfmQueryMdIndex = _HwDot1agCfmQueryMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 10, 1, 1, 2),
    _HwDot1agCfmQueryMdIndex_Type()
)
hwDot1agCfmQueryMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmQueryMdIndex.setStatus("current")
_HwDot1agCfmQueryMaIndexTable_Object = MibTable
hwDot1agCfmQueryMaIndexTable = _HwDot1agCfmQueryMaIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    hwDot1agCfmQueryMaIndexTable.setStatus("current")
_HwDot1agCfmQueryMaIndexEntry_Object = MibTableRow
hwDot1agCfmQueryMaIndexEntry = _HwDot1agCfmQueryMaIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 10, 2, 1)
)
hwDot1agCfmQueryMaIndexEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmQueryMdName"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmQueryMaName"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmQueryMaIndexEntry.setStatus("current")


class _HwDot1agCfmQueryMaName_Type(OctetString):
    """Custom type hwDot1agCfmQueryMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwDot1agCfmQueryMaName_Type.__name__ = "OctetString"
_HwDot1agCfmQueryMaName_Object = MibTableColumn
hwDot1agCfmQueryMaName = _HwDot1agCfmQueryMaName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 10, 2, 1, 1),
    _HwDot1agCfmQueryMaName_Type()
)
hwDot1agCfmQueryMaName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmQueryMaName.setStatus("current")
_HwDot1agCfmQueryMaIndex_Type = Unsigned32
_HwDot1agCfmQueryMaIndex_Object = MibTableColumn
hwDot1agCfmQueryMaIndex = _HwDot1agCfmQueryMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 10, 2, 1, 2),
    _HwDot1agCfmQueryMaIndex_Type()
)
hwDot1agCfmQueryMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmQueryMaIndex.setStatus("current")
_HwDot1agCfmGmacTraceObjects_ObjectIdentity = ObjectIdentity
hwDot1agCfmGmacTraceObjects = _HwDot1agCfmGmacTraceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11)
)
_HwDot1agCfmGmacTraceEnabled_Type = EnabledStatus
_HwDot1agCfmGmacTraceEnabled_Object = MibScalar
hwDot1agCfmGmacTraceEnabled = _HwDot1agCfmGmacTraceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 1),
    _HwDot1agCfmGmacTraceEnabled_Type()
)
hwDot1agCfmGmacTraceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceEnabled.setStatus("current")
_HwDot1agCfmGmacTraceTable_Object = MibTable
hwDot1agCfmGmacTraceTable = _HwDot1agCfmGmacTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceTable.setStatus("current")
_HwDot1agCfmGmacTraceEntry_Object = MibTableRow
hwDot1agCfmGmacTraceEntry = _HwDot1agCfmGmacTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1)
)
hwDot1agCfmGmacTraceEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmGmacTraceIndex"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceEntry.setStatus("current")
_HwDot1agCfmGmacTraceIndex_Type = Unsigned32
_HwDot1agCfmGmacTraceIndex_Object = MibTableColumn
hwDot1agCfmGmacTraceIndex = _HwDot1agCfmGmacTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 1),
    _HwDot1agCfmGmacTraceIndex_Type()
)
hwDot1agCfmGmacTraceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceIndex.setStatus("current")


class _HwDot1agCfmGmacTraceState_Type(EnabledStatus):
    """Custom type hwDot1agCfmGmacTraceState based on EnabledStatus"""


_HwDot1agCfmGmacTraceState_Object = MibTableColumn
hwDot1agCfmGmacTraceState = _HwDot1agCfmGmacTraceState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 2),
    _HwDot1agCfmGmacTraceState_Type()
)
hwDot1agCfmGmacTraceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceState.setStatus("current")
_HwDot1agCfmGmacTraceMacAddress_Type = MacAddress
_HwDot1agCfmGmacTraceMacAddress_Object = MibTableColumn
hwDot1agCfmGmacTraceMacAddress = _HwDot1agCfmGmacTraceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 3),
    _HwDot1agCfmGmacTraceMacAddress_Type()
)
hwDot1agCfmGmacTraceMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceMacAddress.setStatus("current")


class _HwDot1agCfmGmacTraceServiceType_Type(Integer32):
    """Custom type hwDot1agCfmGmacTraceServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 255),
          ("vlan", 1))
    )


_HwDot1agCfmGmacTraceServiceType_Type.__name__ = "Integer32"
_HwDot1agCfmGmacTraceServiceType_Object = MibTableColumn
hwDot1agCfmGmacTraceServiceType = _HwDot1agCfmGmacTraceServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 4),
    _HwDot1agCfmGmacTraceServiceType_Type()
)
hwDot1agCfmGmacTraceServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceServiceType.setStatus("current")
_HwDot1agCfmGmacTraceVlanValue_Type = VlanIdOrNone
_HwDot1agCfmGmacTraceVlanValue_Object = MibTableColumn
hwDot1agCfmGmacTraceVlanValue = _HwDot1agCfmGmacTraceVlanValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 5),
    _HwDot1agCfmGmacTraceVlanValue_Type()
)
hwDot1agCfmGmacTraceVlanValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceVlanValue.setStatus("current")


class _HwDot1agCfmGmacTraceVsiName_Type(OctetString):
    """Custom type hwDot1agCfmGmacTraceVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwDot1agCfmGmacTraceVsiName_Type.__name__ = "OctetString"
_HwDot1agCfmGmacTraceVsiName_Object = MibTableColumn
hwDot1agCfmGmacTraceVsiName = _HwDot1agCfmGmacTraceVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 6),
    _HwDot1agCfmGmacTraceVsiName_Type()
)
hwDot1agCfmGmacTraceVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceVsiName.setStatus("current")
_HwDot1agCfmGmacTraceL2vcValue_Type = Unsigned32
_HwDot1agCfmGmacTraceL2vcValue_Object = MibTableColumn
hwDot1agCfmGmacTraceL2vcValue = _HwDot1agCfmGmacTraceL2vcValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 7),
    _HwDot1agCfmGmacTraceL2vcValue_Type()
)
hwDot1agCfmGmacTraceL2vcValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceL2vcValue.setStatus("current")


class _HwDot1agCfmGmacTraceL2vcType_Type(Integer32):
    """Custom type hwDot1agCfmGmacTraceL2vcType based on Integer32"""
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
        *(("invalid", 1),
          ("l2vcRaw", 2),
          ("l2vcTagged", 3))
    )


_HwDot1agCfmGmacTraceL2vcType_Type.__name__ = "Integer32"
_HwDot1agCfmGmacTraceL2vcType_Object = MibTableColumn
hwDot1agCfmGmacTraceL2vcType = _HwDot1agCfmGmacTraceL2vcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 8),
    _HwDot1agCfmGmacTraceL2vcType_Type()
)
hwDot1agCfmGmacTraceL2vcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceL2vcType.setStatus("current")
_HwDot1agCfmGmacTraceDot1qVlan_Type = VlanIdOrNone
_HwDot1agCfmGmacTraceDot1qVlan_Object = MibTableColumn
hwDot1agCfmGmacTraceDot1qVlan = _HwDot1agCfmGmacTraceDot1qVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 9),
    _HwDot1agCfmGmacTraceDot1qVlan_Type()
)
hwDot1agCfmGmacTraceDot1qVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceDot1qVlan.setStatus("current")
_HwDot1agCfmGmacTracePeVlan_Type = VlanIdOrNone
_HwDot1agCfmGmacTracePeVlan_Object = MibTableColumn
hwDot1agCfmGmacTracePeVlan = _HwDot1agCfmGmacTracePeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 10),
    _HwDot1agCfmGmacTracePeVlan_Type()
)
hwDot1agCfmGmacTracePeVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTracePeVlan.setStatus("current")
_HwDot1agCfmGmacTraceCeVlan_Type = VlanIdOrNone
_HwDot1agCfmGmacTraceCeVlan_Object = MibTableColumn
hwDot1agCfmGmacTraceCeVlan = _HwDot1agCfmGmacTraceCeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 11),
    _HwDot1agCfmGmacTraceCeVlan_Type()
)
hwDot1agCfmGmacTraceCeVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceCeVlan.setStatus("current")


class _HwDot1agCfmGmacTraceOutIfIndex_Type(InterfaceIndexOrZero):
    """Custom type hwDot1agCfmGmacTraceOutIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_HwDot1agCfmGmacTraceOutIfIndex_Object = MibTableColumn
hwDot1agCfmGmacTraceOutIfIndex = _HwDot1agCfmGmacTraceOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 12),
    _HwDot1agCfmGmacTraceOutIfIndex_Type()
)
hwDot1agCfmGmacTraceOutIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceOutIfIndex.setStatus("current")


class _HwDot1agCfmGmacTraceTimeOut_Type(Unsigned32):
    """Custom type hwDot1agCfmGmacTraceTimeOut based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwDot1agCfmGmacTraceTimeOut_Type.__name__ = "Unsigned32"
_HwDot1agCfmGmacTraceTimeOut_Object = MibTableColumn
hwDot1agCfmGmacTraceTimeOut = _HwDot1agCfmGmacTraceTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 13),
    _HwDot1agCfmGmacTraceTimeOut_Type()
)
hwDot1agCfmGmacTraceTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceTimeOut.setStatus("current")
_HwDot1agCfmGmacTraceDisplayHostInfo_Type = TruthValue
_HwDot1agCfmGmacTraceDisplayHostInfo_Object = MibTableColumn
hwDot1agCfmGmacTraceDisplayHostInfo = _HwDot1agCfmGmacTraceDisplayHostInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 14),
    _HwDot1agCfmGmacTraceDisplayHostInfo_Type()
)
hwDot1agCfmGmacTraceDisplayHostInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceDisplayHostInfo.setStatus("current")
_HwDot1agCfmGmacTraceSendSeqNumber_Type = Unsigned32
_HwDot1agCfmGmacTraceSendSeqNumber_Object = MibTableColumn
hwDot1agCfmGmacTraceSendSeqNumber = _HwDot1agCfmGmacTraceSendSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 15),
    _HwDot1agCfmGmacTraceSendSeqNumber_Type()
)
hwDot1agCfmGmacTraceSendSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceSendSeqNumber.setStatus("current")


class _HwDot1agCfmGmacTraceResult_Type(Integer32):
    """Custom type hwDot1agCfmGmacTraceResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("invalid", 1),
          ("successful", 2))
    )


_HwDot1agCfmGmacTraceResult_Type.__name__ = "Integer32"
_HwDot1agCfmGmacTraceResult_Object = MibTableColumn
hwDot1agCfmGmacTraceResult = _HwDot1agCfmGmacTraceResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 16),
    _HwDot1agCfmGmacTraceResult_Type()
)
hwDot1agCfmGmacTraceResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceResult.setStatus("current")
_HwDot1agCfmGmacTraceRowStatus_Type = RowStatus
_HwDot1agCfmGmacTraceRowStatus_Object = MibTableColumn
hwDot1agCfmGmacTraceRowStatus = _HwDot1agCfmGmacTraceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 2, 1, 99),
    _HwDot1agCfmGmacTraceRowStatus_Type()
)
hwDot1agCfmGmacTraceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceRowStatus.setStatus("current")
_HwDot1agCfmGmacTraceReplyTable_Object = MibTable
hwDot1agCfmGmacTraceReplyTable = _HwDot1agCfmGmacTraceReplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3)
)
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyTable.setStatus("current")
_HwDot1agCfmGmacTraceReplyEntry_Object = MibTableRow
hwDot1agCfmGmacTraceReplyEntry = _HwDot1agCfmGmacTraceReplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1)
)
hwDot1agCfmGmacTraceReplyEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmGmacTraceReplySeqNumber"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmGmacTraceReplyRecvOrder"),
)
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyEntry.setStatus("current")
_HwDot1agCfmGmacTraceReplySeqNumber_Type = Unsigned32
_HwDot1agCfmGmacTraceReplySeqNumber_Object = MibTableColumn
hwDot1agCfmGmacTraceReplySeqNumber = _HwDot1agCfmGmacTraceReplySeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 1),
    _HwDot1agCfmGmacTraceReplySeqNumber_Type()
)
hwDot1agCfmGmacTraceReplySeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplySeqNumber.setStatus("current")
_HwDot1agCfmGmacTraceReplyRecvOrder_Type = Unsigned32
_HwDot1agCfmGmacTraceReplyRecvOrder_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyRecvOrder = _HwDot1agCfmGmacTraceReplyRecvOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 2),
    _HwDot1agCfmGmacTraceReplyRecvOrder_Type()
)
hwDot1agCfmGmacTraceReplyRecvOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyRecvOrder.setStatus("current")


class _HwDot1agCfmGmacTraceReplyTTL_Type(Unsigned32):
    """Custom type hwDot1agCfmGmacTraceReplyTTL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwDot1agCfmGmacTraceReplyTTL_Type.__name__ = "Unsigned32"
_HwDot1agCfmGmacTraceReplyTTL_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyTTL = _HwDot1agCfmGmacTraceReplyTTL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 3),
    _HwDot1agCfmGmacTraceReplyTTL_Type()
)
hwDot1agCfmGmacTraceReplyTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyTTL.setStatus("current")
_HwDot1agCfmGmacTraceReplyForwarded_Type = TruthValue
_HwDot1agCfmGmacTraceReplyForwarded_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyForwarded = _HwDot1agCfmGmacTraceReplyForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 4),
    _HwDot1agCfmGmacTraceReplyForwarded_Type()
)
hwDot1agCfmGmacTraceReplyForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyForwarded.setStatus("current")
_HwDot1agCfmGmacTraceReplyHostInfo_Type = OctetString
_HwDot1agCfmGmacTraceReplyHostInfo_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyHostInfo = _HwDot1agCfmGmacTraceReplyHostInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 5),
    _HwDot1agCfmGmacTraceReplyHostInfo_Type()
)
hwDot1agCfmGmacTraceReplyHostInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyHostInfo.setStatus("current")
_HwDot1agCfmGmacTraceReplyRelayAction_Type = HWDot1agCfmRelayActionFieldValue
_HwDot1agCfmGmacTraceReplyRelayAction_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyRelayAction = _HwDot1agCfmGmacTraceReplyRelayAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 6),
    _HwDot1agCfmGmacTraceReplyRelayAction_Type()
)
hwDot1agCfmGmacTraceReplyRelayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyRelayAction.setStatus("current")
_HwDot1agCfmGmacTraceReplyIngressAction_Type = HWDot1agCfmIngressActionFieldValue
_HwDot1agCfmGmacTraceReplyIngressAction_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyIngressAction = _HwDot1agCfmGmacTraceReplyIngressAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 7),
    _HwDot1agCfmGmacTraceReplyIngressAction_Type()
)
hwDot1agCfmGmacTraceReplyIngressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyIngressAction.setStatus("current")
_HwDot1agCfmGmacTraceReplyIngressMac_Type = MacAddress
_HwDot1agCfmGmacTraceReplyIngressMac_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyIngressMac = _HwDot1agCfmGmacTraceReplyIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 8),
    _HwDot1agCfmGmacTraceReplyIngressMac_Type()
)
hwDot1agCfmGmacTraceReplyIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyIngressMac.setStatus("current")
_HwDot1agCfmGmacTraceReplyIngressIfName_Type = OctetString
_HwDot1agCfmGmacTraceReplyIngressIfName_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyIngressIfName = _HwDot1agCfmGmacTraceReplyIngressIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 9),
    _HwDot1agCfmGmacTraceReplyIngressIfName_Type()
)
hwDot1agCfmGmacTraceReplyIngressIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyIngressIfName.setStatus("current")
_HwDot1agCfmGmacTraceReplyEgressAction_Type = HWDot1agCfmEgressActionFieldValue
_HwDot1agCfmGmacTraceReplyEgressAction_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyEgressAction = _HwDot1agCfmGmacTraceReplyEgressAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 10),
    _HwDot1agCfmGmacTraceReplyEgressAction_Type()
)
hwDot1agCfmGmacTraceReplyEgressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyEgressAction.setStatus("current")
_HwDot1agCfmGmacTraceReplyEgressMac_Type = MacAddress
_HwDot1agCfmGmacTraceReplyEgressMac_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyEgressMac = _HwDot1agCfmGmacTraceReplyEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 11),
    _HwDot1agCfmGmacTraceReplyEgressMac_Type()
)
hwDot1agCfmGmacTraceReplyEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyEgressMac.setStatus("current")
_HwDot1agCfmGmacTraceReplyEgressIfName_Type = OctetString
_HwDot1agCfmGmacTraceReplyEgressIfName_Object = MibTableColumn
hwDot1agCfmGmacTraceReplyEgressIfName = _HwDot1agCfmGmacTraceReplyEgressIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 11, 3, 1, 12),
    _HwDot1agCfmGmacTraceReplyEgressIfName_Type()
)
hwDot1agCfmGmacTraceReplyEgressIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1agCfmGmacTraceReplyEgressIfName.setStatus("current")


class _HwDot1agCfmMPAddressModel_Type(Integer32):
    """Custom type hwDot1agCfmMPAddressModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("individual", 2))
    )


_HwDot1agCfmMPAddressModel_Type.__name__ = "Integer32"
_HwDot1agCfmMPAddressModel_Object = MibScalar
hwDot1agCfmMPAddressModel = _HwDot1agCfmMPAddressModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 1, 101),
    _HwDot1agCfmMPAddressModel_Type()
)
hwDot1agCfmMPAddressModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1agCfmMPAddressModel.setStatus("current")
_HwEthOam3ah_ObjectIdentity = ObjectIdentity
hwEthOam3ah = _HwEthOam3ah_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2)
)
_HwDot3ahEfmEnabled_Type = EnabledStatus
_HwDot3ahEfmEnabled_Object = MibScalar
hwDot3ahEfmEnabled = _HwDot3ahEfmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 1),
    _HwDot3ahEfmEnabled_Type()
)
hwDot3ahEfmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmEnabled.setStatus("current")
_HwDot3ahEfmObject_ObjectIdentity = ObjectIdentity
hwDot3ahEfmObject = _HwDot3ahEfmObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2)
)
_HwDot3ahEfmDetectModeTable_Object = MibTable
hwDot3ahEfmDetectModeTable = _HwDot3ahEfmDetectModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwDot3ahEfmDetectModeTable.setStatus("current")
_HwDot3ahEfmDetectModeEntry_Object = MibTableRow
hwDot3ahEfmDetectModeEntry = _HwDot3ahEfmDetectModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwDot3ahEfmDetectModeEntry.setStatus("current")


class _HwDot3ahEfmDetectMode_Type(HWDetectType):
    """Custom type hwDot3ahEfmDetectMode based on HWDetectType"""


_HwDot3ahEfmDetectMode_Object = MibTableColumn
hwDot3ahEfmDetectMode = _HwDot3ahEfmDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 1, 1, 11),
    _HwDot3ahEfmDetectMode_Type()
)
hwDot3ahEfmDetectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmDetectMode.setStatus("current")
_HwDot3ahEfmDetectInterval_Type = TimeInterval
_HwDot3ahEfmDetectInterval_Object = MibTableColumn
hwDot3ahEfmDetectInterval = _HwDot3ahEfmDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 1, 1, 12),
    _HwDot3ahEfmDetectInterval_Type()
)
hwDot3ahEfmDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmDetectInterval.setStatus("current")


class _HwDot3ahEfmDetectMalfunction_Type(Integer32):
    """Custom type hwDot3ahEfmDetectMalfunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 768),
    )


_HwDot3ahEfmDetectMalfunction_Type.__name__ = "Integer32"
_HwDot3ahEfmDetectMalfunction_Object = MibTableColumn
hwDot3ahEfmDetectMalfunction = _HwDot3ahEfmDetectMalfunction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 1, 1, 13),
    _HwDot3ahEfmDetectMalfunction_Type()
)
hwDot3ahEfmDetectMalfunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmDetectMalfunction.setStatus("current")
_HwDot3ahEfmTable_Object = MibTable
hwDot3ahEfmTable = _HwDot3ahEfmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hwDot3ahEfmTable.setStatus("current")
_HwDot3ahEfmEntry_Object = MibTableRow
hwDot3ahEfmEntry = _HwDot3ahEfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 2, 1)
)
hwDot3ahEfmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwDot3ahEfmEntry.setStatus("current")
_HwDot3ahEfmAdminState_Type = EnabledStatus
_HwDot3ahEfmAdminState_Object = MibTableColumn
hwDot3ahEfmAdminState = _HwDot3ahEfmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 2, 1, 1),
    _HwDot3ahEfmAdminState_Type()
)
hwDot3ahEfmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmAdminState.setStatus("current")


class _HwDot3ahEfmOperStatus_Type(Integer32):
    """Custom type hwDot3ahEfmOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("activeSendLocal", 4),
          ("disabled", 1),
          ("linkFault", 2),
          ("nonOperHalfDuplex", 10),
          ("oamPeeringLocallyRejected", 7),
          ("oamPeeringRemotelyRejected", 8),
          ("operational", 9),
          ("passiveWait", 3),
          ("sendLocalAndRemote", 5),
          ("sendLocalAndRemoteOk", 6))
    )


_HwDot3ahEfmOperStatus_Type.__name__ = "Integer32"
_HwDot3ahEfmOperStatus_Object = MibTableColumn
hwDot3ahEfmOperStatus = _HwDot3ahEfmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 2, 1, 2),
    _HwDot3ahEfmOperStatus_Type()
)
hwDot3ahEfmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmOperStatus.setStatus("current")


class _HwDot3ahEfmMode_Type(Integer32):
    """Custom type hwDot3ahEfmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_HwDot3ahEfmMode_Type.__name__ = "Integer32"
_HwDot3ahEfmMode_Object = MibTableColumn
hwDot3ahEfmMode = _HwDot3ahEfmMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 2, 1, 3),
    _HwDot3ahEfmMode_Type()
)
hwDot3ahEfmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmMode.setStatus("current")


class _HwDot3ahEfmMaxOamPduSize_Type(Unsigned32):
    """Custom type hwDot3ahEfmMaxOamPduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_HwDot3ahEfmMaxOamPduSize_Type.__name__ = "Unsigned32"
_HwDot3ahEfmMaxOamPduSize_Object = MibTableColumn
hwDot3ahEfmMaxOamPduSize = _HwDot3ahEfmMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 2, 1, 4),
    _HwDot3ahEfmMaxOamPduSize_Type()
)
hwDot3ahEfmMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmMaxOamPduSize.setUnits("octets")


class _HwDot3ahEfmConfigRevision_Type(Unsigned32):
    """Custom type hwDot3ahEfmConfigRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwDot3ahEfmConfigRevision_Type.__name__ = "Unsigned32"
_HwDot3ahEfmConfigRevision_Object = MibTableColumn
hwDot3ahEfmConfigRevision = _HwDot3ahEfmConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 2, 1, 5),
    _HwDot3ahEfmConfigRevision_Type()
)
hwDot3ahEfmConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmConfigRevision.setStatus("current")


class _HwDot3ahEfmFunctionsSupported_Type(Bits):
    """Custom type hwDot3ahEfmFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_HwDot3ahEfmFunctionsSupported_Type.__name__ = "Bits"
_HwDot3ahEfmFunctionsSupported_Object = MibTableColumn
hwDot3ahEfmFunctionsSupported = _HwDot3ahEfmFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 2, 1, 6),
    _HwDot3ahEfmFunctionsSupported_Type()
)
hwDot3ahEfmFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmFunctionsSupported.setStatus("current")


class _HwDot3ahEfmTimeout_Type(Unsigned32):
    """Custom type hwDot3ahEfmTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 30000),
    )


_HwDot3ahEfmTimeout_Type.__name__ = "Unsigned32"
_HwDot3ahEfmTimeout_Object = MibTableColumn
hwDot3ahEfmTimeout = _HwDot3ahEfmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 2, 1, 7),
    _HwDot3ahEfmTimeout_Type()
)
hwDot3ahEfmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmTimeout.setUnits("milliseconds")


class _HwDot3ahEfmInterval_Type(Unsigned32):
    """Custom type hwDot3ahEfmInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_HwDot3ahEfmInterval_Type.__name__ = "Unsigned32"
_HwDot3ahEfmInterval_Object = MibTableColumn
hwDot3ahEfmInterval = _HwDot3ahEfmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 2, 1, 8),
    _HwDot3ahEfmInterval_Type()
)
hwDot3ahEfmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmInterval.setUnits("milliseconds")
_HwDot3ahEfmPeerTable_Object = MibTable
hwDot3ahEfmPeerTable = _HwDot3ahEfmPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerTable.setStatus("current")
_HwDot3ahEfmPeerEntry_Object = MibTableRow
hwDot3ahEfmPeerEntry = _HwDot3ahEfmPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 3, 1)
)
hwDot3ahEfmPeerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerEntry.setStatus("current")
_HwDot3ahEfmPeerMacAddress_Type = OctetString
_HwDot3ahEfmPeerMacAddress_Object = MibTableColumn
hwDot3ahEfmPeerMacAddress = _HwDot3ahEfmPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 3, 1, 1),
    _HwDot3ahEfmPeerMacAddress_Type()
)
hwDot3ahEfmPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerMacAddress.setStatus("current")
_HwDot3ahEfmPeerVendorOui_Type = HWDot3Oui
_HwDot3ahEfmPeerVendorOui_Object = MibTableColumn
hwDot3ahEfmPeerVendorOui = _HwDot3ahEfmPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 3, 1, 2),
    _HwDot3ahEfmPeerVendorOui_Type()
)
hwDot3ahEfmPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerVendorOui.setStatus("current")
_HwDot3ahEfmPeerVendorInfo_Type = Unsigned32
_HwDot3ahEfmPeerVendorInfo_Object = MibTableColumn
hwDot3ahEfmPeerVendorInfo = _HwDot3ahEfmPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 3, 1, 3),
    _HwDot3ahEfmPeerVendorInfo_Type()
)
hwDot3ahEfmPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerVendorInfo.setStatus("current")


class _HwDot3ahEfmPeerMode_Type(Integer32):
    """Custom type hwDot3ahEfmPeerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2),
          ("unknown", 3))
    )


_HwDot3ahEfmPeerMode_Type.__name__ = "Integer32"
_HwDot3ahEfmPeerMode_Object = MibTableColumn
hwDot3ahEfmPeerMode = _HwDot3ahEfmPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 3, 1, 4),
    _HwDot3ahEfmPeerMode_Type()
)
hwDot3ahEfmPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerMode.setStatus("current")


class _HwDot3ahEfmPeerMaxOamPduSize_Type(Unsigned32):
    """Custom type hwDot3ahEfmPeerMaxOamPduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwDot3ahEfmPeerMaxOamPduSize_Type.__name__ = "Unsigned32"
_HwDot3ahEfmPeerMaxOamPduSize_Object = MibTableColumn
hwDot3ahEfmPeerMaxOamPduSize = _HwDot3ahEfmPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 3, 1, 5),
    _HwDot3ahEfmPeerMaxOamPduSize_Type()
)
hwDot3ahEfmPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerMaxOamPduSize.setUnits("octets")


class _HwDot3ahEfmPeerConfigRevision_Type(Unsigned32):
    """Custom type hwDot3ahEfmPeerConfigRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwDot3ahEfmPeerConfigRevision_Type.__name__ = "Unsigned32"
_HwDot3ahEfmPeerConfigRevision_Object = MibTableColumn
hwDot3ahEfmPeerConfigRevision = _HwDot3ahEfmPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 3, 1, 6),
    _HwDot3ahEfmPeerConfigRevision_Type()
)
hwDot3ahEfmPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerConfigRevision.setStatus("current")


class _HwDot3ahEfmPeerFunctionsSupported_Type(Bits):
    """Custom type hwDot3ahEfmPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_HwDot3ahEfmPeerFunctionsSupported_Type.__name__ = "Bits"
_HwDot3ahEfmPeerFunctionsSupported_Object = MibTableColumn
hwDot3ahEfmPeerFunctionsSupported = _HwDot3ahEfmPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 3, 1, 7),
    _HwDot3ahEfmPeerFunctionsSupported_Type()
)
hwDot3ahEfmPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerFunctionsSupported.setStatus("current")
_HwDot3ahEfmLoopbackTable_Object = MibTable
hwDot3ahEfmLoopbackTable = _HwDot3ahEfmLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackTable.setStatus("current")
_HwDot3ahEfmLoopbackEntry_Object = MibTableRow
hwDot3ahEfmLoopbackEntry = _HwDot3ahEfmLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 4, 1)
)
hwDot3ahEfmLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackEntry.setStatus("current")


class _HwDot3ahEfmLoopbackStatus_Type(Integer32):
    """Custom type hwDot3ahEfmLoopbackStatus based on Integer32"""
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
        *(("initiatingLoopback", 2),
          ("localLoopback", 5),
          ("noLoopback", 1),
          ("remoteLoopback", 3),
          ("terminatingLoopback", 4),
          ("unknown", 6))
    )


_HwDot3ahEfmLoopbackStatus_Type.__name__ = "Integer32"
_HwDot3ahEfmLoopbackStatus_Object = MibTableColumn
hwDot3ahEfmLoopbackStatus = _HwDot3ahEfmLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 4, 1, 1),
    _HwDot3ahEfmLoopbackStatus_Type()
)
hwDot3ahEfmLoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackStatus.setStatus("current")


class _HwDot3ahEfmLoopbackIgnoreRx_Type(Integer32):
    """Custom type hwDot3ahEfmLoopbackIgnoreRx based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 2))
    )


_HwDot3ahEfmLoopbackIgnoreRx_Type.__name__ = "Integer32"
_HwDot3ahEfmLoopbackIgnoreRx_Object = MibTableColumn
hwDot3ahEfmLoopbackIgnoreRx = _HwDot3ahEfmLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 4, 1, 2),
    _HwDot3ahEfmLoopbackIgnoreRx_Type()
)
hwDot3ahEfmLoopbackIgnoreRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackIgnoreRx.setStatus("current")


class _HwDot3ahEfmLoopbackTimeout_Type(Unsigned32):
    """Custom type hwDot3ahEfmLoopbackTimeout based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwDot3ahEfmLoopbackTimeout_Type.__name__ = "Unsigned32"
_HwDot3ahEfmLoopbackTimeout_Object = MibTableColumn
hwDot3ahEfmLoopbackTimeout = _HwDot3ahEfmLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 4, 1, 3),
    _HwDot3ahEfmLoopbackTimeout_Type()
)
hwDot3ahEfmLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackTimeout.setUnits("minutes")
_HwDot3ahEfmStatsTable_Object = MibTable
hwDot3ahEfmStatsTable = _HwDot3ahEfmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hwDot3ahEfmStatsTable.setStatus("current")
_HwDot3ahEfmStatsEntry_Object = MibTableRow
hwDot3ahEfmStatsEntry = _HwDot3ahEfmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1)
)
hwDot3ahEfmStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwDot3ahEfmStatsEntry.setStatus("current")
_HwDot3ahEfmInformationTx_Type = Counter32
_HwDot3ahEfmInformationTx_Object = MibTableColumn
hwDot3ahEfmInformationTx = _HwDot3ahEfmInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 1),
    _HwDot3ahEfmInformationTx_Type()
)
hwDot3ahEfmInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmInformationTx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmInformationTx.setUnits("frames")
_HwDot3ahEfmInformationRx_Type = Counter32
_HwDot3ahEfmInformationRx_Object = MibTableColumn
hwDot3ahEfmInformationRx = _HwDot3ahEfmInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 2),
    _HwDot3ahEfmInformationRx_Type()
)
hwDot3ahEfmInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmInformationRx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmInformationRx.setUnits("frames")
_HwDot3ahEfmUniqueEventNotificationTx_Type = Counter32
_HwDot3ahEfmUniqueEventNotificationTx_Object = MibTableColumn
hwDot3ahEfmUniqueEventNotificationTx = _HwDot3ahEfmUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 3),
    _HwDot3ahEfmUniqueEventNotificationTx_Type()
)
hwDot3ahEfmUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmUniqueEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmUniqueEventNotificationTx.setUnits("frames")
_HwDot3ahEfmUniqueEventNotificationRx_Type = Counter32
_HwDot3ahEfmUniqueEventNotificationRx_Object = MibTableColumn
hwDot3ahEfmUniqueEventNotificationRx = _HwDot3ahEfmUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 4),
    _HwDot3ahEfmUniqueEventNotificationRx_Type()
)
hwDot3ahEfmUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmUniqueEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmUniqueEventNotificationRx.setUnits("frames")
_HwDot3ahEfmDuplicateEventNotificationTx_Type = Counter32
_HwDot3ahEfmDuplicateEventNotificationTx_Object = MibTableColumn
hwDot3ahEfmDuplicateEventNotificationTx = _HwDot3ahEfmDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 5),
    _HwDot3ahEfmDuplicateEventNotificationTx_Type()
)
hwDot3ahEfmDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmDuplicateEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmDuplicateEventNotificationTx.setUnits("frames")
_HwDot3ahEfmDuplicateEventNotificationRx_Type = Counter32
_HwDot3ahEfmDuplicateEventNotificationRx_Object = MibTableColumn
hwDot3ahEfmDuplicateEventNotificationRx = _HwDot3ahEfmDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 6),
    _HwDot3ahEfmDuplicateEventNotificationRx_Type()
)
hwDot3ahEfmDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmDuplicateEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmDuplicateEventNotificationRx.setUnits("frames")
_HwDot3ahEfmLoopbackControlTx_Type = Counter32
_HwDot3ahEfmLoopbackControlTx_Object = MibTableColumn
hwDot3ahEfmLoopbackControlTx = _HwDot3ahEfmLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 7),
    _HwDot3ahEfmLoopbackControlTx_Type()
)
hwDot3ahEfmLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackControlTx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackControlTx.setUnits("frames")
_HwDot3ahEfmLoopbackControlRx_Type = Counter32
_HwDot3ahEfmLoopbackControlRx_Object = MibTableColumn
hwDot3ahEfmLoopbackControlRx = _HwDot3ahEfmLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 8),
    _HwDot3ahEfmLoopbackControlRx_Type()
)
hwDot3ahEfmLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackControlRx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackControlRx.setUnits("frames")
_HwDot3ahEfmVariableRequestTx_Type = Counter32
_HwDot3ahEfmVariableRequestTx_Object = MibTableColumn
hwDot3ahEfmVariableRequestTx = _HwDot3ahEfmVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 9),
    _HwDot3ahEfmVariableRequestTx_Type()
)
hwDot3ahEfmVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmVariableRequestTx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmVariableRequestTx.setUnits("frames")
_HwDot3ahEfmVariableRequestRx_Type = Counter32
_HwDot3ahEfmVariableRequestRx_Object = MibTableColumn
hwDot3ahEfmVariableRequestRx = _HwDot3ahEfmVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 10),
    _HwDot3ahEfmVariableRequestRx_Type()
)
hwDot3ahEfmVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmVariableRequestRx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmVariableRequestRx.setUnits("frames")
_HwDot3ahEfmVariableResponseTx_Type = Counter32
_HwDot3ahEfmVariableResponseTx_Object = MibTableColumn
hwDot3ahEfmVariableResponseTx = _HwDot3ahEfmVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 11),
    _HwDot3ahEfmVariableResponseTx_Type()
)
hwDot3ahEfmVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmVariableResponseTx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmVariableResponseTx.setUnits("frames")
_HwDot3ahEfmVariableResponseRx_Type = Counter32
_HwDot3ahEfmVariableResponseRx_Object = MibTableColumn
hwDot3ahEfmVariableResponseRx = _HwDot3ahEfmVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 12),
    _HwDot3ahEfmVariableResponseRx_Type()
)
hwDot3ahEfmVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmVariableResponseRx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmVariableResponseRx.setUnits("frames")
_HwDot3ahEfmOrgSpecificTx_Type = Counter32
_HwDot3ahEfmOrgSpecificTx_Object = MibTableColumn
hwDot3ahEfmOrgSpecificTx = _HwDot3ahEfmOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 13),
    _HwDot3ahEfmOrgSpecificTx_Type()
)
hwDot3ahEfmOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmOrgSpecificTx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmOrgSpecificTx.setUnits("frames")
_HwDot3ahEfmOrgSpecificRx_Type = Counter32
_HwDot3ahEfmOrgSpecificRx_Object = MibTableColumn
hwDot3ahEfmOrgSpecificRx = _HwDot3ahEfmOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 14),
    _HwDot3ahEfmOrgSpecificRx_Type()
)
hwDot3ahEfmOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmOrgSpecificRx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmOrgSpecificRx.setUnits("frames")
_HwDot3ahEfmUnsupportedCodesTx_Type = Counter32
_HwDot3ahEfmUnsupportedCodesTx_Object = MibTableColumn
hwDot3ahEfmUnsupportedCodesTx = _HwDot3ahEfmUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 15),
    _HwDot3ahEfmUnsupportedCodesTx_Type()
)
hwDot3ahEfmUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmUnsupportedCodesTx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmUnsupportedCodesTx.setUnits("frames")
_HwDot3ahEfmUnsupportedCodesRx_Type = Counter32
_HwDot3ahEfmUnsupportedCodesRx_Object = MibTableColumn
hwDot3ahEfmUnsupportedCodesRx = _HwDot3ahEfmUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 16),
    _HwDot3ahEfmUnsupportedCodesRx_Type()
)
hwDot3ahEfmUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmUnsupportedCodesRx.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmUnsupportedCodesRx.setUnits("frames")
_HwDot3ahEfmFramesLostDueToOam_Type = Counter32
_HwDot3ahEfmFramesLostDueToOam_Object = MibTableColumn
hwDot3ahEfmFramesLostDueToOam = _HwDot3ahEfmFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 5, 1, 17),
    _HwDot3ahEfmFramesLostDueToOam_Type()
)
hwDot3ahEfmFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmFramesLostDueToOam.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmFramesLostDueToOam.setUnits("frames")
_HwDot3ahEfmEventConfigTable_Object = MibTable
hwDot3ahEfmEventConfigTable = _HwDot3ahEfmEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hwDot3ahEfmEventConfigTable.setStatus("current")
_HwDot3ahEfmEventConfigEntry_Object = MibTableRow
hwDot3ahEfmEventConfigEntry = _HwDot3ahEfmEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1)
)
hwDot3ahEfmEventConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwDot3ahEfmEventConfigEntry.setStatus("current")
_HwDot3ahEfmErrSymPeriodWindowHi_Type = Unsigned32
_HwDot3ahEfmErrSymPeriodWindowHi_Object = MibTableColumn
hwDot3ahEfmErrSymPeriodWindowHi = _HwDot3ahEfmErrSymPeriodWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 1),
    _HwDot3ahEfmErrSymPeriodWindowHi_Type()
)
hwDot3ahEfmErrSymPeriodWindowHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrSymPeriodWindowHi.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrSymPeriodWindowHi.setUnits("2^32 symbols")
_HwDot3ahEfmErrSymPeriodWindowLo_Type = Unsigned32
_HwDot3ahEfmErrSymPeriodWindowLo_Object = MibTableColumn
hwDot3ahEfmErrSymPeriodWindowLo = _HwDot3ahEfmErrSymPeriodWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 2),
    _HwDot3ahEfmErrSymPeriodWindowLo_Type()
)
hwDot3ahEfmErrSymPeriodWindowLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrSymPeriodWindowLo.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrSymPeriodWindowLo.setUnits("symbols")
_HwDot3ahEfmErrSymPeriodThresholdHi_Type = Unsigned32
_HwDot3ahEfmErrSymPeriodThresholdHi_Object = MibTableColumn
hwDot3ahEfmErrSymPeriodThresholdHi = _HwDot3ahEfmErrSymPeriodThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 3),
    _HwDot3ahEfmErrSymPeriodThresholdHi_Type()
)
hwDot3ahEfmErrSymPeriodThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrSymPeriodThresholdHi.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrSymPeriodThresholdHi.setUnits("2^32 symbols")
_HwDot3ahEfmErrSymPeriodThresholdLo_Type = Unsigned32
_HwDot3ahEfmErrSymPeriodThresholdLo_Object = MibTableColumn
hwDot3ahEfmErrSymPeriodThresholdLo = _HwDot3ahEfmErrSymPeriodThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 4),
    _HwDot3ahEfmErrSymPeriodThresholdLo_Type()
)
hwDot3ahEfmErrSymPeriodThresholdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrSymPeriodThresholdLo.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrSymPeriodThresholdLo.setUnits("symbols")
_HwDot3ahEfmErrSymPeriodEvNotifEnable_Type = TruthValue
_HwDot3ahEfmErrSymPeriodEvNotifEnable_Object = MibTableColumn
hwDot3ahEfmErrSymPeriodEvNotifEnable = _HwDot3ahEfmErrSymPeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 5),
    _HwDot3ahEfmErrSymPeriodEvNotifEnable_Type()
)
hwDot3ahEfmErrSymPeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrSymPeriodEvNotifEnable.setStatus("current")
_HwDot3ahEfmErrFramePeriodWindow_Type = Unsigned32
_HwDot3ahEfmErrFramePeriodWindow_Object = MibTableColumn
hwDot3ahEfmErrFramePeriodWindow = _HwDot3ahEfmErrFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 6),
    _HwDot3ahEfmErrFramePeriodWindow_Type()
)
hwDot3ahEfmErrFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFramePeriodWindow.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFramePeriodWindow.setUnits("frames")
_HwDot3ahEfmErrFramePeriodThreshold_Type = Unsigned32
_HwDot3ahEfmErrFramePeriodThreshold_Object = MibTableColumn
hwDot3ahEfmErrFramePeriodThreshold = _HwDot3ahEfmErrFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 7),
    _HwDot3ahEfmErrFramePeriodThreshold_Type()
)
hwDot3ahEfmErrFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFramePeriodThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFramePeriodThreshold.setUnits("frames")
_HwDot3ahEfmErrFramePeriodEvNotifEnable_Type = TruthValue
_HwDot3ahEfmErrFramePeriodEvNotifEnable_Object = MibTableColumn
hwDot3ahEfmErrFramePeriodEvNotifEnable = _HwDot3ahEfmErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 8),
    _HwDot3ahEfmErrFramePeriodEvNotifEnable_Type()
)
hwDot3ahEfmErrFramePeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFramePeriodEvNotifEnable.setStatus("current")
_HwDot3ahEfmErrFrameWindow_Type = Unsigned32
_HwDot3ahEfmErrFrameWindow_Object = MibTableColumn
hwDot3ahEfmErrFrameWindow = _HwDot3ahEfmErrFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 9),
    _HwDot3ahEfmErrFrameWindow_Type()
)
hwDot3ahEfmErrFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameWindow.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameWindow.setUnits("tenths of a second")
_HwDot3ahEfmErrFrameThreshold_Type = Unsigned32
_HwDot3ahEfmErrFrameThreshold_Object = MibTableColumn
hwDot3ahEfmErrFrameThreshold = _HwDot3ahEfmErrFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 10),
    _HwDot3ahEfmErrFrameThreshold_Type()
)
hwDot3ahEfmErrFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameThreshold.setUnits("frames")
_HwDot3ahEfmErrFrameEvNotifEnable_Type = TruthValue
_HwDot3ahEfmErrFrameEvNotifEnable_Object = MibTableColumn
hwDot3ahEfmErrFrameEvNotifEnable = _HwDot3ahEfmErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 11),
    _HwDot3ahEfmErrFrameEvNotifEnable_Type()
)
hwDot3ahEfmErrFrameEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameEvNotifEnable.setStatus("current")


class _HwDot3ahEfmErrFrameSecsSummaryWindow_Type(Integer32):
    """Custom type hwDot3ahEfmErrFrameSecsSummaryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9000),
    )


_HwDot3ahEfmErrFrameSecsSummaryWindow_Type.__name__ = "Integer32"
_HwDot3ahEfmErrFrameSecsSummaryWindow_Object = MibTableColumn
hwDot3ahEfmErrFrameSecsSummaryWindow = _HwDot3ahEfmErrFrameSecsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 12),
    _HwDot3ahEfmErrFrameSecsSummaryWindow_Type()
)
hwDot3ahEfmErrFrameSecsSummaryWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameSecsSummaryWindow.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameSecsSummaryWindow.setUnits("tenths of a second")


class _HwDot3ahEfmErrFrameSecsSummaryThreshold_Type(Integer32):
    """Custom type hwDot3ahEfmErrFrameSecsSummaryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_HwDot3ahEfmErrFrameSecsSummaryThreshold_Type.__name__ = "Integer32"
_HwDot3ahEfmErrFrameSecsSummaryThreshold_Object = MibTableColumn
hwDot3ahEfmErrFrameSecsSummaryThreshold = _HwDot3ahEfmErrFrameSecsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 13),
    _HwDot3ahEfmErrFrameSecsSummaryThreshold_Type()
)
hwDot3ahEfmErrFrameSecsSummaryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameSecsSummaryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameSecsSummaryThreshold.setUnits("errored frame seconds")
_HwDot3ahEfmErrFrameSecsEvNotifEnable_Type = TruthValue
_HwDot3ahEfmErrFrameSecsEvNotifEnable_Object = MibTableColumn
hwDot3ahEfmErrFrameSecsEvNotifEnable = _HwDot3ahEfmErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 14),
    _HwDot3ahEfmErrFrameSecsEvNotifEnable_Type()
)
hwDot3ahEfmErrFrameSecsEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameSecsEvNotifEnable.setStatus("current")
_HwDot3ahEfmDyingGaspEnable_Type = TruthValue
_HwDot3ahEfmDyingGaspEnable_Object = MibTableColumn
hwDot3ahEfmDyingGaspEnable = _HwDot3ahEfmDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 15),
    _HwDot3ahEfmDyingGaspEnable_Type()
)
hwDot3ahEfmDyingGaspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmDyingGaspEnable.setStatus("current")
_HwDot3ahEfmCriticalEventEnable_Type = TruthValue
_HwDot3ahEfmCriticalEventEnable_Object = MibTableColumn
hwDot3ahEfmCriticalEventEnable = _HwDot3ahEfmCriticalEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 16),
    _HwDot3ahEfmCriticalEventEnable_Type()
)
hwDot3ahEfmCriticalEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmCriticalEventEnable.setStatus("current")
_HwDot3ahEfmThresholdTriggerErrDown_Type = EnabledStatus
_HwDot3ahEfmThresholdTriggerErrDown_Object = MibTableColumn
hwDot3ahEfmThresholdTriggerErrDown = _HwDot3ahEfmThresholdTriggerErrDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 6, 1, 17),
    _HwDot3ahEfmThresholdTriggerErrDown_Type()
)
hwDot3ahEfmThresholdTriggerErrDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmThresholdTriggerErrDown.setStatus("current")
_HwDot3ahEfmEventLogTable_Object = MibTable
hwDot3ahEfmEventLogTable = _HwDot3ahEfmEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogTable.setStatus("current")
_HwDot3ahEfmEventLogEntry_Object = MibTableRow
hwDot3ahEfmEventLogEntry = _HwDot3ahEfmEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1)
)
hwDot3ahEfmEventLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogIndex"),
)
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogEntry.setStatus("current")
_HwDot3ahEfmEventLogIndex_Type = Unsigned32
_HwDot3ahEfmEventLogIndex_Object = MibTableColumn
hwDot3ahEfmEventLogIndex = _HwDot3ahEfmEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 1),
    _HwDot3ahEfmEventLogIndex_Type()
)
hwDot3ahEfmEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogIndex.setStatus("current")
_HwDot3ahEfmEventLogTimestamp_Type = TimeStamp
_HwDot3ahEfmEventLogTimestamp_Object = MibTableColumn
hwDot3ahEfmEventLogTimestamp = _HwDot3ahEfmEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 2),
    _HwDot3ahEfmEventLogTimestamp_Type()
)
hwDot3ahEfmEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogTimestamp.setStatus("current")
_HwDot3ahEfmEventLogOui_Type = HWDot3Oui
_HwDot3ahEfmEventLogOui_Object = MibTableColumn
hwDot3ahEfmEventLogOui = _HwDot3ahEfmEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 3),
    _HwDot3ahEfmEventLogOui_Type()
)
hwDot3ahEfmEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogOui.setStatus("current")
_HwDot3ahEfmEventLogType_Type = Unsigned32
_HwDot3ahEfmEventLogType_Object = MibTableColumn
hwDot3ahEfmEventLogType = _HwDot3ahEfmEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 4),
    _HwDot3ahEfmEventLogType_Type()
)
hwDot3ahEfmEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogType.setStatus("current")


class _HwDot3ahEfmEventLogLocation_Type(Integer32):
    """Custom type hwDot3ahEfmEventLogLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_HwDot3ahEfmEventLogLocation_Type.__name__ = "Integer32"
_HwDot3ahEfmEventLogLocation_Object = MibTableColumn
hwDot3ahEfmEventLogLocation = _HwDot3ahEfmEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 5),
    _HwDot3ahEfmEventLogLocation_Type()
)
hwDot3ahEfmEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogLocation.setStatus("current")
_HwDot3ahEfmEventLogWindowHi_Type = Unsigned32
_HwDot3ahEfmEventLogWindowHi_Object = MibTableColumn
hwDot3ahEfmEventLogWindowHi = _HwDot3ahEfmEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 6),
    _HwDot3ahEfmEventLogWindowHi_Type()
)
hwDot3ahEfmEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogWindowHi.setStatus("current")
_HwDot3ahEfmEventLogWindowLo_Type = Unsigned32
_HwDot3ahEfmEventLogWindowLo_Object = MibTableColumn
hwDot3ahEfmEventLogWindowLo = _HwDot3ahEfmEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 7),
    _HwDot3ahEfmEventLogWindowLo_Type()
)
hwDot3ahEfmEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogWindowLo.setStatus("current")
_HwDot3ahEfmEventLogThresholdHi_Type = Unsigned32
_HwDot3ahEfmEventLogThresholdHi_Object = MibTableColumn
hwDot3ahEfmEventLogThresholdHi = _HwDot3ahEfmEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 8),
    _HwDot3ahEfmEventLogThresholdHi_Type()
)
hwDot3ahEfmEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogThresholdHi.setStatus("current")
_HwDot3ahEfmEventLogThresholdLo_Type = Unsigned32
_HwDot3ahEfmEventLogThresholdLo_Object = MibTableColumn
hwDot3ahEfmEventLogThresholdLo = _HwDot3ahEfmEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 9),
    _HwDot3ahEfmEventLogThresholdLo_Type()
)
hwDot3ahEfmEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogThresholdLo.setStatus("current")
_HwDot3ahEfmEventLogValue_Type = CounterBasedGauge64
_HwDot3ahEfmEventLogValue_Object = MibTableColumn
hwDot3ahEfmEventLogValue = _HwDot3ahEfmEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 10),
    _HwDot3ahEfmEventLogValue_Type()
)
hwDot3ahEfmEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogValue.setStatus("current")
_HwDot3ahEfmEventLogRunningTotal_Type = CounterBasedGauge64
_HwDot3ahEfmEventLogRunningTotal_Object = MibTableColumn
hwDot3ahEfmEventLogRunningTotal = _HwDot3ahEfmEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 11),
    _HwDot3ahEfmEventLogRunningTotal_Type()
)
hwDot3ahEfmEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogRunningTotal.setStatus("current")
_HwDot3ahEfmEventLogEventTotal_Type = Unsigned32
_HwDot3ahEfmEventLogEventTotal_Object = MibTableColumn
hwDot3ahEfmEventLogEventTotal = _HwDot3ahEfmEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 7, 1, 12),
    _HwDot3ahEfmEventLogEventTotal_Type()
)
hwDot3ahEfmEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogEventTotal.setStatus("current")
_HwDot3ahEfmManagerTable_Object = MibTable
hwDot3ahEfmManagerTable = _HwDot3ahEfmManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hwDot3ahEfmManagerTable.setStatus("current")
_HwDot3ahEfmManagerEntry_Object = MibTableRow
hwDot3ahEfmManagerEntry = _HwDot3ahEfmManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 8, 1)
)
hwDot3ahEfmManagerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwDot3ahEfmManagerEntry.setStatus("current")
_HwDot3ahEfmTriggerIfDown_Type = EnabledStatus
_HwDot3ahEfmTriggerIfDown_Object = MibTableColumn
hwDot3ahEfmTriggerIfDown = _HwDot3ahEfmTriggerIfDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 8, 1, 1),
    _HwDot3ahEfmTriggerIfDown_Type()
)
hwDot3ahEfmTriggerIfDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmTriggerIfDown.setStatus("current")


class _HwDot3ahEfmHoldUpTime_Type(Integer32):
    """Custom type hwDot3ahEfmHoldUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_HwDot3ahEfmHoldUpTime_Type.__name__ = "Integer32"
_HwDot3ahEfmHoldUpTime_Object = MibTableColumn
hwDot3ahEfmHoldUpTime = _HwDot3ahEfmHoldUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 8, 1, 2),
    _HwDot3ahEfmHoldUpTime_Type()
)
hwDot3ahEfmHoldUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEfmHoldUpTime.setStatus("current")
_HwDot3ahEvrrpTable_Object = MibTable
hwDot3ahEvrrpTable = _HwDot3ahEvrrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    hwDot3ahEvrrpTable.setStatus("current")
_HwDot3ahEvrrpEntry_Object = MibTableRow
hwDot3ahEvrrpEntry = _HwDot3ahEvrrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 9, 1)
)
hwDot3ahEvrrpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwDot3ahEvrrpEntry.setStatus("current")


class _HwDot3ahEvrrpCpuState_Type(Integer32):
    """Custom type hwDot3ahEvrrpCpuState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("unknown", 3))
    )


_HwDot3ahEvrrpCpuState_Type.__name__ = "Integer32"
_HwDot3ahEvrrpCpuState_Object = MibTableColumn
hwDot3ahEvrrpCpuState = _HwDot3ahEvrrpCpuState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 9, 1, 1),
    _HwDot3ahEvrrpCpuState_Type()
)
hwDot3ahEvrrpCpuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot3ahEvrrpCpuState.setStatus("current")
_HwDot3ahEvrrpTriggerIfDown_Type = EnabledStatus
_HwDot3ahEvrrpTriggerIfDown_Object = MibTableColumn
hwDot3ahEvrrpTriggerIfDown = _HwDot3ahEvrrpTriggerIfDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 9, 1, 2),
    _HwDot3ahEvrrpTriggerIfDown_Type()
)
hwDot3ahEvrrpTriggerIfDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEvrrpTriggerIfDown.setStatus("obsolete")


class _HwDot3ahEvrrpHoldUpTime_Type(Integer32):
    """Custom type hwDot3ahEvrrpHoldUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_HwDot3ahEvrrpHoldUpTime_Type.__name__ = "Integer32"
_HwDot3ahEvrrpHoldUpTime_Object = MibTableColumn
hwDot3ahEvrrpHoldUpTime = _HwDot3ahEvrrpHoldUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 2, 2, 9, 1, 3),
    _HwDot3ahEvrrpHoldUpTime_Type()
)
hwDot3ahEvrrpHoldUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot3ahEvrrpHoldUpTime.setStatus("obsolete")
_HwOamManager_ObjectIdentity = ObjectIdentity
hwOamManager = _HwOamManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 3)
)
_HwTestMessage_ObjectIdentity = ObjectIdentity
hwTestMessage = _HwTestMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4)
)
_HwTestMessageObject_ObjectIdentity = ObjectIdentity
hwTestMessageObject = _HwTestMessageObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1)
)
_HwTestMessageTableNextIndex_Type = Unsigned32
_HwTestMessageTableNextIndex_Object = MibScalar
hwTestMessageTableNextIndex = _HwTestMessageTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 1),
    _HwTestMessageTableNextIndex_Type()
)
hwTestMessageTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTestMessageTableNextIndex.setStatus("current")
_HwTestMessageTable_Object = MibTable
hwTestMessageTable = _HwTestMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hwTestMessageTable.setStatus("current")
_HwTestMessageEntry_Object = MibTableRow
hwTestMessageEntry = _HwTestMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1)
)
hwTestMessageEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwTestMessageIndex"),
)
if mibBuilder.loadTexts:
    hwTestMessageEntry.setStatus("current")
_HwTestMessageIndex_Type = Unsigned32
_HwTestMessageIndex_Object = MibTableColumn
hwTestMessageIndex = _HwTestMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 1),
    _HwTestMessageIndex_Type()
)
hwTestMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTestMessageIndex.setStatus("current")
_HwTestMessageMacAddress_Type = MacAddress
_HwTestMessageMacAddress_Object = MibTableColumn
hwTestMessageMacAddress = _HwTestMessageMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 11),
    _HwTestMessageMacAddress_Type()
)
hwTestMessageMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTestMessageMacAddress.setStatus("current")
_HwTestMessageVlanID_Type = Unsigned32
_HwTestMessageVlanID_Object = MibTableColumn
hwTestMessageVlanID = _HwTestMessageVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 12),
    _HwTestMessageVlanID_Type()
)
hwTestMessageVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTestMessageVlanID.setStatus("current")
_HwTestMessageInterface_Type = OctetString
_HwTestMessageInterface_Object = MibTableColumn
hwTestMessageInterface = _HwTestMessageInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 13),
    _HwTestMessageInterface_Type()
)
hwTestMessageInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTestMessageInterface.setStatus("current")
_HwTestMessageServiceInstance_Type = OctetString
_HwTestMessageServiceInstance_Object = MibTableColumn
hwTestMessageServiceInstance = _HwTestMessageServiceInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 14),
    _HwTestMessageServiceInstance_Type()
)
hwTestMessageServiceInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTestMessageServiceInstance.setStatus("current")


class _HwTestMessagePacketSize_Type(Unsigned32):
    """Custom type hwTestMessagePacketSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_HwTestMessagePacketSize_Type.__name__ = "Unsigned32"
_HwTestMessagePacketSize_Object = MibTableColumn
hwTestMessagePacketSize = _HwTestMessagePacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 15),
    _HwTestMessagePacketSize_Type()
)
hwTestMessagePacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTestMessagePacketSize.setStatus("current")


class _HwTestMessageSendPackets_Type(Unsigned32):
    """Custom type hwTestMessageSendPackets based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwTestMessageSendPackets_Type.__name__ = "Unsigned32"
_HwTestMessageSendPackets_Object = MibTableColumn
hwTestMessageSendPackets = _HwTestMessageSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 16),
    _HwTestMessageSendPackets_Type()
)
hwTestMessageSendPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTestMessageSendPackets.setStatus("current")


class _HwTestMessageSendSpeed_Type(HWTestMessageSendSpeed):
    """Custom type hwTestMessageSendSpeed based on HWTestMessageSendSpeed"""


_HwTestMessageSendSpeed_Object = MibTableColumn
hwTestMessageSendSpeed = _HwTestMessageSendSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 17),
    _HwTestMessageSendSpeed_Type()
)
hwTestMessageSendSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTestMessageSendSpeed.setStatus("current")
_HwTestMessageSendEnabled_Type = TruthValue
_HwTestMessageSendEnabled_Object = MibTableColumn
hwTestMessageSendEnabled = _HwTestMessageSendEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 18),
    _HwTestMessageSendEnabled_Type()
)
hwTestMessageSendEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTestMessageSendEnabled.setStatus("current")
_HwTestMessageSendFinished_Type = HWTestMessageFinishedValue
_HwTestMessageSendFinished_Object = MibTableColumn
hwTestMessageSendFinished = _HwTestMessageSendFinished_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 19),
    _HwTestMessageSendFinished_Type()
)
hwTestMessageSendFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTestMessageSendFinished.setStatus("current")
_HwTestMessageRowStatus_Type = RowStatus
_HwTestMessageRowStatus_Object = MibTableColumn
hwTestMessageRowStatus = _HwTestMessageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 2, 1, 51),
    _HwTestMessageRowStatus_Type()
)
hwTestMessageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTestMessageRowStatus.setStatus("current")
_HwTestMessageResultTable_Object = MibTable
hwTestMessageResultTable = _HwTestMessageResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hwTestMessageResultTable.setStatus("current")
_HwTestMessageResultEntry_Object = MibTableRow
hwTestMessageResultEntry = _HwTestMessageResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 3, 1)
)
hwTestMessageResultEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwTestMessageIndex"),
)
if mibBuilder.loadTexts:
    hwTestMessageResultEntry.setStatus("current")
_HwTestMessageResultSendPackets_Type = Unsigned32
_HwTestMessageResultSendPackets_Object = MibTableColumn
hwTestMessageResultSendPackets = _HwTestMessageResultSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 3, 1, 11),
    _HwTestMessageResultSendPackets_Type()
)
hwTestMessageResultSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTestMessageResultSendPackets.setStatus("current")
_HwTestMessageResultReceivedPackets_Type = Unsigned32
_HwTestMessageResultReceivedPackets_Object = MibTableColumn
hwTestMessageResultReceivedPackets = _HwTestMessageResultReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 3, 1, 12),
    _HwTestMessageResultReceivedPackets_Type()
)
hwTestMessageResultReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTestMessageResultReceivedPackets.setStatus("current")
_HwTestMessageResultPacketsLost_Type = Unsigned32
_HwTestMessageResultPacketsLost_Object = MibTableColumn
hwTestMessageResultPacketsLost = _HwTestMessageResultPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 3, 1, 13),
    _HwTestMessageResultPacketsLost_Type()
)
hwTestMessageResultPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTestMessageResultPacketsLost.setStatus("current")
_HwTestMessageResultSendBytes_Type = Unsigned32
_HwTestMessageResultSendBytes_Object = MibTableColumn
hwTestMessageResultSendBytes = _HwTestMessageResultSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 3, 1, 14),
    _HwTestMessageResultSendBytes_Type()
)
hwTestMessageResultSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTestMessageResultSendBytes.setStatus("current")
_HwTestMessageResultReceivedBytes_Type = Unsigned32
_HwTestMessageResultReceivedBytes_Object = MibTableColumn
hwTestMessageResultReceivedBytes = _HwTestMessageResultReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 3, 1, 15),
    _HwTestMessageResultReceivedBytes_Type()
)
hwTestMessageResultReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTestMessageResultReceivedBytes.setStatus("current")
_HwTestMessageResultBytesLost_Type = Unsigned32
_HwTestMessageResultBytesLost_Object = MibTableColumn
hwTestMessageResultBytesLost = _HwTestMessageResultBytesLost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 3, 1, 16),
    _HwTestMessageResultBytesLost_Type()
)
hwTestMessageResultBytesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTestMessageResultBytesLost.setStatus("current")
_HwTestMessageBeginTimeStamp_Type = TimeStamp
_HwTestMessageBeginTimeStamp_Object = MibTableColumn
hwTestMessageBeginTimeStamp = _HwTestMessageBeginTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 3, 1, 17),
    _HwTestMessageBeginTimeStamp_Type()
)
hwTestMessageBeginTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTestMessageBeginTimeStamp.setStatus("current")
_HwTestMessageEndTimeStamp_Type = TimeStamp
_HwTestMessageEndTimeStamp_Object = MibTableColumn
hwTestMessageEndTimeStamp = _HwTestMessageEndTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 4, 1, 3, 1, 18),
    _HwTestMessageEndTimeStamp_Type()
)
hwTestMessageEndTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTestMessageEndTimeStamp.setStatus("current")
_HwEthOamTraps_ObjectIdentity = ObjectIdentity
hwEthOamTraps = _HwEthOamTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6)
)
_HwEthOamConformance_ObjectIdentity = ObjectIdentity
hwEthOamConformance = _HwEthOamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7)
)
_HwEthOamCompliances_ObjectIdentity = ObjectIdentity
hwEthOamCompliances = _HwEthOamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 1)
)
_HwEthOamGroups_ObjectIdentity = ObjectIdentity
hwEthOamGroups = _HwEthOamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2)
)
_HwEthOamY1731_ObjectIdentity = ObjectIdentity
hwEthOamY1731 = _HwEthOamY1731_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8)
)
_HwY1731ConfigObject_ObjectIdentity = ObjectIdentity
hwY1731ConfigObject = _HwY1731ConfigObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1)
)
_HwY1731BaseConfigTable_Object = MibTable
hwY1731BaseConfigTable = _HwY1731BaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hwY1731BaseConfigTable.setStatus("current")
_HwY1731BaseConfigEntry_Object = MibTableRow
hwY1731BaseConfigEntry = _HwY1731BaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 1, 1)
)
hwY1731BaseConfigEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    hwY1731BaseConfigEntry.setStatus("current")


class _HwY1731PwMeasureMode_Type(Integer32):
    """Custom type hwY1731PwMeasureMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asymmetry", 3),
          ("invalid", 1),
          ("symmetry", 2))
    )


_HwY1731PwMeasureMode_Type.__name__ = "Integer32"
_HwY1731PwMeasureMode_Object = MibTableColumn
hwY1731PwMeasureMode = _HwY1731PwMeasureMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 1, 1, 1),
    _HwY1731PwMeasureMode_Type()
)
hwY1731PwMeasureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwY1731PwMeasureMode.setStatus("current")
_HwY1731OneDelayThreshold_Type = Unsigned32
_HwY1731OneDelayThreshold_Object = MibTableColumn
hwY1731OneDelayThreshold = _HwY1731OneDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 1, 1, 2),
    _HwY1731OneDelayThreshold_Type()
)
hwY1731OneDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwY1731OneDelayThreshold.setStatus("current")
_HwY1731TwoDelayThreshold_Type = Unsigned32
_HwY1731TwoDelayThreshold_Object = MibTableColumn
hwY1731TwoDelayThreshold = _HwY1731TwoDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 1, 1, 3),
    _HwY1731TwoDelayThreshold_Type()
)
hwY1731TwoDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwY1731TwoDelayThreshold.setStatus("current")
_HwY1731ConfigTable_Object = MibTable
hwY1731ConfigTable = _HwY1731ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hwY1731ConfigTable.setStatus("current")
_HwY1731ConfigEntry_Object = MibTableRow
hwY1731ConfigEntry = _HwY1731ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1)
)
hwY1731ConfigEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731RemoteIp"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731VcId"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731MacAddress"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731ResvIndex"),
)
if mibBuilder.loadTexts:
    hwY1731ConfigEntry.setStatus("current")
_HwY1731RemoteIp_Type = IpAddress
_HwY1731RemoteIp_Object = MibTableColumn
hwY1731RemoteIp = _HwY1731RemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 1),
    _HwY1731RemoteIp_Type()
)
hwY1731RemoteIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731RemoteIp.setStatus("current")
_HwY1731VcId_Type = Unsigned32
_HwY1731VcId_Object = MibTableColumn
hwY1731VcId = _HwY1731VcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 2),
    _HwY1731VcId_Type()
)
hwY1731VcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731VcId.setStatus("current")
_HwY1731MacAddress_Type = MacAddress
_HwY1731MacAddress_Object = MibTableColumn
hwY1731MacAddress = _HwY1731MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 3),
    _HwY1731MacAddress_Type()
)
hwY1731MacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731MacAddress.setStatus("current")
_HwY1731ResvIndex_Type = Integer32
_HwY1731ResvIndex_Object = MibTableColumn
hwY1731ResvIndex = _HwY1731ResvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 4),
    _HwY1731ResvIndex_Type()
)
hwY1731ResvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731ResvIndex.setStatus("current")


class _HwY1731ServiceType_Type(Integer32):
    """Custom type hwY1731ServiceType based on Integer32"""
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
        *(("ccc", 6),
          ("unbind", 5),
          ("unknown", 4),
          ("vlan", 1),
          ("vll", 3),
          ("vsi", 2))
    )


_HwY1731ServiceType_Type.__name__ = "Integer32"
_HwY1731ServiceType_Object = MibTableColumn
hwY1731ServiceType = _HwY1731ServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 5),
    _HwY1731ServiceType_Type()
)
hwY1731ServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731ServiceType.setStatus("current")
_HwY1731SingleLossRecvEnable_Type = EnabledStatus
_HwY1731SingleLossRecvEnable_Object = MibTableColumn
hwY1731SingleLossRecvEnable = _HwY1731SingleLossRecvEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 6),
    _HwY1731SingleLossRecvEnable_Type()
)
hwY1731SingleLossRecvEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossRecvEnable.setStatus("current")
_HwY1731OneDelayRecvEnable_Type = EnabledStatus
_HwY1731OneDelayRecvEnable_Object = MibTableColumn
hwY1731OneDelayRecvEnable = _HwY1731OneDelayRecvEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 7),
    _HwY1731OneDelayRecvEnable_Type()
)
hwY1731OneDelayRecvEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayRecvEnable.setStatus("current")
_HwY1731OneDelayRecvEnableIsContinue_Type = TruthValue
_HwY1731OneDelayRecvEnableIsContinue_Object = MibTableColumn
hwY1731OneDelayRecvEnableIsContinue = _HwY1731OneDelayRecvEnableIsContinue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 8),
    _HwY1731OneDelayRecvEnableIsContinue_Type()
)
hwY1731OneDelayRecvEnableIsContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayRecvEnableIsContinue.setStatus("current")
_HwY1731TwoDelayRecvEnable_Type = EnabledStatus
_HwY1731TwoDelayRecvEnable_Object = MibTableColumn
hwY1731TwoDelayRecvEnable = _HwY1731TwoDelayRecvEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 9),
    _HwY1731TwoDelayRecvEnable_Type()
)
hwY1731TwoDelayRecvEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayRecvEnable.setStatus("current")
_HwY1731SingleLossEnable_Type = EnabledStatus
_HwY1731SingleLossEnable_Object = MibTableColumn
hwY1731SingleLossEnable = _HwY1731SingleLossEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 10),
    _HwY1731SingleLossEnable_Type()
)
hwY1731SingleLossEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossEnable.setStatus("current")
_HwY1731SingleLossIsContinue_Type = TruthValue
_HwY1731SingleLossIsContinue_Object = MibTableColumn
hwY1731SingleLossIsContinue = _HwY1731SingleLossIsContinue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 11),
    _HwY1731SingleLossIsContinue_Type()
)
hwY1731SingleLossIsContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossIsContinue.setStatus("current")


class _HwY1731SingleLossMepId_Type(Integer32):
    """Custom type hwY1731SingleLossMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731SingleLossMepId_Type.__name__ = "Integer32"
_HwY1731SingleLossMepId_Object = MibTableColumn
hwY1731SingleLossMepId = _HwY1731SingleLossMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 12),
    _HwY1731SingleLossMepId_Type()
)
hwY1731SingleLossMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossMepId.setStatus("current")
_HwY1731SingleLossDestIsMepId_Type = TruthValue
_HwY1731SingleLossDestIsMepId_Object = MibTableColumn
hwY1731SingleLossDestIsMepId = _HwY1731SingleLossDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 13),
    _HwY1731SingleLossDestIsMepId_Type()
)
hwY1731SingleLossDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossDestIsMepId.setStatus("current")


class _HwY1731SingleLossDestMepId_Type(Integer32):
    """Custom type hwY1731SingleLossDestMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731SingleLossDestMepId_Type.__name__ = "Integer32"
_HwY1731SingleLossDestMepId_Object = MibTableColumn
hwY1731SingleLossDestMepId = _HwY1731SingleLossDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 14),
    _HwY1731SingleLossDestMepId_Type()
)
hwY1731SingleLossDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossDestMepId.setStatus("current")
_HwY1731SingleLossMacAddress_Type = MacAddress
_HwY1731SingleLossMacAddress_Object = MibTableColumn
hwY1731SingleLossMacAddress = _HwY1731SingleLossMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 15),
    _HwY1731SingleLossMacAddress_Type()
)
hwY1731SingleLossMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossMacAddress.setStatus("current")


class _HwY1731SingleLossInterval_Type(Integer32):
    """Custom type hwY1731SingleLossInterval based on Integer32"""
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
        *(("interval10s", 3),
          ("interval1s", 2),
          ("interval30s", 4),
          ("invalid", 1))
    )


_HwY1731SingleLossInterval_Type.__name__ = "Integer32"
_HwY1731SingleLossInterval_Object = MibTableColumn
hwY1731SingleLossInterval = _HwY1731SingleLossInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 16),
    _HwY1731SingleLossInterval_Type()
)
hwY1731SingleLossInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossInterval.setStatus("current")


class _HwY1731SingleLossCount_Type(Integer32):
    """Custom type hwY1731SingleLossCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 60),
    )


_HwY1731SingleLossCount_Type.__name__ = "Integer32"
_HwY1731SingleLossCount_Object = MibTableColumn
hwY1731SingleLossCount = _HwY1731SingleLossCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 17),
    _HwY1731SingleLossCount_Type()
)
hwY1731SingleLossCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossCount.setStatus("current")


class _HwY1731SingleLoss8021pValue_Type(Integer32):
    """Custom type hwY1731SingleLoss8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_HwY1731SingleLoss8021pValue_Type.__name__ = "Integer32"
_HwY1731SingleLoss8021pValue_Object = MibTableColumn
hwY1731SingleLoss8021pValue = _HwY1731SingleLoss8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 18),
    _HwY1731SingleLoss8021pValue_Type()
)
hwY1731SingleLoss8021pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLoss8021pValue.setStatus("current")
_HwY1731DualLossEnable_Type = EnabledStatus
_HwY1731DualLossEnable_Object = MibTableColumn
hwY1731DualLossEnable = _HwY1731DualLossEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 19),
    _HwY1731DualLossEnable_Type()
)
hwY1731DualLossEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731DualLossEnable.setStatus("current")


class _HwY1731DualLossMepId_Type(Integer32):
    """Custom type hwY1731DualLossMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731DualLossMepId_Type.__name__ = "Integer32"
_HwY1731DualLossMepId_Object = MibTableColumn
hwY1731DualLossMepId = _HwY1731DualLossMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 20),
    _HwY1731DualLossMepId_Type()
)
hwY1731DualLossMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731DualLossMepId.setStatus("current")


class _HwY1731DualLossDestMepId_Type(Integer32):
    """Custom type hwY1731DualLossDestMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731DualLossDestMepId_Type.__name__ = "Integer32"
_HwY1731DualLossDestMepId_Object = MibTableColumn
hwY1731DualLossDestMepId = _HwY1731DualLossDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 21),
    _HwY1731DualLossDestMepId_Type()
)
hwY1731DualLossDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731DualLossDestMepId.setStatus("current")
_HwY1731OneDelayEnable_Type = EnabledStatus
_HwY1731OneDelayEnable_Object = MibTableColumn
hwY1731OneDelayEnable = _HwY1731OneDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 22),
    _HwY1731OneDelayEnable_Type()
)
hwY1731OneDelayEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayEnable.setStatus("current")
_HwY1731OneDelayIsContinue_Type = TruthValue
_HwY1731OneDelayIsContinue_Object = MibTableColumn
hwY1731OneDelayIsContinue = _HwY1731OneDelayIsContinue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 23),
    _HwY1731OneDelayIsContinue_Type()
)
hwY1731OneDelayIsContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayIsContinue.setStatus("current")


class _HwY1731OneDelayMepId_Type(Integer32):
    """Custom type hwY1731OneDelayMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731OneDelayMepId_Type.__name__ = "Integer32"
_HwY1731OneDelayMepId_Object = MibTableColumn
hwY1731OneDelayMepId = _HwY1731OneDelayMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 24),
    _HwY1731OneDelayMepId_Type()
)
hwY1731OneDelayMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayMepId.setStatus("current")
_HwY1731OneDelayDestIsMepId_Type = TruthValue
_HwY1731OneDelayDestIsMepId_Object = MibTableColumn
hwY1731OneDelayDestIsMepId = _HwY1731OneDelayDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 25),
    _HwY1731OneDelayDestIsMepId_Type()
)
hwY1731OneDelayDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayDestIsMepId.setStatus("current")


class _HwY1731OneDelayDestMepId_Type(Integer32):
    """Custom type hwY1731OneDelayDestMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731OneDelayDestMepId_Type.__name__ = "Integer32"
_HwY1731OneDelayDestMepId_Object = MibTableColumn
hwY1731OneDelayDestMepId = _HwY1731OneDelayDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 26),
    _HwY1731OneDelayDestMepId_Type()
)
hwY1731OneDelayDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayDestMepId.setStatus("current")
_HwY1731OneDelayMacAddress_Type = MacAddress
_HwY1731OneDelayMacAddress_Object = MibTableColumn
hwY1731OneDelayMacAddress = _HwY1731OneDelayMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 27),
    _HwY1731OneDelayMacAddress_Type()
)
hwY1731OneDelayMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayMacAddress.setStatus("current")


class _HwY1731OneDelayInterval_Type(Integer32):
    """Custom type hwY1731OneDelayInterval based on Integer32"""
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
        *(("interval10s", 3),
          ("interval1s", 2),
          ("interval30s", 4),
          ("invalid", 1))
    )


_HwY1731OneDelayInterval_Type.__name__ = "Integer32"
_HwY1731OneDelayInterval_Object = MibTableColumn
hwY1731OneDelayInterval = _HwY1731OneDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 28),
    _HwY1731OneDelayInterval_Type()
)
hwY1731OneDelayInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayInterval.setStatus("current")


class _HwY1731OneDelayCount_Type(Integer32):
    """Custom type hwY1731OneDelayCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 60),
    )


_HwY1731OneDelayCount_Type.__name__ = "Integer32"
_HwY1731OneDelayCount_Object = MibTableColumn
hwY1731OneDelayCount = _HwY1731OneDelayCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 29),
    _HwY1731OneDelayCount_Type()
)
hwY1731OneDelayCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayCount.setStatus("current")


class _HwY1731OneDelay8021pValue_Type(Integer32):
    """Custom type hwY1731OneDelay8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_HwY1731OneDelay8021pValue_Type.__name__ = "Integer32"
_HwY1731OneDelay8021pValue_Object = MibTableColumn
hwY1731OneDelay8021pValue = _HwY1731OneDelay8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 30),
    _HwY1731OneDelay8021pValue_Type()
)
hwY1731OneDelay8021pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelay8021pValue.setStatus("current")
_HwY1731TwoDelayEnable_Type = EnabledStatus
_HwY1731TwoDelayEnable_Object = MibTableColumn
hwY1731TwoDelayEnable = _HwY1731TwoDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 31),
    _HwY1731TwoDelayEnable_Type()
)
hwY1731TwoDelayEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayEnable.setStatus("current")
_HwY1731TwoDelayIsContinue_Type = TruthValue
_HwY1731TwoDelayIsContinue_Object = MibTableColumn
hwY1731TwoDelayIsContinue = _HwY1731TwoDelayIsContinue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 32),
    _HwY1731TwoDelayIsContinue_Type()
)
hwY1731TwoDelayIsContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayIsContinue.setStatus("current")


class _HwY1731TwoDelayMepId_Type(Integer32):
    """Custom type hwY1731TwoDelayMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731TwoDelayMepId_Type.__name__ = "Integer32"
_HwY1731TwoDelayMepId_Object = MibTableColumn
hwY1731TwoDelayMepId = _HwY1731TwoDelayMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 33),
    _HwY1731TwoDelayMepId_Type()
)
hwY1731TwoDelayMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayMepId.setStatus("current")
_HwY1731TwoDelayDestIsMepId_Type = TruthValue
_HwY1731TwoDelayDestIsMepId_Object = MibTableColumn
hwY1731TwoDelayDestIsMepId = _HwY1731TwoDelayDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 34),
    _HwY1731TwoDelayDestIsMepId_Type()
)
hwY1731TwoDelayDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayDestIsMepId.setStatus("current")


class _HwY1731TwoDelayDestMepId_Type(Integer32):
    """Custom type hwY1731TwoDelayDestMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731TwoDelayDestMepId_Type.__name__ = "Integer32"
_HwY1731TwoDelayDestMepId_Object = MibTableColumn
hwY1731TwoDelayDestMepId = _HwY1731TwoDelayDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 35),
    _HwY1731TwoDelayDestMepId_Type()
)
hwY1731TwoDelayDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayDestMepId.setStatus("current")
_HwY1731TwoDelayMacAddress_Type = MacAddress
_HwY1731TwoDelayMacAddress_Object = MibTableColumn
hwY1731TwoDelayMacAddress = _HwY1731TwoDelayMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 36),
    _HwY1731TwoDelayMacAddress_Type()
)
hwY1731TwoDelayMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayMacAddress.setStatus("current")


class _HwY1731TwoDelayInterval_Type(Integer32):
    """Custom type hwY1731TwoDelayInterval based on Integer32"""
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
        *(("interval10s", 3),
          ("interval1s", 2),
          ("interval30s", 4),
          ("invalid", 1))
    )


_HwY1731TwoDelayInterval_Type.__name__ = "Integer32"
_HwY1731TwoDelayInterval_Object = MibTableColumn
hwY1731TwoDelayInterval = _HwY1731TwoDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 37),
    _HwY1731TwoDelayInterval_Type()
)
hwY1731TwoDelayInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayInterval.setStatus("current")


class _HwY1731TwoDelayCount_Type(Integer32):
    """Custom type hwY1731TwoDelayCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 60),
    )


_HwY1731TwoDelayCount_Type.__name__ = "Integer32"
_HwY1731TwoDelayCount_Object = MibTableColumn
hwY1731TwoDelayCount = _HwY1731TwoDelayCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 38),
    _HwY1731TwoDelayCount_Type()
)
hwY1731TwoDelayCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayCount.setStatus("current")


class _HwY1731TwoDelay8021pValue_Type(Integer32):
    """Custom type hwY1731TwoDelay8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_HwY1731TwoDelay8021pValue_Type.__name__ = "Integer32"
_HwY1731TwoDelay8021pValue_Object = MibTableColumn
hwY1731TwoDelay8021pValue = _HwY1731TwoDelay8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 39),
    _HwY1731TwoDelay8021pValue_Type()
)
hwY1731TwoDelay8021pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelay8021pValue.setStatus("current")


class _HwY1731SingleLossRecv8021pValue_Type(Integer32):
    """Custom type hwY1731SingleLossRecv8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_HwY1731SingleLossRecv8021pValue_Type.__name__ = "Integer32"
_HwY1731SingleLossRecv8021pValue_Object = MibTableColumn
hwY1731SingleLossRecv8021pValue = _HwY1731SingleLossRecv8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 40),
    _HwY1731SingleLossRecv8021pValue_Type()
)
hwY1731SingleLossRecv8021pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossRecv8021pValue.setStatus("current")


class _HwY1731OneDelayRecv8021pValue_Type(Integer32):
    """Custom type hwY1731OneDelayRecv8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_HwY1731OneDelayRecv8021pValue_Type.__name__ = "Integer32"
_HwY1731OneDelayRecv8021pValue_Object = MibTableColumn
hwY1731OneDelayRecv8021pValue = _HwY1731OneDelayRecv8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 41),
    _HwY1731OneDelayRecv8021pValue_Type()
)
hwY1731OneDelayRecv8021pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayRecv8021pValue.setStatus("current")


class _HwY1731TwoDelayRecv8021pValue_Type(Integer32):
    """Custom type hwY1731TwoDelayRecv8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_HwY1731TwoDelayRecv8021pValue_Type.__name__ = "Integer32"
_HwY1731TwoDelayRecv8021pValue_Object = MibTableColumn
hwY1731TwoDelayRecv8021pValue = _HwY1731TwoDelayRecv8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 42),
    _HwY1731TwoDelayRecv8021pValue_Type()
)
hwY1731TwoDelayRecv8021pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayRecv8021pValue.setStatus("current")


class _HwY1731SingleLossRecvMepId_Type(Integer32):
    """Custom type hwY1731SingleLossRecvMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731SingleLossRecvMepId_Type.__name__ = "Integer32"
_HwY1731SingleLossRecvMepId_Object = MibTableColumn
hwY1731SingleLossRecvMepId = _HwY1731SingleLossRecvMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 43),
    _HwY1731SingleLossRecvMepId_Type()
)
hwY1731SingleLossRecvMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731SingleLossRecvMepId.setStatus("current")


class _HwY1731OneDelayRecvMepId_Type(Integer32):
    """Custom type hwY1731OneDelayRecvMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731OneDelayRecvMepId_Type.__name__ = "Integer32"
_HwY1731OneDelayRecvMepId_Object = MibTableColumn
hwY1731OneDelayRecvMepId = _HwY1731OneDelayRecvMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 44),
    _HwY1731OneDelayRecvMepId_Type()
)
hwY1731OneDelayRecvMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayRecvMepId.setStatus("current")


class _HwY1731TwoDelayRecvMepId_Type(Integer32):
    """Custom type hwY1731TwoDelayRecvMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731TwoDelayRecvMepId_Type.__name__ = "Integer32"
_HwY1731TwoDelayRecvMepId_Object = MibTableColumn
hwY1731TwoDelayRecvMepId = _HwY1731TwoDelayRecvMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 45),
    _HwY1731TwoDelayRecvMepId_Type()
)
hwY1731TwoDelayRecvMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayRecvMepId.setStatus("current")


class _HwY1731OneDelayPacketSize_Type(Integer32):
    """Custom type hwY1731OneDelayPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1518),
    )


_HwY1731OneDelayPacketSize_Type.__name__ = "Integer32"
_HwY1731OneDelayPacketSize_Object = MibTableColumn
hwY1731OneDelayPacketSize = _HwY1731OneDelayPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 46),
    _HwY1731OneDelayPacketSize_Type()
)
hwY1731OneDelayPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731OneDelayPacketSize.setStatus("current")


class _HwY1731TwoDelayPacketSize_Type(Integer32):
    """Custom type hwY1731TwoDelayPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1518),
    )


_HwY1731TwoDelayPacketSize_Type.__name__ = "Integer32"
_HwY1731TwoDelayPacketSize_Object = MibTableColumn
hwY1731TwoDelayPacketSize = _HwY1731TwoDelayPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 2, 1, 47),
    _HwY1731TwoDelayPacketSize_Type()
)
hwY1731TwoDelayPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TwoDelayPacketSize.setStatus("current")
_HwY1731AisTable_Object = MibTable
hwY1731AisTable = _HwY1731AisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hwY1731AisTable.setStatus("current")
_HwY1731AisEntry_Object = MibTableRow
hwY1731AisEntry = _HwY1731AisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 3, 1)
)
hwY1731AisEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    hwY1731AisEntry.setStatus("current")
_HwY1731AisEnable_Type = EnabledStatus
_HwY1731AisEnable_Object = MibTableColumn
hwY1731AisEnable = _HwY1731AisEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 3, 1, 1),
    _HwY1731AisEnable_Type()
)
hwY1731AisEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisEnable.setStatus("current")


class _HwY1731AisSendLevel_Type(Integer32):
    """Custom type hwY1731AisSendLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_HwY1731AisSendLevel_Type.__name__ = "Integer32"
_HwY1731AisSendLevel_Object = MibTableColumn
hwY1731AisSendLevel = _HwY1731AisSendLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 3, 1, 2),
    _HwY1731AisSendLevel_Type()
)
hwY1731AisSendLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisSendLevel.setStatus("current")


class _HwY1731AisSendInterval_Type(Integer32):
    """Custom type hwY1731AisSendInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interval1s", 1),
          ("interval60s", 2))
    )


_HwY1731AisSendInterval_Type.__name__ = "Integer32"
_HwY1731AisSendInterval_Object = MibTableColumn
hwY1731AisSendInterval = _HwY1731AisSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 3, 1, 3),
    _HwY1731AisSendInterval_Type()
)
hwY1731AisSendInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisSendInterval.setStatus("current")
_HwY1731AisSendPktStatus_Type = EnabledStatus
_HwY1731AisSendPktStatus_Object = MibTableColumn
hwY1731AisSendPktStatus = _HwY1731AisSendPktStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 3, 1, 4),
    _HwY1731AisSendPktStatus_Type()
)
hwY1731AisSendPktStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731AisSendPktStatus.setStatus("current")
_HwY1731AisSuppressEnable_Type = EnabledStatus
_HwY1731AisSuppressEnable_Object = MibTableColumn
hwY1731AisSuppressEnable = _HwY1731AisSuppressEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 3, 1, 5),
    _HwY1731AisSuppressEnable_Type()
)
hwY1731AisSuppressEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisSuppressEnable.setStatus("current")
_HwY1731AisSuppressStatus_Type = EnabledStatus
_HwY1731AisSuppressStatus_Object = MibTableColumn
hwY1731AisSuppressStatus = _HwY1731AisSuppressStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 3, 1, 6),
    _HwY1731AisSuppressStatus_Type()
)
hwY1731AisSuppressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731AisSuppressStatus.setStatus("current")
_HwY1731AisVlanTable_Object = MibTable
hwY1731AisVlanTable = _HwY1731AisVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 4)
)
if mibBuilder.loadTexts:
    hwY1731AisVlanTable.setStatus("current")
_HwY1731AisVlanEntry_Object = MibTableRow
hwY1731AisVlanEntry = _HwY1731AisVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 4, 1)
)
hwY1731AisVlanEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731AisVlanEntry.setStatus("current")
_HwY1731AisPeVlan_Type = VlanIdOrNone
_HwY1731AisPeVlan_Object = MibTableColumn
hwY1731AisPeVlan = _HwY1731AisPeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 4, 1, 1),
    _HwY1731AisPeVlan_Type()
)
hwY1731AisPeVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisPeVlan.setStatus("current")
_HwY1731AisLowCeVlan_Type = VlanIdOrNone
_HwY1731AisLowCeVlan_Object = MibTableColumn
hwY1731AisLowCeVlan = _HwY1731AisLowCeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 4, 1, 2),
    _HwY1731AisLowCeVlan_Type()
)
hwY1731AisLowCeVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisLowCeVlan.setStatus("current")
_HwY1731AisHighCeVlan_Type = VlanIdOrNone
_HwY1731AisHighCeVlan_Object = MibTableColumn
hwY1731AisHighCeVlan = _HwY1731AisHighCeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 4, 1, 3),
    _HwY1731AisHighCeVlan_Type()
)
hwY1731AisHighCeVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisHighCeVlan.setStatus("current")
_HwY1731AisLowDot1qVlan_Type = VlanIdOrNone
_HwY1731AisLowDot1qVlan_Object = MibTableColumn
hwY1731AisLowDot1qVlan = _HwY1731AisLowDot1qVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 4, 1, 4),
    _HwY1731AisLowDot1qVlan_Type()
)
hwY1731AisLowDot1qVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisLowDot1qVlan.setStatus("current")
_HwY1731AisHighDot1qVlan_Type = VlanIdOrNone
_HwY1731AisHighDot1qVlan_Object = MibTableColumn
hwY1731AisHighDot1qVlan = _HwY1731AisHighDot1qVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 4, 1, 5),
    _HwY1731AisHighDot1qVlan_Type()
)
hwY1731AisHighDot1qVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisHighDot1qVlan.setStatus("current")
_HwY1731AisRowStatus_Type = RowStatus
_HwY1731AisRowStatus_Object = MibTableColumn
hwY1731AisRowStatus = _HwY1731AisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 4, 1, 99),
    _HwY1731AisRowStatus_Type()
)
hwY1731AisRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisRowStatus.setStatus("current")
_HwY1731AisLinkStatusTable_Object = MibTable
hwY1731AisLinkStatusTable = _HwY1731AisLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 5)
)
if mibBuilder.loadTexts:
    hwY1731AisLinkStatusTable.setStatus("current")
_HwY1731AisLinkStatusEntry_Object = MibTableRow
hwY1731AisLinkStatusEntry = _HwY1731AisLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 5, 1)
)
hwY1731AisLinkStatusEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731AisLinkStatusIfIndex"),
)
if mibBuilder.loadTexts:
    hwY1731AisLinkStatusEntry.setStatus("current")
_HwY1731AisLinkStatusIfIndex_Type = InterfaceIndex
_HwY1731AisLinkStatusIfIndex_Object = MibTableColumn
hwY1731AisLinkStatusIfIndex = _HwY1731AisLinkStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 5, 1, 1),
    _HwY1731AisLinkStatusIfIndex_Type()
)
hwY1731AisLinkStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731AisLinkStatusIfIndex.setStatus("current")
_HwY1731AisLinkRowStatus_Type = RowStatus
_HwY1731AisLinkRowStatus_Object = MibTableColumn
hwY1731AisLinkRowStatus = _HwY1731AisLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 5, 1, 20),
    _HwY1731AisLinkRowStatus_Type()
)
hwY1731AisLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisLinkRowStatus.setStatus("current")
_HwY1731MulPingTable_Object = MibTable
hwY1731MulPingTable = _HwY1731MulPingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6)
)
if mibBuilder.loadTexts:
    hwY1731MulPingTable.setStatus("current")
_HwY1731MulPingEntry_Object = MibTableRow
hwY1731MulPingEntry = _HwY1731MulPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1)
)
hwY1731MulPingEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731MulPingIndex"),
)
if mibBuilder.loadTexts:
    hwY1731MulPingEntry.setStatus("current")
_HwY1731MulPingIndex_Type = Unsigned32
_HwY1731MulPingIndex_Object = MibTableColumn
hwY1731MulPingIndex = _HwY1731MulPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 1),
    _HwY1731MulPingIndex_Type()
)
hwY1731MulPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731MulPingIndex.setStatus("current")
_HwY1731MulPingState_Type = EnabledStatus
_HwY1731MulPingState_Object = MibTableColumn
hwY1731MulPingState = _HwY1731MulPingState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 2),
    _HwY1731MulPingState_Type()
)
hwY1731MulPingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731MulPingState.setStatus("current")


class _HwY1731MulPingMdName_Type(OctetString):
    """Custom type hwY1731MulPingMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwY1731MulPingMdName_Type.__name__ = "OctetString"
_HwY1731MulPingMdName_Object = MibTableColumn
hwY1731MulPingMdName = _HwY1731MulPingMdName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 3),
    _HwY1731MulPingMdName_Type()
)
hwY1731MulPingMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731MulPingMdName.setStatus("current")


class _HwY1731MulPingMaName_Type(OctetString):
    """Custom type hwY1731MulPingMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwY1731MulPingMaName_Type.__name__ = "OctetString"
_HwY1731MulPingMaName_Object = MibTableColumn
hwY1731MulPingMaName = _HwY1731MulPingMaName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 4),
    _HwY1731MulPingMaName_Type()
)
hwY1731MulPingMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731MulPingMaName.setStatus("current")


class _HwY1731MulPingMepId_Type(Integer32):
    """Custom type hwY1731MulPingMepId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731MulPingMepId_Type.__name__ = "Integer32"
_HwY1731MulPingMepId_Object = MibTableColumn
hwY1731MulPingMepId = _HwY1731MulPingMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 5),
    _HwY1731MulPingMepId_Type()
)
hwY1731MulPingMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731MulPingMepId.setStatus("current")


class _HwY1731MulPingTimeout_Type(Unsigned32):
    """Custom type hwY1731MulPingTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwY1731MulPingTimeout_Type.__name__ = "Unsigned32"
_HwY1731MulPingTimeout_Object = MibTableColumn
hwY1731MulPingTimeout = _HwY1731MulPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 6),
    _HwY1731MulPingTimeout_Type()
)
hwY1731MulPingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731MulPingTimeout.setStatus("current")


class _HwY1731MulPingCount_Type(Unsigned32):
    """Custom type hwY1731MulPingCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwY1731MulPingCount_Type.__name__ = "Unsigned32"
_HwY1731MulPingCount_Object = MibTableColumn
hwY1731MulPingCount = _HwY1731MulPingCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 7),
    _HwY1731MulPingCount_Type()
)
hwY1731MulPingCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731MulPingCount.setStatus("current")


class _HwY1731MulPingPriority_Type(Integer32):
    """Custom type hwY1731MulPingPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwY1731MulPingPriority_Type.__name__ = "Integer32"
_HwY1731MulPingPriority_Object = MibTableColumn
hwY1731MulPingPriority = _HwY1731MulPingPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 8),
    _HwY1731MulPingPriority_Type()
)
hwY1731MulPingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731MulPingPriority.setStatus("current")
_HwY1731MulPingSendPacketNum_Type = Counter32
_HwY1731MulPingSendPacketNum_Object = MibTableColumn
hwY1731MulPingSendPacketNum = _HwY1731MulPingSendPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 9),
    _HwY1731MulPingSendPacketNum_Type()
)
hwY1731MulPingSendPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731MulPingSendPacketNum.setStatus("current")
_HwY1731MulPingRecvPacketNum_Type = Counter32
_HwY1731MulPingRecvPacketNum_Object = MibTableColumn
hwY1731MulPingRecvPacketNum = _HwY1731MulPingRecvPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 10),
    _HwY1731MulPingRecvPacketNum_Type()
)
hwY1731MulPingRecvPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731MulPingRecvPacketNum.setStatus("current")
_HwY1731MulPingRecvTimeDelayMin_Type = Unsigned32
_HwY1731MulPingRecvTimeDelayMin_Object = MibTableColumn
hwY1731MulPingRecvTimeDelayMin = _HwY1731MulPingRecvTimeDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 11),
    _HwY1731MulPingRecvTimeDelayMin_Type()
)
hwY1731MulPingRecvTimeDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731MulPingRecvTimeDelayMin.setStatus("current")
_HwY1731MulPingRecvTimeDelayMax_Type = Unsigned32
_HwY1731MulPingRecvTimeDelayMax_Object = MibTableColumn
hwY1731MulPingRecvTimeDelayMax = _HwY1731MulPingRecvTimeDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 12),
    _HwY1731MulPingRecvTimeDelayMax_Type()
)
hwY1731MulPingRecvTimeDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731MulPingRecvTimeDelayMax.setStatus("current")
_HwY1731MulPingRecvTimeDelayAvg_Type = Unsigned32
_HwY1731MulPingRecvTimeDelayAvg_Object = MibTableColumn
hwY1731MulPingRecvTimeDelayAvg = _HwY1731MulPingRecvTimeDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 13),
    _HwY1731MulPingRecvTimeDelayAvg_Type()
)
hwY1731MulPingRecvTimeDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731MulPingRecvTimeDelayAvg.setStatus("current")
_HwY1731MulPingRowStatus_Type = RowStatus
_HwY1731MulPingRowStatus_Object = MibTableColumn
hwY1731MulPingRowStatus = _HwY1731MulPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 6, 1, 99),
    _HwY1731MulPingRowStatus_Type()
)
hwY1731MulPingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731MulPingRowStatus.setStatus("current")
_HwY1731MulPingReplyTable_Object = MibTable
hwY1731MulPingReplyTable = _HwY1731MulPingReplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 7)
)
if mibBuilder.loadTexts:
    hwY1731MulPingReplyTable.setStatus("current")
_HwY1731MulPingReplyEntry_Object = MibTableRow
hwY1731MulPingReplyEntry = _HwY1731MulPingReplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 7, 1)
)
hwY1731MulPingReplyEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731MulPingReplySeqNumber"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731MulPingReplyOrder"),
)
if mibBuilder.loadTexts:
    hwY1731MulPingReplyEntry.setStatus("current")
_HwY1731MulPingReplySeqNumber_Type = Unsigned32
_HwY1731MulPingReplySeqNumber_Object = MibTableColumn
hwY1731MulPingReplySeqNumber = _HwY1731MulPingReplySeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 7, 1, 1),
    _HwY1731MulPingReplySeqNumber_Type()
)
hwY1731MulPingReplySeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731MulPingReplySeqNumber.setStatus("current")
_HwY1731MulPingReplyOrder_Type = Unsigned32
_HwY1731MulPingReplyOrder_Object = MibTableColumn
hwY1731MulPingReplyOrder = _HwY1731MulPingReplyOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 7, 1, 2),
    _HwY1731MulPingReplyOrder_Type()
)
hwY1731MulPingReplyOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731MulPingReplyOrder.setStatus("current")


class _HwY1731MulPingReplyMepId_Type(Integer32):
    """Custom type hwY1731MulPingReplyMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731MulPingReplyMepId_Type.__name__ = "Integer32"
_HwY1731MulPingReplyMepId_Object = MibTableColumn
hwY1731MulPingReplyMepId = _HwY1731MulPingReplyMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 7, 1, 3),
    _HwY1731MulPingReplyMepId_Type()
)
hwY1731MulPingReplyMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731MulPingReplyMepId.setStatus("current")
_HwY1731MulPingReplyMacAddress_Type = MacAddress
_HwY1731MulPingReplyMacAddress_Object = MibTableColumn
hwY1731MulPingReplyMacAddress = _HwY1731MulPingReplyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 7, 1, 4),
    _HwY1731MulPingReplyMacAddress_Type()
)
hwY1731MulPingReplyMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731MulPingReplyMacAddress.setStatus("current")
_HwY1731MulPingReplyTransTime_Type = Unsigned32
_HwY1731MulPingReplyTransTime_Object = MibTableColumn
hwY1731MulPingReplyTransTime = _HwY1731MulPingReplyTransTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 7, 1, 5),
    _HwY1731MulPingReplyTransTime_Type()
)
hwY1731MulPingReplyTransTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731MulPingReplyTransTime.setStatus("current")
_HwY1731AisVlanConfigTable_Object = MibTable
hwY1731AisVlanConfigTable = _HwY1731AisVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 8)
)
if mibBuilder.loadTexts:
    hwY1731AisVlanConfigTable.setStatus("current")
_HwY1731AisVlanConfigEntry_Object = MibTableRow
hwY1731AisVlanConfigEntry = _HwY1731AisVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 8, 1)
)
hwY1731AisVlanConfigEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731AisConfigPeVlan"),
)
if mibBuilder.loadTexts:
    hwY1731AisVlanConfigEntry.setStatus("current")
_HwY1731AisConfigPeVlan_Type = VlanIdOrNone
_HwY1731AisConfigPeVlan_Object = MibTableColumn
hwY1731AisConfigPeVlan = _HwY1731AisConfigPeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 8, 1, 1),
    _HwY1731AisConfigPeVlan_Type()
)
hwY1731AisConfigPeVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731AisConfigPeVlan.setStatus("current")


class _HwY1731AisConfigVlanListLow_Type(OctetString):
    """Custom type hwY1731AisConfigVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwY1731AisConfigVlanListLow_Type.__name__ = "OctetString"
_HwY1731AisConfigVlanListLow_Object = MibTableColumn
hwY1731AisConfigVlanListLow = _HwY1731AisConfigVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 8, 1, 2),
    _HwY1731AisConfigVlanListLow_Type()
)
hwY1731AisConfigVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisConfigVlanListLow.setStatus("current")


class _HwY1731AisConfigVlanListHigh_Type(OctetString):
    """Custom type hwY1731AisConfigVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwY1731AisConfigVlanListHigh_Type.__name__ = "OctetString"
_HwY1731AisConfigVlanListHigh_Object = MibTableColumn
hwY1731AisConfigVlanListHigh = _HwY1731AisConfigVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 8, 1, 3),
    _HwY1731AisConfigVlanListHigh_Type()
)
hwY1731AisConfigVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisConfigVlanListHigh.setStatus("current")
_HwY1731AisVlanConfigRowStatus_Type = RowStatus
_HwY1731AisVlanConfigRowStatus_Object = MibTableColumn
hwY1731AisVlanConfigRowStatus = _HwY1731AisVlanConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 8, 1, 4),
    _HwY1731AisVlanConfigRowStatus_Type()
)
hwY1731AisVlanConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731AisVlanConfigRowStatus.setStatus("current")
_HwY1731TestIdTable_Object = MibTable
hwY1731TestIdTable = _HwY1731TestIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9)
)
if mibBuilder.loadTexts:
    hwY1731TestIdTable.setStatus("current")
_HwY1731TestIdEntry_Object = MibTableRow
hwY1731TestIdEntry = _HwY1731TestIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1)
)
hwY1731TestIdEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdEntry.setStatus("current")


class _HwY1731TestIdentifier_Type(Unsigned32):
    """Custom type hwY1731TestIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwY1731TestIdentifier_Type.__name__ = "Unsigned32"
_HwY1731TestIdentifier_Object = MibTableColumn
hwY1731TestIdentifier = _HwY1731TestIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 1),
    _HwY1731TestIdentifier_Type()
)
hwY1731TestIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdentifier.setStatus("current")


class _HwY1731TestIdMdName_Type(OctetString):
    """Custom type hwY1731TestIdMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwY1731TestIdMdName_Type.__name__ = "OctetString"
_HwY1731TestIdMdName_Object = MibTableColumn
hwY1731TestIdMdName = _HwY1731TestIdMdName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 2),
    _HwY1731TestIdMdName_Type()
)
hwY1731TestIdMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdMdName.setStatus("current")


class _HwY1731TestIdMaName_Type(OctetString):
    """Custom type hwY1731TestIdMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_HwY1731TestIdMaName_Type.__name__ = "OctetString"
_HwY1731TestIdMaName_Object = MibTableColumn
hwY1731TestIdMaName = _HwY1731TestIdMaName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 3),
    _HwY1731TestIdMaName_Type()
)
hwY1731TestIdMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdMaName.setStatus("current")


class _HwY1731TestIdLocalMepId_Type(Integer32):
    """Custom type hwY1731TestIdLocalMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_HwY1731TestIdLocalMepId_Type.__name__ = "Integer32"
_HwY1731TestIdLocalMepId_Object = MibTableColumn
hwY1731TestIdLocalMepId = _HwY1731TestIdLocalMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 4),
    _HwY1731TestIdLocalMepId_Type()
)
hwY1731TestIdLocalMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdLocalMepId.setStatus("current")
_HwY1731TestIdDestIsMepId_Type = TruthValue
_HwY1731TestIdDestIsMepId_Object = MibTableColumn
hwY1731TestIdDestIsMepId = _HwY1731TestIdDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 5),
    _HwY1731TestIdDestIsMepId_Type()
)
hwY1731TestIdDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdDestIsMepId.setStatus("current")


class _HwY1731TestIdDestMepId_Type(Integer32):
    """Custom type hwY1731TestIdDestMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HwY1731TestIdDestMepId_Type.__name__ = "Integer32"
_HwY1731TestIdDestMepId_Object = MibTableColumn
hwY1731TestIdDestMepId = _HwY1731TestIdDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 6),
    _HwY1731TestIdDestMepId_Type()
)
hwY1731TestIdDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdDestMepId.setStatus("current")
_HwY1731TestIdDestMepMacAddress_Type = MacAddress
_HwY1731TestIdDestMepMacAddress_Object = MibTableColumn
hwY1731TestIdDestMepMacAddress = _HwY1731TestIdDestMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 7),
    _HwY1731TestIdDestMepMacAddress_Type()
)
hwY1731TestIdDestMepMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdDestMepMacAddress.setStatus("current")
_HwY1731TestIdOnwardMacAddress_Type = MacAddress
_HwY1731TestIdOnwardMacAddress_Object = MibTableColumn
hwY1731TestIdOnwardMacAddress = _HwY1731TestIdOnwardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 8),
    _HwY1731TestIdOnwardMacAddress_Type()
)
hwY1731TestIdOnwardMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdOnwardMacAddress.setStatus("current")
_HwY1731TestIdBackwardMacAddress_Type = MacAddress
_HwY1731TestIdBackwardMacAddress_Object = MibTableColumn
hwY1731TestIdBackwardMacAddress = _HwY1731TestIdBackwardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 9),
    _HwY1731TestIdBackwardMacAddress_Type()
)
hwY1731TestIdBackwardMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdBackwardMacAddress.setStatus("current")
_HwY1731TestIdIsUpdateOnwardMacAddress_Type = TruthValue
_HwY1731TestIdIsUpdateOnwardMacAddress_Object = MibTableColumn
hwY1731TestIdIsUpdateOnwardMacAddress = _HwY1731TestIdIsUpdateOnwardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 10),
    _HwY1731TestIdIsUpdateOnwardMacAddress_Type()
)
hwY1731TestIdIsUpdateOnwardMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdIsUpdateOnwardMacAddress.setStatus("current")
_HwY1731TestIdIsUpdateBackwardMacAddress_Type = TruthValue
_HwY1731TestIdIsUpdateBackwardMacAddress_Object = MibTableColumn
hwY1731TestIdIsUpdateBackwardMacAddress = _HwY1731TestIdIsUpdateBackwardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 11),
    _HwY1731TestIdIsUpdateBackwardMacAddress_Type()
)
hwY1731TestIdIsUpdateBackwardMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdIsUpdateBackwardMacAddress.setStatus("current")


class _HwY1731TestId8021pValue_Type(Integer32):
    """Custom type hwY1731TestId8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwY1731TestId8021pValue_Type.__name__ = "Integer32"
_HwY1731TestId8021pValue_Object = MibTableColumn
hwY1731TestId8021pValue = _HwY1731TestId8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 12),
    _HwY1731TestId8021pValue_Type()
)
hwY1731TestId8021pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestId8021pValue.setStatus("current")


class _HwY1731TestIdUplink8021p_Type(Integer32):
    """Custom type hwY1731TestIdUplink8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwY1731TestIdUplink8021p_Type.__name__ = "Integer32"
_HwY1731TestIdUplink8021p_Object = MibTableColumn
hwY1731TestIdUplink8021p = _HwY1731TestIdUplink8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 13),
    _HwY1731TestIdUplink8021p_Type()
)
hwY1731TestIdUplink8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdUplink8021p.setStatus("current")


class _HwY1731TestIdDownlink8021p_Type(Integer32):
    """Custom type hwY1731TestIdDownlink8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwY1731TestIdDownlink8021p_Type.__name__ = "Integer32"
_HwY1731TestIdDownlink8021p_Object = MibTableColumn
hwY1731TestIdDownlink8021p = _HwY1731TestIdDownlink8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 14),
    _HwY1731TestIdDownlink8021p_Type()
)
hwY1731TestIdDownlink8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdDownlink8021p.setStatus("current")


class _HwY1731TestIdDescription_Type(OctetString):
    """Custom type hwY1731TestIdDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwY1731TestIdDescription_Type.__name__ = "OctetString"
_HwY1731TestIdDescription_Object = MibTableColumn
hwY1731TestIdDescription = _HwY1731TestIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 15),
    _HwY1731TestIdDescription_Type()
)
hwY1731TestIdDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdDescription.setStatus("current")
_HwY1731TestIdIsRecordFile_Type = TruthValue
_HwY1731TestIdIsRecordFile_Object = MibTableColumn
hwY1731TestIdIsRecordFile = _HwY1731TestIdIsRecordFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 16),
    _HwY1731TestIdIsRecordFile_Type()
)
hwY1731TestIdIsRecordFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdIsRecordFile.setStatus("current")


class _HwY1731TestIdQueuePriority_Type(Integer32):
    """Custom type hwY1731TestIdQueuePriority based on Integer32"""
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 6),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 9),
          ("invalid", 1))
    )


_HwY1731TestIdQueuePriority_Type.__name__ = "Integer32"
_HwY1731TestIdQueuePriority_Object = MibTableColumn
hwY1731TestIdQueuePriority = _HwY1731TestIdQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 17),
    _HwY1731TestIdQueuePriority_Type()
)
hwY1731TestIdQueuePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdQueuePriority.setStatus("current")
_HwY1731TestIdRowStatus_Type = RowStatus
_HwY1731TestIdRowStatus_Object = MibTableColumn
hwY1731TestIdRowStatus = _HwY1731TestIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 9, 1, 99),
    _HwY1731TestIdRowStatus_Type()
)
hwY1731TestIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdRowStatus.setStatus("current")
_HwY1731TestIdSingleEndedLMSendTable_Object = MibTable
hwY1731TestIdSingleEndedLMSendTable = _HwY1731TestIdSingleEndedLMSendTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 10)
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMSendTable.setStatus("current")
_HwY1731TestIdSingleEndedLMSendEntry_Object = MibTableRow
hwY1731TestIdSingleEndedLMSendEntry = _HwY1731TestIdSingleEndedLMSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 10, 1)
)
hwY1731TestIdSingleEndedLMSendEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMSendEntry.setStatus("current")
_HwY1731TestIdSingleEndedLMSendIsContinue_Type = TruthValue
_HwY1731TestIdSingleEndedLMSendIsContinue_Object = MibTableColumn
hwY1731TestIdSingleEndedLMSendIsContinue = _HwY1731TestIdSingleEndedLMSendIsContinue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 10, 1, 1),
    _HwY1731TestIdSingleEndedLMSendIsContinue_Type()
)
hwY1731TestIdSingleEndedLMSendIsContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMSendIsContinue.setStatus("current")


class _HwY1731TestIdSingleEndedLMSendInterval_Type(Integer32):
    """Custom type hwY1731TestIdSingleEndedLMSendInterval based on Integer32"""
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
        *(("interval10s", 3),
          ("interval1s", 2),
          ("interval30s", 4),
          ("interval60s", 5),
          ("invalid", 1))
    )


_HwY1731TestIdSingleEndedLMSendInterval_Type.__name__ = "Integer32"
_HwY1731TestIdSingleEndedLMSendInterval_Object = MibTableColumn
hwY1731TestIdSingleEndedLMSendInterval = _HwY1731TestIdSingleEndedLMSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 10, 1, 2),
    _HwY1731TestIdSingleEndedLMSendInterval_Type()
)
hwY1731TestIdSingleEndedLMSendInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMSendInterval.setStatus("current")


class _HwY1731TestIdSingleEndedLMSendCount_Type(Integer32):
    """Custom type hwY1731TestIdSingleEndedLMSendCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 60),
    )


_HwY1731TestIdSingleEndedLMSendCount_Type.__name__ = "Integer32"
_HwY1731TestIdSingleEndedLMSendCount_Object = MibTableColumn
hwY1731TestIdSingleEndedLMSendCount = _HwY1731TestIdSingleEndedLMSendCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 10, 1, 3),
    _HwY1731TestIdSingleEndedLMSendCount_Type()
)
hwY1731TestIdSingleEndedLMSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMSendCount.setStatus("current")
_HwY1731TestIdSingleEndedLMSendRowStatus_Type = RowStatus
_HwY1731TestIdSingleEndedLMSendRowStatus_Object = MibTableColumn
hwY1731TestIdSingleEndedLMSendRowStatus = _HwY1731TestIdSingleEndedLMSendRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 10, 1, 99),
    _HwY1731TestIdSingleEndedLMSendRowStatus_Type()
)
hwY1731TestIdSingleEndedLMSendRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMSendRowStatus.setStatus("current")
_HwY1731TestIdSingleEndedLMReceiveTable_Object = MibTable
hwY1731TestIdSingleEndedLMReceiveTable = _HwY1731TestIdSingleEndedLMReceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 11)
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMReceiveTable.setStatus("current")
_HwY1731TestIdSingleEndedLMReceiveEntry_Object = MibTableRow
hwY1731TestIdSingleEndedLMReceiveEntry = _HwY1731TestIdSingleEndedLMReceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 11, 1)
)
hwY1731TestIdSingleEndedLMReceiveEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMReceiveEntry.setStatus("current")
_HwY1731TestIdSingleEndedLMReceiveRowStatus_Type = RowStatus
_HwY1731TestIdSingleEndedLMReceiveRowStatus_Object = MibTableColumn
hwY1731TestIdSingleEndedLMReceiveRowStatus = _HwY1731TestIdSingleEndedLMReceiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 11, 1, 99),
    _HwY1731TestIdSingleEndedLMReceiveRowStatus_Type()
)
hwY1731TestIdSingleEndedLMReceiveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMReceiveRowStatus.setStatus("current")
_HwY1731TestIdOneWayDMSendTable_Object = MibTable
hwY1731TestIdOneWayDMSendTable = _HwY1731TestIdOneWayDMSendTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 12)
)
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMSendTable.setStatus("current")
_HwY1731TestIdOneWayDMSendEntry_Object = MibTableRow
hwY1731TestIdOneWayDMSendEntry = _HwY1731TestIdOneWayDMSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 12, 1)
)
hwY1731TestIdOneWayDMSendEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMSendEntry.setStatus("current")
_HwY1731TestIdOneWayDMSendIsContinue_Type = TruthValue
_HwY1731TestIdOneWayDMSendIsContinue_Object = MibTableColumn
hwY1731TestIdOneWayDMSendIsContinue = _HwY1731TestIdOneWayDMSendIsContinue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 12, 1, 1),
    _HwY1731TestIdOneWayDMSendIsContinue_Type()
)
hwY1731TestIdOneWayDMSendIsContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMSendIsContinue.setStatus("current")


class _HwY1731TestIdOneWayDMSendInterval_Type(Integer32):
    """Custom type hwY1731TestIdOneWayDMSendInterval based on Integer32"""
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
        *(("interval10s", 3),
          ("interval1s", 2),
          ("interval30s", 4),
          ("interval60s", 5),
          ("invalid", 1))
    )


_HwY1731TestIdOneWayDMSendInterval_Type.__name__ = "Integer32"
_HwY1731TestIdOneWayDMSendInterval_Object = MibTableColumn
hwY1731TestIdOneWayDMSendInterval = _HwY1731TestIdOneWayDMSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 12, 1, 2),
    _HwY1731TestIdOneWayDMSendInterval_Type()
)
hwY1731TestIdOneWayDMSendInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMSendInterval.setStatus("current")


class _HwY1731TestIdOneWayDMSendCount_Type(Integer32):
    """Custom type hwY1731TestIdOneWayDMSendCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 60),
    )


_HwY1731TestIdOneWayDMSendCount_Type.__name__ = "Integer32"
_HwY1731TestIdOneWayDMSendCount_Object = MibTableColumn
hwY1731TestIdOneWayDMSendCount = _HwY1731TestIdOneWayDMSendCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 12, 1, 3),
    _HwY1731TestIdOneWayDMSendCount_Type()
)
hwY1731TestIdOneWayDMSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMSendCount.setStatus("current")


class _HwY1731TestIdOneWayDMSendPacketSize_Type(Integer32):
    """Custom type hwY1731TestIdOneWayDMSendPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1518),
    )


_HwY1731TestIdOneWayDMSendPacketSize_Type.__name__ = "Integer32"
_HwY1731TestIdOneWayDMSendPacketSize_Object = MibTableColumn
hwY1731TestIdOneWayDMSendPacketSize = _HwY1731TestIdOneWayDMSendPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 12, 1, 4),
    _HwY1731TestIdOneWayDMSendPacketSize_Type()
)
hwY1731TestIdOneWayDMSendPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMSendPacketSize.setStatus("current")
_HwY1731TestIdOneWayDMSendRowStatus_Type = RowStatus
_HwY1731TestIdOneWayDMSendRowStatus_Object = MibTableColumn
hwY1731TestIdOneWayDMSendRowStatus = _HwY1731TestIdOneWayDMSendRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 12, 1, 99),
    _HwY1731TestIdOneWayDMSendRowStatus_Type()
)
hwY1731TestIdOneWayDMSendRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMSendRowStatus.setStatus("current")
_HwY1731TestIdOneWayDMReceiveTable_Object = MibTable
hwY1731TestIdOneWayDMReceiveTable = _HwY1731TestIdOneWayDMReceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 13)
)
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMReceiveTable.setStatus("current")
_HwY1731TestIdOneWayDMReceiveEntry_Object = MibTableRow
hwY1731TestIdOneWayDMReceiveEntry = _HwY1731TestIdOneWayDMReceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 13, 1)
)
hwY1731TestIdOneWayDMReceiveEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMReceiveEntry.setStatus("current")
_HwY1731TestIdOneWayDMReceiveIsContinue_Type = TruthValue
_HwY1731TestIdOneWayDMReceiveIsContinue_Object = MibTableColumn
hwY1731TestIdOneWayDMReceiveIsContinue = _HwY1731TestIdOneWayDMReceiveIsContinue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 13, 1, 1),
    _HwY1731TestIdOneWayDMReceiveIsContinue_Type()
)
hwY1731TestIdOneWayDMReceiveIsContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMReceiveIsContinue.setStatus("current")
_HwY1731TestIdOneWayDMReceiveRowStatus_Type = RowStatus
_HwY1731TestIdOneWayDMReceiveRowStatus_Object = MibTableColumn
hwY1731TestIdOneWayDMReceiveRowStatus = _HwY1731TestIdOneWayDMReceiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 13, 1, 99),
    _HwY1731TestIdOneWayDMReceiveRowStatus_Type()
)
hwY1731TestIdOneWayDMReceiveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMReceiveRowStatus.setStatus("current")
_HwY1731TestIdTwoWayDMSendTable_Object = MibTable
hwY1731TestIdTwoWayDMSendTable = _HwY1731TestIdTwoWayDMSendTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 14)
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMSendTable.setStatus("current")
_HwY1731TestIdTwoWayDMSendEntry_Object = MibTableRow
hwY1731TestIdTwoWayDMSendEntry = _HwY1731TestIdTwoWayDMSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 14, 1)
)
hwY1731TestIdTwoWayDMSendEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMSendEntry.setStatus("current")
_HwY1731TestIdTwoWayDMSendIsContinue_Type = TruthValue
_HwY1731TestIdTwoWayDMSendIsContinue_Object = MibTableColumn
hwY1731TestIdTwoWayDMSendIsContinue = _HwY1731TestIdTwoWayDMSendIsContinue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 14, 1, 1),
    _HwY1731TestIdTwoWayDMSendIsContinue_Type()
)
hwY1731TestIdTwoWayDMSendIsContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMSendIsContinue.setStatus("current")


class _HwY1731TestIdTwoWayDMSendInterval_Type(Integer32):
    """Custom type hwY1731TestIdTwoWayDMSendInterval based on Integer32"""
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
        *(("interval10s", 3),
          ("interval1s", 2),
          ("interval30s", 4),
          ("interval60s", 5),
          ("invalid", 1))
    )


_HwY1731TestIdTwoWayDMSendInterval_Type.__name__ = "Integer32"
_HwY1731TestIdTwoWayDMSendInterval_Object = MibTableColumn
hwY1731TestIdTwoWayDMSendInterval = _HwY1731TestIdTwoWayDMSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 14, 1, 2),
    _HwY1731TestIdTwoWayDMSendInterval_Type()
)
hwY1731TestIdTwoWayDMSendInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMSendInterval.setStatus("current")


class _HwY1731TestIdTwoWayDMSendCount_Type(Integer32):
    """Custom type hwY1731TestIdTwoWayDMSendCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 60),
    )


_HwY1731TestIdTwoWayDMSendCount_Type.__name__ = "Integer32"
_HwY1731TestIdTwoWayDMSendCount_Object = MibTableColumn
hwY1731TestIdTwoWayDMSendCount = _HwY1731TestIdTwoWayDMSendCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 14, 1, 3),
    _HwY1731TestIdTwoWayDMSendCount_Type()
)
hwY1731TestIdTwoWayDMSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMSendCount.setStatus("current")


class _HwY1731TestIdTwoWayDMSendPacketSize_Type(Integer32):
    """Custom type hwY1731TestIdTwoWayDMSendPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1518),
    )


_HwY1731TestIdTwoWayDMSendPacketSize_Type.__name__ = "Integer32"
_HwY1731TestIdTwoWayDMSendPacketSize_Object = MibTableColumn
hwY1731TestIdTwoWayDMSendPacketSize = _HwY1731TestIdTwoWayDMSendPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 14, 1, 4),
    _HwY1731TestIdTwoWayDMSendPacketSize_Type()
)
hwY1731TestIdTwoWayDMSendPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMSendPacketSize.setStatus("current")
_HwY1731TestIdTwoWayDMSendRowStatus_Type = RowStatus
_HwY1731TestIdTwoWayDMSendRowStatus_Object = MibTableColumn
hwY1731TestIdTwoWayDMSendRowStatus = _HwY1731TestIdTwoWayDMSendRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 14, 1, 99),
    _HwY1731TestIdTwoWayDMSendRowStatus_Type()
)
hwY1731TestIdTwoWayDMSendRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMSendRowStatus.setStatus("current")
_HwY1731TestIdTwoWayDMReceiveTable_Object = MibTable
hwY1731TestIdTwoWayDMReceiveTable = _HwY1731TestIdTwoWayDMReceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 15)
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMReceiveTable.setStatus("current")
_HwY1731TestIdTwoWayDMReceiveEntry_Object = MibTableRow
hwY1731TestIdTwoWayDMReceiveEntry = _HwY1731TestIdTwoWayDMReceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 15, 1)
)
hwY1731TestIdTwoWayDMReceiveEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMReceiveEntry.setStatus("current")
_HwY1731TestIdTwoWayDMReceiveRowStatus_Type = RowStatus
_HwY1731TestIdTwoWayDMReceiveRowStatus_Object = MibTableColumn
hwY1731TestIdTwoWayDMReceiveRowStatus = _HwY1731TestIdTwoWayDMReceiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 15, 1, 99),
    _HwY1731TestIdTwoWayDMReceiveRowStatus_Type()
)
hwY1731TestIdTwoWayDMReceiveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMReceiveRowStatus.setStatus("current")
_HwY1731TestIdSingleSynEndedLMSendTable_Object = MibTable
hwY1731TestIdSingleSynEndedLMSendTable = _HwY1731TestIdSingleSynEndedLMSendTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 16)
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMSendTable.setStatus("current")
_HwY1731TestIdSingleSynEndedLMSendEntry_Object = MibTableRow
hwY1731TestIdSingleSynEndedLMSendEntry = _HwY1731TestIdSingleSynEndedLMSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 16, 1)
)
hwY1731TestIdSingleSynEndedLMSendEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMSendEntry.setStatus("current")
_HwY1731TestIdSingleSynEndedLMSendIsContinue_Type = TruthValue
_HwY1731TestIdSingleSynEndedLMSendIsContinue_Object = MibTableColumn
hwY1731TestIdSingleSynEndedLMSendIsContinue = _HwY1731TestIdSingleSynEndedLMSendIsContinue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 16, 1, 1),
    _HwY1731TestIdSingleSynEndedLMSendIsContinue_Type()
)
hwY1731TestIdSingleSynEndedLMSendIsContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMSendIsContinue.setStatus("current")


class _HwY1731TestIdSingleSynEndedLMSendInterval_Type(Integer32):
    """Custom type hwY1731TestIdSingleSynEndedLMSendInterval based on Integer32"""
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
        *(("interval100ms", 6),
          ("interval10ms", 5),
          ("interval10s", 3),
          ("interval1s", 2),
          ("interval3Dot3ms", 4),
          ("invalid", 1))
    )


_HwY1731TestIdSingleSynEndedLMSendInterval_Type.__name__ = "Integer32"
_HwY1731TestIdSingleSynEndedLMSendInterval_Object = MibTableColumn
hwY1731TestIdSingleSynEndedLMSendInterval = _HwY1731TestIdSingleSynEndedLMSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 16, 1, 2),
    _HwY1731TestIdSingleSynEndedLMSendInterval_Type()
)
hwY1731TestIdSingleSynEndedLMSendInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMSendInterval.setStatus("current")


class _HwY1731TestIdSingleSynEndedLMSendCount_Type(Integer32):
    """Custom type hwY1731TestIdSingleSynEndedLMSendCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_HwY1731TestIdSingleSynEndedLMSendCount_Type.__name__ = "Integer32"
_HwY1731TestIdSingleSynEndedLMSendCount_Object = MibTableColumn
hwY1731TestIdSingleSynEndedLMSendCount = _HwY1731TestIdSingleSynEndedLMSendCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 16, 1, 3),
    _HwY1731TestIdSingleSynEndedLMSendCount_Type()
)
hwY1731TestIdSingleSynEndedLMSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMSendCount.setStatus("current")


class _HwY1731TestIdSingleSynEndedLMSendTimeOut_Type(Integer32):
    """Custom type hwY1731TestIdSingleSynEndedLMSendTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_HwY1731TestIdSingleSynEndedLMSendTimeOut_Type.__name__ = "Integer32"
_HwY1731TestIdSingleSynEndedLMSendTimeOut_Object = MibTableColumn
hwY1731TestIdSingleSynEndedLMSendTimeOut = _HwY1731TestIdSingleSynEndedLMSendTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 16, 1, 4),
    _HwY1731TestIdSingleSynEndedLMSendTimeOut_Type()
)
hwY1731TestIdSingleSynEndedLMSendTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMSendTimeOut.setStatus("current")
_HwY1731TestIdSingleSynEndedLMSendRowStatus_Type = RowStatus
_HwY1731TestIdSingleSynEndedLMSendRowStatus_Object = MibTableColumn
hwY1731TestIdSingleSynEndedLMSendRowStatus = _HwY1731TestIdSingleSynEndedLMSendRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 16, 1, 5),
    _HwY1731TestIdSingleSynEndedLMSendRowStatus_Type()
)
hwY1731TestIdSingleSynEndedLMSendRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMSendRowStatus.setStatus("current")
_HwY1731TestIdSingleSynEndedLMReceiveTable_Object = MibTable
hwY1731TestIdSingleSynEndedLMReceiveTable = _HwY1731TestIdSingleSynEndedLMReceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 17)
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMReceiveTable.setStatus("current")
_HwY1731TestIdSingleSynEndedLMReceiveEntry_Object = MibTableRow
hwY1731TestIdSingleSynEndedLMReceiveEntry = _HwY1731TestIdSingleSynEndedLMReceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 17, 1)
)
hwY1731TestIdSingleSynEndedLMReceiveEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMReceiveEntry.setStatus("current")


class _HwY1731TestIdSingleSynEndedLMReceiveTimeOut_Type(Integer32):
    """Custom type hwY1731TestIdSingleSynEndedLMReceiveTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 300),
    )


_HwY1731TestIdSingleSynEndedLMReceiveTimeOut_Type.__name__ = "Integer32"
_HwY1731TestIdSingleSynEndedLMReceiveTimeOut_Object = MibTableColumn
hwY1731TestIdSingleSynEndedLMReceiveTimeOut = _HwY1731TestIdSingleSynEndedLMReceiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 17, 1, 1),
    _HwY1731TestIdSingleSynEndedLMReceiveTimeOut_Type()
)
hwY1731TestIdSingleSynEndedLMReceiveTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMReceiveTimeOut.setStatus("current")
_HwY1731TestIdSingleSynEndedLMReceiveRowStatus_Type = RowStatus
_HwY1731TestIdSingleSynEndedLMReceiveRowStatus_Object = MibTableColumn
hwY1731TestIdSingleSynEndedLMReceiveRowStatus = _HwY1731TestIdSingleSynEndedLMReceiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 1, 17, 1, 2),
    _HwY1731TestIdSingleSynEndedLMReceiveRowStatus_Type()
)
hwY1731TestIdSingleSynEndedLMReceiveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMReceiveRowStatus.setStatus("current")
_HwY1731StatisticObject_ObjectIdentity = ObjectIdentity
hwY1731StatisticObject = _HwY1731StatisticObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2)
)
_HwY1731ResetStatisticTable_Object = MibTable
hwY1731ResetStatisticTable = _HwY1731ResetStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    hwY1731ResetStatisticTable.setStatus("current")
_HwY1731ResetStatisticEntry_Object = MibTableRow
hwY1731ResetStatisticEntry = _HwY1731ResetStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 1, 1)
)
hwY1731ResetStatisticEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731RemoteIp"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731VcId"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731MacAddress"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731ResvIndex"),
)
if mibBuilder.loadTexts:
    hwY1731ResetStatisticEntry.setStatus("current")


class _HwY1731ResetStatisticType_Type(Integer32):
    """Custom type hwY1731ResetStatisticType based on Integer32"""
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
        *(("dualloss", 3),
          ("invalid", 1),
          ("onewaydelay", 4),
          ("singleloss", 2),
          ("twowaydelay", 5))
    )


_HwY1731ResetStatisticType_Type.__name__ = "Integer32"
_HwY1731ResetStatisticType_Object = MibTableColumn
hwY1731ResetStatisticType = _HwY1731ResetStatisticType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 1, 1, 1),
    _HwY1731ResetStatisticType_Type()
)
hwY1731ResetStatisticType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwY1731ResetStatisticType.setStatus("current")


class _HwY1731ResetStatistic8021pValue_Type(Integer32):
    """Custom type hwY1731ResetStatistic8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_HwY1731ResetStatistic8021pValue_Type.__name__ = "Integer32"
_HwY1731ResetStatistic8021pValue_Object = MibTableColumn
hwY1731ResetStatistic8021pValue = _HwY1731ResetStatistic8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 1, 1, 2),
    _HwY1731ResetStatistic8021pValue_Type()
)
hwY1731ResetStatistic8021pValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwY1731ResetStatistic8021pValue.setStatus("current")
_HwY1731StatisticTable_Object = MibTable
hwY1731StatisticTable = _HwY1731StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    hwY1731StatisticTable.setStatus("current")
_HwY1731StatisticEntry_Object = MibTableRow
hwY1731StatisticEntry = _HwY1731StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1)
)
hwY1731StatisticEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731RemoteIp"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731VcId"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731MacAddress"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731ResvIndex"),
)
if mibBuilder.loadTexts:
    hwY1731StatisticEntry.setStatus("current")


class _HwY1731SingleLossStatisticGatherInterval_Type(Integer32):
    """Custom type hwY1731SingleLossStatisticGatherInterval based on Integer32"""
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
        *(("interval10000ms", 3),
          ("interval1000ms", 2),
          ("interval30000ms", 4),
          ("invalid", 1))
    )


_HwY1731SingleLossStatisticGatherInterval_Type.__name__ = "Integer32"
_HwY1731SingleLossStatisticGatherInterval_Object = MibTableColumn
hwY1731SingleLossStatisticGatherInterval = _HwY1731SingleLossStatisticGatherInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 1),
    _HwY1731SingleLossStatisticGatherInterval_Type()
)
hwY1731SingleLossStatisticGatherInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossStatisticGatherInterval.setStatus("current")


class _HwY1731SingleLossLocalStatistic_Type(OctetString):
    """Custom type hwY1731SingleLossLocalStatistic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwY1731SingleLossLocalStatistic_Type.__name__ = "OctetString"
_HwY1731SingleLossLocalStatistic_Object = MibTableColumn
hwY1731SingleLossLocalStatistic = _HwY1731SingleLossLocalStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 2),
    _HwY1731SingleLossLocalStatistic_Type()
)
hwY1731SingleLossLocalStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossLocalStatistic.setStatus("current")


class _HwY1731SingleLossLocalRatio_Type(OctetString):
    """Custom type hwY1731SingleLossLocalRatio based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwY1731SingleLossLocalRatio_Type.__name__ = "OctetString"
_HwY1731SingleLossLocalRatio_Object = MibTableColumn
hwY1731SingleLossLocalRatio = _HwY1731SingleLossLocalRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 3),
    _HwY1731SingleLossLocalRatio_Type()
)
hwY1731SingleLossLocalRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossLocalRatio.setStatus("current")
_HwY1731SingleLossLocalRatioMax_Type = Integer32
_HwY1731SingleLossLocalRatioMax_Object = MibTableColumn
hwY1731SingleLossLocalRatioMax = _HwY1731SingleLossLocalRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 4),
    _HwY1731SingleLossLocalRatioMax_Type()
)
hwY1731SingleLossLocalRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossLocalRatioMax.setStatus("current")
_HwY1731SingleLossLocalRatioMin_Type = Integer32
_HwY1731SingleLossLocalRatioMin_Object = MibTableColumn
hwY1731SingleLossLocalRatioMin = _HwY1731SingleLossLocalRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 5),
    _HwY1731SingleLossLocalRatioMin_Type()
)
hwY1731SingleLossLocalRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossLocalRatioMin.setStatus("current")
_HwY1731SingleLossLocalRatioAvg_Type = Integer32
_HwY1731SingleLossLocalRatioAvg_Object = MibTableColumn
hwY1731SingleLossLocalRatioAvg = _HwY1731SingleLossLocalRatioAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 6),
    _HwY1731SingleLossLocalRatioAvg_Type()
)
hwY1731SingleLossLocalRatioAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossLocalRatioAvg.setStatus("current")


class _HwY1731SingleLossRemoteStatistic_Type(OctetString):
    """Custom type hwY1731SingleLossRemoteStatistic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwY1731SingleLossRemoteStatistic_Type.__name__ = "OctetString"
_HwY1731SingleLossRemoteStatistic_Object = MibTableColumn
hwY1731SingleLossRemoteStatistic = _HwY1731SingleLossRemoteStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 7),
    _HwY1731SingleLossRemoteStatistic_Type()
)
hwY1731SingleLossRemoteStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossRemoteStatistic.setStatus("current")


class _HwY1731SingleLossRemoteRatio_Type(OctetString):
    """Custom type hwY1731SingleLossRemoteRatio based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwY1731SingleLossRemoteRatio_Type.__name__ = "OctetString"
_HwY1731SingleLossRemoteRatio_Object = MibTableColumn
hwY1731SingleLossRemoteRatio = _HwY1731SingleLossRemoteRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 8),
    _HwY1731SingleLossRemoteRatio_Type()
)
hwY1731SingleLossRemoteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossRemoteRatio.setStatus("current")
_HwY1731SingleLossRemoteRatioMax_Type = Integer32
_HwY1731SingleLossRemoteRatioMax_Object = MibTableColumn
hwY1731SingleLossRemoteRatioMax = _HwY1731SingleLossRemoteRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 9),
    _HwY1731SingleLossRemoteRatioMax_Type()
)
hwY1731SingleLossRemoteRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossRemoteRatioMax.setStatus("current")
_HwY1731SingleLossRemoteRatioMin_Type = Integer32
_HwY1731SingleLossRemoteRatioMin_Object = MibTableColumn
hwY1731SingleLossRemoteRatioMin = _HwY1731SingleLossRemoteRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 10),
    _HwY1731SingleLossRemoteRatioMin_Type()
)
hwY1731SingleLossRemoteRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossRemoteRatioMin.setStatus("current")
_HwY1731SingleLossRemoteRatioAvg_Type = Integer32
_HwY1731SingleLossRemoteRatioAvg_Object = MibTableColumn
hwY1731SingleLossRemoteRatioAvg = _HwY1731SingleLossRemoteRatioAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 11),
    _HwY1731SingleLossRemoteRatioAvg_Type()
)
hwY1731SingleLossRemoteRatioAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossRemoteRatioAvg.setStatus("current")


class _HwY1731OneDelayStatistic_Type(OctetString):
    """Custom type hwY1731OneDelayStatistic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwY1731OneDelayStatistic_Type.__name__ = "OctetString"
_HwY1731OneDelayStatistic_Object = MibTableColumn
hwY1731OneDelayStatistic = _HwY1731OneDelayStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 12),
    _HwY1731OneDelayStatistic_Type()
)
hwY1731OneDelayStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731OneDelayStatistic.setStatus("current")


class _HwY1731OneDelayVariation_Type(OctetString):
    """Custom type hwY1731OneDelayVariation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwY1731OneDelayVariation_Type.__name__ = "OctetString"
_HwY1731OneDelayVariation_Object = MibTableColumn
hwY1731OneDelayVariation = _HwY1731OneDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 13),
    _HwY1731OneDelayVariation_Type()
)
hwY1731OneDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731OneDelayVariation.setStatus("current")
_HwY1731OneDelayMax_Type = Unsigned32
_HwY1731OneDelayMax_Object = MibTableColumn
hwY1731OneDelayMax = _HwY1731OneDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 14),
    _HwY1731OneDelayMax_Type()
)
hwY1731OneDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731OneDelayMax.setStatus("current")
_HwY1731OneDelayMin_Type = Unsigned32
_HwY1731OneDelayMin_Object = MibTableColumn
hwY1731OneDelayMin = _HwY1731OneDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 15),
    _HwY1731OneDelayMin_Type()
)
hwY1731OneDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731OneDelayMin.setStatus("current")
_HwY1731OneDelayAvg_Type = Unsigned32
_HwY1731OneDelayAvg_Object = MibTableColumn
hwY1731OneDelayAvg = _HwY1731OneDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 16),
    _HwY1731OneDelayAvg_Type()
)
hwY1731OneDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731OneDelayAvg.setStatus("current")


class _HwY1731TwoDelayStatistic_Type(OctetString):
    """Custom type hwY1731TwoDelayStatistic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwY1731TwoDelayStatistic_Type.__name__ = "OctetString"
_HwY1731TwoDelayStatistic_Object = MibTableColumn
hwY1731TwoDelayStatistic = _HwY1731TwoDelayStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 17),
    _HwY1731TwoDelayStatistic_Type()
)
hwY1731TwoDelayStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayStatistic.setStatus("current")


class _HwY1731TwoDelayVariation_Type(OctetString):
    """Custom type hwY1731TwoDelayVariation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwY1731TwoDelayVariation_Type.__name__ = "OctetString"
_HwY1731TwoDelayVariation_Object = MibTableColumn
hwY1731TwoDelayVariation = _HwY1731TwoDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 18),
    _HwY1731TwoDelayVariation_Type()
)
hwY1731TwoDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayVariation.setStatus("current")
_HwY1731TwoDelayMax_Type = Unsigned32
_HwY1731TwoDelayMax_Object = MibTableColumn
hwY1731TwoDelayMax = _HwY1731TwoDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 19),
    _HwY1731TwoDelayMax_Type()
)
hwY1731TwoDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayMax.setStatus("current")
_HwY1731TwoDelayMin_Type = Unsigned32
_HwY1731TwoDelayMin_Object = MibTableColumn
hwY1731TwoDelayMin = _HwY1731TwoDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 20),
    _HwY1731TwoDelayMin_Type()
)
hwY1731TwoDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayMin.setStatus("current")
_HwY1731TwoDelayAvg_Type = Unsigned32
_HwY1731TwoDelayAvg_Object = MibTableColumn
hwY1731TwoDelayAvg = _HwY1731TwoDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 21),
    _HwY1731TwoDelayAvg_Type()
)
hwY1731TwoDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayAvg.setStatus("current")
_HwY1731SingleLossLocalMax_Type = Unsigned32
_HwY1731SingleLossLocalMax_Object = MibTableColumn
hwY1731SingleLossLocalMax = _HwY1731SingleLossLocalMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 22),
    _HwY1731SingleLossLocalMax_Type()
)
hwY1731SingleLossLocalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossLocalMax.setStatus("current")
_HwY1731SingleLossLocalMin_Type = Unsigned32
_HwY1731SingleLossLocalMin_Object = MibTableColumn
hwY1731SingleLossLocalMin = _HwY1731SingleLossLocalMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 23),
    _HwY1731SingleLossLocalMin_Type()
)
hwY1731SingleLossLocalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossLocalMin.setStatus("current")
_HwY1731SingleLossLocalAvg_Type = Unsigned32
_HwY1731SingleLossLocalAvg_Object = MibTableColumn
hwY1731SingleLossLocalAvg = _HwY1731SingleLossLocalAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 24),
    _HwY1731SingleLossLocalAvg_Type()
)
hwY1731SingleLossLocalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossLocalAvg.setStatus("current")
_HwY1731SingleLossRemoteMax_Type = Unsigned32
_HwY1731SingleLossRemoteMax_Object = MibTableColumn
hwY1731SingleLossRemoteMax = _HwY1731SingleLossRemoteMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 25),
    _HwY1731SingleLossRemoteMax_Type()
)
hwY1731SingleLossRemoteMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossRemoteMax.setStatus("current")
_HwY1731SingleLossRemoteMin_Type = Unsigned32
_HwY1731SingleLossRemoteMin_Object = MibTableColumn
hwY1731SingleLossRemoteMin = _HwY1731SingleLossRemoteMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 26),
    _HwY1731SingleLossRemoteMin_Type()
)
hwY1731SingleLossRemoteMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossRemoteMin.setStatus("current")
_HwY1731SingleLossRemoteAvg_Type = Unsigned32
_HwY1731SingleLossRemoteAvg_Object = MibTableColumn
hwY1731SingleLossRemoteAvg = _HwY1731SingleLossRemoteAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 27),
    _HwY1731SingleLossRemoteAvg_Type()
)
hwY1731SingleLossRemoteAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossRemoteAvg.setStatus("current")
_HwY1731OneDelayStatisticMax_Type = Integer32
_HwY1731OneDelayStatisticMax_Object = MibTableColumn
hwY1731OneDelayStatisticMax = _HwY1731OneDelayStatisticMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 28),
    _HwY1731OneDelayStatisticMax_Type()
)
hwY1731OneDelayStatisticMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731OneDelayStatisticMax.setStatus("current")
_HwY1731OneDelayStatisticMin_Type = Integer32
_HwY1731OneDelayStatisticMin_Object = MibTableColumn
hwY1731OneDelayStatisticMin = _HwY1731OneDelayStatisticMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 29),
    _HwY1731OneDelayStatisticMin_Type()
)
hwY1731OneDelayStatisticMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731OneDelayStatisticMin.setStatus("current")
_HwY1731OneDelayStatisticAvg_Type = Integer32
_HwY1731OneDelayStatisticAvg_Object = MibTableColumn
hwY1731OneDelayStatisticAvg = _HwY1731OneDelayStatisticAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 30),
    _HwY1731OneDelayStatisticAvg_Type()
)
hwY1731OneDelayStatisticAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731OneDelayStatisticAvg.setStatus("current")
_HwY1731TwoDelayStatisticMax_Type = Unsigned32
_HwY1731TwoDelayStatisticMax_Object = MibTableColumn
hwY1731TwoDelayStatisticMax = _HwY1731TwoDelayStatisticMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 31),
    _HwY1731TwoDelayStatisticMax_Type()
)
hwY1731TwoDelayStatisticMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayStatisticMax.setStatus("current")
_HwY1731TwoDelayStatisticMin_Type = Unsigned32
_HwY1731TwoDelayStatisticMin_Object = MibTableColumn
hwY1731TwoDelayStatisticMin = _HwY1731TwoDelayStatisticMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 32),
    _HwY1731TwoDelayStatisticMin_Type()
)
hwY1731TwoDelayStatisticMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayStatisticMin.setStatus("current")
_HwY1731TwoDelayStatisticAvg_Type = Unsigned32
_HwY1731TwoDelayStatisticAvg_Object = MibTableColumn
hwY1731TwoDelayStatisticAvg = _HwY1731TwoDelayStatisticAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 33),
    _HwY1731TwoDelayStatisticAvg_Type()
)
hwY1731TwoDelayStatisticAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayStatisticAvg.setStatus("current")
_HwY1731TwoDelayUnresponsivePacketCount_Type = Unsigned32
_HwY1731TwoDelayUnresponsivePacketCount_Object = MibTableColumn
hwY1731TwoDelayUnresponsivePacketCount = _HwY1731TwoDelayUnresponsivePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 34),
    _HwY1731TwoDelayUnresponsivePacketCount_Type()
)
hwY1731TwoDelayUnresponsivePacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayUnresponsivePacketCount.setStatus("current")


class _HwY1731SingleLossStatistic8021pValue_Type(Integer32):
    """Custom type hwY1731SingleLossStatistic8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwY1731SingleLossStatistic8021pValue_Type.__name__ = "Integer32"
_HwY1731SingleLossStatistic8021pValue_Object = MibTableColumn
hwY1731SingleLossStatistic8021pValue = _HwY1731SingleLossStatistic8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 35),
    _HwY1731SingleLossStatistic8021pValue_Type()
)
hwY1731SingleLossStatistic8021pValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossStatistic8021pValue.setStatus("current")


class _HwY1731OneDelayStatistic8021pValue_Type(Integer32):
    """Custom type hwY1731OneDelayStatistic8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwY1731OneDelayStatistic8021pValue_Type.__name__ = "Integer32"
_HwY1731OneDelayStatistic8021pValue_Object = MibTableColumn
hwY1731OneDelayStatistic8021pValue = _HwY1731OneDelayStatistic8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 36),
    _HwY1731OneDelayStatistic8021pValue_Type()
)
hwY1731OneDelayStatistic8021pValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731OneDelayStatistic8021pValue.setStatus("current")


class _HwY1731TwoDelayStatistic8021pValue_Type(Integer32):
    """Custom type hwY1731TwoDelayStatistic8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwY1731TwoDelayStatistic8021pValue_Type.__name__ = "Integer32"
_HwY1731TwoDelayStatistic8021pValue_Object = MibTableColumn
hwY1731TwoDelayStatistic8021pValue = _HwY1731TwoDelayStatistic8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 37),
    _HwY1731TwoDelayStatistic8021pValue_Type()
)
hwY1731TwoDelayStatistic8021pValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayStatistic8021pValue.setStatus("current")
_HwY1731OneDelayOnDemandStartTime_Type = DateAndTime
_HwY1731OneDelayOnDemandStartTime_Object = MibTableColumn
hwY1731OneDelayOnDemandStartTime = _HwY1731OneDelayOnDemandStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 38),
    _HwY1731OneDelayOnDemandStartTime_Type()
)
hwY1731OneDelayOnDemandStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731OneDelayOnDemandStartTime.setStatus("current")
_HwY1731TwoDelayOnDemandStartTime_Type = DateAndTime
_HwY1731TwoDelayOnDemandStartTime_Object = MibTableColumn
hwY1731TwoDelayOnDemandStartTime = _HwY1731TwoDelayOnDemandStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 39),
    _HwY1731TwoDelayOnDemandStartTime_Type()
)
hwY1731TwoDelayOnDemandStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TwoDelayOnDemandStartTime.setStatus("current")
_HwY1731SingleLossOnDemandStartTime_Type = DateAndTime
_HwY1731SingleLossOnDemandStartTime_Object = MibTableColumn
hwY1731SingleLossOnDemandStartTime = _HwY1731SingleLossOnDemandStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 2, 1, 40),
    _HwY1731SingleLossOnDemandStartTime_Type()
)
hwY1731SingleLossOnDemandStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossOnDemandStartTime.setStatus("current")
_HwCfmVlanOneDelayTrapLogTable_Object = MibTable
hwCfmVlanOneDelayTrapLogTable = _HwCfmVlanOneDelayTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 3)
)
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayTrapLogTable.setStatus("current")
_HwCfmVlanOneDelayTrapLogEntry_Object = MibTableRow
hwCfmVlanOneDelayTrapLogEntry = _HwCfmVlanOneDelayTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 3, 1)
)
hwCfmVlanOneDelayTrapLogEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayTrapLogEntry.setStatus("current")
_HwCfmOneDelayTrapLogMacAddress_Type = MacAddress
_HwCfmOneDelayTrapLogMacAddress_Object = MibTableColumn
hwCfmOneDelayTrapLogMacAddress = _HwCfmOneDelayTrapLogMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 3, 1, 1),
    _HwCfmOneDelayTrapLogMacAddress_Type()
)
hwCfmOneDelayTrapLogMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmOneDelayTrapLogMacAddress.setStatus("current")
_HwCfmVlanOneDelayTrapLogTimestamp_Type = TimeStamp
_HwCfmVlanOneDelayTrapLogTimestamp_Object = MibTableColumn
hwCfmVlanOneDelayTrapLogTimestamp = _HwCfmVlanOneDelayTrapLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 3, 1, 2),
    _HwCfmVlanOneDelayTrapLogTimestamp_Type()
)
hwCfmVlanOneDelayTrapLogTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayTrapLogTimestamp.setStatus("current")
_HwCfmVlanOneDelayTrapLogDelayValue_Type = Unsigned32
_HwCfmVlanOneDelayTrapLogDelayValue_Object = MibTableColumn
hwCfmVlanOneDelayTrapLogDelayValue = _HwCfmVlanOneDelayTrapLogDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 3, 1, 3),
    _HwCfmVlanOneDelayTrapLogDelayValue_Type()
)
hwCfmVlanOneDelayTrapLogDelayValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayTrapLogDelayValue.setStatus("current")
_HwCfmVlanOneDelayTrapLogThreshold_Type = Unsigned32
_HwCfmVlanOneDelayTrapLogThreshold_Object = MibTableColumn
hwCfmVlanOneDelayTrapLogThreshold = _HwCfmVlanOneDelayTrapLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 3, 1, 4),
    _HwCfmVlanOneDelayTrapLogThreshold_Type()
)
hwCfmVlanOneDelayTrapLogThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayTrapLogThreshold.setStatus("current")
_HwCfmVlanOneDelayTrapLogDelayValueHigh_Type = Unsigned32
_HwCfmVlanOneDelayTrapLogDelayValueHigh_Object = MibTableColumn
hwCfmVlanOneDelayTrapLogDelayValueHigh = _HwCfmVlanOneDelayTrapLogDelayValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 3, 1, 5),
    _HwCfmVlanOneDelayTrapLogDelayValueHigh_Type()
)
hwCfmVlanOneDelayTrapLogDelayValueHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayTrapLogDelayValueHigh.setStatus("current")
_HwCfmVlanOneDelayTrapLogDelayValueLow_Type = Unsigned32
_HwCfmVlanOneDelayTrapLogDelayValueLow_Object = MibTableColumn
hwCfmVlanOneDelayTrapLogDelayValueLow = _HwCfmVlanOneDelayTrapLogDelayValueLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 3, 1, 6),
    _HwCfmVlanOneDelayTrapLogDelayValueLow_Type()
)
hwCfmVlanOneDelayTrapLogDelayValueLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayTrapLogDelayValueLow.setStatus("current")
_HwCfmVlanOneDelayRcoverTrapLogTable_Object = MibTable
hwCfmVlanOneDelayRcoverTrapLogTable = _HwCfmVlanOneDelayRcoverTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 4)
)
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayRcoverTrapLogTable.setStatus("current")
_HwCfmVlanOneDelayRcoverTrapLogEntry_Object = MibTableRow
hwCfmVlanOneDelayRcoverTrapLogEntry = _HwCfmVlanOneDelayRcoverTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 4, 1)
)
hwCfmVlanOneDelayRcoverTrapLogEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayRcoverTrapLogEntry.setStatus("current")
_HwCfmOneDelayRecoveryTrapMacAddress_Type = MacAddress
_HwCfmOneDelayRecoveryTrapMacAddress_Object = MibTableColumn
hwCfmOneDelayRecoveryTrapMacAddress = _HwCfmOneDelayRecoveryTrapMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 4, 1, 1),
    _HwCfmOneDelayRecoveryTrapMacAddress_Type()
)
hwCfmOneDelayRecoveryTrapMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmOneDelayRecoveryTrapMacAddress.setStatus("current")
_HwCfmVlanOneDelayRecoveryTrapLogTimestamp_Type = TimeStamp
_HwCfmVlanOneDelayRecoveryTrapLogTimestamp_Object = MibTableColumn
hwCfmVlanOneDelayRecoveryTrapLogTimestamp = _HwCfmVlanOneDelayRecoveryTrapLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 4, 1, 2),
    _HwCfmVlanOneDelayRecoveryTrapLogTimestamp_Type()
)
hwCfmVlanOneDelayRecoveryTrapLogTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayRecoveryTrapLogTimestamp.setStatus("current")
_HwCfmVlanOneDelayRecoveryTrapLogDelayValue_Type = Unsigned32
_HwCfmVlanOneDelayRecoveryTrapLogDelayValue_Object = MibTableColumn
hwCfmVlanOneDelayRecoveryTrapLogDelayValue = _HwCfmVlanOneDelayRecoveryTrapLogDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 4, 1, 3),
    _HwCfmVlanOneDelayRecoveryTrapLogDelayValue_Type()
)
hwCfmVlanOneDelayRecoveryTrapLogDelayValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayRecoveryTrapLogDelayValue.setStatus("current")
_HwCfmVlanOneDelayRecoveryTrapLogThreshold_Type = Unsigned32
_HwCfmVlanOneDelayRecoveryTrapLogThreshold_Object = MibTableColumn
hwCfmVlanOneDelayRecoveryTrapLogThreshold = _HwCfmVlanOneDelayRecoveryTrapLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 4, 1, 4),
    _HwCfmVlanOneDelayRecoveryTrapLogThreshold_Type()
)
hwCfmVlanOneDelayRecoveryTrapLogThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayRecoveryTrapLogThreshold.setStatus("current")
_HwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh_Type = Unsigned32
_HwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh_Object = MibTableColumn
hwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh = _HwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 4, 1, 5),
    _HwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh_Type()
)
hwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh.setStatus("current")
_HwCfmVlanOneDelayRecoveryTrapLogDelayValueLow_Type = Unsigned32
_HwCfmVlanOneDelayRecoveryTrapLogDelayValueLow_Object = MibTableColumn
hwCfmVlanOneDelayRecoveryTrapLogDelayValueLow = _HwCfmVlanOneDelayRecoveryTrapLogDelayValueLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 4, 1, 6),
    _HwCfmVlanOneDelayRecoveryTrapLogDelayValueLow_Type()
)
hwCfmVlanOneDelayRecoveryTrapLogDelayValueLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanOneDelayRecoveryTrapLogDelayValueLow.setStatus("current")
_HwCfmVlanTwoDelayTrapLogTable_Object = MibTable
hwCfmVlanTwoDelayTrapLogTable = _HwCfmVlanTwoDelayTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 5)
)
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayTrapLogTable.setStatus("current")
_HwCfmVlanTwoDelayTrapLogEntry_Object = MibTableRow
hwCfmVlanTwoDelayTrapLogEntry = _HwCfmVlanTwoDelayTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 5, 1)
)
hwCfmVlanTwoDelayTrapLogEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayTrapLogEntry.setStatus("current")
_HwCfmTwoDelayTrapMacAddress_Type = MacAddress
_HwCfmTwoDelayTrapMacAddress_Object = MibTableColumn
hwCfmTwoDelayTrapMacAddress = _HwCfmTwoDelayTrapMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 5, 1, 1),
    _HwCfmTwoDelayTrapMacAddress_Type()
)
hwCfmTwoDelayTrapMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmTwoDelayTrapMacAddress.setStatus("current")
_HwCfmVlanTwoDelayTrapLogTimestamp_Type = TimeStamp
_HwCfmVlanTwoDelayTrapLogTimestamp_Object = MibTableColumn
hwCfmVlanTwoDelayTrapLogTimestamp = _HwCfmVlanTwoDelayTrapLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 5, 1, 2),
    _HwCfmVlanTwoDelayTrapLogTimestamp_Type()
)
hwCfmVlanTwoDelayTrapLogTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayTrapLogTimestamp.setStatus("current")
_HwCfmVlanTwoDelayTrapLogDelayValue_Type = Unsigned32
_HwCfmVlanTwoDelayTrapLogDelayValue_Object = MibTableColumn
hwCfmVlanTwoDelayTrapLogDelayValue = _HwCfmVlanTwoDelayTrapLogDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 5, 1, 3),
    _HwCfmVlanTwoDelayTrapLogDelayValue_Type()
)
hwCfmVlanTwoDelayTrapLogDelayValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayTrapLogDelayValue.setStatus("current")
_HwCfmVlanTwoDelayTrapLogThreshold_Type = Unsigned32
_HwCfmVlanTwoDelayTrapLogThreshold_Object = MibTableColumn
hwCfmVlanTwoDelayTrapLogThreshold = _HwCfmVlanTwoDelayTrapLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 5, 1, 4),
    _HwCfmVlanTwoDelayTrapLogThreshold_Type()
)
hwCfmVlanTwoDelayTrapLogThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayTrapLogThreshold.setStatus("current")
_HwCfmVlanTwoDelayTrapLogDelayValueHigh_Type = Unsigned32
_HwCfmVlanTwoDelayTrapLogDelayValueHigh_Object = MibTableColumn
hwCfmVlanTwoDelayTrapLogDelayValueHigh = _HwCfmVlanTwoDelayTrapLogDelayValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 5, 1, 5),
    _HwCfmVlanTwoDelayTrapLogDelayValueHigh_Type()
)
hwCfmVlanTwoDelayTrapLogDelayValueHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayTrapLogDelayValueHigh.setStatus("current")
_HwCfmVlanTwoDelayTrapLogDelayValueLow_Type = Unsigned32
_HwCfmVlanTwoDelayTrapLogDelayValueLow_Object = MibTableColumn
hwCfmVlanTwoDelayTrapLogDelayValueLow = _HwCfmVlanTwoDelayTrapLogDelayValueLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 5, 1, 6),
    _HwCfmVlanTwoDelayTrapLogDelayValueLow_Type()
)
hwCfmVlanTwoDelayTrapLogDelayValueLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayTrapLogDelayValueLow.setStatus("current")
_HwCfmVlanTwoDelayRcoverTrapLogTable_Object = MibTable
hwCfmVlanTwoDelayRcoverTrapLogTable = _HwCfmVlanTwoDelayRcoverTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 6)
)
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayRcoverTrapLogTable.setStatus("current")
_HwCfmVlanTwoDelayRcoverTrapLogEntry_Object = MibTableRow
hwCfmVlanTwoDelayRcoverTrapLogEntry = _HwCfmVlanTwoDelayRcoverTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 6, 1)
)
hwCfmVlanTwoDelayRcoverTrapLogEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayRcoverTrapLogEntry.setStatus("current")
_HwCfmTwoDelayRecoveryTrapMacAddress_Type = MacAddress
_HwCfmTwoDelayRecoveryTrapMacAddress_Object = MibTableColumn
hwCfmTwoDelayRecoveryTrapMacAddress = _HwCfmTwoDelayRecoveryTrapMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 6, 1, 1),
    _HwCfmTwoDelayRecoveryTrapMacAddress_Type()
)
hwCfmTwoDelayRecoveryTrapMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmTwoDelayRecoveryTrapMacAddress.setStatus("current")
_HwCfmVlanTwoDelayRecoveryTrapLogTimestamp_Type = TimeStamp
_HwCfmVlanTwoDelayRecoveryTrapLogTimestamp_Object = MibTableColumn
hwCfmVlanTwoDelayRecoveryTrapLogTimestamp = _HwCfmVlanTwoDelayRecoveryTrapLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 6, 1, 2),
    _HwCfmVlanTwoDelayRecoveryTrapLogTimestamp_Type()
)
hwCfmVlanTwoDelayRecoveryTrapLogTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayRecoveryTrapLogTimestamp.setStatus("current")
_HwCfmVlanTwoDelayRecoveryTrapLogDelayValue_Type = Unsigned32
_HwCfmVlanTwoDelayRecoveryTrapLogDelayValue_Object = MibTableColumn
hwCfmVlanTwoDelayRecoveryTrapLogDelayValue = _HwCfmVlanTwoDelayRecoveryTrapLogDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 6, 1, 3),
    _HwCfmVlanTwoDelayRecoveryTrapLogDelayValue_Type()
)
hwCfmVlanTwoDelayRecoveryTrapLogDelayValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayRecoveryTrapLogDelayValue.setStatus("current")
_HwCfmVlanTwoDelayRecoveryTrapLogThreshold_Type = Unsigned32
_HwCfmVlanTwoDelayRecoveryTrapLogThreshold_Object = MibTableColumn
hwCfmVlanTwoDelayRecoveryTrapLogThreshold = _HwCfmVlanTwoDelayRecoveryTrapLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 6, 1, 4),
    _HwCfmVlanTwoDelayRecoveryTrapLogThreshold_Type()
)
hwCfmVlanTwoDelayRecoveryTrapLogThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayRecoveryTrapLogThreshold.setStatus("current")
_HwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh_Type = Unsigned32
_HwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh_Object = MibTableColumn
hwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh = _HwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 6, 1, 5),
    _HwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh_Type()
)
hwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh.setStatus("current")
_HwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow_Type = Unsigned32
_HwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow_Object = MibTableColumn
hwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow = _HwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 6, 1, 6),
    _HwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow_Type()
)
hwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow.setStatus("current")
_HwY1731StatisticTrapLogTable_Object = MibTable
hwY1731StatisticTrapLogTable = _HwY1731StatisticTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 7)
)
if mibBuilder.loadTexts:
    hwY1731StatisticTrapLogTable.setStatus("current")
_HwY1731StatisticTrapLogEntry_Object = MibTableRow
hwY1731StatisticTrapLogEntry = _HwY1731StatisticTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 7, 1)
)
hwY1731StatisticTrapLogEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogType"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogMacAddress"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLog8021pPriority"),
)
if mibBuilder.loadTexts:
    hwY1731StatisticTrapLogEntry.setStatus("current")


class _HwY1731StatisticTrapLogType_Type(Integer32):
    """Custom type hwY1731StatisticTrapLogType based on Integer32"""
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
        *(("duallosslocalratio", 7),
          ("duallossremoteratio", 8),
          ("onedelay", 1),
          ("onedelayvariation", 3),
          ("singlelosslocalratio", 5),
          ("singlelossremoteratio", 6),
          ("twedelayvariation", 4),
          ("twodelay", 2))
    )


_HwY1731StatisticTrapLogType_Type.__name__ = "Integer32"
_HwY1731StatisticTrapLogType_Object = MibTableColumn
hwY1731StatisticTrapLogType = _HwY1731StatisticTrapLogType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 7, 1, 1),
    _HwY1731StatisticTrapLogType_Type()
)
hwY1731StatisticTrapLogType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731StatisticTrapLogType.setStatus("current")
_HwY1731StatisticTrapLogMacAddress_Type = MacAddress
_HwY1731StatisticTrapLogMacAddress_Object = MibTableColumn
hwY1731StatisticTrapLogMacAddress = _HwY1731StatisticTrapLogMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 7, 1, 2),
    _HwY1731StatisticTrapLogMacAddress_Type()
)
hwY1731StatisticTrapLogMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731StatisticTrapLogMacAddress.setStatus("current")
_HwY1731StatisticTrapLog8021pPriority_Type = Integer32
_HwY1731StatisticTrapLog8021pPriority_Object = MibTableColumn
hwY1731StatisticTrapLog8021pPriority = _HwY1731StatisticTrapLog8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 7, 1, 3),
    _HwY1731StatisticTrapLog8021pPriority_Type()
)
hwY1731StatisticTrapLog8021pPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731StatisticTrapLog8021pPriority.setStatus("current")
_HwY1731StatisticTrapLogValue_Type = Unsigned32
_HwY1731StatisticTrapLogValue_Object = MibTableColumn
hwY1731StatisticTrapLogValue = _HwY1731StatisticTrapLogValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 7, 1, 4),
    _HwY1731StatisticTrapLogValue_Type()
)
hwY1731StatisticTrapLogValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731StatisticTrapLogValue.setStatus("current")
_HwY1731StatisticTrapLogUpperLimitThreshold_Type = Unsigned32
_HwY1731StatisticTrapLogUpperLimitThreshold_Object = MibTableColumn
hwY1731StatisticTrapLogUpperLimitThreshold = _HwY1731StatisticTrapLogUpperLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 7, 1, 5),
    _HwY1731StatisticTrapLogUpperLimitThreshold_Type()
)
hwY1731StatisticTrapLogUpperLimitThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731StatisticTrapLogUpperLimitThreshold.setStatus("current")
_HwY1731StatisticTrapLogLowerLimitThreshold_Type = Unsigned32
_HwY1731StatisticTrapLogLowerLimitThreshold_Object = MibTableColumn
hwY1731StatisticTrapLogLowerLimitThreshold = _HwY1731StatisticTrapLogLowerLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 7, 1, 6),
    _HwY1731StatisticTrapLogLowerLimitThreshold_Type()
)
hwY1731StatisticTrapLogLowerLimitThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731StatisticTrapLogLowerLimitThreshold.setStatus("current")
_HwY1731StatisticTrapLogValueHigh_Type = Unsigned32
_HwY1731StatisticTrapLogValueHigh_Object = MibTableColumn
hwY1731StatisticTrapLogValueHigh = _HwY1731StatisticTrapLogValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 7, 1, 7),
    _HwY1731StatisticTrapLogValueHigh_Type()
)
hwY1731StatisticTrapLogValueHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731StatisticTrapLogValueHigh.setStatus("current")
_HwY1731StatisticTrapLogValueLow_Type = Unsigned32
_HwY1731StatisticTrapLogValueLow_Object = MibTableColumn
hwY1731StatisticTrapLogValueLow = _HwY1731StatisticTrapLogValueLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 7, 1, 8),
    _HwY1731StatisticTrapLogValueLow_Type()
)
hwY1731StatisticTrapLogValueLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731StatisticTrapLogValueLow.setStatus("current")
_HwY1731TestIdSingleLossStatTable_Object = MibTable
hwY1731TestIdSingleLossStatTable = _HwY1731TestIdSingleLossStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 8)
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossStatTable.setStatus("current")
_HwY1731TestIdSingleLossStatEntry_Object = MibTableRow
hwY1731TestIdSingleLossStatEntry = _HwY1731TestIdSingleLossStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 8, 1)
)
hwY1731TestIdSingleLossStatEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossSequence"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossStatEntry.setStatus("current")
_HwY1731TestIdSingleLossSequence_Type = Unsigned32
_HwY1731TestIdSingleLossSequence_Object = MibTableColumn
hwY1731TestIdSingleLossSequence = _HwY1731TestIdSingleLossSequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 8, 1, 1),
    _HwY1731TestIdSingleLossSequence_Type()
)
hwY1731TestIdSingleLossSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossSequence.setStatus("current")
_HwY1731TestIdSingleLossErrInfo_Type = Unsigned32
_HwY1731TestIdSingleLossErrInfo_Object = MibTableColumn
hwY1731TestIdSingleLossErrInfo = _HwY1731TestIdSingleLossErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 8, 1, 2),
    _HwY1731TestIdSingleLossErrInfo_Type()
)
hwY1731TestIdSingleLossErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossErrInfo.setStatus("current")
_HwY1731TestIdSingleLossLocal_Type = Counter64
_HwY1731TestIdSingleLossLocal_Object = MibTableColumn
hwY1731TestIdSingleLossLocal = _HwY1731TestIdSingleLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 8, 1, 3),
    _HwY1731TestIdSingleLossLocal_Type()
)
hwY1731TestIdSingleLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossLocal.setStatus("current")
_HwY1731TestIdSingleLossLocalRatio_Type = Unsigned32
_HwY1731TestIdSingleLossLocalRatio_Object = MibTableColumn
hwY1731TestIdSingleLossLocalRatio = _HwY1731TestIdSingleLossLocalRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 8, 1, 4),
    _HwY1731TestIdSingleLossLocalRatio_Type()
)
hwY1731TestIdSingleLossLocalRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossLocalRatio.setStatus("current")
_HwY1731TestIdSingleLossRemote_Type = Counter64
_HwY1731TestIdSingleLossRemote_Object = MibTableColumn
hwY1731TestIdSingleLossRemote = _HwY1731TestIdSingleLossRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 8, 1, 5),
    _HwY1731TestIdSingleLossRemote_Type()
)
hwY1731TestIdSingleLossRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossRemote.setStatus("current")
_HwY1731TestIdSingleLossRemoteRatio_Type = Unsigned32
_HwY1731TestIdSingleLossRemoteRatio_Object = MibTableColumn
hwY1731TestIdSingleLossRemoteRatio = _HwY1731TestIdSingleLossRemoteRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 8, 1, 6),
    _HwY1731TestIdSingleLossRemoteRatio_Type()
)
hwY1731TestIdSingleLossRemoteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossRemoteRatio.setStatus("current")
_HwY1731TestIdSingleLossOnDemandStartTime_Type = DateAndTime
_HwY1731TestIdSingleLossOnDemandStartTime_Object = MibTableColumn
hwY1731TestIdSingleLossOnDemandStartTime = _HwY1731TestIdSingleLossOnDemandStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 8, 1, 7),
    _HwY1731TestIdSingleLossOnDemandStartTime_Type()
)
hwY1731TestIdSingleLossOnDemandStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossOnDemandStartTime.setStatus("current")
_HwY1731TestIdOneDelayStatTable_Object = MibTable
hwY1731TestIdOneDelayStatTable = _HwY1731TestIdOneDelayStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 9)
)
if mibBuilder.loadTexts:
    hwY1731TestIdOneDelayStatTable.setStatus("current")
_HwY1731TestIdOneDelayStatEntry_Object = MibTableRow
hwY1731TestIdOneDelayStatEntry = _HwY1731TestIdOneDelayStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 9, 1)
)
hwY1731TestIdOneDelayStatEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneDelaySequence"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdOneDelayStatEntry.setStatus("current")
_HwY1731TestIdOneDelaySequence_Type = Unsigned32
_HwY1731TestIdOneDelaySequence_Object = MibTableColumn
hwY1731TestIdOneDelaySequence = _HwY1731TestIdOneDelaySequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 9, 1, 1),
    _HwY1731TestIdOneDelaySequence_Type()
)
hwY1731TestIdOneDelaySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdOneDelaySequence.setStatus("current")
_HwY1731TestIdOneDelayErrInfo_Type = Unsigned32
_HwY1731TestIdOneDelayErrInfo_Object = MibTableColumn
hwY1731TestIdOneDelayErrInfo = _HwY1731TestIdOneDelayErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 9, 1, 2),
    _HwY1731TestIdOneDelayErrInfo_Type()
)
hwY1731TestIdOneDelayErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdOneDelayErrInfo.setStatus("current")
_HwY1731TestIdOneDelay_Type = Integer32
_HwY1731TestIdOneDelay_Object = MibTableColumn
hwY1731TestIdOneDelay = _HwY1731TestIdOneDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 9, 1, 3),
    _HwY1731TestIdOneDelay_Type()
)
hwY1731TestIdOneDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdOneDelay.setStatus("current")
_HwY1731TestIdOneDelayVariation_Type = Unsigned32
_HwY1731TestIdOneDelayVariation_Object = MibTableColumn
hwY1731TestIdOneDelayVariation = _HwY1731TestIdOneDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 9, 1, 4),
    _HwY1731TestIdOneDelayVariation_Type()
)
hwY1731TestIdOneDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdOneDelayVariation.setStatus("current")
_HwY1731TestIdOneDelayOnDemandStartTime_Type = DateAndTime
_HwY1731TestIdOneDelayOnDemandStartTime_Object = MibTableColumn
hwY1731TestIdOneDelayOnDemandStartTime = _HwY1731TestIdOneDelayOnDemandStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 9, 1, 5),
    _HwY1731TestIdOneDelayOnDemandStartTime_Type()
)
hwY1731TestIdOneDelayOnDemandStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdOneDelayOnDemandStartTime.setStatus("current")
_HwY1731TestIdTwoDelayStatTable_Object = MibTable
hwY1731TestIdTwoDelayStatTable = _HwY1731TestIdTwoDelayStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 10)
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayStatTable.setStatus("current")
_HwY1731TestIdTwoDelayStatEntry_Object = MibTableRow
hwY1731TestIdTwoDelayStatEntry = _HwY1731TestIdTwoDelayStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 10, 1)
)
hwY1731TestIdTwoDelayStatEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelaySequence"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayStatEntry.setStatus("current")
_HwY1731TestIdTwoDelaySequence_Type = Unsigned32
_HwY1731TestIdTwoDelaySequence_Object = MibTableColumn
hwY1731TestIdTwoDelaySequence = _HwY1731TestIdTwoDelaySequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 10, 1, 1),
    _HwY1731TestIdTwoDelaySequence_Type()
)
hwY1731TestIdTwoDelaySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelaySequence.setStatus("current")
_HwY1731TestIdTwoDelayErrInfo_Type = Unsigned32
_HwY1731TestIdTwoDelayErrInfo_Object = MibTableColumn
hwY1731TestIdTwoDelayErrInfo = _HwY1731TestIdTwoDelayErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 10, 1, 2),
    _HwY1731TestIdTwoDelayErrInfo_Type()
)
hwY1731TestIdTwoDelayErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayErrInfo.setStatus("current")
_HwY1731TestIdTwoDelay_Type = Unsigned32
_HwY1731TestIdTwoDelay_Object = MibTableColumn
hwY1731TestIdTwoDelay = _HwY1731TestIdTwoDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 10, 1, 3),
    _HwY1731TestIdTwoDelay_Type()
)
hwY1731TestIdTwoDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelay.setStatus("current")
_HwY1731TestIdTwoDelayVariation_Type = Unsigned32
_HwY1731TestIdTwoDelayVariation_Object = MibTableColumn
hwY1731TestIdTwoDelayVariation = _HwY1731TestIdTwoDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 10, 1, 4),
    _HwY1731TestIdTwoDelayVariation_Type()
)
hwY1731TestIdTwoDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayVariation.setStatus("current")
_HwY1731TestIdTwoDelayOnDemandStartTime_Type = DateAndTime
_HwY1731TestIdTwoDelayOnDemandStartTime_Object = MibTableColumn
hwY1731TestIdTwoDelayOnDemandStartTime = _HwY1731TestIdTwoDelayOnDemandStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 10, 1, 5),
    _HwY1731TestIdTwoDelayOnDemandStartTime_Type()
)
hwY1731TestIdTwoDelayOnDemandStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayOnDemandStartTime.setStatus("current")
_HwY1731TestIdStatisticResetTable_Object = MibTable
hwY1731TestIdStatisticResetTable = _HwY1731TestIdStatisticResetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 11)
)
if mibBuilder.loadTexts:
    hwY1731TestIdStatisticResetTable.setStatus("current")
_HwY1731TestIdStatisticResetEntry_Object = MibTableRow
hwY1731TestIdStatisticResetEntry = _HwY1731TestIdStatisticResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 11, 1)
)
hwY1731TestIdStatisticResetEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdStatisticResetEntry.setStatus("current")


class _HwY1731TestIdResetStatisticType_Type(Integer32):
    """Custom type hwY1731TestIdResetStatisticType based on Integer32"""
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
        *(("dualloss", 3),
          ("invalid", 1),
          ("onewaydelay", 4),
          ("singleloss", 2),
          ("singlesynloss", 6),
          ("twowaydelay", 5))
    )


_HwY1731TestIdResetStatisticType_Type.__name__ = "Integer32"
_HwY1731TestIdResetStatisticType_Object = MibTableColumn
hwY1731TestIdResetStatisticType = _HwY1731TestIdResetStatisticType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 11, 1, 1),
    _HwY1731TestIdResetStatisticType_Type()
)
hwY1731TestIdResetStatisticType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwY1731TestIdResetStatisticType.setStatus("current")
_HwY1731TestIdTwoDelaySummaryStatTable_Object = MibTable
hwY1731TestIdTwoDelaySummaryStatTable = _HwY1731TestIdTwoDelaySummaryStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12)
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelaySummaryStatTable.setStatus("current")
_HwY1731TestIdTwoDelaySummaryStatEntry_Object = MibTableRow
hwY1731TestIdTwoDelaySummaryStatEntry = _HwY1731TestIdTwoDelaySummaryStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1)
)
hwY1731TestIdTwoDelaySummaryStatEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayIndex"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelaySummaryStatEntry.setStatus("current")
_HwY1731TestIdTwoDelayIndex_Type = Unsigned32
_HwY1731TestIdTwoDelayIndex_Object = MibTableColumn
hwY1731TestIdTwoDelayIndex = _HwY1731TestIdTwoDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 1),
    _HwY1731TestIdTwoDelayIndex_Type()
)
hwY1731TestIdTwoDelayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayIndex.setStatus("current")
_HwY1731TestIdTwoDelayNbrSamples_Type = Unsigned32
_HwY1731TestIdTwoDelayNbrSamples_Object = MibTableColumn
hwY1731TestIdTwoDelayNbrSamples = _HwY1731TestIdTwoDelayNbrSamples_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 2),
    _HwY1731TestIdTwoDelayNbrSamples_Type()
)
hwY1731TestIdTwoDelayNbrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayNbrSamples.setStatus("current")
_HwY1731TestIdTwoDelayMax_Type = Unsigned32
_HwY1731TestIdTwoDelayMax_Object = MibTableColumn
hwY1731TestIdTwoDelayMax = _HwY1731TestIdTwoDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 3),
    _HwY1731TestIdTwoDelayMax_Type()
)
hwY1731TestIdTwoDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayMax.setStatus("current")
_HwY1731TestIdTwoDelayMin_Type = Unsigned32
_HwY1731TestIdTwoDelayMin_Object = MibTableColumn
hwY1731TestIdTwoDelayMin = _HwY1731TestIdTwoDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 4),
    _HwY1731TestIdTwoDelayMin_Type()
)
hwY1731TestIdTwoDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayMin.setStatus("current")
_HwY1731TestIdTwoDelayAve_Type = Unsigned32
_HwY1731TestIdTwoDelayAve_Object = MibTableColumn
hwY1731TestIdTwoDelayAve = _HwY1731TestIdTwoDelayAve_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 5),
    _HwY1731TestIdTwoDelayAve_Type()
)
hwY1731TestIdTwoDelayAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayAve.setStatus("current")
_HwY1731TestIdTwoDelayExceedUpLimitNum_Type = Unsigned32
_HwY1731TestIdTwoDelayExceedUpLimitNum_Object = MibTableColumn
hwY1731TestIdTwoDelayExceedUpLimitNum = _HwY1731TestIdTwoDelayExceedUpLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 6),
    _HwY1731TestIdTwoDelayExceedUpLimitNum_Type()
)
hwY1731TestIdTwoDelayExceedUpLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayExceedUpLimitNum.setStatus("current")
_HwY1731TestIdTwoDelayBelowLowLimitNum_Type = Unsigned32
_HwY1731TestIdTwoDelayBelowLowLimitNum_Object = MibTableColumn
hwY1731TestIdTwoDelayBelowLowLimitNum = _HwY1731TestIdTwoDelayBelowLowLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 7),
    _HwY1731TestIdTwoDelayBelowLowLimitNum_Type()
)
hwY1731TestIdTwoDelayBelowLowLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayBelowLowLimitNum.setStatus("current")
_HwY1731TestIdTwoDelayVariationNbrSamples_Type = Unsigned32
_HwY1731TestIdTwoDelayVariationNbrSamples_Object = MibTableColumn
hwY1731TestIdTwoDelayVariationNbrSamples = _HwY1731TestIdTwoDelayVariationNbrSamples_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 8),
    _HwY1731TestIdTwoDelayVariationNbrSamples_Type()
)
hwY1731TestIdTwoDelayVariationNbrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayVariationNbrSamples.setStatus("current")
_HwY1731TestIdTwoDelayVariationMax_Type = Unsigned32
_HwY1731TestIdTwoDelayVariationMax_Object = MibTableColumn
hwY1731TestIdTwoDelayVariationMax = _HwY1731TestIdTwoDelayVariationMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 9),
    _HwY1731TestIdTwoDelayVariationMax_Type()
)
hwY1731TestIdTwoDelayVariationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayVariationMax.setStatus("current")
_HwY1731TestIdTwoDelayVariationMin_Type = Unsigned32
_HwY1731TestIdTwoDelayVariationMin_Object = MibTableColumn
hwY1731TestIdTwoDelayVariationMin = _HwY1731TestIdTwoDelayVariationMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 10),
    _HwY1731TestIdTwoDelayVariationMin_Type()
)
hwY1731TestIdTwoDelayVariationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayVariationMin.setStatus("current")
_HwY1731TestIdTwoDelayVariationAve_Type = Unsigned32
_HwY1731TestIdTwoDelayVariationAve_Object = MibTableColumn
hwY1731TestIdTwoDelayVariationAve = _HwY1731TestIdTwoDelayVariationAve_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 11),
    _HwY1731TestIdTwoDelayVariationAve_Type()
)
hwY1731TestIdTwoDelayVariationAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayVariationAve.setStatus("current")
_HwY1731TestIdTwoDelayVarExceedUpLimitNum_Type = Unsigned32
_HwY1731TestIdTwoDelayVarExceedUpLimitNum_Object = MibTableColumn
hwY1731TestIdTwoDelayVarExceedUpLimitNum = _HwY1731TestIdTwoDelayVarExceedUpLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 12),
    _HwY1731TestIdTwoDelayVarExceedUpLimitNum_Type()
)
hwY1731TestIdTwoDelayVarExceedUpLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayVarExceedUpLimitNum.setStatus("current")
_HwY1731TestIdTwoDelayVarBelowLowLimitNum_Type = Unsigned32
_HwY1731TestIdTwoDelayVarBelowLowLimitNum_Object = MibTableColumn
hwY1731TestIdTwoDelayVarBelowLowLimitNum = _HwY1731TestIdTwoDelayVarBelowLowLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 12, 1, 13),
    _HwY1731TestIdTwoDelayVarBelowLowLimitNum_Type()
)
hwY1731TestIdTwoDelayVarBelowLowLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayVarBelowLowLimitNum.setStatus("current")
_HwY1731TestIdSingleSynLossSummaryStatTable_Object = MibTable
hwY1731TestIdSingleSynLossSummaryStatTable = _HwY1731TestIdSingleSynLossSummaryStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13)
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossSummaryStatTable.setStatus("current")
_HwY1731TestIdSingleSynLossSummaryStatEntry_Object = MibTableRow
hwY1731TestIdSingleSynLossSummaryStatEntry = _HwY1731TestIdSingleSynLossSummaryStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1)
)
hwY1731TestIdSingleSynLossSummaryStatEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossIndex"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossSummaryStatEntry.setStatus("current")
_HwY1731TestIdSingleSynLossIndex_Type = Unsigned32
_HwY1731TestIdSingleSynLossIndex_Object = MibTableColumn
hwY1731TestIdSingleSynLossIndex = _HwY1731TestIdSingleSynLossIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 1),
    _HwY1731TestIdSingleSynLossIndex_Type()
)
hwY1731TestIdSingleSynLossIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossIndex.setStatus("current")
_HwY1731TestIdSingleSynLossNbrSamples_Type = Unsigned32
_HwY1731TestIdSingleSynLossNbrSamples_Object = MibTableColumn
hwY1731TestIdSingleSynLossNbrSamples = _HwY1731TestIdSingleSynLossNbrSamples_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 2),
    _HwY1731TestIdSingleSynLossNbrSamples_Type()
)
hwY1731TestIdSingleSynLossNbrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossNbrSamples.setStatus("current")
_HwY1731TestIdSingleSynSendRemote_Type = Unsigned32
_HwY1731TestIdSingleSynSendRemote_Object = MibTableColumn
hwY1731TestIdSingleSynSendRemote = _HwY1731TestIdSingleSynSendRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 3),
    _HwY1731TestIdSingleSynSendRemote_Type()
)
hwY1731TestIdSingleSynSendRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynSendRemote.setStatus("current")
_HwY1731TestIdSingleSynRecvLocal_Type = Unsigned32
_HwY1731TestIdSingleSynRecvLocal_Object = MibTableColumn
hwY1731TestIdSingleSynRecvLocal = _HwY1731TestIdSingleSynRecvLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 4),
    _HwY1731TestIdSingleSynRecvLocal_Type()
)
hwY1731TestIdSingleSynRecvLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynRecvLocal.setStatus("current")
_HwY1731TestIdSingleSynLossLocal_Type = Integer32
_HwY1731TestIdSingleSynLossLocal_Object = MibTableColumn
hwY1731TestIdSingleSynLossLocal = _HwY1731TestIdSingleSynLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 5),
    _HwY1731TestIdSingleSynLossLocal_Type()
)
hwY1731TestIdSingleSynLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossLocal.setStatus("current")
_HwY1731TestIdSingleSynExceedLocalUpLimitNum_Type = Unsigned32
_HwY1731TestIdSingleSynExceedLocalUpLimitNum_Object = MibTableColumn
hwY1731TestIdSingleSynExceedLocalUpLimitNum = _HwY1731TestIdSingleSynExceedLocalUpLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 6),
    _HwY1731TestIdSingleSynExceedLocalUpLimitNum_Type()
)
hwY1731TestIdSingleSynExceedLocalUpLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynExceedLocalUpLimitNum.setStatus("current")
_HwY1731TestIdSingleSynBelowLocalLowLimitNum_Type = Unsigned32
_HwY1731TestIdSingleSynBelowLocalLowLimitNum_Object = MibTableColumn
hwY1731TestIdSingleSynBelowLocalLowLimitNum = _HwY1731TestIdSingleSynBelowLocalLowLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 7),
    _HwY1731TestIdSingleSynBelowLocalLowLimitNum_Type()
)
hwY1731TestIdSingleSynBelowLocalLowLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynBelowLocalLowLimitNum.setStatus("current")
_HwY1731TestIdSingleSynSendLocal_Type = Unsigned32
_HwY1731TestIdSingleSynSendLocal_Object = MibTableColumn
hwY1731TestIdSingleSynSendLocal = _HwY1731TestIdSingleSynSendLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 8),
    _HwY1731TestIdSingleSynSendLocal_Type()
)
hwY1731TestIdSingleSynSendLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynSendLocal.setStatus("current")
_HwY1731TestIdSingleSynRecvRemote_Type = Unsigned32
_HwY1731TestIdSingleSynRecvRemote_Object = MibTableColumn
hwY1731TestIdSingleSynRecvRemote = _HwY1731TestIdSingleSynRecvRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 9),
    _HwY1731TestIdSingleSynRecvRemote_Type()
)
hwY1731TestIdSingleSynRecvRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynRecvRemote.setStatus("current")
_HwY1731TestIdSingleSynLossRemote_Type = Integer32
_HwY1731TestIdSingleSynLossRemote_Object = MibTableColumn
hwY1731TestIdSingleSynLossRemote = _HwY1731TestIdSingleSynLossRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 10),
    _HwY1731TestIdSingleSynLossRemote_Type()
)
hwY1731TestIdSingleSynLossRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossRemote.setStatus("current")
_HwY1731TestIdSingleSynExceedRemoteUpLimitNum_Type = Unsigned32
_HwY1731TestIdSingleSynExceedRemoteUpLimitNum_Object = MibTableColumn
hwY1731TestIdSingleSynExceedRemoteUpLimitNum = _HwY1731TestIdSingleSynExceedRemoteUpLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 11),
    _HwY1731TestIdSingleSynExceedRemoteUpLimitNum_Type()
)
hwY1731TestIdSingleSynExceedRemoteUpLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynExceedRemoteUpLimitNum.setStatus("current")
_HwY1731TestIdSingleSynBelowRemoteLowLimitNum_Type = Unsigned32
_HwY1731TestIdSingleSynBelowRemoteLowLimitNum_Object = MibTableColumn
hwY1731TestIdSingleSynBelowRemoteLowLimitNum = _HwY1731TestIdSingleSynBelowRemoteLowLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 13, 1, 12),
    _HwY1731TestIdSingleSynBelowRemoteLowLimitNum_Type()
)
hwY1731TestIdSingleSynBelowRemoteLowLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynBelowRemoteLowLimitNum.setStatus("current")
_HwY1731SingleLossSummaryStatTable_Object = MibTable
hwY1731SingleLossSummaryStatTable = _HwY1731SingleLossSummaryStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14)
)
if mibBuilder.loadTexts:
    hwY1731SingleLossSummaryStatTable.setStatus("current")
_HwY1731SingleLossSummaryStatEntry_Object = MibTableRow
hwY1731SingleLossSummaryStatEntry = _HwY1731SingleLossSummaryStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1)
)
hwY1731SingleLossSummaryStatEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaIndex"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731RemoteIp"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731VcId"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731SingleLoss8021pValue"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731SingleLossIndex"),
)
if mibBuilder.loadTexts:
    hwY1731SingleLossSummaryStatEntry.setStatus("current")
_HwY1731SingleLossIndex_Type = Unsigned32
_HwY1731SingleLossIndex_Object = MibTableColumn
hwY1731SingleLossIndex = _HwY1731SingleLossIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 1),
    _HwY1731SingleLossIndex_Type()
)
hwY1731SingleLossIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731SingleLossIndex.setStatus("current")
_HwY1731SingleLossNbrSamples_Type = Unsigned32
_HwY1731SingleLossNbrSamples_Object = MibTableColumn
hwY1731SingleLossNbrSamples = _HwY1731SingleLossNbrSamples_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 2),
    _HwY1731SingleLossNbrSamples_Type()
)
hwY1731SingleLossNbrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossNbrSamples.setStatus("current")
_HwY1731SingleLossSendRemote_Type = Counter64
_HwY1731SingleLossSendRemote_Object = MibTableColumn
hwY1731SingleLossSendRemote = _HwY1731SingleLossSendRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 3),
    _HwY1731SingleLossSendRemote_Type()
)
hwY1731SingleLossSendRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossSendRemote.setStatus("current")
_HwY1731SingleLossRecvLocal_Type = Counter64
_HwY1731SingleLossRecvLocal_Object = MibTableColumn
hwY1731SingleLossRecvLocal = _HwY1731SingleLossRecvLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 4),
    _HwY1731SingleLossRecvLocal_Type()
)
hwY1731SingleLossRecvLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossRecvLocal.setStatus("current")
_HwY1731SingleLossLossLocal_Type = Counter64
_HwY1731SingleLossLossLocal_Object = MibTableColumn
hwY1731SingleLossLossLocal = _HwY1731SingleLossLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 5),
    _HwY1731SingleLossLossLocal_Type()
)
hwY1731SingleLossLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossLossLocal.setStatus("current")
_HwY1731SingleLossExceedLocalUpLimitNum_Type = Unsigned32
_HwY1731SingleLossExceedLocalUpLimitNum_Object = MibTableColumn
hwY1731SingleLossExceedLocalUpLimitNum = _HwY1731SingleLossExceedLocalUpLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 6),
    _HwY1731SingleLossExceedLocalUpLimitNum_Type()
)
hwY1731SingleLossExceedLocalUpLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossExceedLocalUpLimitNum.setStatus("current")
_HwY1731SingleLossBelowLocallowLimitNum_Type = Unsigned32
_HwY1731SingleLossBelowLocallowLimitNum_Object = MibTableColumn
hwY1731SingleLossBelowLocallowLimitNum = _HwY1731SingleLossBelowLocallowLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 7),
    _HwY1731SingleLossBelowLocallowLimitNum_Type()
)
hwY1731SingleLossBelowLocallowLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossBelowLocallowLimitNum.setStatus("current")
_HwY1731SingleLossSendLocal_Type = Counter64
_HwY1731SingleLossSendLocal_Object = MibTableColumn
hwY1731SingleLossSendLocal = _HwY1731SingleLossSendLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 8),
    _HwY1731SingleLossSendLocal_Type()
)
hwY1731SingleLossSendLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossSendLocal.setStatus("current")
_HwY1731SingleLossRecvRemote_Type = Counter64
_HwY1731SingleLossRecvRemote_Object = MibTableColumn
hwY1731SingleLossRecvRemote = _HwY1731SingleLossRecvRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 9),
    _HwY1731SingleLossRecvRemote_Type()
)
hwY1731SingleLossRecvRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossRecvRemote.setStatus("current")
_HwY1731SingleLossLossRemote_Type = Counter64
_HwY1731SingleLossLossRemote_Object = MibTableColumn
hwY1731SingleLossLossRemote = _HwY1731SingleLossLossRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 10),
    _HwY1731SingleLossLossRemote_Type()
)
hwY1731SingleLossLossRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossLossRemote.setStatus("current")
_HwY1731SingleLossExceedRemoteUpLimitNum_Type = Unsigned32
_HwY1731SingleLossExceedRemoteUpLimitNum_Object = MibTableColumn
hwY1731SingleLossExceedRemoteUpLimitNum = _HwY1731SingleLossExceedRemoteUpLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 11),
    _HwY1731SingleLossExceedRemoteUpLimitNum_Type()
)
hwY1731SingleLossExceedRemoteUpLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossExceedRemoteUpLimitNum.setStatus("current")
_HwY1731SingleLossBelowRemotelowLimitNum_Type = Unsigned32
_HwY1731SingleLossBelowRemotelowLimitNum_Object = MibTableColumn
hwY1731SingleLossBelowRemotelowLimitNum = _HwY1731SingleLossBelowRemotelowLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 14, 1, 12),
    _HwY1731SingleLossBelowRemotelowLimitNum_Type()
)
hwY1731SingleLossBelowRemotelowLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731SingleLossBelowRemotelowLimitNum.setStatus("current")
_HwY1731TestIdSingleLossSummaryStatTable_Object = MibTable
hwY1731TestIdSingleLossSummaryStatTable = _HwY1731TestIdSingleLossSummaryStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15)
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossSummaryStatTable.setStatus("current")
_HwY1731TestIdSingleLossSummaryStatEntry_Object = MibTableRow
hwY1731TestIdSingleLossSummaryStatEntry = _HwY1731TestIdSingleLossSummaryStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1)
)
hwY1731TestIdSingleLossSummaryStatEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossIndex"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossSummaryStatEntry.setStatus("current")
_HwY1731TestIdSingleLossIndex_Type = Unsigned32
_HwY1731TestIdSingleLossIndex_Object = MibTableColumn
hwY1731TestIdSingleLossIndex = _HwY1731TestIdSingleLossIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 1),
    _HwY1731TestIdSingleLossIndex_Type()
)
hwY1731TestIdSingleLossIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossIndex.setStatus("current")
_HwY1731TestIdSingleLossNbrSamples_Type = Unsigned32
_HwY1731TestIdSingleLossNbrSamples_Object = MibTableColumn
hwY1731TestIdSingleLossNbrSamples = _HwY1731TestIdSingleLossNbrSamples_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 2),
    _HwY1731TestIdSingleLossNbrSamples_Type()
)
hwY1731TestIdSingleLossNbrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossNbrSamples.setStatus("current")
_HwY1731TestIdSingleLossSendRemote_Type = Counter64
_HwY1731TestIdSingleLossSendRemote_Object = MibTableColumn
hwY1731TestIdSingleLossSendRemote = _HwY1731TestIdSingleLossSendRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 3),
    _HwY1731TestIdSingleLossSendRemote_Type()
)
hwY1731TestIdSingleLossSendRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossSendRemote.setStatus("current")
_HwY1731TestIdSingleLossRecvLocal_Type = Counter64
_HwY1731TestIdSingleLossRecvLocal_Object = MibTableColumn
hwY1731TestIdSingleLossRecvLocal = _HwY1731TestIdSingleLossRecvLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 4),
    _HwY1731TestIdSingleLossRecvLocal_Type()
)
hwY1731TestIdSingleLossRecvLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossRecvLocal.setStatus("current")
_HwY1731TestIdSingleLossLossLocal_Type = Counter64
_HwY1731TestIdSingleLossLossLocal_Object = MibTableColumn
hwY1731TestIdSingleLossLossLocal = _HwY1731TestIdSingleLossLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 5),
    _HwY1731TestIdSingleLossLossLocal_Type()
)
hwY1731TestIdSingleLossLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossLossLocal.setStatus("current")
_HwY1731TestIdSingleLossExceedLocalUpLimitNum_Type = Unsigned32
_HwY1731TestIdSingleLossExceedLocalUpLimitNum_Object = MibTableColumn
hwY1731TestIdSingleLossExceedLocalUpLimitNum = _HwY1731TestIdSingleLossExceedLocalUpLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 6),
    _HwY1731TestIdSingleLossExceedLocalUpLimitNum_Type()
)
hwY1731TestIdSingleLossExceedLocalUpLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossExceedLocalUpLimitNum.setStatus("current")
_HwY1731TestIdSingleLossBelowLocallowLimitNum_Type = Unsigned32
_HwY1731TestIdSingleLossBelowLocallowLimitNum_Object = MibTableColumn
hwY1731TestIdSingleLossBelowLocallowLimitNum = _HwY1731TestIdSingleLossBelowLocallowLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 7),
    _HwY1731TestIdSingleLossBelowLocallowLimitNum_Type()
)
hwY1731TestIdSingleLossBelowLocallowLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossBelowLocallowLimitNum.setStatus("current")
_HwY1731TestIdSingleLossSendLocal_Type = Counter64
_HwY1731TestIdSingleLossSendLocal_Object = MibTableColumn
hwY1731TestIdSingleLossSendLocal = _HwY1731TestIdSingleLossSendLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 8),
    _HwY1731TestIdSingleLossSendLocal_Type()
)
hwY1731TestIdSingleLossSendLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossSendLocal.setStatus("current")
_HwY1731TestIdSingleLossRecvRemote_Type = Counter64
_HwY1731TestIdSingleLossRecvRemote_Object = MibTableColumn
hwY1731TestIdSingleLossRecvRemote = _HwY1731TestIdSingleLossRecvRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 9),
    _HwY1731TestIdSingleLossRecvRemote_Type()
)
hwY1731TestIdSingleLossRecvRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossRecvRemote.setStatus("current")
_HwY1731TestIdSingleLossLossRemote_Type = Counter64
_HwY1731TestIdSingleLossLossRemote_Object = MibTableColumn
hwY1731TestIdSingleLossLossRemote = _HwY1731TestIdSingleLossLossRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 10),
    _HwY1731TestIdSingleLossLossRemote_Type()
)
hwY1731TestIdSingleLossLossRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossLossRemote.setStatus("current")
_HwY1731TestIdSingleLossExceedRemoteUpLimitNum_Type = Unsigned32
_HwY1731TestIdSingleLossExceedRemoteUpLimitNum_Object = MibTableColumn
hwY1731TestIdSingleLossExceedRemoteUpLimitNum = _HwY1731TestIdSingleLossExceedRemoteUpLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 11),
    _HwY1731TestIdSingleLossExceedRemoteUpLimitNum_Type()
)
hwY1731TestIdSingleLossExceedRemoteUpLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossExceedRemoteUpLimitNum.setStatus("current")
_HwY1731TestIdSingleLossBelowRemotelowLimitNum_Type = Unsigned32
_HwY1731TestIdSingleLossBelowRemotelowLimitNum_Object = MibTableColumn
hwY1731TestIdSingleLossBelowRemotelowLimitNum = _HwY1731TestIdSingleLossBelowRemotelowLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 15, 1, 12),
    _HwY1731TestIdSingleLossBelowRemotelowLimitNum_Type()
)
hwY1731TestIdSingleLossBelowRemotelowLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossBelowRemotelowLimitNum.setStatus("current")
_HwY1731TestIdSingleSynLossStatTable_Object = MibTable
hwY1731TestIdSingleSynLossStatTable = _HwY1731TestIdSingleSynLossStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16)
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossStatTable.setStatus("current")
_HwY1731TestIdSingleSynLossStatEntry_Object = MibTableRow
hwY1731TestIdSingleSynLossStatEntry = _HwY1731TestIdSingleSynLossStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1)
)
hwY1731TestIdSingleSynLossStatEntry.setIndexNames(
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
    (0, "HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossSequence"),
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossStatEntry.setStatus("current")
_HwY1731TestIdSingleSynLossSequence_Type = Unsigned32
_HwY1731TestIdSingleSynLossSequence_Object = MibTableColumn
hwY1731TestIdSingleSynLossSequence = _HwY1731TestIdSingleSynLossSequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 1),
    _HwY1731TestIdSingleSynLossSequence_Type()
)
hwY1731TestIdSingleSynLossSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossSequence.setStatus("current")
_HwY1731TestIdSingleSynLossErrInfo_Type = Unsigned32
_HwY1731TestIdSingleSynLossErrInfo_Object = MibTableColumn
hwY1731TestIdSingleSynLossErrInfo = _HwY1731TestIdSingleSynLossErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 2),
    _HwY1731TestIdSingleSynLossErrInfo_Type()
)
hwY1731TestIdSingleSynLossErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossErrInfo.setStatus("current")
_HwY1731TestIdSingleSynLossLocalSend_Type = Unsigned32
_HwY1731TestIdSingleSynLossLocalSend_Object = MibTableColumn
hwY1731TestIdSingleSynLossLocalSend = _HwY1731TestIdSingleSynLossLocalSend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 3),
    _HwY1731TestIdSingleSynLossLocalSend_Type()
)
hwY1731TestIdSingleSynLossLocalSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossLocalSend.setStatus("current")
_HwY1731TestIdSingleSynLossRemoteSend_Type = Unsigned32
_HwY1731TestIdSingleSynLossRemoteSend_Object = MibTableColumn
hwY1731TestIdSingleSynLossRemoteSend = _HwY1731TestIdSingleSynLossRemoteSend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 4),
    _HwY1731TestIdSingleSynLossRemoteSend_Type()
)
hwY1731TestIdSingleSynLossRemoteSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossRemoteSend.setStatus("current")
_HwY1731TestIdSingleSynLossLocalReceive_Type = Unsigned32
_HwY1731TestIdSingleSynLossLocalReceive_Object = MibTableColumn
hwY1731TestIdSingleSynLossLocalReceive = _HwY1731TestIdSingleSynLossLocalReceive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 5),
    _HwY1731TestIdSingleSynLossLocalReceive_Type()
)
hwY1731TestIdSingleSynLossLocalReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossLocalReceive.setStatus("current")
_HwY1731TestIdSingleSynLossUnack_Type = Unsigned32
_HwY1731TestIdSingleSynLossUnack_Object = MibTableColumn
hwY1731TestIdSingleSynLossUnack = _HwY1731TestIdSingleSynLossUnack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 6),
    _HwY1731TestIdSingleSynLossUnack_Type()
)
hwY1731TestIdSingleSynLossUnack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossUnack.setStatus("current")
_HwY1731TestIdSingleSynLossLossLocal_Type = Integer32
_HwY1731TestIdSingleSynLossLossLocal_Object = MibTableColumn
hwY1731TestIdSingleSynLossLossLocal = _HwY1731TestIdSingleSynLossLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 7),
    _HwY1731TestIdSingleSynLossLossLocal_Type()
)
hwY1731TestIdSingleSynLossLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossLossLocal.setStatus("current")
_HwY1731TestIdSingleSynLossLocalRatio_Type = Unsigned32
_HwY1731TestIdSingleSynLossLocalRatio_Object = MibTableColumn
hwY1731TestIdSingleSynLossLocalRatio = _HwY1731TestIdSingleSynLossLocalRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 8),
    _HwY1731TestIdSingleSynLossLocalRatio_Type()
)
hwY1731TestIdSingleSynLossLocalRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossLocalRatio.setStatus("current")
_HwY1731TestIdSingleSynLossLossRemote_Type = Integer32
_HwY1731TestIdSingleSynLossLossRemote_Object = MibTableColumn
hwY1731TestIdSingleSynLossLossRemote = _HwY1731TestIdSingleSynLossLossRemote_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 9),
    _HwY1731TestIdSingleSynLossLossRemote_Type()
)
hwY1731TestIdSingleSynLossLossRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossLossRemote.setStatus("current")
_HwY1731TestIdSingleSynLossRemoteRatio_Type = Unsigned32
_HwY1731TestIdSingleSynLossRemoteRatio_Object = MibTableColumn
hwY1731TestIdSingleSynLossRemoteRatio = _HwY1731TestIdSingleSynLossRemoteRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 10),
    _HwY1731TestIdSingleSynLossRemoteRatio_Type()
)
hwY1731TestIdSingleSynLossRemoteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossRemoteRatio.setStatus("current")
_HwY1731TestIdSingleSynLossOnDemandStartTime_Type = DateAndTime
_HwY1731TestIdSingleSynLossOnDemandStartTime_Object = MibTableColumn
hwY1731TestIdSingleSynLossOnDemandStartTime = _HwY1731TestIdSingleSynLossOnDemandStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 2, 16, 1, 11),
    _HwY1731TestIdSingleSynLossOnDemandStartTime_Type()
)
hwY1731TestIdSingleSynLossOnDemandStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossOnDemandStartTime.setStatus("current")
_HwY1731AisMaxPktNum_Type = Unsigned32
_HwY1731AisMaxPktNum_Object = MibScalar
hwY1731AisMaxPktNum = _HwY1731AisMaxPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 3),
    _HwY1731AisMaxPktNum_Type()
)
hwY1731AisMaxPktNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731AisMaxPktNum.setStatus("current")
_HwY1731PMModeEnable_Type = EnabledStatus
_HwY1731PMModeEnable_Object = MibScalar
hwY1731PMModeEnable = _HwY1731PMModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 4),
    _HwY1731PMModeEnable_Type()
)
hwY1731PMModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwY1731PMModeEnable.setStatus("current")
_HwY1731GlobalObject_ObjectIdentity = ObjectIdentity
hwY1731GlobalObject = _HwY1731GlobalObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 5)
)
_HwY1731MaxTestId_Type = Unsigned32
_HwY1731MaxTestId_Object = MibScalar
hwY1731MaxTestId = _HwY1731MaxTestId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 5, 1),
    _HwY1731MaxTestId_Type()
)
hwY1731MaxTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwY1731MaxTestId.setStatus("current")
_HwY1731LckMaxPktNum_Type = Unsigned32
_HwY1731LckMaxPktNum_Object = MibScalar
hwY1731LckMaxPktNum = _HwY1731LckMaxPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 5, 2),
    _HwY1731LckMaxPktNum_Type()
)
hwY1731LckMaxPktNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731LckMaxPktNum.setStatus("current")
_HwY1731LckCurrentPktNum_Type = Unsigned32
_HwY1731LckCurrentPktNum_Object = MibScalar
hwY1731LckCurrentPktNum = _HwY1731LckCurrentPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 5, 3),
    _HwY1731LckCurrentPktNum_Type()
)
hwY1731LckCurrentPktNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731LckCurrentPktNum.setStatus("current")
_HwY1731LckUpperThreshold_Type = Unsigned32
_HwY1731LckUpperThreshold_Object = MibScalar
hwY1731LckUpperThreshold = _HwY1731LckUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 5, 4),
    _HwY1731LckUpperThreshold_Type()
)
hwY1731LckUpperThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731LckUpperThreshold.setStatus("current")
_HwY1731LckLowerThreshold_Type = Unsigned32
_HwY1731LckLowerThreshold_Object = MibScalar
hwY1731LckLowerThreshold = _HwY1731LckLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 8, 5, 5),
    _HwY1731LckLowerThreshold_Type()
)
hwY1731LckLowerThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwY1731LckLowerThreshold.setStatus("current")
hwDot3ahEfmEntry.registerAugmentions(
    ("HUAWEI-ETHOAM-MIB",
     "hwDot3ahEfmDetectModeEntry")
)
hwDot3ahEfmDetectModeEntry.setIndexNames(*hwDot3ahEfmEntry.getIndexNames())

# Managed Objects groups

hwDot1agCfmMdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 1)
)
hwDot1agCfmMdGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdTableNextIndex"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdFormat"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdMdLevel"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdMhfCreation"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdMhfIdPermission"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdRowStatus"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmMdGroup.setStatus("current")

hwDot1agCfmMaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 2)
)
hwDot1agCfmMaGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaNextIndex"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaMapType"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaMapVlanValue"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaMapVsiName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaMapL2vcType"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaMapL2vcValue"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaPktPriority"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaRmepActiveTime"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaMepFngAlarmTime"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaMepFngResetTime"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaRowStatus"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaCcmInterval"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmMaGroup.setStatus("current")

hwDot1agCfmMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 3)
)
hwDot1agCfmMepGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIsVlanType"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIfIndex"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepDot1qVlan"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepPeVlan"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepCeVlan"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepDirection"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepCcmSendEnabled"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepRowStatus"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmMepGroup.setStatus("current")

hwDot1agCfmRMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 4)
)
hwDot1agCfmRMepGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepCcmRecvEnabled"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepStateIsUp"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepHighestPrDefect"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepRowStatus"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmRMepGroup.setStatus("current")

hwDot1agCfmMipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 5)
)
hwDot1agCfmMipGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMipLevel"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMipIfMacAddress"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmMipGroup.setStatus("current")

hwDot1agCfmMacPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 6)
)
hwDot1agCfmMacPingGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingState"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingDestIsMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingDestMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingOutIfIndex"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingTimeOut"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingCount"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingPacketSize"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingPriority"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingSendPacketNum"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingRecvPacketNum"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingPacketLossRatio"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingRecvTimeDelayMin"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingRecvTimeDelayMax"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingRecvTimeDelayAvg"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacPingRowStatus"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmMacPingGroup.setStatus("current")

hwDot1agCfmMacTraceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 7)
)
hwDot1agCfmMacTraceGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceState"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceDestIsMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceDestMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceOutIfIndex"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceTimeOut"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceTTL"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceSendSeqNumber"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceResult"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceRowStatus"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceGroup.setStatus("current")

hwDot1agCfmMacTraceReplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 8)
)
hwDot1agCfmMacTraceReplyGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyTTL"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyForwarded"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyTerminalMep"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyRelayAction"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyIngressAction"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyIngressMac"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyIngressIfName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyEgressAction"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyEgressMac"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMacTraceReplyEgressIfName"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmMacTraceReplyGroup.setStatus("current")

hwDot1agCfmQueryMdIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 9)
)
hwDot1agCfmQueryMdIndexGroup.setObjects(
    ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmQueryMdIndex")
)
if mibBuilder.loadTexts:
    hwDot1agCfmQueryMdIndexGroup.setStatus("current")

hwDot1agCfmQueryMaIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 10)
)
hwDot1agCfmQueryMaIndexGroup.setObjects(
    ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmQueryMaIndex")
)
if mibBuilder.loadTexts:
    hwDot1agCfmQueryMaIndexGroup.setStatus("current")

hwDot3ahEfmDetectModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 11)
)
hwDot3ahEfmDetectModeGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEnabled"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmDetectMode"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmDetectInterval"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmDetectMalfunction"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmDetectModeGroup.setStatus("current")

hwTestMessageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 12)
)
hwTestMessageGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwTestMessageTableNextIndex"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageInterface"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageServiceInstance"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageVlanID"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessagePacketSize"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageSendPackets"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageSendSpeed"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageSendEnabled"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageSendFinished"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageRowStatus"))
)
if mibBuilder.loadTexts:
    hwTestMessageGroup.setStatus("current")

hwTestMessageResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 13)
)
hwTestMessageResultGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwTestMessageResultSendPackets"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultReceivedPackets"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultPacketsLost"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultSendBytes"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultReceivedBytes"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultBytesLost"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageBeginTimeStamp"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageEndTimeStamp"))
)
if mibBuilder.loadTexts:
    hwTestMessageResultGroup.setStatus("current")

hwDot1agCfmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 15)
)
hwDot1agCfmGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmVersion"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmEnabled"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmGroup.setStatus("current")

hwDot3ahEfmControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 16)
)
hwDot3ahEfmControlGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmAdminState"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmOperStatus"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmMode"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmMaxOamPduSize"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmConfigRevision"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmFunctionsSupported"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmTimeout"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmInterval"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmControlGroup.setStatus("current")

hwDot3ahEfmPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 17)
)
hwDot3ahEfmPeerGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmPeerMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmPeerVendorOui"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmPeerVendorInfo"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmPeerMode"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmPeerFunctionsSupported"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmPeerMaxOamPduSize"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmPeerConfigRevision"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmPeerGroup.setStatus("current")

hwDot3ahEfmStatsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 18)
)
hwDot3ahEfmStatsBaseGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmInformationTx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmInformationRx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmUniqueEventNotificationTx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmUniqueEventNotificationRx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmDuplicateEventNotificationTx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmDuplicateEventNotificationRx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmLoopbackControlTx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmLoopbackControlRx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmVariableRequestTx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmVariableRequestRx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmVariableResponseTx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmVariableResponseRx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmOrgSpecificTx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmOrgSpecificRx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmUnsupportedCodesTx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmUnsupportedCodesRx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmFramesLostDueToOam"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmStatsBaseGroup.setStatus("current")

hwDot3ahEfmLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 19)
)
hwDot3ahEfmLoopbackGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmLoopbackStatus"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmLoopbackIgnoreRx"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmLoopbackTimeout"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackGroup.setStatus("current")

hwDot3ahEfmErrSymbolPeriodEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 20)
)
hwDot3ahEfmErrSymbolPeriodEventGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrSymPeriodWindowHi"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrSymPeriodWindowLo"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrSymPeriodThresholdHi"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrSymPeriodThresholdLo"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrSymPeriodEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmErrSymbolPeriodEventGroup.setStatus("current")

hwDot3ahEfmErrFramePeriodEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 21)
)
hwDot3ahEfmErrFramePeriodEventGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrFramePeriodWindow"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrFramePeriodThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrFramePeriodEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFramePeriodEventGroup.setStatus("current")

hwDot3ahEfmErrFrameEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 22)
)
hwDot3ahEfmErrFrameEventGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrFrameWindow"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrFrameThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrFrameEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameEventGroup.setStatus("current")

hwDot3ahEfmErrFrameSecsSummaryEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 23)
)
hwDot3ahEfmErrFrameSecsSummaryEventGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrFrameSecsSummaryWindow"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrFrameSecsSummaryThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmErrFrameSecsEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmErrFrameSecsSummaryEventGroup.setStatus("current")

hwDot3ahEfmFlagEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 24)
)
hwDot3ahEfmFlagEventGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmDyingGaspEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmCriticalEventEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmThresholdTriggerErrDown"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmFlagEventGroup.setStatus("current")

hwDot3ahEfmEventLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 25)
)
hwDot3ahEfmEventLogGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogOui"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogType"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogLocation"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogWindowHi"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogWindowLo"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogThresholdHi"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogThresholdLo"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogValue"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogRunningTotal"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmEventLogGroup.setStatus("current")

hwDot3ahEfmManagerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 26)
)
hwDot3ahEfmManagerGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmTriggerIfDown"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmHoldUpTime"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmManagerGroup.setStatus("current")

hwDot3ahEvrrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 27)
)
hwDot3ahEvrrpGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEvrrpCpuState"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEvrrpTriggerIfDown"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEvrrpHoldUpTime"))
)
if mibBuilder.loadTexts:
    hwDot3ahEvrrpGroup.setStatus("current")

hwY1731BaseConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 28)
)
hwY1731BaseConfigGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731PwMeasureMode"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayThreshold"))
)
if mibBuilder.loadTexts:
    hwY1731BaseConfigGroup.setStatus("current")

hwY1731ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 29)
)
hwY1731ConfigGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731ServiceType"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRecvEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayRecvEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayRecvEnableIsContinue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayRecvEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossIsContinue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossDestIsMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossDestMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossInterval"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossCount"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLoss8021pValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731DualLossEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731DualLossMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731DualLossDestMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayIsContinue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayDestIsMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayDestMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayInterval"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayCount"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelay8021pValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayIsContinue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayDestIsMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayDestMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayInterval"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayCount"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelay8021pValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRecv8021pValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayRecv8021pValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayRecv8021pValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRecvMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayRecvMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayRecvMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayPacketSize"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayPacketSize"))
)
if mibBuilder.loadTexts:
    hwY1731ConfigGroup.setStatus("current")

hwY1731AisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 30)
)
hwY1731AisGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731AisEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisSendLevel"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisSendInterval"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisSendPktStatus"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisSuppressEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisSuppressStatus"))
)
if mibBuilder.loadTexts:
    hwY1731AisGroup.setStatus("current")

hwY1731AisVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 31)
)
hwY1731AisVlanGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731AisPeVlan"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisLowCeVlan"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisHighCeVlan"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisLowDot1qVlan"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisHighDot1qVlan"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisRowStatus"))
)
if mibBuilder.loadTexts:
    hwY1731AisVlanGroup.setStatus("current")

hwY1731AisLinkStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 32)
)
hwY1731AisLinkStatusGroup.setObjects(
    ("HUAWEI-ETHOAM-MIB", "hwY1731AisLinkRowStatus")
)
if mibBuilder.loadTexts:
    hwY1731AisLinkStatusGroup.setStatus("current")

hwY1731MulPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 33)
)
hwY1731MulPingGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731MulPingState"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingTimeout"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingCount"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingPriority"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingSendPacketNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingRecvPacketNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingRecvTimeDelayMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingRecvTimeDelayMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingRecvTimeDelayAvg"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingRowStatus"))
)
if mibBuilder.loadTexts:
    hwY1731MulPingGroup.setStatus("current")

hwY1731MulPingReplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 34)
)
hwY1731MulPingReplyGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731MulPingReplyMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingReplyMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MulPingReplyTransTime"))
)
if mibBuilder.loadTexts:
    hwY1731MulPingReplyGroup.setStatus("current")

hwY1731ResetStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 35)
)
hwY1731ResetStatisticGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731ResetStatisticType"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731ResetStatistic8021pValue"))
)
if mibBuilder.loadTexts:
    hwY1731ResetStatisticGroup.setStatus("current")

hwY1731ManagerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 36)
)
hwY1731ManagerGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossStatisticGatherInterval"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossLocalStatistic"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossLocalRatio"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossLocalRatioMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossLocalRatioMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossLocalRatioAvg"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRemoteStatistic"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRemoteRatio"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRemoteRatioMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRemoteRatioMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRemoteRatioAvg"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayStatistic"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayVariation"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayAvg"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayStatistic"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayVariation"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayAvg"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossLocalMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossLocalMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossLocalAvg"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRemoteMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRemoteMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRemoteAvg"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayStatisticMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayStatisticMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayStatisticAvg"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayStatisticMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayStatisticMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayStatisticAvg"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayUnresponsivePacketCount"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossStatistic8021pValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayStatistic8021pValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayStatistic8021pValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731OneDelayOnDemandStartTime"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TwoDelayOnDemandStartTime"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossOnDemandStartTime"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmOneDelayTrapLogMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayTrapLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayTrapLogDelayValue"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayTrapLogDelayValueHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayTrapLogDelayValueLow"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayTrapLogThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmOneDelayRecoveryTrapMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayRecoveryTrapLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayRecoveryTrapLogDelayValue"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayRecoveryTrapLogDelayValueLow"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayRecoveryTrapLogThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmTwoDelayTrapMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayTrapLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayTrapLogDelayValue"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayTrapLogDelayValueHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayTrapLogDelayValueLow"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayTrapLogThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmTwoDelayRecoveryTrapMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayRecoveryTrapLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayRecoveryTrapLogDelayValue"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayRecoveryTrapLogThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisMaxPktNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731PMModeEnable"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731MaxTestId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckMaxPktNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckCurrentPktNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckUpperThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckLowerThreshold"))
)
if mibBuilder.loadTexts:
    hwY1731ManagerGroup.setStatus("current")

hwY1731AisVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 37)
)
hwY1731AisVlanConfigGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731AisConfigVlanListLow"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisConfigVlanListHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisVlanConfigRowStatus"))
)
if mibBuilder.loadTexts:
    hwY1731AisVlanConfigGroup.setStatus("current")

hwDot1agCfmMPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 38)
)
hwDot1agCfmMPGroup.setObjects(
    ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMPAddressModel")
)
if mibBuilder.loadTexts:
    hwDot1agCfmMPGroup.setStatus("current")

hwY1731TestIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 39)
)
hwY1731TestIdGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdLocalMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdDestIsMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdDestMepId"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdDestMepMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOnwardMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdBackwardMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdIsUpdateOnwardMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdIsUpdateBackwardMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestId8021pValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdUplink8021p"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdDownlink8021p"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdDescription"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdIsRecordFile"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdRowStatus"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdQueuePriority"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdGroup.setStatus("current")

hwY1731TestIdSingleEndedLMSendGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 40)
)
hwY1731TestIdSingleEndedLMSendGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleEndedLMSendIsContinue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleEndedLMSendInterval"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleEndedLMSendCount"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleEndedLMSendRowStatus"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMSendGroup.setStatus("current")

hwY1731TestIdSingleEndedLMReceiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 41)
)
hwY1731TestIdSingleEndedLMReceiveGroup.setObjects(
    ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleEndedLMReceiveRowStatus")
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleEndedLMReceiveGroup.setStatus("current")

hwY1731TestIdOneWayDMSendGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 42)
)
hwY1731TestIdOneWayDMSendGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneWayDMSendIsContinue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneWayDMSendInterval"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneWayDMSendCount"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneWayDMSendPacketSize"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneWayDMSendRowStatus"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMSendGroup.setStatus("current")

hwY1731TestIdOneWayDMReceiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 43)
)
hwY1731TestIdOneWayDMReceiveGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneWayDMReceiveIsContinue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneWayDMReceiveRowStatus"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdOneWayDMReceiveGroup.setStatus("current")

hwY1731TestIdTwoWayDMSendGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 44)
)
hwY1731TestIdTwoWayDMSendGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoWayDMSendIsContinue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoWayDMSendInterval"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoWayDMSendCount"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoWayDMSendPacketSize"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoWayDMSendRowStatus"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMSendGroup.setStatus("current")

hwY1731TestIdTwoWayDMReceiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 45)
)
hwY1731TestIdTwoWayDMReceiveGroup.setObjects(
    ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoWayDMReceiveRowStatus")
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoWayDMReceiveGroup.setStatus("current")

hwY1731TestIdSingleLossStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 46)
)
hwY1731TestIdSingleLossStatTableGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossSequence"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossErrInfo"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossLocalRatio"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossRemoteRatio"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossOnDemandStartTime"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossStatTableGroup.setStatus("current")

hwY1731TestIdOneDelayStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 47)
)
hwY1731TestIdOneDelayStatTableGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneDelaySequence"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneDelayErrInfo"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneDelay"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneDelayVariation"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdOneDelayOnDemandStartTime"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdOneDelayStatTableGroup.setStatus("current")

hwY1731TestIdTwoDelayStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 48)
)
hwY1731TestIdTwoDelayStatTableGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelaySequence"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayErrInfo"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelay"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayVariation"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayOnDemandStartTime"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelayStatTableGroup.setStatus("current")

hwY1731TestIdStatisticResetTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 49)
)
hwY1731TestIdStatisticResetTableGroup.setObjects(
    ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdResetStatisticType")
)
if mibBuilder.loadTexts:
    hwY1731TestIdStatisticResetTableGroup.setStatus("current")

hwY1731TestIdTwoDelaySummaryStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 50)
)
hwY1731TestIdTwoDelaySummaryStatTableGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayNbrSamples"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayAve"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayExceedUpLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayBelowLowLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayVariationNbrSamples"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayVariationMax"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayVariationMin"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayVariationAve"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayVarExceedUpLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdTwoDelayVarBelowLowLimitNum"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdTwoDelaySummaryStatTableGroup.setStatus("current")

hwY1731TestIdSingleSynLossSummaryStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 51)
)
hwY1731TestIdSingleSynLossSummaryStatTableGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossNbrSamples"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynSendRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynRecvLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynExceedLocalUpLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynBelowLocalLowLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynSendLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynRecvRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynExceedRemoteUpLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynBelowRemoteLowLimitNum"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossSummaryStatTableGroup.setStatus("current")

hwY1731SingleLossSummaryStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 52)
)
hwY1731SingleLossSummaryStatTableGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossNbrSamples"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossSendRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRecvLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossLossLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossExceedLocalUpLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossBelowLocallowLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossSendLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossRecvRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossLossRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossExceedRemoteUpLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731SingleLossBelowRemotelowLimitNum"))
)
if mibBuilder.loadTexts:
    hwY1731SingleLossSummaryStatTableGroup.setStatus("current")

hwY1731TestIdSingleSynEndedLMSendTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 53)
)
hwY1731TestIdSingleSynEndedLMSendTableGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynEndedLMSendIsContinue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynEndedLMSendInterval"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynEndedLMSendCount"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynEndedLMSendTimeOut"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynEndedLMSendRowStatus"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMSendTableGroup.setStatus("current")

hwY1731TestIdSingleSynEndedLMReceiveTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 54)
)
hwY1731TestIdSingleSynEndedLMReceiveTableGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynEndedLMReceiveTimeOut"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynEndedLMReceiveRowStatus"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynEndedLMReceiveTableGroup.setStatus("current")

hwY1731TestIdSingleLossSummaryStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 55)
)
hwY1731TestIdSingleLossSummaryStatTableGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossNbrSamples"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossSendRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossRecvLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossLossLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossExceedLocalUpLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossBelowLocallowLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossSendLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossRecvRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossLossRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossExceedRemoteUpLimitNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleLossBelowRemotelowLimitNum"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleLossSummaryStatTableGroup.setStatus("current")

hwY1731TestIdSingleSynLossStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 56)
)
hwY1731TestIdSingleSynLossStatTableGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossErrInfo"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossLocalSend"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossRemoteSend"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossLocalReceive"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossUnack"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossLossLocal"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossLocalRatio"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossLossRemote"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossRemoteRatio"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731TestIdSingleSynLossOnDemandStartTime"))
)
if mibBuilder.loadTexts:
    hwY1731TestIdSingleSynLossStatTableGroup.setStatus("current")


# Notification objects

hwDot1agCfmFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 1)
)
hwDot1agCfmFaultAlarm.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepHighestPrDefect"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdMdLevel"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmFaultAlarm.setStatus(
        "current"
    )

hwTestMessageFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 2)
)
hwTestMessageFailed.setObjects(
    ("HUAWEI-ETHOAM-MIB", "hwTestMessageSendFinished")
)
if mibBuilder.loadTexts:
    hwTestMessageFailed.setStatus(
        "obsolete"
    )

hwTestMessageCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 3)
)
hwTestMessageCompleted.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwTestMessageSendFinished"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultSendPackets"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultReceivedPackets"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultPacketsLost"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultSendBytes"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultReceivedBytes"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageResultBytesLost"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageBeginTimeStamp"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageEndTimeStamp"))
)
if mibBuilder.loadTexts:
    hwTestMessageCompleted.setStatus(
        "obsolete"
    )

hwDot3ahEfmThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 4)
)
hwDot3ahEfmThresholdEvent.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogOui"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogType"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogLocation"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogWindowHi"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogWindowLo"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogThresholdHi"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogThresholdLo"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogValue"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogRunningTotal"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmThresholdEvent.setStatus(
        "current"
    )

hwDot3ahEfmNonThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 5)
)
hwDot3ahEfmNonThresholdEvent.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogOui"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogType"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogLocation"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmNonThresholdEvent.setStatus(
        "current"
    )

hwDot3ahEfmRemoteDyingGaspEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 8)
)
hwDot3ahEfmRemoteDyingGaspEvent.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmPeerMacAddress"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmRemoteDyingGaspEvent.setStatus(
        "current"
    )

hwDot3ahEfmNonThresholdRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 17)
)
hwDot3ahEfmNonThresholdRecovery.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogOui"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogType"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmEventLogLocation"))
)
if mibBuilder.loadTexts:
    hwDot3ahEfmNonThresholdRecovery.setStatus(
        "current"
    )

hwCfmVlanOnewayDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 23)
)
hwCfmVlanOnewayDelay.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwCfmOneDelayTrapLogMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayTrapLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayTrapLogDelayValue"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayTrapLogThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayTrapLogDelayValueHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayTrapLogDelayValueLow"))
)
if mibBuilder.loadTexts:
    hwCfmVlanOnewayDelay.setStatus(
        "current"
    )

hwCfmVlanOnewayDelayRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 24)
)
hwCfmVlanOnewayDelayRecovery.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwCfmOneDelayRecoveryTrapMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayRecoveryTrapLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayRecoveryTrapLogDelayValue"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayRecoveryTrapLogThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOneDelayRecoveryTrapLogDelayValueLow"))
)
if mibBuilder.loadTexts:
    hwCfmVlanOnewayDelayRecovery.setStatus(
        "current"
    )

hwCfmVlanTwowayDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 25)
)
hwCfmVlanTwowayDelay.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwCfmTwoDelayTrapMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayTrapLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayTrapLogDelayValue"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayTrapLogThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayTrapLogDelayValueHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayTrapLogDelayValueLow"))
)
if mibBuilder.loadTexts:
    hwCfmVlanTwowayDelay.setStatus(
        "current"
    )

hwCfmVlanTwowayDelayRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 26)
)
hwCfmVlanTwowayDelayRecovery.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwCfmTwoDelayRecoveryTrapMacAddress"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayRecoveryTrapLogTimestamp"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayRecoveryTrapLogDelayValue"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayRecoveryTrapLogThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow"))
)
if mibBuilder.loadTexts:
    hwCfmVlanTwowayDelayRecovery.setStatus(
        "current"
    )

hwDot3ahEfmLoopbackFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 29)
)
hwDot3ahEfmLoopbackFailed.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    hwDot3ahEfmLoopbackFailed.setStatus(
        "current"
    )

hwY1731AisDefectAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 30)
)
hwY1731AisDefectAlarm.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwY1731AisDefectAlarm.setStatus(
        "current"
    )

hwY1731AisDefectAlarmRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 31)
)
hwY1731AisDefectAlarmRecovery.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwY1731AisDefectAlarmRecovery.setStatus(
        "current"
    )

hwDot1agCfmUnexpectedMEGLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 32)
)
hwDot1agCfmUnexpectedMEGLevel.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmUnexpectedMEGLevel.setStatus(
        "current"
    )

hwDot1agCfmUnexpectedMEGLevelCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 33)
)
hwDot1agCfmUnexpectedMEGLevelCleared.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmUnexpectedMEGLevelCleared.setStatus(
        "current"
    )

hwDot1agCfmMismerge = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 34)
)
hwDot1agCfmMismerge.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmMismerge.setStatus(
        "current"
    )

hwDot1agCfmMismergeCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 35)
)
hwDot1agCfmMismergeCleared.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmMismergeCleared.setStatus(
        "current"
    )

hwDot1agCfmUnexpectedMEP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 36)
)
hwDot1agCfmUnexpectedMEP.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmUnexpectedMEP.setStatus(
        "current"
    )

hwDot1agCfmUnexpectedMEPCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 37)
)
hwDot1agCfmUnexpectedMEPCleared.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmUnexpectedMEPCleared.setStatus(
        "current"
    )

hwDot1agCfmUnexpectedPeriod = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 38)
)
hwDot1agCfmUnexpectedPeriod.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmUnexpectedPeriod.setStatus(
        "current"
    )

hwDot1agCfmUnexpectedPeriodCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 39)
)
hwDot1agCfmUnexpectedPeriodCleared.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmUnexpectedPeriodCleared.setStatus(
        "current"
    )

hwDot1agCfmUnexpectedMAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 40)
)
hwDot1agCfmUnexpectedMAC.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmUnexpectedMAC.setStatus(
        "current"
    )

hwDot1agCfmUnexpectedMACCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 41)
)
hwDot1agCfmUnexpectedMACCleared.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmUnexpectedMACCleared.setStatus(
        "current"
    )

hwDot1agCfmLOC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 42)
)
hwDot1agCfmLOC.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmLOC.setStatus(
        "current"
    )

hwDot1agCfmLOCCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 43)
)
hwDot1agCfmLOCCleared.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmLOCCleared.setStatus(
        "current"
    )

hwDot1agCfmExceptionalMACStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 44)
)
hwDot1agCfmExceptionalMACStatus.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmExceptionalMACStatus.setStatus(
        "current"
    )

hwDot1agCfmExceptionalMACStatusCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 45)
)
hwDot1agCfmExceptionalMACStatusCleared.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmExceptionalMACStatusCleared.setStatus(
        "current"
    )

hwDot1agCfmRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 46)
)
hwDot1agCfmRDI.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmRDI.setStatus(
        "current"
    )

hwDot1agCfmRDICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 47)
)
hwDot1agCfmRDICleared.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwDot1agCfmRDICleared.setStatus(
        "current"
    )

hwY1731AisExceedMaxPktNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 48)
)
hwY1731AisExceedMaxPktNum.setObjects(
    ("HUAWEI-ETHOAM-MIB", "hwY1731AisMaxPktNum")
)
if mibBuilder.loadTexts:
    hwY1731AisExceedMaxPktNum.setStatus(
        "current"
    )

hwY1731AisExceedMaxPktNumCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 49)
)
if mibBuilder.loadTexts:
    hwY1731AisExceedMaxPktNumCleared.setStatus(
        "current"
    )

hwY1731LckDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 50)
)
hwY1731LckDefect.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwY1731LckDefect.setStatus(
        "current"
    )

hwY1731LckDefectCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 51)
)
hwY1731LckDefectCleared.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    hwY1731LckDefectCleared.setStatus(
        "current"
    )

hwY1731Statistic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 52)
)
hwY1731Statistic.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogUpperLimitThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogLowerLimitThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogValueHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogValueLow"))
)
if mibBuilder.loadTexts:
    hwY1731Statistic.setStatus(
        "current"
    )

hwY1731StatisticClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 53)
)
hwY1731StatisticClear.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMdName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMaName"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMepIdentifier"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogValue"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogUpperLimitThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogLowerLimitThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogValueHigh"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticTrapLogValueLow"))
)
if mibBuilder.loadTexts:
    hwY1731StatisticClear.setStatus(
        "current"
    )

hwY1731LckExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 54)
)
hwY1731LckExceedThreshold.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731LckMaxPktNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckCurrentPktNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckUpperThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckLowerThreshold"))
)
if mibBuilder.loadTexts:
    hwY1731LckExceedThreshold.setStatus(
        "current"
    )

hwY1731LckExceedThresholdRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 6, 55)
)
hwY1731LckExceedThresholdRecovery.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwY1731LckMaxPktNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckCurrentPktNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckUpperThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckLowerThreshold"))
)
if mibBuilder.loadTexts:
    hwY1731LckExceedThresholdRecovery.setStatus(
        "current"
    )


# Notifications groups

hwEthOamTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 2, 14)
)
hwEthOamTrapsGroup.setObjects(
      *(("HUAWEI-ETHOAM-MIB", "hwDot1agCfmFaultAlarm"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageFailed"),
        ("HUAWEI-ETHOAM-MIB", "hwTestMessageCompleted"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmThresholdEvent"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmNonThresholdEvent"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmRemoteDyingGaspEvent"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmNonThresholdRecovery"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOnewayDelay"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanOnewayDelayRecovery"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwowayDelay"),
        ("HUAWEI-ETHOAM-MIB", "hwCfmVlanTwowayDelayRecovery"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmUnexpectedMEGLevel"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmUnexpectedMEGLevelCleared"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMismerge"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmMismergeCleared"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmUnexpectedMEP"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmUnexpectedMEPCleared"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmUnexpectedPeriod"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmUnexpectedPeriodCleared"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmUnexpectedMAC"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmUnexpectedMACCleared"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmLOC"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmLOCCleared"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmExceptionalMACStatus"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmExceptionalMACStatusCleared"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRDI"),
        ("HUAWEI-ETHOAM-MIB", "hwDot1agCfmRDICleared"),
        ("HUAWEI-ETHOAM-MIB", "hwDot3ahEfmLoopbackFailed"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisDefectAlarm"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisDefectAlarmRecovery"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisExceedMaxPktNum"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731AisExceedMaxPktNumCleared"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckDefect"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckDefectCleared"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731Statistic"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731StatisticClear"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckExceedThreshold"),
        ("HUAWEI-ETHOAM-MIB", "hwY1731LckExceedThresholdRecovery"))
)
if mibBuilder.loadTexts:
    hwEthOamTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwEthOamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 136, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hwEthOamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ETHOAM-MIB",
    **{"HWDetectType": HWDetectType,
       "HWDot3Oui": HWDot3Oui,
       "HWTestMessageSendSpeed": HWTestMessageSendSpeed,
       "HWTestMessageFinishedValue": HWTestMessageFinishedValue,
       "HWDot1agCfmRelayActionFieldValue": HWDot1agCfmRelayActionFieldValue,
       "HWDot1agCfmIngressActionFieldValue": HWDot1agCfmIngressActionFieldValue,
       "HWDot1agCfmEgressActionFieldValue": HWDot1agCfmEgressActionFieldValue,
       "HWDot1agCfmHighestDefectPri": HWDot1agCfmHighestDefectPri,
       "HWDot1agCfmMDLevel": HWDot1agCfmMDLevel,
       "hwEthOam": hwEthOam,
       "hwEthOamMib": hwEthOamMib,
       "hwEthOam1ag": hwEthOam1ag,
       "hwDot1agCfmEnabled": hwDot1agCfmEnabled,
       "hwDot1agCfmVersion": hwDot1agCfmVersion,
       "hwDot1agCfmMdObject": hwDot1agCfmMdObject,
       "hwDot1agCfmMdTableNextIndex": hwDot1agCfmMdTableNextIndex,
       "hwDot1agCfmMdTable": hwDot1agCfmMdTable,
       "hwDot1agCfmMdEntry": hwDot1agCfmMdEntry,
       "hwDot1agCfmMdIndex": hwDot1agCfmMdIndex,
       "hwDot1agCfmMdFormat": hwDot1agCfmMdFormat,
       "hwDot1agCfmMdName": hwDot1agCfmMdName,
       "hwDot1agCfmMdMdLevel": hwDot1agCfmMdMdLevel,
       "hwDot1agCfmMdMhfCreation": hwDot1agCfmMdMhfCreation,
       "hwDot1agCfmMdMhfIdPermission": hwDot1agCfmMdMhfIdPermission,
       "hwDot1agCfmMdFormatName": hwDot1agCfmMdFormatName,
       "hwDot1agCfmMdRowStatus": hwDot1agCfmMdRowStatus,
       "hwDot1agCfmMaObject": hwDot1agCfmMaObject,
       "hwDot1agCfmMaNextIndex": hwDot1agCfmMaNextIndex,
       "hwDot1agCfmMaTable": hwDot1agCfmMaTable,
       "hwDot1agCfmMaEntry": hwDot1agCfmMaEntry,
       "hwDot1agCfmMaIndex": hwDot1agCfmMaIndex,
       "hwDot1agCfmMaName": hwDot1agCfmMaName,
       "hwDot1agCfmMaMapType": hwDot1agCfmMaMapType,
       "hwDot1agCfmMaMapVlanValue": hwDot1agCfmMaMapVlanValue,
       "hwDot1agCfmMaMapVsiName": hwDot1agCfmMaMapVsiName,
       "hwDot1agCfmMaMapL2vcValue": hwDot1agCfmMaMapL2vcValue,
       "hwDot1agCfmMaMapL2vcType": hwDot1agCfmMaMapL2vcType,
       "hwDot1agCfmMaPktPriority": hwDot1agCfmMaPktPriority,
       "hwDot1agCfmMaCcmInterval": hwDot1agCfmMaCcmInterval,
       "hwDot1agCfmMaRmepActiveTime": hwDot1agCfmMaRmepActiveTime,
       "hwDot1agCfmMaMepFngAlarmTime": hwDot1agCfmMaMepFngAlarmTime,
       "hwDot1agCfmMaMepFngResetTime": hwDot1agCfmMaMepFngResetTime,
       "hwDot1agCfmMaFormat": hwDot1agCfmMaFormat,
       "hwDot1agCfmMaFormatName": hwDot1agCfmMaFormatName,
       "hwDot1agCfmMaMapCccName": hwDot1agCfmMaMapCccName,
       "hwDot1agCfmMaRowStatus": hwDot1agCfmMaRowStatus,
       "hwDot1agCfmMepObject": hwDot1agCfmMepObject,
       "hwDot1agCfmMepTable": hwDot1agCfmMepTable,
       "hwDot1agCfmMepEntry": hwDot1agCfmMepEntry,
       "hwDot1agCfmMepIdentifier": hwDot1agCfmMepIdentifier,
       "hwDot1agCfmMepIsVlanType": hwDot1agCfmMepIsVlanType,
       "hwDot1agCfmMepIfIndex": hwDot1agCfmMepIfIndex,
       "hwDot1agCfmMepDot1qVlan": hwDot1agCfmMepDot1qVlan,
       "hwDot1agCfmMepPeVlan": hwDot1agCfmMepPeVlan,
       "hwDot1agCfmMepCeVlan": hwDot1agCfmMepCeVlan,
       "hwDot1agCfmMepDirection": hwDot1agCfmMepDirection,
       "hwDot1agCfmMepCcmSendEnabled": hwDot1agCfmMepCcmSendEnabled,
       "hwDot1agCfmMepMacAddress": hwDot1agCfmMepMacAddress,
       "hwDot1agCfmMepRowStatus": hwDot1agCfmMepRowStatus,
       "hwDot1agCfmRMepObject": hwDot1agCfmRMepObject,
       "hwDot1agCfmRMepTable": hwDot1agCfmRMepTable,
       "hwDot1agCfmRMepEntry": hwDot1agCfmRMepEntry,
       "hwDot1agCfmRMepIdentifier": hwDot1agCfmRMepIdentifier,
       "hwDot1agCfmRMepMacAddress": hwDot1agCfmRMepMacAddress,
       "hwDot1agCfmRMepCcmRecvEnabled": hwDot1agCfmRMepCcmRecvEnabled,
       "hwDot1agCfmRMepStateIsUp": hwDot1agCfmRMepStateIsUp,
       "hwDot1agCfmRMepHighestPrDefect": hwDot1agCfmRMepHighestPrDefect,
       "hwDot1agCfmRMepRowStatus": hwDot1agCfmRMepRowStatus,
       "hwDot1agCfmMipObject": hwDot1agCfmMipObject,
       "hwDot1agCfmMipTable": hwDot1agCfmMipTable,
       "hwDot1agCfmMipEntry": hwDot1agCfmMipEntry,
       "hwDot1agCfmMipIfIndex": hwDot1agCfmMipIfIndex,
       "hwDot1agCfmMipLevel": hwDot1agCfmMipLevel,
       "hwDot1agCfmMipIfMacAddress": hwDot1agCfmMipIfMacAddress,
       "hwDot1agCfmMacPingObject": hwDot1agCfmMacPingObject,
       "hwDot1agCfmMacPingTable": hwDot1agCfmMacPingTable,
       "hwDot1agCfmMacPingEntry": hwDot1agCfmMacPingEntry,
       "hwDot1agCfmMacPingIndex": hwDot1agCfmMacPingIndex,
       "hwDot1agCfmMacPingState": hwDot1agCfmMacPingState,
       "hwDot1agCfmMacPingMdName": hwDot1agCfmMacPingMdName,
       "hwDot1agCfmMacPingMaName": hwDot1agCfmMacPingMaName,
       "hwDot1agCfmMacPingMepId": hwDot1agCfmMacPingMepId,
       "hwDot1agCfmMacPingDestIsMepId": hwDot1agCfmMacPingDestIsMepId,
       "hwDot1agCfmMacPingDestMepId": hwDot1agCfmMacPingDestMepId,
       "hwDot1agCfmMacPingMacAddress": hwDot1agCfmMacPingMacAddress,
       "hwDot1agCfmMacPingOutIfIndex": hwDot1agCfmMacPingOutIfIndex,
       "hwDot1agCfmMacPingTimeOut": hwDot1agCfmMacPingTimeOut,
       "hwDot1agCfmMacPingCount": hwDot1agCfmMacPingCount,
       "hwDot1agCfmMacPingPacketSize": hwDot1agCfmMacPingPacketSize,
       "hwDot1agCfmMacPingPriority": hwDot1agCfmMacPingPriority,
       "hwDot1agCfmMacPingSendPacketNum": hwDot1agCfmMacPingSendPacketNum,
       "hwDot1agCfmMacPingRecvPacketNum": hwDot1agCfmMacPingRecvPacketNum,
       "hwDot1agCfmMacPingPacketLossRatio": hwDot1agCfmMacPingPacketLossRatio,
       "hwDot1agCfmMacPingRecvTimeDelayMin": hwDot1agCfmMacPingRecvTimeDelayMin,
       "hwDot1agCfmMacPingRecvTimeDelayMax": hwDot1agCfmMacPingRecvTimeDelayMax,
       "hwDot1agCfmMacPingRecvTimeDelayAvg": hwDot1agCfmMacPingRecvTimeDelayAvg,
       "hwDot1agCfmMacPingRowStatus": hwDot1agCfmMacPingRowStatus,
       "hwDot1agCfmMacTraceObjects": hwDot1agCfmMacTraceObjects,
       "hwDot1agCfmMacTraceTable": hwDot1agCfmMacTraceTable,
       "hwDot1agCfmMacTraceEntry": hwDot1agCfmMacTraceEntry,
       "hwDot1agCfmMacTraceIndex": hwDot1agCfmMacTraceIndex,
       "hwDot1agCfmMacTraceState": hwDot1agCfmMacTraceState,
       "hwDot1agCfmMacTraceMdName": hwDot1agCfmMacTraceMdName,
       "hwDot1agCfmMacTraceMaName": hwDot1agCfmMacTraceMaName,
       "hwDot1agCfmMacTraceMepId": hwDot1agCfmMacTraceMepId,
       "hwDot1agCfmMacTraceDestIsMepId": hwDot1agCfmMacTraceDestIsMepId,
       "hwDot1agCfmMacTraceDestMepId": hwDot1agCfmMacTraceDestMepId,
       "hwDot1agCfmMacTraceMacAddress": hwDot1agCfmMacTraceMacAddress,
       "hwDot1agCfmMacTraceOutIfIndex": hwDot1agCfmMacTraceOutIfIndex,
       "hwDot1agCfmMacTraceTimeOut": hwDot1agCfmMacTraceTimeOut,
       "hwDot1agCfmMacTraceTTL": hwDot1agCfmMacTraceTTL,
       "hwDot1agCfmMacTraceSendSeqNumber": hwDot1agCfmMacTraceSendSeqNumber,
       "hwDot1agCfmMacTraceResult": hwDot1agCfmMacTraceResult,
       "hwDot1agCfmMacTraceRowStatus": hwDot1agCfmMacTraceRowStatus,
       "hwDot1agCfmMacTraceReplyTable": hwDot1agCfmMacTraceReplyTable,
       "hwDot1agCfmMacTraceReplyEntry": hwDot1agCfmMacTraceReplyEntry,
       "hwDot1agCfmMacTraceReplySeqNumber": hwDot1agCfmMacTraceReplySeqNumber,
       "hwDot1agCfmMacTraceReplyRecvOrder": hwDot1agCfmMacTraceReplyRecvOrder,
       "hwDot1agCfmMacTraceReplyTTL": hwDot1agCfmMacTraceReplyTTL,
       "hwDot1agCfmMacTraceReplyForwarded": hwDot1agCfmMacTraceReplyForwarded,
       "hwDot1agCfmMacTraceReplyTerminalMep": hwDot1agCfmMacTraceReplyTerminalMep,
       "hwDot1agCfmMacTraceReplyRelayAction": hwDot1agCfmMacTraceReplyRelayAction,
       "hwDot1agCfmMacTraceReplyIngressAction": hwDot1agCfmMacTraceReplyIngressAction,
       "hwDot1agCfmMacTraceReplyIngressMac": hwDot1agCfmMacTraceReplyIngressMac,
       "hwDot1agCfmMacTraceReplyIngressIfName": hwDot1agCfmMacTraceReplyIngressIfName,
       "hwDot1agCfmMacTraceReplyEgressAction": hwDot1agCfmMacTraceReplyEgressAction,
       "hwDot1agCfmMacTraceReplyEgressMac": hwDot1agCfmMacTraceReplyEgressMac,
       "hwDot1agCfmMacTraceReplyEgressIfName": hwDot1agCfmMacTraceReplyEgressIfName,
       "hwDot1agCfmQueryObject": hwDot1agCfmQueryObject,
       "hwDot1agCfmQueryMdIndexTable": hwDot1agCfmQueryMdIndexTable,
       "hwDot1agCfmQueryMdIndexEntry": hwDot1agCfmQueryMdIndexEntry,
       "hwDot1agCfmQueryMdName": hwDot1agCfmQueryMdName,
       "hwDot1agCfmQueryMdIndex": hwDot1agCfmQueryMdIndex,
       "hwDot1agCfmQueryMaIndexTable": hwDot1agCfmQueryMaIndexTable,
       "hwDot1agCfmQueryMaIndexEntry": hwDot1agCfmQueryMaIndexEntry,
       "hwDot1agCfmQueryMaName": hwDot1agCfmQueryMaName,
       "hwDot1agCfmQueryMaIndex": hwDot1agCfmQueryMaIndex,
       "hwDot1agCfmGmacTraceObjects": hwDot1agCfmGmacTraceObjects,
       "hwDot1agCfmGmacTraceEnabled": hwDot1agCfmGmacTraceEnabled,
       "hwDot1agCfmGmacTraceTable": hwDot1agCfmGmacTraceTable,
       "hwDot1agCfmGmacTraceEntry": hwDot1agCfmGmacTraceEntry,
       "hwDot1agCfmGmacTraceIndex": hwDot1agCfmGmacTraceIndex,
       "hwDot1agCfmGmacTraceState": hwDot1agCfmGmacTraceState,
       "hwDot1agCfmGmacTraceMacAddress": hwDot1agCfmGmacTraceMacAddress,
       "hwDot1agCfmGmacTraceServiceType": hwDot1agCfmGmacTraceServiceType,
       "hwDot1agCfmGmacTraceVlanValue": hwDot1agCfmGmacTraceVlanValue,
       "hwDot1agCfmGmacTraceVsiName": hwDot1agCfmGmacTraceVsiName,
       "hwDot1agCfmGmacTraceL2vcValue": hwDot1agCfmGmacTraceL2vcValue,
       "hwDot1agCfmGmacTraceL2vcType": hwDot1agCfmGmacTraceL2vcType,
       "hwDot1agCfmGmacTraceDot1qVlan": hwDot1agCfmGmacTraceDot1qVlan,
       "hwDot1agCfmGmacTracePeVlan": hwDot1agCfmGmacTracePeVlan,
       "hwDot1agCfmGmacTraceCeVlan": hwDot1agCfmGmacTraceCeVlan,
       "hwDot1agCfmGmacTraceOutIfIndex": hwDot1agCfmGmacTraceOutIfIndex,
       "hwDot1agCfmGmacTraceTimeOut": hwDot1agCfmGmacTraceTimeOut,
       "hwDot1agCfmGmacTraceDisplayHostInfo": hwDot1agCfmGmacTraceDisplayHostInfo,
       "hwDot1agCfmGmacTraceSendSeqNumber": hwDot1agCfmGmacTraceSendSeqNumber,
       "hwDot1agCfmGmacTraceResult": hwDot1agCfmGmacTraceResult,
       "hwDot1agCfmGmacTraceRowStatus": hwDot1agCfmGmacTraceRowStatus,
       "hwDot1agCfmGmacTraceReplyTable": hwDot1agCfmGmacTraceReplyTable,
       "hwDot1agCfmGmacTraceReplyEntry": hwDot1agCfmGmacTraceReplyEntry,
       "hwDot1agCfmGmacTraceReplySeqNumber": hwDot1agCfmGmacTraceReplySeqNumber,
       "hwDot1agCfmGmacTraceReplyRecvOrder": hwDot1agCfmGmacTraceReplyRecvOrder,
       "hwDot1agCfmGmacTraceReplyTTL": hwDot1agCfmGmacTraceReplyTTL,
       "hwDot1agCfmGmacTraceReplyForwarded": hwDot1agCfmGmacTraceReplyForwarded,
       "hwDot1agCfmGmacTraceReplyHostInfo": hwDot1agCfmGmacTraceReplyHostInfo,
       "hwDot1agCfmGmacTraceReplyRelayAction": hwDot1agCfmGmacTraceReplyRelayAction,
       "hwDot1agCfmGmacTraceReplyIngressAction": hwDot1agCfmGmacTraceReplyIngressAction,
       "hwDot1agCfmGmacTraceReplyIngressMac": hwDot1agCfmGmacTraceReplyIngressMac,
       "hwDot1agCfmGmacTraceReplyIngressIfName": hwDot1agCfmGmacTraceReplyIngressIfName,
       "hwDot1agCfmGmacTraceReplyEgressAction": hwDot1agCfmGmacTraceReplyEgressAction,
       "hwDot1agCfmGmacTraceReplyEgressMac": hwDot1agCfmGmacTraceReplyEgressMac,
       "hwDot1agCfmGmacTraceReplyEgressIfName": hwDot1agCfmGmacTraceReplyEgressIfName,
       "hwDot1agCfmMPAddressModel": hwDot1agCfmMPAddressModel,
       "hwEthOam3ah": hwEthOam3ah,
       "hwDot3ahEfmEnabled": hwDot3ahEfmEnabled,
       "hwDot3ahEfmObject": hwDot3ahEfmObject,
       "hwDot3ahEfmDetectModeTable": hwDot3ahEfmDetectModeTable,
       "hwDot3ahEfmDetectModeEntry": hwDot3ahEfmDetectModeEntry,
       "hwDot3ahEfmDetectMode": hwDot3ahEfmDetectMode,
       "hwDot3ahEfmDetectInterval": hwDot3ahEfmDetectInterval,
       "hwDot3ahEfmDetectMalfunction": hwDot3ahEfmDetectMalfunction,
       "hwDot3ahEfmTable": hwDot3ahEfmTable,
       "hwDot3ahEfmEntry": hwDot3ahEfmEntry,
       "hwDot3ahEfmAdminState": hwDot3ahEfmAdminState,
       "hwDot3ahEfmOperStatus": hwDot3ahEfmOperStatus,
       "hwDot3ahEfmMode": hwDot3ahEfmMode,
       "hwDot3ahEfmMaxOamPduSize": hwDot3ahEfmMaxOamPduSize,
       "hwDot3ahEfmConfigRevision": hwDot3ahEfmConfigRevision,
       "hwDot3ahEfmFunctionsSupported": hwDot3ahEfmFunctionsSupported,
       "hwDot3ahEfmTimeout": hwDot3ahEfmTimeout,
       "hwDot3ahEfmInterval": hwDot3ahEfmInterval,
       "hwDot3ahEfmPeerTable": hwDot3ahEfmPeerTable,
       "hwDot3ahEfmPeerEntry": hwDot3ahEfmPeerEntry,
       "hwDot3ahEfmPeerMacAddress": hwDot3ahEfmPeerMacAddress,
       "hwDot3ahEfmPeerVendorOui": hwDot3ahEfmPeerVendorOui,
       "hwDot3ahEfmPeerVendorInfo": hwDot3ahEfmPeerVendorInfo,
       "hwDot3ahEfmPeerMode": hwDot3ahEfmPeerMode,
       "hwDot3ahEfmPeerMaxOamPduSize": hwDot3ahEfmPeerMaxOamPduSize,
       "hwDot3ahEfmPeerConfigRevision": hwDot3ahEfmPeerConfigRevision,
       "hwDot3ahEfmPeerFunctionsSupported": hwDot3ahEfmPeerFunctionsSupported,
       "hwDot3ahEfmLoopbackTable": hwDot3ahEfmLoopbackTable,
       "hwDot3ahEfmLoopbackEntry": hwDot3ahEfmLoopbackEntry,
       "hwDot3ahEfmLoopbackStatus": hwDot3ahEfmLoopbackStatus,
       "hwDot3ahEfmLoopbackIgnoreRx": hwDot3ahEfmLoopbackIgnoreRx,
       "hwDot3ahEfmLoopbackTimeout": hwDot3ahEfmLoopbackTimeout,
       "hwDot3ahEfmStatsTable": hwDot3ahEfmStatsTable,
       "hwDot3ahEfmStatsEntry": hwDot3ahEfmStatsEntry,
       "hwDot3ahEfmInformationTx": hwDot3ahEfmInformationTx,
       "hwDot3ahEfmInformationRx": hwDot3ahEfmInformationRx,
       "hwDot3ahEfmUniqueEventNotificationTx": hwDot3ahEfmUniqueEventNotificationTx,
       "hwDot3ahEfmUniqueEventNotificationRx": hwDot3ahEfmUniqueEventNotificationRx,
       "hwDot3ahEfmDuplicateEventNotificationTx": hwDot3ahEfmDuplicateEventNotificationTx,
       "hwDot3ahEfmDuplicateEventNotificationRx": hwDot3ahEfmDuplicateEventNotificationRx,
       "hwDot3ahEfmLoopbackControlTx": hwDot3ahEfmLoopbackControlTx,
       "hwDot3ahEfmLoopbackControlRx": hwDot3ahEfmLoopbackControlRx,
       "hwDot3ahEfmVariableRequestTx": hwDot3ahEfmVariableRequestTx,
       "hwDot3ahEfmVariableRequestRx": hwDot3ahEfmVariableRequestRx,
       "hwDot3ahEfmVariableResponseTx": hwDot3ahEfmVariableResponseTx,
       "hwDot3ahEfmVariableResponseRx": hwDot3ahEfmVariableResponseRx,
       "hwDot3ahEfmOrgSpecificTx": hwDot3ahEfmOrgSpecificTx,
       "hwDot3ahEfmOrgSpecificRx": hwDot3ahEfmOrgSpecificRx,
       "hwDot3ahEfmUnsupportedCodesTx": hwDot3ahEfmUnsupportedCodesTx,
       "hwDot3ahEfmUnsupportedCodesRx": hwDot3ahEfmUnsupportedCodesRx,
       "hwDot3ahEfmFramesLostDueToOam": hwDot3ahEfmFramesLostDueToOam,
       "hwDot3ahEfmEventConfigTable": hwDot3ahEfmEventConfigTable,
       "hwDot3ahEfmEventConfigEntry": hwDot3ahEfmEventConfigEntry,
       "hwDot3ahEfmErrSymPeriodWindowHi": hwDot3ahEfmErrSymPeriodWindowHi,
       "hwDot3ahEfmErrSymPeriodWindowLo": hwDot3ahEfmErrSymPeriodWindowLo,
       "hwDot3ahEfmErrSymPeriodThresholdHi": hwDot3ahEfmErrSymPeriodThresholdHi,
       "hwDot3ahEfmErrSymPeriodThresholdLo": hwDot3ahEfmErrSymPeriodThresholdLo,
       "hwDot3ahEfmErrSymPeriodEvNotifEnable": hwDot3ahEfmErrSymPeriodEvNotifEnable,
       "hwDot3ahEfmErrFramePeriodWindow": hwDot3ahEfmErrFramePeriodWindow,
       "hwDot3ahEfmErrFramePeriodThreshold": hwDot3ahEfmErrFramePeriodThreshold,
       "hwDot3ahEfmErrFramePeriodEvNotifEnable": hwDot3ahEfmErrFramePeriodEvNotifEnable,
       "hwDot3ahEfmErrFrameWindow": hwDot3ahEfmErrFrameWindow,
       "hwDot3ahEfmErrFrameThreshold": hwDot3ahEfmErrFrameThreshold,
       "hwDot3ahEfmErrFrameEvNotifEnable": hwDot3ahEfmErrFrameEvNotifEnable,
       "hwDot3ahEfmErrFrameSecsSummaryWindow": hwDot3ahEfmErrFrameSecsSummaryWindow,
       "hwDot3ahEfmErrFrameSecsSummaryThreshold": hwDot3ahEfmErrFrameSecsSummaryThreshold,
       "hwDot3ahEfmErrFrameSecsEvNotifEnable": hwDot3ahEfmErrFrameSecsEvNotifEnable,
       "hwDot3ahEfmDyingGaspEnable": hwDot3ahEfmDyingGaspEnable,
       "hwDot3ahEfmCriticalEventEnable": hwDot3ahEfmCriticalEventEnable,
       "hwDot3ahEfmThresholdTriggerErrDown": hwDot3ahEfmThresholdTriggerErrDown,
       "hwDot3ahEfmEventLogTable": hwDot3ahEfmEventLogTable,
       "hwDot3ahEfmEventLogEntry": hwDot3ahEfmEventLogEntry,
       "hwDot3ahEfmEventLogIndex": hwDot3ahEfmEventLogIndex,
       "hwDot3ahEfmEventLogTimestamp": hwDot3ahEfmEventLogTimestamp,
       "hwDot3ahEfmEventLogOui": hwDot3ahEfmEventLogOui,
       "hwDot3ahEfmEventLogType": hwDot3ahEfmEventLogType,
       "hwDot3ahEfmEventLogLocation": hwDot3ahEfmEventLogLocation,
       "hwDot3ahEfmEventLogWindowHi": hwDot3ahEfmEventLogWindowHi,
       "hwDot3ahEfmEventLogWindowLo": hwDot3ahEfmEventLogWindowLo,
       "hwDot3ahEfmEventLogThresholdHi": hwDot3ahEfmEventLogThresholdHi,
       "hwDot3ahEfmEventLogThresholdLo": hwDot3ahEfmEventLogThresholdLo,
       "hwDot3ahEfmEventLogValue": hwDot3ahEfmEventLogValue,
       "hwDot3ahEfmEventLogRunningTotal": hwDot3ahEfmEventLogRunningTotal,
       "hwDot3ahEfmEventLogEventTotal": hwDot3ahEfmEventLogEventTotal,
       "hwDot3ahEfmManagerTable": hwDot3ahEfmManagerTable,
       "hwDot3ahEfmManagerEntry": hwDot3ahEfmManagerEntry,
       "hwDot3ahEfmTriggerIfDown": hwDot3ahEfmTriggerIfDown,
       "hwDot3ahEfmHoldUpTime": hwDot3ahEfmHoldUpTime,
       "hwDot3ahEvrrpTable": hwDot3ahEvrrpTable,
       "hwDot3ahEvrrpEntry": hwDot3ahEvrrpEntry,
       "hwDot3ahEvrrpCpuState": hwDot3ahEvrrpCpuState,
       "hwDot3ahEvrrpTriggerIfDown": hwDot3ahEvrrpTriggerIfDown,
       "hwDot3ahEvrrpHoldUpTime": hwDot3ahEvrrpHoldUpTime,
       "hwOamManager": hwOamManager,
       "hwTestMessage": hwTestMessage,
       "hwTestMessageObject": hwTestMessageObject,
       "hwTestMessageTableNextIndex": hwTestMessageTableNextIndex,
       "hwTestMessageTable": hwTestMessageTable,
       "hwTestMessageEntry": hwTestMessageEntry,
       "hwTestMessageIndex": hwTestMessageIndex,
       "hwTestMessageMacAddress": hwTestMessageMacAddress,
       "hwTestMessageVlanID": hwTestMessageVlanID,
       "hwTestMessageInterface": hwTestMessageInterface,
       "hwTestMessageServiceInstance": hwTestMessageServiceInstance,
       "hwTestMessagePacketSize": hwTestMessagePacketSize,
       "hwTestMessageSendPackets": hwTestMessageSendPackets,
       "hwTestMessageSendSpeed": hwTestMessageSendSpeed,
       "hwTestMessageSendEnabled": hwTestMessageSendEnabled,
       "hwTestMessageSendFinished": hwTestMessageSendFinished,
       "hwTestMessageRowStatus": hwTestMessageRowStatus,
       "hwTestMessageResultTable": hwTestMessageResultTable,
       "hwTestMessageResultEntry": hwTestMessageResultEntry,
       "hwTestMessageResultSendPackets": hwTestMessageResultSendPackets,
       "hwTestMessageResultReceivedPackets": hwTestMessageResultReceivedPackets,
       "hwTestMessageResultPacketsLost": hwTestMessageResultPacketsLost,
       "hwTestMessageResultSendBytes": hwTestMessageResultSendBytes,
       "hwTestMessageResultReceivedBytes": hwTestMessageResultReceivedBytes,
       "hwTestMessageResultBytesLost": hwTestMessageResultBytesLost,
       "hwTestMessageBeginTimeStamp": hwTestMessageBeginTimeStamp,
       "hwTestMessageEndTimeStamp": hwTestMessageEndTimeStamp,
       "hwEthOamTraps": hwEthOamTraps,
       "hwDot1agCfmFaultAlarm": hwDot1agCfmFaultAlarm,
       "hwTestMessageFailed": hwTestMessageFailed,
       "hwTestMessageCompleted": hwTestMessageCompleted,
       "hwDot3ahEfmThresholdEvent": hwDot3ahEfmThresholdEvent,
       "hwDot3ahEfmNonThresholdEvent": hwDot3ahEfmNonThresholdEvent,
       "hwDot3ahEfmRemoteDyingGaspEvent": hwDot3ahEfmRemoteDyingGaspEvent,
       "hwDot3ahEfmNonThresholdRecovery": hwDot3ahEfmNonThresholdRecovery,
       "hwCfmVlanOnewayDelay": hwCfmVlanOnewayDelay,
       "hwCfmVlanOnewayDelayRecovery": hwCfmVlanOnewayDelayRecovery,
       "hwCfmVlanTwowayDelay": hwCfmVlanTwowayDelay,
       "hwCfmVlanTwowayDelayRecovery": hwCfmVlanTwowayDelayRecovery,
       "hwDot3ahEfmLoopbackFailed": hwDot3ahEfmLoopbackFailed,
       "hwY1731AisDefectAlarm": hwY1731AisDefectAlarm,
       "hwY1731AisDefectAlarmRecovery": hwY1731AisDefectAlarmRecovery,
       "hwDot1agCfmUnexpectedMEGLevel": hwDot1agCfmUnexpectedMEGLevel,
       "hwDot1agCfmUnexpectedMEGLevelCleared": hwDot1agCfmUnexpectedMEGLevelCleared,
       "hwDot1agCfmMismerge": hwDot1agCfmMismerge,
       "hwDot1agCfmMismergeCleared": hwDot1agCfmMismergeCleared,
       "hwDot1agCfmUnexpectedMEP": hwDot1agCfmUnexpectedMEP,
       "hwDot1agCfmUnexpectedMEPCleared": hwDot1agCfmUnexpectedMEPCleared,
       "hwDot1agCfmUnexpectedPeriod": hwDot1agCfmUnexpectedPeriod,
       "hwDot1agCfmUnexpectedPeriodCleared": hwDot1agCfmUnexpectedPeriodCleared,
       "hwDot1agCfmUnexpectedMAC": hwDot1agCfmUnexpectedMAC,
       "hwDot1agCfmUnexpectedMACCleared": hwDot1agCfmUnexpectedMACCleared,
       "hwDot1agCfmLOC": hwDot1agCfmLOC,
       "hwDot1agCfmLOCCleared": hwDot1agCfmLOCCleared,
       "hwDot1agCfmExceptionalMACStatus": hwDot1agCfmExceptionalMACStatus,
       "hwDot1agCfmExceptionalMACStatusCleared": hwDot1agCfmExceptionalMACStatusCleared,
       "hwDot1agCfmRDI": hwDot1agCfmRDI,
       "hwDot1agCfmRDICleared": hwDot1agCfmRDICleared,
       "hwY1731AisExceedMaxPktNum": hwY1731AisExceedMaxPktNum,
       "hwY1731AisExceedMaxPktNumCleared": hwY1731AisExceedMaxPktNumCleared,
       "hwY1731LckDefect": hwY1731LckDefect,
       "hwY1731LckDefectCleared": hwY1731LckDefectCleared,
       "hwY1731Statistic": hwY1731Statistic,
       "hwY1731StatisticClear": hwY1731StatisticClear,
       "hwY1731LckExceedThreshold": hwY1731LckExceedThreshold,
       "hwY1731LckExceedThresholdRecovery": hwY1731LckExceedThresholdRecovery,
       "hwEthOamConformance": hwEthOamConformance,
       "hwEthOamCompliances": hwEthOamCompliances,
       "hwEthOamCompliance": hwEthOamCompliance,
       "hwEthOamGroups": hwEthOamGroups,
       "hwDot1agCfmMdGroup": hwDot1agCfmMdGroup,
       "hwDot1agCfmMaGroup": hwDot1agCfmMaGroup,
       "hwDot1agCfmMepGroup": hwDot1agCfmMepGroup,
       "hwDot1agCfmRMepGroup": hwDot1agCfmRMepGroup,
       "hwDot1agCfmMipGroup": hwDot1agCfmMipGroup,
       "hwDot1agCfmMacPingGroup": hwDot1agCfmMacPingGroup,
       "hwDot1agCfmMacTraceGroup": hwDot1agCfmMacTraceGroup,
       "hwDot1agCfmMacTraceReplyGroup": hwDot1agCfmMacTraceReplyGroup,
       "hwDot1agCfmQueryMdIndexGroup": hwDot1agCfmQueryMdIndexGroup,
       "hwDot1agCfmQueryMaIndexGroup": hwDot1agCfmQueryMaIndexGroup,
       "hwDot3ahEfmDetectModeGroup": hwDot3ahEfmDetectModeGroup,
       "hwTestMessageGroup": hwTestMessageGroup,
       "hwTestMessageResultGroup": hwTestMessageResultGroup,
       "hwEthOamTrapsGroup": hwEthOamTrapsGroup,
       "hwDot1agCfmGroup": hwDot1agCfmGroup,
       "hwDot3ahEfmControlGroup": hwDot3ahEfmControlGroup,
       "hwDot3ahEfmPeerGroup": hwDot3ahEfmPeerGroup,
       "hwDot3ahEfmStatsBaseGroup": hwDot3ahEfmStatsBaseGroup,
       "hwDot3ahEfmLoopbackGroup": hwDot3ahEfmLoopbackGroup,
       "hwDot3ahEfmErrSymbolPeriodEventGroup": hwDot3ahEfmErrSymbolPeriodEventGroup,
       "hwDot3ahEfmErrFramePeriodEventGroup": hwDot3ahEfmErrFramePeriodEventGroup,
       "hwDot3ahEfmErrFrameEventGroup": hwDot3ahEfmErrFrameEventGroup,
       "hwDot3ahEfmErrFrameSecsSummaryEventGroup": hwDot3ahEfmErrFrameSecsSummaryEventGroup,
       "hwDot3ahEfmFlagEventGroup": hwDot3ahEfmFlagEventGroup,
       "hwDot3ahEfmEventLogGroup": hwDot3ahEfmEventLogGroup,
       "hwDot3ahEfmManagerGroup": hwDot3ahEfmManagerGroup,
       "hwDot3ahEvrrpGroup": hwDot3ahEvrrpGroup,
       "hwY1731BaseConfigGroup": hwY1731BaseConfigGroup,
       "hwY1731ConfigGroup": hwY1731ConfigGroup,
       "hwY1731AisGroup": hwY1731AisGroup,
       "hwY1731AisVlanGroup": hwY1731AisVlanGroup,
       "hwY1731AisLinkStatusGroup": hwY1731AisLinkStatusGroup,
       "hwY1731MulPingGroup": hwY1731MulPingGroup,
       "hwY1731MulPingReplyGroup": hwY1731MulPingReplyGroup,
       "hwY1731ResetStatisticGroup": hwY1731ResetStatisticGroup,
       "hwY1731ManagerGroup": hwY1731ManagerGroup,
       "hwY1731AisVlanConfigGroup": hwY1731AisVlanConfigGroup,
       "hwDot1agCfmMPGroup": hwDot1agCfmMPGroup,
       "hwY1731TestIdGroup": hwY1731TestIdGroup,
       "hwY1731TestIdSingleEndedLMSendGroup": hwY1731TestIdSingleEndedLMSendGroup,
       "hwY1731TestIdSingleEndedLMReceiveGroup": hwY1731TestIdSingleEndedLMReceiveGroup,
       "hwY1731TestIdOneWayDMSendGroup": hwY1731TestIdOneWayDMSendGroup,
       "hwY1731TestIdOneWayDMReceiveGroup": hwY1731TestIdOneWayDMReceiveGroup,
       "hwY1731TestIdTwoWayDMSendGroup": hwY1731TestIdTwoWayDMSendGroup,
       "hwY1731TestIdTwoWayDMReceiveGroup": hwY1731TestIdTwoWayDMReceiveGroup,
       "hwY1731TestIdSingleLossStatTableGroup": hwY1731TestIdSingleLossStatTableGroup,
       "hwY1731TestIdOneDelayStatTableGroup": hwY1731TestIdOneDelayStatTableGroup,
       "hwY1731TestIdTwoDelayStatTableGroup": hwY1731TestIdTwoDelayStatTableGroup,
       "hwY1731TestIdStatisticResetTableGroup": hwY1731TestIdStatisticResetTableGroup,
       "hwY1731TestIdTwoDelaySummaryStatTableGroup": hwY1731TestIdTwoDelaySummaryStatTableGroup,
       "hwY1731TestIdSingleSynLossSummaryStatTableGroup": hwY1731TestIdSingleSynLossSummaryStatTableGroup,
       "hwY1731SingleLossSummaryStatTableGroup": hwY1731SingleLossSummaryStatTableGroup,
       "hwY1731TestIdSingleSynEndedLMSendTableGroup": hwY1731TestIdSingleSynEndedLMSendTableGroup,
       "hwY1731TestIdSingleSynEndedLMReceiveTableGroup": hwY1731TestIdSingleSynEndedLMReceiveTableGroup,
       "hwY1731TestIdSingleLossSummaryStatTableGroup": hwY1731TestIdSingleLossSummaryStatTableGroup,
       "hwY1731TestIdSingleSynLossStatTableGroup": hwY1731TestIdSingleSynLossStatTableGroup,
       "hwEthOamY1731": hwEthOamY1731,
       "hwY1731ConfigObject": hwY1731ConfigObject,
       "hwY1731BaseConfigTable": hwY1731BaseConfigTable,
       "hwY1731BaseConfigEntry": hwY1731BaseConfigEntry,
       "hwY1731PwMeasureMode": hwY1731PwMeasureMode,
       "hwY1731OneDelayThreshold": hwY1731OneDelayThreshold,
       "hwY1731TwoDelayThreshold": hwY1731TwoDelayThreshold,
       "hwY1731ConfigTable": hwY1731ConfigTable,
       "hwY1731ConfigEntry": hwY1731ConfigEntry,
       "hwY1731RemoteIp": hwY1731RemoteIp,
       "hwY1731VcId": hwY1731VcId,
       "hwY1731MacAddress": hwY1731MacAddress,
       "hwY1731ResvIndex": hwY1731ResvIndex,
       "hwY1731ServiceType": hwY1731ServiceType,
       "hwY1731SingleLossRecvEnable": hwY1731SingleLossRecvEnable,
       "hwY1731OneDelayRecvEnable": hwY1731OneDelayRecvEnable,
       "hwY1731OneDelayRecvEnableIsContinue": hwY1731OneDelayRecvEnableIsContinue,
       "hwY1731TwoDelayRecvEnable": hwY1731TwoDelayRecvEnable,
       "hwY1731SingleLossEnable": hwY1731SingleLossEnable,
       "hwY1731SingleLossIsContinue": hwY1731SingleLossIsContinue,
       "hwY1731SingleLossMepId": hwY1731SingleLossMepId,
       "hwY1731SingleLossDestIsMepId": hwY1731SingleLossDestIsMepId,
       "hwY1731SingleLossDestMepId": hwY1731SingleLossDestMepId,
       "hwY1731SingleLossMacAddress": hwY1731SingleLossMacAddress,
       "hwY1731SingleLossInterval": hwY1731SingleLossInterval,
       "hwY1731SingleLossCount": hwY1731SingleLossCount,
       "hwY1731SingleLoss8021pValue": hwY1731SingleLoss8021pValue,
       "hwY1731DualLossEnable": hwY1731DualLossEnable,
       "hwY1731DualLossMepId": hwY1731DualLossMepId,
       "hwY1731DualLossDestMepId": hwY1731DualLossDestMepId,
       "hwY1731OneDelayEnable": hwY1731OneDelayEnable,
       "hwY1731OneDelayIsContinue": hwY1731OneDelayIsContinue,
       "hwY1731OneDelayMepId": hwY1731OneDelayMepId,
       "hwY1731OneDelayDestIsMepId": hwY1731OneDelayDestIsMepId,
       "hwY1731OneDelayDestMepId": hwY1731OneDelayDestMepId,
       "hwY1731OneDelayMacAddress": hwY1731OneDelayMacAddress,
       "hwY1731OneDelayInterval": hwY1731OneDelayInterval,
       "hwY1731OneDelayCount": hwY1731OneDelayCount,
       "hwY1731OneDelay8021pValue": hwY1731OneDelay8021pValue,
       "hwY1731TwoDelayEnable": hwY1731TwoDelayEnable,
       "hwY1731TwoDelayIsContinue": hwY1731TwoDelayIsContinue,
       "hwY1731TwoDelayMepId": hwY1731TwoDelayMepId,
       "hwY1731TwoDelayDestIsMepId": hwY1731TwoDelayDestIsMepId,
       "hwY1731TwoDelayDestMepId": hwY1731TwoDelayDestMepId,
       "hwY1731TwoDelayMacAddress": hwY1731TwoDelayMacAddress,
       "hwY1731TwoDelayInterval": hwY1731TwoDelayInterval,
       "hwY1731TwoDelayCount": hwY1731TwoDelayCount,
       "hwY1731TwoDelay8021pValue": hwY1731TwoDelay8021pValue,
       "hwY1731SingleLossRecv8021pValue": hwY1731SingleLossRecv8021pValue,
       "hwY1731OneDelayRecv8021pValue": hwY1731OneDelayRecv8021pValue,
       "hwY1731TwoDelayRecv8021pValue": hwY1731TwoDelayRecv8021pValue,
       "hwY1731SingleLossRecvMepId": hwY1731SingleLossRecvMepId,
       "hwY1731OneDelayRecvMepId": hwY1731OneDelayRecvMepId,
       "hwY1731TwoDelayRecvMepId": hwY1731TwoDelayRecvMepId,
       "hwY1731OneDelayPacketSize": hwY1731OneDelayPacketSize,
       "hwY1731TwoDelayPacketSize": hwY1731TwoDelayPacketSize,
       "hwY1731AisTable": hwY1731AisTable,
       "hwY1731AisEntry": hwY1731AisEntry,
       "hwY1731AisEnable": hwY1731AisEnable,
       "hwY1731AisSendLevel": hwY1731AisSendLevel,
       "hwY1731AisSendInterval": hwY1731AisSendInterval,
       "hwY1731AisSendPktStatus": hwY1731AisSendPktStatus,
       "hwY1731AisSuppressEnable": hwY1731AisSuppressEnable,
       "hwY1731AisSuppressStatus": hwY1731AisSuppressStatus,
       "hwY1731AisVlanTable": hwY1731AisVlanTable,
       "hwY1731AisVlanEntry": hwY1731AisVlanEntry,
       "hwY1731AisPeVlan": hwY1731AisPeVlan,
       "hwY1731AisLowCeVlan": hwY1731AisLowCeVlan,
       "hwY1731AisHighCeVlan": hwY1731AisHighCeVlan,
       "hwY1731AisLowDot1qVlan": hwY1731AisLowDot1qVlan,
       "hwY1731AisHighDot1qVlan": hwY1731AisHighDot1qVlan,
       "hwY1731AisRowStatus": hwY1731AisRowStatus,
       "hwY1731AisLinkStatusTable": hwY1731AisLinkStatusTable,
       "hwY1731AisLinkStatusEntry": hwY1731AisLinkStatusEntry,
       "hwY1731AisLinkStatusIfIndex": hwY1731AisLinkStatusIfIndex,
       "hwY1731AisLinkRowStatus": hwY1731AisLinkRowStatus,
       "hwY1731MulPingTable": hwY1731MulPingTable,
       "hwY1731MulPingEntry": hwY1731MulPingEntry,
       "hwY1731MulPingIndex": hwY1731MulPingIndex,
       "hwY1731MulPingState": hwY1731MulPingState,
       "hwY1731MulPingMdName": hwY1731MulPingMdName,
       "hwY1731MulPingMaName": hwY1731MulPingMaName,
       "hwY1731MulPingMepId": hwY1731MulPingMepId,
       "hwY1731MulPingTimeout": hwY1731MulPingTimeout,
       "hwY1731MulPingCount": hwY1731MulPingCount,
       "hwY1731MulPingPriority": hwY1731MulPingPriority,
       "hwY1731MulPingSendPacketNum": hwY1731MulPingSendPacketNum,
       "hwY1731MulPingRecvPacketNum": hwY1731MulPingRecvPacketNum,
       "hwY1731MulPingRecvTimeDelayMin": hwY1731MulPingRecvTimeDelayMin,
       "hwY1731MulPingRecvTimeDelayMax": hwY1731MulPingRecvTimeDelayMax,
       "hwY1731MulPingRecvTimeDelayAvg": hwY1731MulPingRecvTimeDelayAvg,
       "hwY1731MulPingRowStatus": hwY1731MulPingRowStatus,
       "hwY1731MulPingReplyTable": hwY1731MulPingReplyTable,
       "hwY1731MulPingReplyEntry": hwY1731MulPingReplyEntry,
       "hwY1731MulPingReplySeqNumber": hwY1731MulPingReplySeqNumber,
       "hwY1731MulPingReplyOrder": hwY1731MulPingReplyOrder,
       "hwY1731MulPingReplyMepId": hwY1731MulPingReplyMepId,
       "hwY1731MulPingReplyMacAddress": hwY1731MulPingReplyMacAddress,
       "hwY1731MulPingReplyTransTime": hwY1731MulPingReplyTransTime,
       "hwY1731AisVlanConfigTable": hwY1731AisVlanConfigTable,
       "hwY1731AisVlanConfigEntry": hwY1731AisVlanConfigEntry,
       "hwY1731AisConfigPeVlan": hwY1731AisConfigPeVlan,
       "hwY1731AisConfigVlanListLow": hwY1731AisConfigVlanListLow,
       "hwY1731AisConfigVlanListHigh": hwY1731AisConfigVlanListHigh,
       "hwY1731AisVlanConfigRowStatus": hwY1731AisVlanConfigRowStatus,
       "hwY1731TestIdTable": hwY1731TestIdTable,
       "hwY1731TestIdEntry": hwY1731TestIdEntry,
       "hwY1731TestIdentifier": hwY1731TestIdentifier,
       "hwY1731TestIdMdName": hwY1731TestIdMdName,
       "hwY1731TestIdMaName": hwY1731TestIdMaName,
       "hwY1731TestIdLocalMepId": hwY1731TestIdLocalMepId,
       "hwY1731TestIdDestIsMepId": hwY1731TestIdDestIsMepId,
       "hwY1731TestIdDestMepId": hwY1731TestIdDestMepId,
       "hwY1731TestIdDestMepMacAddress": hwY1731TestIdDestMepMacAddress,
       "hwY1731TestIdOnwardMacAddress": hwY1731TestIdOnwardMacAddress,
       "hwY1731TestIdBackwardMacAddress": hwY1731TestIdBackwardMacAddress,
       "hwY1731TestIdIsUpdateOnwardMacAddress": hwY1731TestIdIsUpdateOnwardMacAddress,
       "hwY1731TestIdIsUpdateBackwardMacAddress": hwY1731TestIdIsUpdateBackwardMacAddress,
       "hwY1731TestId8021pValue": hwY1731TestId8021pValue,
       "hwY1731TestIdUplink8021p": hwY1731TestIdUplink8021p,
       "hwY1731TestIdDownlink8021p": hwY1731TestIdDownlink8021p,
       "hwY1731TestIdDescription": hwY1731TestIdDescription,
       "hwY1731TestIdIsRecordFile": hwY1731TestIdIsRecordFile,
       "hwY1731TestIdQueuePriority": hwY1731TestIdQueuePriority,
       "hwY1731TestIdRowStatus": hwY1731TestIdRowStatus,
       "hwY1731TestIdSingleEndedLMSendTable": hwY1731TestIdSingleEndedLMSendTable,
       "hwY1731TestIdSingleEndedLMSendEntry": hwY1731TestIdSingleEndedLMSendEntry,
       "hwY1731TestIdSingleEndedLMSendIsContinue": hwY1731TestIdSingleEndedLMSendIsContinue,
       "hwY1731TestIdSingleEndedLMSendInterval": hwY1731TestIdSingleEndedLMSendInterval,
       "hwY1731TestIdSingleEndedLMSendCount": hwY1731TestIdSingleEndedLMSendCount,
       "hwY1731TestIdSingleEndedLMSendRowStatus": hwY1731TestIdSingleEndedLMSendRowStatus,
       "hwY1731TestIdSingleEndedLMReceiveTable": hwY1731TestIdSingleEndedLMReceiveTable,
       "hwY1731TestIdSingleEndedLMReceiveEntry": hwY1731TestIdSingleEndedLMReceiveEntry,
       "hwY1731TestIdSingleEndedLMReceiveRowStatus": hwY1731TestIdSingleEndedLMReceiveRowStatus,
       "hwY1731TestIdOneWayDMSendTable": hwY1731TestIdOneWayDMSendTable,
       "hwY1731TestIdOneWayDMSendEntry": hwY1731TestIdOneWayDMSendEntry,
       "hwY1731TestIdOneWayDMSendIsContinue": hwY1731TestIdOneWayDMSendIsContinue,
       "hwY1731TestIdOneWayDMSendInterval": hwY1731TestIdOneWayDMSendInterval,
       "hwY1731TestIdOneWayDMSendCount": hwY1731TestIdOneWayDMSendCount,
       "hwY1731TestIdOneWayDMSendPacketSize": hwY1731TestIdOneWayDMSendPacketSize,
       "hwY1731TestIdOneWayDMSendRowStatus": hwY1731TestIdOneWayDMSendRowStatus,
       "hwY1731TestIdOneWayDMReceiveTable": hwY1731TestIdOneWayDMReceiveTable,
       "hwY1731TestIdOneWayDMReceiveEntry": hwY1731TestIdOneWayDMReceiveEntry,
       "hwY1731TestIdOneWayDMReceiveIsContinue": hwY1731TestIdOneWayDMReceiveIsContinue,
       "hwY1731TestIdOneWayDMReceiveRowStatus": hwY1731TestIdOneWayDMReceiveRowStatus,
       "hwY1731TestIdTwoWayDMSendTable": hwY1731TestIdTwoWayDMSendTable,
       "hwY1731TestIdTwoWayDMSendEntry": hwY1731TestIdTwoWayDMSendEntry,
       "hwY1731TestIdTwoWayDMSendIsContinue": hwY1731TestIdTwoWayDMSendIsContinue,
       "hwY1731TestIdTwoWayDMSendInterval": hwY1731TestIdTwoWayDMSendInterval,
       "hwY1731TestIdTwoWayDMSendCount": hwY1731TestIdTwoWayDMSendCount,
       "hwY1731TestIdTwoWayDMSendPacketSize": hwY1731TestIdTwoWayDMSendPacketSize,
       "hwY1731TestIdTwoWayDMSendRowStatus": hwY1731TestIdTwoWayDMSendRowStatus,
       "hwY1731TestIdTwoWayDMReceiveTable": hwY1731TestIdTwoWayDMReceiveTable,
       "hwY1731TestIdTwoWayDMReceiveEntry": hwY1731TestIdTwoWayDMReceiveEntry,
       "hwY1731TestIdTwoWayDMReceiveRowStatus": hwY1731TestIdTwoWayDMReceiveRowStatus,
       "hwY1731TestIdSingleSynEndedLMSendTable": hwY1731TestIdSingleSynEndedLMSendTable,
       "hwY1731TestIdSingleSynEndedLMSendEntry": hwY1731TestIdSingleSynEndedLMSendEntry,
       "hwY1731TestIdSingleSynEndedLMSendIsContinue": hwY1731TestIdSingleSynEndedLMSendIsContinue,
       "hwY1731TestIdSingleSynEndedLMSendInterval": hwY1731TestIdSingleSynEndedLMSendInterval,
       "hwY1731TestIdSingleSynEndedLMSendCount": hwY1731TestIdSingleSynEndedLMSendCount,
       "hwY1731TestIdSingleSynEndedLMSendTimeOut": hwY1731TestIdSingleSynEndedLMSendTimeOut,
       "hwY1731TestIdSingleSynEndedLMSendRowStatus": hwY1731TestIdSingleSynEndedLMSendRowStatus,
       "hwY1731TestIdSingleSynEndedLMReceiveTable": hwY1731TestIdSingleSynEndedLMReceiveTable,
       "hwY1731TestIdSingleSynEndedLMReceiveEntry": hwY1731TestIdSingleSynEndedLMReceiveEntry,
       "hwY1731TestIdSingleSynEndedLMReceiveTimeOut": hwY1731TestIdSingleSynEndedLMReceiveTimeOut,
       "hwY1731TestIdSingleSynEndedLMReceiveRowStatus": hwY1731TestIdSingleSynEndedLMReceiveRowStatus,
       "hwY1731StatisticObject": hwY1731StatisticObject,
       "hwY1731ResetStatisticTable": hwY1731ResetStatisticTable,
       "hwY1731ResetStatisticEntry": hwY1731ResetStatisticEntry,
       "hwY1731ResetStatisticType": hwY1731ResetStatisticType,
       "hwY1731ResetStatistic8021pValue": hwY1731ResetStatistic8021pValue,
       "hwY1731StatisticTable": hwY1731StatisticTable,
       "hwY1731StatisticEntry": hwY1731StatisticEntry,
       "hwY1731SingleLossStatisticGatherInterval": hwY1731SingleLossStatisticGatherInterval,
       "hwY1731SingleLossLocalStatistic": hwY1731SingleLossLocalStatistic,
       "hwY1731SingleLossLocalRatio": hwY1731SingleLossLocalRatio,
       "hwY1731SingleLossLocalRatioMax": hwY1731SingleLossLocalRatioMax,
       "hwY1731SingleLossLocalRatioMin": hwY1731SingleLossLocalRatioMin,
       "hwY1731SingleLossLocalRatioAvg": hwY1731SingleLossLocalRatioAvg,
       "hwY1731SingleLossRemoteStatistic": hwY1731SingleLossRemoteStatistic,
       "hwY1731SingleLossRemoteRatio": hwY1731SingleLossRemoteRatio,
       "hwY1731SingleLossRemoteRatioMax": hwY1731SingleLossRemoteRatioMax,
       "hwY1731SingleLossRemoteRatioMin": hwY1731SingleLossRemoteRatioMin,
       "hwY1731SingleLossRemoteRatioAvg": hwY1731SingleLossRemoteRatioAvg,
       "hwY1731OneDelayStatistic": hwY1731OneDelayStatistic,
       "hwY1731OneDelayVariation": hwY1731OneDelayVariation,
       "hwY1731OneDelayMax": hwY1731OneDelayMax,
       "hwY1731OneDelayMin": hwY1731OneDelayMin,
       "hwY1731OneDelayAvg": hwY1731OneDelayAvg,
       "hwY1731TwoDelayStatistic": hwY1731TwoDelayStatistic,
       "hwY1731TwoDelayVariation": hwY1731TwoDelayVariation,
       "hwY1731TwoDelayMax": hwY1731TwoDelayMax,
       "hwY1731TwoDelayMin": hwY1731TwoDelayMin,
       "hwY1731TwoDelayAvg": hwY1731TwoDelayAvg,
       "hwY1731SingleLossLocalMax": hwY1731SingleLossLocalMax,
       "hwY1731SingleLossLocalMin": hwY1731SingleLossLocalMin,
       "hwY1731SingleLossLocalAvg": hwY1731SingleLossLocalAvg,
       "hwY1731SingleLossRemoteMax": hwY1731SingleLossRemoteMax,
       "hwY1731SingleLossRemoteMin": hwY1731SingleLossRemoteMin,
       "hwY1731SingleLossRemoteAvg": hwY1731SingleLossRemoteAvg,
       "hwY1731OneDelayStatisticMax": hwY1731OneDelayStatisticMax,
       "hwY1731OneDelayStatisticMin": hwY1731OneDelayStatisticMin,
       "hwY1731OneDelayStatisticAvg": hwY1731OneDelayStatisticAvg,
       "hwY1731TwoDelayStatisticMax": hwY1731TwoDelayStatisticMax,
       "hwY1731TwoDelayStatisticMin": hwY1731TwoDelayStatisticMin,
       "hwY1731TwoDelayStatisticAvg": hwY1731TwoDelayStatisticAvg,
       "hwY1731TwoDelayUnresponsivePacketCount": hwY1731TwoDelayUnresponsivePacketCount,
       "hwY1731SingleLossStatistic8021pValue": hwY1731SingleLossStatistic8021pValue,
       "hwY1731OneDelayStatistic8021pValue": hwY1731OneDelayStatistic8021pValue,
       "hwY1731TwoDelayStatistic8021pValue": hwY1731TwoDelayStatistic8021pValue,
       "hwY1731OneDelayOnDemandStartTime": hwY1731OneDelayOnDemandStartTime,
       "hwY1731TwoDelayOnDemandStartTime": hwY1731TwoDelayOnDemandStartTime,
       "hwY1731SingleLossOnDemandStartTime": hwY1731SingleLossOnDemandStartTime,
       "hwCfmVlanOneDelayTrapLogTable": hwCfmVlanOneDelayTrapLogTable,
       "hwCfmVlanOneDelayTrapLogEntry": hwCfmVlanOneDelayTrapLogEntry,
       "hwCfmOneDelayTrapLogMacAddress": hwCfmOneDelayTrapLogMacAddress,
       "hwCfmVlanOneDelayTrapLogTimestamp": hwCfmVlanOneDelayTrapLogTimestamp,
       "hwCfmVlanOneDelayTrapLogDelayValue": hwCfmVlanOneDelayTrapLogDelayValue,
       "hwCfmVlanOneDelayTrapLogThreshold": hwCfmVlanOneDelayTrapLogThreshold,
       "hwCfmVlanOneDelayTrapLogDelayValueHigh": hwCfmVlanOneDelayTrapLogDelayValueHigh,
       "hwCfmVlanOneDelayTrapLogDelayValueLow": hwCfmVlanOneDelayTrapLogDelayValueLow,
       "hwCfmVlanOneDelayRcoverTrapLogTable": hwCfmVlanOneDelayRcoverTrapLogTable,
       "hwCfmVlanOneDelayRcoverTrapLogEntry": hwCfmVlanOneDelayRcoverTrapLogEntry,
       "hwCfmOneDelayRecoveryTrapMacAddress": hwCfmOneDelayRecoveryTrapMacAddress,
       "hwCfmVlanOneDelayRecoveryTrapLogTimestamp": hwCfmVlanOneDelayRecoveryTrapLogTimestamp,
       "hwCfmVlanOneDelayRecoveryTrapLogDelayValue": hwCfmVlanOneDelayRecoveryTrapLogDelayValue,
       "hwCfmVlanOneDelayRecoveryTrapLogThreshold": hwCfmVlanOneDelayRecoveryTrapLogThreshold,
       "hwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh": hwCfmVlanOneDelayRecoveryTrapLogDelayValueHigh,
       "hwCfmVlanOneDelayRecoveryTrapLogDelayValueLow": hwCfmVlanOneDelayRecoveryTrapLogDelayValueLow,
       "hwCfmVlanTwoDelayTrapLogTable": hwCfmVlanTwoDelayTrapLogTable,
       "hwCfmVlanTwoDelayTrapLogEntry": hwCfmVlanTwoDelayTrapLogEntry,
       "hwCfmTwoDelayTrapMacAddress": hwCfmTwoDelayTrapMacAddress,
       "hwCfmVlanTwoDelayTrapLogTimestamp": hwCfmVlanTwoDelayTrapLogTimestamp,
       "hwCfmVlanTwoDelayTrapLogDelayValue": hwCfmVlanTwoDelayTrapLogDelayValue,
       "hwCfmVlanTwoDelayTrapLogThreshold": hwCfmVlanTwoDelayTrapLogThreshold,
       "hwCfmVlanTwoDelayTrapLogDelayValueHigh": hwCfmVlanTwoDelayTrapLogDelayValueHigh,
       "hwCfmVlanTwoDelayTrapLogDelayValueLow": hwCfmVlanTwoDelayTrapLogDelayValueLow,
       "hwCfmVlanTwoDelayRcoverTrapLogTable": hwCfmVlanTwoDelayRcoverTrapLogTable,
       "hwCfmVlanTwoDelayRcoverTrapLogEntry": hwCfmVlanTwoDelayRcoverTrapLogEntry,
       "hwCfmTwoDelayRecoveryTrapMacAddress": hwCfmTwoDelayRecoveryTrapMacAddress,
       "hwCfmVlanTwoDelayRecoveryTrapLogTimestamp": hwCfmVlanTwoDelayRecoveryTrapLogTimestamp,
       "hwCfmVlanTwoDelayRecoveryTrapLogDelayValue": hwCfmVlanTwoDelayRecoveryTrapLogDelayValue,
       "hwCfmVlanTwoDelayRecoveryTrapLogThreshold": hwCfmVlanTwoDelayRecoveryTrapLogThreshold,
       "hwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh": hwCfmVlanTwoDelayRecoveryTrapLogDelayValueHigh,
       "hwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow": hwCfmVlanTwoDelayRecoveryTrapLogDelayValueLow,
       "hwY1731StatisticTrapLogTable": hwY1731StatisticTrapLogTable,
       "hwY1731StatisticTrapLogEntry": hwY1731StatisticTrapLogEntry,
       "hwY1731StatisticTrapLogType": hwY1731StatisticTrapLogType,
       "hwY1731StatisticTrapLogMacAddress": hwY1731StatisticTrapLogMacAddress,
       "hwY1731StatisticTrapLog8021pPriority": hwY1731StatisticTrapLog8021pPriority,
       "hwY1731StatisticTrapLogValue": hwY1731StatisticTrapLogValue,
       "hwY1731StatisticTrapLogUpperLimitThreshold": hwY1731StatisticTrapLogUpperLimitThreshold,
       "hwY1731StatisticTrapLogLowerLimitThreshold": hwY1731StatisticTrapLogLowerLimitThreshold,
       "hwY1731StatisticTrapLogValueHigh": hwY1731StatisticTrapLogValueHigh,
       "hwY1731StatisticTrapLogValueLow": hwY1731StatisticTrapLogValueLow,
       "hwY1731TestIdSingleLossStatTable": hwY1731TestIdSingleLossStatTable,
       "hwY1731TestIdSingleLossStatEntry": hwY1731TestIdSingleLossStatEntry,
       "hwY1731TestIdSingleLossSequence": hwY1731TestIdSingleLossSequence,
       "hwY1731TestIdSingleLossErrInfo": hwY1731TestIdSingleLossErrInfo,
       "hwY1731TestIdSingleLossLocal": hwY1731TestIdSingleLossLocal,
       "hwY1731TestIdSingleLossLocalRatio": hwY1731TestIdSingleLossLocalRatio,
       "hwY1731TestIdSingleLossRemote": hwY1731TestIdSingleLossRemote,
       "hwY1731TestIdSingleLossRemoteRatio": hwY1731TestIdSingleLossRemoteRatio,
       "hwY1731TestIdSingleLossOnDemandStartTime": hwY1731TestIdSingleLossOnDemandStartTime,
       "hwY1731TestIdOneDelayStatTable": hwY1731TestIdOneDelayStatTable,
       "hwY1731TestIdOneDelayStatEntry": hwY1731TestIdOneDelayStatEntry,
       "hwY1731TestIdOneDelaySequence": hwY1731TestIdOneDelaySequence,
       "hwY1731TestIdOneDelayErrInfo": hwY1731TestIdOneDelayErrInfo,
       "hwY1731TestIdOneDelay": hwY1731TestIdOneDelay,
       "hwY1731TestIdOneDelayVariation": hwY1731TestIdOneDelayVariation,
       "hwY1731TestIdOneDelayOnDemandStartTime": hwY1731TestIdOneDelayOnDemandStartTime,
       "hwY1731TestIdTwoDelayStatTable": hwY1731TestIdTwoDelayStatTable,
       "hwY1731TestIdTwoDelayStatEntry": hwY1731TestIdTwoDelayStatEntry,
       "hwY1731TestIdTwoDelaySequence": hwY1731TestIdTwoDelaySequence,
       "hwY1731TestIdTwoDelayErrInfo": hwY1731TestIdTwoDelayErrInfo,
       "hwY1731TestIdTwoDelay": hwY1731TestIdTwoDelay,
       "hwY1731TestIdTwoDelayVariation": hwY1731TestIdTwoDelayVariation,
       "hwY1731TestIdTwoDelayOnDemandStartTime": hwY1731TestIdTwoDelayOnDemandStartTime,
       "hwY1731TestIdStatisticResetTable": hwY1731TestIdStatisticResetTable,
       "hwY1731TestIdStatisticResetEntry": hwY1731TestIdStatisticResetEntry,
       "hwY1731TestIdResetStatisticType": hwY1731TestIdResetStatisticType,
       "hwY1731TestIdTwoDelaySummaryStatTable": hwY1731TestIdTwoDelaySummaryStatTable,
       "hwY1731TestIdTwoDelaySummaryStatEntry": hwY1731TestIdTwoDelaySummaryStatEntry,
       "hwY1731TestIdTwoDelayIndex": hwY1731TestIdTwoDelayIndex,
       "hwY1731TestIdTwoDelayNbrSamples": hwY1731TestIdTwoDelayNbrSamples,
       "hwY1731TestIdTwoDelayMax": hwY1731TestIdTwoDelayMax,
       "hwY1731TestIdTwoDelayMin": hwY1731TestIdTwoDelayMin,
       "hwY1731TestIdTwoDelayAve": hwY1731TestIdTwoDelayAve,
       "hwY1731TestIdTwoDelayExceedUpLimitNum": hwY1731TestIdTwoDelayExceedUpLimitNum,
       "hwY1731TestIdTwoDelayBelowLowLimitNum": hwY1731TestIdTwoDelayBelowLowLimitNum,
       "hwY1731TestIdTwoDelayVariationNbrSamples": hwY1731TestIdTwoDelayVariationNbrSamples,
       "hwY1731TestIdTwoDelayVariationMax": hwY1731TestIdTwoDelayVariationMax,
       "hwY1731TestIdTwoDelayVariationMin": hwY1731TestIdTwoDelayVariationMin,
       "hwY1731TestIdTwoDelayVariationAve": hwY1731TestIdTwoDelayVariationAve,
       "hwY1731TestIdTwoDelayVarExceedUpLimitNum": hwY1731TestIdTwoDelayVarExceedUpLimitNum,
       "hwY1731TestIdTwoDelayVarBelowLowLimitNum": hwY1731TestIdTwoDelayVarBelowLowLimitNum,
       "hwY1731TestIdSingleSynLossSummaryStatTable": hwY1731TestIdSingleSynLossSummaryStatTable,
       "hwY1731TestIdSingleSynLossSummaryStatEntry": hwY1731TestIdSingleSynLossSummaryStatEntry,
       "hwY1731TestIdSingleSynLossIndex": hwY1731TestIdSingleSynLossIndex,
       "hwY1731TestIdSingleSynLossNbrSamples": hwY1731TestIdSingleSynLossNbrSamples,
       "hwY1731TestIdSingleSynSendRemote": hwY1731TestIdSingleSynSendRemote,
       "hwY1731TestIdSingleSynRecvLocal": hwY1731TestIdSingleSynRecvLocal,
       "hwY1731TestIdSingleSynLossLocal": hwY1731TestIdSingleSynLossLocal,
       "hwY1731TestIdSingleSynExceedLocalUpLimitNum": hwY1731TestIdSingleSynExceedLocalUpLimitNum,
       "hwY1731TestIdSingleSynBelowLocalLowLimitNum": hwY1731TestIdSingleSynBelowLocalLowLimitNum,
       "hwY1731TestIdSingleSynSendLocal": hwY1731TestIdSingleSynSendLocal,
       "hwY1731TestIdSingleSynRecvRemote": hwY1731TestIdSingleSynRecvRemote,
       "hwY1731TestIdSingleSynLossRemote": hwY1731TestIdSingleSynLossRemote,
       "hwY1731TestIdSingleSynExceedRemoteUpLimitNum": hwY1731TestIdSingleSynExceedRemoteUpLimitNum,
       "hwY1731TestIdSingleSynBelowRemoteLowLimitNum": hwY1731TestIdSingleSynBelowRemoteLowLimitNum,
       "hwY1731SingleLossSummaryStatTable": hwY1731SingleLossSummaryStatTable,
       "hwY1731SingleLossSummaryStatEntry": hwY1731SingleLossSummaryStatEntry,
       "hwY1731SingleLossIndex": hwY1731SingleLossIndex,
       "hwY1731SingleLossNbrSamples": hwY1731SingleLossNbrSamples,
       "hwY1731SingleLossSendRemote": hwY1731SingleLossSendRemote,
       "hwY1731SingleLossRecvLocal": hwY1731SingleLossRecvLocal,
       "hwY1731SingleLossLossLocal": hwY1731SingleLossLossLocal,
       "hwY1731SingleLossExceedLocalUpLimitNum": hwY1731SingleLossExceedLocalUpLimitNum,
       "hwY1731SingleLossBelowLocallowLimitNum": hwY1731SingleLossBelowLocallowLimitNum,
       "hwY1731SingleLossSendLocal": hwY1731SingleLossSendLocal,
       "hwY1731SingleLossRecvRemote": hwY1731SingleLossRecvRemote,
       "hwY1731SingleLossLossRemote": hwY1731SingleLossLossRemote,
       "hwY1731SingleLossExceedRemoteUpLimitNum": hwY1731SingleLossExceedRemoteUpLimitNum,
       "hwY1731SingleLossBelowRemotelowLimitNum": hwY1731SingleLossBelowRemotelowLimitNum,
       "hwY1731TestIdSingleLossSummaryStatTable": hwY1731TestIdSingleLossSummaryStatTable,
       "hwY1731TestIdSingleLossSummaryStatEntry": hwY1731TestIdSingleLossSummaryStatEntry,
       "hwY1731TestIdSingleLossIndex": hwY1731TestIdSingleLossIndex,
       "hwY1731TestIdSingleLossNbrSamples": hwY1731TestIdSingleLossNbrSamples,
       "hwY1731TestIdSingleLossSendRemote": hwY1731TestIdSingleLossSendRemote,
       "hwY1731TestIdSingleLossRecvLocal": hwY1731TestIdSingleLossRecvLocal,
       "hwY1731TestIdSingleLossLossLocal": hwY1731TestIdSingleLossLossLocal,
       "hwY1731TestIdSingleLossExceedLocalUpLimitNum": hwY1731TestIdSingleLossExceedLocalUpLimitNum,
       "hwY1731TestIdSingleLossBelowLocallowLimitNum": hwY1731TestIdSingleLossBelowLocallowLimitNum,
       "hwY1731TestIdSingleLossSendLocal": hwY1731TestIdSingleLossSendLocal,
       "hwY1731TestIdSingleLossRecvRemote": hwY1731TestIdSingleLossRecvRemote,
       "hwY1731TestIdSingleLossLossRemote": hwY1731TestIdSingleLossLossRemote,
       "hwY1731TestIdSingleLossExceedRemoteUpLimitNum": hwY1731TestIdSingleLossExceedRemoteUpLimitNum,
       "hwY1731TestIdSingleLossBelowRemotelowLimitNum": hwY1731TestIdSingleLossBelowRemotelowLimitNum,
       "hwY1731TestIdSingleSynLossStatTable": hwY1731TestIdSingleSynLossStatTable,
       "hwY1731TestIdSingleSynLossStatEntry": hwY1731TestIdSingleSynLossStatEntry,
       "hwY1731TestIdSingleSynLossSequence": hwY1731TestIdSingleSynLossSequence,
       "hwY1731TestIdSingleSynLossErrInfo": hwY1731TestIdSingleSynLossErrInfo,
       "hwY1731TestIdSingleSynLossLocalSend": hwY1731TestIdSingleSynLossLocalSend,
       "hwY1731TestIdSingleSynLossRemoteSend": hwY1731TestIdSingleSynLossRemoteSend,
       "hwY1731TestIdSingleSynLossLocalReceive": hwY1731TestIdSingleSynLossLocalReceive,
       "hwY1731TestIdSingleSynLossUnack": hwY1731TestIdSingleSynLossUnack,
       "hwY1731TestIdSingleSynLossLossLocal": hwY1731TestIdSingleSynLossLossLocal,
       "hwY1731TestIdSingleSynLossLocalRatio": hwY1731TestIdSingleSynLossLocalRatio,
       "hwY1731TestIdSingleSynLossLossRemote": hwY1731TestIdSingleSynLossLossRemote,
       "hwY1731TestIdSingleSynLossRemoteRatio": hwY1731TestIdSingleSynLossRemoteRatio,
       "hwY1731TestIdSingleSynLossOnDemandStartTime": hwY1731TestIdSingleSynLossOnDemandStartTime,
       "hwY1731AisMaxPktNum": hwY1731AisMaxPktNum,
       "hwY1731PMModeEnable": hwY1731PMModeEnable,
       "hwY1731GlobalObject": hwY1731GlobalObject,
       "hwY1731MaxTestId": hwY1731MaxTestId,
       "hwY1731LckMaxPktNum": hwY1731LckMaxPktNum,
       "hwY1731LckCurrentPktNum": hwY1731LckCurrentPktNum,
       "hwY1731LckUpperThreshold": hwY1731LckUpperThreshold,
       "hwY1731LckLowerThreshold": hwY1731LckLowerThreshold}
)
