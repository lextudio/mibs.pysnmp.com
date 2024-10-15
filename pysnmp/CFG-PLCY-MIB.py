# SNMP MIB module (CFG-PLCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CFG-PLCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:30 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

sitaraCfgPlcyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 1)
)
sitaraCfgPlcyMIB.setRevisions(
        ("2002-03-06 16:00",
         "2001-11-06 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdmissionState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("drop", 3),
          ("none", 0),
          ("squeeze", 1))
    )



class PolicyStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pending", 2),
          ("running", 1))
    )



class PolicyPriority(Integer32, TextualConvention):
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
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("veryHigh", 5),
          ("veryLow", 1))
    )



class DaysOfWeek(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class TimeAndZone(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d:1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(5, 5),
    )



class PolicyAlias(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )



class PolicyCustomerId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )



class PolicyPathName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )



class TrafficDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("toLan", 0),
          ("toLantoWan", 2),
          ("toWan", 1))
    )



class PolicyDisplayString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class SitaraOwnerString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



# MIB Managed Objects in the order of their OIDs

_Sitara_ObjectIdentity = ObjectIdentity
sitara = _Sitara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302)
)
_SitaraCfg_ObjectIdentity = ObjectIdentity
sitaraCfg = _SitaraCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1)
)
_SitaraCfgPlcy_ObjectIdentity = ObjectIdentity
sitaraCfgPlcy = _SitaraCfgPlcy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1)
)
_SitaraCfgPlcyGenlObjs_ObjectIdentity = ObjectIdentity
sitaraCfgPlcyGenlObjs = _SitaraCfgPlcyGenlObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 2)
)


class _SitaraCfgPlcyVersion_Type(OctetString):
    """Custom type sitaraCfgPlcyVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SitaraCfgPlcyVersion_Type.__name__ = "OctetString"
_SitaraCfgPlcyVersion_Object = MibScalar
sitaraCfgPlcyVersion = _SitaraCfgPlcyVersion_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 2, 1),
    _SitaraCfgPlcyVersion_Type()
)
sitaraCfgPlcyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyVersion.setStatus("current")


class _SitaraCfgPlcyPerRowUpdate_Type(OctetString):
    """Custom type sitaraCfgPlcyPerRowUpdate based on OctetString"""
    defaultValue = 0

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SitaraCfgPlcyPerRowUpdate_Type.__name__ = "OctetString"
_SitaraCfgPlcyPerRowUpdate_Object = MibScalar
sitaraCfgPlcyPerRowUpdate = _SitaraCfgPlcyPerRowUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 2, 2),
    _SitaraCfgPlcyPerRowUpdate_Type()
)
sitaraCfgPlcyPerRowUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitaraCfgPlcyPerRowUpdate.setStatus("current")


class _SitaraCfgPlcyGlobalStorage_Type(Integer32):
    """Custom type sitaraCfgPlcyGlobalStorage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearAllTables", 2),
          ("saveToPerm", 1),
          ("syncRunningPlcy", 3),
          ("unlock", 0))
    )


_SitaraCfgPlcyGlobalStorage_Type.__name__ = "Integer32"
_SitaraCfgPlcyGlobalStorage_Object = MibScalar
sitaraCfgPlcyGlobalStorage = _SitaraCfgPlcyGlobalStorage_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 2, 3),
    _SitaraCfgPlcyGlobalStorage_Type()
)
sitaraCfgPlcyGlobalStorage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGlobalStorage.setStatus("current")
_SitaraCfgPlcyLastUpdateTime_Type = DateAndTime
_SitaraCfgPlcyLastUpdateTime_Object = MibScalar
sitaraCfgPlcyLastUpdateTime = _SitaraCfgPlcyLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 2, 4),
    _SitaraCfgPlcyLastUpdateTime_Type()
)
sitaraCfgPlcyLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLastUpdateTime.setStatus("current")
_SitaraCfgPlcyApplyError_Type = PolicyDisplayString
_SitaraCfgPlcyApplyError_Object = MibScalar
sitaraCfgPlcyApplyError = _SitaraCfgPlcyApplyError_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 2, 5),
    _SitaraCfgPlcyApplyError_Type()
)
sitaraCfgPlcyApplyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyApplyError.setStatus("current")
_SitaraCfgPlcyCrossGroup_ObjectIdentity = ObjectIdentity
sitaraCfgPlcyCrossGroup = _SitaraCfgPlcyCrossGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3)
)
_SitaraCfgPlcyCrossIndexTable_Object = MibTable
sitaraCfgPlcyCrossIndexTable = _SitaraCfgPlcyCrossIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossIndexTable.setStatus("obsolete")
_SitaraCfgPlcyCrossIndexTableEntry_Object = MibTableRow
sitaraCfgPlcyCrossIndexTableEntry = _SitaraCfgPlcyCrossIndexTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1)
)
sitaraCfgPlcyCrossIndexTableEntry.setIndexNames(
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyCrossSchdAlias"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyCrossLinkAlias"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyCrossGroupAlias"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyCrossCbqClassAlias"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyCrossFilterAlias"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyCrossIndex"),
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossIndexTableEntry.setStatus("obsolete")
_SitaraCfgPlcyCrossSchdAlias_Type = PolicyAlias
_SitaraCfgPlcyCrossSchdAlias_Object = MibTableColumn
sitaraCfgPlcyCrossSchdAlias = _SitaraCfgPlcyCrossSchdAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 1),
    _SitaraCfgPlcyCrossSchdAlias_Type()
)
sitaraCfgPlcyCrossSchdAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossSchdAlias.setStatus("obsolete")
_SitaraCfgPlcyCrossLinkAlias_Type = PolicyAlias
_SitaraCfgPlcyCrossLinkAlias_Object = MibTableColumn
sitaraCfgPlcyCrossLinkAlias = _SitaraCfgPlcyCrossLinkAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 2),
    _SitaraCfgPlcyCrossLinkAlias_Type()
)
sitaraCfgPlcyCrossLinkAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossLinkAlias.setStatus("obsolete")
_SitaraCfgPlcyCrossGroupAlias_Type = PolicyAlias
_SitaraCfgPlcyCrossGroupAlias_Object = MibTableColumn
sitaraCfgPlcyCrossGroupAlias = _SitaraCfgPlcyCrossGroupAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 3),
    _SitaraCfgPlcyCrossGroupAlias_Type()
)
sitaraCfgPlcyCrossGroupAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossGroupAlias.setStatus("obsolete")
_SitaraCfgPlcyCrossCbqClassAlias_Type = PolicyAlias
_SitaraCfgPlcyCrossCbqClassAlias_Object = MibTableColumn
sitaraCfgPlcyCrossCbqClassAlias = _SitaraCfgPlcyCrossCbqClassAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 4),
    _SitaraCfgPlcyCrossCbqClassAlias_Type()
)
sitaraCfgPlcyCrossCbqClassAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossCbqClassAlias.setStatus("obsolete")
_SitaraCfgPlcyCrossFilterAlias_Type = PolicyAlias
_SitaraCfgPlcyCrossFilterAlias_Object = MibTableColumn
sitaraCfgPlcyCrossFilterAlias = _SitaraCfgPlcyCrossFilterAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 5),
    _SitaraCfgPlcyCrossFilterAlias_Type()
)
sitaraCfgPlcyCrossFilterAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossFilterAlias.setStatus("obsolete")
_SitaraCfgPlcyCrossIndex_Type = Unsigned32
_SitaraCfgPlcyCrossIndex_Object = MibTableColumn
sitaraCfgPlcyCrossIndex = _SitaraCfgPlcyCrossIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 6),
    _SitaraCfgPlcyCrossIndex_Type()
)
sitaraCfgPlcyCrossIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossIndex.setStatus("obsolete")
_SitaraCfgPlcyCrossSchdIndex_Type = Unsigned32
_SitaraCfgPlcyCrossSchdIndex_Object = MibTableColumn
sitaraCfgPlcyCrossSchdIndex = _SitaraCfgPlcyCrossSchdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 7),
    _SitaraCfgPlcyCrossSchdIndex_Type()
)
sitaraCfgPlcyCrossSchdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossSchdIndex.setStatus("obsolete")
_SitaraCfgPlcyCrossLinkIndex_Type = Unsigned32
_SitaraCfgPlcyCrossLinkIndex_Object = MibTableColumn
sitaraCfgPlcyCrossLinkIndex = _SitaraCfgPlcyCrossLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 8),
    _SitaraCfgPlcyCrossLinkIndex_Type()
)
sitaraCfgPlcyCrossLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossLinkIndex.setStatus("obsolete")
_SitaraCfgPlcyCrossLinkNetDestIndex_Type = Unsigned32
_SitaraCfgPlcyCrossLinkNetDestIndex_Object = MibTableColumn
sitaraCfgPlcyCrossLinkNetDestIndex = _SitaraCfgPlcyCrossLinkNetDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 9),
    _SitaraCfgPlcyCrossLinkNetDestIndex_Type()
)
sitaraCfgPlcyCrossLinkNetDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossLinkNetDestIndex.setStatus("obsolete")
_SitaraCfgPlcyCrossGroupIndex_Type = Unsigned32
_SitaraCfgPlcyCrossGroupIndex_Object = MibTableColumn
sitaraCfgPlcyCrossGroupIndex = _SitaraCfgPlcyCrossGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 10),
    _SitaraCfgPlcyCrossGroupIndex_Type()
)
sitaraCfgPlcyCrossGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossGroupIndex.setStatus("obsolete")
_SitaraCfgPlcyCrossCbqClassIndex_Type = Unsigned32
_SitaraCfgPlcyCrossCbqClassIndex_Object = MibTableColumn
sitaraCfgPlcyCrossCbqClassIndex = _SitaraCfgPlcyCrossCbqClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 11),
    _SitaraCfgPlcyCrossCbqClassIndex_Type()
)
sitaraCfgPlcyCrossCbqClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossCbqClassIndex.setStatus("obsolete")
_SitaraCfgPlcyCrossFilterIndex_Type = Unsigned32
_SitaraCfgPlcyCrossFilterIndex_Object = MibTableColumn
sitaraCfgPlcyCrossFilterIndex = _SitaraCfgPlcyCrossFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 3, 1, 1, 12),
    _SitaraCfgPlcyCrossFilterIndex_Type()
)
sitaraCfgPlcyCrossFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCrossFilterIndex.setStatus("obsolete")
_SitaraCfgPlcySchd_ObjectIdentity = ObjectIdentity
sitaraCfgPlcySchd = _SitaraCfgPlcySchd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4)
)
_SitaraCfgPlcySchdNextIndex_Type = Unsigned32
_SitaraCfgPlcySchdNextIndex_Object = MibScalar
sitaraCfgPlcySchdNextIndex = _SitaraCfgPlcySchdNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 1),
    _SitaraCfgPlcySchdNextIndex_Type()
)
sitaraCfgPlcySchdNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdNextIndex.setStatus("current")
_SitaraCfgPlcySchdTable_Object = MibTable
sitaraCfgPlcySchdTable = _SitaraCfgPlcySchdTable_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdTable.setStatus("current")
_SitaraCfgPlcySchdEntry_Object = MibTableRow
sitaraCfgPlcySchdEntry = _SitaraCfgPlcySchdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 2, 1)
)
sitaraCfgPlcySchdEntry.setIndexNames(
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcySchdIndex"),
)
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdEntry.setStatus("current")
_SitaraCfgPlcySchdIndex_Type = Unsigned32
_SitaraCfgPlcySchdIndex_Object = MibTableColumn
sitaraCfgPlcySchdIndex = _SitaraCfgPlcySchdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 2, 1, 1),
    _SitaraCfgPlcySchdIndex_Type()
)
sitaraCfgPlcySchdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdIndex.setStatus("current")
_SitaraCfgPlcySchdAlias_Type = PolicyAlias
_SitaraCfgPlcySchdAlias_Object = MibTableColumn
sitaraCfgPlcySchdAlias = _SitaraCfgPlcySchdAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 2, 1, 2),
    _SitaraCfgPlcySchdAlias_Type()
)
sitaraCfgPlcySchdAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdAlias.setStatus("current")


class _SitaraCfgPlcySchdDaysOfWeek_Type(DaysOfWeek):
    """Custom type sitaraCfgPlcySchdDaysOfWeek based on DaysOfWeek"""
    defaultValue = 0


_SitaraCfgPlcySchdDaysOfWeek_Object = MibTableColumn
sitaraCfgPlcySchdDaysOfWeek = _SitaraCfgPlcySchdDaysOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 2, 1, 3),
    _SitaraCfgPlcySchdDaysOfWeek_Type()
)
sitaraCfgPlcySchdDaysOfWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdDaysOfWeek.setStatus("current")
_SitaraCfgPlcySchdStartTime_Type = TimeAndZone
_SitaraCfgPlcySchdStartTime_Object = MibTableColumn
sitaraCfgPlcySchdStartTime = _SitaraCfgPlcySchdStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 2, 1, 4),
    _SitaraCfgPlcySchdStartTime_Type()
)
sitaraCfgPlcySchdStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdStartTime.setStatus("current")
_SitaraCfgPlcySchdEndTime_Type = TimeAndZone
_SitaraCfgPlcySchdEndTime_Object = MibTableColumn
sitaraCfgPlcySchdEndTime = _SitaraCfgPlcySchdEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 2, 1, 5),
    _SitaraCfgPlcySchdEndTime_Type()
)
sitaraCfgPlcySchdEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdEndTime.setStatus("current")
_SitaraCfgPlcySchdOwner_Type = SitaraOwnerString
_SitaraCfgPlcySchdOwner_Object = MibTableColumn
sitaraCfgPlcySchdOwner = _SitaraCfgPlcySchdOwner_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 2, 1, 6),
    _SitaraCfgPlcySchdOwner_Type()
)
sitaraCfgPlcySchdOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdOwner.setStatus("current")


class _SitaraCfgPlcySchdPolicyStatus_Type(PolicyStatus):
    """Custom type sitaraCfgPlcySchdPolicyStatus based on PolicyStatus"""


_SitaraCfgPlcySchdPolicyStatus_Object = MibTableColumn
sitaraCfgPlcySchdPolicyStatus = _SitaraCfgPlcySchdPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 2, 1, 7),
    _SitaraCfgPlcySchdPolicyStatus_Type()
)
sitaraCfgPlcySchdPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdPolicyStatus.setStatus("current")
_SitaraCfgPlcySchdStatus_Type = RowStatus
_SitaraCfgPlcySchdStatus_Object = MibTableColumn
sitaraCfgPlcySchdStatus = _SitaraCfgPlcySchdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 4, 2, 1, 8),
    _SitaraCfgPlcySchdStatus_Type()
)
sitaraCfgPlcySchdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcySchdStatus.setStatus("current")
_SitaraCfgPlcyLink_ObjectIdentity = ObjectIdentity
sitaraCfgPlcyLink = _SitaraCfgPlcyLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5)
)
_SitaraCfgPlcyLinkNextIndex_Type = Unsigned32
_SitaraCfgPlcyLinkNextIndex_Object = MibScalar
sitaraCfgPlcyLinkNextIndex = _SitaraCfgPlcyLinkNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 1),
    _SitaraCfgPlcyLinkNextIndex_Type()
)
sitaraCfgPlcyLinkNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkNextIndex.setStatus("current")
_SitaraCfgPlcyLinkTable_Object = MibTable
sitaraCfgPlcyLinkTable = _SitaraCfgPlcyLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkTable.setStatus("current")
_SitaraCfgPlcyLinkEntry_Object = MibTableRow
sitaraCfgPlcyLinkEntry = _SitaraCfgPlcyLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1)
)
sitaraCfgPlcyLinkEntry.setIndexNames(
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcySchdIndex"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyLinkIndex"),
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkEntry.setStatus("current")
_SitaraCfgPlcyLinkIndex_Type = Unsigned32
_SitaraCfgPlcyLinkIndex_Object = MibTableColumn
sitaraCfgPlcyLinkIndex = _SitaraCfgPlcyLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 1),
    _SitaraCfgPlcyLinkIndex_Type()
)
sitaraCfgPlcyLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkIndex.setStatus("current")
_SitaraCfgPlcyLinkAlias_Type = PolicyAlias
_SitaraCfgPlcyLinkAlias_Object = MibTableColumn
sitaraCfgPlcyLinkAlias = _SitaraCfgPlcyLinkAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 2),
    _SitaraCfgPlcyLinkAlias_Type()
)
sitaraCfgPlcyLinkAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkAlias.setStatus("current")
_SitaraCfgPlcyLinkPathName_Type = PolicyPathName
_SitaraCfgPlcyLinkPathName_Object = MibTableColumn
sitaraCfgPlcyLinkPathName = _SitaraCfgPlcyLinkPathName_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 3),
    _SitaraCfgPlcyLinkPathName_Type()
)
sitaraCfgPlcyLinkPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkPathName.setStatus("current")


class _SitaraCfgPlcyLinkEnabled_Type(Integer32):
    """Custom type sitaraCfgPlcyLinkEnabled based on Integer32"""
    defaultValue = 2

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


_SitaraCfgPlcyLinkEnabled_Type.__name__ = "Integer32"
_SitaraCfgPlcyLinkEnabled_Object = MibTableColumn
sitaraCfgPlcyLinkEnabled = _SitaraCfgPlcyLinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 4),
    _SitaraCfgPlcyLinkEnabled_Type()
)
sitaraCfgPlcyLinkEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkEnabled.setStatus("current")
_SitaraCfgPlcyLinkDscr_Type = PolicyDisplayString
_SitaraCfgPlcyLinkDscr_Object = MibTableColumn
sitaraCfgPlcyLinkDscr = _SitaraCfgPlcyLinkDscr_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 5),
    _SitaraCfgPlcyLinkDscr_Type()
)
sitaraCfgPlcyLinkDscr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkDscr.setStatus("current")
_SitaraCfgPlcyLinkLanBandWidth_Type = Gauge32
_SitaraCfgPlcyLinkLanBandWidth_Object = MibTableColumn
sitaraCfgPlcyLinkLanBandWidth = _SitaraCfgPlcyLinkLanBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 6),
    _SitaraCfgPlcyLinkLanBandWidth_Type()
)
sitaraCfgPlcyLinkLanBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkLanBandWidth.setStatus("current")
_SitaraCfgPlcyLinkLanBurst_Type = Gauge32
_SitaraCfgPlcyLinkLanBurst_Object = MibTableColumn
sitaraCfgPlcyLinkLanBurst = _SitaraCfgPlcyLinkLanBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 7),
    _SitaraCfgPlcyLinkLanBurst_Type()
)
sitaraCfgPlcyLinkLanBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkLanBurst.setStatus("current")
_SitaraCfgPlcyLinkLanAvlBandWidth_Type = Gauge32
_SitaraCfgPlcyLinkLanAvlBandWidth_Object = MibTableColumn
sitaraCfgPlcyLinkLanAvlBandWidth = _SitaraCfgPlcyLinkLanAvlBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 8),
    _SitaraCfgPlcyLinkLanAvlBandWidth_Type()
)
sitaraCfgPlcyLinkLanAvlBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkLanAvlBandWidth.setStatus("current")
_SitaraCfgPlcyLinkWanBandWidth_Type = Gauge32
_SitaraCfgPlcyLinkWanBandWidth_Object = MibTableColumn
sitaraCfgPlcyLinkWanBandWidth = _SitaraCfgPlcyLinkWanBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 9),
    _SitaraCfgPlcyLinkWanBandWidth_Type()
)
sitaraCfgPlcyLinkWanBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkWanBandWidth.setStatus("current")
_SitaraCfgPlcyLinkWanBurst_Type = Gauge32
_SitaraCfgPlcyLinkWanBurst_Object = MibTableColumn
sitaraCfgPlcyLinkWanBurst = _SitaraCfgPlcyLinkWanBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 10),
    _SitaraCfgPlcyLinkWanBurst_Type()
)
sitaraCfgPlcyLinkWanBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkWanBurst.setStatus("current")
_SitaraCfgPlcyLinkWanAvlBandWidth_Type = Gauge32
_SitaraCfgPlcyLinkWanAvlBandWidth_Object = MibTableColumn
sitaraCfgPlcyLinkWanAvlBandWidth = _SitaraCfgPlcyLinkWanAvlBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 11),
    _SitaraCfgPlcyLinkWanAvlBandWidth_Type()
)
sitaraCfgPlcyLinkWanAvlBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkWanAvlBandWidth.setStatus("current")
_SitaraCfgPlcyLinkOwner_Type = SitaraOwnerString
_SitaraCfgPlcyLinkOwner_Object = MibTableColumn
sitaraCfgPlcyLinkOwner = _SitaraCfgPlcyLinkOwner_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 12),
    _SitaraCfgPlcyLinkOwner_Type()
)
sitaraCfgPlcyLinkOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkOwner.setStatus("current")


class _SitaraCfgPlcyLinkPolicyStatus_Type(PolicyStatus):
    """Custom type sitaraCfgPlcyLinkPolicyStatus based on PolicyStatus"""


_SitaraCfgPlcyLinkPolicyStatus_Object = MibTableColumn
sitaraCfgPlcyLinkPolicyStatus = _SitaraCfgPlcyLinkPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 13),
    _SitaraCfgPlcyLinkPolicyStatus_Type()
)
sitaraCfgPlcyLinkPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkPolicyStatus.setStatus("current")
_SitaraCfgPlcyLinkStatus_Type = RowStatus
_SitaraCfgPlcyLinkStatus_Object = MibTableColumn
sitaraCfgPlcyLinkStatus = _SitaraCfgPlcyLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 2, 1, 14),
    _SitaraCfgPlcyLinkStatus_Type()
)
sitaraCfgPlcyLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkStatus.setStatus("current")
_SitaraCfgPlcyLinkNetDestNextIndex_Type = Unsigned32
_SitaraCfgPlcyLinkNetDestNextIndex_Object = MibScalar
sitaraCfgPlcyLinkNetDestNextIndex = _SitaraCfgPlcyLinkNetDestNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 3),
    _SitaraCfgPlcyLinkNetDestNextIndex_Type()
)
sitaraCfgPlcyLinkNetDestNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkNetDestNextIndex.setStatus("current")
_SitaraCfgPlcyLinkNetDestTable_Object = MibTable
sitaraCfgPlcyLinkNetDestTable = _SitaraCfgPlcyLinkNetDestTable_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkNetDestTable.setStatus("current")
_SitaraCfgPlcyLinkNetDestEntry_Object = MibTableRow
sitaraCfgPlcyLinkNetDestEntry = _SitaraCfgPlcyLinkNetDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 4, 1)
)
sitaraCfgPlcyLinkNetDestEntry.setIndexNames(
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyLinkNetDestIndex"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyLinkIndex"),
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkNetDestEntry.setStatus("current")
_SitaraCfgPlcyLinkNetDestIndex_Type = Unsigned32
_SitaraCfgPlcyLinkNetDestIndex_Object = MibTableColumn
sitaraCfgPlcyLinkNetDestIndex = _SitaraCfgPlcyLinkNetDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 4, 1, 1),
    _SitaraCfgPlcyLinkNetDestIndex_Type()
)
sitaraCfgPlcyLinkNetDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkNetDestIndex.setStatus("current")
_SitaraCfgPlcyLinkNetDestAddr_Type = IpAddress
_SitaraCfgPlcyLinkNetDestAddr_Object = MibTableColumn
sitaraCfgPlcyLinkNetDestAddr = _SitaraCfgPlcyLinkNetDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 4, 1, 2),
    _SitaraCfgPlcyLinkNetDestAddr_Type()
)
sitaraCfgPlcyLinkNetDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkNetDestAddr.setStatus("current")
_SitaraCfgPlcyLinkNetDestMask_Type = IpAddress
_SitaraCfgPlcyLinkNetDestMask_Object = MibTableColumn
sitaraCfgPlcyLinkNetDestMask = _SitaraCfgPlcyLinkNetDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 4, 1, 3),
    _SitaraCfgPlcyLinkNetDestMask_Type()
)
sitaraCfgPlcyLinkNetDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkNetDestMask.setStatus("current")
_SitaraCfgPlcyLinkNetDestOwner_Type = SitaraOwnerString
_SitaraCfgPlcyLinkNetDestOwner_Object = MibTableColumn
sitaraCfgPlcyLinkNetDestOwner = _SitaraCfgPlcyLinkNetDestOwner_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 4, 1, 4),
    _SitaraCfgPlcyLinkNetDestOwner_Type()
)
sitaraCfgPlcyLinkNetDestOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkNetDestOwner.setStatus("current")
_SitaraCfgPlcyLinkNetDestStatus_Type = RowStatus
_SitaraCfgPlcyLinkNetDestStatus_Object = MibTableColumn
sitaraCfgPlcyLinkNetDestStatus = _SitaraCfgPlcyLinkNetDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 5, 4, 1, 5),
    _SitaraCfgPlcyLinkNetDestStatus_Type()
)
sitaraCfgPlcyLinkNetDestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyLinkNetDestStatus.setStatus("current")
_SitaraCfgPlcyGroup_ObjectIdentity = ObjectIdentity
sitaraCfgPlcyGroup = _SitaraCfgPlcyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6)
)
_SitaraCfgPlcyGroupNextIndex_Type = Unsigned32
_SitaraCfgPlcyGroupNextIndex_Object = MibScalar
sitaraCfgPlcyGroupNextIndex = _SitaraCfgPlcyGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 1),
    _SitaraCfgPlcyGroupNextIndex_Type()
)
sitaraCfgPlcyGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupNextIndex.setStatus("current")
_SitaraCfgPlcyGroupTable_Object = MibTable
sitaraCfgPlcyGroupTable = _SitaraCfgPlcyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupTable.setStatus("current")
_SitaraCfgPlcyGroupEntry_Object = MibTableRow
sitaraCfgPlcyGroupEntry = _SitaraCfgPlcyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1)
)
sitaraCfgPlcyGroupEntry.setIndexNames(
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcySchdIndex"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyLinkIndex"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyGroupIndex"),
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupEntry.setStatus("current")
_SitaraCfgPlcyGroupIndex_Type = Unsigned32
_SitaraCfgPlcyGroupIndex_Object = MibTableColumn
sitaraCfgPlcyGroupIndex = _SitaraCfgPlcyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 1),
    _SitaraCfgPlcyGroupIndex_Type()
)
sitaraCfgPlcyGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupIndex.setStatus("current")
_SitaraCfgPlcyGroupAlias_Type = PolicyAlias
_SitaraCfgPlcyGroupAlias_Object = MibTableColumn
sitaraCfgPlcyGroupAlias = _SitaraCfgPlcyGroupAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 2),
    _SitaraCfgPlcyGroupAlias_Type()
)
sitaraCfgPlcyGroupAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupAlias.setStatus("current")
_SitaraCfgPlcyGroupPathName_Type = PolicyPathName
_SitaraCfgPlcyGroupPathName_Object = MibTableColumn
sitaraCfgPlcyGroupPathName = _SitaraCfgPlcyGroupPathName_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 3),
    _SitaraCfgPlcyGroupPathName_Type()
)
sitaraCfgPlcyGroupPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupPathName.setStatus("current")


class _SitaraCfgPlcyGroupEnabled_Type(Integer32):
    """Custom type sitaraCfgPlcyGroupEnabled based on Integer32"""
    defaultValue = 2

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


_SitaraCfgPlcyGroupEnabled_Type.__name__ = "Integer32"
_SitaraCfgPlcyGroupEnabled_Object = MibTableColumn
sitaraCfgPlcyGroupEnabled = _SitaraCfgPlcyGroupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 4),
    _SitaraCfgPlcyGroupEnabled_Type()
)
sitaraCfgPlcyGroupEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupEnabled.setStatus("current")
_SitaraCfgPlcyGroupDscr_Type = PolicyDisplayString
_SitaraCfgPlcyGroupDscr_Object = MibTableColumn
sitaraCfgPlcyGroupDscr = _SitaraCfgPlcyGroupDscr_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 5),
    _SitaraCfgPlcyGroupDscr_Type()
)
sitaraCfgPlcyGroupDscr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupDscr.setStatus("current")
_SitaraCfgPlcyGroupLanBandWidth_Type = Gauge32
_SitaraCfgPlcyGroupLanBandWidth_Object = MibTableColumn
sitaraCfgPlcyGroupLanBandWidth = _SitaraCfgPlcyGroupLanBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 6),
    _SitaraCfgPlcyGroupLanBandWidth_Type()
)
sitaraCfgPlcyGroupLanBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupLanBandWidth.setStatus("current")
_SitaraCfgPlcyGroupLanBurst_Type = Gauge32
_SitaraCfgPlcyGroupLanBurst_Object = MibTableColumn
sitaraCfgPlcyGroupLanBurst = _SitaraCfgPlcyGroupLanBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 7),
    _SitaraCfgPlcyGroupLanBurst_Type()
)
sitaraCfgPlcyGroupLanBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupLanBurst.setStatus("current")
_SitaraCfgPlcyGroupLanAvlBandWidth_Type = Gauge32
_SitaraCfgPlcyGroupLanAvlBandWidth_Object = MibTableColumn
sitaraCfgPlcyGroupLanAvlBandWidth = _SitaraCfgPlcyGroupLanAvlBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 8),
    _SitaraCfgPlcyGroupLanAvlBandWidth_Type()
)
sitaraCfgPlcyGroupLanAvlBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupLanAvlBandWidth.setStatus("current")
_SitaraCfgPlcyGroupWanBandWidth_Type = Gauge32
_SitaraCfgPlcyGroupWanBandWidth_Object = MibTableColumn
sitaraCfgPlcyGroupWanBandWidth = _SitaraCfgPlcyGroupWanBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 9),
    _SitaraCfgPlcyGroupWanBandWidth_Type()
)
sitaraCfgPlcyGroupWanBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupWanBandWidth.setStatus("current")
_SitaraCfgPlcyGroupWanBurst_Type = Gauge32
_SitaraCfgPlcyGroupWanBurst_Object = MibTableColumn
sitaraCfgPlcyGroupWanBurst = _SitaraCfgPlcyGroupWanBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 10),
    _SitaraCfgPlcyGroupWanBurst_Type()
)
sitaraCfgPlcyGroupWanBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupWanBurst.setStatus("current")
_SitaraCfgPlcyGroupWanAvlBandWidth_Type = Gauge32
_SitaraCfgPlcyGroupWanAvlBandWidth_Object = MibTableColumn
sitaraCfgPlcyGroupWanAvlBandWidth = _SitaraCfgPlcyGroupWanAvlBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 11),
    _SitaraCfgPlcyGroupWanAvlBandWidth_Type()
)
sitaraCfgPlcyGroupWanAvlBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupWanAvlBandWidth.setStatus("current")
_SitaraCfgPlcyGroupDirection_Type = TrafficDirection
_SitaraCfgPlcyGroupDirection_Object = MibTableColumn
sitaraCfgPlcyGroupDirection = _SitaraCfgPlcyGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 12),
    _SitaraCfgPlcyGroupDirection_Type()
)
sitaraCfgPlcyGroupDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupDirection.setStatus("current")


class _SitaraCfgPlcyGroupParentIndex_Type(Unsigned32):
    """Custom type sitaraCfgPlcyGroupParentIndex based on Unsigned32"""
    defaultValue = 0


_SitaraCfgPlcyGroupParentIndex_Object = MibTableColumn
sitaraCfgPlcyGroupParentIndex = _SitaraCfgPlcyGroupParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 13),
    _SitaraCfgPlcyGroupParentIndex_Type()
)
sitaraCfgPlcyGroupParentIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupParentIndex.setStatus("current")
_SitaraCfgPlcyGroupOwner_Type = SitaraOwnerString
_SitaraCfgPlcyGroupOwner_Object = MibTableColumn
sitaraCfgPlcyGroupOwner = _SitaraCfgPlcyGroupOwner_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 14),
    _SitaraCfgPlcyGroupOwner_Type()
)
sitaraCfgPlcyGroupOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupOwner.setStatus("current")


class _SitaraCfgPlcyGroupPolicyStatus_Type(PolicyStatus):
    """Custom type sitaraCfgPlcyGroupPolicyStatus based on PolicyStatus"""


_SitaraCfgPlcyGroupPolicyStatus_Object = MibTableColumn
sitaraCfgPlcyGroupPolicyStatus = _SitaraCfgPlcyGroupPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 15),
    _SitaraCfgPlcyGroupPolicyStatus_Type()
)
sitaraCfgPlcyGroupPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupPolicyStatus.setStatus("current")
_SitaraCfgPlcyGroupStatus_Type = RowStatus
_SitaraCfgPlcyGroupStatus_Object = MibTableColumn
sitaraCfgPlcyGroupStatus = _SitaraCfgPlcyGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 6, 2, 1, 16),
    _SitaraCfgPlcyGroupStatus_Type()
)
sitaraCfgPlcyGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyGroupStatus.setStatus("current")
_SitaraCfgPlcyAction_ObjectIdentity = ObjectIdentity
sitaraCfgPlcyAction = _SitaraCfgPlcyAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7)
)
_SitaraCfgPlcyQClass_ObjectIdentity = ObjectIdentity
sitaraCfgPlcyQClass = _SitaraCfgPlcyQClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1)
)
_SitaraCfgPlcyCbqClass_ObjectIdentity = ObjectIdentity
sitaraCfgPlcyCbqClass = _SitaraCfgPlcyCbqClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1)
)
_SitaraCfgPlcyCbqClassNextIndex_Type = Unsigned32
_SitaraCfgPlcyCbqClassNextIndex_Object = MibScalar
sitaraCfgPlcyCbqClassNextIndex = _SitaraCfgPlcyCbqClassNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 1),
    _SitaraCfgPlcyCbqClassNextIndex_Type()
)
sitaraCfgPlcyCbqClassNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassNextIndex.setStatus("current")
_SitaraCfgPlcyCbqClassTable_Object = MibTable
sitaraCfgPlcyCbqClassTable = _SitaraCfgPlcyCbqClassTable_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassTable.setStatus("current")
_SitaraCfgPlcyCbqClassEntry_Object = MibTableRow
sitaraCfgPlcyCbqClassEntry = _SitaraCfgPlcyCbqClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1)
)
sitaraCfgPlcyCbqClassEntry.setIndexNames(
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcySchdIndex"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyLinkIndex"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyGroupIndex"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassIndex"),
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassEntry.setStatus("current")
_SitaraCfgPlcyCbqClassIndex_Type = Unsigned32
_SitaraCfgPlcyCbqClassIndex_Object = MibTableColumn
sitaraCfgPlcyCbqClassIndex = _SitaraCfgPlcyCbqClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 1),
    _SitaraCfgPlcyCbqClassIndex_Type()
)
sitaraCfgPlcyCbqClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassIndex.setStatus("current")
_SitaraCfgPlcyCbqClassAlias_Type = PolicyAlias
_SitaraCfgPlcyCbqClassAlias_Object = MibTableColumn
sitaraCfgPlcyCbqClassAlias = _SitaraCfgPlcyCbqClassAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 2),
    _SitaraCfgPlcyCbqClassAlias_Type()
)
sitaraCfgPlcyCbqClassAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassAlias.setStatus("current")
_SitaraCfgPlcyCbqClassPathName_Type = PolicyPathName
_SitaraCfgPlcyCbqClassPathName_Object = MibTableColumn
sitaraCfgPlcyCbqClassPathName = _SitaraCfgPlcyCbqClassPathName_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 3),
    _SitaraCfgPlcyCbqClassPathName_Type()
)
sitaraCfgPlcyCbqClassPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassPathName.setStatus("current")


class _SitaraCfgPlcyCbqClassEnabled_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassEnabled based on Integer32"""
    defaultValue = 2

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


_SitaraCfgPlcyCbqClassEnabled_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassEnabled_Object = MibTableColumn
sitaraCfgPlcyCbqClassEnabled = _SitaraCfgPlcyCbqClassEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 4),
    _SitaraCfgPlcyCbqClassEnabled_Type()
)
sitaraCfgPlcyCbqClassEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassEnabled.setStatus("current")
_SitaraCfgPlcyCbqClassLanBandWidth_Type = Gauge32
_SitaraCfgPlcyCbqClassLanBandWidth_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanBandWidth = _SitaraCfgPlcyCbqClassLanBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 5),
    _SitaraCfgPlcyCbqClassLanBandWidth_Type()
)
sitaraCfgPlcyCbqClassLanBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanBandWidth.setStatus("current")
_SitaraCfgPlcyCbqClassLanBurst_Type = Gauge32
_SitaraCfgPlcyCbqClassLanBurst_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanBurst = _SitaraCfgPlcyCbqClassLanBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 6),
    _SitaraCfgPlcyCbqClassLanBurst_Type()
)
sitaraCfgPlcyCbqClassLanBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanBurst.setStatus("current")
_SitaraCfgPlcyCbqClassLanPriority_Type = PolicyPriority
_SitaraCfgPlcyCbqClassLanPriority_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanPriority = _SitaraCfgPlcyCbqClassLanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 7),
    _SitaraCfgPlcyCbqClassLanPriority_Type()
)
sitaraCfgPlcyCbqClassLanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanPriority.setStatus("current")
_SitaraCfgPlcyCbqClassLanSessionBw_Type = Gauge32
_SitaraCfgPlcyCbqClassLanSessionBw_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanSessionBw = _SitaraCfgPlcyCbqClassLanSessionBw_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 8),
    _SitaraCfgPlcyCbqClassLanSessionBw_Type()
)
sitaraCfgPlcyCbqClassLanSessionBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanSessionBw.setStatus("current")
_SitaraCfgPlcyCbqClassLanAdminCtrl_Type = AdmissionState
_SitaraCfgPlcyCbqClassLanAdminCtrl_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanAdminCtrl = _SitaraCfgPlcyCbqClassLanAdminCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 9),
    _SitaraCfgPlcyCbqClassLanAdminCtrl_Type()
)
sitaraCfgPlcyCbqClassLanAdminCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanAdminCtrl.setStatus("current")


class _SitaraCfgPlcyCbqClassLanHttpCaching_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassLanHttpCaching based on Integer32"""
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


_SitaraCfgPlcyCbqClassLanHttpCaching_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassLanHttpCaching_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanHttpCaching = _SitaraCfgPlcyCbqClassLanHttpCaching_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 10),
    _SitaraCfgPlcyCbqClassLanHttpCaching_Type()
)
sitaraCfgPlcyCbqClassLanHttpCaching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanHttpCaching.setStatus("current")


class _SitaraCfgPlcyCbqClassLanTosEnabled_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassLanTosEnabled based on Integer32"""
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


_SitaraCfgPlcyCbqClassLanTosEnabled_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassLanTosEnabled_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanTosEnabled = _SitaraCfgPlcyCbqClassLanTosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 11),
    _SitaraCfgPlcyCbqClassLanTosEnabled_Type()
)
sitaraCfgPlcyCbqClassLanTosEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanTosEnabled.setStatus("current")


class _SitaraCfgPlcyCbqClassLanTosValue_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassLanTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SitaraCfgPlcyCbqClassLanTosValue_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassLanTosValue_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanTosValue = _SitaraCfgPlcyCbqClassLanTosValue_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 12),
    _SitaraCfgPlcyCbqClassLanTosValue_Type()
)
sitaraCfgPlcyCbqClassLanTosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanTosValue.setStatus("current")


class _SitaraCfgPlcyCbqClassLanTosMask_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassLanTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SitaraCfgPlcyCbqClassLanTosMask_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassLanTosMask_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanTosMask = _SitaraCfgPlcyCbqClassLanTosMask_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 13),
    _SitaraCfgPlcyCbqClassLanTosMask_Type()
)
sitaraCfgPlcyCbqClassLanTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanTosMask.setStatus("current")


class _SitaraCfgPlcyCbqClassLanMtuValue_Type(Unsigned32):
    """Custom type sitaraCfgPlcyCbqClassLanMtuValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_SitaraCfgPlcyCbqClassLanMtuValue_Type.__name__ = "Unsigned32"
_SitaraCfgPlcyCbqClassLanMtuValue_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanMtuValue = _SitaraCfgPlcyCbqClassLanMtuValue_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 14),
    _SitaraCfgPlcyCbqClassLanMtuValue_Type()
)
sitaraCfgPlcyCbqClassLanMtuValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanMtuValue.setStatus("current")
_SitaraCfgPlcyCbqClassLanMaxDelay_Type = TimeTicks
_SitaraCfgPlcyCbqClassLanMaxDelay_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanMaxDelay = _SitaraCfgPlcyCbqClassLanMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 15),
    _SitaraCfgPlcyCbqClassLanMaxDelay_Type()
)
sitaraCfgPlcyCbqClassLanMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanMaxDelay.setStatus("current")
_SitaraCfgPlcyCbqClassWanBandWidth_Type = Gauge32
_SitaraCfgPlcyCbqClassWanBandWidth_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanBandWidth = _SitaraCfgPlcyCbqClassWanBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 16),
    _SitaraCfgPlcyCbqClassWanBandWidth_Type()
)
sitaraCfgPlcyCbqClassWanBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanBandWidth.setStatus("current")
_SitaraCfgPlcyCbqClassWanBurst_Type = Gauge32
_SitaraCfgPlcyCbqClassWanBurst_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanBurst = _SitaraCfgPlcyCbqClassWanBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 17),
    _SitaraCfgPlcyCbqClassWanBurst_Type()
)
sitaraCfgPlcyCbqClassWanBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanBurst.setStatus("current")
_SitaraCfgPlcyCbqClassWanPriority_Type = PolicyPriority
_SitaraCfgPlcyCbqClassWanPriority_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanPriority = _SitaraCfgPlcyCbqClassWanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 18),
    _SitaraCfgPlcyCbqClassWanPriority_Type()
)
sitaraCfgPlcyCbqClassWanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanPriority.setStatus("current")
_SitaraCfgPlcyCbqClassWanSessionBw_Type = Gauge32
_SitaraCfgPlcyCbqClassWanSessionBw_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanSessionBw = _SitaraCfgPlcyCbqClassWanSessionBw_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 19),
    _SitaraCfgPlcyCbqClassWanSessionBw_Type()
)
sitaraCfgPlcyCbqClassWanSessionBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanSessionBw.setStatus("current")
_SitaraCfgPlcyCbqClassWanAdminCtrl_Type = AdmissionState
_SitaraCfgPlcyCbqClassWanAdminCtrl_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanAdminCtrl = _SitaraCfgPlcyCbqClassWanAdminCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 20),
    _SitaraCfgPlcyCbqClassWanAdminCtrl_Type()
)
sitaraCfgPlcyCbqClassWanAdminCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanAdminCtrl.setStatus("current")


class _SitaraCfgPlcyCbqClassWanHttpCaching_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassWanHttpCaching based on Integer32"""
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


_SitaraCfgPlcyCbqClassWanHttpCaching_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassWanHttpCaching_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanHttpCaching = _SitaraCfgPlcyCbqClassWanHttpCaching_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 21),
    _SitaraCfgPlcyCbqClassWanHttpCaching_Type()
)
sitaraCfgPlcyCbqClassWanHttpCaching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanHttpCaching.setStatus("current")


class _SitaraCfgPlcyCbqClassWanTosEnabled_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassWanTosEnabled based on Integer32"""
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


_SitaraCfgPlcyCbqClassWanTosEnabled_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassWanTosEnabled_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanTosEnabled = _SitaraCfgPlcyCbqClassWanTosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 22),
    _SitaraCfgPlcyCbqClassWanTosEnabled_Type()
)
sitaraCfgPlcyCbqClassWanTosEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanTosEnabled.setStatus("current")


class _SitaraCfgPlcyCbqClassWanTosValue_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassWanTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SitaraCfgPlcyCbqClassWanTosValue_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassWanTosValue_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanTosValue = _SitaraCfgPlcyCbqClassWanTosValue_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 23),
    _SitaraCfgPlcyCbqClassWanTosValue_Type()
)
sitaraCfgPlcyCbqClassWanTosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanTosValue.setStatus("current")


class _SitaraCfgPlcyCbqClassWanTosMask_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassWanTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SitaraCfgPlcyCbqClassWanTosMask_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassWanTosMask_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanTosMask = _SitaraCfgPlcyCbqClassWanTosMask_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 24),
    _SitaraCfgPlcyCbqClassWanTosMask_Type()
)
sitaraCfgPlcyCbqClassWanTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanTosMask.setStatus("current")


class _SitaraCfgPlcyCbqClassWanMtuValue_Type(Unsigned32):
    """Custom type sitaraCfgPlcyCbqClassWanMtuValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_SitaraCfgPlcyCbqClassWanMtuValue_Type.__name__ = "Unsigned32"
_SitaraCfgPlcyCbqClassWanMtuValue_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanMtuValue = _SitaraCfgPlcyCbqClassWanMtuValue_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 25),
    _SitaraCfgPlcyCbqClassWanMtuValue_Type()
)
sitaraCfgPlcyCbqClassWanMtuValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanMtuValue.setStatus("current")
_SitaraCfgPlcyCbqClassWanMaxDelay_Type = TimeTicks
_SitaraCfgPlcyCbqClassWanMaxDelay_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanMaxDelay = _SitaraCfgPlcyCbqClassWanMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 26),
    _SitaraCfgPlcyCbqClassWanMaxDelay_Type()
)
sitaraCfgPlcyCbqClassWanMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanMaxDelay.setStatus("current")
_SitaraCfgPlcyCbqClassDirection_Type = TrafficDirection
_SitaraCfgPlcyCbqClassDirection_Object = MibTableColumn
sitaraCfgPlcyCbqClassDirection = _SitaraCfgPlcyCbqClassDirection_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 27),
    _SitaraCfgPlcyCbqClassDirection_Type()
)
sitaraCfgPlcyCbqClassDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassDirection.setStatus("current")
_SitaraCfgPlcyCbqClassOwner_Type = SitaraOwnerString
_SitaraCfgPlcyCbqClassOwner_Object = MibTableColumn
sitaraCfgPlcyCbqClassOwner = _SitaraCfgPlcyCbqClassOwner_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 28),
    _SitaraCfgPlcyCbqClassOwner_Type()
)
sitaraCfgPlcyCbqClassOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassOwner.setStatus("current")
_SitaraCfgPlcyCbqClassDscr_Type = PolicyDisplayString
_SitaraCfgPlcyCbqClassDscr_Object = MibTableColumn
sitaraCfgPlcyCbqClassDscr = _SitaraCfgPlcyCbqClassDscr_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 29),
    _SitaraCfgPlcyCbqClassDscr_Type()
)
sitaraCfgPlcyCbqClassDscr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassDscr.setStatus("current")


class _SitaraCfgPlcyCbqClassPolicyStatus_Type(PolicyStatus):
    """Custom type sitaraCfgPlcyCbqClassPolicyStatus based on PolicyStatus"""


_SitaraCfgPlcyCbqClassPolicyStatus_Object = MibTableColumn
sitaraCfgPlcyCbqClassPolicyStatus = _SitaraCfgPlcyCbqClassPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 30),
    _SitaraCfgPlcyCbqClassPolicyStatus_Type()
)
sitaraCfgPlcyCbqClassPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassPolicyStatus.setStatus("current")
_SitaraCfgPlcyCbqClassStatus_Type = RowStatus
_SitaraCfgPlcyCbqClassStatus_Object = MibTableColumn
sitaraCfgPlcyCbqClassStatus = _SitaraCfgPlcyCbqClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 31),
    _SitaraCfgPlcyCbqClassStatus_Type()
)
sitaraCfgPlcyCbqClassStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassStatus.setStatus("current")


class _SitaraCfgPlcyCbqClassLanMinBurst_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassLanMinBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SitaraCfgPlcyCbqClassLanMinBurst_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassLanMinBurst_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanMinBurst = _SitaraCfgPlcyCbqClassLanMinBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 37),
    _SitaraCfgPlcyCbqClassLanMinBurst_Type()
)
sitaraCfgPlcyCbqClassLanMinBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanMinBurst.setStatus("current")


class _SitaraCfgPlcyCbqClassLanMaxBurst_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassLanMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SitaraCfgPlcyCbqClassLanMaxBurst_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassLanMaxBurst_Object = MibTableColumn
sitaraCfgPlcyCbqClassLanMaxBurst = _SitaraCfgPlcyCbqClassLanMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 38),
    _SitaraCfgPlcyCbqClassLanMaxBurst_Type()
)
sitaraCfgPlcyCbqClassLanMaxBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassLanMaxBurst.setStatus("current")


class _SitaraCfgPlcyCbqClassWanMinBurst_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassWanMinBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SitaraCfgPlcyCbqClassWanMinBurst_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassWanMinBurst_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanMinBurst = _SitaraCfgPlcyCbqClassWanMinBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 39),
    _SitaraCfgPlcyCbqClassWanMinBurst_Type()
)
sitaraCfgPlcyCbqClassWanMinBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanMinBurst.setStatus("current")


class _SitaraCfgPlcyCbqClassWanMaxBurst_Type(Integer32):
    """Custom type sitaraCfgPlcyCbqClassWanMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SitaraCfgPlcyCbqClassWanMaxBurst_Type.__name__ = "Integer32"
_SitaraCfgPlcyCbqClassWanMaxBurst_Object = MibTableColumn
sitaraCfgPlcyCbqClassWanMaxBurst = _SitaraCfgPlcyCbqClassWanMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 7, 1, 1, 2, 1, 40),
    _SitaraCfgPlcyCbqClassWanMaxBurst_Type()
)
sitaraCfgPlcyCbqClassWanMaxBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyCbqClassWanMaxBurst.setStatus("current")
_SitaraCfgPlcyFilter_ObjectIdentity = ObjectIdentity
sitaraCfgPlcyFilter = _SitaraCfgPlcyFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8)
)
_SitaraCfgPlcyFilterNextIndex_Type = Unsigned32
_SitaraCfgPlcyFilterNextIndex_Object = MibScalar
sitaraCfgPlcyFilterNextIndex = _SitaraCfgPlcyFilterNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 1),
    _SitaraCfgPlcyFilterNextIndex_Type()
)
sitaraCfgPlcyFilterNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterNextIndex.setStatus("current")
_SitaraCfgPlcyFilterTable_Object = MibTable
sitaraCfgPlcyFilterTable = _SitaraCfgPlcyFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterTable.setStatus("current")
_SitaraCfgPlcyFilterEntry_Object = MibTableRow
sitaraCfgPlcyFilterEntry = _SitaraCfgPlcyFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1)
)
sitaraCfgPlcyFilterEntry.setIndexNames(
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassIndex"),
    (0, "CFG-PLCY-MIB", "sitaraCfgPlcyFilterIndex"),
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterEntry.setStatus("current")
_SitaraCfgPlcyFilterIndex_Type = Unsigned32
_SitaraCfgPlcyFilterIndex_Object = MibTableColumn
sitaraCfgPlcyFilterIndex = _SitaraCfgPlcyFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 1),
    _SitaraCfgPlcyFilterIndex_Type()
)
sitaraCfgPlcyFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterIndex.setStatus("current")
_SitaraCfgPlcyFilterAlias_Type = PolicyAlias
_SitaraCfgPlcyFilterAlias_Object = MibTableColumn
sitaraCfgPlcyFilterAlias = _SitaraCfgPlcyFilterAlias_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 2),
    _SitaraCfgPlcyFilterAlias_Type()
)
sitaraCfgPlcyFilterAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterAlias.setStatus("current")
_SitaraCfgPlcyFilterPathName_Type = PolicyPathName
_SitaraCfgPlcyFilterPathName_Object = MibTableColumn
sitaraCfgPlcyFilterPathName = _SitaraCfgPlcyFilterPathName_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 3),
    _SitaraCfgPlcyFilterPathName_Type()
)
sitaraCfgPlcyFilterPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterPathName.setStatus("current")


class _SitaraCfgPlcyFilterProtocolType_Type(Integer32):
    """Custom type sitaraCfgPlcyFilterProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SitaraCfgPlcyFilterProtocolType_Type.__name__ = "Integer32"
_SitaraCfgPlcyFilterProtocolType_Object = MibTableColumn
sitaraCfgPlcyFilterProtocolType = _SitaraCfgPlcyFilterProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 4),
    _SitaraCfgPlcyFilterProtocolType_Type()
)
sitaraCfgPlcyFilterProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterProtocolType.setStatus("current")


class _SitaraCfgPlcyFilterLanIpStartPort_Type(Integer32):
    """Custom type sitaraCfgPlcyFilterLanIpStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SitaraCfgPlcyFilterLanIpStartPort_Type.__name__ = "Integer32"
_SitaraCfgPlcyFilterLanIpStartPort_Object = MibTableColumn
sitaraCfgPlcyFilterLanIpStartPort = _SitaraCfgPlcyFilterLanIpStartPort_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 5),
    _SitaraCfgPlcyFilterLanIpStartPort_Type()
)
sitaraCfgPlcyFilterLanIpStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterLanIpStartPort.setStatus("current")


class _SitaraCfgPlcyFilterLanIpEndPort_Type(Integer32):
    """Custom type sitaraCfgPlcyFilterLanIpEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SitaraCfgPlcyFilterLanIpEndPort_Type.__name__ = "Integer32"
_SitaraCfgPlcyFilterLanIpEndPort_Object = MibTableColumn
sitaraCfgPlcyFilterLanIpEndPort = _SitaraCfgPlcyFilterLanIpEndPort_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 6),
    _SitaraCfgPlcyFilterLanIpEndPort_Type()
)
sitaraCfgPlcyFilterLanIpEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterLanIpEndPort.setStatus("current")
_SitaraCfgPlcyFilterLanIpAddr_Type = IpAddress
_SitaraCfgPlcyFilterLanIpAddr_Object = MibTableColumn
sitaraCfgPlcyFilterLanIpAddr = _SitaraCfgPlcyFilterLanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 7),
    _SitaraCfgPlcyFilterLanIpAddr_Type()
)
sitaraCfgPlcyFilterLanIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterLanIpAddr.setStatus("current")
_SitaraCfgPlcyFilterLanNetMask_Type = IpAddress
_SitaraCfgPlcyFilterLanNetMask_Object = MibTableColumn
sitaraCfgPlcyFilterLanNetMask = _SitaraCfgPlcyFilterLanNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 8),
    _SitaraCfgPlcyFilterLanNetMask_Type()
)
sitaraCfgPlcyFilterLanNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterLanNetMask.setStatus("current")


class _SitaraCfgPlcyFilterWanIpStartPort_Type(Integer32):
    """Custom type sitaraCfgPlcyFilterWanIpStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SitaraCfgPlcyFilterWanIpStartPort_Type.__name__ = "Integer32"
_SitaraCfgPlcyFilterWanIpStartPort_Object = MibTableColumn
sitaraCfgPlcyFilterWanIpStartPort = _SitaraCfgPlcyFilterWanIpStartPort_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 9),
    _SitaraCfgPlcyFilterWanIpStartPort_Type()
)
sitaraCfgPlcyFilterWanIpStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterWanIpStartPort.setStatus("current")


class _SitaraCfgPlcyFilterWanIpEndPort_Type(Integer32):
    """Custom type sitaraCfgPlcyFilterWanIpEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SitaraCfgPlcyFilterWanIpEndPort_Type.__name__ = "Integer32"
_SitaraCfgPlcyFilterWanIpEndPort_Object = MibTableColumn
sitaraCfgPlcyFilterWanIpEndPort = _SitaraCfgPlcyFilterWanIpEndPort_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 10),
    _SitaraCfgPlcyFilterWanIpEndPort_Type()
)
sitaraCfgPlcyFilterWanIpEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterWanIpEndPort.setStatus("current")
_SitaraCfgPlcyFilterWanIpAddr_Type = IpAddress
_SitaraCfgPlcyFilterWanIpAddr_Object = MibTableColumn
sitaraCfgPlcyFilterWanIpAddr = _SitaraCfgPlcyFilterWanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 11),
    _SitaraCfgPlcyFilterWanIpAddr_Type()
)
sitaraCfgPlcyFilterWanIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterWanIpAddr.setStatus("current")
_SitaraCfgPlcyFilterWanNetMask_Type = IpAddress
_SitaraCfgPlcyFilterWanNetMask_Object = MibTableColumn
sitaraCfgPlcyFilterWanNetMask = _SitaraCfgPlcyFilterWanNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 12),
    _SitaraCfgPlcyFilterWanNetMask_Type()
)
sitaraCfgPlcyFilterWanNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterWanNetMask.setStatus("current")


class _SitaraCfgPlcyFilterOrder_Type(Integer32):
    """Custom type sitaraCfgPlcyFilterOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SitaraCfgPlcyFilterOrder_Type.__name__ = "Integer32"
_SitaraCfgPlcyFilterOrder_Object = MibTableColumn
sitaraCfgPlcyFilterOrder = _SitaraCfgPlcyFilterOrder_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 13),
    _SitaraCfgPlcyFilterOrder_Type()
)
sitaraCfgPlcyFilterOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterOrder.setStatus("current")
_SitaraCfgPlcyFilterOwner_Type = SitaraOwnerString
_SitaraCfgPlcyFilterOwner_Object = MibTableColumn
sitaraCfgPlcyFilterOwner = _SitaraCfgPlcyFilterOwner_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 14),
    _SitaraCfgPlcyFilterOwner_Type()
)
sitaraCfgPlcyFilterOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterOwner.setStatus("current")
_SitaraCfgPlcyFilterDscr_Type = PolicyDisplayString
_SitaraCfgPlcyFilterDscr_Object = MibTableColumn
sitaraCfgPlcyFilterDscr = _SitaraCfgPlcyFilterDscr_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 15),
    _SitaraCfgPlcyFilterDscr_Type()
)
sitaraCfgPlcyFilterDscr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterDscr.setStatus("current")


class _SitaraCfgPlcyFilterPolicyStatus_Type(PolicyStatus):
    """Custom type sitaraCfgPlcyFilterPolicyStatus based on PolicyStatus"""


_SitaraCfgPlcyFilterPolicyStatus_Object = MibTableColumn
sitaraCfgPlcyFilterPolicyStatus = _SitaraCfgPlcyFilterPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 16),
    _SitaraCfgPlcyFilterPolicyStatus_Type()
)
sitaraCfgPlcyFilterPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterPolicyStatus.setStatus("current")
_SitaraCfgPlcyFilterStatus_Type = RowStatus
_SitaraCfgPlcyFilterStatus_Object = MibTableColumn
sitaraCfgPlcyFilterStatus = _SitaraCfgPlcyFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 17),
    _SitaraCfgPlcyFilterStatus_Type()
)
sitaraCfgPlcyFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterStatus.setStatus("current")


class _SitaraCfgPlcyFilterTosEnabled_Type(Integer32):
    """Custom type sitaraCfgPlcyFilterTosEnabled based on Integer32"""
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


_SitaraCfgPlcyFilterTosEnabled_Type.__name__ = "Integer32"
_SitaraCfgPlcyFilterTosEnabled_Object = MibTableColumn
sitaraCfgPlcyFilterTosEnabled = _SitaraCfgPlcyFilterTosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 18),
    _SitaraCfgPlcyFilterTosEnabled_Type()
)
sitaraCfgPlcyFilterTosEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterTosEnabled.setStatus("current")


class _SitaraCfgPlcyFilterTosValue_Type(Integer32):
    """Custom type sitaraCfgPlcyFilterTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SitaraCfgPlcyFilterTosValue_Type.__name__ = "Integer32"
_SitaraCfgPlcyFilterTosValue_Object = MibTableColumn
sitaraCfgPlcyFilterTosValue = _SitaraCfgPlcyFilterTosValue_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 19),
    _SitaraCfgPlcyFilterTosValue_Type()
)
sitaraCfgPlcyFilterTosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterTosValue.setStatus("current")


class _SitaraCfgPlcyFilterTosMask_Type(Integer32):
    """Custom type sitaraCfgPlcyFilterTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SitaraCfgPlcyFilterTosMask_Type.__name__ = "Integer32"
_SitaraCfgPlcyFilterTosMask_Object = MibTableColumn
sitaraCfgPlcyFilterTosMask = _SitaraCfgPlcyFilterTosMask_Object(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 8, 2, 1, 20),
    _SitaraCfgPlcyFilterTosMask_Type()
)
sitaraCfgPlcyFilterTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sitaraCfgPlcyFilterTosMask.setStatus("current")
_SitaraCfgPlcyNotifns_ObjectIdentity = ObjectIdentity
sitaraCfgPlcyNotifns = _SitaraCfgPlcyNotifns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9)
)

# Managed Objects groups


# Notification objects

sitaraCfgPlcyNotifnsPlcyUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 1)
)
sitaraCfgPlcyNotifnsPlcyUpdate.setObjects(
    ("CFG-PLCY-MIB", "sitaraCfgPlcyLastUpdateTime")
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsPlcyUpdate.setStatus(
        "current"
    )

sitaraCfgPlcyNotifnsCbqdReStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 2)
)
sitaraCfgPlcyNotifnsCbqdReStart.setObjects(
    ("CFG-PLCY-MIB", "sitaraCfgPlcyLastUpdateTime")
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsCbqdReStart.setStatus(
        "obsolete"
    )

sitaraCfgPlcyNotifnsFailToReStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 3)
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsFailToReStart.setStatus(
        "obsolete"
    )

sitaraCfgPlcyNotifnsFailToUpdatePolicy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 4)
)
sitaraCfgPlcyNotifnsFailToUpdatePolicy.setObjects(
    ("CFG-PLCY-MIB", "sitaraCfgPlcyApplyError")
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsFailToUpdatePolicy.setStatus(
        "current"
    )

sitaraCfgPlcyNotifnsFailToXlatePolicy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 5)
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsFailToXlatePolicy.setStatus(
        "obsolete"
    )

sitaraCfgPlcyNotifnsInvalidPolicy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 6)
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsInvalidPolicy.setStatus(
        "current"
    )

sitaraCfgPlcyNotifnsSchdEntryUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 7)
)
sitaraCfgPlcyNotifnsSchdEntryUpdate.setObjects(
      *(("CFG-PLCY-MIB", "sitaraCfgPlcySchdAlias"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcySchdDaysOfWeek"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcySchdStartTime"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcySchdEndTime"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcySchdOwner"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcySchdPolicyStatus"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcySchdStatus"))
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsSchdEntryUpdate.setStatus(
        "current"
    )

sitaraCfgPlcyNotifnsLinkEntryUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 8)
)
sitaraCfgPlcyNotifnsLinkEntryUpdate.setObjects(
      *(("CFG-PLCY-MIB", "sitaraCfgPlcyLinkAlias"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkPathName"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkEnabled"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkDscr"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkLanBandWidth"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkLanBurst"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkLanAvlBandWidth"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkWanBandWidth"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkWanBurst"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkWanAvlBandWidth"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkOwner"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkPolicyStatus"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkStatus"))
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsLinkEntryUpdate.setStatus(
        "current"
    )

sitaraCfgPlcyNotifnsNetDestEntryUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 9)
)
sitaraCfgPlcyNotifnsNetDestEntryUpdate.setObjects(
      *(("CFG-PLCY-MIB", "sitaraCfgPlcyLinkNetDestAddr"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkNetDestMask"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkNetDestOwner"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyLinkNetDestStatus"))
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsNetDestEntryUpdate.setStatus(
        "current"
    )

sitaraCfgPlcyNotifnsGroupEntryUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 10)
)
sitaraCfgPlcyNotifnsGroupEntryUpdate.setObjects(
      *(("CFG-PLCY-MIB", "sitaraCfgPlcyGroupAlias"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupPathName"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupEnabled"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupDscr"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupLanBandWidth"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupLanAvlBandWidth"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupLanBurst"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupWanBandWidth"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupWanAvlBandWidth"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupWanBurst"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupDirection"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupParentIndex"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupOwner"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupPolicyStatus"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyGroupStatus"))
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsGroupEntryUpdate.setStatus(
        "current"
    )

sitaraCfgPlcyNotifnsClassEntryUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 11)
)
sitaraCfgPlcyNotifnsClassEntryUpdate.setObjects(
      *(("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassAlias"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassPathName"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassEnabled"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanBandWidth"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanBurst"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanPriority"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanSessionBw"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanAdminCtrl"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanHttpCaching"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanTosEnabled"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanTosValue"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanTosMask"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanMtuValue"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassLanMaxDelay"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanBandWidth"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanBurst"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanPriority"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanSessionBw"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanAdminCtrl"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanHttpCaching"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanTosEnabled"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanTosValue"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanTosMask"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanMtuValue"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassWanMaxDelay"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassDirection"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassOwner"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassDscr"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassPolicyStatus"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyCbqClassStatus"))
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsClassEntryUpdate.setStatus(
        "current"
    )

sitaraCfgPlcyNotifnsFilterEntryUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 12)
)
sitaraCfgPlcyNotifnsFilterEntryUpdate.setObjects(
      *(("CFG-PLCY-MIB", "sitaraCfgPlcyFilterAlias"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterPathName"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterProtocolType"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterLanIpStartPort"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterLanIpEndPort"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterLanIpAddr"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterLanNetMask"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterWanIpStartPort"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterWanIpEndPort"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterWanIpAddr"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterWanNetMask"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterOrder"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterOwner"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterDscr"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterPolicyStatus"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterStatus"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterTosEnabled"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterTosValue"),
        ("CFG-PLCY-MIB", "sitaraCfgPlcyFilterTosMask"))
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsFilterEntryUpdate.setStatus(
        "current"
    )

sitaraCfgPlcyNotifnsPlcySyncUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 13)
)
sitaraCfgPlcyNotifnsPlcySyncUp.setObjects(
    ("CFG-PLCY-MIB", "sitaraCfgPlcyLastUpdateTime")
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsPlcySyncUp.setStatus(
        "current"
    )

sitaraCfgPlcyNotifnsPlcySyncUpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2302, 1, 1, 9, 14)
)
sitaraCfgPlcyNotifnsPlcySyncUpFailure.setObjects(
    ("CFG-PLCY-MIB", "sitaraCfgPlcyLastUpdateTime")
)
if mibBuilder.loadTexts:
    sitaraCfgPlcyNotifnsPlcySyncUpFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CFG-PLCY-MIB",
    **{"AdmissionState": AdmissionState,
       "PolicyStatus": PolicyStatus,
       "PolicyPriority": PolicyPriority,
       "DaysOfWeek": DaysOfWeek,
       "TimeAndZone": TimeAndZone,
       "PolicyAlias": PolicyAlias,
       "PolicyCustomerId": PolicyCustomerId,
       "PolicyPathName": PolicyPathName,
       "TrafficDirection": TrafficDirection,
       "PolicyDisplayString": PolicyDisplayString,
       "SitaraOwnerString": SitaraOwnerString,
       "sitara": sitara,
       "sitaraCfg": sitaraCfg,
       "sitaraCfgPlcy": sitaraCfgPlcy,
       "sitaraCfgPlcyMIB": sitaraCfgPlcyMIB,
       "sitaraCfgPlcyGenlObjs": sitaraCfgPlcyGenlObjs,
       "sitaraCfgPlcyVersion": sitaraCfgPlcyVersion,
       "sitaraCfgPlcyPerRowUpdate": sitaraCfgPlcyPerRowUpdate,
       "sitaraCfgPlcyGlobalStorage": sitaraCfgPlcyGlobalStorage,
       "sitaraCfgPlcyLastUpdateTime": sitaraCfgPlcyLastUpdateTime,
       "sitaraCfgPlcyApplyError": sitaraCfgPlcyApplyError,
       "sitaraCfgPlcyCrossGroup": sitaraCfgPlcyCrossGroup,
       "sitaraCfgPlcyCrossIndexTable": sitaraCfgPlcyCrossIndexTable,
       "sitaraCfgPlcyCrossIndexTableEntry": sitaraCfgPlcyCrossIndexTableEntry,
       "sitaraCfgPlcyCrossSchdAlias": sitaraCfgPlcyCrossSchdAlias,
       "sitaraCfgPlcyCrossLinkAlias": sitaraCfgPlcyCrossLinkAlias,
       "sitaraCfgPlcyCrossGroupAlias": sitaraCfgPlcyCrossGroupAlias,
       "sitaraCfgPlcyCrossCbqClassAlias": sitaraCfgPlcyCrossCbqClassAlias,
       "sitaraCfgPlcyCrossFilterAlias": sitaraCfgPlcyCrossFilterAlias,
       "sitaraCfgPlcyCrossIndex": sitaraCfgPlcyCrossIndex,
       "sitaraCfgPlcyCrossSchdIndex": sitaraCfgPlcyCrossSchdIndex,
       "sitaraCfgPlcyCrossLinkIndex": sitaraCfgPlcyCrossLinkIndex,
       "sitaraCfgPlcyCrossLinkNetDestIndex": sitaraCfgPlcyCrossLinkNetDestIndex,
       "sitaraCfgPlcyCrossGroupIndex": sitaraCfgPlcyCrossGroupIndex,
       "sitaraCfgPlcyCrossCbqClassIndex": sitaraCfgPlcyCrossCbqClassIndex,
       "sitaraCfgPlcyCrossFilterIndex": sitaraCfgPlcyCrossFilterIndex,
       "sitaraCfgPlcySchd": sitaraCfgPlcySchd,
       "sitaraCfgPlcySchdNextIndex": sitaraCfgPlcySchdNextIndex,
       "sitaraCfgPlcySchdTable": sitaraCfgPlcySchdTable,
       "sitaraCfgPlcySchdEntry": sitaraCfgPlcySchdEntry,
       "sitaraCfgPlcySchdIndex": sitaraCfgPlcySchdIndex,
       "sitaraCfgPlcySchdAlias": sitaraCfgPlcySchdAlias,
       "sitaraCfgPlcySchdDaysOfWeek": sitaraCfgPlcySchdDaysOfWeek,
       "sitaraCfgPlcySchdStartTime": sitaraCfgPlcySchdStartTime,
       "sitaraCfgPlcySchdEndTime": sitaraCfgPlcySchdEndTime,
       "sitaraCfgPlcySchdOwner": sitaraCfgPlcySchdOwner,
       "sitaraCfgPlcySchdPolicyStatus": sitaraCfgPlcySchdPolicyStatus,
       "sitaraCfgPlcySchdStatus": sitaraCfgPlcySchdStatus,
       "sitaraCfgPlcyLink": sitaraCfgPlcyLink,
       "sitaraCfgPlcyLinkNextIndex": sitaraCfgPlcyLinkNextIndex,
       "sitaraCfgPlcyLinkTable": sitaraCfgPlcyLinkTable,
       "sitaraCfgPlcyLinkEntry": sitaraCfgPlcyLinkEntry,
       "sitaraCfgPlcyLinkIndex": sitaraCfgPlcyLinkIndex,
       "sitaraCfgPlcyLinkAlias": sitaraCfgPlcyLinkAlias,
       "sitaraCfgPlcyLinkPathName": sitaraCfgPlcyLinkPathName,
       "sitaraCfgPlcyLinkEnabled": sitaraCfgPlcyLinkEnabled,
       "sitaraCfgPlcyLinkDscr": sitaraCfgPlcyLinkDscr,
       "sitaraCfgPlcyLinkLanBandWidth": sitaraCfgPlcyLinkLanBandWidth,
       "sitaraCfgPlcyLinkLanBurst": sitaraCfgPlcyLinkLanBurst,
       "sitaraCfgPlcyLinkLanAvlBandWidth": sitaraCfgPlcyLinkLanAvlBandWidth,
       "sitaraCfgPlcyLinkWanBandWidth": sitaraCfgPlcyLinkWanBandWidth,
       "sitaraCfgPlcyLinkWanBurst": sitaraCfgPlcyLinkWanBurst,
       "sitaraCfgPlcyLinkWanAvlBandWidth": sitaraCfgPlcyLinkWanAvlBandWidth,
       "sitaraCfgPlcyLinkOwner": sitaraCfgPlcyLinkOwner,
       "sitaraCfgPlcyLinkPolicyStatus": sitaraCfgPlcyLinkPolicyStatus,
       "sitaraCfgPlcyLinkStatus": sitaraCfgPlcyLinkStatus,
       "sitaraCfgPlcyLinkNetDestNextIndex": sitaraCfgPlcyLinkNetDestNextIndex,
       "sitaraCfgPlcyLinkNetDestTable": sitaraCfgPlcyLinkNetDestTable,
       "sitaraCfgPlcyLinkNetDestEntry": sitaraCfgPlcyLinkNetDestEntry,
       "sitaraCfgPlcyLinkNetDestIndex": sitaraCfgPlcyLinkNetDestIndex,
       "sitaraCfgPlcyLinkNetDestAddr": sitaraCfgPlcyLinkNetDestAddr,
       "sitaraCfgPlcyLinkNetDestMask": sitaraCfgPlcyLinkNetDestMask,
       "sitaraCfgPlcyLinkNetDestOwner": sitaraCfgPlcyLinkNetDestOwner,
       "sitaraCfgPlcyLinkNetDestStatus": sitaraCfgPlcyLinkNetDestStatus,
       "sitaraCfgPlcyGroup": sitaraCfgPlcyGroup,
       "sitaraCfgPlcyGroupNextIndex": sitaraCfgPlcyGroupNextIndex,
       "sitaraCfgPlcyGroupTable": sitaraCfgPlcyGroupTable,
       "sitaraCfgPlcyGroupEntry": sitaraCfgPlcyGroupEntry,
       "sitaraCfgPlcyGroupIndex": sitaraCfgPlcyGroupIndex,
       "sitaraCfgPlcyGroupAlias": sitaraCfgPlcyGroupAlias,
       "sitaraCfgPlcyGroupPathName": sitaraCfgPlcyGroupPathName,
       "sitaraCfgPlcyGroupEnabled": sitaraCfgPlcyGroupEnabled,
       "sitaraCfgPlcyGroupDscr": sitaraCfgPlcyGroupDscr,
       "sitaraCfgPlcyGroupLanBandWidth": sitaraCfgPlcyGroupLanBandWidth,
       "sitaraCfgPlcyGroupLanBurst": sitaraCfgPlcyGroupLanBurst,
       "sitaraCfgPlcyGroupLanAvlBandWidth": sitaraCfgPlcyGroupLanAvlBandWidth,
       "sitaraCfgPlcyGroupWanBandWidth": sitaraCfgPlcyGroupWanBandWidth,
       "sitaraCfgPlcyGroupWanBurst": sitaraCfgPlcyGroupWanBurst,
       "sitaraCfgPlcyGroupWanAvlBandWidth": sitaraCfgPlcyGroupWanAvlBandWidth,
       "sitaraCfgPlcyGroupDirection": sitaraCfgPlcyGroupDirection,
       "sitaraCfgPlcyGroupParentIndex": sitaraCfgPlcyGroupParentIndex,
       "sitaraCfgPlcyGroupOwner": sitaraCfgPlcyGroupOwner,
       "sitaraCfgPlcyGroupPolicyStatus": sitaraCfgPlcyGroupPolicyStatus,
       "sitaraCfgPlcyGroupStatus": sitaraCfgPlcyGroupStatus,
       "sitaraCfgPlcyAction": sitaraCfgPlcyAction,
       "sitaraCfgPlcyQClass": sitaraCfgPlcyQClass,
       "sitaraCfgPlcyCbqClass": sitaraCfgPlcyCbqClass,
       "sitaraCfgPlcyCbqClassNextIndex": sitaraCfgPlcyCbqClassNextIndex,
       "sitaraCfgPlcyCbqClassTable": sitaraCfgPlcyCbqClassTable,
       "sitaraCfgPlcyCbqClassEntry": sitaraCfgPlcyCbqClassEntry,
       "sitaraCfgPlcyCbqClassIndex": sitaraCfgPlcyCbqClassIndex,
       "sitaraCfgPlcyCbqClassAlias": sitaraCfgPlcyCbqClassAlias,
       "sitaraCfgPlcyCbqClassPathName": sitaraCfgPlcyCbqClassPathName,
       "sitaraCfgPlcyCbqClassEnabled": sitaraCfgPlcyCbqClassEnabled,
       "sitaraCfgPlcyCbqClassLanBandWidth": sitaraCfgPlcyCbqClassLanBandWidth,
       "sitaraCfgPlcyCbqClassLanBurst": sitaraCfgPlcyCbqClassLanBurst,
       "sitaraCfgPlcyCbqClassLanPriority": sitaraCfgPlcyCbqClassLanPriority,
       "sitaraCfgPlcyCbqClassLanSessionBw": sitaraCfgPlcyCbqClassLanSessionBw,
       "sitaraCfgPlcyCbqClassLanAdminCtrl": sitaraCfgPlcyCbqClassLanAdminCtrl,
       "sitaraCfgPlcyCbqClassLanHttpCaching": sitaraCfgPlcyCbqClassLanHttpCaching,
       "sitaraCfgPlcyCbqClassLanTosEnabled": sitaraCfgPlcyCbqClassLanTosEnabled,
       "sitaraCfgPlcyCbqClassLanTosValue": sitaraCfgPlcyCbqClassLanTosValue,
       "sitaraCfgPlcyCbqClassLanTosMask": sitaraCfgPlcyCbqClassLanTosMask,
       "sitaraCfgPlcyCbqClassLanMtuValue": sitaraCfgPlcyCbqClassLanMtuValue,
       "sitaraCfgPlcyCbqClassLanMaxDelay": sitaraCfgPlcyCbqClassLanMaxDelay,
       "sitaraCfgPlcyCbqClassWanBandWidth": sitaraCfgPlcyCbqClassWanBandWidth,
       "sitaraCfgPlcyCbqClassWanBurst": sitaraCfgPlcyCbqClassWanBurst,
       "sitaraCfgPlcyCbqClassWanPriority": sitaraCfgPlcyCbqClassWanPriority,
       "sitaraCfgPlcyCbqClassWanSessionBw": sitaraCfgPlcyCbqClassWanSessionBw,
       "sitaraCfgPlcyCbqClassWanAdminCtrl": sitaraCfgPlcyCbqClassWanAdminCtrl,
       "sitaraCfgPlcyCbqClassWanHttpCaching": sitaraCfgPlcyCbqClassWanHttpCaching,
       "sitaraCfgPlcyCbqClassWanTosEnabled": sitaraCfgPlcyCbqClassWanTosEnabled,
       "sitaraCfgPlcyCbqClassWanTosValue": sitaraCfgPlcyCbqClassWanTosValue,
       "sitaraCfgPlcyCbqClassWanTosMask": sitaraCfgPlcyCbqClassWanTosMask,
       "sitaraCfgPlcyCbqClassWanMtuValue": sitaraCfgPlcyCbqClassWanMtuValue,
       "sitaraCfgPlcyCbqClassWanMaxDelay": sitaraCfgPlcyCbqClassWanMaxDelay,
       "sitaraCfgPlcyCbqClassDirection": sitaraCfgPlcyCbqClassDirection,
       "sitaraCfgPlcyCbqClassOwner": sitaraCfgPlcyCbqClassOwner,
       "sitaraCfgPlcyCbqClassDscr": sitaraCfgPlcyCbqClassDscr,
       "sitaraCfgPlcyCbqClassPolicyStatus": sitaraCfgPlcyCbqClassPolicyStatus,
       "sitaraCfgPlcyCbqClassStatus": sitaraCfgPlcyCbqClassStatus,
       "sitaraCfgPlcyCbqClassLanMinBurst": sitaraCfgPlcyCbqClassLanMinBurst,
       "sitaraCfgPlcyCbqClassLanMaxBurst": sitaraCfgPlcyCbqClassLanMaxBurst,
       "sitaraCfgPlcyCbqClassWanMinBurst": sitaraCfgPlcyCbqClassWanMinBurst,
       "sitaraCfgPlcyCbqClassWanMaxBurst": sitaraCfgPlcyCbqClassWanMaxBurst,
       "sitaraCfgPlcyFilter": sitaraCfgPlcyFilter,
       "sitaraCfgPlcyFilterNextIndex": sitaraCfgPlcyFilterNextIndex,
       "sitaraCfgPlcyFilterTable": sitaraCfgPlcyFilterTable,
       "sitaraCfgPlcyFilterEntry": sitaraCfgPlcyFilterEntry,
       "sitaraCfgPlcyFilterIndex": sitaraCfgPlcyFilterIndex,
       "sitaraCfgPlcyFilterAlias": sitaraCfgPlcyFilterAlias,
       "sitaraCfgPlcyFilterPathName": sitaraCfgPlcyFilterPathName,
       "sitaraCfgPlcyFilterProtocolType": sitaraCfgPlcyFilterProtocolType,
       "sitaraCfgPlcyFilterLanIpStartPort": sitaraCfgPlcyFilterLanIpStartPort,
       "sitaraCfgPlcyFilterLanIpEndPort": sitaraCfgPlcyFilterLanIpEndPort,
       "sitaraCfgPlcyFilterLanIpAddr": sitaraCfgPlcyFilterLanIpAddr,
       "sitaraCfgPlcyFilterLanNetMask": sitaraCfgPlcyFilterLanNetMask,
       "sitaraCfgPlcyFilterWanIpStartPort": sitaraCfgPlcyFilterWanIpStartPort,
       "sitaraCfgPlcyFilterWanIpEndPort": sitaraCfgPlcyFilterWanIpEndPort,
       "sitaraCfgPlcyFilterWanIpAddr": sitaraCfgPlcyFilterWanIpAddr,
       "sitaraCfgPlcyFilterWanNetMask": sitaraCfgPlcyFilterWanNetMask,
       "sitaraCfgPlcyFilterOrder": sitaraCfgPlcyFilterOrder,
       "sitaraCfgPlcyFilterOwner": sitaraCfgPlcyFilterOwner,
       "sitaraCfgPlcyFilterDscr": sitaraCfgPlcyFilterDscr,
       "sitaraCfgPlcyFilterPolicyStatus": sitaraCfgPlcyFilterPolicyStatus,
       "sitaraCfgPlcyFilterStatus": sitaraCfgPlcyFilterStatus,
       "sitaraCfgPlcyFilterTosEnabled": sitaraCfgPlcyFilterTosEnabled,
       "sitaraCfgPlcyFilterTosValue": sitaraCfgPlcyFilterTosValue,
       "sitaraCfgPlcyFilterTosMask": sitaraCfgPlcyFilterTosMask,
       "sitaraCfgPlcyNotifns": sitaraCfgPlcyNotifns,
       "sitaraCfgPlcyNotifnsPlcyUpdate": sitaraCfgPlcyNotifnsPlcyUpdate,
       "sitaraCfgPlcyNotifnsCbqdReStart": sitaraCfgPlcyNotifnsCbqdReStart,
       "sitaraCfgPlcyNotifnsFailToReStart": sitaraCfgPlcyNotifnsFailToReStart,
       "sitaraCfgPlcyNotifnsFailToUpdatePolicy": sitaraCfgPlcyNotifnsFailToUpdatePolicy,
       "sitaraCfgPlcyNotifnsFailToXlatePolicy": sitaraCfgPlcyNotifnsFailToXlatePolicy,
       "sitaraCfgPlcyNotifnsInvalidPolicy": sitaraCfgPlcyNotifnsInvalidPolicy,
       "sitaraCfgPlcyNotifnsSchdEntryUpdate": sitaraCfgPlcyNotifnsSchdEntryUpdate,
       "sitaraCfgPlcyNotifnsLinkEntryUpdate": sitaraCfgPlcyNotifnsLinkEntryUpdate,
       "sitaraCfgPlcyNotifnsNetDestEntryUpdate": sitaraCfgPlcyNotifnsNetDestEntryUpdate,
       "sitaraCfgPlcyNotifnsGroupEntryUpdate": sitaraCfgPlcyNotifnsGroupEntryUpdate,
       "sitaraCfgPlcyNotifnsClassEntryUpdate": sitaraCfgPlcyNotifnsClassEntryUpdate,
       "sitaraCfgPlcyNotifnsFilterEntryUpdate": sitaraCfgPlcyNotifnsFilterEntryUpdate,
       "sitaraCfgPlcyNotifnsPlcySyncUp": sitaraCfgPlcyNotifnsPlcySyncUp,
       "sitaraCfgPlcyNotifnsPlcySyncUpFailure": sitaraCfgPlcyNotifnsPlcySyncUpFailure}
)
