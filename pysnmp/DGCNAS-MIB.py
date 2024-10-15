# SNMP MIB module (DGCNAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGCNAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:22 2024
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

_DataGeneral_ObjectIdentity = ObjectIdentity
dataGeneral = _DataGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 106)
)
_DgEvent_ObjectIdentity = ObjectIdentity
dgEvent = _DgEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 106, 3)
)
_DgNasEvent_ObjectIdentity = ObjectIdentity
dgNasEvent = _DgNasEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 106, 3, 3)
)
_DgNasEventLog_ObjectIdentity = ObjectIdentity
dgNasEventLog = _DgNasEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 106, 3, 3, 1)
)


class _DgNasEventLogSeverity_Type(Integer32):
    """Custom type dgNasEventLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("debug", 1),
          ("error", 4),
          ("info", 2),
          ("none", 0),
          ("warning", 3))
    )


_DgNasEventLogSeverity_Type.__name__ = "Integer32"
_DgNasEventLogSeverity_Object = MibScalar
dgNasEventLogSeverity = _DgNasEventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 106, 3, 3, 1, 1),
    _DgNasEventLogSeverity_Type()
)
dgNasEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgNasEventLogSeverity.setStatus("mandatory")


class _DgNasEventLogSource_Type(OctetString):
    """Custom type dgNasEventLogSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DgNasEventLogSource_Type.__name__ = "OctetString"
_DgNasEventLogSource_Object = MibScalar
dgNasEventLogSource = _DgNasEventLogSource_Object(
    (1, 3, 6, 1, 4, 1, 106, 3, 3, 1, 2),
    _DgNasEventLogSource_Type()
)
dgNasEventLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgNasEventLogSource.setStatus("mandatory")


class _DgNasEventLogDescription_Type(OctetString):
    """Custom type dgNasEventLogDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DgNasEventLogDescription_Type.__name__ = "OctetString"
_DgNasEventLogDescription_Object = MibScalar
dgNasEventLogDescription = _DgNasEventLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 106, 3, 3, 1, 3),
    _DgNasEventLogDescription_Type()
)
dgNasEventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgNasEventLogDescription.setStatus("mandatory")


class _DgNasEventLogSerialNumber_Type(DisplayString):
    """Custom type dgNasEventLogSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DgNasEventLogSerialNumber_Type.__name__ = "DisplayString"
_DgNasEventLogSerialNumber_Object = MibScalar
dgNasEventLogSerialNumber = _DgNasEventLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 106, 3, 3, 1, 4),
    _DgNasEventLogSerialNumber_Type()
)
dgNasEventLogSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgNasEventLogSerialNumber.setStatus("mandatory")


class _DgNasEventLogSystemType_Type(DisplayString):
    """Custom type dgNasEventLogSystemType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DgNasEventLogSystemType_Type.__name__ = "DisplayString"
_DgNasEventLogSystemType_Object = MibScalar
dgNasEventLogSystemType = _DgNasEventLogSystemType_Object(
    (1, 3, 6, 1, 4, 1, 106, 3, 3, 1, 5),
    _DgNasEventLogSystemType_Type()
)
dgNasEventLogSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgNasEventLogSystemType.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dgTrapNasEventLogNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 106, 0, 4)
)
dgTrapNasEventLogNotification.setObjects(
      *(("DGCNAS-MIB", "dgNasEventLogSeverity"),
        ("DGCNAS-MIB", "dgNasEventLogSource"),
        ("DGCNAS-MIB", "dgNasEventLogDescription"),
        ("DGCNAS-MIB", "dgNasEventLogSerialNumber"),
        ("DGCNAS-MIB", "dgNasEventLogSystemType"))
)
if mibBuilder.loadTexts:
    dgTrapNasEventLogNotification.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGCNAS-MIB",
    **{"dataGeneral": dataGeneral,
       "dgTrapNasEventLogNotification": dgTrapNasEventLogNotification,
       "dgEvent": dgEvent,
       "dgNasEvent": dgNasEvent,
       "dgNasEventLog": dgNasEventLog,
       "dgNasEventLogSeverity": dgNasEventLogSeverity,
       "dgNasEventLogSource": dgNasEventLogSource,
       "dgNasEventLogDescription": dgNasEventLogDescription,
       "dgNasEventLogSerialNumber": dgNasEventLogSerialNumber,
       "dgNasEventLogSystemType": dgNasEventLogSystemType}
)
