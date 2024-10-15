# SNMP MIB module (HDSL730D1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL730D1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:16 2024
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

(hdsl730D1,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl730D1")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hdsl730D1System_ObjectIdentity = ObjectIdentity
hdsl730D1System = _Hdsl730D1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 1)
)
_Hdsl730D1Version_ObjectIdentity = ObjectIdentity
hdsl730D1Version = _Hdsl730D1Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 1, 1)
)


class _Gdc730D1SystemMIBversion_Type(DisplayString):
    """Custom type gdc730D1SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc730D1SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc730D1SystemMIBversion_Object = MibScalar
gdc730D1SystemMIBversion = _Gdc730D1SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 1, 1, 1),
    _Gdc730D1SystemMIBversion_Type()
)
gdc730D1SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc730D1SystemMIBversion.setStatus("mandatory")
_Hdsl730D1Alarms_ObjectIdentity = ObjectIdentity
hdsl730D1Alarms = _Hdsl730D1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2)
)
_Hdsl730D1NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl730D1NoResponseAlm = _Hdsl730D1NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 1)
)
_Hdsl730D1DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl730D1DiagRxErrAlm = _Hdsl730D1DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 2)
)
_Hdsl730D1PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl730D1PowerUpAlm = _Hdsl730D1PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 3)
)
_Hdsl730D1UnitFailure_ObjectIdentity = ObjectIdentity
hdsl730D1UnitFailure = _Hdsl730D1UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 4)
)
_Hdsl730D1ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl730D1ChecksumCorrupt = _Hdsl730D1ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 5)
)
_Hdsl730D1LossofSignal_ObjectIdentity = ObjectIdentity
hdsl730D1LossofSignal = _Hdsl730D1LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 6)
)
_Hdsl730D1UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl730D1UnavailableSec = _Hdsl730D1UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 7)
)
_Hdsl730D1ErrorSec_ObjectIdentity = ObjectIdentity
hdsl730D1ErrorSec = _Hdsl730D1ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 8)
)
_Hdsl730D1LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl730D1LossofSyncWord = _Hdsl730D1LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 9)
)
_Hdsl730D1MajorBER_ObjectIdentity = ObjectIdentity
hdsl730D1MajorBER = _Hdsl730D1MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 10)
)
_Hdsl730D1MinorBER_ObjectIdentity = ObjectIdentity
hdsl730D1MinorBER = _Hdsl730D1MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL730D1-MIB",
    **{"hdsl730D1System": hdsl730D1System,
       "hdsl730D1Version": hdsl730D1Version,
       "gdc730D1SystemMIBversion": gdc730D1SystemMIBversion,
       "hdsl730D1Alarms": hdsl730D1Alarms,
       "hdsl730D1NoResponseAlm": hdsl730D1NoResponseAlm,
       "hdsl730D1DiagRxErrAlm": hdsl730D1DiagRxErrAlm,
       "hdsl730D1PowerUpAlm": hdsl730D1PowerUpAlm,
       "hdsl730D1UnitFailure": hdsl730D1UnitFailure,
       "hdsl730D1ChecksumCorrupt": hdsl730D1ChecksumCorrupt,
       "hdsl730D1LossofSignal": hdsl730D1LossofSignal,
       "hdsl730D1UnavailableSec": hdsl730D1UnavailableSec,
       "hdsl730D1ErrorSec": hdsl730D1ErrorSec,
       "hdsl730D1LossofSyncWord": hdsl730D1LossofSyncWord,
       "hdsl730D1MajorBER": hdsl730D1MajorBER,
       "hdsl730D1MinorBER": hdsl730D1MinorBER}
)
