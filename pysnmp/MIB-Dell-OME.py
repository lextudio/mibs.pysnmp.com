# SNMP MIB module (MIB-Dell-OME) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIB-Dell-OME
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:27 2024
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



class DellString(DisplayString):
    """Custom type DellString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )





class DellString1(DisplayString):
    """Custom type DellString1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_EnterpriseSW_ObjectIdentity = ObjectIdentity
enterpriseSW = _EnterpriseSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000)
)
_SysMgmtBranch_ObjectIdentity = ObjectIdentity
sysMgmtBranch = _SysMgmtBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000)
)
_OmEssentialsMIB_ObjectIdentity = ObjectIdentity
omEssentialsMIB = _OmEssentialsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100)
)
_OmEssentialsTrap_ObjectIdentity = ObjectIdentity
omEssentialsTrap = _OmEssentialsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1)
)
_OmeAlertMessage_Type = DellString
_OmeAlertMessage_Object = MibScalar
omeAlertMessage = _OmeAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 1),
    _OmeAlertMessage_Type()
)
omeAlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omeAlertMessage.setStatus("mandatory")
_OmeAlertDevice_Type = DellString
_OmeAlertDevice_Object = MibScalar
omeAlertDevice = _OmeAlertDevice_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 2),
    _OmeAlertDevice_Type()
)
omeAlertDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omeAlertDevice.setStatus("mandatory")
_OmeAlertSeverity_Type = DellString1
_OmeAlertSeverity_Object = MibScalar
omeAlertSeverity = _OmeAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 3),
    _OmeAlertSeverity_Type()
)
omeAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omeAlertSeverity.setStatus("mandatory")

# Managed Objects groups


# Notification objects

omeTestAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 0, 1)
)
omeTestAlert.setObjects(
      *(("MIB-Dell-OME", "omeAlertMessage"),
        ("MIB-Dell-OME", "omeAlertDevice"),
        ("MIB-Dell-OME", "omeAlertSeverity"))
)
if mibBuilder.loadTexts:
    omeTestAlert.setStatus(
        ""
    )

omeAlertSystemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 0, 1000)
)
omeAlertSystemUp.setObjects(
      *(("MIB-Dell-OME", "omeAlertMessage"),
        ("MIB-Dell-OME", "omeAlertDevice"))
)
if mibBuilder.loadTexts:
    omeAlertSystemUp.setStatus(
        ""
    )

omeAlertSystemDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 0, 1001)
)
omeAlertSystemDown.setObjects(
      *(("MIB-Dell-OME", "omeAlertMessage"),
        ("MIB-Dell-OME", "omeAlertDevice"))
)
if mibBuilder.loadTexts:
    omeAlertSystemDown.setStatus(
        ""
    )

omeAlertForwardedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 0, 2000)
)
omeAlertForwardedAlert.setObjects(
      *(("MIB-Dell-OME", "omeAlertMessage"),
        ("MIB-Dell-OME", "omeAlertDevice"),
        ("MIB-Dell-OME", "omeAlertSeverity"))
)
if mibBuilder.loadTexts:
    omeAlertForwardedAlert.setStatus(
        ""
    )

omeAlertUnknownStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 0, 3001)
)
omeAlertUnknownStatus.setObjects(
    ("MIB-Dell-OME", "omeAlertDevice")
)
if mibBuilder.loadTexts:
    omeAlertUnknownStatus.setStatus(
        ""
    )

omeAlertNormalStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 0, 3002)
)
omeAlertNormalStatus.setObjects(
    ("MIB-Dell-OME", "omeAlertDevice")
)
if mibBuilder.loadTexts:
    omeAlertNormalStatus.setStatus(
        ""
    )

omeAlertWarningStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 0, 3003)
)
omeAlertWarningStatus.setObjects(
    ("MIB-Dell-OME", "omeAlertDevice")
)
if mibBuilder.loadTexts:
    omeAlertWarningStatus.setStatus(
        ""
    )

omeAlertCriticalStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 0, 3004)
)
omeAlertCriticalStatus.setObjects(
    ("MIB-Dell-OME", "omeAlertDevice")
)
if mibBuilder.loadTexts:
    omeAlertCriticalStatus.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIB-Dell-OME",
    **{"DellString": DellString,
       "DellString1": DellString1,
       "dell": dell,
       "enterpriseSW": enterpriseSW,
       "sysMgmtBranch": sysMgmtBranch,
       "omEssentialsMIB": omEssentialsMIB,
       "omEssentialsTrap": omEssentialsTrap,
       "omeTestAlert": omeTestAlert,
       "omeAlertSystemUp": omeAlertSystemUp,
       "omeAlertSystemDown": omeAlertSystemDown,
       "omeAlertForwardedAlert": omeAlertForwardedAlert,
       "omeAlertUnknownStatus": omeAlertUnknownStatus,
       "omeAlertNormalStatus": omeAlertNormalStatus,
       "omeAlertWarningStatus": omeAlertWarningStatus,
       "omeAlertCriticalStatus": omeAlertCriticalStatus,
       "omeAlertMessage": omeAlertMessage,
       "omeAlertDevice": omeAlertDevice,
       "omeAlertSeverity": omeAlertSeverity}
)
