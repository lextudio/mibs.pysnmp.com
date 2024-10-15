# SNMP MIB module (CISCO-CABLE-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CABLE-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:33 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCableDiagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 390)
)
ciscoCableDiagMIB.setRevisions(
        ("2004-09-13 00:00",
         "2004-01-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCableDiagMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCableDiagMIBNotifs = _CiscoCableDiagMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 0)
)
_CiscoCableDiagMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCableDiagMIBObjects = _CiscoCableDiagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1)
)
_CcdPrbsObjects_ObjectIdentity = ObjectIdentity
ccdPrbsObjects = _CcdPrbsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1)
)
_CcdPrbsIfTable_Object = MibTable
ccdPrbsIfTable = _CcdPrbsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccdPrbsIfTable.setStatus("current")
_CcdPrbsIfEntry_Object = MibTableRow
ccdPrbsIfEntry = _CcdPrbsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1)
)
ccdPrbsIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ccdPrbsIfEntry.setStatus("current")


class _CcdPrbsIfAction_Type(Integer32):
    """Custom type ccdPrbsIfAction based on Integer32"""
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
        *(("errorReset", 3),
          ("notRunning", 5),
          ("running", 4),
          ("start", 1),
          ("stop", 2))
    )


_CcdPrbsIfAction_Type.__name__ = "Integer32"
_CcdPrbsIfAction_Object = MibTableColumn
ccdPrbsIfAction = _CcdPrbsIfAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1, 1),
    _CcdPrbsIfAction_Type()
)
ccdPrbsIfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccdPrbsIfAction.setStatus("current")


class _CcdPrbsIfActionStatus_Type(Integer32):
    """Custom type ccdPrbsIfActionStatus based on Integer32"""
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
        *(("failedDueToInterfaceDisabled", 7),
          ("failedDueToInternalError", 4),
          ("failedDueToResourceUnavailable", 3),
          ("failedDueToTestAlreadyStarted", 5),
          ("failedDueToTestAlreadyStopped", 6),
          ("failedDueToUnknownReason", 2),
          ("succeeded", 1))
    )


_CcdPrbsIfActionStatus_Type.__name__ = "Integer32"
_CcdPrbsIfActionStatus_Object = MibTableColumn
ccdPrbsIfActionStatus = _CcdPrbsIfActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1, 2),
    _CcdPrbsIfActionStatus_Type()
)
ccdPrbsIfActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdPrbsIfActionStatus.setStatus("current")
_CcdPrbsIfTestErrors_Type = Gauge32
_CcdPrbsIfTestErrors_Object = MibTableColumn
ccdPrbsIfTestErrors = _CcdPrbsIfTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1, 3),
    _CcdPrbsIfTestErrors_Type()
)
ccdPrbsIfTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdPrbsIfTestErrors.setStatus("current")
_CcdPrbsIfTestErrorsResetTime_Type = TimeStamp
_CcdPrbsIfTestErrorsResetTime_Object = MibTableColumn
ccdPrbsIfTestErrorsResetTime = _CcdPrbsIfTestErrorsResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1, 4),
    _CcdPrbsIfTestErrorsResetTime_Type()
)
ccdPrbsIfTestErrorsResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdPrbsIfTestErrorsResetTime.setStatus("current")
_CcdPrbsIfTestErrorsMaxValue_Type = Unsigned32
_CcdPrbsIfTestErrorsMaxValue_Object = MibTableColumn
ccdPrbsIfTestErrorsMaxValue = _CcdPrbsIfTestErrorsMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1, 5),
    _CcdPrbsIfTestErrorsMaxValue_Type()
)
ccdPrbsIfTestErrorsMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdPrbsIfTestErrorsMaxValue.setStatus("current")
_CcdTdrObjects_ObjectIdentity = ObjectIdentity
ccdTdrObjects = _CcdTdrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2)
)
_CcdTdrIfTable_Object = MibTable
ccdTdrIfTable = _CcdTdrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccdTdrIfTable.setStatus("current")
_CcdTdrIfEntry_Object = MibTableRow
ccdTdrIfEntry = _CcdTdrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1, 1)
)
ccdTdrIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ccdTdrIfEntry.setStatus("current")


class _CcdTdrIfAction_Type(Integer32):
    """Custom type ccdTdrIfAction based on Integer32"""
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
        *(("clear", 2),
          ("notRunning", 4),
          ("running", 3),
          ("start", 1))
    )


_CcdTdrIfAction_Type.__name__ = "Integer32"
_CcdTdrIfAction_Object = MibTableColumn
ccdTdrIfAction = _CcdTdrIfAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1, 1, 1),
    _CcdTdrIfAction_Type()
)
ccdTdrIfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccdTdrIfAction.setStatus("current")


class _CcdTdrIfActionStatus_Type(Integer32):
    """Custom type ccdTdrIfActionStatus based on Integer32"""
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
        *(("failedDueToInterfaceDisabled", 6),
          ("failedDueToInternalError", 4),
          ("failedDueToResourceUnavailable", 3),
          ("failedDueToTestAlreadyRunning", 5),
          ("failedDueToUnknownReason", 2),
          ("succeeded", 1))
    )


_CcdTdrIfActionStatus_Type.__name__ = "Integer32"
_CcdTdrIfActionStatus_Object = MibTableColumn
ccdTdrIfActionStatus = _CcdTdrIfActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1, 1, 2),
    _CcdTdrIfActionStatus_Type()
)
ccdTdrIfActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdTdrIfActionStatus.setStatus("current")
_CcdTdrIfLastTestTime_Type = TimeStamp
_CcdTdrIfLastTestTime_Object = MibTableColumn
ccdTdrIfLastTestTime = _CcdTdrIfLastTestTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1, 1, 3),
    _CcdTdrIfLastTestTime_Type()
)
ccdTdrIfLastTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdTdrIfLastTestTime.setStatus("current")
_CcdTdrIfResultValid_Type = TruthValue
_CcdTdrIfResultValid_Object = MibTableColumn
ccdTdrIfResultValid = _CcdTdrIfResultValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1, 1, 4),
    _CcdTdrIfResultValid_Type()
)
ccdTdrIfResultValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdTdrIfResultValid.setStatus("current")
_CcdTdrIfResultTable_Object = MibTable
ccdTdrIfResultTable = _CcdTdrIfResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccdTdrIfResultTable.setStatus("current")
_CcdTdrIfResultEntry_Object = MibTableRow
ccdTdrIfResultEntry = _CcdTdrIfResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1)
)
ccdTdrIfResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairIndex"),
)
if mibBuilder.loadTexts:
    ccdTdrIfResultEntry.setStatus("current")


class _CcdTdrIfResultPairIndex_Type(Integer32):
    """Custom type ccdTdrIfResultPairIndex based on Integer32"""
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
        *(("pair1to2", 1),
          ("pair3to6", 2),
          ("pair4to5", 3),
          ("pair7to8", 4))
    )


_CcdTdrIfResultPairIndex_Type.__name__ = "Integer32"
_CcdTdrIfResultPairIndex_Object = MibTableColumn
ccdTdrIfResultPairIndex = _CcdTdrIfResultPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 1),
    _CcdTdrIfResultPairIndex_Type()
)
ccdTdrIfResultPairIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccdTdrIfResultPairIndex.setStatus("current")


class _CcdTdrIfResultPairChannel_Type(Integer32):
    """Custom type ccdTdrIfResultPairChannel based on Integer32"""
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
        *(("channelA", 2),
          ("channelB", 3),
          ("channelC", 4),
          ("channelD", 5),
          ("other", 1))
    )


_CcdTdrIfResultPairChannel_Type.__name__ = "Integer32"
_CcdTdrIfResultPairChannel_Object = MibTableColumn
ccdTdrIfResultPairChannel = _CcdTdrIfResultPairChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 2),
    _CcdTdrIfResultPairChannel_Type()
)
ccdTdrIfResultPairChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdTdrIfResultPairChannel.setStatus("current")


class _CcdTdrIfResultPairLength_Type(Integer32):
    """Custom type ccdTdrIfResultPairLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CcdTdrIfResultPairLength_Type.__name__ = "Integer32"
_CcdTdrIfResultPairLength_Object = MibTableColumn
ccdTdrIfResultPairLength = _CcdTdrIfResultPairLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 3),
    _CcdTdrIfResultPairLength_Type()
)
ccdTdrIfResultPairLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdTdrIfResultPairLength.setStatus("current")


class _CcdTdrIfResultPairLenAccuracy_Type(Integer32):
    """Custom type ccdTdrIfResultPairLenAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CcdTdrIfResultPairLenAccuracy_Type.__name__ = "Integer32"
_CcdTdrIfResultPairLenAccuracy_Object = MibTableColumn
ccdTdrIfResultPairLenAccuracy = _CcdTdrIfResultPairLenAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 4),
    _CcdTdrIfResultPairLenAccuracy_Type()
)
ccdTdrIfResultPairLenAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdTdrIfResultPairLenAccuracy.setStatus("current")


class _CcdTdrIfResultPairDistToFault_Type(Integer32):
    """Custom type ccdTdrIfResultPairDistToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CcdTdrIfResultPairDistToFault_Type.__name__ = "Integer32"
_CcdTdrIfResultPairDistToFault_Object = MibTableColumn
ccdTdrIfResultPairDistToFault = _CcdTdrIfResultPairDistToFault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 5),
    _CcdTdrIfResultPairDistToFault_Type()
)
ccdTdrIfResultPairDistToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdTdrIfResultPairDistToFault.setStatus("current")


class _CcdTdrIfResultPairDistAccuracy_Type(Integer32):
    """Custom type ccdTdrIfResultPairDistAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CcdTdrIfResultPairDistAccuracy_Type.__name__ = "Integer32"
_CcdTdrIfResultPairDistAccuracy_Object = MibTableColumn
ccdTdrIfResultPairDistAccuracy = _CcdTdrIfResultPairDistAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 6),
    _CcdTdrIfResultPairDistAccuracy_Type()
)
ccdTdrIfResultPairDistAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdTdrIfResultPairDistAccuracy.setStatus("current")


class _CcdTdrIfResultPairLengthUnit_Type(Integer32):
    """Custom type ccdTdrIfResultPairLengthUnit based on Integer32"""
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
        *(("centimeter", 3),
          ("kilometer", 4),
          ("meter", 2),
          ("unknown", 1))
    )


_CcdTdrIfResultPairLengthUnit_Type.__name__ = "Integer32"
_CcdTdrIfResultPairLengthUnit_Object = MibTableColumn
ccdTdrIfResultPairLengthUnit = _CcdTdrIfResultPairLengthUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 7),
    _CcdTdrIfResultPairLengthUnit_Type()
)
ccdTdrIfResultPairLengthUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdTdrIfResultPairLengthUnit.setStatus("current")


class _CcdTdrIfResultPairStatus_Type(Integer32):
    """Custom type ccdTdrIfResultPairStatus based on Integer32"""
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
        *(("broken", 8),
          ("impedanceMismatch", 7),
          ("indeterminate", 9),
          ("notCompleted", 3),
          ("notSupported", 4),
          ("open", 5),
          ("shorted", 6),
          ("terminated", 2),
          ("unknown", 1))
    )


_CcdTdrIfResultPairStatus_Type.__name__ = "Integer32"
_CcdTdrIfResultPairStatus_Object = MibTableColumn
ccdTdrIfResultPairStatus = _CcdTdrIfResultPairStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 8),
    _CcdTdrIfResultPairStatus_Type()
)
ccdTdrIfResultPairStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdTdrIfResultPairStatus.setStatus("current")
_CiscoCableDiagMIBConform_ObjectIdentity = ObjectIdentity
ciscoCableDiagMIBConform = _CiscoCableDiagMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 2)
)
_CiscoCableDiagMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCableDiagMIBCompliances = _CiscoCableDiagMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 2, 1)
)
_CiscoCableDiagMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCableDiagMIBGroups = _CiscoCableDiagMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 2, 2)
)

# Managed Objects groups

ccdPrbsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 2, 2, 1)
)
ccdPrbsGroup.setObjects(
      *(("CISCO-CABLE-DIAG-MIB", "ccdPrbsIfAction"),
        ("CISCO-CABLE-DIAG-MIB", "ccdPrbsIfActionStatus"),
        ("CISCO-CABLE-DIAG-MIB", "ccdPrbsIfTestErrors"),
        ("CISCO-CABLE-DIAG-MIB", "ccdPrbsIfTestErrorsResetTime"),
        ("CISCO-CABLE-DIAG-MIB", "ccdPrbsIfTestErrorsMaxValue"))
)
if mibBuilder.loadTexts:
    ccdPrbsGroup.setStatus("current")

ccdTdrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 2, 2, 2)
)
ccdTdrGroup.setObjects(
      *(("CISCO-CABLE-DIAG-MIB", "ccdTdrIfAction"),
        ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfActionStatus"),
        ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfLastTestTime"),
        ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultValid"),
        ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairChannel"),
        ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairLength"),
        ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairLenAccuracy"),
        ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairDistToFault"),
        ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairDistAccuracy"),
        ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairLengthUnit"),
        ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairStatus"))
)
if mibBuilder.loadTexts:
    ccdTdrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCableDiagMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 390, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCableDiagMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-DIAG-MIB",
    **{"ciscoCableDiagMIB": ciscoCableDiagMIB,
       "ciscoCableDiagMIBNotifs": ciscoCableDiagMIBNotifs,
       "ciscoCableDiagMIBObjects": ciscoCableDiagMIBObjects,
       "ccdPrbsObjects": ccdPrbsObjects,
       "ccdPrbsIfTable": ccdPrbsIfTable,
       "ccdPrbsIfEntry": ccdPrbsIfEntry,
       "ccdPrbsIfAction": ccdPrbsIfAction,
       "ccdPrbsIfActionStatus": ccdPrbsIfActionStatus,
       "ccdPrbsIfTestErrors": ccdPrbsIfTestErrors,
       "ccdPrbsIfTestErrorsResetTime": ccdPrbsIfTestErrorsResetTime,
       "ccdPrbsIfTestErrorsMaxValue": ccdPrbsIfTestErrorsMaxValue,
       "ccdTdrObjects": ccdTdrObjects,
       "ccdTdrIfTable": ccdTdrIfTable,
       "ccdTdrIfEntry": ccdTdrIfEntry,
       "ccdTdrIfAction": ccdTdrIfAction,
       "ccdTdrIfActionStatus": ccdTdrIfActionStatus,
       "ccdTdrIfLastTestTime": ccdTdrIfLastTestTime,
       "ccdTdrIfResultValid": ccdTdrIfResultValid,
       "ccdTdrIfResultTable": ccdTdrIfResultTable,
       "ccdTdrIfResultEntry": ccdTdrIfResultEntry,
       "ccdTdrIfResultPairIndex": ccdTdrIfResultPairIndex,
       "ccdTdrIfResultPairChannel": ccdTdrIfResultPairChannel,
       "ccdTdrIfResultPairLength": ccdTdrIfResultPairLength,
       "ccdTdrIfResultPairLenAccuracy": ccdTdrIfResultPairLenAccuracy,
       "ccdTdrIfResultPairDistToFault": ccdTdrIfResultPairDistToFault,
       "ccdTdrIfResultPairDistAccuracy": ccdTdrIfResultPairDistAccuracy,
       "ccdTdrIfResultPairLengthUnit": ccdTdrIfResultPairLengthUnit,
       "ccdTdrIfResultPairStatus": ccdTdrIfResultPairStatus,
       "ciscoCableDiagMIBConform": ciscoCableDiagMIBConform,
       "ciscoCableDiagMIBCompliances": ciscoCableDiagMIBCompliances,
       "ciscoCableDiagMIBComplianceRev1": ciscoCableDiagMIBComplianceRev1,
       "ciscoCableDiagMIBGroups": ciscoCableDiagMIBGroups,
       "ccdPrbsGroup": ccdPrbsGroup,
       "ccdTdrGroup": ccdTdrGroup}
)
