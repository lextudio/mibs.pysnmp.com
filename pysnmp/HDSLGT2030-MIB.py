# SNMP MIB module (HDSLGT2030-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSLGT2030-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:21 2024
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

(hdslGT2030,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdslGT2030")

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

_HdslGT2030System_ObjectIdentity = ObjectIdentity
hdslGT2030System = _HdslGT2030System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 1)
)
_HdslGT2030Version_ObjectIdentity = ObjectIdentity
hdslGT2030Version = _HdslGT2030Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 1, 1)
)


class _GdcGT2030SystemMIBversion_Type(DisplayString):
    """Custom type gdcGT2030SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_GdcGT2030SystemMIBversion_Type.__name__ = "DisplayString"
_GdcGT2030SystemMIBversion_Object = MibScalar
gdcGT2030SystemMIBversion = _GdcGT2030SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 1, 1, 1),
    _GdcGT2030SystemMIBversion_Type()
)
gdcGT2030SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcGT2030SystemMIBversion.setStatus("mandatory")
_HdslGT2030Alarms_ObjectIdentity = ObjectIdentity
hdslGT2030Alarms = _HdslGT2030Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2)
)
_HdslGT2030NoResponseAlm_ObjectIdentity = ObjectIdentity
hdslGT2030NoResponseAlm = _HdslGT2030NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 1)
)
_HdslGT2030DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdslGT2030DiagRxErrAlm = _HdslGT2030DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 2)
)
_HdslGT2030PowerUpAlm_ObjectIdentity = ObjectIdentity
hdslGT2030PowerUpAlm = _HdslGT2030PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 3)
)
_HdslGT2030UnitFailure_ObjectIdentity = ObjectIdentity
hdslGT2030UnitFailure = _HdslGT2030UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 4)
)
_HdslGT2030ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdslGT2030ChecksumCorrupt = _HdslGT2030ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 5)
)
_HdslGT2030LossofSignal_ObjectIdentity = ObjectIdentity
hdslGT2030LossofSignal = _HdslGT2030LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 6)
)
_HdslGT2030UnavailableSec_ObjectIdentity = ObjectIdentity
hdslGT2030UnavailableSec = _HdslGT2030UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 7)
)
_HdslGT2030ErrorSec_ObjectIdentity = ObjectIdentity
hdslGT2030ErrorSec = _HdslGT2030ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 8)
)
_HdslGT2030LossofSyncWord_ObjectIdentity = ObjectIdentity
hdslGT2030LossofSyncWord = _HdslGT2030LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 9)
)
_HdslGT2030MajorBER_ObjectIdentity = ObjectIdentity
hdslGT2030MajorBER = _HdslGT2030MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 10)
)
_HdslGT2030MinorBER_ObjectIdentity = ObjectIdentity
hdslGT2030MinorBER = _HdslGT2030MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSLGT2030-MIB",
    **{"hdslGT2030System": hdslGT2030System,
       "hdslGT2030Version": hdslGT2030Version,
       "gdcGT2030SystemMIBversion": gdcGT2030SystemMIBversion,
       "hdslGT2030Alarms": hdslGT2030Alarms,
       "hdslGT2030NoResponseAlm": hdslGT2030NoResponseAlm,
       "hdslGT2030DiagRxErrAlm": hdslGT2030DiagRxErrAlm,
       "hdslGT2030PowerUpAlm": hdslGT2030PowerUpAlm,
       "hdslGT2030UnitFailure": hdslGT2030UnitFailure,
       "hdslGT2030ChecksumCorrupt": hdslGT2030ChecksumCorrupt,
       "hdslGT2030LossofSignal": hdslGT2030LossofSignal,
       "hdslGT2030UnavailableSec": hdslGT2030UnavailableSec,
       "hdslGT2030ErrorSec": hdslGT2030ErrorSec,
       "hdslGT2030LossofSyncWord": hdslGT2030LossofSyncWord,
       "hdslGT2030MajorBER": hdslGT2030MajorBER,
       "hdslGT2030MinorBER": hdslGT2030MinorBER}
)
