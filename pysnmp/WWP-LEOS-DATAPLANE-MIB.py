# SNMP MIB module (WWP-LEOS-DATAPLANE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-DATAPLANE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:49 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosDataplaneMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500)
)
wwpLeosDataplaneMIB.setRevisions(
        ("2012-06-08 00:50",
         "2011-06-13 00:50",
         "2011-05-10 00:50",
         "2010-07-28 00:00",
         "2010-02-12 00:00",
         "2008-11-11 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DpTsQSredDropProbability(Integer32, TextualConvention):
    status = "current"
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
        *(("drop-0-0976562-percent", 8),
          ("drop-0-1953125-percent", 7),
          ("drop-0-390625-percent", 6),
          ("drop-0-78125-percent", 5),
          ("drop-1-5625-percent", 4),
          ("drop-100-percent", 1),
          ("drop-3-125-percent", 3),
          ("drop-6-25-percent", 2))
    )



class DpTsQWredSimpleMaxDropProbability(Integer32, TextualConvention):
    status = "current"
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("drop-0-percent", 15),
          ("drop-1-percent", 14),
          ("drop-10-percent", 5),
          ("drop-100-percent", 1),
          ("drop-2-percent", 13),
          ("drop-25-percent", 4),
          ("drop-3-percent", 12),
          ("drop-4-percent", 11),
          ("drop-5-percent", 10),
          ("drop-50-percent", 3),
          ("drop-6-percent", 9),
          ("drop-7-percent", 8),
          ("drop-75-percent", 2),
          ("drop-8-percent", 7),
          ("drop-9-percent", 6))
    )



class DpTsRCosMappingColor(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosDpMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosDpMIBObjects = _WwpLeosDpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1)
)
_WwpLeosDpTs_ObjectIdentity = ObjectIdentity
wwpLeosDpTs = _WwpLeosDpTs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1)
)
_WwpLeosDpTsQueuing_ObjectIdentity = ObjectIdentity
wwpLeosDpTsQueuing = _WwpLeosDpTsQueuing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1)
)
_WwpLeosDpTsQCongestionAvoidanceProfile_ObjectIdentity = ObjectIdentity
wwpLeosDpTsQCongestionAvoidanceProfile = _WwpLeosDpTsQCongestionAvoidanceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1)
)
_WwpLeosDpTsQCAProfileSREDTable_Object = MibTable
wwpLeosDpTsQCAProfileSREDTable = _WwpLeosDpTsQCAProfileSREDTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileSREDTable.setStatus("current")
_WwpLeosDpTsQCAProfileSREDEntry_Object = MibTableRow
wwpLeosDpTsQCAProfileSREDEntry = _WwpLeosDpTsQCAProfileSREDEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 1, 1)
)
wwpLeosDpTsQCAProfileSREDEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsQCAProfileSREDId"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileSREDEntry.setStatus("current")


class _WwpLeosDpTsQCAProfileSREDId_Type(Integer32):
    """Custom type wwpLeosDpTsQCAProfileSREDId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosDpTsQCAProfileSREDId_Type.__name__ = "Integer32"
_WwpLeosDpTsQCAProfileSREDId_Object = MibTableColumn
wwpLeosDpTsQCAProfileSREDId = _WwpLeosDpTsQCAProfileSREDId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 1, 1, 1),
    _WwpLeosDpTsQCAProfileSREDId_Type()
)
wwpLeosDpTsQCAProfileSREDId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileSREDId.setStatus("current")


class _WwpLeosDpTsQCAProfileSREDName_Type(DisplayString):
    """Custom type wwpLeosDpTsQCAProfileSREDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WwpLeosDpTsQCAProfileSREDName_Type.__name__ = "DisplayString"
_WwpLeosDpTsQCAProfileSREDName_Object = MibTableColumn
wwpLeosDpTsQCAProfileSREDName = _WwpLeosDpTsQCAProfileSREDName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 1, 1, 2),
    _WwpLeosDpTsQCAProfileSREDName_Type()
)
wwpLeosDpTsQCAProfileSREDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileSREDName.setStatus("current")
_WwpLeosDpTsQCAProfileSREDGreenThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileSREDGreenThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileSREDGreenThreshold = _WwpLeosDpTsQCAProfileSREDGreenThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 1, 1, 4),
    _WwpLeosDpTsQCAProfileSREDGreenThreshold_Type()
)
wwpLeosDpTsQCAProfileSREDGreenThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileSREDGreenThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileSREDGreenDropProbability_Type = DpTsQSredDropProbability
_WwpLeosDpTsQCAProfileSREDGreenDropProbability_Object = MibTableColumn
wwpLeosDpTsQCAProfileSREDGreenDropProbability = _WwpLeosDpTsQCAProfileSREDGreenDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 1, 1, 5),
    _WwpLeosDpTsQCAProfileSREDGreenDropProbability_Type()
)
wwpLeosDpTsQCAProfileSREDGreenDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileSREDGreenDropProbability.setStatus("current")
_WwpLeosDpTsQCAProfileSREDYellowThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileSREDYellowThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileSREDYellowThreshold = _WwpLeosDpTsQCAProfileSREDYellowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 1, 1, 6),
    _WwpLeosDpTsQCAProfileSREDYellowThreshold_Type()
)
wwpLeosDpTsQCAProfileSREDYellowThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileSREDYellowThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileSREDYellowDropProbability_Type = DpTsQSredDropProbability
_WwpLeosDpTsQCAProfileSREDYellowDropProbability_Object = MibTableColumn
wwpLeosDpTsQCAProfileSREDYellowDropProbability = _WwpLeosDpTsQCAProfileSREDYellowDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 1, 1, 7),
    _WwpLeosDpTsQCAProfileSREDYellowDropProbability_Type()
)
wwpLeosDpTsQCAProfileSREDYellowDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileSREDYellowDropProbability.setStatus("current")
_WwpLeosDpTsQCAProfileSREDRowStatus_Type = RowStatus
_WwpLeosDpTsQCAProfileSREDRowStatus_Object = MibTableColumn
wwpLeosDpTsQCAProfileSREDRowStatus = _WwpLeosDpTsQCAProfileSREDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 1, 1, 9),
    _WwpLeosDpTsQCAProfileSREDRowStatus_Type()
)
wwpLeosDpTsQCAProfileSREDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileSREDRowStatus.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleTable_Object = MibTable
wwpLeosDpTsQCAProfileWREDSimpleTable = _WwpLeosDpTsQCAProfileWREDSimpleTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleTable.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleEntry_Object = MibTableRow
wwpLeosDpTsQCAProfileWREDSimpleEntry = _WwpLeosDpTsQCAProfileWREDSimpleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1)
)
wwpLeosDpTsQCAProfileWREDSimpleEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsQCAProfileWREDSimpleId"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleEntry.setStatus("current")


class _WwpLeosDpTsQCAProfileWREDSimpleId_Type(Integer32):
    """Custom type wwpLeosDpTsQCAProfileWREDSimpleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosDpTsQCAProfileWREDSimpleId_Type.__name__ = "Integer32"
_WwpLeosDpTsQCAProfileWREDSimpleId_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleId = _WwpLeosDpTsQCAProfileWREDSimpleId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 1),
    _WwpLeosDpTsQCAProfileWREDSimpleId_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleId.setStatus("current")


class _WwpLeosDpTsQCAProfileWREDSimpleName_Type(DisplayString):
    """Custom type wwpLeosDpTsQCAProfileWREDSimpleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_WwpLeosDpTsQCAProfileWREDSimpleName_Type.__name__ = "DisplayString"
_WwpLeosDpTsQCAProfileWREDSimpleName_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleName = _WwpLeosDpTsQCAProfileWREDSimpleName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 2),
    _WwpLeosDpTsQCAProfileWREDSimpleName_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleName.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold = _WwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 3),
    _WwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold = _WwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 4),
    _WwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability_Type = DpTsQWredSimpleMaxDropProbability
_WwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability = _WwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 5),
    _WwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold = _WwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 6),
    _WwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold = _WwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 7),
    _WwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability_Type = DpTsQWredSimpleMaxDropProbability
_WwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability = _WwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 8),
    _WwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleRowStatus_Type = RowStatus
_WwpLeosDpTsQCAProfileWREDSimpleRowStatus_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleRowStatus = _WwpLeosDpTsQCAProfileWREDSimpleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 9),
    _WwpLeosDpTsQCAProfileWREDSimpleRowStatus_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleRowStatus.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold = _WwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 10),
    _WwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold = _WwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 11),
    _WwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability_Type = DpTsQWredSimpleMaxDropProbability
_WwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability = _WwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 12),
    _WwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold = _WwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 13),
    _WwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold = _WwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 14),
    _WwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability_Type = DpTsQWredSimpleMaxDropProbability
_WwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability = _WwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 15),
    _WwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold = _WwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 16),
    _WwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold = _WwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 17),
    _WwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability_Type = DpTsQWredSimpleMaxDropProbability
_WwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability = _WwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 18),
    _WwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability.setStatus("current")
_WwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit_Type = Integer32
_WwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit_Object = MibTableColumn
wwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit = _WwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 1, 2, 1, 19),
    _WwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit_Type()
)
wwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroup_ObjectIdentity = ObjectIdentity
wwpLeosDpTsQEgressPortQueueGroup = _WwpLeosDpTsQEgressPortQueueGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2)
)
_WwpLeosDpTsQEgressPortQueueGroupTable_Object = MibTable
wwpLeosDpTsQEgressPortQueueGroupTable = _WwpLeosDpTsQEgressPortQueueGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupTable.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupEntry_Object = MibTableRow
wwpLeosDpTsQEgressPortQueueGroupEntry = _WwpLeosDpTsQEgressPortQueueGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 1, 1)
)
wwpLeosDpTsQEgressPortQueueGroupEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsQEgressPortQueueGroupId"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupEntry.setStatus("current")


class _WwpLeosDpTsQEgressPortQueueGroupId_Type(Integer32):
    """Custom type wwpLeosDpTsQEgressPortQueueGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosDpTsQEgressPortQueueGroupId_Type.__name__ = "Integer32"
_WwpLeosDpTsQEgressPortQueueGroupId_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupId = _WwpLeosDpTsQEgressPortQueueGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 1, 1, 1),
    _WwpLeosDpTsQEgressPortQueueGroupId_Type()
)
wwpLeosDpTsQEgressPortQueueGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupId.setStatus("current")


class _WwpLeosDpTsQEgressPortQueueGroupQCount_Type(Integer32):
    """Custom type wwpLeosDpTsQEgressPortQueueGroupQCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WwpLeosDpTsQEgressPortQueueGroupQCount_Type.__name__ = "Integer32"
_WwpLeosDpTsQEgressPortQueueGroupQCount_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQCount = _WwpLeosDpTsQEgressPortQueueGroupQCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 1, 1, 2),
    _WwpLeosDpTsQEgressPortQueueGroupQCount_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQCount.setStatus("current")


class _WwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm_Type(Integer32):
    """Custom type wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 3),
          ("strictpriority", 1),
          ("unknown", 99),
          ("weighteddeficitroundrobin", 4),
          ("weightedfairqueuing", 2),
          ("weightedroundrobin", 5))
    )


_WwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm_Type.__name__ = "Integer32"
_WwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm = _WwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 1, 1, 3),
    _WwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm_Type()
)
wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupShaperBandwidth_Type = Unsigned32
_WwpLeosDpTsQEgressPortQueueGroupShaperBandwidth_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth = _WwpLeosDpTsQEgressPortQueueGroupShaperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 1, 1, 4),
    _WwpLeosDpTsQEgressPortQueueGroupShaperBandwidth_Type()
)
wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth.setUnits("kbps")


class _WwpLeosDpTsQEgressPortQueueGroupBurstSize_Type(Unsigned32):
    """Custom type wwpLeosDpTsQEgressPortQueueGroupBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 262144),
    )


_WwpLeosDpTsQEgressPortQueueGroupBurstSize_Type.__name__ = "Unsigned32"
_WwpLeosDpTsQEgressPortQueueGroupBurstSize_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupBurstSize = _WwpLeosDpTsQEgressPortQueueGroupBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 1, 1, 5),
    _WwpLeosDpTsQEgressPortQueueGroupBurstSize_Type()
)
wwpLeosDpTsQEgressPortQueueGroupBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupBurstSize.setUnits("kb")


class _WwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity_Type(Unsigned32):
    """Custom type wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1600),
    )


_WwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity_Type.__name__ = "Unsigned32"
_WwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity = _WwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 1, 1, 6),
    _WwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity_Type()
)
wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity.setUnits("kb")
_WwpLeosDpTsQEgressPortQueueGroupQConfigTable_Object = MibTable
wwpLeosDpTsQEgressPortQueueGroupQConfigTable = _WwpLeosDpTsQEgressPortQueueGroupQConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQConfigTable.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQConfigEntry_Object = MibTableRow
wwpLeosDpTsQEgressPortQueueGroupQConfigEntry = _WwpLeosDpTsQEgressPortQueueGroupQConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2, 1)
)
wwpLeosDpTsQEgressPortQueueGroupQConfigEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsQEgressPortQueueGroupId"),
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsQEgressPortQueueGroupQueueId"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQConfigEntry.setStatus("current")


class _WwpLeosDpTsQEgressPortQueueGroupQueueId_Type(Integer32):
    """Custom type wwpLeosDpTsQEgressPortQueueGroupQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsQEgressPortQueueGroupQueueId_Type.__name__ = "Integer32"
_WwpLeosDpTsQEgressPortQueueGroupQueueId_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueId = _WwpLeosDpTsQEgressPortQueueGroupQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2, 1, 1),
    _WwpLeosDpTsQEgressPortQueueGroupQueueId_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueId.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQueueCAPId_Type = Integer32
_WwpLeosDpTsQEgressPortQueueGroupQueueCAPId_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueCAPId = _WwpLeosDpTsQEgressPortQueueGroupQueueCAPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2, 1, 2),
    _WwpLeosDpTsQEgressPortQueueGroupQueueCAPId_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueCAPId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueCAPId.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQueuePriorityId_Type = Unsigned32
_WwpLeosDpTsQEgressPortQueueGroupQueuePriorityId_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueuePriorityId = _WwpLeosDpTsQEgressPortQueueGroupQueuePriorityId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2, 1, 3),
    _WwpLeosDpTsQEgressPortQueueGroupQueuePriorityId_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueuePriorityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueuePriorityId.setStatus("current")


class _WwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight_Type(Unsigned32):
    """Custom type wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight_Type.__name__ = "Unsigned32"
_WwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight = _WwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2, 1, 4),
    _WwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQueueSize_Type = Unsigned32
_WwpLeosDpTsQEgressPortQueueGroupQueueSize_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueSize = _WwpLeosDpTsQEgressPortQueueGroupQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2, 1, 5),
    _WwpLeosDpTsQEgressPortQueueGroupQueueSize_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueSize.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQueueCIR_Type = Unsigned32
_WwpLeosDpTsQEgressPortQueueGroupQueueCIR_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueCIR = _WwpLeosDpTsQEgressPortQueueGroupQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2, 1, 6),
    _WwpLeosDpTsQEgressPortQueueGroupQueueCIR_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueCIR.setStatus("current")


class _WwpLeosDpTsQEgressPortQueueGroupQueueCBS_Type(Unsigned32):
    """Custom type wwpLeosDpTsQEgressPortQueueGroupQueueCBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_WwpLeosDpTsQEgressPortQueueGroupQueueCBS_Type.__name__ = "Unsigned32"
_WwpLeosDpTsQEgressPortQueueGroupQueueCBS_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueCBS = _WwpLeosDpTsQEgressPortQueueGroupQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2, 1, 7),
    _WwpLeosDpTsQEgressPortQueueGroupQueueCBS_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueCBS.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQueueEIR_Type = Unsigned32
_WwpLeosDpTsQEgressPortQueueGroupQueueEIR_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueEIR = _WwpLeosDpTsQEgressPortQueueGroupQueueEIR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2, 1, 8),
    _WwpLeosDpTsQEgressPortQueueGroupQueueEIR_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueEIR.setStatus("current")


class _WwpLeosDpTsQEgressPortQueueGroupQueueEBS_Type(Unsigned32):
    """Custom type wwpLeosDpTsQEgressPortQueueGroupQueueEBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_WwpLeosDpTsQEgressPortQueueGroupQueueEBS_Type.__name__ = "Unsigned32"
_WwpLeosDpTsQEgressPortQueueGroupQueueEBS_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueEBS = _WwpLeosDpTsQEgressPortQueueGroupQueueEBS_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 2, 1, 9),
    _WwpLeosDpTsQEgressPortQueueGroupQueueEBS_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueEBS.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQStatsTable_Object = MibTable
wwpLeosDpTsQEgressPortQueueGroupQStatsTable = _WwpLeosDpTsQEgressPortQueueGroupQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQStatsTable.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQStatsEntry_Object = MibTableRow
wwpLeosDpTsQEgressPortQueueGroupQStatsEntry = _WwpLeosDpTsQEgressPortQueueGroupQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 3, 1)
)
wwpLeosDpTsQEgressPortQueueGroupQStatsEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsQEgressPortQueueGroupId"),
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsQEgressPortQueueGroupStatsQueueId"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQStatsEntry.setStatus("current")


class _WwpLeosDpTsQEgressPortQueueGroupStatsQueueId_Type(Integer32):
    """Custom type wwpLeosDpTsQEgressPortQueueGroupStatsQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsQEgressPortQueueGroupStatsQueueId_Type.__name__ = "Integer32"
_WwpLeosDpTsQEgressPortQueueGroupStatsQueueId_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupStatsQueueId = _WwpLeosDpTsQEgressPortQueueGroupStatsQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 3, 1, 1),
    _WwpLeosDpTsQEgressPortQueueGroupStatsQueueId_Type()
)
wwpLeosDpTsQEgressPortQueueGroupStatsQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupStatsQueueId.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes_Type = Counter64
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes = _WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 3, 1, 2),
    _WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts_Type = Counter64
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts = _WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 3, 1, 3),
    _WwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes_Type = Counter64
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes = _WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 3, 1, 4),
    _WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts_Type = Counter64
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts = _WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 3, 1, 5),
    _WwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts.setStatus("current")
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsClear_Type = TruthValue
_WwpLeosDpTsQEgressPortQueueGroupQueueStatsClear_Object = MibTableColumn
wwpLeosDpTsQEgressPortQueueGroupQueueStatsClear = _WwpLeosDpTsQEgressPortQueueGroupQueueStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 2, 3, 1, 6),
    _WwpLeosDpTsQEgressPortQueueGroupQueueStatsClear_Type()
)
wwpLeosDpTsQEgressPortQueueGroupQueueStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsQEgressPortQueueGroupQueueStatsClear.setStatus("current")
_WwpLeosDpTsQRcosToCosQueueMap_ObjectIdentity = ObjectIdentity
wwpLeosDpTsQRcosToCosQueueMap = _WwpLeosDpTsQRcosToCosQueueMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3)
)
_WwpLeosDpTsQueueMapTable_Object = MibTable
wwpLeosDpTsQueueMapTable = _WwpLeosDpTsQueueMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapTable.setStatus("current")
_WwpLeosDpTsQueueMapEntry_Object = MibTableRow
wwpLeosDpTsQueueMapEntry = _WwpLeosDpTsQueueMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1)
)
wwpLeosDpTsQueueMapEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsQueueMapId"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapEntry.setStatus("current")


class _WwpLeosDpTsQueueMapId_Type(Integer32):
    """Custom type wwpLeosDpTsQueueMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosDpTsQueueMapId_Type.__name__ = "Integer32"
_WwpLeosDpTsQueueMapId_Object = MibTableColumn
wwpLeosDpTsQueueMapId = _WwpLeosDpTsQueueMapId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 1),
    _WwpLeosDpTsQueueMapId_Type()
)
wwpLeosDpTsQueueMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapId.setStatus("current")


class _WwpLeosDpTsQueueMapName_Type(DisplayString):
    """Custom type wwpLeosDpTsQueueMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosDpTsQueueMapName_Type.__name__ = "DisplayString"
_WwpLeosDpTsQueueMapName_Object = MibTableColumn
wwpLeosDpTsQueueMapName = _WwpLeosDpTsQueueMapName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 2),
    _WwpLeosDpTsQueueMapName_Type()
)
wwpLeosDpTsQueueMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapName.setStatus("current")
_WwpLeosDpTsQueueMapQCount_Type = Integer32
_WwpLeosDpTsQueueMapQCount_Object = MibTableColumn
wwpLeosDpTsQueueMapQCount = _WwpLeosDpTsQueueMapQCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 3),
    _WwpLeosDpTsQueueMapQCount_Type()
)
wwpLeosDpTsQueueMapQCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapQCount.setStatus("current")
_WwpLeosDpTsQueueMapRCOS0_Type = Integer32
_WwpLeosDpTsQueueMapRCOS0_Object = MibTableColumn
wwpLeosDpTsQueueMapRCOS0 = _WwpLeosDpTsQueueMapRCOS0_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 4),
    _WwpLeosDpTsQueueMapRCOS0_Type()
)
wwpLeosDpTsQueueMapRCOS0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapRCOS0.setStatus("current")
_WwpLeosDpTsQueueMapRCOS1_Type = Integer32
_WwpLeosDpTsQueueMapRCOS1_Object = MibTableColumn
wwpLeosDpTsQueueMapRCOS1 = _WwpLeosDpTsQueueMapRCOS1_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 5),
    _WwpLeosDpTsQueueMapRCOS1_Type()
)
wwpLeosDpTsQueueMapRCOS1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapRCOS1.setStatus("current")
_WwpLeosDpTsQueueMapRCOS2_Type = Integer32
_WwpLeosDpTsQueueMapRCOS2_Object = MibTableColumn
wwpLeosDpTsQueueMapRCOS2 = _WwpLeosDpTsQueueMapRCOS2_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 6),
    _WwpLeosDpTsQueueMapRCOS2_Type()
)
wwpLeosDpTsQueueMapRCOS2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapRCOS2.setStatus("current")
_WwpLeosDpTsQueueMapRCOS3_Type = Integer32
_WwpLeosDpTsQueueMapRCOS3_Object = MibTableColumn
wwpLeosDpTsQueueMapRCOS3 = _WwpLeosDpTsQueueMapRCOS3_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 7),
    _WwpLeosDpTsQueueMapRCOS3_Type()
)
wwpLeosDpTsQueueMapRCOS3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapRCOS3.setStatus("current")
_WwpLeosDpTsQueueMapRCOS4_Type = Integer32
_WwpLeosDpTsQueueMapRCOS4_Object = MibTableColumn
wwpLeosDpTsQueueMapRCOS4 = _WwpLeosDpTsQueueMapRCOS4_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 8),
    _WwpLeosDpTsQueueMapRCOS4_Type()
)
wwpLeosDpTsQueueMapRCOS4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapRCOS4.setStatus("current")
_WwpLeosDpTsQueueMapRCOS5_Type = Integer32
_WwpLeosDpTsQueueMapRCOS5_Object = MibTableColumn
wwpLeosDpTsQueueMapRCOS5 = _WwpLeosDpTsQueueMapRCOS5_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 9),
    _WwpLeosDpTsQueueMapRCOS5_Type()
)
wwpLeosDpTsQueueMapRCOS5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapRCOS5.setStatus("current")
_WwpLeosDpTsQueueMapRCOS6_Type = Integer32
_WwpLeosDpTsQueueMapRCOS6_Object = MibTableColumn
wwpLeosDpTsQueueMapRCOS6 = _WwpLeosDpTsQueueMapRCOS6_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 10),
    _WwpLeosDpTsQueueMapRCOS6_Type()
)
wwpLeosDpTsQueueMapRCOS6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapRCOS6.setStatus("current")
_WwpLeosDpTsQueueMapRCOS7_Type = Integer32
_WwpLeosDpTsQueueMapRCOS7_Object = MibTableColumn
wwpLeosDpTsQueueMapRCOS7 = _WwpLeosDpTsQueueMapRCOS7_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 11),
    _WwpLeosDpTsQueueMapRCOS7_Type()
)
wwpLeosDpTsQueueMapRCOS7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapRCOS7.setStatus("current")
_WwpLeosDpTsQueueMapRowStatus_Type = RowStatus
_WwpLeosDpTsQueueMapRowStatus_Object = MibTableColumn
wwpLeosDpTsQueueMapRowStatus = _WwpLeosDpTsQueueMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 1, 3, 2, 1, 12),
    _WwpLeosDpTsQueueMapRowStatus_Type()
)
wwpLeosDpTsQueueMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsQueueMapRowStatus.setStatus("current")
_WwpLeosDpTsCosMapping_ObjectIdentity = ObjectIdentity
wwpLeosDpTsCosMapping = _WwpLeosDpTsCosMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2)
)
_WwpLeosDpTsCosMapProfileTable_Object = MibTable
wwpLeosDpTsCosMapProfileTable = _WwpLeosDpTsCosMapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsCosMapProfileTable.setStatus("current")
_WwpLeosDpTsCosMapProfileEntry_Object = MibTableRow
wwpLeosDpTsCosMapProfileEntry = _WwpLeosDpTsCosMapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 1, 1)
)
wwpLeosDpTsCosMapProfileEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsCosMapProfileId"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsCosMapProfileEntry.setStatus("current")


class _WwpLeosDpTsCosMapProfileId_Type(Integer32):
    """Custom type wwpLeosDpTsCosMapProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosDpTsCosMapProfileId_Type.__name__ = "Integer32"
_WwpLeosDpTsCosMapProfileId_Object = MibTableColumn
wwpLeosDpTsCosMapProfileId = _WwpLeosDpTsCosMapProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 1, 1, 1),
    _WwpLeosDpTsCosMapProfileId_Type()
)
wwpLeosDpTsCosMapProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsCosMapProfileId.setStatus("current")


class _WwpLeosDpTsCosMapProfileName_Type(DisplayString):
    """Custom type wwpLeosDpTsCosMapProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WwpLeosDpTsCosMapProfileName_Type.__name__ = "DisplayString"
_WwpLeosDpTsCosMapProfileName_Object = MibTableColumn
wwpLeosDpTsCosMapProfileName = _WwpLeosDpTsCosMapProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 1, 1, 2),
    _WwpLeosDpTsCosMapProfileName_Type()
)
wwpLeosDpTsCosMapProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsCosMapProfileName.setStatus("current")
_WwpLeosDpTsCosMapRowStatus_Type = RowStatus
_WwpLeosDpTsCosMapRowStatus_Object = MibTableColumn
wwpLeosDpTsCosMapRowStatus = _WwpLeosDpTsCosMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 1, 1, 3),
    _WwpLeosDpTsCosMapRowStatus_Type()
)
wwpLeosDpTsCosMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsCosMapRowStatus.setStatus("current")
_WwpLeosDpTsDot1dCosMapTable_Object = MibTable
wwpLeosDpTsDot1dCosMapTable = _WwpLeosDpTsDot1dCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsDot1dCosMapTable.setStatus("deprecated")
_WwpLeosDpTsDot1dCosMapEntry_Object = MibTableRow
wwpLeosDpTsDot1dCosMapEntry = _WwpLeosDpTsDot1dCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 2, 1)
)
wwpLeosDpTsDot1dCosMapEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsCosMapProfileId"),
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsDot1dCosMapDot1dValue"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsDot1dCosMapEntry.setStatus("deprecated")


class _WwpLeosDpTsDot1dCosMapDot1dValue_Type(Integer32):
    """Custom type wwpLeosDpTsDot1dCosMapDot1dValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsDot1dCosMapDot1dValue_Type.__name__ = "Integer32"
_WwpLeosDpTsDot1dCosMapDot1dValue_Object = MibTableColumn
wwpLeosDpTsDot1dCosMapDot1dValue = _WwpLeosDpTsDot1dCosMapDot1dValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 2, 1, 1),
    _WwpLeosDpTsDot1dCosMapDot1dValue_Type()
)
wwpLeosDpTsDot1dCosMapDot1dValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsDot1dCosMapDot1dValue.setStatus("current")


class _WwpLeosDpTsDot1dCosMapRCOS_Type(Integer32):
    """Custom type wwpLeosDpTsDot1dCosMapRCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsDot1dCosMapRCOS_Type.__name__ = "Integer32"
_WwpLeosDpTsDot1dCosMapRCOS_Object = MibTableColumn
wwpLeosDpTsDot1dCosMapRCOS = _WwpLeosDpTsDot1dCosMapRCOS_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 2, 1, 2),
    _WwpLeosDpTsDot1dCosMapRCOS_Type()
)
wwpLeosDpTsDot1dCosMapRCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsDot1dCosMapRCOS.setStatus("current")
_WwpLeosDpTsDscpCosMapTable_Object = MibTable
wwpLeosDpTsDscpCosMapTable = _WwpLeosDpTsDscpCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsDscpCosMapTable.setStatus("current")
_WwpLeosDpTsDscpCosMapEntry_Object = MibTableRow
wwpLeosDpTsDscpCosMapEntry = _WwpLeosDpTsDscpCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 3, 1)
)
wwpLeosDpTsDscpCosMapEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsCosMapProfileId"),
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsDscpCosMapDscpValue"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsDscpCosMapEntry.setStatus("current")


class _WwpLeosDpTsDscpCosMapDscpValue_Type(Integer32):
    """Custom type wwpLeosDpTsDscpCosMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WwpLeosDpTsDscpCosMapDscpValue_Type.__name__ = "Integer32"
_WwpLeosDpTsDscpCosMapDscpValue_Object = MibTableColumn
wwpLeosDpTsDscpCosMapDscpValue = _WwpLeosDpTsDscpCosMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 3, 1, 1),
    _WwpLeosDpTsDscpCosMapDscpValue_Type()
)
wwpLeosDpTsDscpCosMapDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsDscpCosMapDscpValue.setStatus("current")


class _WwpLeosDpTsDscpCosMapRCOS_Type(Integer32):
    """Custom type wwpLeosDpTsDscpCosMapRCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsDscpCosMapRCOS_Type.__name__ = "Integer32"
_WwpLeosDpTsDscpCosMapRCOS_Object = MibTableColumn
wwpLeosDpTsDscpCosMapRCOS = _WwpLeosDpTsDscpCosMapRCOS_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 3, 1, 2),
    _WwpLeosDpTsDscpCosMapRCOS_Type()
)
wwpLeosDpTsDscpCosMapRCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsDscpCosMapRCOS.setStatus("current")
_WwpLeosDpTsDscpCosMapRColorValue_Type = DpTsRCosMappingColor
_WwpLeosDpTsDscpCosMapRColorValue_Object = MibTableColumn
wwpLeosDpTsDscpCosMapRColorValue = _WwpLeosDpTsDscpCosMapRColorValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 3, 1, 3),
    _WwpLeosDpTsDscpCosMapRColorValue_Type()
)
wwpLeosDpTsDscpCosMapRColorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsDscpCosMapRColorValue.setStatus("current")
_WwpLeosDpTsDot1dDeiCosMapTable_Object = MibTable
wwpLeosDpTsDot1dDeiCosMapTable = _WwpLeosDpTsDot1dDeiCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsDot1dDeiCosMapTable.setStatus("current")
_WwpLeosDpTsDot1dDeiCosMapEntry_Object = MibTableRow
wwpLeosDpTsDot1dDeiCosMapEntry = _WwpLeosDpTsDot1dDeiCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 4, 1)
)
wwpLeosDpTsDot1dDeiCosMapEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsCosMapProfileId"),
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsDot1dDeiCosMapDot1dValue"),
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsDot1dDeiCosMapDeiValue"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsDot1dDeiCosMapEntry.setStatus("current")


class _WwpLeosDpTsDot1dDeiCosMapDot1dValue_Type(Integer32):
    """Custom type wwpLeosDpTsDot1dDeiCosMapDot1dValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsDot1dDeiCosMapDot1dValue_Type.__name__ = "Integer32"
_WwpLeosDpTsDot1dDeiCosMapDot1dValue_Object = MibTableColumn
wwpLeosDpTsDot1dDeiCosMapDot1dValue = _WwpLeosDpTsDot1dDeiCosMapDot1dValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 4, 1, 1),
    _WwpLeosDpTsDot1dDeiCosMapDot1dValue_Type()
)
wwpLeosDpTsDot1dDeiCosMapDot1dValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsDot1dDeiCosMapDot1dValue.setStatus("current")


class _WwpLeosDpTsDot1dDeiCosMapDeiValue_Type(Integer32):
    """Custom type wwpLeosDpTsDot1dDeiCosMapDeiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WwpLeosDpTsDot1dDeiCosMapDeiValue_Type.__name__ = "Integer32"
_WwpLeosDpTsDot1dDeiCosMapDeiValue_Object = MibTableColumn
wwpLeosDpTsDot1dDeiCosMapDeiValue = _WwpLeosDpTsDot1dDeiCosMapDeiValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 4, 1, 2),
    _WwpLeosDpTsDot1dDeiCosMapDeiValue_Type()
)
wwpLeosDpTsDot1dDeiCosMapDeiValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsDot1dDeiCosMapDeiValue.setStatus("current")


class _WwpLeosDpTsDot1dDeiCosMapRCosValue_Type(Integer32):
    """Custom type wwpLeosDpTsDot1dDeiCosMapRCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsDot1dDeiCosMapRCosValue_Type.__name__ = "Integer32"
_WwpLeosDpTsDot1dDeiCosMapRCosValue_Object = MibTableColumn
wwpLeosDpTsDot1dDeiCosMapRCosValue = _WwpLeosDpTsDot1dDeiCosMapRCosValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 4, 1, 3),
    _WwpLeosDpTsDot1dDeiCosMapRCosValue_Type()
)
wwpLeosDpTsDot1dDeiCosMapRCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsDot1dDeiCosMapRCosValue.setStatus("current")
_WwpLeosDpTsDot1dDeiCosMapRColorValue_Type = DpTsRCosMappingColor
_WwpLeosDpTsDot1dDeiCosMapRColorValue_Object = MibTableColumn
wwpLeosDpTsDot1dDeiCosMapRColorValue = _WwpLeosDpTsDot1dDeiCosMapRColorValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 4, 1, 4),
    _WwpLeosDpTsDot1dDeiCosMapRColorValue_Type()
)
wwpLeosDpTsDot1dDeiCosMapRColorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsDot1dDeiCosMapRColorValue.setStatus("current")
_WwpLeosDpTsMplsTcCosMapTable_Object = MibTable
wwpLeosDpTsMplsTcCosMapTable = _WwpLeosDpTsMplsTcCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsMplsTcCosMapTable.setStatus("current")
_WwpLeosDpTsMplsTcCosMapEntry_Object = MibTableRow
wwpLeosDpTsMplsTcCosMapEntry = _WwpLeosDpTsMplsTcCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 5, 1)
)
wwpLeosDpTsMplsTcCosMapEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsCosMapProfileId"),
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsMplsTcCosMapMplsTcValue"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsMplsTcCosMapEntry.setStatus("current")


class _WwpLeosDpTsMplsTcCosMapMplsTcValue_Type(Integer32):
    """Custom type wwpLeosDpTsMplsTcCosMapMplsTcValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsMplsTcCosMapMplsTcValue_Type.__name__ = "Integer32"
_WwpLeosDpTsMplsTcCosMapMplsTcValue_Object = MibTableColumn
wwpLeosDpTsMplsTcCosMapMplsTcValue = _WwpLeosDpTsMplsTcCosMapMplsTcValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 5, 1, 1),
    _WwpLeosDpTsMplsTcCosMapMplsTcValue_Type()
)
wwpLeosDpTsMplsTcCosMapMplsTcValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsMplsTcCosMapMplsTcValue.setStatus("current")


class _WwpLeosDpTsMplsTcCosMapRCosValue_Type(Integer32):
    """Custom type wwpLeosDpTsMplsTcCosMapRCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsMplsTcCosMapRCosValue_Type.__name__ = "Integer32"
_WwpLeosDpTsMplsTcCosMapRCosValue_Object = MibTableColumn
wwpLeosDpTsMplsTcCosMapRCosValue = _WwpLeosDpTsMplsTcCosMapRCosValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 5, 1, 2),
    _WwpLeosDpTsMplsTcCosMapRCosValue_Type()
)
wwpLeosDpTsMplsTcCosMapRCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsMplsTcCosMapRCosValue.setStatus("current")
_WwpLeosDpTsMplsTcCosMapRColorValue_Type = DpTsRCosMappingColor
_WwpLeosDpTsMplsTcCosMapRColorValue_Object = MibTableColumn
wwpLeosDpTsMplsTcCosMapRColorValue = _WwpLeosDpTsMplsTcCosMapRColorValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 2, 5, 1, 3),
    _WwpLeosDpTsMplsTcCosMapRColorValue_Type()
)
wwpLeosDpTsMplsTcCosMapRColorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsMplsTcCosMapRColorValue.setStatus("current")
_WwpLeosDpTsFrameCosMapping_ObjectIdentity = ObjectIdentity
wwpLeosDpTsFrameCosMapping = _WwpLeosDpTsFrameCosMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3)
)
_WwpLeosDpTsFrameCosMapProfileTable_Object = MibTable
wwpLeosDpTsFrameCosMapProfileTable = _WwpLeosDpTsFrameCosMapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapProfileTable.setStatus("current")
_WwpLeosDpTsFrameCosMapProfileEntry_Object = MibTableRow
wwpLeosDpTsFrameCosMapProfileEntry = _WwpLeosDpTsFrameCosMapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 1, 1)
)
wwpLeosDpTsFrameCosMapProfileEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsFrameCosMapProfileId"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapProfileEntry.setStatus("current")


class _WwpLeosDpTsFrameCosMapProfileId_Type(Integer32):
    """Custom type wwpLeosDpTsFrameCosMapProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosDpTsFrameCosMapProfileId_Type.__name__ = "Integer32"
_WwpLeosDpTsFrameCosMapProfileId_Object = MibTableColumn
wwpLeosDpTsFrameCosMapProfileId = _WwpLeosDpTsFrameCosMapProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 1, 1, 1),
    _WwpLeosDpTsFrameCosMapProfileId_Type()
)
wwpLeosDpTsFrameCosMapProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapProfileId.setStatus("current")


class _WwpLeosDpTsFrameCosMapProfileName_Type(DisplayString):
    """Custom type wwpLeosDpTsFrameCosMapProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WwpLeosDpTsFrameCosMapProfileName_Type.__name__ = "DisplayString"
_WwpLeosDpTsFrameCosMapProfileName_Object = MibTableColumn
wwpLeosDpTsFrameCosMapProfileName = _WwpLeosDpTsFrameCosMapProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 1, 1, 2),
    _WwpLeosDpTsFrameCosMapProfileName_Type()
)
wwpLeosDpTsFrameCosMapProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapProfileName.setStatus("current")
_WwpLeosDpTsFrameCosMapRowStatus_Type = RowStatus
_WwpLeosDpTsFrameCosMapRowStatus_Object = MibTableColumn
wwpLeosDpTsFrameCosMapRowStatus = _WwpLeosDpTsFrameCosMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 1, 1, 3),
    _WwpLeosDpTsFrameCosMapRowStatus_Type()
)
wwpLeosDpTsFrameCosMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapRowStatus.setStatus("current")
_WwpLeosDpTsFrameCosMapTable_Object = MibTable
wwpLeosDpTsFrameCosMapTable = _WwpLeosDpTsFrameCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapTable.setStatus("current")
_WwpLeosDpTsFrameCosMapEntry_Object = MibTableRow
wwpLeosDpTsFrameCosMapEntry = _WwpLeosDpTsFrameCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 2, 1)
)
wwpLeosDpTsFrameCosMapEntry.setIndexNames(
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsFrameCosMapProfileId"),
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsFrameCosMapRCosValue"),
    (0, "WWP-LEOS-DATAPLANE-MIB", "wwpLeosDpTsFrameCosMapRColorValue"),
)
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapEntry.setStatus("current")


class _WwpLeosDpTsFrameCosMapRCosValue_Type(Integer32):
    """Custom type wwpLeosDpTsFrameCosMapRCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsFrameCosMapRCosValue_Type.__name__ = "Integer32"
_WwpLeosDpTsFrameCosMapRCosValue_Object = MibTableColumn
wwpLeosDpTsFrameCosMapRCosValue = _WwpLeosDpTsFrameCosMapRCosValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 2, 1, 1),
    _WwpLeosDpTsFrameCosMapRCosValue_Type()
)
wwpLeosDpTsFrameCosMapRCosValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapRCosValue.setStatus("current")
_WwpLeosDpTsFrameCosMapRColorValue_Type = DpTsRCosMappingColor
_WwpLeosDpTsFrameCosMapRColorValue_Object = MibTableColumn
wwpLeosDpTsFrameCosMapRColorValue = _WwpLeosDpTsFrameCosMapRColorValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 2, 1, 2),
    _WwpLeosDpTsFrameCosMapRColorValue_Type()
)
wwpLeosDpTsFrameCosMapRColorValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapRColorValue.setStatus("current")


class _WwpLeosDpTsFrameCosMapDot1dValue_Type(Integer32):
    """Custom type wwpLeosDpTsFrameCosMapDot1dValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsFrameCosMapDot1dValue_Type.__name__ = "Integer32"
_WwpLeosDpTsFrameCosMapDot1dValue_Object = MibTableColumn
wwpLeosDpTsFrameCosMapDot1dValue = _WwpLeosDpTsFrameCosMapDot1dValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 2, 1, 3),
    _WwpLeosDpTsFrameCosMapDot1dValue_Type()
)
wwpLeosDpTsFrameCosMapDot1dValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapDot1dValue.setStatus("current")


class _WwpLeosDpTsFrameCosMapDot1dDeiValue_Type(Integer32):
    """Custom type wwpLeosDpTsFrameCosMapDot1dDeiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WwpLeosDpTsFrameCosMapDot1dDeiValue_Type.__name__ = "Integer32"
_WwpLeosDpTsFrameCosMapDot1dDeiValue_Object = MibTableColumn
wwpLeosDpTsFrameCosMapDot1dDeiValue = _WwpLeosDpTsFrameCosMapDot1dDeiValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 2, 1, 4),
    _WwpLeosDpTsFrameCosMapDot1dDeiValue_Type()
)
wwpLeosDpTsFrameCosMapDot1dDeiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapDot1dDeiValue.setStatus("current")


class _WwpLeosDpTsFrameCosMapMplsTcValue_Type(Integer32):
    """Custom type wwpLeosDpTsFrameCosMapMplsTcValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosDpTsFrameCosMapMplsTcValue_Type.__name__ = "Integer32"
_WwpLeosDpTsFrameCosMapMplsTcValue_Object = MibTableColumn
wwpLeosDpTsFrameCosMapMplsTcValue = _WwpLeosDpTsFrameCosMapMplsTcValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 500, 1, 1, 3, 2, 1, 5),
    _WwpLeosDpTsFrameCosMapMplsTcValue_Type()
)
wwpLeosDpTsFrameCosMapMplsTcValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDpTsFrameCosMapMplsTcValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-DATAPLANE-MIB",
    **{"DpTsQSredDropProbability": DpTsQSredDropProbability,
       "DpTsQWredSimpleMaxDropProbability": DpTsQWredSimpleMaxDropProbability,
       "DpTsRCosMappingColor": DpTsRCosMappingColor,
       "wwpLeosDataplaneMIB": wwpLeosDataplaneMIB,
       "wwpLeosDpMIBObjects": wwpLeosDpMIBObjects,
       "wwpLeosDpTs": wwpLeosDpTs,
       "wwpLeosDpTsQueuing": wwpLeosDpTsQueuing,
       "wwpLeosDpTsQCongestionAvoidanceProfile": wwpLeosDpTsQCongestionAvoidanceProfile,
       "wwpLeosDpTsQCAProfileSREDTable": wwpLeosDpTsQCAProfileSREDTable,
       "wwpLeosDpTsQCAProfileSREDEntry": wwpLeosDpTsQCAProfileSREDEntry,
       "wwpLeosDpTsQCAProfileSREDId": wwpLeosDpTsQCAProfileSREDId,
       "wwpLeosDpTsQCAProfileSREDName": wwpLeosDpTsQCAProfileSREDName,
       "wwpLeosDpTsQCAProfileSREDGreenThreshold": wwpLeosDpTsQCAProfileSREDGreenThreshold,
       "wwpLeosDpTsQCAProfileSREDGreenDropProbability": wwpLeosDpTsQCAProfileSREDGreenDropProbability,
       "wwpLeosDpTsQCAProfileSREDYellowThreshold": wwpLeosDpTsQCAProfileSREDYellowThreshold,
       "wwpLeosDpTsQCAProfileSREDYellowDropProbability": wwpLeosDpTsQCAProfileSREDYellowDropProbability,
       "wwpLeosDpTsQCAProfileSREDRowStatus": wwpLeosDpTsQCAProfileSREDRowStatus,
       "wwpLeosDpTsQCAProfileWREDSimpleTable": wwpLeosDpTsQCAProfileWREDSimpleTable,
       "wwpLeosDpTsQCAProfileWREDSimpleEntry": wwpLeosDpTsQCAProfileWREDSimpleEntry,
       "wwpLeosDpTsQCAProfileWREDSimpleId": wwpLeosDpTsQCAProfileWREDSimpleId,
       "wwpLeosDpTsQCAProfileWREDSimpleName": wwpLeosDpTsQCAProfileWREDSimpleName,
       "wwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold": wwpLeosDpTsQCAProfileWREDSimpleTCPGreenThreshold,
       "wwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold": wwpLeosDpTsQCAProfileWREDSimpleTCPGreenUpperThreshold,
       "wwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability": wwpLeosDpTsQCAProfileWREDSimpleTCPGreenMaxDropProbability,
       "wwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold": wwpLeosDpTsQCAProfileWREDSimpleTCPYellowThreshold,
       "wwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold": wwpLeosDpTsQCAProfileWREDSimpleTCPYellowUpperThreshold,
       "wwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability": wwpLeosDpTsQCAProfileWREDSimpleTCPYellowMaxDropProbability,
       "wwpLeosDpTsQCAProfileWREDSimpleRowStatus": wwpLeosDpTsQCAProfileWREDSimpleRowStatus,
       "wwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold": wwpLeosDpTsQCAProfileWREDSimpleNonTCPThreshold,
       "wwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold": wwpLeosDpTsQCAProfileWREDSimpleNonTCPUpperThreshold,
       "wwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability": wwpLeosDpTsQCAProfileWREDSimpleNonTCPMaxDropProbability,
       "wwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold": wwpLeosDpTsQCAProfileWREDSimpleGreenLowerThreshold,
       "wwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold": wwpLeosDpTsQCAProfileWREDSimpleGreenUpperThreshold,
       "wwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability": wwpLeosDpTsQCAProfileWREDSimpleGreenMaxDropProbability,
       "wwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold": wwpLeosDpTsQCAProfileWREDSimpleYellowLowerThreshold,
       "wwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold": wwpLeosDpTsQCAProfileWREDSimpleYellowUpperThreshold,
       "wwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability": wwpLeosDpTsQCAProfileWREDSimpleYellowMaxDropProbability,
       "wwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit": wwpLeosDpTsQCAProfileWREDSimpleYellowAdmitLimit,
       "wwpLeosDpTsQEgressPortQueueGroup": wwpLeosDpTsQEgressPortQueueGroup,
       "wwpLeosDpTsQEgressPortQueueGroupTable": wwpLeosDpTsQEgressPortQueueGroupTable,
       "wwpLeosDpTsQEgressPortQueueGroupEntry": wwpLeosDpTsQEgressPortQueueGroupEntry,
       "wwpLeosDpTsQEgressPortQueueGroupId": wwpLeosDpTsQEgressPortQueueGroupId,
       "wwpLeosDpTsQEgressPortQueueGroupQCount": wwpLeosDpTsQEgressPortQueueGroupQCount,
       "wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm": wwpLeosDpTsQEgressPortQueueGroupSchedulerAlgorithm,
       "wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth": wwpLeosDpTsQEgressPortQueueGroupShaperBandwidth,
       "wwpLeosDpTsQEgressPortQueueGroupBurstSize": wwpLeosDpTsQEgressPortQueueGroupBurstSize,
       "wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity": wwpLeosDpTsQEgressPortQueueGroupWdrrSchedulerGranularity,
       "wwpLeosDpTsQEgressPortQueueGroupQConfigTable": wwpLeosDpTsQEgressPortQueueGroupQConfigTable,
       "wwpLeosDpTsQEgressPortQueueGroupQConfigEntry": wwpLeosDpTsQEgressPortQueueGroupQConfigEntry,
       "wwpLeosDpTsQEgressPortQueueGroupQueueId": wwpLeosDpTsQEgressPortQueueGroupQueueId,
       "wwpLeosDpTsQEgressPortQueueGroupQueueCAPId": wwpLeosDpTsQEgressPortQueueGroupQueueCAPId,
       "wwpLeosDpTsQEgressPortQueueGroupQueuePriorityId": wwpLeosDpTsQEgressPortQueueGroupQueuePriorityId,
       "wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight": wwpLeosDpTsQEgressPortQueueGroupQueueSchedulerWeight,
       "wwpLeosDpTsQEgressPortQueueGroupQueueSize": wwpLeosDpTsQEgressPortQueueGroupQueueSize,
       "wwpLeosDpTsQEgressPortQueueGroupQueueCIR": wwpLeosDpTsQEgressPortQueueGroupQueueCIR,
       "wwpLeosDpTsQEgressPortQueueGroupQueueCBS": wwpLeosDpTsQEgressPortQueueGroupQueueCBS,
       "wwpLeosDpTsQEgressPortQueueGroupQueueEIR": wwpLeosDpTsQEgressPortQueueGroupQueueEIR,
       "wwpLeosDpTsQEgressPortQueueGroupQueueEBS": wwpLeosDpTsQEgressPortQueueGroupQueueEBS,
       "wwpLeosDpTsQEgressPortQueueGroupQStatsTable": wwpLeosDpTsQEgressPortQueueGroupQStatsTable,
       "wwpLeosDpTsQEgressPortQueueGroupQStatsEntry": wwpLeosDpTsQEgressPortQueueGroupQStatsEntry,
       "wwpLeosDpTsQEgressPortQueueGroupStatsQueueId": wwpLeosDpTsQEgressPortQueueGroupStatsQueueId,
       "wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes": wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxBytes,
       "wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts": wwpLeosDpTsQEgressPortQueueGroupQueueStatsTxPkts,
       "wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes": wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedBytes,
       "wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts": wwpLeosDpTsQEgressPortQueueGroupQueueStatsDroppedPkts,
       "wwpLeosDpTsQEgressPortQueueGroupQueueStatsClear": wwpLeosDpTsQEgressPortQueueGroupQueueStatsClear,
       "wwpLeosDpTsQRcosToCosQueueMap": wwpLeosDpTsQRcosToCosQueueMap,
       "wwpLeosDpTsQueueMapTable": wwpLeosDpTsQueueMapTable,
       "wwpLeosDpTsQueueMapEntry": wwpLeosDpTsQueueMapEntry,
       "wwpLeosDpTsQueueMapId": wwpLeosDpTsQueueMapId,
       "wwpLeosDpTsQueueMapName": wwpLeosDpTsQueueMapName,
       "wwpLeosDpTsQueueMapQCount": wwpLeosDpTsQueueMapQCount,
       "wwpLeosDpTsQueueMapRCOS0": wwpLeosDpTsQueueMapRCOS0,
       "wwpLeosDpTsQueueMapRCOS1": wwpLeosDpTsQueueMapRCOS1,
       "wwpLeosDpTsQueueMapRCOS2": wwpLeosDpTsQueueMapRCOS2,
       "wwpLeosDpTsQueueMapRCOS3": wwpLeosDpTsQueueMapRCOS3,
       "wwpLeosDpTsQueueMapRCOS4": wwpLeosDpTsQueueMapRCOS4,
       "wwpLeosDpTsQueueMapRCOS5": wwpLeosDpTsQueueMapRCOS5,
       "wwpLeosDpTsQueueMapRCOS6": wwpLeosDpTsQueueMapRCOS6,
       "wwpLeosDpTsQueueMapRCOS7": wwpLeosDpTsQueueMapRCOS7,
       "wwpLeosDpTsQueueMapRowStatus": wwpLeosDpTsQueueMapRowStatus,
       "wwpLeosDpTsCosMapping": wwpLeosDpTsCosMapping,
       "wwpLeosDpTsCosMapProfileTable": wwpLeosDpTsCosMapProfileTable,
       "wwpLeosDpTsCosMapProfileEntry": wwpLeosDpTsCosMapProfileEntry,
       "wwpLeosDpTsCosMapProfileId": wwpLeosDpTsCosMapProfileId,
       "wwpLeosDpTsCosMapProfileName": wwpLeosDpTsCosMapProfileName,
       "wwpLeosDpTsCosMapRowStatus": wwpLeosDpTsCosMapRowStatus,
       "wwpLeosDpTsDot1dCosMapTable": wwpLeosDpTsDot1dCosMapTable,
       "wwpLeosDpTsDot1dCosMapEntry": wwpLeosDpTsDot1dCosMapEntry,
       "wwpLeosDpTsDot1dCosMapDot1dValue": wwpLeosDpTsDot1dCosMapDot1dValue,
       "wwpLeosDpTsDot1dCosMapRCOS": wwpLeosDpTsDot1dCosMapRCOS,
       "wwpLeosDpTsDscpCosMapTable": wwpLeosDpTsDscpCosMapTable,
       "wwpLeosDpTsDscpCosMapEntry": wwpLeosDpTsDscpCosMapEntry,
       "wwpLeosDpTsDscpCosMapDscpValue": wwpLeosDpTsDscpCosMapDscpValue,
       "wwpLeosDpTsDscpCosMapRCOS": wwpLeosDpTsDscpCosMapRCOS,
       "wwpLeosDpTsDscpCosMapRColorValue": wwpLeosDpTsDscpCosMapRColorValue,
       "wwpLeosDpTsDot1dDeiCosMapTable": wwpLeosDpTsDot1dDeiCosMapTable,
       "wwpLeosDpTsDot1dDeiCosMapEntry": wwpLeosDpTsDot1dDeiCosMapEntry,
       "wwpLeosDpTsDot1dDeiCosMapDot1dValue": wwpLeosDpTsDot1dDeiCosMapDot1dValue,
       "wwpLeosDpTsDot1dDeiCosMapDeiValue": wwpLeosDpTsDot1dDeiCosMapDeiValue,
       "wwpLeosDpTsDot1dDeiCosMapRCosValue": wwpLeosDpTsDot1dDeiCosMapRCosValue,
       "wwpLeosDpTsDot1dDeiCosMapRColorValue": wwpLeosDpTsDot1dDeiCosMapRColorValue,
       "wwpLeosDpTsMplsTcCosMapTable": wwpLeosDpTsMplsTcCosMapTable,
       "wwpLeosDpTsMplsTcCosMapEntry": wwpLeosDpTsMplsTcCosMapEntry,
       "wwpLeosDpTsMplsTcCosMapMplsTcValue": wwpLeosDpTsMplsTcCosMapMplsTcValue,
       "wwpLeosDpTsMplsTcCosMapRCosValue": wwpLeosDpTsMplsTcCosMapRCosValue,
       "wwpLeosDpTsMplsTcCosMapRColorValue": wwpLeosDpTsMplsTcCosMapRColorValue,
       "wwpLeosDpTsFrameCosMapping": wwpLeosDpTsFrameCosMapping,
       "wwpLeosDpTsFrameCosMapProfileTable": wwpLeosDpTsFrameCosMapProfileTable,
       "wwpLeosDpTsFrameCosMapProfileEntry": wwpLeosDpTsFrameCosMapProfileEntry,
       "wwpLeosDpTsFrameCosMapProfileId": wwpLeosDpTsFrameCosMapProfileId,
       "wwpLeosDpTsFrameCosMapProfileName": wwpLeosDpTsFrameCosMapProfileName,
       "wwpLeosDpTsFrameCosMapRowStatus": wwpLeosDpTsFrameCosMapRowStatus,
       "wwpLeosDpTsFrameCosMapTable": wwpLeosDpTsFrameCosMapTable,
       "wwpLeosDpTsFrameCosMapEntry": wwpLeosDpTsFrameCosMapEntry,
       "wwpLeosDpTsFrameCosMapRCosValue": wwpLeosDpTsFrameCosMapRCosValue,
       "wwpLeosDpTsFrameCosMapRColorValue": wwpLeosDpTsFrameCosMapRColorValue,
       "wwpLeosDpTsFrameCosMapDot1dValue": wwpLeosDpTsFrameCosMapDot1dValue,
       "wwpLeosDpTsFrameCosMapDot1dDeiValue": wwpLeosDpTsFrameCosMapDot1dDeiValue,
       "wwpLeosDpTsFrameCosMapMplsTcValue": wwpLeosDpTsFrameCosMapMplsTcValue}
)
