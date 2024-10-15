# SNMP MIB module (CISCO-OPTICAL-IF-CROSS-CONNECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OPTICAL-IF-CROSS-CONNECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:21 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoOpticalIfCrossConnectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 68)
)
ciscoOpticalIfCrossConnectMIB.setRevisions(
        ("2002-03-13 00:00",
         "2001-04-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CoifccCrossConnectOperStatus(Integer32, TextualConvention):
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
        *(("dormant", 3),
          ("down", 2),
          ("unknown", 4),
          ("up", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CoifccMIBObjects_ObjectIdentity = ObjectIdentity
coifccMIBObjects = _CoifccMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1)
)
_CoifccInterface_ObjectIdentity = ObjectIdentity
coifccInterface = _CoifccInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 1)
)
_CoifccInterfaceTable_Object = MibTable
coifccInterfaceTable = _CoifccInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coifccInterfaceTable.setStatus("current")
_CoifccInterfaceEntry_Object = MibTableRow
coifccInterfaceEntry = _CoifccInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 1, 1, 1)
)
coifccInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coifccInterfaceEntry.setStatus("current")


class _CoifccIfCrossConnectIdentifier_Type(Integer32):
    """Custom type coifccIfCrossConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483547),
    )


_CoifccIfCrossConnectIdentifier_Type.__name__ = "Integer32"
_CoifccIfCrossConnectIdentifier_Object = MibTableColumn
coifccIfCrossConnectIdentifier = _CoifccIfCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 1, 1, 1, 1),
    _CoifccIfCrossConnectIdentifier_Type()
)
coifccIfCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coifccIfCrossConnectIdentifier.setStatus("current")
_CoifccCrossConnect_ObjectIdentity = ObjectIdentity
coifccCrossConnect = _CoifccCrossConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2)
)


class _CoifccCcIndexNext_Type(Integer32):
    """Custom type coifccCcIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CoifccCcIndexNext_Type.__name__ = "Integer32"
_CoifccCcIndexNext_Object = MibScalar
coifccCcIndexNext = _CoifccCcIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 1),
    _CoifccCcIndexNext_Type()
)
coifccCcIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coifccCcIndexNext.setStatus("current")
_CoifccCcLastChange_Type = TimeStamp
_CoifccCcLastChange_Object = MibScalar
coifccCcLastChange = _CoifccCcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 2),
    _CoifccCcLastChange_Type()
)
coifccCcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coifccCcLastChange.setStatus("current")
_CoifccCrossConnectTable_Object = MibTable
coifccCrossConnectTable = _CoifccCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3)
)
if mibBuilder.loadTexts:
    coifccCrossConnectTable.setStatus("current")
_CoifccCrossConnectEntry_Object = MibTableRow
coifccCrossConnectEntry = _CoifccCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1)
)
coifccCrossConnectEntry.setIndexNames(
    (0, "CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcIndex"),
    (0, "CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcLowIfIndex"),
    (0, "CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcHighIfIndex"),
)
if mibBuilder.loadTexts:
    coifccCrossConnectEntry.setStatus("current")


class _CoifccCcIndex_Type(Integer32):
    """Custom type coifccCcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoifccCcIndex_Type.__name__ = "Integer32"
_CoifccCcIndex_Object = MibTableColumn
coifccCcIndex = _CoifccCcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 1),
    _CoifccCcIndex_Type()
)
coifccCcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coifccCcIndex.setStatus("current")
_CoifccCcLowIfIndex_Type = InterfaceIndex
_CoifccCcLowIfIndex_Object = MibTableColumn
coifccCcLowIfIndex = _CoifccCcLowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 2),
    _CoifccCcLowIfIndex_Type()
)
coifccCcLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coifccCcLowIfIndex.setStatus("current")
_CoifccCcHighIfIndex_Type = InterfaceIndex
_CoifccCcHighIfIndex_Object = MibTableColumn
coifccCcHighIfIndex = _CoifccCcHighIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 3),
    _CoifccCcHighIfIndex_Type()
)
coifccCcHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coifccCcHighIfIndex.setStatus("current")


class _CoifccCcSwitchType_Type(Integer32):
    """Custom type coifccCcSwitchType based on Integer32"""
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
        *(("autoSelect", 4),
          ("electricalCrossConnect", 2),
          ("opticalCrossConnect", 3),
          ("unknown", 1))
    )


_CoifccCcSwitchType_Type.__name__ = "Integer32"
_CoifccCcSwitchType_Object = MibTableColumn
coifccCcSwitchType = _CoifccCcSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 4),
    _CoifccCcSwitchType_Type()
)
coifccCcSwitchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coifccCcSwitchType.setStatus("current")


class _CoifccCcKind_Type(Integer32):
    """Custom type coifccCcKind based on Integer32"""
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
        *(("automatic", 2),
          ("dynamic", 3),
          ("other", 5),
          ("protection", 4),
          ("provisioned", 1))
    )


_CoifccCcKind_Type.__name__ = "Integer32"
_CoifccCcKind_Object = MibTableColumn
coifccCcKind = _CoifccCcKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 5),
    _CoifccCcKind_Type()
)
coifccCcKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coifccCcKind.setStatus("current")
_CoifccCcCreationTime_Type = TimeStamp
_CoifccCcCreationTime_Object = MibTableColumn
coifccCcCreationTime = _CoifccCcCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 6),
    _CoifccCcCreationTime_Type()
)
coifccCcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coifccCcCreationTime.setStatus("current")
_CoifccCcL2HOperStatus_Type = CoifccCrossConnectOperStatus
_CoifccCcL2HOperStatus_Object = MibTableColumn
coifccCcL2HOperStatus = _CoifccCcL2HOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 7),
    _CoifccCcL2HOperStatus_Type()
)
coifccCcL2HOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coifccCcL2HOperStatus.setStatus("current")
_CoifccCcH2LOperStatus_Type = CoifccCrossConnectOperStatus
_CoifccCcH2LOperStatus_Object = MibTableColumn
coifccCcH2LOperStatus = _CoifccCcH2LOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 8),
    _CoifccCcH2LOperStatus_Type()
)
coifccCcH2LOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coifccCcH2LOperStatus.setStatus("current")
_CoifccCcL2HLastChange_Type = TimeStamp
_CoifccCcL2HLastChange_Object = MibTableColumn
coifccCcL2HLastChange = _CoifccCcL2HLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 9),
    _CoifccCcL2HLastChange_Type()
)
coifccCcL2HLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coifccCcL2HLastChange.setStatus("current")
_CoifccCcH2LLastChange_Type = TimeStamp
_CoifccCcH2LLastChange_Object = MibTableColumn
coifccCcH2LLastChange = _CoifccCcH2LLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 10),
    _CoifccCcH2LLastChange_Type()
)
coifccCcH2LLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coifccCcH2LLastChange.setStatus("current")
_CoifccCcRowStatus_Type = RowStatus
_CoifccCcRowStatus_Object = MibTableColumn
coifccCcRowStatus = _CoifccCcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 11),
    _CoifccCcRowStatus_Type()
)
coifccCcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coifccCcRowStatus.setStatus("current")


class _CoifccCcL2HAttenuation_Type(Integer32):
    """Custom type coifccCcL2HAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 0),
    )


_CoifccCcL2HAttenuation_Type.__name__ = "Integer32"
_CoifccCcL2HAttenuation_Object = MibTableColumn
coifccCcL2HAttenuation = _CoifccCcL2HAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 12),
    _CoifccCcL2HAttenuation_Type()
)
coifccCcL2HAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coifccCcL2HAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    coifccCcL2HAttenuation.setUnits("1/10ths of dB")


class _CoifccCcH2LAttenuation_Type(Integer32):
    """Custom type coifccCcH2LAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 0),
    )


_CoifccCcH2LAttenuation_Type.__name__ = "Integer32"
_CoifccCcH2LAttenuation_Object = MibTableColumn
coifccCcH2LAttenuation = _CoifccCcH2LAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 1, 2, 3, 1, 13),
    _CoifccCcH2LAttenuation_Type()
)
coifccCcH2LAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coifccCcH2LAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    coifccCcH2LAttenuation.setUnits("1/10ths of dB")
_CoifccMIBConformance_ObjectIdentity = ObjectIdentity
coifccMIBConformance = _CoifccMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 2)
)
_CoifccMIBCompliances_ObjectIdentity = ObjectIdentity
coifccMIBCompliances = _CoifccMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 1)
)
_CoifccMIBGroups_ObjectIdentity = ObjectIdentity
coifccMIBGroups = _CoifccMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 2)
)

# Managed Objects groups

coifccInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 2, 1)
)
coifccInterfaceGroup.setObjects(
    ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccIfCrossConnectIdentifier")
)
if mibBuilder.loadTexts:
    coifccInterfaceGroup.setStatus("current")

coifccCrossConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 2, 2)
)
coifccCrossConnectGroup.setObjects(
      *(("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcIndexNext"),
        ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcLastChange"),
        ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcSwitchType"),
        ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcKind"),
        ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcCreationTime"),
        ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcL2HOperStatus"),
        ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcH2LOperStatus"),
        ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcL2HLastChange"),
        ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcH2LLastChange"),
        ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcRowStatus"))
)
if mibBuilder.loadTexts:
    coifccCrossConnectGroup.setStatus("current")

coifccAttenuationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 2, 3)
)
coifccAttenuationGroup.setObjects(
      *(("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcL2HAttenuation"),
        ("CISCO-OPTICAL-IF-CROSS-CONNECT-MIB", "coifccCcH2LAttenuation"))
)
if mibBuilder.loadTexts:
    coifccAttenuationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

coifccMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 1, 1)
)
if mibBuilder.loadTexts:
    coifccMIBCompliance.setStatus(
        "deprecated"
    )

coifccMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 68, 2, 1, 2)
)
if mibBuilder.loadTexts:
    coifccMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OPTICAL-IF-CROSS-CONNECT-MIB",
    **{"CoifccCrossConnectOperStatus": CoifccCrossConnectOperStatus,
       "ciscoOpticalIfCrossConnectMIB": ciscoOpticalIfCrossConnectMIB,
       "coifccMIBObjects": coifccMIBObjects,
       "coifccInterface": coifccInterface,
       "coifccInterfaceTable": coifccInterfaceTable,
       "coifccInterfaceEntry": coifccInterfaceEntry,
       "coifccIfCrossConnectIdentifier": coifccIfCrossConnectIdentifier,
       "coifccCrossConnect": coifccCrossConnect,
       "coifccCcIndexNext": coifccCcIndexNext,
       "coifccCcLastChange": coifccCcLastChange,
       "coifccCrossConnectTable": coifccCrossConnectTable,
       "coifccCrossConnectEntry": coifccCrossConnectEntry,
       "coifccCcIndex": coifccCcIndex,
       "coifccCcLowIfIndex": coifccCcLowIfIndex,
       "coifccCcHighIfIndex": coifccCcHighIfIndex,
       "coifccCcSwitchType": coifccCcSwitchType,
       "coifccCcKind": coifccCcKind,
       "coifccCcCreationTime": coifccCcCreationTime,
       "coifccCcL2HOperStatus": coifccCcL2HOperStatus,
       "coifccCcH2LOperStatus": coifccCcH2LOperStatus,
       "coifccCcL2HLastChange": coifccCcL2HLastChange,
       "coifccCcH2LLastChange": coifccCcH2LLastChange,
       "coifccCcRowStatus": coifccCcRowStatus,
       "coifccCcL2HAttenuation": coifccCcL2HAttenuation,
       "coifccCcH2LAttenuation": coifccCcH2LAttenuation,
       "coifccMIBConformance": coifccMIBConformance,
       "coifccMIBCompliances": coifccMIBCompliances,
       "coifccMIBCompliance": coifccMIBCompliance,
       "coifccMIBComplianceRev1": coifccMIBComplianceRev1,
       "coifccMIBGroups": coifccMIBGroups,
       "coifccInterfaceGroup": coifccInterfaceGroup,
       "coifccCrossConnectGroup": coifccCrossConnectGroup,
       "coifccAttenuationGroup": coifccAttenuationGroup}
)
