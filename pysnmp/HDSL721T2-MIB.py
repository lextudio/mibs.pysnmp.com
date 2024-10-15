# SNMP MIB module (HDSL721T2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL721T2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:15 2024
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

(hdsl721T2,) = mibBuilder.importSymbols(
    "GDCHDSL-MIB",
    "hdsl721T2")

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

_Hdsl721T2System_ObjectIdentity = ObjectIdentity
hdsl721T2System = _Hdsl721T2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 1)
)
_Hdsl721T2Version_ObjectIdentity = ObjectIdentity
hdsl721T2Version = _Hdsl721T2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 1, 1)
)


class _Gdc721T2SystemMIBversion_Type(DisplayString):
    """Custom type gdc721T2SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Gdc721T2SystemMIBversion_Type.__name__ = "DisplayString"
_Gdc721T2SystemMIBversion_Object = MibScalar
gdc721T2SystemMIBversion = _Gdc721T2SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 1, 1, 1),
    _Gdc721T2SystemMIBversion_Type()
)
gdc721T2SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdc721T2SystemMIBversion.setStatus("mandatory")
_Hdsl721T2Alarms_ObjectIdentity = ObjectIdentity
hdsl721T2Alarms = _Hdsl721T2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2)
)
_Hdsl721T2NoResponseAlm_ObjectIdentity = ObjectIdentity
hdsl721T2NoResponseAlm = _Hdsl721T2NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 1)
)
_Hdsl721T2DiagRxErrAlm_ObjectIdentity = ObjectIdentity
hdsl721T2DiagRxErrAlm = _Hdsl721T2DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 2)
)
_Hdsl721T2PowerUpAlm_ObjectIdentity = ObjectIdentity
hdsl721T2PowerUpAlm = _Hdsl721T2PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 3)
)
_Hdsl721T2UnitFailure_ObjectIdentity = ObjectIdentity
hdsl721T2UnitFailure = _Hdsl721T2UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 4)
)
_Hdsl721T2ChecksumCorrupt_ObjectIdentity = ObjectIdentity
hdsl721T2ChecksumCorrupt = _Hdsl721T2ChecksumCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 5)
)
_Hdsl721T2LossofSignal_ObjectIdentity = ObjectIdentity
hdsl721T2LossofSignal = _Hdsl721T2LossofSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 6)
)
_Hdsl721T2UnavailableSec_ObjectIdentity = ObjectIdentity
hdsl721T2UnavailableSec = _Hdsl721T2UnavailableSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 7)
)
_Hdsl721T2ErrorSec_ObjectIdentity = ObjectIdentity
hdsl721T2ErrorSec = _Hdsl721T2ErrorSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 8)
)
_Hdsl721T2LossofSyncWord_ObjectIdentity = ObjectIdentity
hdsl721T2LossofSyncWord = _Hdsl721T2LossofSyncWord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 9)
)
_Hdsl721T2OutofFrame_ObjectIdentity = ObjectIdentity
hdsl721T2OutofFrame = _Hdsl721T2OutofFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 10)
)
_Hdsl721T2AllOnes_ObjectIdentity = ObjectIdentity
hdsl721T2AllOnes = _Hdsl721T2AllOnes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 11)
)
_Hdsl721T2RemoteLossofSig_ObjectIdentity = ObjectIdentity
hdsl721T2RemoteLossofSig = _Hdsl721T2RemoteLossofSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 12)
)
_Hdsl721T2RemoteAlarmInd_ObjectIdentity = ObjectIdentity
hdsl721T2RemoteAlarmInd = _Hdsl721T2RemoteAlarmInd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 13)
)
_Hdsl721T2MajorBER_ObjectIdentity = ObjectIdentity
hdsl721T2MajorBER = _Hdsl721T2MajorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 14)
)
_Hdsl721T2MinorBER_ObjectIdentity = ObjectIdentity
hdsl721T2MinorBER = _Hdsl721T2MinorBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17, 2, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL721T2-MIB",
    **{"hdsl721T2System": hdsl721T2System,
       "hdsl721T2Version": hdsl721T2Version,
       "gdc721T2SystemMIBversion": gdc721T2SystemMIBversion,
       "hdsl721T2Alarms": hdsl721T2Alarms,
       "hdsl721T2NoResponseAlm": hdsl721T2NoResponseAlm,
       "hdsl721T2DiagRxErrAlm": hdsl721T2DiagRxErrAlm,
       "hdsl721T2PowerUpAlm": hdsl721T2PowerUpAlm,
       "hdsl721T2UnitFailure": hdsl721T2UnitFailure,
       "hdsl721T2ChecksumCorrupt": hdsl721T2ChecksumCorrupt,
       "hdsl721T2LossofSignal": hdsl721T2LossofSignal,
       "hdsl721T2UnavailableSec": hdsl721T2UnavailableSec,
       "hdsl721T2ErrorSec": hdsl721T2ErrorSec,
       "hdsl721T2LossofSyncWord": hdsl721T2LossofSyncWord,
       "hdsl721T2OutofFrame": hdsl721T2OutofFrame,
       "hdsl721T2AllOnes": hdsl721T2AllOnes,
       "hdsl721T2RemoteLossofSig": hdsl721T2RemoteLossofSig,
       "hdsl721T2RemoteAlarmInd": hdsl721T2RemoteAlarmInd,
       "hdsl721T2MajorBER": hdsl721T2MajorBER,
       "hdsl721T2MinorBER": hdsl721T2MinorBER}
)
