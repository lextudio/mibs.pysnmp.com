# SNMP MIB module (IBM-LES-LECS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-LES-LECS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:36 2024
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

(AtmPrivateAddrEsi,
 AtmSelector,
 AtmVccTrafficType,
 Bandwidth,
 mssServerLanE) = mibBuilder.importSymbols(
    "NWAYSMSS-MIB",
    "AtmPrivateAddrEsi",
    "AtmSelector",
    "AtmVccTrafficType",
    "Bandwidth",
    "mssServerLanE")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbmLesLecsMIB_ObjectIdentity = ObjectIdentity
ibmLesLecsMIB = _IbmLesLecsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2)
)
_IbmLesLecsConfGroup_ObjectIdentity = ObjectIdentity
ibmLesLecsConfGroup = _IbmLesLecsConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1)
)
_LesLecsConfTable_Object = MibTable
lesLecsConfTable = _LesLecsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lesLecsConfTable.setStatus("mandatory")
_LesLecsConfEntry_Object = MibTableRow
lesLecsConfEntry = _LesLecsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1)
)
lesLecsConfEntry.setIndexNames(
    (0, "IBM-LES-LECS-MIB", "lesLecsAtmDevNum"),
)
if mibBuilder.loadTexts:
    lesLecsConfEntry.setStatus("mandatory")


class _LesLecsOperStatus_Type(Integer32):
    """Custom type lesLecsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_LesLecsOperStatus_Type.__name__ = "Integer32"
_LesLecsOperStatus_Object = MibTableColumn
lesLecsOperStatus = _LesLecsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 1),
    _LesLecsOperStatus_Type()
)
lesLecsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecsOperStatus.setStatus("mandatory")


class _LesLecsAdminStatus_Type(Integer32):
    """Custom type lesLecsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("up", 2))
    )


_LesLecsAdminStatus_Type.__name__ = "Integer32"
_LesLecsAdminStatus_Object = MibTableColumn
lesLecsAdminStatus = _LesLecsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 2),
    _LesLecsAdminStatus_Type()
)
lesLecsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLecsAdminStatus.setStatus("mandatory")


class _LesLecsAtmDevNum_Type(Integer32):
    """Custom type lesLecsAtmDevNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LesLecsAtmDevNum_Type.__name__ = "Integer32"
_LesLecsAtmDevNum_Object = MibTableColumn
lesLecsAtmDevNum = _LesLecsAtmDevNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 3),
    _LesLecsAtmDevNum_Type()
)
lesLecsAtmDevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecsAtmDevNum.setStatus("mandatory")
_LesLecsAtmDevLineSpeed_Type = Integer32
_LesLecsAtmDevLineSpeed_Object = MibTableColumn
lesLecsAtmDevLineSpeed = _LesLecsAtmDevLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 4),
    _LesLecsAtmDevLineSpeed_Type()
)
lesLecsAtmDevLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecsAtmDevLineSpeed.setStatus("mandatory")
_LesLecsUseBurnedInEsi_Type = TruthValue
_LesLecsUseBurnedInEsi_Object = MibTableColumn
lesLecsUseBurnedInEsi = _LesLecsUseBurnedInEsi_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 5),
    _LesLecsUseBurnedInEsi_Type()
)
lesLecsUseBurnedInEsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLecsUseBurnedInEsi.setStatus("mandatory")
_LesLecsConfiguredEsi_Type = AtmPrivateAddrEsi
_LesLecsConfiguredEsi_Object = MibTableColumn
lesLecsConfiguredEsi = _LesLecsConfiguredEsi_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 6),
    _LesLecsConfiguredEsi_Type()
)
lesLecsConfiguredEsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLecsConfiguredEsi.setStatus("mandatory")
_LesLecsConfiguredSelector_Type = AtmSelector
_LesLecsConfiguredSelector_Object = MibTableColumn
lesLecsConfiguredSelector = _LesLecsConfiguredSelector_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 7),
    _LesLecsConfiguredSelector_Type()
)
lesLecsConfiguredSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLecsConfiguredSelector.setStatus("mandatory")
_ConfigDirectVccType_Type = AtmVccTrafficType
_ConfigDirectVccType_Object = MibTableColumn
configDirectVccType = _ConfigDirectVccType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 8),
    _ConfigDirectVccType_Type()
)
configDirectVccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDirectVccType.setStatus("mandatory")
_ConfigDirectPcr_Type = Bandwidth
_ConfigDirectPcr_Object = MibTableColumn
configDirectPcr = _ConfigDirectPcr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 9),
    _ConfigDirectPcr_Type()
)
configDirectPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDirectPcr.setStatus("mandatory")
_ConfigDirectScr_Type = Bandwidth
_ConfigDirectScr_Object = MibTableColumn
configDirectScr = _ConfigDirectScr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 10),
    _ConfigDirectScr_Type()
)
configDirectScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDirectScr.setStatus("mandatory")
_LesLecsConfRowStatus_Type = RowStatus
_LesLecsConfRowStatus_Object = MibTableColumn
lesLecsConfRowStatus = _LesLecsConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 1, 1, 1, 11),
    _LesLecsConfRowStatus_Type()
)
lesLecsConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLecsConfRowStatus.setStatus("mandatory")
_IbmLesLecsMIBConformance_ObjectIdentity = ObjectIdentity
ibmLesLecsMIBConformance = _IbmLesLecsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 2)
)
_IbmLesLecsMIBGroups_ObjectIdentity = ObjectIdentity
ibmLesLecsMIBGroups = _IbmLesLecsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 2, 1)
)
_IbmLesLecsCConfGroup_ObjectIdentity = ObjectIdentity
ibmLesLecsCConfGroup = _IbmLesLecsCConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 2, 1, 1)
)
_IbmLesLecsMIBCompliances_ObjectIdentity = ObjectIdentity
ibmLesLecsMIBCompliances = _IbmLesLecsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 2, 2)
)
_IbmLesLecsMIBCompliance_ObjectIdentity = ObjectIdentity
ibmLesLecsMIBCompliance = _IbmLesLecsMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 2, 2, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-LES-LECS-MIB",
    **{"ibmLesLecsMIB": ibmLesLecsMIB,
       "ibmLesLecsConfGroup": ibmLesLecsConfGroup,
       "lesLecsConfTable": lesLecsConfTable,
       "lesLecsConfEntry": lesLecsConfEntry,
       "lesLecsOperStatus": lesLecsOperStatus,
       "lesLecsAdminStatus": lesLecsAdminStatus,
       "lesLecsAtmDevNum": lesLecsAtmDevNum,
       "lesLecsAtmDevLineSpeed": lesLecsAtmDevLineSpeed,
       "lesLecsUseBurnedInEsi": lesLecsUseBurnedInEsi,
       "lesLecsConfiguredEsi": lesLecsConfiguredEsi,
       "lesLecsConfiguredSelector": lesLecsConfiguredSelector,
       "configDirectVccType": configDirectVccType,
       "configDirectPcr": configDirectPcr,
       "configDirectScr": configDirectScr,
       "lesLecsConfRowStatus": lesLecsConfRowStatus,
       "ibmLesLecsMIBConformance": ibmLesLecsMIBConformance,
       "ibmLesLecsMIBGroups": ibmLesLecsMIBGroups,
       "ibmLesLecsCConfGroup": ibmLesLecsCConfGroup,
       "ibmLesLecsMIBCompliances": ibmLesLecsMIBCompliances,
       "ibmLesLecsMIBCompliance": ibmLesLecsMIBCompliance}
)
