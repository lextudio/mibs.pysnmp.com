# SNMP MIB module (HDSL721T1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL721T1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:14 2024
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

(hdsl721T1,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl721T1")

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

_Hdsl721T1System_ObjectIdentity = ObjectIdentity
hdsl721T1System = _Hdsl721T1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 1)
)
_Hdsl721T1Version_ObjectIdentity = ObjectIdentity
hdsl721T1Version = _Hdsl721T1Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 1, 1)
)


class _Gdc721T1SystemMIBversion_Type(DisplayString):
    """Custom type gdc721T1SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc721T1SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc721T1SystemMIBversion_Object = MibScalar
gdc721T1SystemMIBversion = _Gdc721T1SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 1, 1, 1),
    _Gdc721T1SystemMIBversion_Type()
)
gdc721T1SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc721T1SystemMIBversion.setStatus("mandatory")
_Hdsl721T1Alarms_ObjectIdentity = ObjectIdentity
hdsl721T1Alarms = _Hdsl721T1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2)
)
_Hdsl721T1NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl721T1NoResponseAlm = _Hdsl721T1NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 1)
)
_Hdsl721T1DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl721T1DiagRxErrAlm = _Hdsl721T1DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 2)
)
_Hdsl721T1PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl721T1PowerUpAlm = _Hdsl721T1PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 3)
)
_Hdsl721T1UnitFailure_ObjectIdentity = ObjectIdentity
hdsl721T1UnitFailure = _Hdsl721T1UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 4)
)
_Hdsl721T1ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl721T1ChecksumCorrupt = _Hdsl721T1ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 5)
)
_Hdsl721T1LossofSignal_ObjectIdentity = ObjectIdentity
hdsl721T1LossofSignal = _Hdsl721T1LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 6)
)
_Hdsl721T1UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl721T1UnavailableSec = _Hdsl721T1UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 7)
)
_Hdsl721T1ErrorSec_ObjectIdentity = ObjectIdentity
hdsl721T1ErrorSec = _Hdsl721T1ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 8)
)
_Hdsl721T1LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl721T1LossofSyncWord = _Hdsl721T1LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 9)
)
_Hdsl721T1OutofFrame_ObjectIdentity = ObjectIdentity
hdsl721T1OutofFrame = _Hdsl721T1OutofFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 10)
)
_Hdsl721T1AllOnes_ObjectIdentity = ObjectIdentity
hdsl721T1AllOnes = _Hdsl721T1AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 11)
)
_Hdsl721T1RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdsl721T1RemoteLossofSig = _Hdsl721T1RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 12)
)
_Hdsl721T1RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdsl721T1RemoteAlarmInd = _Hdsl721T1RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 13)
)
_Hdsl721T1MajorBER_ObjectIdentity = ObjectIdentity
hdsl721T1MajorBER = _Hdsl721T1MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 14)
)
_Hdsl721T1MinorBER_ObjectIdentity = ObjectIdentity
hdsl721T1MinorBER = _Hdsl721T1MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL721T1-MIB",
    **{"hdsl721T1System": hdsl721T1System,
       "hdsl721T1Version": hdsl721T1Version,
       "gdc721T1SystemMIBversion": gdc721T1SystemMIBversion,
       "hdsl721T1Alarms": hdsl721T1Alarms,
       "hdsl721T1NoResponseAlm": hdsl721T1NoResponseAlm,
       "hdsl721T1DiagRxErrAlm": hdsl721T1DiagRxErrAlm,
       "hdsl721T1PowerUpAlm": hdsl721T1PowerUpAlm,
       "hdsl721T1UnitFailure": hdsl721T1UnitFailure,
       "hdsl721T1ChecksumCorrupt": hdsl721T1ChecksumCorrupt,
       "hdsl721T1LossofSignal": hdsl721T1LossofSignal,
       "hdsl721T1UnavailableSec": hdsl721T1UnavailableSec,
       "hdsl721T1ErrorSec": hdsl721T1ErrorSec,
       "hdsl721T1LossofSyncWord": hdsl721T1LossofSyncWord,
       "hdsl721T1OutofFrame": hdsl721T1OutofFrame,
       "hdsl721T1AllOnes": hdsl721T1AllOnes,
       "hdsl721T1RemoteLossofSig": hdsl721T1RemoteLossofSig,
       "hdsl721T1RemoteAlarmInd": hdsl721T1RemoteAlarmInd,
       "hdsl721T1MajorBER": hdsl721T1MajorBER,
       "hdsl721T1MinorBER": hdsl721T1MinorBER}
)
