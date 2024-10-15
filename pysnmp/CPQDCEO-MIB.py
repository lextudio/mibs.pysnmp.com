# SNMP MIB module (CPQDCEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQDCEO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:18 2024
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysDescr,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysDescr",
    "sysLocation",
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

_CpqDceo_ObjectIdentity = ObjectIdentity
cpqDceo = _CpqDceo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 173)
)
_EnvironmentalDevice_ObjectIdentity = ObjectIdentity
environmentalDevice = _EnvironmentalDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 173, 1)
)
_DceoTrapInfo_ObjectIdentity = ObjectIdentity
dceoTrapInfo = _DceoTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 173, 1, 1)
)


class _TrapDescription_Type(DisplayString):
    """Custom type trapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDescription_Type.__name__ = "DisplayString"
_TrapDescription_Object = MibScalar
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 173, 1, 1, 1),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("mandatory")


class _TrapDeviceDetails_Type(DisplayString):
    """Custom type trapDeviceDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDeviceDetails_Type.__name__ = "DisplayString"
_TrapDeviceDetails_Object = MibScalar
trapDeviceDetails = _TrapDeviceDetails_Object(
    (1, 3, 6, 1, 4, 1, 232, 173, 1, 1, 2),
    _TrapDeviceDetails_Type()
)
trapDeviceDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDeviceDetails.setStatus("mandatory")


class _TrapDeviceMgmtUrl_Type(DisplayString):
    """Custom type trapDeviceMgmtUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDeviceMgmtUrl_Type.__name__ = "DisplayString"
_TrapDeviceMgmtUrl_Object = MibScalar
trapDeviceMgmtUrl = _TrapDeviceMgmtUrl_Object(
    (1, 3, 6, 1, 4, 1, 232, 173, 1, 1, 3),
    _TrapDeviceMgmtUrl_Type()
)
trapDeviceMgmtUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDeviceMgmtUrl.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapDceoHighPriority = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 173, 0, 1)
)
trapDceoHighPriority.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQDCEO-MIB", "trapDescription"),
        ("CPQDCEO-MIB", "trapDeviceDetails"),
        ("CPQDCEO-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapDceoHighPriority.setStatus(
        ""
    )

trapDceoMediumPriority = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 173, 0, 2)
)
trapDceoMediumPriority.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQDCEO-MIB", "trapDescription"),
        ("CPQDCEO-MIB", "trapDeviceDetails"),
        ("CPQDCEO-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapDceoMediumPriority.setStatus(
        ""
    )

trapDceoLowPriority = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 173, 0, 3)
)
trapDceoLowPriority.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQDCEO-MIB", "trapDescription"),
        ("CPQDCEO-MIB", "trapDeviceDetails"),
        ("CPQDCEO-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapDceoLowPriority.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQDCEO-MIB",
    **{"cpqDceo": cpqDceo,
       "trapDceoHighPriority": trapDceoHighPriority,
       "trapDceoMediumPriority": trapDceoMediumPriority,
       "trapDceoLowPriority": trapDceoLowPriority,
       "environmentalDevice": environmentalDevice,
       "dceoTrapInfo": dceoTrapInfo,
       "trapDescription": trapDescription,
       "trapDeviceDetails": trapDeviceDetails,
       "trapDeviceMgmtUrl": trapDeviceMgmtUrl}
)
