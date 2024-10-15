# SNMP MIB module (HDSLGT1030-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSLGT1030-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:20 2024
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

(hdslGT1030,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdslGT1030")

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

_HdslGT1030System_ObjectIdentity = ObjectIdentity
hdslGT1030System = _HdslGT1030System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 1)
)
_HdslGT1030Version_ObjectIdentity = ObjectIdentity
hdslGT1030Version = _HdslGT1030Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 1, 1)
)


class _GdcGT1030SystemMIBversion_Type(DisplayString):
    """Custom type gdcGT1030SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_GdcGT1030SystemMIBversion_Type.__name__ = "DisplayString"
_GdcGT1030SystemMIBversion_Object = MibScalar
gdcGT1030SystemMIBversion = _GdcGT1030SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 1, 1, 1),
    _GdcGT1030SystemMIBversion_Type()
)
gdcGT1030SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcGT1030SystemMIBversion.setStatus("mandatory")
_HdslGT1030Alarms_ObjectIdentity = ObjectIdentity
hdslGT1030Alarms = _HdslGT1030Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2)
)
_HdslGT1030NoResponseAlm_ObjectIdentity = ObjectIdentity
hdslGT1030NoResponseAlm = _HdslGT1030NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 1)
)
_HdslGT1030DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdslGT1030DiagRxErrAlm = _HdslGT1030DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 2)
)
_HdslGT1030PowerUpAlm_ObjectIdentity = ObjectIdentity
hdslGT1030PowerUpAlm = _HdslGT1030PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 3)
)
_HdslGT1030UnitFailure_ObjectIdentity = ObjectIdentity
hdslGT1030UnitFailure = _HdslGT1030UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 4)
)
_HdslGT1030ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdslGT1030ChecksumCorrupt = _HdslGT1030ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 5)
)
_HdslGT1030LossofSignal_ObjectIdentity = ObjectIdentity
hdslGT1030LossofSignal = _HdslGT1030LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 6)
)
_HdslGT1030UnavailableSec_ObjectIdentity = ObjectIdentity
hdslGT1030UnavailableSec = _HdslGT1030UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 7)
)
_HdslGT1030ErrorSec_ObjectIdentity = ObjectIdentity
hdslGT1030ErrorSec = _HdslGT1030ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 8)
)
_HdslGT1030LossofSyncWord_ObjectIdentity = ObjectIdentity
hdslGT1030LossofSyncWord = _HdslGT1030LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 9)
)
_HdslGT1030MajorBER_ObjectIdentity = ObjectIdentity
hdslGT1030MajorBER = _HdslGT1030MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 10)
)
_HdslGT1030MinorBER_ObjectIdentity = ObjectIdentity
hdslGT1030MinorBER = _HdslGT1030MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSLGT1030-MIB",
    **{"hdslGT1030System": hdslGT1030System,
       "hdslGT1030Version": hdslGT1030Version,
       "gdcGT1030SystemMIBversion": gdcGT1030SystemMIBversion,
       "hdslGT1030Alarms": hdslGT1030Alarms,
       "hdslGT1030NoResponseAlm": hdslGT1030NoResponseAlm,
       "hdslGT1030DiagRxErrAlm": hdslGT1030DiagRxErrAlm,
       "hdslGT1030PowerUpAlm": hdslGT1030PowerUpAlm,
       "hdslGT1030UnitFailure": hdslGT1030UnitFailure,
       "hdslGT1030ChecksumCorrupt": hdslGT1030ChecksumCorrupt,
       "hdslGT1030LossofSignal": hdslGT1030LossofSignal,
       "hdslGT1030UnavailableSec": hdslGT1030UnavailableSec,
       "hdslGT1030ErrorSec": hdslGT1030ErrorSec,
       "hdslGT1030LossofSyncWord": hdslGT1030LossofSyncWord,
       "hdslGT1030MajorBER": hdslGT1030MajorBER,
       "hdslGT1030MinorBER": hdslGT1030MinorBER}
)
