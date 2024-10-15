# SNMP MIB module (HDSLGT2020-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSLGT2020-MIB
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

(hdslGT2020,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdslGT2020")

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

_HdslGT2020System_ObjectIdentity = ObjectIdentity
hdslGT2020System = _HdslGT2020System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 1)
)
_HdslGT2020Version_ObjectIdentity = ObjectIdentity
hdslGT2020Version = _HdslGT2020Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 1, 1)
)


class _GdcGT2020SystemMIBversion_Type(DisplayString):
    """Custom type gdcGT2020SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_GdcGT2020SystemMIBversion_Type.__name__ = "DisplayString"
_GdcGT2020SystemMIBversion_Object = MibScalar
gdcGT2020SystemMIBversion = _GdcGT2020SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 1, 1, 1),
    _GdcGT2020SystemMIBversion_Type()
)
gdcGT2020SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcGT2020SystemMIBversion.setStatus("mandatory")
_HdslGT2020Alarms_ObjectIdentity = ObjectIdentity
hdslGT2020Alarms = _HdslGT2020Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2)
)
_HdslGT2020NoResponseAlm_ObjectIdentity = ObjectIdentity
hdslGT2020NoResponseAlm = _HdslGT2020NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 1)
)
_HdslGT2020DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdslGT2020DiagRxErrAlm = _HdslGT2020DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 2)
)
_HdslGT2020PowerUpAlm_ObjectIdentity = ObjectIdentity
hdslGT2020PowerUpAlm = _HdslGT2020PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 3)
)
_HdslGT2020UnitFailure_ObjectIdentity = ObjectIdentity
hdslGT2020UnitFailure = _HdslGT2020UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 4)
)
_HdslGT2020ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdslGT2020ChecksumCorrupt = _HdslGT2020ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 5)
)
_HdslGT2020LossofSignal_ObjectIdentity = ObjectIdentity
hdslGT2020LossofSignal = _HdslGT2020LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 6)
)
_HdslGT2020UnavailableSec_ObjectIdentity = ObjectIdentity
hdslGT2020UnavailableSec = _HdslGT2020UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 7)
)
_HdslGT2020ErrorSec_ObjectIdentity = ObjectIdentity
hdslGT2020ErrorSec = _HdslGT2020ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 8)
)
_HdslGT2020LossofSyncWord_ObjectIdentity = ObjectIdentity
hdslGT2020LossofSyncWord = _HdslGT2020LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 9)
)
_HdslGT2020LossofFrameAlign_ObjectIdentity = ObjectIdentity
hdslGT2020LossofFrameAlign = _HdslGT2020LossofFrameAlign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 10)
)
_HdslGT2020AllOnes_ObjectIdentity = ObjectIdentity
hdslGT2020AllOnes = _HdslGT2020AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 11)
)
_HdslGT2020RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdslGT2020RemoteLossofSig = _HdslGT2020RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 12)
)
_HdslGT2020RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdslGT2020RemoteAlarmInd = _HdslGT2020RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 13)
)
_HdslGT2020MajorBER_ObjectIdentity = ObjectIdentity
hdslGT2020MajorBER = _HdslGT2020MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 14)
)
_HdslGT2020MinorBER_ObjectIdentity = ObjectIdentity
hdslGT2020MinorBER = _HdslGT2020MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSLGT2020-MIB",
    **{"hdslGT2020System": hdslGT2020System,
       "hdslGT2020Version": hdslGT2020Version,
       "gdcGT2020SystemMIBversion": gdcGT2020SystemMIBversion,
       "hdslGT2020Alarms": hdslGT2020Alarms,
       "hdslGT2020NoResponseAlm": hdslGT2020NoResponseAlm,
       "hdslGT2020DiagRxErrAlm": hdslGT2020DiagRxErrAlm,
       "hdslGT2020PowerUpAlm": hdslGT2020PowerUpAlm,
       "hdslGT2020UnitFailure": hdslGT2020UnitFailure,
       "hdslGT2020ChecksumCorrupt": hdslGT2020ChecksumCorrupt,
       "hdslGT2020LossofSignal": hdslGT2020LossofSignal,
       "hdslGT2020UnavailableSec": hdslGT2020UnavailableSec,
       "hdslGT2020ErrorSec": hdslGT2020ErrorSec,
       "hdslGT2020LossofSyncWord": hdslGT2020LossofSyncWord,
       "hdslGT2020LossofFrameAlign": hdslGT2020LossofFrameAlign,
       "hdslGT2020AllOnes": hdslGT2020AllOnes,
       "hdslGT2020RemoteLossofSig": hdslGT2020RemoteLossofSig,
       "hdslGT2020RemoteAlarmInd": hdslGT2020RemoteAlarmInd,
       "hdslGT2020MajorBER": hdslGT2020MajorBER,
       "hdslGT2020MinorBER": hdslGT2020MinorBER}
)
