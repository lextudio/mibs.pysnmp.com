# SNMP MIB module (ZXR10-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-CFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:50 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxr10,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10")


# MODULE-IDENTITY

zxr10cfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120)
)
zxr10cfmMIB.setRevisions(
        ("2007-01-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class VlanIdOrNone(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



class VlanId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class Dot1agCfmMaintDomainNameType(Integer32, TextualConvention):
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
        *(("charString", 4),
          ("dnsLikeName", 2),
          ("macAddressAndUint", 3),
          ("none", 1))
    )



class Dot1agCfmMaintDomainName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )



class Dot1agCfmMaintAssocNameType(Integer32, TextualConvention):
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
        *(("charString", 2),
          ("primaryVid", 1),
          ("rfc2865VpnId", 4),
          ("unsignedInt16", 3))
    )



class Dot1agCfmMaintAssocName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )



class Dot1agCfmMDLevel(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Dot1agCfmMpDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )



class Dot1agCfmHighestDefectPri(Integer32, TextualConvention):
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



class Dot1agCfmLowestAlarmPri(Integer32, TextualConvention):
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
        *(("allDef", 1),
          ("errXcon", 4),
          ("macRemErrXcon", 2),
          ("noXcon", 6),
          ("remErrXcon", 3),
          ("xcon", 5))
    )



class Dot1agCfmSessionId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class Dot1agCfmMhfCreation(Integer32, TextualConvention):
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
        *(("defMHFdefault", 2),
          ("defMHFdefer", 4),
          ("defMHFexplicit", 3),
          ("defMHFnone", 1))
    )



class Dot1agCfmIdPermission(Integer32, TextualConvention):
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
        *(("sendIdChassis", 2),
          ("sendIdChassisManage", 4),
          ("sendIdDefer", 5),
          ("sendIdManage", 3),
          ("sendIdNone", 1))
    )



class Dot1agCfmSpeed(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fastSpeed", 0),
          ("slowSpeed", 1))
    )



class Dot1agCfmCcmInterval(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("interval100ms", 3),
          ("interval10min", 7),
          ("interval10ms", 2),
          ("interval10s", 5),
          ("interval1min", 6),
          ("interval1s", 4),
          ("interval300Hz", 1),
          ("intervalInvalid", 0))
    )



class Dot1agCfmFngState(Integer32, TextualConvention):
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
        *(("fngDefect", 2),
          ("fngDefectClearing", 5),
          ("fngDefectReported", 4),
          ("fngReportDefect", 3),
          ("fngReset", 1))
    )



class Dot1agCfmRelayActionFieldValue(Integer32, TextualConvention):
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
        *(("rlyFdb", 2),
          ("rlyHit", 1),
          ("rlyMpdb", 3))
    )



class Dot1agCfmIngressActionFieldValue(Integer32, TextualConvention):
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
        *(("ingBlocked", 3),
          ("ingDown", 2),
          ("ingOk", 1),
          ("ingVid", 4))
    )



class Dot1agCfmEgressActionFieldValue(Integer32, TextualConvention):
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
        *(("egrBlocked", 3),
          ("egrDown", 2),
          ("egrOK", 1),
          ("egrVid", 4))
    )



class Dot1afCfmIndexIntegerNextFree(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class Dot1agCfmMepDefects(Bits, TextualConvention):
    status = "current"


class Dot1agCfmLbrTransId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_Dot1agNotifications_ObjectIdentity = ObjectIdentity
dot1agNotifications = _Dot1agNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 0)
)
_Dot1agMIBObjects_ObjectIdentity = ObjectIdentity
dot1agMIBObjects = _Dot1agMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1)
)
_Dot1agCfmMd_ObjectIdentity = ObjectIdentity
dot1agCfmMd = _Dot1agCfmMd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1)
)
_Dot1agCfmMdTableNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_Dot1agCfmMdTableNextIndex_Object = MibScalar
dot1agCfmMdTableNextIndex = _Dot1agCfmMdTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 1),
    _Dot1agCfmMdTableNextIndex_Type()
)
dot1agCfmMdTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdTableNextIndex.setStatus("current")
_Dot1agCfmMdTable_Object = MibTable
dot1agCfmMdTable = _Dot1agCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmMdTable.setStatus("current")
_Dot1agCfmMdEntry_Object = MibTableRow
dot1agCfmMdEntry = _Dot1agCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1)
)
dot1agCfmMdEntry.setIndexNames(
    (0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmMdEntry.setStatus("current")


class _Dot1agCfmMdIndex_Type(Unsigned32):
    """Custom type dot1agCfmMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Dot1agCfmMdIndex_Type.__name__ = "Unsigned32"
_Dot1agCfmMdIndex_Object = MibTableColumn
dot1agCfmMdIndex = _Dot1agCfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 1),
    _Dot1agCfmMdIndex_Type()
)
dot1agCfmMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMdIndex.setStatus("current")


class _Dot1agCfmMdFormat_Type(Dot1agCfmMaintDomainNameType):
    """Custom type dot1agCfmMdFormat based on Dot1agCfmMaintDomainNameType"""


_Dot1agCfmMdFormat_Object = MibTableColumn
dot1agCfmMdFormat = _Dot1agCfmMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 2),
    _Dot1agCfmMdFormat_Type()
)
dot1agCfmMdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdFormat.setStatus("current")


class _Dot1agCfmMdName_Type(Dot1agCfmMaintDomainName):
    """Custom type dot1agCfmMdName based on Dot1agCfmMaintDomainName"""
    defaultValue = OctetString("DEFAULT")


_Dot1agCfmMdName_Object = MibTableColumn
dot1agCfmMdName = _Dot1agCfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 3),
    _Dot1agCfmMdName_Type()
)
dot1agCfmMdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdName.setStatus("current")


class _Dot1agCfmMdMdLevel_Type(Dot1agCfmMDLevel):
    """Custom type dot1agCfmMdMdLevel based on Dot1agCfmMDLevel"""
    defaultValue = 0


_Dot1agCfmMdMdLevel_Object = MibTableColumn
dot1agCfmMdMdLevel = _Dot1agCfmMdMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 4),
    _Dot1agCfmMdMdLevel_Type()
)
dot1agCfmMdMdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdMdLevel.setStatus("current")


class _Dot1agCfmMdMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmMdMhfCreation based on Dot1agCfmMhfCreation"""


_Dot1agCfmMdMhfCreation_Object = MibTableColumn
dot1agCfmMdMhfCreation = _Dot1agCfmMdMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 5),
    _Dot1agCfmMdMhfCreation_Type()
)
dot1agCfmMdMhfCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdMhfCreation.setStatus("current")


class _Dot1agCfmMdMhfIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type dot1agCfmMdMhfIdPermission based on Dot1agCfmIdPermission"""


_Dot1agCfmMdMhfIdPermission_Object = MibTableColumn
dot1agCfmMdMhfIdPermission = _Dot1agCfmMdMhfIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 6),
    _Dot1agCfmMdMhfIdPermission_Type()
)
dot1agCfmMdMhfIdPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdMhfIdPermission.setStatus("current")
_Dot1agCfmMdMaTableNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_Dot1agCfmMdMaTableNextIndex_Object = MibTableColumn
dot1agCfmMdMaTableNextIndex = _Dot1agCfmMdMaTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 7),
    _Dot1agCfmMdMaTableNextIndex_Type()
)
dot1agCfmMdMaTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdMaTableNextIndex.setStatus("current")
_Dot1agCfmMdRowStatus_Type = RowStatus
_Dot1agCfmMdRowStatus_Object = MibTableColumn
dot1agCfmMdRowStatus = _Dot1agCfmMdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 8),
    _Dot1agCfmMdRowStatus_Type()
)
dot1agCfmMdRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdRowStatus.setStatus("current")
_Dot1agCfmMa_ObjectIdentity = ObjectIdentity
dot1agCfmMa = _Dot1agCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2)
)
_Dot1agCfmMaTable_Object = MibTable
dot1agCfmMaTable = _Dot1agCfmMaTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmMaTable.setStatus("current")
_Dot1agCfmMaEntry_Object = MibTableRow
dot1agCfmMaEntry = _Dot1agCfmMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1)
)
dot1agCfmMaEntry.setIndexNames(
    (0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaEntry.setStatus("current")


class _Dot1agCfmMaIndex_Type(Unsigned32):
    """Custom type dot1agCfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Dot1agCfmMaIndex_Type.__name__ = "Unsigned32"
_Dot1agCfmMaIndex_Object = MibTableColumn
dot1agCfmMaIndex = _Dot1agCfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 1),
    _Dot1agCfmMaIndex_Type()
)
dot1agCfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaIndex.setStatus("current")
_Dot1agCfmMaPrimaryVlanId_Type = VlanIdOrNone
_Dot1agCfmMaPrimaryVlanId_Object = MibTableColumn
dot1agCfmMaPrimaryVlanId = _Dot1agCfmMaPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 2),
    _Dot1agCfmMaPrimaryVlanId_Type()
)
dot1agCfmMaPrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaPrimaryVlanId.setStatus("current")
_Dot1agCfmMaFormat_Type = Dot1agCfmMaintAssocNameType
_Dot1agCfmMaFormat_Object = MibTableColumn
dot1agCfmMaFormat = _Dot1agCfmMaFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 3),
    _Dot1agCfmMaFormat_Type()
)
dot1agCfmMaFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaFormat.setStatus("current")
_Dot1agCfmMaName_Type = Dot1agCfmMaintAssocName
_Dot1agCfmMaName_Object = MibTableColumn
dot1agCfmMaName = _Dot1agCfmMaName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 4),
    _Dot1agCfmMaName_Type()
)
dot1agCfmMaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaName.setStatus("current")


class _Dot1agCfmMaMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmMaMhfCreation based on Dot1agCfmMhfCreation"""


_Dot1agCfmMaMhfCreation_Object = MibTableColumn
dot1agCfmMaMhfCreation = _Dot1agCfmMaMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 5),
    _Dot1agCfmMaMhfCreation_Type()
)
dot1agCfmMaMhfCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaMhfCreation.setStatus("current")


class _Dot1agCfmMaIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type dot1agCfmMaIdPermission based on Dot1agCfmIdPermission"""


_Dot1agCfmMaIdPermission_Object = MibTableColumn
dot1agCfmMaIdPermission = _Dot1agCfmMaIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 6),
    _Dot1agCfmMaIdPermission_Type()
)
dot1agCfmMaIdPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaIdPermission.setStatus("current")


class _Dot1agCfmMaCcmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type dot1agCfmMaCcmInterval based on Dot1agCfmCcmInterval"""


_Dot1agCfmMaCcmInterval_Object = MibTableColumn
dot1agCfmMaCcmInterval = _Dot1agCfmMaCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 7),
    _Dot1agCfmMaCcmInterval_Type()
)
dot1agCfmMaCcmInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaCcmInterval.setStatus("current")
_Dot1agCfmMaRowStatus_Type = RowStatus
_Dot1agCfmMaRowStatus_Object = MibTableColumn
dot1agCfmMaRowStatus = _Dot1agCfmMaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 8),
    _Dot1agCfmMaRowStatus_Type()
)
dot1agCfmMaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaRowStatus.setStatus("current")
_Dot1agCfmMASpeed_Type = Dot1agCfmSpeed
_Dot1agCfmMASpeed_Object = MibTableColumn
dot1agCfmMASpeed = _Dot1agCfmMASpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 9),
    _Dot1agCfmMASpeed_Type()
)
dot1agCfmMASpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMASpeed.setStatus("current")
_Dot1agCfmMaVlanListTable_Object = MibTable
dot1agCfmMaVlanListTable = _Dot1agCfmMaVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmMaVlanListTable.setStatus("current")
_Dot1agCfmMaVlanListEntry_Object = MibTableRow
dot1agCfmMaVlanListEntry = _Dot1agCfmMaVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 2, 1)
)
dot1agCfmMaVlanListEntry.setIndexNames(
    (0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmMaVlanListIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaVlanListEntry.setStatus("current")
_Dot1agCfmMaVlanListIdentifier_Type = VlanId
_Dot1agCfmMaVlanListIdentifier_Object = MibTableColumn
dot1agCfmMaVlanListIdentifier = _Dot1agCfmMaVlanListIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 2, 1, 1),
    _Dot1agCfmMaVlanListIdentifier_Type()
)
dot1agCfmMaVlanListIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaVlanListIdentifier.setStatus("current")
_Dot1agCfmMaVlanListRowStatus_Type = RowStatus
_Dot1agCfmMaVlanListRowStatus_Object = MibTableColumn
dot1agCfmMaVlanListRowStatus = _Dot1agCfmMaVlanListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 2, 1, 2),
    _Dot1agCfmMaVlanListRowStatus_Type()
)
dot1agCfmMaVlanListRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaVlanListRowStatus.setStatus("current")
_Dot1agCfmMaMepListTable_Object = MibTable
dot1agCfmMaMepListTable = _Dot1agCfmMaMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dot1agCfmMaMepListTable.setStatus("current")
_Dot1agCfmMaMepListEntry_Object = MibTableRow
dot1agCfmMaMepListEntry = _Dot1agCfmMaMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 3, 1)
)
dot1agCfmMaMepListEntry.setIndexNames(
    (0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmMaMepListSessionId"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaMepListEntry.setStatus("current")
_Dot1agCfmMaMepListSessionId_Type = Dot1agCfmSessionId
_Dot1agCfmMaMepListSessionId_Object = MibTableColumn
dot1agCfmMaMepListSessionId = _Dot1agCfmMaMepListSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 3, 1, 1),
    _Dot1agCfmMaMepListSessionId_Type()
)
dot1agCfmMaMepListSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaMepListSessionId.setStatus("current")
_Dot1agCfmMaMepListRowStatus_Type = RowStatus
_Dot1agCfmMaMepListRowStatus_Object = MibTableColumn
dot1agCfmMaMepListRowStatus = _Dot1agCfmMaMepListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 3, 1, 2),
    _Dot1agCfmMaMepListRowStatus_Type()
)
dot1agCfmMaMepListRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaMepListRowStatus.setStatus("current")
_Dot1agCfmMep_ObjectIdentity = ObjectIdentity
dot1agCfmMep = _Dot1agCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3)
)
_Dot1agCfmMepTable_Object = MibTable
dot1agCfmMepTable = _Dot1agCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmMepTable.setStatus("current")
_Dot1agCfmMepEntry_Object = MibTableRow
dot1agCfmMepEntry = _Dot1agCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1)
)
dot1agCfmMepEntry.setIndexNames(
    (0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmSessionId"),
)
if mibBuilder.loadTexts:
    dot1agCfmMepEntry.setStatus("current")
_Dot1agCfmSessionId_Type = Dot1agCfmSessionId
_Dot1agCfmSessionId_Object = MibTableColumn
dot1agCfmSessionId = _Dot1agCfmSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 1),
    _Dot1agCfmSessionId_Type()
)
dot1agCfmSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmSessionId.setStatus("current")
_Dot1agCfmMepIfIndex_Type = InterfaceIndexOrZero
_Dot1agCfmMepIfIndex_Object = MibTableColumn
dot1agCfmMepIfIndex = _Dot1agCfmMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 2),
    _Dot1agCfmMepIfIndex_Type()
)
dot1agCfmMepIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepIfIndex.setStatus("current")
_Dot1agCfmMepDirection_Type = Dot1agCfmMpDirection
_Dot1agCfmMepDirection_Object = MibTableColumn
dot1agCfmMepDirection = _Dot1agCfmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 3),
    _Dot1agCfmMepDirection_Type()
)
dot1agCfmMepDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDirection.setStatus("current")


class _Dot1agCfmMepPrimaryVid_Type(Unsigned32):
    """Custom type dot1agCfmMepPrimaryVid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Dot1agCfmMepPrimaryVid_Type.__name__ = "Unsigned32"
_Dot1agCfmMepPrimaryVid_Object = MibTableColumn
dot1agCfmMepPrimaryVid = _Dot1agCfmMepPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 4),
    _Dot1agCfmMepPrimaryVid_Type()
)
dot1agCfmMepPrimaryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepPrimaryVid.setStatus("current")


class _Dot1agCfmMepActive_Type(TruthValue):
    """Custom type dot1agCfmMepActive based on TruthValue"""


_Dot1agCfmMepActive_Object = MibTableColumn
dot1agCfmMepActive = _Dot1agCfmMepActive_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 5),
    _Dot1agCfmMepActive_Type()
)
dot1agCfmMepActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepActive.setStatus("current")


class _Dot1agCfmMepFngState_Type(Dot1agCfmFngState):
    """Custom type dot1agCfmMepFngState based on Dot1agCfmFngState"""


_Dot1agCfmMepFngState_Object = MibTableColumn
dot1agCfmMepFngState = _Dot1agCfmMepFngState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 6),
    _Dot1agCfmMepFngState_Type()
)
dot1agCfmMepFngState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepFngState.setStatus("current")


class _Dot1agCfmMepCciEnabled_Type(TruthValue):
    """Custom type dot1agCfmMepCciEnabled based on TruthValue"""


_Dot1agCfmMepCciEnabled_Object = MibTableColumn
dot1agCfmMepCciEnabled = _Dot1agCfmMepCciEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 7),
    _Dot1agCfmMepCciEnabled_Type()
)
dot1agCfmMepCciEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepCciEnabled.setStatus("current")


class _Dot1agCfmMepCcmLtmPriority_Type(Unsigned32):
    """Custom type dot1agCfmMepCcmLtmPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1agCfmMepCcmLtmPriority_Type.__name__ = "Unsigned32"
_Dot1agCfmMepCcmLtmPriority_Object = MibTableColumn
dot1agCfmMepCcmLtmPriority = _Dot1agCfmMepCcmLtmPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 8),
    _Dot1agCfmMepCcmLtmPriority_Type()
)
dot1agCfmMepCcmLtmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepCcmLtmPriority.setStatus("current")
_Dot1agCfmMepMacAddress_Type = MacAddress
_Dot1agCfmMepMacAddress_Object = MibTableColumn
dot1agCfmMepMacAddress = _Dot1agCfmMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 9),
    _Dot1agCfmMepMacAddress_Type()
)
dot1agCfmMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepMacAddress.setStatus("current")


class _Dot1agCfmMepLowPrDef_Type(Dot1agCfmLowestAlarmPri):
    """Custom type dot1agCfmMepLowPrDef based on Dot1agCfmLowestAlarmPri"""


_Dot1agCfmMepLowPrDef_Object = MibTableColumn
dot1agCfmMepLowPrDef = _Dot1agCfmMepLowPrDef_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 10),
    _Dot1agCfmMepLowPrDef_Type()
)
dot1agCfmMepLowPrDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLowPrDef.setStatus("current")
_Dot1agCfmMepHighestPrDefect_Type = Dot1agCfmHighestDefectPri
_Dot1agCfmMepHighestPrDefect_Object = MibTableColumn
dot1agCfmMepHighestPrDefect = _Dot1agCfmMepHighestPrDefect_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 11),
    _Dot1agCfmMepHighestPrDefect_Type()
)
dot1agCfmMepHighestPrDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepHighestPrDefect.setStatus("current")
_Dot1agCfmMepDefects_Type = Dot1agCfmMepDefects
_Dot1agCfmMepDefects_Object = MibTableColumn
dot1agCfmMepDefects = _Dot1agCfmMepDefects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 12),
    _Dot1agCfmMepDefects_Type()
)
dot1agCfmMepDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDefects.setStatus("current")
_Dot1agCfmMepCciSentCcms_Type = Counter32
_Dot1agCfmMepCciSentCcms_Object = MibTableColumn
dot1agCfmMepCciSentCcms = _Dot1agCfmMepCciSentCcms_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 13),
    _Dot1agCfmMepCciSentCcms_Type()
)
dot1agCfmMepCciSentCcms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepCciSentCcms.setStatus("current")
_Dot1agCfmMepId_Type = Unsigned32
_Dot1agCfmMepId_Object = MibTableColumn
dot1agCfmMepId = _Dot1agCfmMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 14),
    _Dot1agCfmMepId_Type()
)
dot1agCfmMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepId.setStatus("current")
_Dot1agCfmMepMEPAttachType_Type = Unsigned32
_Dot1agCfmMepMEPAttachType_Object = MibTableColumn
dot1agCfmMepMEPAttachType = _Dot1agCfmMepMEPAttachType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 15),
    _Dot1agCfmMepMEPAttachType_Type()
)
dot1agCfmMepMEPAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepMEPAttachType.setStatus("current")
_Dot1agCfmMepTunnelId_Type = Unsigned32
_Dot1agCfmMepTunnelId_Object = MibTableColumn
dot1agCfmMepTunnelId = _Dot1agCfmMepTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 16),
    _Dot1agCfmMepTunnelId_Type()
)
dot1agCfmMepTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTunnelId.setStatus("current")


class _Dot1agCfmMepLMFlage_Type(TruthValue):
    """Custom type dot1agCfmMepLMFlage based on TruthValue"""


_Dot1agCfmMepLMFlage_Object = MibTableColumn
dot1agCfmMepLMFlage = _Dot1agCfmMepLMFlage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 17),
    _Dot1agCfmMepLMFlage_Type()
)
dot1agCfmMepLMFlage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLMFlage.setStatus("current")


class _Dot1agCfmMepDMFlage_Type(TruthValue):
    """Custom type dot1agCfmMepDMFlage based on TruthValue"""


_Dot1agCfmMepDMFlage_Object = MibTableColumn
dot1agCfmMepDMFlage = _Dot1agCfmMepDMFlage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 18),
    _Dot1agCfmMepDMFlage_Type()
)
dot1agCfmMepDMFlage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDMFlage.setStatus("current")
_Dot1agCfmMepPortName_Type = DisplayString
_Dot1agCfmMepPortName_Object = MibTableColumn
dot1agCfmMepPortName = _Dot1agCfmMepPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 19),
    _Dot1agCfmMepPortName_Type()
)
dot1agCfmMepPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepPortName.setStatus("current")
_Dot1agCfmMepLbrIn_Type = Counter32
_Dot1agCfmMepLbrIn_Object = MibTableColumn
dot1agCfmMepLbrIn = _Dot1agCfmMepLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 20),
    _Dot1agCfmMepLbrIn_Type()
)
dot1agCfmMepLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrIn.setStatus("current")
_Dot1agCfmMepLbrInOutOfOrder_Type = Counter32
_Dot1agCfmMepLbrInOutOfOrder_Object = MibTableColumn
dot1agCfmMepLbrInOutOfOrder = _Dot1agCfmMepLbrInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 21),
    _Dot1agCfmMepLbrInOutOfOrder_Type()
)
dot1agCfmMepLbrInOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrInOutOfOrder.setStatus("current")
_Dot1agCfmMepLbrBadMsdu_Type = Counter32
_Dot1agCfmMepLbrBadMsdu_Object = MibTableColumn
dot1agCfmMepLbrBadMsdu = _Dot1agCfmMepLbrBadMsdu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 22),
    _Dot1agCfmMepLbrBadMsdu_Type()
)
dot1agCfmMepLbrBadMsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrBadMsdu.setStatus("current")
_Dot1agCfmMepLtmNextSeqNumber_Type = Unsigned32
_Dot1agCfmMepLtmNextSeqNumber_Object = MibTableColumn
dot1agCfmMepLtmNextSeqNumber = _Dot1agCfmMepLtmNextSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 23),
    _Dot1agCfmMepLtmNextSeqNumber_Type()
)
dot1agCfmMepLtmNextSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLtmNextSeqNumber.setStatus("current")
_Dot1agCfmMepUnexpLtrIn_Type = Counter32
_Dot1agCfmMepUnexpLtrIn_Object = MibTableColumn
dot1agCfmMepUnexpLtrIn = _Dot1agCfmMepUnexpLtrIn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 24),
    _Dot1agCfmMepUnexpLtrIn_Type()
)
dot1agCfmMepUnexpLtrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepUnexpLtrIn.setStatus("current")
_Dot1agCfmMepLbrOut_Type = Counter32
_Dot1agCfmMepLbrOut_Object = MibTableColumn
dot1agCfmMepLbrOut = _Dot1agCfmMepLbrOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 25),
    _Dot1agCfmMepLbrOut_Type()
)
dot1agCfmMepLbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrOut.setStatus("current")
_Dot1agCfmMepRowStatus_Type = RowStatus
_Dot1agCfmMepRowStatus_Object = MibTableColumn
dot1agCfmMepRowStatus = _Dot1agCfmMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 26),
    _Dot1agCfmMepRowStatus_Type()
)
dot1agCfmMepRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepRowStatus.setStatus("current")
_Dot1agCfmLtrTable_Object = MibTable
dot1agCfmLtrTable = _Dot1agCfmLtrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmLtrTable.setStatus("current")
_Dot1agCfmLtrEntry_Object = MibTableRow
dot1agCfmLtrEntry = _Dot1agCfmLtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1)
)
dot1agCfmLtrEntry.setIndexNames(
    (0, "ZXR10-CFM-MIB", "dot1agCfmLtrSeqNumber"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmLtrReceiveOrder"),
)
if mibBuilder.loadTexts:
    dot1agCfmLtrEntry.setStatus("current")


class _Dot1agCfmLtrSeqNumber_Type(Unsigned32):
    """Custom type dot1agCfmLtrSeqNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Dot1agCfmLtrSeqNumber_Type.__name__ = "Unsigned32"
_Dot1agCfmLtrSeqNumber_Object = MibTableColumn
dot1agCfmLtrSeqNumber = _Dot1agCfmLtrSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 1),
    _Dot1agCfmLtrSeqNumber_Type()
)
dot1agCfmLtrSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmLtrSeqNumber.setStatus("current")


class _Dot1agCfmLtrReceiveOrder_Type(Unsigned32):
    """Custom type dot1agCfmLtrReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot1agCfmLtrReceiveOrder_Type.__name__ = "Unsigned32"
_Dot1agCfmLtrReceiveOrder_Object = MibTableColumn
dot1agCfmLtrReceiveOrder = _Dot1agCfmLtrReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 2),
    _Dot1agCfmLtrReceiveOrder_Type()
)
dot1agCfmLtrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmLtrReceiveOrder.setStatus("current")


class _Dot1agCfmLtrTtl_Type(Unsigned32):
    """Custom type dot1agCfmLtrTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1agCfmLtrTtl_Type.__name__ = "Unsigned32"
_Dot1agCfmLtrTtl_Object = MibTableColumn
dot1agCfmLtrTtl = _Dot1agCfmLtrTtl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 3),
    _Dot1agCfmLtrTtl_Type()
)
dot1agCfmLtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrTtl.setStatus("current")
_Dot1agCfmLtrForwarded_Type = TruthValue
_Dot1agCfmLtrForwarded_Object = MibTableColumn
dot1agCfmLtrForwarded = _Dot1agCfmLtrForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 4),
    _Dot1agCfmLtrForwarded_Type()
)
dot1agCfmLtrForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrForwarded.setStatus("current")
_Dot1agCfmLtrTerminalMep_Type = TruthValue
_Dot1agCfmLtrTerminalMep_Object = MibTableColumn
dot1agCfmLtrTerminalMep = _Dot1agCfmLtrTerminalMep_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 5),
    _Dot1agCfmLtrTerminalMep_Type()
)
dot1agCfmLtrTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrTerminalMep.setStatus("current")


class _Dot1agCfmLtrLastEgressIdentifier_Type(OctetString):
    """Custom type dot1agCfmLtrLastEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Dot1agCfmLtrLastEgressIdentifier_Type.__name__ = "OctetString"
_Dot1agCfmLtrLastEgressIdentifier_Object = MibTableColumn
dot1agCfmLtrLastEgressIdentifier = _Dot1agCfmLtrLastEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 6),
    _Dot1agCfmLtrLastEgressIdentifier_Type()
)
dot1agCfmLtrLastEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrLastEgressIdentifier.setStatus("current")


class _Dot1agCfmLtrNextEgressIdentifier_Type(OctetString):
    """Custom type dot1agCfmLtrNextEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Dot1agCfmLtrNextEgressIdentifier_Type.__name__ = "OctetString"
_Dot1agCfmLtrNextEgressIdentifier_Object = MibTableColumn
dot1agCfmLtrNextEgressIdentifier = _Dot1agCfmLtrNextEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 7),
    _Dot1agCfmLtrNextEgressIdentifier_Type()
)
dot1agCfmLtrNextEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrNextEgressIdentifier.setStatus("current")
_Dot1agCfmLtrRelay_Type = Dot1agCfmRelayActionFieldValue
_Dot1agCfmLtrRelay_Object = MibTableColumn
dot1agCfmLtrRelay = _Dot1agCfmLtrRelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 8),
    _Dot1agCfmLtrRelay_Type()
)
dot1agCfmLtrRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrRelay.setStatus("current")
_Dot1agCfmLtrIngress_Type = Dot1agCfmIngressActionFieldValue
_Dot1agCfmLtrIngress_Object = MibTableColumn
dot1agCfmLtrIngress = _Dot1agCfmLtrIngress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 9),
    _Dot1agCfmLtrIngress_Type()
)
dot1agCfmLtrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngress.setStatus("current")
_Dot1agCfmLtrIngressMac_Type = MacAddress
_Dot1agCfmLtrIngressMac_Object = MibTableColumn
dot1agCfmLtrIngressMac = _Dot1agCfmLtrIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 10),
    _Dot1agCfmLtrIngressMac_Type()
)
dot1agCfmLtrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngressMac.setStatus("current")
_Dot1agCfmLtrEgress_Type = Dot1agCfmEgressActionFieldValue
_Dot1agCfmLtrEgress_Object = MibTableColumn
dot1agCfmLtrEgress = _Dot1agCfmLtrEgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 11),
    _Dot1agCfmLtrEgress_Type()
)
dot1agCfmLtrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgress.setStatus("current")
_Dot1agCfmLtrEgressMac_Type = MacAddress
_Dot1agCfmLtrEgressMac_Object = MibTableColumn
dot1agCfmLtrEgressMac = _Dot1agCfmLtrEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 12),
    _Dot1agCfmLtrEgressMac_Type()
)
dot1agCfmLtrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgressMac.setStatus("current")
_Dot1agCfmMepDbTable_Object = MibTable
dot1agCfmMepDbTable = _Dot1agCfmMepDbTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dot1agCfmMepDbTable.setStatus("current")
_Dot1agCfmMepDbEntry_Object = MibTableRow
dot1agCfmMepDbEntry = _Dot1agCfmMepDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3, 1)
)
dot1agCfmMepDbEntry.setIndexNames(
    (0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmMepDbRSessionId"),
)
if mibBuilder.loadTexts:
    dot1agCfmMepDbEntry.setStatus("current")
_Dot1agCfmMepDbRSessionId_Type = Dot1agCfmSessionId
_Dot1agCfmMepDbRSessionId_Object = MibTableColumn
dot1agCfmMepDbRSessionId = _Dot1agCfmMepDbRSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3, 1, 1),
    _Dot1agCfmMepDbRSessionId_Type()
)
dot1agCfmMepDbRSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRSessionId.setStatus("current")
_Dot1agCfmMepDbMacAddress_Type = MacAddress
_Dot1agCfmMepDbMacAddress_Object = MibTableColumn
dot1agCfmMepDbMacAddress = _Dot1agCfmMepDbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3, 1, 2),
    _Dot1agCfmMepDbMacAddress_Type()
)
dot1agCfmMepDbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbMacAddress.setStatus("current")
_Dot1agCfmMepDbRdi_Type = TruthValue
_Dot1agCfmMepDbRdi_Object = MibTableColumn
dot1agCfmMepDbRdi = _Dot1agCfmMepDbRdi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3, 1, 3),
    _Dot1agCfmMepDbRdi_Type()
)
dot1agCfmMepDbRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRdi.setStatus("current")
_Dot1agCfmMepDbId_Type = Unsigned32
_Dot1agCfmMepDbId_Object = MibTableColumn
dot1agCfmMepDbId = _Dot1agCfmMepDbId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3, 1, 4),
    _Dot1agCfmMepDbId_Type()
)
dot1agCfmMepDbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDbId.setStatus("current")
_Dot1agCfmLbrInfo_ObjectIdentity = ObjectIdentity
dot1agCfmLbrInfo = _Dot1agCfmLbrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 4)
)
_Dot1agCfmLbrTransId_Type = Dot1agCfmLbrTransId
_Dot1agCfmLbrTransId_Object = MibScalar
dot1agCfmLbrTransId = _Dot1agCfmLbrTransId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 4, 1),
    _Dot1agCfmLbrTransId_Type()
)
dot1agCfmLbrTransId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLbrTransId.setStatus("current")
_Dot1agCfmLbrPrintInfo_Type = DisplayString
_Dot1agCfmLbrPrintInfo_Object = MibScalar
dot1agCfmLbrPrintInfo = _Dot1agCfmLbrPrintInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 4, 2),
    _Dot1agCfmLbrPrintInfo_Type()
)
dot1agCfmLbrPrintInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLbrPrintInfo.setStatus("current")
_Dot1agCfmMipTable_Object = MibTable
dot1agCfmMipTable = _Dot1agCfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 5)
)
if mibBuilder.loadTexts:
    dot1agCfmMipTable.setStatus("current")
_Dot1agCfmMipEntry_Object = MibTableRow
dot1agCfmMipEntry = _Dot1agCfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 5, 1)
)
dot1agCfmMipEntry.setIndexNames(
    (0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZXR10-CFM-MIB", "dot1agCfmMipSessionId"),
)
if mibBuilder.loadTexts:
    dot1agCfmMipEntry.setStatus("current")
_Dot1agCfmMipSessionId_Type = Unsigned32
_Dot1agCfmMipSessionId_Object = MibTableColumn
dot1agCfmMipSessionId = _Dot1agCfmMipSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 5, 1, 1),
    _Dot1agCfmMipSessionId_Type()
)
dot1agCfmMipSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMipSessionId.setStatus("current")
_Dot1agCfmMipName_Type = DisplayString
_Dot1agCfmMipName_Object = MibTableColumn
dot1agCfmMipName = _Dot1agCfmMipName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 5, 1, 2),
    _Dot1agCfmMipName_Type()
)
dot1agCfmMipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMipName.setStatus("current")
_Dot1agCfmMipPortName_Type = DisplayString
_Dot1agCfmMipPortName_Object = MibTableColumn
dot1agCfmMipPortName = _Dot1agCfmMipPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 5, 1, 3),
    _Dot1agCfmMipPortName_Type()
)
dot1agCfmMipPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMipPortName.setStatus("current")
_Dot1agCfmGloPara_ObjectIdentity = ObjectIdentity
dot1agCfmGloPara = _Dot1agCfmGloPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 4)
)
_Dot1agCfmGlobalIsEnable_Type = TruthValue
_Dot1agCfmGlobalIsEnable_Object = MibScalar
dot1agCfmGlobalIsEnable = _Dot1agCfmGlobalIsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 4, 4),
    _Dot1agCfmGlobalIsEnable_Type()
)
dot1agCfmGlobalIsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmGlobalIsEnable.setStatus("current")

# Managed Objects groups


# Notification objects

dot1agCfmFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 120, 0, 1)
)
dot1agCfmFaultAlarm.setObjects(
    ("ZXR10-CFM-MIB", "dot1agCfmMepHighestPrDefect")
)
if mibBuilder.loadTexts:
    dot1agCfmFaultAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-CFM-MIB",
    **{"InterfaceIndexOrZero": InterfaceIndexOrZero,
       "VlanIdOrNone": VlanIdOrNone,
       "VlanId": VlanId,
       "Dot1agCfmMaintDomainNameType": Dot1agCfmMaintDomainNameType,
       "Dot1agCfmMaintDomainName": Dot1agCfmMaintDomainName,
       "Dot1agCfmMaintAssocNameType": Dot1agCfmMaintAssocNameType,
       "Dot1agCfmMaintAssocName": Dot1agCfmMaintAssocName,
       "Dot1agCfmMDLevel": Dot1agCfmMDLevel,
       "Dot1agCfmMpDirection": Dot1agCfmMpDirection,
       "Dot1agCfmHighestDefectPri": Dot1agCfmHighestDefectPri,
       "Dot1agCfmLowestAlarmPri": Dot1agCfmLowestAlarmPri,
       "Dot1agCfmSessionId": Dot1agCfmSessionId,
       "Dot1agCfmMhfCreation": Dot1agCfmMhfCreation,
       "Dot1agCfmIdPermission": Dot1agCfmIdPermission,
       "Dot1agCfmSpeed": Dot1agCfmSpeed,
       "Dot1agCfmCcmInterval": Dot1agCfmCcmInterval,
       "Dot1agCfmFngState": Dot1agCfmFngState,
       "Dot1agCfmRelayActionFieldValue": Dot1agCfmRelayActionFieldValue,
       "Dot1agCfmIngressActionFieldValue": Dot1agCfmIngressActionFieldValue,
       "Dot1agCfmEgressActionFieldValue": Dot1agCfmEgressActionFieldValue,
       "Dot1afCfmIndexIntegerNextFree": Dot1afCfmIndexIntegerNextFree,
       "Dot1agCfmMepDefects": Dot1agCfmMepDefects,
       "Dot1agCfmLbrTransId": Dot1agCfmLbrTransId,
       "zxr10cfmMIB": zxr10cfmMIB,
       "dot1agNotifications": dot1agNotifications,
       "dot1agCfmFaultAlarm": dot1agCfmFaultAlarm,
       "dot1agMIBObjects": dot1agMIBObjects,
       "dot1agCfmMd": dot1agCfmMd,
       "dot1agCfmMdTableNextIndex": dot1agCfmMdTableNextIndex,
       "dot1agCfmMdTable": dot1agCfmMdTable,
       "dot1agCfmMdEntry": dot1agCfmMdEntry,
       "dot1agCfmMdIndex": dot1agCfmMdIndex,
       "dot1agCfmMdFormat": dot1agCfmMdFormat,
       "dot1agCfmMdName": dot1agCfmMdName,
       "dot1agCfmMdMdLevel": dot1agCfmMdMdLevel,
       "dot1agCfmMdMhfCreation": dot1agCfmMdMhfCreation,
       "dot1agCfmMdMhfIdPermission": dot1agCfmMdMhfIdPermission,
       "dot1agCfmMdMaTableNextIndex": dot1agCfmMdMaTableNextIndex,
       "dot1agCfmMdRowStatus": dot1agCfmMdRowStatus,
       "dot1agCfmMa": dot1agCfmMa,
       "dot1agCfmMaTable": dot1agCfmMaTable,
       "dot1agCfmMaEntry": dot1agCfmMaEntry,
       "dot1agCfmMaIndex": dot1agCfmMaIndex,
       "dot1agCfmMaPrimaryVlanId": dot1agCfmMaPrimaryVlanId,
       "dot1agCfmMaFormat": dot1agCfmMaFormat,
       "dot1agCfmMaName": dot1agCfmMaName,
       "dot1agCfmMaMhfCreation": dot1agCfmMaMhfCreation,
       "dot1agCfmMaIdPermission": dot1agCfmMaIdPermission,
       "dot1agCfmMaCcmInterval": dot1agCfmMaCcmInterval,
       "dot1agCfmMaRowStatus": dot1agCfmMaRowStatus,
       "dot1agCfmMASpeed": dot1agCfmMASpeed,
       "dot1agCfmMaVlanListTable": dot1agCfmMaVlanListTable,
       "dot1agCfmMaVlanListEntry": dot1agCfmMaVlanListEntry,
       "dot1agCfmMaVlanListIdentifier": dot1agCfmMaVlanListIdentifier,
       "dot1agCfmMaVlanListRowStatus": dot1agCfmMaVlanListRowStatus,
       "dot1agCfmMaMepListTable": dot1agCfmMaMepListTable,
       "dot1agCfmMaMepListEntry": dot1agCfmMaMepListEntry,
       "dot1agCfmMaMepListSessionId": dot1agCfmMaMepListSessionId,
       "dot1agCfmMaMepListRowStatus": dot1agCfmMaMepListRowStatus,
       "dot1agCfmMep": dot1agCfmMep,
       "dot1agCfmMepTable": dot1agCfmMepTable,
       "dot1agCfmMepEntry": dot1agCfmMepEntry,
       "dot1agCfmSessionId": dot1agCfmSessionId,
       "dot1agCfmMepIfIndex": dot1agCfmMepIfIndex,
       "dot1agCfmMepDirection": dot1agCfmMepDirection,
       "dot1agCfmMepPrimaryVid": dot1agCfmMepPrimaryVid,
       "dot1agCfmMepActive": dot1agCfmMepActive,
       "dot1agCfmMepFngState": dot1agCfmMepFngState,
       "dot1agCfmMepCciEnabled": dot1agCfmMepCciEnabled,
       "dot1agCfmMepCcmLtmPriority": dot1agCfmMepCcmLtmPriority,
       "dot1agCfmMepMacAddress": dot1agCfmMepMacAddress,
       "dot1agCfmMepLowPrDef": dot1agCfmMepLowPrDef,
       "dot1agCfmMepHighestPrDefect": dot1agCfmMepHighestPrDefect,
       "dot1agCfmMepDefects": dot1agCfmMepDefects,
       "dot1agCfmMepCciSentCcms": dot1agCfmMepCciSentCcms,
       "dot1agCfmMepId": dot1agCfmMepId,
       "dot1agCfmMepMEPAttachType": dot1agCfmMepMEPAttachType,
       "dot1agCfmMepTunnelId": dot1agCfmMepTunnelId,
       "dot1agCfmMepLMFlage": dot1agCfmMepLMFlage,
       "dot1agCfmMepDMFlage": dot1agCfmMepDMFlage,
       "dot1agCfmMepPortName": dot1agCfmMepPortName,
       "dot1agCfmMepLbrIn": dot1agCfmMepLbrIn,
       "dot1agCfmMepLbrInOutOfOrder": dot1agCfmMepLbrInOutOfOrder,
       "dot1agCfmMepLbrBadMsdu": dot1agCfmMepLbrBadMsdu,
       "dot1agCfmMepLtmNextSeqNumber": dot1agCfmMepLtmNextSeqNumber,
       "dot1agCfmMepUnexpLtrIn": dot1agCfmMepUnexpLtrIn,
       "dot1agCfmMepLbrOut": dot1agCfmMepLbrOut,
       "dot1agCfmMepRowStatus": dot1agCfmMepRowStatus,
       "dot1agCfmLtrTable": dot1agCfmLtrTable,
       "dot1agCfmLtrEntry": dot1agCfmLtrEntry,
       "dot1agCfmLtrSeqNumber": dot1agCfmLtrSeqNumber,
       "dot1agCfmLtrReceiveOrder": dot1agCfmLtrReceiveOrder,
       "dot1agCfmLtrTtl": dot1agCfmLtrTtl,
       "dot1agCfmLtrForwarded": dot1agCfmLtrForwarded,
       "dot1agCfmLtrTerminalMep": dot1agCfmLtrTerminalMep,
       "dot1agCfmLtrLastEgressIdentifier": dot1agCfmLtrLastEgressIdentifier,
       "dot1agCfmLtrNextEgressIdentifier": dot1agCfmLtrNextEgressIdentifier,
       "dot1agCfmLtrRelay": dot1agCfmLtrRelay,
       "dot1agCfmLtrIngress": dot1agCfmLtrIngress,
       "dot1agCfmLtrIngressMac": dot1agCfmLtrIngressMac,
       "dot1agCfmLtrEgress": dot1agCfmLtrEgress,
       "dot1agCfmLtrEgressMac": dot1agCfmLtrEgressMac,
       "dot1agCfmMepDbTable": dot1agCfmMepDbTable,
       "dot1agCfmMepDbEntry": dot1agCfmMepDbEntry,
       "dot1agCfmMepDbRSessionId": dot1agCfmMepDbRSessionId,
       "dot1agCfmMepDbMacAddress": dot1agCfmMepDbMacAddress,
       "dot1agCfmMepDbRdi": dot1agCfmMepDbRdi,
       "dot1agCfmMepDbId": dot1agCfmMepDbId,
       "dot1agCfmLbrInfo": dot1agCfmLbrInfo,
       "dot1agCfmLbrTransId": dot1agCfmLbrTransId,
       "dot1agCfmLbrPrintInfo": dot1agCfmLbrPrintInfo,
       "dot1agCfmMipTable": dot1agCfmMipTable,
       "dot1agCfmMipEntry": dot1agCfmMipEntry,
       "dot1agCfmMipSessionId": dot1agCfmMipSessionId,
       "dot1agCfmMipName": dot1agCfmMipName,
       "dot1agCfmMipPortName": dot1agCfmMipPortName,
       "dot1agCfmGloPara": dot1agCfmGloPara,
       "dot1agCfmGlobalIsEnable": dot1agCfmGlobalIsEnable}
)
