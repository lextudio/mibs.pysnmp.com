# SNMP MIB module (MULTIPLE-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MULTIPLE-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:07 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ati_ObjectIdentity = ObjectIdentity
ati = _Ati_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
_Mibobjs_ObjectIdentity = ObjectIdentity
mibobjs = _Mibobjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_AtiSwitchObjs_ObjectIdentity = ObjectIdentity
atiSwitchObjs = _AtiSwitchObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 3)
)
_AtiSystemConfig_ObjectIdentity = ObjectIdentity
atiSystemConfig = _AtiSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 1)
)


class _AtiSysSerialno_Type(DisplayString):
    """Custom type atiSysSerialno based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiSysSerialno_Type.__name__ = "DisplayString"
_AtiSysSerialno_Object = MibScalar
atiSysSerialno = _AtiSysSerialno_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 1),
    _AtiSysSerialno_Type()
)
atiSysSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiSysSerialno.setStatus("mandatory")
_AtiSysTftpIPAddress_Type = IpAddress
_AtiSysTftpIPAddress_Object = MibScalar
atiSysTftpIPAddress = _AtiSysTftpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 2),
    _AtiSysTftpIPAddress_Type()
)
atiSysTftpIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSysTftpIPAddress.setStatus("mandatory")


class _AtiSysTftpFilename_Type(DisplayString):
    """Custom type atiSysTftpFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiSysTftpFilename_Type.__name__ = "DisplayString"
_AtiSysTftpFilename_Object = MibScalar
atiSysTftpFilename = _AtiSysTftpFilename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 3),
    _AtiSysTftpFilename_Type()
)
atiSysTftpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSysTftpFilename.setStatus("mandatory")
_AtiSysPowerupCount_Type = Integer32
_AtiSysPowerupCount_Object = MibScalar
atiSysPowerupCount = _AtiSysPowerupCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 4),
    _AtiSysPowerupCount_Type()
)
atiSysPowerupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiSysPowerupCount.setStatus("mandatory")
_AtiSysBrcastCutoffRate_Type = Integer32
_AtiSysBrcastCutoffRate_Object = MibScalar
atiSysBrcastCutoffRate = _AtiSysBrcastCutoffRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 5),
    _AtiSysBrcastCutoffRate_Type()
)
atiSysBrcastCutoffRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSysBrcastCutoffRate.setStatus("mandatory")
_AtiSysGatewayIPAddress_Type = IpAddress
_AtiSysGatewayIPAddress_Object = MibScalar
atiSysGatewayIPAddress = _AtiSysGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 6),
    _AtiSysGatewayIPAddress_Type()
)
atiSysGatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSysGatewayIPAddress.setStatus("mandatory")
_AtiPortTable_Object = MibTable
atiPortTable = _AtiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 2)
)
if mibBuilder.loadTexts:
    atiPortTable.setStatus("mandatory")
_AtiPortEntry_Object = MibTableRow
atiPortEntry = _AtiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1)
)
atiPortEntry.setIndexNames(
    (0, "MULTIPLE-BRIDGE-MIB", "atiPort"),
)
if mibBuilder.loadTexts:
    atiPortEntry.setStatus("mandatory")
_AtiPort_Type = Integer32
_AtiPort_Object = MibTableColumn
atiPort = _AtiPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 1),
    _AtiPort_Type()
)
atiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiPort.setStatus("mandatory")


class _AtiPortStatus_Type(Integer32):
    """Custom type atiPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtiPortStatus_Type.__name__ = "Integer32"
_AtiPortStatus_Object = MibTableColumn
atiPortStatus = _AtiPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 2),
    _AtiPortStatus_Type()
)
atiPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiPortStatus.setStatus("mandatory")


class _AtiPortDuplexStatus_Type(Integer32):
    """Custom type atiPortDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_AtiPortDuplexStatus_Type.__name__ = "Integer32"
_AtiPortDuplexStatus_Object = MibTableColumn
atiPortDuplexStatus = _AtiPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 3),
    _AtiPortDuplexStatus_Type()
)
atiPortDuplexStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiPortDuplexStatus.setStatus("mandatory")
_AtiPortForwardedFrames_Type = Counter32
_AtiPortForwardedFrames_Object = MibTableColumn
atiPortForwardedFrames = _AtiPortForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 4),
    _AtiPortForwardedFrames_Type()
)
atiPortForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiPortForwardedFrames.setStatus("mandatory")
_AtiPortRcvdLocalFrames_Type = Counter32
_AtiPortRcvdLocalFrames_Object = MibTableColumn
atiPortRcvdLocalFrames = _AtiPortRcvdLocalFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 5),
    _AtiPortRcvdLocalFrames_Type()
)
atiPortRcvdLocalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiPortRcvdLocalFrames.setStatus("mandatory")
_AtiSwitch_ObjectIdentity = ObjectIdentity
atiSwitch = _AtiSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3)
)
_AtiSwitchIPAddress_Type = IpAddress
_AtiSwitchIPAddress_Object = MibScalar
atiSwitchIPAddress = _AtiSwitchIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 1),
    _AtiSwitchIPAddress_Type()
)
atiSwitchIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSwitchIPAddress.setStatus("mandatory")
_AtiSwitchSubnetMask_Type = IpAddress
_AtiSwitchSubnetMask_Object = MibScalar
atiSwitchSubnetMask = _AtiSwitchSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 2),
    _AtiSwitchSubnetMask_Type()
)
atiSwitchSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSwitchSubnetMask.setStatus("mandatory")
_AtiActiveAgingTime_Type = Integer32
_AtiActiveAgingTime_Object = MibScalar
atiActiveAgingTime = _AtiActiveAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 3),
    _AtiActiveAgingTime_Type()
)
atiActiveAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiActiveAgingTime.setStatus("mandatory")
_AtiPurgeAgingTime_Type = Integer32
_AtiPurgeAgingTime_Object = MibScalar
atiPurgeAgingTime = _AtiPurgeAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 4),
    _AtiPurgeAgingTime_Type()
)
atiPurgeAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiPurgeAgingTime.setStatus("mandatory")


class _AtiSwitchSTPStatus_Type(Integer32):
    """Custom type atiSwitchSTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AtiSwitchSTPStatus_Type.__name__ = "Integer32"
_AtiSwitchSTPStatus_Object = MibScalar
atiSwitchSTPStatus = _AtiSwitchSTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 5),
    _AtiSwitchSTPStatus_Type()
)
atiSwitchSTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSwitchSTPStatus.setStatus("mandatory")
_AtiSwitchManager_ObjectIdentity = ObjectIdentity
atiSwitchManager = _AtiSwitchManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6)
)
_AtiSwitchTrapRcvr1_Type = IpAddress
_AtiSwitchTrapRcvr1_Object = MibScalar
atiSwitchTrapRcvr1 = _AtiSwitchTrapRcvr1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 1),
    _AtiSwitchTrapRcvr1_Type()
)
atiSwitchTrapRcvr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSwitchTrapRcvr1.setStatus("mandatory")
_AtiSwitchTrapRcvr2_Type = IpAddress
_AtiSwitchTrapRcvr2_Object = MibScalar
atiSwitchTrapRcvr2 = _AtiSwitchTrapRcvr2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 2),
    _AtiSwitchTrapRcvr2_Type()
)
atiSwitchTrapRcvr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSwitchTrapRcvr2.setStatus("mandatory")
_AtiSwitchTrapRcvr3_Type = IpAddress
_AtiSwitchTrapRcvr3_Object = MibScalar
atiSwitchTrapRcvr3 = _AtiSwitchTrapRcvr3_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 3),
    _AtiSwitchTrapRcvr3_Type()
)
atiSwitchTrapRcvr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSwitchTrapRcvr3.setStatus("mandatory")
_AtiSwitchTrapRcvr4_Type = IpAddress
_AtiSwitchTrapRcvr4_Object = MibScalar
atiSwitchTrapRcvr4 = _AtiSwitchTrapRcvr4_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 4),
    _AtiSwitchTrapRcvr4_Type()
)
atiSwitchTrapRcvr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSwitchTrapRcvr4.setStatus("mandatory")


class _AtiSwitchPortMirroring_Type(Integer32):
    """Custom type atiSwitchPortMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtiSwitchPortMirroring_Type.__name__ = "Integer32"
_AtiSwitchPortMirroring_Object = MibScalar
atiSwitchPortMirroring = _AtiSwitchPortMirroring_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 7),
    _AtiSwitchPortMirroring_Type()
)
atiSwitchPortMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSwitchPortMirroring.setStatus("mandatory")
_AtiSwitchMirroredPort_Type = Integer32
_AtiSwitchMirroredPort_Object = MibScalar
atiSwitchMirroredPort = _AtiSwitchMirroredPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 8),
    _AtiSwitchMirroredPort_Type()
)
atiSwitchMirroredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiSwitchMirroredPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MULTIPLE-BRIDGE-MIB",
    **{"MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "ati": ati,
       "mibobjs": mibobjs,
       "atiSwitchObjs": atiSwitchObjs,
       "atiSystemConfig": atiSystemConfig,
       "atiSysSerialno": atiSysSerialno,
       "atiSysTftpIPAddress": atiSysTftpIPAddress,
       "atiSysTftpFilename": atiSysTftpFilename,
       "atiSysPowerupCount": atiSysPowerupCount,
       "atiSysBrcastCutoffRate": atiSysBrcastCutoffRate,
       "atiSysGatewayIPAddress": atiSysGatewayIPAddress,
       "atiPortTable": atiPortTable,
       "atiPortEntry": atiPortEntry,
       "atiPort": atiPort,
       "atiPortStatus": atiPortStatus,
       "atiPortDuplexStatus": atiPortDuplexStatus,
       "atiPortForwardedFrames": atiPortForwardedFrames,
       "atiPortRcvdLocalFrames": atiPortRcvdLocalFrames,
       "atiSwitch": atiSwitch,
       "atiSwitchIPAddress": atiSwitchIPAddress,
       "atiSwitchSubnetMask": atiSwitchSubnetMask,
       "atiActiveAgingTime": atiActiveAgingTime,
       "atiPurgeAgingTime": atiPurgeAgingTime,
       "atiSwitchSTPStatus": atiSwitchSTPStatus,
       "atiSwitchManager": atiSwitchManager,
       "atiSwitchTrapRcvr1": atiSwitchTrapRcvr1,
       "atiSwitchTrapRcvr2": atiSwitchTrapRcvr2,
       "atiSwitchTrapRcvr3": atiSwitchTrapRcvr3,
       "atiSwitchTrapRcvr4": atiSwitchTrapRcvr4,
       "atiSwitchPortMirroring": atiSwitchPortMirroring,
       "atiSwitchMirroredPort": atiSwitchMirroredPort}
)
