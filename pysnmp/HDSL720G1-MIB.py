# SNMP MIB module (HDSL720G1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL720G1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:12 2024
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

(hdsl720G1,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl720G1")

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

_Hdsl720G1System_ObjectIdentity = ObjectIdentity
hdsl720G1System = _Hdsl720G1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 1)
)
_Hdsl720G1Version_ObjectIdentity = ObjectIdentity
hdsl720G1Version = _Hdsl720G1Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 1, 1)
)


class _Gdc720G1SystemMIBversion_Type(DisplayString):
    """Custom type gdc720G1SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc720G1SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc720G1SystemMIBversion_Object = MibScalar
gdc720G1SystemMIBversion = _Gdc720G1SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 1, 1, 1),
    _Gdc720G1SystemMIBversion_Type()
)
gdc720G1SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc720G1SystemMIBversion.setStatus("mandatory")
_Hdsl720G1Alarms_ObjectIdentity = ObjectIdentity
hdsl720G1Alarms = _Hdsl720G1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2)
)
_Hdsl720G1NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl720G1NoResponseAlm = _Hdsl720G1NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 1)
)
_Hdsl720G1DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl720G1DiagRxErrAlm = _Hdsl720G1DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 2)
)
_Hdsl720G1PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl720G1PowerUpAlm = _Hdsl720G1PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 3)
)
_Hdsl720G1UnitFailure_ObjectIdentity = ObjectIdentity
hdsl720G1UnitFailure = _Hdsl720G1UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 4)
)
_Hdsl720G1ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl720G1ChecksumCorrupt = _Hdsl720G1ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 5)
)
_Hdsl720G1LossofSignal_ObjectIdentity = ObjectIdentity
hdsl720G1LossofSignal = _Hdsl720G1LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 6)
)
_Hdsl720G1UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl720G1UnavailableSec = _Hdsl720G1UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 7)
)
_Hdsl720G1ErrorSec_ObjectIdentity = ObjectIdentity
hdsl720G1ErrorSec = _Hdsl720G1ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 8)
)
_Hdsl720G1LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl720G1LossofSyncWord = _Hdsl720G1LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 9)
)
_Hdsl720G1LossofFrameAlign_ObjectIdentity = ObjectIdentity
hdsl720G1LossofFrameAlign = _Hdsl720G1LossofFrameAlign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 10)
)
_Hdsl720G1AllOnes_ObjectIdentity = ObjectIdentity
hdsl720G1AllOnes = _Hdsl720G1AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 11)
)
_Hdsl720G1RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdsl720G1RemoteLossofSig = _Hdsl720G1RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 12)
)
_Hdsl720G1RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdsl720G1RemoteAlarmInd = _Hdsl720G1RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 13)
)
_Hdsl720G1MajorBER_ObjectIdentity = ObjectIdentity
hdsl720G1MajorBER = _Hdsl720G1MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 14)
)
_Hdsl720G1MinorBER_ObjectIdentity = ObjectIdentity
hdsl720G1MinorBER = _Hdsl720G1MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL720G1-MIB",
    **{"hdsl720G1System": hdsl720G1System,
       "hdsl720G1Version": hdsl720G1Version,
       "gdc720G1SystemMIBversion": gdc720G1SystemMIBversion,
       "hdsl720G1Alarms": hdsl720G1Alarms,
       "hdsl720G1NoResponseAlm": hdsl720G1NoResponseAlm,
       "hdsl720G1DiagRxErrAlm": hdsl720G1DiagRxErrAlm,
       "hdsl720G1PowerUpAlm": hdsl720G1PowerUpAlm,
       "hdsl720G1UnitFailure": hdsl720G1UnitFailure,
       "hdsl720G1ChecksumCorrupt": hdsl720G1ChecksumCorrupt,
       "hdsl720G1LossofSignal": hdsl720G1LossofSignal,
       "hdsl720G1UnavailableSec": hdsl720G1UnavailableSec,
       "hdsl720G1ErrorSec": hdsl720G1ErrorSec,
       "hdsl720G1LossofSyncWord": hdsl720G1LossofSyncWord,
       "hdsl720G1LossofFrameAlign": hdsl720G1LossofFrameAlign,
       "hdsl720G1AllOnes": hdsl720G1AllOnes,
       "hdsl720G1RemoteLossofSig": hdsl720G1RemoteLossofSig,
       "hdsl720G1RemoteAlarmInd": hdsl720G1RemoteAlarmInd,
       "hdsl720G1MajorBER": hdsl720G1MajorBER,
       "hdsl720G1MinorBER": hdsl720G1MinorBER}
)
