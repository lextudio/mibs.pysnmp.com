# SNMP MIB module (HP-ICF-LINKTEST) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-LINKTEST
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:43 2024
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

(hpicfCommon,
 hpicfObjectModules) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon",
    "hpicfObjectModules")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 RowStatus,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

hpicfLinkTestMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7)
)
hpicfLinkTestMib.setRevisions(
        ("2000-11-03 22:25",
         "1997-03-06 03:38",
         "1996-09-06 22:18")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfLinkTestConformance_ObjectIdentity = ObjectIdentity
hpicfLinkTestConformance = _HpicfLinkTestConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1)
)
_HpicfLinkTestCompliances_ObjectIdentity = ObjectIdentity
hpicfLinkTestCompliances = _HpicfLinkTestCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 1)
)
_HpicfLinkTestGroups_ObjectIdentity = ObjectIdentity
hpicfLinkTestGroups = _HpicfLinkTestGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 2)
)
_HpicfLinktest_ObjectIdentity = ObjectIdentity
hpicfLinktest = _HpicfLinktest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6)
)


class _HpicfLinkTestNextIndex_Type(Integer32):
    """Custom type hpicfLinkTestNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfLinkTestNextIndex_Type.__name__ = "Integer32"
_HpicfLinkTestNextIndex_Object = MibScalar
hpicfLinkTestNextIndex = _HpicfLinkTestNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 1),
    _HpicfLinkTestNextIndex_Type()
)
hpicfLinkTestNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLinkTestNextIndex.setStatus("current")
_HpicfLinkTestTable_Object = MibTable
hpicfLinkTestTable = _HpicfLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hpicfLinkTestTable.setStatus("current")
_HpicfLinkTestEntry_Object = MibTableRow
hpicfLinkTestEntry = _HpicfLinkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1)
)
hpicfLinkTestEntry.setIndexNames(
    (0, "HP-ICF-LINKTEST", "hpicfLinkTestIndex"),
)
if mibBuilder.loadTexts:
    hpicfLinkTestEntry.setStatus("current")


class _HpicfLinkTestIndex_Type(Integer32):
    """Custom type hpicfLinkTestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfLinkTestIndex_Type.__name__ = "Integer32"
_HpicfLinkTestIndex_Object = MibTableColumn
hpicfLinkTestIndex = _HpicfLinkTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 1),
    _HpicfLinkTestIndex_Type()
)
hpicfLinkTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLinkTestIndex.setStatus("current")


class _HpicfLinkTestType_Type(Integer32):
    """Custom type hpicfLinkTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("icmpEcho", 1),
          ("ieee8022Test", 2),
          ("ipxDiagnostic", 3))
    )


_HpicfLinkTestType_Type.__name__ = "Integer32"
_HpicfLinkTestType_Object = MibTableColumn
hpicfLinkTestType = _HpicfLinkTestType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 2),
    _HpicfLinkTestType_Type()
)
hpicfLinkTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLinkTestType.setStatus("current")


class _HpicfLinkTestAddress_Type(OctetString):
    """Custom type hpicfLinkTestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(10, 10),
    )


_HpicfLinkTestAddress_Type.__name__ = "OctetString"
_HpicfLinkTestAddress_Object = MibTableColumn
hpicfLinkTestAddress = _HpicfLinkTestAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 3),
    _HpicfLinkTestAddress_Type()
)
hpicfLinkTestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLinkTestAddress.setStatus("current")


class _HpicfLinkTestIfIndex_Type(Integer32):
    """Custom type hpicfLinkTestIfIndex based on Integer32"""
    defaultValue = 0


_HpicfLinkTestIfIndex_Object = MibTableColumn
hpicfLinkTestIfIndex = _HpicfLinkTestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 4),
    _HpicfLinkTestIfIndex_Type()
)
hpicfLinkTestIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLinkTestIfIndex.setStatus("current")


class _HpicfLinkTestTimeout_Type(TimeInterval):
    """Custom type hpicfLinkTestTimeout based on TimeInterval"""
    defaultValue = 100


_HpicfLinkTestTimeout_Object = MibTableColumn
hpicfLinkTestTimeout = _HpicfLinkTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 5),
    _HpicfLinkTestTimeout_Type()
)
hpicfLinkTestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLinkTestTimeout.setStatus("current")


class _HpicfLinkTestRepetitions_Type(Integer32):
    """Custom type hpicfLinkTestRepetitions based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfLinkTestRepetitions_Type.__name__ = "Integer32"
_HpicfLinkTestRepetitions_Object = MibTableColumn
hpicfLinkTestRepetitions = _HpicfLinkTestRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 6),
    _HpicfLinkTestRepetitions_Type()
)
hpicfLinkTestRepetitions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLinkTestRepetitions.setStatus("current")


class _HpicfLinkTestAttempts_Type(Integer32):
    """Custom type hpicfLinkTestAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfLinkTestAttempts_Type.__name__ = "Integer32"
_HpicfLinkTestAttempts_Object = MibTableColumn
hpicfLinkTestAttempts = _HpicfLinkTestAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 7),
    _HpicfLinkTestAttempts_Type()
)
hpicfLinkTestAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLinkTestAttempts.setStatus("current")


class _HpicfLinkTestSuccesses_Type(Integer32):
    """Custom type hpicfLinkTestSuccesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfLinkTestSuccesses_Type.__name__ = "Integer32"
_HpicfLinkTestSuccesses_Object = MibTableColumn
hpicfLinkTestSuccesses = _HpicfLinkTestSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 8),
    _HpicfLinkTestSuccesses_Type()
)
hpicfLinkTestSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLinkTestSuccesses.setStatus("current")
_HpicfLinkTestMinRespTime_Type = Integer32
_HpicfLinkTestMinRespTime_Object = MibTableColumn
hpicfLinkTestMinRespTime = _HpicfLinkTestMinRespTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 9),
    _HpicfLinkTestMinRespTime_Type()
)
hpicfLinkTestMinRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLinkTestMinRespTime.setStatus("current")
_HpicfLinkTestMaxRespTime_Type = Integer32
_HpicfLinkTestMaxRespTime_Object = MibTableColumn
hpicfLinkTestMaxRespTime = _HpicfLinkTestMaxRespTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 10),
    _HpicfLinkTestMaxRespTime_Type()
)
hpicfLinkTestMaxRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLinkTestMaxRespTime.setStatus("current")
_HpicfLinkTestTotalRespTime_Type = Integer32
_HpicfLinkTestTotalRespTime_Object = MibTableColumn
hpicfLinkTestTotalRespTime = _HpicfLinkTestTotalRespTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 11),
    _HpicfLinkTestTotalRespTime_Type()
)
hpicfLinkTestTotalRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLinkTestTotalRespTime.setStatus("current")
_HpicfLinkTestOwner_Type = OwnerString
_HpicfLinkTestOwner_Object = MibTableColumn
hpicfLinkTestOwner = _HpicfLinkTestOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 12),
    _HpicfLinkTestOwner_Type()
)
hpicfLinkTestOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLinkTestOwner.setStatus("current")
_HpicfLinkTestStatus_Type = RowStatus
_HpicfLinkTestStatus_Object = MibTableColumn
hpicfLinkTestStatus = _HpicfLinkTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 13),
    _HpicfLinkTestStatus_Type()
)
hpicfLinkTestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLinkTestStatus.setStatus("current")


class _HpicfLinkTestDeleteMode_Type(Integer32):
    """Custom type hpicfLinkTestDeleteMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destroyWhenDone", 2),
          ("keepWhenDone", 1))
    )


_HpicfLinkTestDeleteMode_Type.__name__ = "Integer32"
_HpicfLinkTestDeleteMode_Object = MibTableColumn
hpicfLinkTestDeleteMode = _HpicfLinkTestDeleteMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 14),
    _HpicfLinkTestDeleteMode_Type()
)
hpicfLinkTestDeleteMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLinkTestDeleteMode.setStatus("current")

# Managed Objects groups

hpicfLinkTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 2, 1)
)
hpicfLinkTestGroup.setObjects(
      *(("HP-ICF-LINKTEST", "hpicfLinkTestNextIndex"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestType"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestAddress"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestIfIndex"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestTimeout"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestRepetitions"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestAttempts"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestSuccesses"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestMinRespTime"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestMaxRespTime"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestTotalRespTime"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestOwner"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestStatus"))
)
if mibBuilder.loadTexts:
    hpicfLinkTestGroup.setStatus("deprecated")

hpicfLinkTestGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 2, 2)
)
hpicfLinkTestGroup2.setObjects(
      *(("HP-ICF-LINKTEST", "hpicfLinkTestNextIndex"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestType"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestAddress"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestIfIndex"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestTimeout"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestRepetitions"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestAttempts"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestSuccesses"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestMinRespTime"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestMaxRespTime"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestTotalRespTime"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestOwner"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestStatus"),
        ("HP-ICF-LINKTEST", "hpicfLinkTestDeleteMode"))
)
if mibBuilder.loadTexts:
    hpicfLinkTestGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfLinkTestCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfLinkTestCompliance.setStatus(
        "deprecated"
    )

hpicfLinkTestCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfLinkTestCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-LINKTEST",
    **{"hpicfLinkTestMib": hpicfLinkTestMib,
       "hpicfLinkTestConformance": hpicfLinkTestConformance,
       "hpicfLinkTestCompliances": hpicfLinkTestCompliances,
       "hpicfLinkTestCompliance": hpicfLinkTestCompliance,
       "hpicfLinkTestCompliance2": hpicfLinkTestCompliance2,
       "hpicfLinkTestGroups": hpicfLinkTestGroups,
       "hpicfLinkTestGroup": hpicfLinkTestGroup,
       "hpicfLinkTestGroup2": hpicfLinkTestGroup2,
       "hpicfLinktest": hpicfLinktest,
       "hpicfLinkTestNextIndex": hpicfLinkTestNextIndex,
       "hpicfLinkTestTable": hpicfLinkTestTable,
       "hpicfLinkTestEntry": hpicfLinkTestEntry,
       "hpicfLinkTestIndex": hpicfLinkTestIndex,
       "hpicfLinkTestType": hpicfLinkTestType,
       "hpicfLinkTestAddress": hpicfLinkTestAddress,
       "hpicfLinkTestIfIndex": hpicfLinkTestIfIndex,
       "hpicfLinkTestTimeout": hpicfLinkTestTimeout,
       "hpicfLinkTestRepetitions": hpicfLinkTestRepetitions,
       "hpicfLinkTestAttempts": hpicfLinkTestAttempts,
       "hpicfLinkTestSuccesses": hpicfLinkTestSuccesses,
       "hpicfLinkTestMinRespTime": hpicfLinkTestMinRespTime,
       "hpicfLinkTestMaxRespTime": hpicfLinkTestMaxRespTime,
       "hpicfLinkTestTotalRespTime": hpicfLinkTestTotalRespTime,
       "hpicfLinkTestOwner": hpicfLinkTestOwner,
       "hpicfLinkTestStatus": hpicfLinkTestStatus,
       "hpicfLinkTestDeleteMode": hpicfLinkTestDeleteMode}
)
