# SNMP MIB module (HDSL700G3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL700G3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:08 2024
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

(hdsl700G3,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl700G3")

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

_Hdsl700G3System_ObjectIdentity = ObjectIdentity
hdsl700G3System = _Hdsl700G3System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 1)
)
_Hdsl700G3Version_ObjectIdentity = ObjectIdentity
hdsl700G3Version = _Hdsl700G3Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 1, 1)
)


class _Gdc700G3SystemMIBversion_Type(DisplayString):
    """Custom type gdc700G3SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc700G3SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc700G3SystemMIBversion_Object = MibScalar
gdc700G3SystemMIBversion = _Gdc700G3SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 1, 1, 1),
    _Gdc700G3SystemMIBversion_Type()
)
gdc700G3SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc700G3SystemMIBversion.setStatus("mandatory")
_Hdsl700G3Alarms_ObjectIdentity = ObjectIdentity
hdsl700G3Alarms = _Hdsl700G3Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2)
)
_Hdsl700G3NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl700G3NoResponseAlm = _Hdsl700G3NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 1)
)
_Hdsl700G3DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl700G3DiagRxErrAlm = _Hdsl700G3DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 2)
)
_Hdsl700G3PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl700G3PowerUpAlm = _Hdsl700G3PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 3)
)
_Hdsl700G3UnitFailure_ObjectIdentity = ObjectIdentity
hdsl700G3UnitFailure = _Hdsl700G3UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 4)
)
_Hdsl700G3ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl700G3ChecksumCorrupt = _Hdsl700G3ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 5)
)
_Hdsl700G3LossofSignal_ObjectIdentity = ObjectIdentity
hdsl700G3LossofSignal = _Hdsl700G3LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 6)
)
_Hdsl700G3UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl700G3UnavailableSec = _Hdsl700G3UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 7)
)
_Hdsl700G3ErrorSec_ObjectIdentity = ObjectIdentity
hdsl700G3ErrorSec = _Hdsl700G3ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 8)
)
_Hdsl700G3LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl700G3LossofSyncWord = _Hdsl700G3LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 9)
)
_Hdsl700G3LossofFrameAlign_ObjectIdentity = ObjectIdentity
hdsl700G3LossofFrameAlign = _Hdsl700G3LossofFrameAlign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 10)
)
_Hdsl700G3AllOnes_ObjectIdentity = ObjectIdentity
hdsl700G3AllOnes = _Hdsl700G3AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 11)
)
_Hdsl700G3RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdsl700G3RemoteLossofSig = _Hdsl700G3RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 12)
)
_Hdsl700G3RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdsl700G3RemoteAlarmInd = _Hdsl700G3RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 13)
)
_Hdsl700G3MajorBER_ObjectIdentity = ObjectIdentity
hdsl700G3MajorBER = _Hdsl700G3MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 14)
)
_Hdsl700G3MinorBER_ObjectIdentity = ObjectIdentity
hdsl700G3MinorBER = _Hdsl700G3MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL700G3-MIB",
    **{"hdsl700G3System": hdsl700G3System,
       "hdsl700G3Version": hdsl700G3Version,
       "gdc700G3SystemMIBversion": gdc700G3SystemMIBversion,
       "hdsl700G3Alarms": hdsl700G3Alarms,
       "hdsl700G3NoResponseAlm": hdsl700G3NoResponseAlm,
       "hdsl700G3DiagRxErrAlm": hdsl700G3DiagRxErrAlm,
       "hdsl700G3PowerUpAlm": hdsl700G3PowerUpAlm,
       "hdsl700G3UnitFailure": hdsl700G3UnitFailure,
       "hdsl700G3ChecksumCorrupt": hdsl700G3ChecksumCorrupt,
       "hdsl700G3LossofSignal": hdsl700G3LossofSignal,
       "hdsl700G3UnavailableSec": hdsl700G3UnavailableSec,
       "hdsl700G3ErrorSec": hdsl700G3ErrorSec,
       "hdsl700G3LossofSyncWord": hdsl700G3LossofSyncWord,
       "hdsl700G3LossofFrameAlign": hdsl700G3LossofFrameAlign,
       "hdsl700G3AllOnes": hdsl700G3AllOnes,
       "hdsl700G3RemoteLossofSig": hdsl700G3RemoteLossofSig,
       "hdsl700G3RemoteAlarmInd": hdsl700G3RemoteAlarmInd,
       "hdsl700G3MajorBER": hdsl700G3MajorBER,
       "hdsl700G3MinorBER": hdsl700G3MinorBER}
)
