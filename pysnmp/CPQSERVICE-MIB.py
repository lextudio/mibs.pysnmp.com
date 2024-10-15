# SNMP MIB module (CPQSERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQSERVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:41 2024
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

(compaq,) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqService_ObjectIdentity = ObjectIdentity
cpqService = _CpqService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 164)
)
_CpqServiceMibRev_ObjectIdentity = ObjectIdentity
cpqServiceMibRev = _CpqServiceMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 164, 1)
)


class _CpqServiceMibRevMinor_Type(Integer32):
    """Custom type cpqServiceMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqServiceMibRevMinor_Type.__name__ = "Integer32"
_CpqServiceMibRevMinor_Object = MibScalar
cpqServiceMibRevMinor = _CpqServiceMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 1, 1),
    _CpqServiceMibRevMinor_Type()
)
cpqServiceMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceMibRevMinor.setStatus("mandatory")


class _CpqServiceMibRevMajor_Type(Integer32):
    """Custom type cpqServiceMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqServiceMibRevMajor_Type.__name__ = "Integer32"
_CpqServiceMibRevMajor_Object = MibScalar
cpqServiceMibRevMajor = _CpqServiceMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 1, 2),
    _CpqServiceMibRevMajor_Type()
)
cpqServiceMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceMibRevMajor.setStatus("mandatory")
_CpqServiceIncident_ObjectIdentity = ObjectIdentity
cpqServiceIncident = _CpqServiceIncident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 164, 2)
)


class _CpqServiceIncidentSeverity_Type(Integer32):
    """Custom type cpqServiceIncidentSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("important", 1),
          ("informational", 2))
    )


_CpqServiceIncidentSeverity_Type.__name__ = "Integer32"
_CpqServiceIncidentSeverity_Object = MibScalar
cpqServiceIncidentSeverity = _CpqServiceIncidentSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 1),
    _CpqServiceIncidentSeverity_Type()
)
cpqServiceIncidentSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentSeverity.setStatus("deprecated")


class _CpqServiceIncidentStatus_Type(Integer32):
    """Custom type cpqServiceIncidentStatus based on Integer32"""
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
        *(("assigned", 5),
          ("closed", 6),
          ("delivered", 3),
          ("intransit", 2),
          ("other", 1),
          ("submitted-to-ISEE", 7),
          ("undelivered", 4))
    )


_CpqServiceIncidentStatus_Type.__name__ = "Integer32"
_CpqServiceIncidentStatus_Object = MibScalar
cpqServiceIncidentStatus = _CpqServiceIncidentStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 2),
    _CpqServiceIncidentStatus_Type()
)
cpqServiceIncidentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentStatus.setStatus("mandatory")


class _CpqServiceIncidentInformation_Type(DisplayString):
    """Custom type cpqServiceIncidentInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentInformation_Type.__name__ = "DisplayString"
_CpqServiceIncidentInformation_Object = MibScalar
cpqServiceIncidentInformation = _CpqServiceIncidentInformation_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 3),
    _CpqServiceIncidentInformation_Type()
)
cpqServiceIncidentInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentInformation.setStatus("mandatory")


class _CpqServiceIncidentEvent_Type(DisplayString):
    """Custom type cpqServiceIncidentEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentEvent_Type.__name__ = "DisplayString"
_CpqServiceIncidentEvent_Object = MibScalar
cpqServiceIncidentEvent = _CpqServiceIncidentEvent_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 4),
    _CpqServiceIncidentEvent_Type()
)
cpqServiceIncidentEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentEvent.setStatus("mandatory")


class _CpqServiceIncidentUniqueID_Type(DisplayString):
    """Custom type cpqServiceIncidentUniqueID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentUniqueID_Type.__name__ = "DisplayString"
_CpqServiceIncidentUniqueID_Object = MibScalar
cpqServiceIncidentUniqueID = _CpqServiceIncidentUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 5),
    _CpqServiceIncidentUniqueID_Type()
)
cpqServiceIncidentUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentUniqueID.setStatus("mandatory")


class _CpqServiceIncidentTimeofOriginalEvent_Type(DisplayString):
    """Custom type cpqServiceIncidentTimeofOriginalEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentTimeofOriginalEvent_Type.__name__ = "DisplayString"
_CpqServiceIncidentTimeofOriginalEvent_Object = MibScalar
cpqServiceIncidentTimeofOriginalEvent = _CpqServiceIncidentTimeofOriginalEvent_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 6),
    _CpqServiceIncidentTimeofOriginalEvent_Type()
)
cpqServiceIncidentTimeofOriginalEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentTimeofOriginalEvent.setStatus("mandatory")


class _CpqServiceIncidentSourceSystemName_Type(DisplayString):
    """Custom type cpqServiceIncidentSourceSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentSourceSystemName_Type.__name__ = "DisplayString"
_CpqServiceIncidentSourceSystemName_Object = MibScalar
cpqServiceIncidentSourceSystemName = _CpqServiceIncidentSourceSystemName_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 7),
    _CpqServiceIncidentSourceSystemName_Type()
)
cpqServiceIncidentSourceSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentSourceSystemName.setStatus("mandatory")
_CpqServiceIncidentIPAddessOfSource_Type = IpAddress
_CpqServiceIncidentIPAddessOfSource_Object = MibScalar
cpqServiceIncidentIPAddessOfSource = _CpqServiceIncidentIPAddessOfSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 8),
    _CpqServiceIncidentIPAddessOfSource_Type()
)
cpqServiceIncidentIPAddessOfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentIPAddessOfSource.setStatus("mandatory")


class _CpqServiceISEEIncidentInformation_Type(DisplayString):
    """Custom type cpqServiceISEEIncidentInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceISEEIncidentInformation_Type.__name__ = "DisplayString"
_CpqServiceISEEIncidentInformation_Object = MibScalar
cpqServiceISEEIncidentInformation = _CpqServiceISEEIncidentInformation_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 9),
    _CpqServiceISEEIncidentInformation_Type()
)
cpqServiceISEEIncidentInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceISEEIncidentInformation.setStatus("mandatory")


class _CpqServiceIncidentIdentifier_Type(DisplayString):
    """Custom type cpqServiceIncidentIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentIdentifier_Type.__name__ = "DisplayString"
_CpqServiceIncidentIdentifier_Object = MibScalar
cpqServiceIncidentIdentifier = _CpqServiceIncidentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 10),
    _CpqServiceIncidentIdentifier_Type()
)
cpqServiceIncidentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentIdentifier.setStatus("mandatory")
_CpqServiceIncidentReceiveTrapOID_Type = ObjectIdentifier
_CpqServiceIncidentReceiveTrapOID_Object = MibScalar
cpqServiceIncidentReceiveTrapOID = _CpqServiceIncidentReceiveTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 11),
    _CpqServiceIncidentReceiveTrapOID_Type()
)
cpqServiceIncidentReceiveTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentReceiveTrapOID.setStatus("mandatory")
_CpqServiceIncidentFilterOID_Type = ObjectIdentifier
_CpqServiceIncidentFilterOID_Object = MibScalar
cpqServiceIncidentFilterOID = _CpqServiceIncidentFilterOID_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 12),
    _CpqServiceIncidentFilterOID_Type()
)
cpqServiceIncidentFilterOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentFilterOID.setStatus("deprecated")


class _CpqServiceIncidentFilterValue_Type(DisplayString):
    """Custom type cpqServiceIncidentFilterValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentFilterValue_Type.__name__ = "DisplayString"
_CpqServiceIncidentFilterValue_Object = MibScalar
cpqServiceIncidentFilterValue = _CpqServiceIncidentFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 13),
    _CpqServiceIncidentFilterValue_Type()
)
cpqServiceIncidentFilterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentFilterValue.setStatus("deprecated")


class _CpqServiceRecommendedAction1_Type(DisplayString):
    """Custom type cpqServiceRecommendedAction1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceRecommendedAction1_Type.__name__ = "DisplayString"
_CpqServiceRecommendedAction1_Object = MibScalar
cpqServiceRecommendedAction1 = _CpqServiceRecommendedAction1_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 14),
    _CpqServiceRecommendedAction1_Type()
)
cpqServiceRecommendedAction1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceRecommendedAction1.setStatus("mandatory")


class _CpqServiceRecommendedAction2_Type(DisplayString):
    """Custom type cpqServiceRecommendedAction2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceRecommendedAction2_Type.__name__ = "DisplayString"
_CpqServiceRecommendedAction2_Object = MibScalar
cpqServiceRecommendedAction2 = _CpqServiceRecommendedAction2_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 15),
    _CpqServiceRecommendedAction2_Type()
)
cpqServiceRecommendedAction2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceRecommendedAction2.setStatus("mandatory")


class _CpqServiceRecommendedAction3_Type(DisplayString):
    """Custom type cpqServiceRecommendedAction3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceRecommendedAction3_Type.__name__ = "DisplayString"
_CpqServiceRecommendedAction3_Object = MibScalar
cpqServiceRecommendedAction3 = _CpqServiceRecommendedAction3_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 16),
    _CpqServiceRecommendedAction3_Type()
)
cpqServiceRecommendedAction3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceRecommendedAction3.setStatus("mandatory")


class _CpqServiceCustomerSelfRepairInstructionURL_Type(DisplayString):
    """Custom type cpqServiceCustomerSelfRepairInstructionURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceCustomerSelfRepairInstructionURL_Type.__name__ = "DisplayString"
_CpqServiceCustomerSelfRepairInstructionURL_Object = MibScalar
cpqServiceCustomerSelfRepairInstructionURL = _CpqServiceCustomerSelfRepairInstructionURL_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 17),
    _CpqServiceCustomerSelfRepairInstructionURL_Type()
)
cpqServiceCustomerSelfRepairInstructionURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceCustomerSelfRepairInstructionURL.setStatus("mandatory")


class _CpqServiceEventSeverity_Type(Integer32):
    """Custom type cpqServiceEventSeverity based on Integer32"""
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
        *(("critical", 1),
          ("informational", 5),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_CpqServiceEventSeverity_Type.__name__ = "Integer32"
_CpqServiceEventSeverity_Object = MibScalar
cpqServiceEventSeverity = _CpqServiceEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 18),
    _CpqServiceEventSeverity_Type()
)
cpqServiceEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceEventSeverity.setStatus("mandatory")


class _CpqServiceAnalyzerSystemName_Type(DisplayString):
    """Custom type cpqServiceAnalyzerSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceAnalyzerSystemName_Type.__name__ = "DisplayString"
_CpqServiceAnalyzerSystemName_Object = MibScalar
cpqServiceAnalyzerSystemName = _CpqServiceAnalyzerSystemName_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 19),
    _CpqServiceAnalyzerSystemName_Type()
)
cpqServiceAnalyzerSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceAnalyzerSystemName.setStatus("mandatory")


class _CpqServiceFRUList1_Type(DisplayString):
    """Custom type cpqServiceFRUList1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceFRUList1_Type.__name__ = "DisplayString"
_CpqServiceFRUList1_Object = MibScalar
cpqServiceFRUList1 = _CpqServiceFRUList1_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 20),
    _CpqServiceFRUList1_Type()
)
cpqServiceFRUList1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceFRUList1.setStatus("mandatory")


class _CpqServiceFRUList2_Type(DisplayString):
    """Custom type cpqServiceFRUList2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceFRUList2_Type.__name__ = "DisplayString"
_CpqServiceFRUList2_Object = MibScalar
cpqServiceFRUList2 = _CpqServiceFRUList2_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 21),
    _CpqServiceFRUList2_Type()
)
cpqServiceFRUList2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceFRUList2.setStatus("mandatory")


class _CpqServiceFRUList3_Type(DisplayString):
    """Custom type cpqServiceFRUList3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceFRUList3_Type.__name__ = "DisplayString"
_CpqServiceFRUList3_Object = MibScalar
cpqServiceFRUList3 = _CpqServiceFRUList3_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 22),
    _CpqServiceFRUList3_Type()
)
cpqServiceFRUList3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceFRUList3.setStatus("mandatory")


class _CpqServiceFRUList4_Type(DisplayString):
    """Custom type cpqServiceFRUList4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceFRUList4_Type.__name__ = "DisplayString"
_CpqServiceFRUList4_Object = MibScalar
cpqServiceFRUList4 = _CpqServiceFRUList4_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 23),
    _CpqServiceFRUList4_Type()
)
cpqServiceFRUList4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceFRUList4.setStatus("mandatory")


class _CpqServiceLocation1_Type(DisplayString):
    """Custom type cpqServiceLocation1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceLocation1_Type.__name__ = "DisplayString"
_CpqServiceLocation1_Object = MibScalar
cpqServiceLocation1 = _CpqServiceLocation1_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 24),
    _CpqServiceLocation1_Type()
)
cpqServiceLocation1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceLocation1.setStatus("mandatory")


class _CpqServiceLocation2_Type(DisplayString):
    """Custom type cpqServiceLocation2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceLocation2_Type.__name__ = "DisplayString"
_CpqServiceLocation2_Object = MibScalar
cpqServiceLocation2 = _CpqServiceLocation2_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 25),
    _CpqServiceLocation2_Type()
)
cpqServiceLocation2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceLocation2.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqServiceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 164, 0, 164001)
)
cpqServiceInformation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentSeverity"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentStatus"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentEvent"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentUniqueID"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentTimeofOriginalEvent"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentSourceSystemName"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentIPAddessOfSource"),
        ("CPQSERVICE-MIB", "cpqServiceISEEIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentIdentifier"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentReceiveTrapOID"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentFilterOID"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentFilterValue"))
)
if mibBuilder.loadTexts:
    cpqServiceInformation.setStatus(
        ""
    )

cpqService2Information = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 164, 0, 164002)
)
cpqService2Information.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentStatus"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentEvent"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentUniqueID"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentTimeofOriginalEvent"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentSourceSystemName"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentIPAddessOfSource"),
        ("CPQSERVICE-MIB", "cpqServiceISEEIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentIdentifier"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentReceiveTrapOID"),
        ("CPQSERVICE-MIB", "cpqServiceRecommendedAction1"),
        ("CPQSERVICE-MIB", "cpqServiceRecommendedAction2"),
        ("CPQSERVICE-MIB", "cpqServiceRecommendedAction3"),
        ("CPQSERVICE-MIB", "cpqServiceCustomerSelfRepairInstructionURL"))
)
if mibBuilder.loadTexts:
    cpqService2Information.setStatus(
        ""
    )

cpqService3Information = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 164, 0, 164003)
)
cpqService3Information.setObjects(
      *(("CPQSERVICE-MIB", "cpqServiceIncidentSourceSystemName"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentIPAddessOfSource"),
        ("CPQSERVICE-MIB", "cpqServiceEventSeverity"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentStatus"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentEvent"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentUniqueID"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentTimeofOriginalEvent"),
        ("CPQSERVICE-MIB", "cpqServiceAnalyzerSystemName"),
        ("CPQSERVICE-MIB", "cpqServiceISEEIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentIdentifier"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentReceiveTrapOID"),
        ("CPQSERVICE-MIB", "cpqServiceRecommendedAction1"),
        ("CPQSERVICE-MIB", "cpqServiceRecommendedAction2"),
        ("CPQSERVICE-MIB", "cpqServiceRecommendedAction3"),
        ("CPQSERVICE-MIB", "cpqServiceFRUList1"),
        ("CPQSERVICE-MIB", "cpqServiceFRUList2"),
        ("CPQSERVICE-MIB", "cpqServiceFRUList3"),
        ("CPQSERVICE-MIB", "cpqServiceFRUList4"),
        ("CPQSERVICE-MIB", "cpqServiceLocation1"),
        ("CPQSERVICE-MIB", "cpqServiceLocation2"),
        ("CPQSERVICE-MIB", "cpqServiceCustomerSelfRepairInstructionURL"))
)
if mibBuilder.loadTexts:
    cpqService3Information.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSERVICE-MIB",
    **{"cpqService": cpqService,
       "cpqServiceInformation": cpqServiceInformation,
       "cpqService2Information": cpqService2Information,
       "cpqService3Information": cpqService3Information,
       "cpqServiceMibRev": cpqServiceMibRev,
       "cpqServiceMibRevMinor": cpqServiceMibRevMinor,
       "cpqServiceMibRevMajor": cpqServiceMibRevMajor,
       "cpqServiceIncident": cpqServiceIncident,
       "cpqServiceIncidentSeverity": cpqServiceIncidentSeverity,
       "cpqServiceIncidentStatus": cpqServiceIncidentStatus,
       "cpqServiceIncidentInformation": cpqServiceIncidentInformation,
       "cpqServiceIncidentEvent": cpqServiceIncidentEvent,
       "cpqServiceIncidentUniqueID": cpqServiceIncidentUniqueID,
       "cpqServiceIncidentTimeofOriginalEvent": cpqServiceIncidentTimeofOriginalEvent,
       "cpqServiceIncidentSourceSystemName": cpqServiceIncidentSourceSystemName,
       "cpqServiceIncidentIPAddessOfSource": cpqServiceIncidentIPAddessOfSource,
       "cpqServiceISEEIncidentInformation": cpqServiceISEEIncidentInformation,
       "cpqServiceIncidentIdentifier": cpqServiceIncidentIdentifier,
       "cpqServiceIncidentReceiveTrapOID": cpqServiceIncidentReceiveTrapOID,
       "cpqServiceIncidentFilterOID": cpqServiceIncidentFilterOID,
       "cpqServiceIncidentFilterValue": cpqServiceIncidentFilterValue,
       "cpqServiceRecommendedAction1": cpqServiceRecommendedAction1,
       "cpqServiceRecommendedAction2": cpqServiceRecommendedAction2,
       "cpqServiceRecommendedAction3": cpqServiceRecommendedAction3,
       "cpqServiceCustomerSelfRepairInstructionURL": cpqServiceCustomerSelfRepairInstructionURL,
       "cpqServiceEventSeverity": cpqServiceEventSeverity,
       "cpqServiceAnalyzerSystemName": cpqServiceAnalyzerSystemName,
       "cpqServiceFRUList1": cpqServiceFRUList1,
       "cpqServiceFRUList2": cpqServiceFRUList2,
       "cpqServiceFRUList3": cpqServiceFRUList3,
       "cpqServiceFRUList4": cpqServiceFRUList4,
       "cpqServiceLocation1": cpqServiceLocation1,
       "cpqServiceLocation2": cpqServiceLocation2}
)
