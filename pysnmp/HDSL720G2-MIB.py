# SNMP MIB module (HDSL720G2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL720G2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:13 2024
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

(hdsl720G2,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl720G2")

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

_Hdsl720G2System_ObjectIdentity = ObjectIdentity
hdsl720G2System = _Hdsl720G2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 1)
)
_Hdsl720G2Version_ObjectIdentity = ObjectIdentity
hdsl720G2Version = _Hdsl720G2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 1, 1)
)


class _Gdc720G2SystemMIBversion_Type(DisplayString):
    """Custom type gdc720G2SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc720G2SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc720G2SystemMIBversion_Object = MibScalar
gdc720G2SystemMIBversion = _Gdc720G2SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 1, 1, 1),
    _Gdc720G2SystemMIBversion_Type()
)
gdc720G2SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc720G2SystemMIBversion.setStatus("mandatory")
_Hdsl720G2Alarms_ObjectIdentity = ObjectIdentity
hdsl720G2Alarms = _Hdsl720G2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2)
)
_Hdsl720G2NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl720G2NoResponseAlm = _Hdsl720G2NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 1)
)
_Hdsl720G2DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl720G2DiagRxErrAlm = _Hdsl720G2DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 2)
)
_Hdsl720G2PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl720G2PowerUpAlm = _Hdsl720G2PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 3)
)
_Hdsl720G2UnitFailure_ObjectIdentity = ObjectIdentity
hdsl720G2UnitFailure = _Hdsl720G2UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 4)
)
_Hdsl720G2ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl720G2ChecksumCorrupt = _Hdsl720G2ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 5)
)
_Hdsl720G2LossofSignal_ObjectIdentity = ObjectIdentity
hdsl720G2LossofSignal = _Hdsl720G2LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 6)
)
_Hdsl720G2UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl720G2UnavailableSec = _Hdsl720G2UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 7)
)
_Hdsl720G2ErrorSec_ObjectIdentity = ObjectIdentity
hdsl720G2ErrorSec = _Hdsl720G2ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 8)
)
_Hdsl720G2LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl720G2LossofSyncWord = _Hdsl720G2LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 9)
)
_Hdsl720G2LossofFrameAlign_ObjectIdentity = ObjectIdentity
hdsl720G2LossofFrameAlign = _Hdsl720G2LossofFrameAlign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 10)
)
_Hdsl720G2AllOnes_ObjectIdentity = ObjectIdentity
hdsl720G2AllOnes = _Hdsl720G2AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 11)
)
_Hdsl720G2RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdsl720G2RemoteLossofSig = _Hdsl720G2RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 12)
)
_Hdsl720G2RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdsl720G2RemoteAlarmInd = _Hdsl720G2RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 13)
)
_Hdsl720G2MajorBER_ObjectIdentity = ObjectIdentity
hdsl720G2MajorBER = _Hdsl720G2MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 14)
)
_Hdsl720G2MinorBER_ObjectIdentity = ObjectIdentity
hdsl720G2MinorBER = _Hdsl720G2MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL720G2-MIB",
    **{"hdsl720G2System": hdsl720G2System,
       "hdsl720G2Version": hdsl720G2Version,
       "gdc720G2SystemMIBversion": gdc720G2SystemMIBversion,
       "hdsl720G2Alarms": hdsl720G2Alarms,
       "hdsl720G2NoResponseAlm": hdsl720G2NoResponseAlm,
       "hdsl720G2DiagRxErrAlm": hdsl720G2DiagRxErrAlm,
       "hdsl720G2PowerUpAlm": hdsl720G2PowerUpAlm,
       "hdsl720G2UnitFailure": hdsl720G2UnitFailure,
       "hdsl720G2ChecksumCorrupt": hdsl720G2ChecksumCorrupt,
       "hdsl720G2LossofSignal": hdsl720G2LossofSignal,
       "hdsl720G2UnavailableSec": hdsl720G2UnavailableSec,
       "hdsl720G2ErrorSec": hdsl720G2ErrorSec,
       "hdsl720G2LossofSyncWord": hdsl720G2LossofSyncWord,
       "hdsl720G2LossofFrameAlign": hdsl720G2LossofFrameAlign,
       "hdsl720G2AllOnes": hdsl720G2AllOnes,
       "hdsl720G2RemoteLossofSig": hdsl720G2RemoteLossofSig,
       "hdsl720G2RemoteAlarmInd": hdsl720G2RemoteAlarmInd,
       "hdsl720G2MajorBER": hdsl720G2MajorBER,
       "hdsl720G2MinorBER": hdsl720G2MinorBER}
)
