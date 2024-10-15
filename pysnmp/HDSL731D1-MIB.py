# SNMP MIB module (HDSL731D1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL731D1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:17 2024
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

(hdsl731D1,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl731D1")

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

_Hdsl731D1System_ObjectIdentity = ObjectIdentity
hdsl731D1System = _Hdsl731D1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 1)
)
_Hdsl731D1Version_ObjectIdentity = ObjectIdentity
hdsl731D1Version = _Hdsl731D1Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 1, 1)
)


class _Gdc731D1SystemMIBversion_Type(DisplayString):
    """Custom type gdc731D1SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc731D1SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc731D1SystemMIBversion_Object = MibScalar
gdc731D1SystemMIBversion = _Gdc731D1SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 1, 1, 1),
    _Gdc731D1SystemMIBversion_Type()
)
gdc731D1SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc731D1SystemMIBversion.setStatus("mandatory")
_Hdsl731D1Alarms_ObjectIdentity = ObjectIdentity
hdsl731D1Alarms = _Hdsl731D1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2)
)
_Hdsl731D1NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl731D1NoResponseAlm = _Hdsl731D1NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 1)
)
_Hdsl731D1DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl731D1DiagRxErrAlm = _Hdsl731D1DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 2)
)
_Hdsl731D1PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl731D1PowerUpAlm = _Hdsl731D1PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 3)
)
_Hdsl731D1UnitFailure_ObjectIdentity = ObjectIdentity
hdsl731D1UnitFailure = _Hdsl731D1UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 4)
)
_Hdsl731D1ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl731D1ChecksumCorrupt = _Hdsl731D1ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 5)
)
_Hdsl731D1LossofSignal_ObjectIdentity = ObjectIdentity
hdsl731D1LossofSignal = _Hdsl731D1LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 6)
)
_Hdsl731D1UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl731D1UnavailableSec = _Hdsl731D1UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 7)
)
_Hdsl731D1ErrorSec_ObjectIdentity = ObjectIdentity
hdsl731D1ErrorSec = _Hdsl731D1ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 8)
)
_Hdsl731D1LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl731D1LossofSyncWord = _Hdsl731D1LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 9)
)
_Hdsl731D1MajorBER_ObjectIdentity = ObjectIdentity
hdsl731D1MajorBER = _Hdsl731D1MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 10)
)
_Hdsl731D1MinorBER_ObjectIdentity = ObjectIdentity
hdsl731D1MinorBER = _Hdsl731D1MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL731D1-MIB",
    **{"hdsl731D1System": hdsl731D1System,
       "hdsl731D1Version": hdsl731D1Version,
       "gdc731D1SystemMIBversion": gdc731D1SystemMIBversion,
       "hdsl731D1Alarms": hdsl731D1Alarms,
       "hdsl731D1NoResponseAlm": hdsl731D1NoResponseAlm,
       "hdsl731D1DiagRxErrAlm": hdsl731D1DiagRxErrAlm,
       "hdsl731D1PowerUpAlm": hdsl731D1PowerUpAlm,
       "hdsl731D1UnitFailure": hdsl731D1UnitFailure,
       "hdsl731D1ChecksumCorrupt": hdsl731D1ChecksumCorrupt,
       "hdsl731D1LossofSignal": hdsl731D1LossofSignal,
       "hdsl731D1UnavailableSec": hdsl731D1UnavailableSec,
       "hdsl731D1ErrorSec": hdsl731D1ErrorSec,
       "hdsl731D1LossofSyncWord": hdsl731D1LossofSyncWord,
       "hdsl731D1MajorBER": hdsl731D1MajorBER,
       "hdsl731D1MinorBER": hdsl731D1MinorBER}
)
