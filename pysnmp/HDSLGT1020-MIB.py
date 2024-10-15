# SNMP MIB module (HDSLGT1020-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSLGT1020-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:19 2024
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

(hdslGT1020,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdslGT1020")

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

_HdslGT1020System_ObjectIdentity = ObjectIdentity
hdslGT1020System = _HdslGT1020System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 1)
)
_HdslGT1020Version_ObjectIdentity = ObjectIdentity
hdslGT1020Version = _HdslGT1020Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 1, 1)
)


class _GdcGT1020SystemMIBversion_Type(DisplayString):
    """Custom type gdcGT1020SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_GdcGT1020SystemMIBversion_Type.__name__ = "DisplayString"
_GdcGT1020SystemMIBversion_Object = MibScalar
gdcGT1020SystemMIBversion = _GdcGT1020SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 1, 1, 1),
    _GdcGT1020SystemMIBversion_Type()
)
gdcGT1020SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcGT1020SystemMIBversion.setStatus("mandatory")
_HdslGT1020Alarms_ObjectIdentity = ObjectIdentity
hdslGT1020Alarms = _HdslGT1020Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2)
)
_HdslGT1020NoResponseAlm_ObjectIdentity = ObjectIdentity
hdslGT1020NoResponseAlm = _HdslGT1020NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 1)
)
_HdslGT1020DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdslGT1020DiagRxErrAlm = _HdslGT1020DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 2)
)
_HdslGT1020PowerUpAlm_ObjectIdentity = ObjectIdentity
hdslGT1020PowerUpAlm = _HdslGT1020PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 3)
)
_HdslGT1020UnitFailure_ObjectIdentity = ObjectIdentity
hdslGT1020UnitFailure = _HdslGT1020UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 4)
)
_HdslGT1020ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdslGT1020ChecksumCorrupt = _HdslGT1020ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 5)
)
_HdslGT1020LossofSignal_ObjectIdentity = ObjectIdentity
hdslGT1020LossofSignal = _HdslGT1020LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 6)
)
_HdslGT1020UnavailableSec_ObjectIdentity = ObjectIdentity
hdslGT1020UnavailableSec = _HdslGT1020UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 7)
)
_HdslGT1020ErrorSec_ObjectIdentity = ObjectIdentity
hdslGT1020ErrorSec = _HdslGT1020ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 8)
)
_HdslGT1020LossofSyncWord_ObjectIdentity = ObjectIdentity
hdslGT1020LossofSyncWord = _HdslGT1020LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 9)
)
_HdslGT1020LossofFrameAlign_ObjectIdentity = ObjectIdentity
hdslGT1020LossofFrameAlign = _HdslGT1020LossofFrameAlign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 10)
)
_HdslGT1020AllOnes_ObjectIdentity = ObjectIdentity
hdslGT1020AllOnes = _HdslGT1020AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 11)
)
_HdslGT1020RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdslGT1020RemoteLossofSig = _HdslGT1020RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 12)
)
_HdslGT1020RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdslGT1020RemoteAlarmInd = _HdslGT1020RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 13)
)
_HdslGT1020MajorBER_ObjectIdentity = ObjectIdentity
hdslGT1020MajorBER = _HdslGT1020MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 14)
)
_HdslGT1020MinorBER_ObjectIdentity = ObjectIdentity
hdslGT1020MinorBER = _HdslGT1020MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSLGT1020-MIB",
    **{"hdslGT1020System": hdslGT1020System,
       "hdslGT1020Version": hdslGT1020Version,
       "gdcGT1020SystemMIBversion": gdcGT1020SystemMIBversion,
       "hdslGT1020Alarms": hdslGT1020Alarms,
       "hdslGT1020NoResponseAlm": hdslGT1020NoResponseAlm,
       "hdslGT1020DiagRxErrAlm": hdslGT1020DiagRxErrAlm,
       "hdslGT1020PowerUpAlm": hdslGT1020PowerUpAlm,
       "hdslGT1020UnitFailure": hdslGT1020UnitFailure,
       "hdslGT1020ChecksumCorrupt": hdslGT1020ChecksumCorrupt,
       "hdslGT1020LossofSignal": hdslGT1020LossofSignal,
       "hdslGT1020UnavailableSec": hdslGT1020UnavailableSec,
       "hdslGT1020ErrorSec": hdslGT1020ErrorSec,
       "hdslGT1020LossofSyncWord": hdslGT1020LossofSyncWord,
       "hdslGT1020LossofFrameAlign": hdslGT1020LossofFrameAlign,
       "hdslGT1020AllOnes": hdslGT1020AllOnes,
       "hdslGT1020RemoteLossofSig": hdslGT1020RemoteLossofSig,
       "hdslGT1020RemoteAlarmInd": hdslGT1020RemoteAlarmInd,
       "hdslGT1020MajorBER": hdslGT1020MajorBER,
       "hdslGT1020MinorBER": hdslGT1020MinorBER}
)
