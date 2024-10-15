# SNMP MIB module (APPLETALK-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPLETALK-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:50 2024
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

(cjnProtocol,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnProtocol")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cjnAtalk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4)
)


# Types definitions



class DdpAddress(OctetString):
    """Custom type DdpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnAtGblGroup_ObjectIdentity = ObjectIdentity
cjnAtGblGroup = _CjnAtGblGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 1)
)


class _CjnAtIsEnabled_Type(Integer32):
    """Custom type cjnAtIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CjnAtIsEnabled_Type.__name__ = "Integer32"
_CjnAtIsEnabled_Object = MibScalar
cjnAtIsEnabled = _CjnAtIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 1, 1),
    _CjnAtIsEnabled_Type()
)
cjnAtIsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnAtIsEnabled.setStatus("current")


class _CjnAtGlobalStatsReset_Type(Integer32):
    """Custom type cjnAtGlobalStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CjnAtGlobalStatsReset_Type.__name__ = "Integer32"
_CjnAtGlobalStatsReset_Object = MibScalar
cjnAtGlobalStatsReset = _CjnAtGlobalStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 1, 2),
    _CjnAtGlobalStatsReset_Type()
)
cjnAtGlobalStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnAtGlobalStatsReset.setStatus("current")
_CjnAtIfZoneGroup_ObjectIdentity = ObjectIdentity
cjnAtIfZoneGroup = _CjnAtIfZoneGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 2)
)
_CjnAtIfNextZoneIndex_Type = Integer32
_CjnAtIfNextZoneIndex_Object = MibScalar
cjnAtIfNextZoneIndex = _CjnAtIfNextZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 2, 1),
    _CjnAtIfNextZoneIndex_Type()
)
cjnAtIfNextZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtIfNextZoneIndex.setStatus("current")
_CjnAtIfZoneTable_Object = MibTable
cjnAtIfZoneTable = _CjnAtIfZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    cjnAtIfZoneTable.setStatus("current")
_CjnAtIfZoneEntry_Object = MibTableRow
cjnAtIfZoneEntry = _CjnAtIfZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 2, 2, 1)
)
cjnAtIfZoneEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtPortIndex"),
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtIfZoneIndex"),
)
if mibBuilder.loadTexts:
    cjnAtIfZoneEntry.setStatus("current")
_CjnAtIfZoneIndex_Type = Integer32
_CjnAtIfZoneIndex_Object = MibTableColumn
cjnAtIfZoneIndex = _CjnAtIfZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 2, 2, 1, 1),
    _CjnAtIfZoneIndex_Type()
)
cjnAtIfZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtIfZoneIndex.setStatus("current")


class _CjnAtIfZoneName_Type(OctetString):
    """Custom type cjnAtIfZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CjnAtIfZoneName_Type.__name__ = "OctetString"
_CjnAtIfZoneName_Object = MibTableColumn
cjnAtIfZoneName = _CjnAtIfZoneName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 2, 2, 1, 2),
    _CjnAtIfZoneName_Type()
)
cjnAtIfZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtIfZoneName.setStatus("current")


class _CjnAtIfZoneDefault_Type(Integer32):
    """Custom type cjnAtIfZoneDefault based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("guessed", 3),
          ("no", 2),
          ("yes", 1))
    )


_CjnAtIfZoneDefault_Type.__name__ = "Integer32"
_CjnAtIfZoneDefault_Object = MibTableColumn
cjnAtIfZoneDefault = _CjnAtIfZoneDefault_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 2, 2, 1, 3),
    _CjnAtIfZoneDefault_Type()
)
cjnAtIfZoneDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtIfZoneDefault.setStatus("current")
_CjnAtIfZoneRowStatus_Type = RowStatus
_CjnAtIfZoneRowStatus_Object = MibTableColumn
cjnAtIfZoneRowStatus = _CjnAtIfZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 2, 2, 1, 4),
    _CjnAtIfZoneRowStatus_Type()
)
cjnAtIfZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtIfZoneRowStatus.setStatus("current")
_CjnAtStatRtGroup_ObjectIdentity = ObjectIdentity
cjnAtStatRtGroup = _CjnAtStatRtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 3)
)
_CjnAtStatRtTable_Object = MibTable
cjnAtStatRtTable = _CjnAtStatRtTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cjnAtStatRtTable.setStatus("current")
_CjnAtStatRtEntry_Object = MibTableRow
cjnAtStatRtEntry = _CjnAtStatRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 3, 1, 1)
)
cjnAtStatRtEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtStatRtRangeStart"),
)
if mibBuilder.loadTexts:
    cjnAtStatRtEntry.setStatus("current")
_CjnAtStatRtRangeStart_Type = Integer32
_CjnAtStatRtRangeStart_Object = MibTableColumn
cjnAtStatRtRangeStart = _CjnAtStatRtRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 3, 1, 1, 1),
    _CjnAtStatRtRangeStart_Type()
)
cjnAtStatRtRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtStatRtRangeStart.setStatus("current")
_CjnAtStatRtRangeEnd_Type = Integer32
_CjnAtStatRtRangeEnd_Object = MibTableColumn
cjnAtStatRtRangeEnd = _CjnAtStatRtRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 3, 1, 1, 2),
    _CjnAtStatRtRangeEnd_Type()
)
cjnAtStatRtRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnAtStatRtRangeEnd.setStatus("current")
_CjnAtStatRtRowStatus_Type = RowStatus
_CjnAtStatRtRowStatus_Object = MibTableColumn
cjnAtStatRtRowStatus = _CjnAtStatRtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 3, 1, 1, 3),
    _CjnAtStatRtRowStatus_Type()
)
cjnAtStatRtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnAtStatRtRowStatus.setStatus("current")
_CjnAtStatRtNextHop_Type = DdpAddress
_CjnAtStatRtNextHop_Object = MibTableColumn
cjnAtStatRtNextHop = _CjnAtStatRtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 3, 1, 1, 4),
    _CjnAtStatRtNextHop_Type()
)
cjnAtStatRtNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnAtStatRtNextHop.setStatus("current")


class _CjnAtStatRtType_Type(Integer32):
    """Custom type cjnAtStatRtType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_CjnAtStatRtType_Type.__name__ = "Integer32"
_CjnAtStatRtType_Object = MibTableColumn
cjnAtStatRtType = _CjnAtStatRtType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 3, 1, 1, 5),
    _CjnAtStatRtType_Type()
)
cjnAtStatRtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnAtStatRtType.setStatus("current")
_CjnAtStatRtZoneGroup_ObjectIdentity = ObjectIdentity
cjnAtStatRtZoneGroup = _CjnAtStatRtZoneGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 4)
)
_CjnAtNextStatRtZoneIndex_Type = Integer32
_CjnAtNextStatRtZoneIndex_Object = MibScalar
cjnAtNextStatRtZoneIndex = _CjnAtNextStatRtZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 4, 1),
    _CjnAtNextStatRtZoneIndex_Type()
)
cjnAtNextStatRtZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtNextStatRtZoneIndex.setStatus("current")
_CjnAtStatRtZoneTable_Object = MibTable
cjnAtStatRtZoneTable = _CjnAtStatRtZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    cjnAtStatRtZoneTable.setStatus("current")
_CjnAtStatRtZoneEntry_Object = MibTableRow
cjnAtStatRtZoneEntry = _CjnAtStatRtZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 4, 2, 1)
)
cjnAtStatRtZoneEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtStatRtRangeStart"),
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtStatRtZoneIndex"),
)
if mibBuilder.loadTexts:
    cjnAtStatRtZoneEntry.setStatus("current")
_CjnAtStatRtZoneIndex_Type = Integer32
_CjnAtStatRtZoneIndex_Object = MibTableColumn
cjnAtStatRtZoneIndex = _CjnAtStatRtZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 4, 2, 1, 1),
    _CjnAtStatRtZoneIndex_Type()
)
cjnAtStatRtZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtStatRtZoneIndex.setStatus("current")


class _CjnAtStatRtZoneName_Type(OctetString):
    """Custom type cjnAtStatRtZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CjnAtStatRtZoneName_Type.__name__ = "OctetString"
_CjnAtStatRtZoneName_Object = MibTableColumn
cjnAtStatRtZoneName = _CjnAtStatRtZoneName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 4, 2, 1, 2),
    _CjnAtStatRtZoneName_Type()
)
cjnAtStatRtZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtStatRtZoneName.setStatus("current")
_CjnAtStatRtZoneRowStatus_Type = RowStatus
_CjnAtStatRtZoneRowStatus_Object = MibTableColumn
cjnAtStatRtZoneRowStatus = _CjnAtStatRtZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 4, 2, 1, 3),
    _CjnAtStatRtZoneRowStatus_Type()
)
cjnAtStatRtZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtStatRtZoneRowStatus.setStatus("current")
_CjnAtAarp_ObjectIdentity = ObjectIdentity
cjnAtAarp = _CjnAtAarp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 5)
)


class _CjnAarpReset_Type(Integer32):
    """Custom type cjnAarpReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CjnAarpReset_Type.__name__ = "Integer32"
_CjnAarpReset_Object = MibScalar
cjnAarpReset = _CjnAarpReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 5, 1),
    _CjnAarpReset_Type()
)
cjnAarpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnAarpReset.setStatus("current")
_CjnAarpTable_Object = MibTable
cjnAarpTable = _CjnAarpTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    cjnAarpTable.setStatus("current")
_CjnAarpEntry_Object = MibTableRow
cjnAarpEntry = _CjnAarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 5, 2, 1)
)
cjnAarpEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtPortIfIndex"),
    (0, "APPLETALK-PRIVATE-MIB", "cjnAarpNetAddress"),
)
if mibBuilder.loadTexts:
    cjnAarpEntry.setStatus("current")
_CjnAarpRowStatus_Type = RowStatus
_CjnAarpRowStatus_Object = MibTableColumn
cjnAarpRowStatus = _CjnAarpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 5, 2, 1, 1),
    _CjnAarpRowStatus_Type()
)
cjnAarpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnAarpRowStatus.setStatus("current")
_CjnAarpPhysAddress_Type = OctetString
_CjnAarpPhysAddress_Object = MibTableColumn
cjnAarpPhysAddress = _CjnAarpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 5, 2, 1, 2),
    _CjnAarpPhysAddress_Type()
)
cjnAarpPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAarpPhysAddress.setStatus("current")
_CjnAarpNetAddress_Type = DdpAddress
_CjnAarpNetAddress_Object = MibTableColumn
cjnAarpNetAddress = _CjnAarpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 5, 2, 1, 3),
    _CjnAarpNetAddress_Type()
)
cjnAarpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAarpNetAddress.setStatus("current")
_CjnAarpDescr_Type = DisplayString
_CjnAarpDescr_Object = MibTableColumn
cjnAarpDescr = _CjnAarpDescr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 5, 2, 1, 4),
    _CjnAarpDescr_Type()
)
cjnAarpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAarpDescr.setStatus("current")


class _CjnAarpType_Type(Integer32):
    """Custom type cjnAarpType based on Integer32"""
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
        *(("broadcast", 2),
          ("local", 4),
          ("multicast", 3),
          ("remote", 5),
          ("router", 7),
          ("static", 6),
          ("unknown", 1))
    )


_CjnAarpType_Type.__name__ = "Integer32"
_CjnAarpType_Object = MibTableColumn
cjnAarpType = _CjnAarpType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 5, 2, 1, 5),
    _CjnAarpType_Type()
)
cjnAarpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAarpType.setStatus("current")
_CjnAarpTtl_Type = Integer32
_CjnAarpTtl_Object = MibTableColumn
cjnAarpTtl = _CjnAarpTtl_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 5, 2, 1, 6),
    _CjnAarpTtl_Type()
)
cjnAarpTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAarpTtl.setStatus("current")
_CjnAtRtmp_ObjectIdentity = ObjectIdentity
cjnAtRtmp = _CjnAtRtmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6)
)


class _CjnRtmpReset_Type(Integer32):
    """Custom type cjnRtmpReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CjnRtmpReset_Type.__name__ = "Integer32"
_CjnRtmpReset_Object = MibScalar
cjnRtmpReset = _CjnRtmpReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 1),
    _CjnRtmpReset_Type()
)
cjnRtmpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnRtmpReset.setStatus("current")
_CjnRtmpTable_Object = MibTable
cjnRtmpTable = _CjnRtmpTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 2)
)
if mibBuilder.loadTexts:
    cjnRtmpTable.setStatus("current")
_CjnRtmpEntry_Object = MibTableRow
cjnRtmpEntry = _CjnRtmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 2, 1)
)
cjnRtmpEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnRtmpRangeStart"),
)
if mibBuilder.loadTexts:
    cjnRtmpEntry.setStatus("current")
_CjnRtmpRangeStart_Type = Integer32
_CjnRtmpRangeStart_Object = MibTableColumn
cjnRtmpRangeStart = _CjnRtmpRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 2, 1, 1),
    _CjnRtmpRangeStart_Type()
)
cjnRtmpRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnRtmpRangeStart.setStatus("current")
_CjnRtmpRangeEnd_Type = Integer32
_CjnRtmpRangeEnd_Object = MibTableColumn
cjnRtmpRangeEnd = _CjnRtmpRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 2, 1, 2),
    _CjnRtmpRangeEnd_Type()
)
cjnRtmpRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnRtmpRangeEnd.setStatus("current")
_CjnRtmpNextHop_Type = DdpAddress
_CjnRtmpNextHop_Object = MibTableColumn
cjnRtmpNextHop = _CjnRtmpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 2, 1, 3),
    _CjnRtmpNextHop_Type()
)
cjnRtmpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnRtmpNextHop.setStatus("current")
_CjnRtmpHops_Type = Integer32
_CjnRtmpHops_Object = MibTableColumn
cjnRtmpHops = _CjnRtmpHops_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 2, 1, 4),
    _CjnRtmpHops_Type()
)
cjnRtmpHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnRtmpHops.setStatus("current")


class _CjnRtmpState_Type(Integer32):
    """Custom type cjnRtmpState based on Integer32"""
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
        *(("bad", 4),
          ("goingBad", 3),
          ("good", 1),
          ("suspect", 2))
    )


_CjnRtmpState_Type.__name__ = "Integer32"
_CjnRtmpState_Object = MibTableColumn
cjnRtmpState = _CjnRtmpState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 2, 1, 5),
    _CjnRtmpState_Type()
)
cjnRtmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnRtmpState.setStatus("current")


class _CjnRtmpOwner_Type(Integer32):
    """Custom type cjnRtmpOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 3),
          ("static", 2))
    )


_CjnRtmpOwner_Type.__name__ = "Integer32"
_CjnRtmpOwner_Object = MibTableColumn
cjnRtmpOwner = _CjnRtmpOwner_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 2, 1, 6),
    _CjnRtmpOwner_Type()
)
cjnRtmpOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnRtmpOwner.setStatus("current")
_CjnRtmpDescr_Type = DisplayString
_CjnRtmpDescr_Object = MibTableColumn
cjnRtmpDescr = _CjnRtmpDescr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 2, 1, 7),
    _CjnRtmpDescr_Type()
)
cjnRtmpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnRtmpDescr.setStatus("current")
_CjnRtmpRowStatus_Type = RowStatus
_CjnRtmpRowStatus_Object = MibTableColumn
cjnRtmpRowStatus = _CjnRtmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 6, 2, 1, 8),
    _CjnRtmpRowStatus_Type()
)
cjnRtmpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnRtmpRowStatus.setStatus("current")
_CjnAtZip_ObjectIdentity = ObjectIdentity
cjnAtZip = _CjnAtZip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 7)
)
_CjnZipTable_Object = MibTable
cjnZipTable = _CjnZipTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 7, 1)
)
if mibBuilder.loadTexts:
    cjnZipTable.setStatus("current")
_CjnZipEntry_Object = MibTableRow
cjnZipEntry = _CjnZipEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 7, 1, 1)
)
cjnZipEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnZipZoneNetStart"),
    (0, "APPLETALK-PRIVATE-MIB", "cjnZipZoneIndex"),
)
if mibBuilder.loadTexts:
    cjnZipEntry.setStatus("current")
_CjnZipZoneIndex_Type = Integer32
_CjnZipZoneIndex_Object = MibTableColumn
cjnZipZoneIndex = _CjnZipZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 7, 1, 1, 1),
    _CjnZipZoneIndex_Type()
)
cjnZipZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnZipZoneIndex.setStatus("current")


class _CjnZipZoneName_Type(OctetString):
    """Custom type cjnZipZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CjnZipZoneName_Type.__name__ = "OctetString"
_CjnZipZoneName_Object = MibTableColumn
cjnZipZoneName = _CjnZipZoneName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 7, 1, 1, 2),
    _CjnZipZoneName_Type()
)
cjnZipZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnZipZoneName.setStatus("current")
_CjnZipZoneNetStart_Type = Integer32
_CjnZipZoneNetStart_Object = MibTableColumn
cjnZipZoneNetStart = _CjnZipZoneNetStart_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 7, 1, 1, 3),
    _CjnZipZoneNetStart_Type()
)
cjnZipZoneNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnZipZoneNetStart.setStatus("current")
_CjnZipZoneNetEnd_Type = Integer32
_CjnZipZoneNetEnd_Object = MibTableColumn
cjnZipZoneNetEnd = _CjnZipZoneNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 7, 1, 1, 4),
    _CjnZipZoneNetEnd_Type()
)
cjnZipZoneNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnZipZoneNetEnd.setStatus("current")
_CjnAtNbp_ObjectIdentity = ObjectIdentity
cjnAtNbp = _CjnAtNbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 8)
)
_CjnNbpTable_Object = MibTable
cjnNbpTable = _CjnNbpTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 8, 1)
)
if mibBuilder.loadTexts:
    cjnNbpTable.setStatus("current")
_CjnNbpEntry_Object = MibTableRow
cjnNbpEntry = _CjnNbpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 8, 1, 1)
)
cjnNbpEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnNbpIndex"),
)
if mibBuilder.loadTexts:
    cjnNbpEntry.setStatus("current")
_CjnNbpIndex_Type = Integer32
_CjnNbpIndex_Object = MibTableColumn
cjnNbpIndex = _CjnNbpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 8, 1, 1, 1),
    _CjnNbpIndex_Type()
)
cjnNbpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnNbpIndex.setStatus("current")


class _CjnNbpObject_Type(OctetString):
    """Custom type cjnNbpObject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CjnNbpObject_Type.__name__ = "OctetString"
_CjnNbpObject_Object = MibTableColumn
cjnNbpObject = _CjnNbpObject_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 8, 1, 1, 2),
    _CjnNbpObject_Type()
)
cjnNbpObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnNbpObject.setStatus("current")


class _CjnNbpType_Type(OctetString):
    """Custom type cjnNbpType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CjnNbpType_Type.__name__ = "OctetString"
_CjnNbpType_Object = MibTableColumn
cjnNbpType = _CjnNbpType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 8, 1, 1, 3),
    _CjnNbpType_Type()
)
cjnNbpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnNbpType.setStatus("current")


class _CjnNbpZone_Type(OctetString):
    """Custom type cjnNbpZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CjnNbpZone_Type.__name__ = "OctetString"
_CjnNbpZone_Object = MibTableColumn
cjnNbpZone = _CjnNbpZone_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 8, 1, 1, 4),
    _CjnNbpZone_Type()
)
cjnNbpZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnNbpZone.setStatus("current")


class _CjnNbpState_Type(Integer32):
    """Custom type cjnNbpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_CjnNbpState_Type.__name__ = "Integer32"
_CjnNbpState_Object = MibTableColumn
cjnNbpState = _CjnNbpState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 8, 1, 1, 5),
    _CjnNbpState_Type()
)
cjnNbpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnNbpState.setStatus("current")
_CjnAtEcho_ObjectIdentity = ObjectIdentity
cjnAtEcho = _CjnAtEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 9)
)
_CjnAtEchoRequests_Type = Integer32
_CjnAtEchoRequests_Object = MibScalar
cjnAtEchoRequests = _CjnAtEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 9, 1),
    _CjnAtEchoRequests_Type()
)
cjnAtEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtEchoRequests.setStatus("current")
_CjnAtEchoReplies_Type = Integer32
_CjnAtEchoReplies_Object = MibScalar
cjnAtEchoReplies = _CjnAtEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 9, 2),
    _CjnAtEchoReplies_Type()
)
cjnAtEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtEchoReplies.setStatus("current")
_CjnAtEchoTimeouts_Type = Integer32
_CjnAtEchoTimeouts_Object = MibScalar
cjnAtEchoTimeouts = _CjnAtEchoTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 9, 3),
    _CjnAtEchoTimeouts_Type()
)
cjnAtEchoTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtEchoTimeouts.setStatus("current")
_CjnAtEchoSend_Type = DdpAddress
_CjnAtEchoSend_Object = MibScalar
cjnAtEchoSend = _CjnAtEchoSend_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 9, 4),
    _CjnAtEchoSend_Type()
)
cjnAtEchoSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnAtEchoSend.setStatus("current")


class _CjnAtEchoReset_Type(Integer32):
    """Custom type cjnAtEchoReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CjnAtEchoReset_Type.__name__ = "Integer32"
_CjnAtEchoReset_Object = MibScalar
cjnAtEchoReset = _CjnAtEchoReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 9, 5),
    _CjnAtEchoReset_Type()
)
cjnAtEchoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnAtEchoReset.setStatus("current")
_CjnAtGblStatsGroup_ObjectIdentity = ObjectIdentity
cjnAtGblStatsGroup = _CjnAtGblStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10)
)
_CjnAtDdp_ObjectIdentity = ObjectIdentity
cjnAtDdp = _CjnAtDdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1)
)
_CjnDdpOutRequests_Type = Integer32
_CjnDdpOutRequests_Object = MibScalar
cjnDdpOutRequests = _CjnDdpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 1),
    _CjnDdpOutRequests_Type()
)
cjnDdpOutRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpOutRequests.setStatus("current")
_CjnDdpOutShorts_Type = Integer32
_CjnDdpOutShorts_Object = MibScalar
cjnDdpOutShorts = _CjnDdpOutShorts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 2),
    _CjnDdpOutShorts_Type()
)
cjnDdpOutShorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpOutShorts.setStatus("current")
_CjnDdpOutLongs_Type = Integer32
_CjnDdpOutLongs_Object = MibScalar
cjnDdpOutLongs = _CjnDdpOutLongs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 3),
    _CjnDdpOutLongs_Type()
)
cjnDdpOutLongs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpOutLongs.setStatus("current")
_CjnDdpInReceives_Type = Integer32
_CjnDdpInReceives_Object = MibScalar
cjnDdpInReceives = _CjnDdpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 4),
    _CjnDdpInReceives_Type()
)
cjnDdpInReceives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpInReceives.setStatus("current")
_CjnDdpForwRequests_Type = Integer32
_CjnDdpForwRequests_Object = MibScalar
cjnDdpForwRequests = _CjnDdpForwRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 5),
    _CjnDdpForwRequests_Type()
)
cjnDdpForwRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpForwRequests.setStatus("current")
_CjnDdpInLocalDatagrams_Type = Integer32
_CjnDdpInLocalDatagrams_Object = MibScalar
cjnDdpInLocalDatagrams = _CjnDdpInLocalDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 6),
    _CjnDdpInLocalDatagrams_Type()
)
cjnDdpInLocalDatagrams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpInLocalDatagrams.setStatus("current")
_CjnDdpNoProtocolHandlers_Type = Integer32
_CjnDdpNoProtocolHandlers_Object = MibScalar
cjnDdpNoProtocolHandlers = _CjnDdpNoProtocolHandlers_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 7),
    _CjnDdpNoProtocolHandlers_Type()
)
cjnDdpNoProtocolHandlers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpNoProtocolHandlers.setStatus("current")
_CjnDdpOutNoRoutes_Type = Integer32
_CjnDdpOutNoRoutes_Object = MibScalar
cjnDdpOutNoRoutes = _CjnDdpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 8),
    _CjnDdpOutNoRoutes_Type()
)
cjnDdpOutNoRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpOutNoRoutes.setStatus("current")
_CjnDdpTooShortErrors_Type = Integer32
_CjnDdpTooShortErrors_Object = MibScalar
cjnDdpTooShortErrors = _CjnDdpTooShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 9),
    _CjnDdpTooShortErrors_Type()
)
cjnDdpTooShortErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpTooShortErrors.setStatus("current")
_CjnDdpTooLongErrors_Type = Integer32
_CjnDdpTooLongErrors_Object = MibScalar
cjnDdpTooLongErrors = _CjnDdpTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 10),
    _CjnDdpTooLongErrors_Type()
)
cjnDdpTooLongErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpTooLongErrors.setStatus("current")
_CjnDdpBroadcastErrors_Type = Integer32
_CjnDdpBroadcastErrors_Object = MibScalar
cjnDdpBroadcastErrors = _CjnDdpBroadcastErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 11),
    _CjnDdpBroadcastErrors_Type()
)
cjnDdpBroadcastErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpBroadcastErrors.setStatus("current")
_CjnDdpShortDDPErrors_Type = Integer32
_CjnDdpShortDDPErrors_Object = MibScalar
cjnDdpShortDDPErrors = _CjnDdpShortDDPErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 12),
    _CjnDdpShortDDPErrors_Type()
)
cjnDdpShortDDPErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpShortDDPErrors.setStatus("current")
_CjnDdpHopCountErrors_Type = Integer32
_CjnDdpHopCountErrors_Object = MibScalar
cjnDdpHopCountErrors = _CjnDdpHopCountErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 13),
    _CjnDdpHopCountErrors_Type()
)
cjnDdpHopCountErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpHopCountErrors.setStatus("current")
_CjnDdpChecksumErrors_Type = Integer32
_CjnDdpChecksumErrors_Object = MibScalar
cjnDdpChecksumErrors = _CjnDdpChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 14),
    _CjnDdpChecksumErrors_Type()
)
cjnDdpChecksumErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpChecksumErrors.setStatus("current")
_CjnDdpAarpRqRcv_Type = Integer32
_CjnDdpAarpRqRcv_Object = MibScalar
cjnDdpAarpRqRcv = _CjnDdpAarpRqRcv_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 15),
    _CjnDdpAarpRqRcv_Type()
)
cjnDdpAarpRqRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpAarpRqRcv.setStatus("current")
_CjnDdpAarpReplyRcv_Type = Integer32
_CjnDdpAarpReplyRcv_Object = MibScalar
cjnDdpAarpReplyRcv = _CjnDdpAarpReplyRcv_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 16),
    _CjnDdpAarpReplyRcv_Type()
)
cjnDdpAarpReplyRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpAarpReplyRcv.setStatus("current")
_CjnDdpAarpRqTx_Type = Integer32
_CjnDdpAarpRqTx_Object = MibScalar
cjnDdpAarpRqTx = _CjnDdpAarpRqTx_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 17),
    _CjnDdpAarpRqTx_Type()
)
cjnDdpAarpRqTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpAarpRqTx.setStatus("current")
_CjnDdpAarpReplyTx_Type = Integer32
_CjnDdpAarpReplyTx_Object = MibScalar
cjnDdpAarpReplyTx = _CjnDdpAarpReplyTx_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 18),
    _CjnDdpAarpReplyTx_Type()
)
cjnDdpAarpReplyTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpAarpReplyTx.setStatus("current")
_CjnDdpAarpBadPdu_Type = Integer32
_CjnDdpAarpBadPdu_Object = MibScalar
cjnDdpAarpBadPdu = _CjnDdpAarpBadPdu_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 19),
    _CjnDdpAarpBadPdu_Type()
)
cjnDdpAarpBadPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpAarpBadPdu.setStatus("current")
_CjnDdpCfgAddrError_Type = Integer32
_CjnDdpCfgAddrError_Object = MibScalar
cjnDdpCfgAddrError = _CjnDdpCfgAddrError_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 20),
    _CjnDdpCfgAddrError_Type()
)
cjnDdpCfgAddrError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpCfgAddrError.setStatus("current")
_CjnDdpCfgZoneError_Type = Integer32
_CjnDdpCfgZoneError_Object = MibScalar
cjnDdpCfgZoneError = _CjnDdpCfgZoneError_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 21),
    _CjnDdpCfgZoneError_Type()
)
cjnDdpCfgZoneError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpCfgZoneError.setStatus("current")
_CjnDdpEchoRqRcv_Type = Integer32
_CjnDdpEchoRqRcv_Object = MibScalar
cjnDdpEchoRqRcv = _CjnDdpEchoRqRcv_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 22),
    _CjnDdpEchoRqRcv_Type()
)
cjnDdpEchoRqRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpEchoRqRcv.setStatus("current")
_CjnDdpEchoReplyRcv_Type = Integer32
_CjnDdpEchoReplyRcv_Object = MibScalar
cjnDdpEchoReplyRcv = _CjnDdpEchoReplyRcv_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 23),
    _CjnDdpEchoReplyRcv_Type()
)
cjnDdpEchoReplyRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpEchoReplyRcv.setStatus("current")
_CjnDdpEchoRqTx_Type = Integer32
_CjnDdpEchoRqTx_Object = MibScalar
cjnDdpEchoRqTx = _CjnDdpEchoRqTx_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 10, 1, 24),
    _CjnDdpEchoRqTx_Type()
)
cjnDdpEchoRqTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDdpEchoRqTx.setStatus("current")
_CjnAtPortConfGroup_ObjectIdentity = ObjectIdentity
cjnAtPortConfGroup = _CjnAtPortConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11)
)
_CjnAtPortNextIndex_Type = Integer32
_CjnAtPortNextIndex_Object = MibScalar
cjnAtPortNextIndex = _CjnAtPortNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 1),
    _CjnAtPortNextIndex_Type()
)
cjnAtPortNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtPortNextIndex.setStatus("current")
_CjnAtPortTable_Object = MibTable
cjnAtPortTable = _CjnAtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2)
)
if mibBuilder.loadTexts:
    cjnAtPortTable.setStatus("current")
_CjnAtPortEntry_Object = MibTableRow
cjnAtPortEntry = _CjnAtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1)
)
cjnAtPortEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtPortIndex"),
)
if mibBuilder.loadTexts:
    cjnAtPortEntry.setStatus("current")
_CjnAtPortIndex_Type = Integer32
_CjnAtPortIndex_Object = MibTableColumn
cjnAtPortIndex = _CjnAtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 1),
    _CjnAtPortIndex_Type()
)
cjnAtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtPortIndex.setStatus("current")
_CjnAtPortRowStatus_Type = RowStatus
_CjnAtPortRowStatus_Object = MibTableColumn
cjnAtPortRowStatus = _CjnAtPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 2),
    _CjnAtPortRowStatus_Type()
)
cjnAtPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtPortRowStatus.setStatus("current")


class _CjnAtPortDescr_Type(DisplayString):
    """Custom type cjnAtPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CjnAtPortDescr_Type.__name__ = "DisplayString"
_CjnAtPortDescr_Object = MibTableColumn
cjnAtPortDescr = _CjnAtPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 3),
    _CjnAtPortDescr_Type()
)
cjnAtPortDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtPortDescr.setStatus("current")


class _CjnAtPortMetric_Type(Integer32):
    """Custom type cjnAtPortMetric based on Integer32"""
    defaultValue = 1


_CjnAtPortMetric_Object = MibTableColumn
cjnAtPortMetric = _CjnAtPortMetric_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 4),
    _CjnAtPortMetric_Type()
)
cjnAtPortMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtPortMetric.setStatus("current")


class _CjnAtPortFrameType_Type(Integer32):
    """Custom type cjnAtPortFrameType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet2", 2),
          ("snap", 1))
    )


_CjnAtPortFrameType_Type.__name__ = "Integer32"
_CjnAtPortFrameType_Object = MibTableColumn
cjnAtPortFrameType = _CjnAtPortFrameType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 5),
    _CjnAtPortFrameType_Type()
)
cjnAtPortFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtPortFrameType.setStatus("current")


class _CjnAtPortNetStart_Type(Integer32):
    """Custom type cjnAtPortNetStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_CjnAtPortNetStart_Type.__name__ = "Integer32"
_CjnAtPortNetStart_Object = MibTableColumn
cjnAtPortNetStart = _CjnAtPortNetStart_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 6),
    _CjnAtPortNetStart_Type()
)
cjnAtPortNetStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtPortNetStart.setStatus("current")


class _CjnAtPortNetEnd_Type(Integer32):
    """Custom type cjnAtPortNetEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_CjnAtPortNetEnd_Type.__name__ = "Integer32"
_CjnAtPortNetEnd_Object = MibTableColumn
cjnAtPortNetEnd = _CjnAtPortNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 7),
    _CjnAtPortNetEnd_Type()
)
cjnAtPortNetEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtPortNetEnd.setStatus("current")


class _CjnAtPortNetAddress_Type(DdpAddress):
    """Custom type cjnAtPortNetAddress based on DdpAddress"""
    defaultValue = OctetString("000000")


_CjnAtPortNetAddress_Object = MibTableColumn
cjnAtPortNetAddress = _CjnAtPortNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 8),
    _CjnAtPortNetAddress_Type()
)
cjnAtPortNetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtPortNetAddress.setStatus("current")


class _CjnAtPortAdminState_Type(Integer32):
    """Custom type cjnAtPortAdminState based on Integer32"""
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


_CjnAtPortAdminState_Type.__name__ = "Integer32"
_CjnAtPortAdminState_Object = MibTableColumn
cjnAtPortAdminState = _CjnAtPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 9),
    _CjnAtPortAdminState_Type()
)
cjnAtPortAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtPortAdminState.setStatus("current")
_CjnAtPortIfIndex_Type = Integer32
_CjnAtPortIfIndex_Object = MibTableColumn
cjnAtPortIfIndex = _CjnAtPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 10),
    _CjnAtPortIfIndex_Type()
)
cjnAtPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtPortIfIndex.setStatus("current")


class _CjnAtPortVlan_Type(DisplayString):
    """Custom type cjnAtPortVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CjnAtPortVlan_Type.__name__ = "DisplayString"
_CjnAtPortVlan_Object = MibTableColumn
cjnAtPortVlan = _CjnAtPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 11),
    _CjnAtPortVlan_Type()
)
cjnAtPortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtPortVlan.setStatus("current")


class _CjnAtPortClearZones_Type(Integer32):
    """Custom type cjnAtPortClearZones based on Integer32"""
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


_CjnAtPortClearZones_Type.__name__ = "Integer32"
_CjnAtPortClearZones_Object = MibTableColumn
cjnAtPortClearZones = _CjnAtPortClearZones_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 11, 2, 1, 12),
    _CjnAtPortClearZones_Type()
)
cjnAtPortClearZones.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtPortClearZones.setStatus("current")
_CjnAtPortStateGroup_ObjectIdentity = ObjectIdentity
cjnAtPortStateGroup = _CjnAtPortStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 12)
)
_CjnAtPortStateTable_Object = MibTable
cjnAtPortStateTable = _CjnAtPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 12, 3)
)
if mibBuilder.loadTexts:
    cjnAtPortStateTable.setStatus("current")
_CjnAtPortStateEntry_Object = MibTableRow
cjnAtPortStateEntry = _CjnAtPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 12, 3, 1)
)
cjnAtPortStateEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtPortStateIndex"),
)
if mibBuilder.loadTexts:
    cjnAtPortStateEntry.setStatus("current")
_CjnAtPortStateIndex_Type = Integer32
_CjnAtPortStateIndex_Object = MibTableColumn
cjnAtPortStateIndex = _CjnAtPortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 12, 3, 1, 1),
    _CjnAtPortStateIndex_Type()
)
cjnAtPortStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtPortStateIndex.setStatus("current")
_CjnAtPortStateDescr_Type = DisplayString
_CjnAtPortStateDescr_Object = MibTableColumn
cjnAtPortStateDescr = _CjnAtPortStateDescr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 12, 3, 1, 2),
    _CjnAtPortStateDescr_Type()
)
cjnAtPortStateDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtPortStateDescr.setStatus("current")


class _CjnAtPortStateNetConfig_Type(Integer32):
    """Custom type cjnAtPortStateNetConfig based on Integer32"""
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
        *(("configured", 1),
          ("garnered", 2),
          ("guessed", 3),
          ("unconfigured", 4))
    )


_CjnAtPortStateNetConfig_Type.__name__ = "Integer32"
_CjnAtPortStateNetConfig_Object = MibTableColumn
cjnAtPortStateNetConfig = _CjnAtPortStateNetConfig_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 12, 3, 1, 3),
    _CjnAtPortStateNetConfig_Type()
)
cjnAtPortStateNetConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtPortStateNetConfig.setStatus("current")
_CjnAtPortStateNetStart_Type = Integer32
_CjnAtPortStateNetStart_Object = MibTableColumn
cjnAtPortStateNetStart = _CjnAtPortStateNetStart_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 12, 3, 1, 4),
    _CjnAtPortStateNetStart_Type()
)
cjnAtPortStateNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtPortStateNetStart.setStatus("current")
_CjnAtPortStateNetEnd_Type = Integer32
_CjnAtPortStateNetEnd_Object = MibTableColumn
cjnAtPortStateNetEnd = _CjnAtPortStateNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 12, 3, 1, 5),
    _CjnAtPortStateNetEnd_Type()
)
cjnAtPortStateNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtPortStateNetEnd.setStatus("current")
_CjnAtPortStateNetAddress_Type = DdpAddress
_CjnAtPortStateNetAddress_Object = MibTableColumn
cjnAtPortStateNetAddress = _CjnAtPortStateNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 12, 3, 1, 6),
    _CjnAtPortStateNetAddress_Type()
)
cjnAtPortStateNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtPortStateNetAddress.setStatus("current")


class _CjnAtPortStateState_Type(Integer32):
    """Custom type cjnAtPortStateState based on Integer32"""
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


_CjnAtPortStateState_Type.__name__ = "Integer32"
_CjnAtPortStateState_Object = MibTableColumn
cjnAtPortStateState = _CjnAtPortStateState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 12, 3, 1, 7),
    _CjnAtPortStateState_Type()
)
cjnAtPortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtPortStateState.setStatus("current")
_CjnAtFilterGroup_ObjectIdentity = ObjectIdentity
cjnAtFilterGroup = _CjnAtFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 13)
)
_CjnAtFilterTable_Object = MibTable
cjnAtFilterTable = _CjnAtFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 13, 1)
)
if mibBuilder.loadTexts:
    cjnAtFilterTable.setStatus("current")
_CjnAtFilterEntry_Object = MibTableRow
cjnAtFilterEntry = _CjnAtFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 13, 1, 1)
)
cjnAtFilterEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtFilterIndex"),
)
if mibBuilder.loadTexts:
    cjnAtFilterEntry.setStatus("current")
_CjnAtFilterIndex_Type = Integer32
_CjnAtFilterIndex_Object = MibTableColumn
cjnAtFilterIndex = _CjnAtFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 13, 1, 1, 1),
    _CjnAtFilterIndex_Type()
)
cjnAtFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnAtFilterIndex.setStatus("current")
_CjnAtFilterRowStatus_Type = RowStatus
_CjnAtFilterRowStatus_Object = MibTableColumn
cjnAtFilterRowStatus = _CjnAtFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 13, 1, 1, 2),
    _CjnAtFilterRowStatus_Type()
)
cjnAtFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtFilterRowStatus.setStatus("current")


class _CjnAtFilterItem_Type(Integer32):
    """Custom type cjnAtFilterItem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nbpObject", 2),
          ("zoneName", 1))
    )


_CjnAtFilterItem_Type.__name__ = "Integer32"
_CjnAtFilterItem_Object = MibTableColumn
cjnAtFilterItem = _CjnAtFilterItem_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 13, 1, 1, 3),
    _CjnAtFilterItem_Type()
)
cjnAtFilterItem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtFilterItem.setStatus("current")


class _CjnAtFilterOperation_Type(Integer32):
    """Custom type cjnAtFilterOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_CjnAtFilterOperation_Type.__name__ = "Integer32"
_CjnAtFilterOperation_Object = MibTableColumn
cjnAtFilterOperation = _CjnAtFilterOperation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 13, 1, 1, 4),
    _CjnAtFilterOperation_Type()
)
cjnAtFilterOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtFilterOperation.setStatus("current")


class _CjnAtFilterString_Type(OctetString):
    """Custom type cjnAtFilterString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CjnAtFilterString_Type.__name__ = "OctetString"
_CjnAtFilterString_Object = MibTableColumn
cjnAtFilterString = _CjnAtFilterString_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 13, 1, 1, 5),
    _CjnAtFilterString_Type()
)
cjnAtFilterString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtFilterString.setStatus("current")
_CjnAtAccessIfGroup_ObjectIdentity = ObjectIdentity
cjnAtAccessIfGroup = _CjnAtAccessIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 14)
)
_CjnAtAccessIfTable_Object = MibTable
cjnAtAccessIfTable = _CjnAtAccessIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 14, 1)
)
if mibBuilder.loadTexts:
    cjnAtAccessIfTable.setStatus("current")
_CjnAtAccessIfEntry_Object = MibTableRow
cjnAtAccessIfEntry = _CjnAtAccessIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 14, 1, 1)
)
cjnAtAccessIfEntry.setIndexNames(
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtFilterIndex"),
    (0, "APPLETALK-PRIVATE-MIB", "cjnAtPortIndex"),
)
if mibBuilder.loadTexts:
    cjnAtAccessIfEntry.setStatus("current")
_CjnAtAccessIfRowStatus_Type = RowStatus
_CjnAtAccessIfRowStatus_Object = MibTableColumn
cjnAtAccessIfRowStatus = _CjnAtAccessIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4, 14, 1, 1, 1),
    _CjnAtAccessIfRowStatus_Type()
)
cjnAtAccessIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnAtAccessIfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPLETALK-PRIVATE-MIB",
    **{"DdpAddress": DdpAddress,
       "DisplayString": DisplayString,
       "cjnAtalk": cjnAtalk,
       "cjnAtGblGroup": cjnAtGblGroup,
       "cjnAtIsEnabled": cjnAtIsEnabled,
       "cjnAtGlobalStatsReset": cjnAtGlobalStatsReset,
       "cjnAtIfZoneGroup": cjnAtIfZoneGroup,
       "cjnAtIfNextZoneIndex": cjnAtIfNextZoneIndex,
       "cjnAtIfZoneTable": cjnAtIfZoneTable,
       "cjnAtIfZoneEntry": cjnAtIfZoneEntry,
       "cjnAtIfZoneIndex": cjnAtIfZoneIndex,
       "cjnAtIfZoneName": cjnAtIfZoneName,
       "cjnAtIfZoneDefault": cjnAtIfZoneDefault,
       "cjnAtIfZoneRowStatus": cjnAtIfZoneRowStatus,
       "cjnAtStatRtGroup": cjnAtStatRtGroup,
       "cjnAtStatRtTable": cjnAtStatRtTable,
       "cjnAtStatRtEntry": cjnAtStatRtEntry,
       "cjnAtStatRtRangeStart": cjnAtStatRtRangeStart,
       "cjnAtStatRtRangeEnd": cjnAtStatRtRangeEnd,
       "cjnAtStatRtRowStatus": cjnAtStatRtRowStatus,
       "cjnAtStatRtNextHop": cjnAtStatRtNextHop,
       "cjnAtStatRtType": cjnAtStatRtType,
       "cjnAtStatRtZoneGroup": cjnAtStatRtZoneGroup,
       "cjnAtNextStatRtZoneIndex": cjnAtNextStatRtZoneIndex,
       "cjnAtStatRtZoneTable": cjnAtStatRtZoneTable,
       "cjnAtStatRtZoneEntry": cjnAtStatRtZoneEntry,
       "cjnAtStatRtZoneIndex": cjnAtStatRtZoneIndex,
       "cjnAtStatRtZoneName": cjnAtStatRtZoneName,
       "cjnAtStatRtZoneRowStatus": cjnAtStatRtZoneRowStatus,
       "cjnAtAarp": cjnAtAarp,
       "cjnAarpReset": cjnAarpReset,
       "cjnAarpTable": cjnAarpTable,
       "cjnAarpEntry": cjnAarpEntry,
       "cjnAarpRowStatus": cjnAarpRowStatus,
       "cjnAarpPhysAddress": cjnAarpPhysAddress,
       "cjnAarpNetAddress": cjnAarpNetAddress,
       "cjnAarpDescr": cjnAarpDescr,
       "cjnAarpType": cjnAarpType,
       "cjnAarpTtl": cjnAarpTtl,
       "cjnAtRtmp": cjnAtRtmp,
       "cjnRtmpReset": cjnRtmpReset,
       "cjnRtmpTable": cjnRtmpTable,
       "cjnRtmpEntry": cjnRtmpEntry,
       "cjnRtmpRangeStart": cjnRtmpRangeStart,
       "cjnRtmpRangeEnd": cjnRtmpRangeEnd,
       "cjnRtmpNextHop": cjnRtmpNextHop,
       "cjnRtmpHops": cjnRtmpHops,
       "cjnRtmpState": cjnRtmpState,
       "cjnRtmpOwner": cjnRtmpOwner,
       "cjnRtmpDescr": cjnRtmpDescr,
       "cjnRtmpRowStatus": cjnRtmpRowStatus,
       "cjnAtZip": cjnAtZip,
       "cjnZipTable": cjnZipTable,
       "cjnZipEntry": cjnZipEntry,
       "cjnZipZoneIndex": cjnZipZoneIndex,
       "cjnZipZoneName": cjnZipZoneName,
       "cjnZipZoneNetStart": cjnZipZoneNetStart,
       "cjnZipZoneNetEnd": cjnZipZoneNetEnd,
       "cjnAtNbp": cjnAtNbp,
       "cjnNbpTable": cjnNbpTable,
       "cjnNbpEntry": cjnNbpEntry,
       "cjnNbpIndex": cjnNbpIndex,
       "cjnNbpObject": cjnNbpObject,
       "cjnNbpType": cjnNbpType,
       "cjnNbpZone": cjnNbpZone,
       "cjnNbpState": cjnNbpState,
       "cjnAtEcho": cjnAtEcho,
       "cjnAtEchoRequests": cjnAtEchoRequests,
       "cjnAtEchoReplies": cjnAtEchoReplies,
       "cjnAtEchoTimeouts": cjnAtEchoTimeouts,
       "cjnAtEchoSend": cjnAtEchoSend,
       "cjnAtEchoReset": cjnAtEchoReset,
       "cjnAtGblStatsGroup": cjnAtGblStatsGroup,
       "cjnAtDdp": cjnAtDdp,
       "cjnDdpOutRequests": cjnDdpOutRequests,
       "cjnDdpOutShorts": cjnDdpOutShorts,
       "cjnDdpOutLongs": cjnDdpOutLongs,
       "cjnDdpInReceives": cjnDdpInReceives,
       "cjnDdpForwRequests": cjnDdpForwRequests,
       "cjnDdpInLocalDatagrams": cjnDdpInLocalDatagrams,
       "cjnDdpNoProtocolHandlers": cjnDdpNoProtocolHandlers,
       "cjnDdpOutNoRoutes": cjnDdpOutNoRoutes,
       "cjnDdpTooShortErrors": cjnDdpTooShortErrors,
       "cjnDdpTooLongErrors": cjnDdpTooLongErrors,
       "cjnDdpBroadcastErrors": cjnDdpBroadcastErrors,
       "cjnDdpShortDDPErrors": cjnDdpShortDDPErrors,
       "cjnDdpHopCountErrors": cjnDdpHopCountErrors,
       "cjnDdpChecksumErrors": cjnDdpChecksumErrors,
       "cjnDdpAarpRqRcv": cjnDdpAarpRqRcv,
       "cjnDdpAarpReplyRcv": cjnDdpAarpReplyRcv,
       "cjnDdpAarpRqTx": cjnDdpAarpRqTx,
       "cjnDdpAarpReplyTx": cjnDdpAarpReplyTx,
       "cjnDdpAarpBadPdu": cjnDdpAarpBadPdu,
       "cjnDdpCfgAddrError": cjnDdpCfgAddrError,
       "cjnDdpCfgZoneError": cjnDdpCfgZoneError,
       "cjnDdpEchoRqRcv": cjnDdpEchoRqRcv,
       "cjnDdpEchoReplyRcv": cjnDdpEchoReplyRcv,
       "cjnDdpEchoRqTx": cjnDdpEchoRqTx,
       "cjnAtPortConfGroup": cjnAtPortConfGroup,
       "cjnAtPortNextIndex": cjnAtPortNextIndex,
       "cjnAtPortTable": cjnAtPortTable,
       "cjnAtPortEntry": cjnAtPortEntry,
       "cjnAtPortIndex": cjnAtPortIndex,
       "cjnAtPortRowStatus": cjnAtPortRowStatus,
       "cjnAtPortDescr": cjnAtPortDescr,
       "cjnAtPortMetric": cjnAtPortMetric,
       "cjnAtPortFrameType": cjnAtPortFrameType,
       "cjnAtPortNetStart": cjnAtPortNetStart,
       "cjnAtPortNetEnd": cjnAtPortNetEnd,
       "cjnAtPortNetAddress": cjnAtPortNetAddress,
       "cjnAtPortAdminState": cjnAtPortAdminState,
       "cjnAtPortIfIndex": cjnAtPortIfIndex,
       "cjnAtPortVlan": cjnAtPortVlan,
       "cjnAtPortClearZones": cjnAtPortClearZones,
       "cjnAtPortStateGroup": cjnAtPortStateGroup,
       "cjnAtPortStateTable": cjnAtPortStateTable,
       "cjnAtPortStateEntry": cjnAtPortStateEntry,
       "cjnAtPortStateIndex": cjnAtPortStateIndex,
       "cjnAtPortStateDescr": cjnAtPortStateDescr,
       "cjnAtPortStateNetConfig": cjnAtPortStateNetConfig,
       "cjnAtPortStateNetStart": cjnAtPortStateNetStart,
       "cjnAtPortStateNetEnd": cjnAtPortStateNetEnd,
       "cjnAtPortStateNetAddress": cjnAtPortStateNetAddress,
       "cjnAtPortStateState": cjnAtPortStateState,
       "cjnAtFilterGroup": cjnAtFilterGroup,
       "cjnAtFilterTable": cjnAtFilterTable,
       "cjnAtFilterEntry": cjnAtFilterEntry,
       "cjnAtFilterIndex": cjnAtFilterIndex,
       "cjnAtFilterRowStatus": cjnAtFilterRowStatus,
       "cjnAtFilterItem": cjnAtFilterItem,
       "cjnAtFilterOperation": cjnAtFilterOperation,
       "cjnAtFilterString": cjnAtFilterString,
       "cjnAtAccessIfGroup": cjnAtAccessIfGroup,
       "cjnAtAccessIfTable": cjnAtAccessIfTable,
       "cjnAtAccessIfEntry": cjnAtAccessIfEntry,
       "cjnAtAccessIfRowStatus": cjnAtAccessIfRowStatus}
)
