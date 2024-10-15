# SNMP MIB module (IBM-NetFinity-Text-Alert-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-NetFinity-Text-Alert-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:37 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_NetFinity_ObjectIdentity = ObjectIdentity
netFinity = _NetFinity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71)
)
_TrapDesc1_Type = OctetString
_TrapDesc1_Object = MibScalar
trapDesc1 = _TrapDesc1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 1),
    _TrapDesc1_Type()
)
trapDesc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDesc1.setStatus("mandatory")
_TrapSystemName_Type = OctetString
_TrapSystemName_Object = MibScalar
trapSystemName = _TrapSystemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 2),
    _TrapSystemName_Type()
)
trapSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSystemName.setStatus("mandatory")
_TrapTime_Type = OctetString
_TrapTime_Object = MibScalar
trapTime = _TrapTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 3),
    _TrapTime_Type()
)
trapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTime.setStatus("mandatory")
_TrapDate_Type = OctetString
_TrapDate_Object = MibScalar
trapDate = _TrapDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 4),
    _TrapDate_Type()
)
trapDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDate.setStatus("mandatory")
_TrapSeverity_Type = Integer32
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 5),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("mandatory")
_TrapType_Type = OctetString
_TrapType_Object = MibScalar
trapType = _TrapType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 6),
    _TrapType_Type()
)
trapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapType.setStatus("mandatory")
_TrapApplicationID_Type = OctetString
_TrapApplicationID_Object = MibScalar
trapApplicationID = _TrapApplicationID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 7),
    _TrapApplicationID_Type()
)
trapApplicationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapApplicationID.setStatus("mandatory")
_TrapAppType_Type = Integer32
_TrapAppType_Object = MibScalar
trapAppType = _TrapAppType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 8),
    _TrapAppType_Type()
)
trapAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAppType.setStatus("mandatory")
_TrapRecFrom_Type = OctetString
_TrapRecFrom_Object = MibScalar
trapRecFrom = _TrapRecFrom_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 9),
    _TrapRecFrom_Type()
)
trapRecFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRecFrom.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapText1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 0, 1)
)
trapText1.setObjects(
      *(("IBM-NetFinity-Text-Alert-MIB", "trapDesc1"),
        ("IBM-NetFinity-Text-Alert-MIB", "trapSystemName"),
        ("IBM-NetFinity-Text-Alert-MIB", "trapTime"),
        ("IBM-NetFinity-Text-Alert-MIB", "trapDate"),
        ("IBM-NetFinity-Text-Alert-MIB", "trapSeverity"),
        ("IBM-NetFinity-Text-Alert-MIB", "trapType"),
        ("IBM-NetFinity-Text-Alert-MIB", "trapApplicationID"),
        ("IBM-NetFinity-Text-Alert-MIB", "trapAppType"),
        ("IBM-NetFinity-Text-Alert-MIB", "trapRecFrom"))
)
if mibBuilder.loadTexts:
    trapText1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-NetFinity-Text-Alert-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "netFinity": netFinity,
       "trapText1": trapText1,
       "trapDesc1": trapDesc1,
       "trapSystemName": trapSystemName,
       "trapTime": trapTime,
       "trapDate": trapDate,
       "trapSeverity": trapSeverity,
       "trapType": trapType,
       "trapApplicationID": trapApplicationID,
       "trapAppType": trapAppType,
       "trapRecFrom": trapRecFrom}
)
