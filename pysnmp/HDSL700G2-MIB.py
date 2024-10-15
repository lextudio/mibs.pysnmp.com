# SNMP MIB module (HDSL700G2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL700G2-MIB
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

(hdsl700G2,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl700G2")

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

_Hdsl700G2System_ObjectIdentity = ObjectIdentity
hdsl700G2System = _Hdsl700G2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 1)
)
_Hdsl700G2Version_ObjectIdentity = ObjectIdentity
hdsl700G2Version = _Hdsl700G2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 1, 1)
)


class _Gdc700G2SystemMIBversion_Type(DisplayString):
    """Custom type gdc700G2SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc700G2SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc700G2SystemMIBversion_Object = MibScalar
gdc700G2SystemMIBversion = _Gdc700G2SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 1, 1, 1),
    _Gdc700G2SystemMIBversion_Type()
)
gdc700G2SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc700G2SystemMIBversion.setStatus("mandatory")
_Hdsl700G2Alarms_ObjectIdentity = ObjectIdentity
hdsl700G2Alarms = _Hdsl700G2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2)
)
_Hdsl700G2NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl700G2NoResponseAlm = _Hdsl700G2NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 1)
)
_Hdsl700G2DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl700G2DiagRxErrAlm = _Hdsl700G2DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 2)
)
_Hdsl700G2PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl700G2PowerUpAlm = _Hdsl700G2PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 3)
)
_Hdsl700G2UnitFailure_ObjectIdentity = ObjectIdentity
hdsl700G2UnitFailure = _Hdsl700G2UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 4)
)
_Hdsl700G2ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl700G2ChecksumCorrupt = _Hdsl700G2ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 5)
)
_Hdsl700G2LossofSignal_ObjectIdentity = ObjectIdentity
hdsl700G2LossofSignal = _Hdsl700G2LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 6)
)
_Hdsl700G2UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl700G2UnavailableSec = _Hdsl700G2UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 7)
)
_Hdsl700G2ErrorSec_ObjectIdentity = ObjectIdentity
hdsl700G2ErrorSec = _Hdsl700G2ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 8)
)
_Hdsl700G2LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl700G2LossofSyncWord = _Hdsl700G2LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 9)
)
_Hdsl700G2LossofFrameAlign_ObjectIdentity = ObjectIdentity
hdsl700G2LossofFrameAlign = _Hdsl700G2LossofFrameAlign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 10)
)
_Hdsl700G2AllOnes_ObjectIdentity = ObjectIdentity
hdsl700G2AllOnes = _Hdsl700G2AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 11)
)
_Hdsl700G2RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdsl700G2RemoteLossofSig = _Hdsl700G2RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 12)
)
_Hdsl700G2RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdsl700G2RemoteAlarmInd = _Hdsl700G2RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 13)
)
_Hdsl700G2MajorBER_ObjectIdentity = ObjectIdentity
hdsl700G2MajorBER = _Hdsl700G2MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 14)
)
_Hdsl700G2MinorBER_ObjectIdentity = ObjectIdentity
hdsl700G2MinorBER = _Hdsl700G2MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL700G2-MIB",
    **{"hdsl700G2System": hdsl700G2System,
       "hdsl700G2Version": hdsl700G2Version,
       "gdc700G2SystemMIBversion": gdc700G2SystemMIBversion,
       "hdsl700G2Alarms": hdsl700G2Alarms,
       "hdsl700G2NoResponseAlm": hdsl700G2NoResponseAlm,
       "hdsl700G2DiagRxErrAlm": hdsl700G2DiagRxErrAlm,
       "hdsl700G2PowerUpAlm": hdsl700G2PowerUpAlm,
       "hdsl700G2UnitFailure": hdsl700G2UnitFailure,
       "hdsl700G2ChecksumCorrupt": hdsl700G2ChecksumCorrupt,
       "hdsl700G2LossofSignal": hdsl700G2LossofSignal,
       "hdsl700G2UnavailableSec": hdsl700G2UnavailableSec,
       "hdsl700G2ErrorSec": hdsl700G2ErrorSec,
       "hdsl700G2LossofSyncWord": hdsl700G2LossofSyncWord,
       "hdsl700G2LossofFrameAlign": hdsl700G2LossofFrameAlign,
       "hdsl700G2AllOnes": hdsl700G2AllOnes,
       "hdsl700G2RemoteLossofSig": hdsl700G2RemoteLossofSig,
       "hdsl700G2RemoteAlarmInd": hdsl700G2RemoteAlarmInd,
       "hdsl700G2MajorBER": hdsl700G2MajorBER,
       "hdsl700G2MinorBER": hdsl700G2MinorBER}
)
