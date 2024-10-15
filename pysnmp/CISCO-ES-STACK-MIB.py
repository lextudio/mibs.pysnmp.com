# SNMP MIB module (CISCO-ES-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ES-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:53 2024
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

(sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation",
    "sysName")

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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddr(OctetString):
    """Custom type MacAddr based on OctetString"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cisco_ObjectIdentity = ObjectIdentity
cisco = _Cisco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9)
)
_Workgroup_ObjectIdentity = ObjectIdentity
workgroup = _Workgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5)
)
_EsStack_ObjectIdentity = ObjectIdentity
esStack = _EsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14)
)
_CiscoEsMain_ObjectIdentity = ObjectIdentity
ciscoEsMain = _CiscoEsMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1)
)
_CiscoEsConfig_ObjectIdentity = ObjectIdentity
ciscoEsConfig = _CiscoEsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1)
)
_CiscoEsIpAddr_Type = IpAddress
_CiscoEsIpAddr_Object = MibScalar
ciscoEsIpAddr = _CiscoEsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 1),
    _CiscoEsIpAddr_Type()
)
ciscoEsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsIpAddr.setStatus("mandatory")
_CiscoEsNetMask_Type = IpAddress
_CiscoEsNetMask_Object = MibScalar
ciscoEsNetMask = _CiscoEsNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 2),
    _CiscoEsNetMask_Type()
)
ciscoEsNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsNetMask.setStatus("mandatory")
_CiscoEsDefaultGateway_Type = IpAddress
_CiscoEsDefaultGateway_Object = MibScalar
ciscoEsDefaultGateway = _CiscoEsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 3),
    _CiscoEsDefaultGateway_Type()
)
ciscoEsDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDefaultGateway.setStatus("mandatory")


class _CiscoEsSysCurTime_Type(DisplayString):
    """Custom type ciscoEsSysCurTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CiscoEsSysCurTime_Type.__name__ = "DisplayString"
_CiscoEsSysCurTime_Object = MibScalar
ciscoEsSysCurTime = _CiscoEsSysCurTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 4),
    _CiscoEsSysCurTime_Type()
)
ciscoEsSysCurTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsSysCurTime.setStatus("mandatory")


class _CiscoEsConfiguration_Type(Integer32):
    """Custom type ciscoEsConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("back-to-back", 2),
          ("prostack-matrix", 3),
          ("stand-alone", 1))
    )


_CiscoEsConfiguration_Type.__name__ = "Integer32"
_CiscoEsConfiguration_Object = MibScalar
ciscoEsConfiguration = _CiscoEsConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 5),
    _CiscoEsConfiguration_Type()
)
ciscoEsConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsConfiguration.setStatus("mandatory")
_CiscoEsNumSwitches_Type = Integer32
_CiscoEsNumSwitches_Object = MibScalar
ciscoEsNumSwitches = _CiscoEsNumSwitches_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 6),
    _CiscoEsNumSwitches_Type()
)
ciscoEsNumSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsNumSwitches.setStatus("mandatory")


class _CiscoEsStackStatus_Type(Integer32):
    """Custom type ciscoEsStackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("updating", 2))
    )


_CiscoEsStackStatus_Type.__name__ = "Integer32"
_CiscoEsStackStatus_Object = MibScalar
ciscoEsStackStatus = _CiscoEsStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 7),
    _CiscoEsStackStatus_Type()
)
ciscoEsStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackStatus.setStatus("mandatory")
_CiscoEsTftpServer_Type = IpAddress
_CiscoEsTftpServer_Object = MibScalar
ciscoEsTftpServer = _CiscoEsTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 8),
    _CiscoEsTftpServer_Type()
)
ciscoEsTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsTftpServer.setStatus("mandatory")


class _CiscoEsTftpServerDomain_Type(Integer32):
    """Custom type ciscoEsTftpServerDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CiscoEsTftpServerDomain_Type.__name__ = "Integer32"
_CiscoEsTftpServerDomain_Object = MibScalar
ciscoEsTftpServerDomain = _CiscoEsTftpServerDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 9),
    _CiscoEsTftpServerDomain_Type()
)
ciscoEsTftpServerDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsTftpServerDomain.setStatus("mandatory")


class _CiscoEsTftpFileLoc_Type(DisplayString):
    """Custom type ciscoEsTftpFileLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CiscoEsTftpFileLoc_Type.__name__ = "DisplayString"
_CiscoEsTftpFileLoc_Object = MibScalar
ciscoEsTftpFileLoc = _CiscoEsTftpFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 10),
    _CiscoEsTftpFileLoc_Type()
)
ciscoEsTftpFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsTftpFileLoc.setStatus("mandatory")
_CiscoEsSetLock_Type = IpAddress
_CiscoEsSetLock_Object = MibScalar
ciscoEsSetLock = _CiscoEsSetLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 11),
    _CiscoEsSetLock_Type()
)
ciscoEsSetLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsSetLock.setStatus("mandatory")


class _CiscoEsProStackMatrixStatus_Type(Integer32):
    """Custom type ciscoEsProStackMatrixStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("none", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_CiscoEsProStackMatrixStatus_Type.__name__ = "Integer32"
_CiscoEsProStackMatrixStatus_Object = MibScalar
ciscoEsProStackMatrixStatus = _CiscoEsProStackMatrixStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 12),
    _CiscoEsProStackMatrixStatus_Type()
)
ciscoEsProStackMatrixStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsProStackMatrixStatus.setStatus("mandatory")
_CiscoEsNumMatrixModules_Type = Integer32
_CiscoEsNumMatrixModules_Object = MibScalar
ciscoEsNumMatrixModules = _CiscoEsNumMatrixModules_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 13),
    _CiscoEsNumMatrixModules_Type()
)
ciscoEsNumMatrixModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsNumMatrixModules.setStatus("mandatory")


class _CiscoEsLLPortDsbld_Type(Integer32):
    """Custom type ciscoEsLLPortDsbld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disabled", 1)
    )


_CiscoEsLLPortDsbld_Type.__name__ = "Integer32"
_CiscoEsLLPortDsbld_Object = MibScalar
ciscoEsLLPortDsbld = _CiscoEsLLPortDsbld_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 14),
    _CiscoEsLLPortDsbld_Type()
)
ciscoEsLLPortDsbld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsLLPortDsbld.setStatus("mandatory")
_CiscoEsTrapRcvrTable_Object = MibTable
ciscoEsTrapRcvrTable = _CiscoEsTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 25)
)
if mibBuilder.loadTexts:
    ciscoEsTrapRcvrTable.setStatus("mandatory")
_CiscoEsTrapRcvrEntry_Object = MibTableRow
ciscoEsTrapRcvrEntry = _CiscoEsTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 25, 1)
)
ciscoEsTrapRcvrEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsTrapRcvrIndex"),
)
if mibBuilder.loadTexts:
    ciscoEsTrapRcvrEntry.setStatus("mandatory")


class _CiscoEsTrapRcvrIndex_Type(Integer32):
    """Custom type ciscoEsTrapRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CiscoEsTrapRcvrIndex_Type.__name__ = "Integer32"
_CiscoEsTrapRcvrIndex_Object = MibTableColumn
ciscoEsTrapRcvrIndex = _CiscoEsTrapRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 25, 1, 1),
    _CiscoEsTrapRcvrIndex_Type()
)
ciscoEsTrapRcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsTrapRcvrIndex.setStatus("mandatory")


class _CiscoEsTrapRcvrStatus_Type(Integer32):
    """Custom type ciscoEsTrapRcvrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("create", 4),
          ("invalid", 3),
          ("other", 1),
          ("valid", 2))
    )


_CiscoEsTrapRcvrStatus_Type.__name__ = "Integer32"
_CiscoEsTrapRcvrStatus_Object = MibTableColumn
ciscoEsTrapRcvrStatus = _CiscoEsTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 25, 1, 2),
    _CiscoEsTrapRcvrStatus_Type()
)
ciscoEsTrapRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsTrapRcvrStatus.setStatus("mandatory")
_CiscoEsTrapRcvrIpAddress_Type = IpAddress
_CiscoEsTrapRcvrIpAddress_Object = MibTableColumn
ciscoEsTrapRcvrIpAddress = _CiscoEsTrapRcvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 25, 1, 3),
    _CiscoEsTrapRcvrIpAddress_Type()
)
ciscoEsTrapRcvrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsTrapRcvrIpAddress.setStatus("mandatory")


class _CiscoEsTrapRcvrComm_Type(DisplayString):
    """Custom type ciscoEsTrapRcvrComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CiscoEsTrapRcvrComm_Type.__name__ = "DisplayString"
_CiscoEsTrapRcvrComm_Object = MibTableColumn
ciscoEsTrapRcvrComm = _CiscoEsTrapRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 25, 1, 4),
    _CiscoEsTrapRcvrComm_Type()
)
ciscoEsTrapRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsTrapRcvrComm.setStatus("mandatory")


class _CiscoEsTrapRcvrVLANs_Type(OctetString):
    """Custom type ciscoEsTrapRcvrVLANs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CiscoEsTrapRcvrVLANs_Type.__name__ = "OctetString"
_CiscoEsTrapRcvrVLANs_Object = MibTableColumn
ciscoEsTrapRcvrVLANs = _CiscoEsTrapRcvrVLANs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 25, 1, 5),
    _CiscoEsTrapRcvrVLANs_Type()
)
ciscoEsTrapRcvrVLANs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsTrapRcvrVLANs.setStatus("mandatory")
_CiscoEsStack_ObjectIdentity = ObjectIdentity
ciscoEsStack = _CiscoEsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2)
)
_CiscoEsStackTable_Object = MibTable
ciscoEsStackTable = _CiscoEsStackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoEsStackTable.setStatus("mandatory")
_CiscoEsStackEntry_Object = MibTableRow
ciscoEsStackEntry = _CiscoEsStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1)
)
ciscoEsStackEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsStackSwitchNumber"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsStackSwitchAddr"),
)
if mibBuilder.loadTexts:
    ciscoEsStackEntry.setStatus("mandatory")


class _CiscoEsStackSwitchNumber_Type(Integer32):
    """Custom type ciscoEsStackSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsStackSwitchNumber_Type.__name__ = "Integer32"
_CiscoEsStackSwitchNumber_Object = MibTableColumn
ciscoEsStackSwitchNumber = _CiscoEsStackSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 1),
    _CiscoEsStackSwitchNumber_Type()
)
ciscoEsStackSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchNumber.setStatus("mandatory")
_CiscoEsStackSwitchAddr_Type = MacAddr
_CiscoEsStackSwitchAddr_Object = MibTableColumn
ciscoEsStackSwitchAddr = _CiscoEsStackSwitchAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 2),
    _CiscoEsStackSwitchAddr_Type()
)
ciscoEsStackSwitchAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchAddr.setStatus("mandatory")


class _CiscoEsStackSwitchFwVersion_Type(DisplayString):
    """Custom type ciscoEsStackSwitchFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CiscoEsStackSwitchFwVersion_Type.__name__ = "DisplayString"
_CiscoEsStackSwitchFwVersion_Object = MibTableColumn
ciscoEsStackSwitchFwVersion = _CiscoEsStackSwitchFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 3),
    _CiscoEsStackSwitchFwVersion_Type()
)
ciscoEsStackSwitchFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchFwVersion.setStatus("mandatory")


class _CiscoEsStackSwitchHwVersion_Type(DisplayString):
    """Custom type ciscoEsStackSwitchHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CiscoEsStackSwitchHwVersion_Type.__name__ = "DisplayString"
_CiscoEsStackSwitchHwVersion_Object = MibTableColumn
ciscoEsStackSwitchHwVersion = _CiscoEsStackSwitchHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 4),
    _CiscoEsStackSwitchHwVersion_Type()
)
ciscoEsStackSwitchHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchHwVersion.setStatus("mandatory")
_CiscoEsStackSwitchUptime_Type = TimeTicks
_CiscoEsStackSwitchUptime_Object = MibTableColumn
ciscoEsStackSwitchUptime = _CiscoEsStackSwitchUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 6),
    _CiscoEsStackSwitchUptime_Type()
)
ciscoEsStackSwitchUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchUptime.setStatus("mandatory")


class _CiscoEsStackSwitchStatus_Type(Integer32):
    """Custom type ciscoEsStackSwitchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldReset", 2),
          ("running", 1),
          ("warmReset", 3))
    )


_CiscoEsStackSwitchStatus_Type.__name__ = "Integer32"
_CiscoEsStackSwitchStatus_Object = MibTableColumn
ciscoEsStackSwitchStatus = _CiscoEsStackSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 7),
    _CiscoEsStackSwitchStatus_Type()
)
ciscoEsStackSwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchStatus.setStatus("mandatory")


class _CiscoEsStackSwitchTemperature_Type(Integer32):
    """Custom type ciscoEsStackSwitchTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("toohigh", 2),
          ("unknown", 3))
    )


_CiscoEsStackSwitchTemperature_Type.__name__ = "Integer32"
_CiscoEsStackSwitchTemperature_Object = MibTableColumn
ciscoEsStackSwitchTemperature = _CiscoEsStackSwitchTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 8),
    _CiscoEsStackSwitchTemperature_Type()
)
ciscoEsStackSwitchTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchTemperature.setStatus("mandatory")
_CiscoEsStackSwitchMemory_Type = Integer32
_CiscoEsStackSwitchMemory_Object = MibTableColumn
ciscoEsStackSwitchMemory = _CiscoEsStackSwitchMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 9),
    _CiscoEsStackSwitchMemory_Type()
)
ciscoEsStackSwitchMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchMemory.setStatus("mandatory")


class _CiscoEsStackSwitchProbe_Type(Integer32):
    """Custom type ciscoEsStackSwitchProbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CiscoEsStackSwitchProbe_Type.__name__ = "Integer32"
_CiscoEsStackSwitchProbe_Object = MibTableColumn
ciscoEsStackSwitchProbe = _CiscoEsStackSwitchProbe_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 10),
    _CiscoEsStackSwitchProbe_Type()
)
ciscoEsStackSwitchProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchProbe.setStatus("mandatory")


class _CiscoEsStackSwitchProbeDirection_Type(Integer32):
    """Custom type ciscoEsStackSwitchProbeDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("none", 4),
          ("receive", 2),
          ("transmit", 1))
    )


_CiscoEsStackSwitchProbeDirection_Type.__name__ = "Integer32"
_CiscoEsStackSwitchProbeDirection_Object = MibTableColumn
ciscoEsStackSwitchProbeDirection = _CiscoEsStackSwitchProbeDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 11),
    _CiscoEsStackSwitchProbeDirection_Type()
)
ciscoEsStackSwitchProbeDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchProbeDirection.setStatus("mandatory")


class _CiscoEsStackSwitchFeatureStatus_Type(Integer32):
    """Custom type ciscoEsStackSwitchFeatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enhanced", 2),
          ("standard", 1),
          ("unknown", 3))
    )


_CiscoEsStackSwitchFeatureStatus_Type.__name__ = "Integer32"
_CiscoEsStackSwitchFeatureStatus_Object = MibTableColumn
ciscoEsStackSwitchFeatureStatus = _CiscoEsStackSwitchFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 12),
    _CiscoEsStackSwitchFeatureStatus_Type()
)
ciscoEsStackSwitchFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchFeatureStatus.setStatus("mandatory")
_CiscoEsStackSwitchFeatureKey_Type = Integer32
_CiscoEsStackSwitchFeatureKey_Object = MibTableColumn
ciscoEsStackSwitchFeatureKey = _CiscoEsStackSwitchFeatureKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 13),
    _CiscoEsStackSwitchFeatureKey_Type()
)
ciscoEsStackSwitchFeatureKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchFeatureKey.setStatus("mandatory")


class _CiscoEsStackSwitchPorts_Type(OctetString):
    """Custom type ciscoEsStackSwitchPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoEsStackSwitchPorts_Type.__name__ = "OctetString"
_CiscoEsStackSwitchPorts_Object = MibTableColumn
ciscoEsStackSwitchPorts = _CiscoEsStackSwitchPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 14),
    _CiscoEsStackSwitchPorts_Type()
)
ciscoEsStackSwitchPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchPorts.setStatus("mandatory")


class _CiscoEsStackSwitchAgingTime_Type(Integer32):
    """Custom type ciscoEsStackSwitchAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CiscoEsStackSwitchAgingTime_Type.__name__ = "Integer32"
_CiscoEsStackSwitchAgingTime_Object = MibTableColumn
ciscoEsStackSwitchAgingTime = _CiscoEsStackSwitchAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 15),
    _CiscoEsStackSwitchAgingTime_Type()
)
ciscoEsStackSwitchAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchAgingTime.setStatus("mandatory")


class _CiscoEsStackSwitchAgingLevel_Type(Integer32):
    """Custom type ciscoEsStackSwitchAgingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_CiscoEsStackSwitchAgingLevel_Type.__name__ = "Integer32"
_CiscoEsStackSwitchAgingLevel_Object = MibTableColumn
ciscoEsStackSwitchAgingLevel = _CiscoEsStackSwitchAgingLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 16),
    _CiscoEsStackSwitchAgingLevel_Type()
)
ciscoEsStackSwitchAgingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchAgingLevel.setStatus("mandatory")
_CiscoEsStackSwitchBufferOverruns_Type = Counter32
_CiscoEsStackSwitchBufferOverruns_Object = MibTableColumn
ciscoEsStackSwitchBufferOverruns = _CiscoEsStackSwitchBufferOverruns_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 17),
    _CiscoEsStackSwitchBufferOverruns_Type()
)
ciscoEsStackSwitchBufferOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchBufferOverruns.setStatus("mandatory")
_CiscoEsStackSwitchSoftwareFrames_Type = Counter32
_CiscoEsStackSwitchSoftwareFrames_Object = MibTableColumn
ciscoEsStackSwitchSoftwareFrames = _CiscoEsStackSwitchSoftwareFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 18),
    _CiscoEsStackSwitchSoftwareFrames_Type()
)
ciscoEsStackSwitchSoftwareFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchSoftwareFrames.setStatus("mandatory")
_CiscoEsStackSwitchInErrFrames_Type = Counter32
_CiscoEsStackSwitchInErrFrames_Object = MibTableColumn
ciscoEsStackSwitchInErrFrames = _CiscoEsStackSwitchInErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 19),
    _CiscoEsStackSwitchInErrFrames_Type()
)
ciscoEsStackSwitchInErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchInErrFrames.setStatus("mandatory")
_CiscoEsStackSwitchInShortFrames_Type = Counter32
_CiscoEsStackSwitchInShortFrames_Object = MibTableColumn
ciscoEsStackSwitchInShortFrames = _CiscoEsStackSwitchInShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 20),
    _CiscoEsStackSwitchInShortFrames_Type()
)
ciscoEsStackSwitchInShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchInShortFrames.setStatus("mandatory")
_CiscoEsStackSwitchInLongFrames_Type = Counter32
_CiscoEsStackSwitchInLongFrames_Object = MibTableColumn
ciscoEsStackSwitchInLongFrames = _CiscoEsStackSwitchInLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 21),
    _CiscoEsStackSwitchInLongFrames_Type()
)
ciscoEsStackSwitchInLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchInLongFrames.setStatus("mandatory")
_CiscoEsStackSwitchOutDroppedFrames_Type = Counter32
_CiscoEsStackSwitchOutDroppedFrames_Object = MibTableColumn
ciscoEsStackSwitchOutDroppedFrames = _CiscoEsStackSwitchOutDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 22),
    _CiscoEsStackSwitchOutDroppedFrames_Type()
)
ciscoEsStackSwitchOutDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchOutDroppedFrames.setStatus("mandatory")
_CiscoEsStackSwitchInNoSpaceFrames_Type = Counter32
_CiscoEsStackSwitchInNoSpaceFrames_Object = MibTableColumn
ciscoEsStackSwitchInNoSpaceFrames = _CiscoEsStackSwitchInNoSpaceFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 23),
    _CiscoEsStackSwitchInNoSpaceFrames_Type()
)
ciscoEsStackSwitchInNoSpaceFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchInNoSpaceFrames.setStatus("mandatory")
_CiscoEsStackSwitchOutTotalReqs_Type = Counter32
_CiscoEsStackSwitchOutTotalReqs_Object = MibTableColumn
ciscoEsStackSwitchOutTotalReqs = _CiscoEsStackSwitchOutTotalReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 24),
    _CiscoEsStackSwitchOutTotalReqs_Type()
)
ciscoEsStackSwitchOutTotalReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchOutTotalReqs.setStatus("mandatory")
_CiscoEsStackSwitchOutTotalFrames_Type = Counter32
_CiscoEsStackSwitchOutTotalFrames_Object = MibTableColumn
ciscoEsStackSwitchOutTotalFrames = _CiscoEsStackSwitchOutTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 25),
    _CiscoEsStackSwitchOutTotalFrames_Type()
)
ciscoEsStackSwitchOutTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchOutTotalFrames.setStatus("mandatory")
_CiscoEsStackSwitchLongestHashChain_Type = Gauge32
_CiscoEsStackSwitchLongestHashChain_Object = MibTableColumn
ciscoEsStackSwitchLongestHashChain = _CiscoEsStackSwitchLongestHashChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 26),
    _CiscoEsStackSwitchLongestHashChain_Type()
)
ciscoEsStackSwitchLongestHashChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchLongestHashChain.setStatus("mandatory")
_CiscoEsStackSwitchHashTableFulls_Type = Counter32
_CiscoEsStackSwitchHashTableFulls_Object = MibTableColumn
ciscoEsStackSwitchHashTableFulls = _CiscoEsStackSwitchHashTableFulls_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 27),
    _CiscoEsStackSwitchHashTableFulls_Type()
)
ciscoEsStackSwitchHashTableFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchHashTableFulls.setStatus("mandatory")
_CiscoEsStackSwitchId_Type = ObjectIdentifier
_CiscoEsStackSwitchId_Object = MibTableColumn
ciscoEsStackSwitchId = _CiscoEsStackSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 28),
    _CiscoEsStackSwitchId_Type()
)
ciscoEsStackSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchId.setStatus("mandatory")


class _CiscoEsStackSwitchDplxCtrl_Type(Integer32):
    """Custom type ciscoEsStackSwitchDplxCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 1),
          ("software", 2))
    )


_CiscoEsStackSwitchDplxCtrl_Type.__name__ = "Integer32"
_CiscoEsStackSwitchDplxCtrl_Object = MibTableColumn
ciscoEsStackSwitchDplxCtrl = _CiscoEsStackSwitchDplxCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 1, 1, 29),
    _CiscoEsStackSwitchDplxCtrl_Type()
)
ciscoEsStackSwitchDplxCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsStackSwitchDplxCtrl.setStatus("mandatory")
_CiscoEsModule_ObjectIdentity = ObjectIdentity
ciscoEsModule = _CiscoEsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 3)
)
_CiscoEsModTable_Object = MibTable
ciscoEsModTable = _CiscoEsModTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoEsModTable.setStatus("mandatory")
_CiscoEsModEntry_Object = MibTableRow
ciscoEsModEntry = _CiscoEsModEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 3, 1, 1)
)
ciscoEsModEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsModSwitchNumber"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsModNumber"),
)
if mibBuilder.loadTexts:
    ciscoEsModEntry.setStatus("mandatory")


class _CiscoEsModSwitchNumber_Type(Integer32):
    """Custom type ciscoEsModSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsModSwitchNumber_Type.__name__ = "Integer32"
_CiscoEsModSwitchNumber_Object = MibTableColumn
ciscoEsModSwitchNumber = _CiscoEsModSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 3, 1, 1, 1),
    _CiscoEsModSwitchNumber_Type()
)
ciscoEsModSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsModSwitchNumber.setStatus("mandatory")


class _CiscoEsModNumber_Type(Integer32):
    """Custom type ciscoEsModNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsModNumber_Type.__name__ = "Integer32"
_CiscoEsModNumber_Object = MibTableColumn
ciscoEsModNumber = _CiscoEsModNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 3, 1, 1, 2),
    _CiscoEsModNumber_Type()
)
ciscoEsModNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsModNumber.setStatus("mandatory")


class _CiscoEsModState_Type(Integer32):
    """Custom type ciscoEsModState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 4),
          ("nomodule", 1),
          ("running", 2),
          ("stopped", 3))
    )


_CiscoEsModState_Type.__name__ = "Integer32"
_CiscoEsModState_Object = MibTableColumn
ciscoEsModState = _CiscoEsModState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 3, 1, 1, 3),
    _CiscoEsModState_Type()
)
ciscoEsModState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsModState.setStatus("mandatory")


class _CiscoEsModType_Type(Integer32):
    """Custom type ciscoEsModType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 10),
          ("system", 1),
          ("unknown", 9),
          ("ws-X3001", 3),
          ("ws-X3002", 5),
          ("ws-X3003", 7),
          ("ws-X3004", 2),
          ("ws-X3005", 4),
          ("ws-X3006", 8),
          ("ws-X3007-8", 11),
          ("ws-X3009", 12),
          ("ws-X3010", 13),
          ("ws-X3011", 14),
          ("ws-X3013", 6))
    )


_CiscoEsModType_Type.__name__ = "Integer32"
_CiscoEsModType_Object = MibTableColumn
ciscoEsModType = _CiscoEsModType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 3, 1, 1, 4),
    _CiscoEsModType_Type()
)
ciscoEsModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsModType.setStatus("mandatory")
_CiscoEsModRevision_Type = Integer32
_CiscoEsModRevision_Object = MibTableColumn
ciscoEsModRevision = _CiscoEsModRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 3, 1, 1, 5),
    _CiscoEsModRevision_Type()
)
ciscoEsModRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsModRevision.setStatus("mandatory")
_CiscoEsModNumPorts_Type = Integer32
_CiscoEsModNumPorts_Object = MibTableColumn
ciscoEsModNumPorts = _CiscoEsModNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 3, 1, 1, 6),
    _CiscoEsModNumPorts_Type()
)
ciscoEsModNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsModNumPorts.setStatus("mandatory")
_CiscoEsModUptime_Type = TimeTicks
_CiscoEsModUptime_Object = MibTableColumn
ciscoEsModUptime = _CiscoEsModUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 3, 1, 1, 7),
    _CiscoEsModUptime_Type()
)
ciscoEsModUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsModUptime.setStatus("mandatory")
_CiscoEsPort_ObjectIdentity = ObjectIdentity
ciscoEsPort = _CiscoEsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4)
)
_CiscoEsPortTable_Object = MibTable
ciscoEsPortTable = _CiscoEsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1)
)
if mibBuilder.loadTexts:
    ciscoEsPortTable.setStatus("mandatory")
_CiscoEsPortEntry_Object = MibTableRow
ciscoEsPortEntry = _CiscoEsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1)
)
ciscoEsPortEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsPortSwitchNumber"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsPortNumber"),
)
if mibBuilder.loadTexts:
    ciscoEsPortEntry.setStatus("mandatory")


class _CiscoEsPortSwitchNumber_Type(Integer32):
    """Custom type ciscoEsPortSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsPortSwitchNumber_Type.__name__ = "Integer32"
_CiscoEsPortSwitchNumber_Object = MibTableColumn
ciscoEsPortSwitchNumber = _CiscoEsPortSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 1),
    _CiscoEsPortSwitchNumber_Type()
)
ciscoEsPortSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortSwitchNumber.setStatus("mandatory")


class _CiscoEsPortNumber_Type(Integer32):
    """Custom type ciscoEsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiscoEsPortNumber_Type.__name__ = "Integer32"
_CiscoEsPortNumber_Object = MibTableColumn
ciscoEsPortNumber = _CiscoEsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 2),
    _CiscoEsPortNumber_Type()
)
ciscoEsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortNumber.setStatus("mandatory")


class _CiscoEsPortModNumber_Type(Integer32):
    """Custom type ciscoEsPortModNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CiscoEsPortModNumber_Type.__name__ = "Integer32"
_CiscoEsPortModNumber_Object = MibTableColumn
ciscoEsPortModNumber = _CiscoEsPortModNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 3),
    _CiscoEsPortModNumber_Type()
)
ciscoEsPortModNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortModNumber.setStatus("mandatory")
_CiscoEsPortIfIndex_Type = Integer32
_CiscoEsPortIfIndex_Object = MibTableColumn
ciscoEsPortIfIndex = _CiscoEsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 4),
    _CiscoEsPortIfIndex_Type()
)
ciscoEsPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortIfIndex.setStatus("mandatory")


class _CiscoEsPortDuplex_Type(Integer32):
    """Custom type ciscoEsPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_CiscoEsPortDuplex_Type.__name__ = "Integer32"
_CiscoEsPortDuplex_Object = MibTableColumn
ciscoEsPortDuplex = _CiscoEsPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 5),
    _CiscoEsPortDuplex_Type()
)
ciscoEsPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortDuplex.setStatus("mandatory")
_CiscoEsPortRcvLocalFrames_Type = Counter32
_CiscoEsPortRcvLocalFrames_Object = MibTableColumn
ciscoEsPortRcvLocalFrames = _CiscoEsPortRcvLocalFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 6),
    _CiscoEsPortRcvLocalFrames_Type()
)
ciscoEsPortRcvLocalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortRcvLocalFrames.setStatus("mandatory")
_CiscoEsPortForwardedFrames_Type = Counter32
_CiscoEsPortForwardedFrames_Object = MibTableColumn
ciscoEsPortForwardedFrames = _CiscoEsPortForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 7),
    _CiscoEsPortForwardedFrames_Type()
)
ciscoEsPortForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortForwardedFrames.setStatus("mandatory")
_CiscoEsPortMostStations_Type = Counter32
_CiscoEsPortMostStations_Object = MibTableColumn
ciscoEsPortMostStations = _CiscoEsPortMostStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 8),
    _CiscoEsPortMostStations_Type()
)
ciscoEsPortMostStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortMostStations.setStatus("mandatory")
_CiscoEsPortMaxStations_Type = Counter32
_CiscoEsPortMaxStations_Object = MibTableColumn
ciscoEsPortMaxStations = _CiscoEsPortMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 9),
    _CiscoEsPortMaxStations_Type()
)
ciscoEsPortMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortMaxStations.setStatus("mandatory")
_CiscoEsPortSWHandledFrames_Type = Counter32
_CiscoEsPortSWHandledFrames_Object = MibTableColumn
ciscoEsPortSWHandledFrames = _CiscoEsPortSWHandledFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 10),
    _CiscoEsPortSWHandledFrames_Type()
)
ciscoEsPortSWHandledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortSWHandledFrames.setStatus("mandatory")
_CiscoEsPortLocalStations_Type = Counter32
_CiscoEsPortLocalStations_Object = MibTableColumn
ciscoEsPortLocalStations = _CiscoEsPortLocalStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 11),
    _CiscoEsPortLocalStations_Type()
)
ciscoEsPortLocalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortLocalStations.setStatus("mandatory")
_CiscoEsPortRemoteStations_Type = Counter32
_CiscoEsPortRemoteStations_Object = MibTableColumn
ciscoEsPortRemoteStations = _CiscoEsPortRemoteStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 12),
    _CiscoEsPortRemoteStations_Type()
)
ciscoEsPortRemoteStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortRemoteStations.setStatus("mandatory")
_CiscoEsPortUnknownStaFrames_Type = Counter32
_CiscoEsPortUnknownStaFrames_Object = MibTableColumn
ciscoEsPortUnknownStaFrames = _CiscoEsPortUnknownStaFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 13),
    _CiscoEsPortUnknownStaFrames_Type()
)
ciscoEsPortUnknownStaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortUnknownStaFrames.setStatus("mandatory")


class _CiscoEsPortResetStats_Type(Integer32):
    """Custom type ciscoEsPortResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 3),
          ("running", 2))
    )


_CiscoEsPortResetStats_Type.__name__ = "Integer32"
_CiscoEsPortResetStats_Object = MibTableColumn
ciscoEsPortResetStats = _CiscoEsPortResetStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 14),
    _CiscoEsPortResetStats_Type()
)
ciscoEsPortResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortResetStats.setStatus("mandatory")
_CiscoEsPortResetTimer_Type = TimeTicks
_CiscoEsPortResetTimer_Object = MibTableColumn
ciscoEsPortResetTimer = _CiscoEsPortResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 15),
    _CiscoEsPortResetTimer_Type()
)
ciscoEsPortResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortResetTimer.setStatus("mandatory")


class _CiscoEsPortResetAddrs_Type(Integer32):
    """Custom type ciscoEsPortResetAddrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 3),
          ("running", 2))
    )


_CiscoEsPortResetAddrs_Type.__name__ = "Integer32"
_CiscoEsPortResetAddrs_Object = MibTableColumn
ciscoEsPortResetAddrs = _CiscoEsPortResetAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 16),
    _CiscoEsPortResetAddrs_Type()
)
ciscoEsPortResetAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortResetAddrs.setStatus("mandatory")
_CiscoEsPortInFrames_Type = Counter32
_CiscoEsPortInFrames_Object = MibTableColumn
ciscoEsPortInFrames = _CiscoEsPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 17),
    _CiscoEsPortInFrames_Type()
)
ciscoEsPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortInFrames.setStatus("mandatory")
_CiscoEsPortOutFrames_Type = Counter32
_CiscoEsPortOutFrames_Object = MibTableColumn
ciscoEsPortOutFrames = _CiscoEsPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 18),
    _CiscoEsPortOutFrames_Type()
)
ciscoEsPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortOutFrames.setStatus("mandatory")
_CiscoEsPortLongFrames_Type = Counter32
_CiscoEsPortLongFrames_Object = MibTableColumn
ciscoEsPortLongFrames = _CiscoEsPortLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 19),
    _CiscoEsPortLongFrames_Type()
)
ciscoEsPortLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortLongFrames.setStatus("mandatory")
_CiscoEsPortShortFrames_Type = Counter32
_CiscoEsPortShortFrames_Object = MibTableColumn
ciscoEsPortShortFrames = _CiscoEsPortShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 20),
    _CiscoEsPortShortFrames_Type()
)
ciscoEsPortShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortShortFrames.setStatus("mandatory")
_CiscoEsPortInBufOverflows_Type = Counter32
_CiscoEsPortInBufOverflows_Object = MibTableColumn
ciscoEsPortInBufOverflows = _CiscoEsPortInBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 21),
    _CiscoEsPortInBufOverflows_Type()
)
ciscoEsPortInBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortInBufOverflows.setStatus("mandatory")
_CiscoEsPortOutBufOverflows_Type = Counter32
_CiscoEsPortOutBufOverflows_Object = MibTableColumn
ciscoEsPortOutBufOverflows = _CiscoEsPortOutBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 22),
    _CiscoEsPortOutBufOverflows_Type()
)
ciscoEsPortOutBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortOutBufOverflows.setStatus("mandatory")
_CiscoEsPortRcvBcasts_Type = Counter32
_CiscoEsPortRcvBcasts_Object = MibTableColumn
ciscoEsPortRcvBcasts = _CiscoEsPortRcvBcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 23),
    _CiscoEsPortRcvBcasts_Type()
)
ciscoEsPortRcvBcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortRcvBcasts.setStatus("mandatory")
_CiscoEsPortRcvMcasts_Type = Counter32
_CiscoEsPortRcvMcasts_Object = MibTableColumn
ciscoEsPortRcvMcasts = _CiscoEsPortRcvMcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 24),
    _CiscoEsPortRcvMcasts_Type()
)
ciscoEsPortRcvMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortRcvMcasts.setStatus("mandatory")
_CiscoEsPortSwitchedFrames_Type = Counter32
_CiscoEsPortSwitchedFrames_Object = MibTableColumn
ciscoEsPortSwitchedFrames = _CiscoEsPortSwitchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 25),
    _CiscoEsPortSwitchedFrames_Type()
)
ciscoEsPortSwitchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortSwitchedFrames.setStatus("mandatory")
_CiscoEsPortInOctets_Type = Counter32
_CiscoEsPortInOctets_Object = MibTableColumn
ciscoEsPortInOctets = _CiscoEsPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 26),
    _CiscoEsPortInOctets_Type()
)
ciscoEsPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortInOctets.setStatus("mandatory")
_CiscoEsPortOutOctets_Type = Counter32
_CiscoEsPortOutOctets_Object = MibTableColumn
ciscoEsPortOutOctets = _CiscoEsPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 27),
    _CiscoEsPortOutOctets_Type()
)
ciscoEsPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortOutOctets.setStatus("mandatory")
_CiscoEsPortPktsInErrors_Type = Counter32
_CiscoEsPortPktsInErrors_Object = MibTableColumn
ciscoEsPortPktsInErrors = _CiscoEsPortPktsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 28),
    _CiscoEsPortPktsInErrors_Type()
)
ciscoEsPortPktsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortPktsInErrors.setStatus("mandatory")


class _CiscoEsPortLinkState_Type(Integer32):
    """Custom type ciscoEsPortLinkState based on Integer32"""
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


_CiscoEsPortLinkState_Type.__name__ = "Integer32"
_CiscoEsPortLinkState_Object = MibTableColumn
ciscoEsPortLinkState = _CiscoEsPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 29),
    _CiscoEsPortLinkState_Type()
)
ciscoEsPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortLinkState.setStatus("mandatory")


class _CiscoEsPortOprStatus_Type(Integer32):
    """Custom type ciscoEsPortOprStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("failed", 3))
    )


_CiscoEsPortOprStatus_Type.__name__ = "Integer32"
_CiscoEsPortOprStatus_Object = MibTableColumn
ciscoEsPortOprStatus = _CiscoEsPortOprStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 30),
    _CiscoEsPortOprStatus_Type()
)
ciscoEsPortOprStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortOprStatus.setStatus("mandatory")


class _CiscoEsPortMdiMdix_Type(Integer32):
    """Custom type ciscoEsPortMdiMdix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("internal-term-off", 5),
          ("internal-term-on", 4),
          ("mdi", 1),
          ("mdix", 2),
          ("none", 3))
    )


_CiscoEsPortMdiMdix_Type.__name__ = "Integer32"
_CiscoEsPortMdiMdix_Object = MibTableColumn
ciscoEsPortMdiMdix = _CiscoEsPortMdiMdix_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 31),
    _CiscoEsPortMdiMdix_Type()
)
ciscoEsPortMdiMdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortMdiMdix.setStatus("mandatory")
_CiscoEsPortHashOverflows_Type = Counter32
_CiscoEsPortHashOverflows_Object = MibTableColumn
ciscoEsPortHashOverflows = _CiscoEsPortHashOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 32),
    _CiscoEsPortHashOverflows_Type()
)
ciscoEsPortHashOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortHashOverflows.setStatus("mandatory")
_CiscoEsPortTableOverflows_Type = Counter32
_CiscoEsPortTableOverflows_Object = MibTableColumn
ciscoEsPortTableOverflows = _CiscoEsPortTableOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 33),
    _CiscoEsPortTableOverflows_Type()
)
ciscoEsPortTableOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortTableOverflows.setStatus("mandatory")


class _CiscoEsPortAddrAgingTime_Type(Integer32):
    """Custom type ciscoEsPortAddrAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CiscoEsPortAddrAgingTime_Type.__name__ = "Integer32"
_CiscoEsPortAddrAgingTime_Object = MibTableColumn
ciscoEsPortAddrAgingTime = _CiscoEsPortAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 34),
    _CiscoEsPortAddrAgingTime_Type()
)
ciscoEsPortAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortAddrAgingTime.setStatus("mandatory")


class _CiscoEsPortDemandAgingLevel_Type(Integer32):
    """Custom type ciscoEsPortDemandAgingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_CiscoEsPortDemandAgingLevel_Type.__name__ = "Integer32"
_CiscoEsPortDemandAgingLevel_Object = MibTableColumn
ciscoEsPortDemandAgingLevel = _CiscoEsPortDemandAgingLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 35),
    _CiscoEsPortDemandAgingLevel_Type()
)
ciscoEsPortDemandAgingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortDemandAgingLevel.setStatus("mandatory")


class _CiscoEsPortCfgMode_Type(Integer32):
    """Custom type ciscoEsPortCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("cutthru", 2),
          ("ieee8021d", 1))
    )


_CiscoEsPortCfgMode_Type.__name__ = "Integer32"
_CiscoEsPortCfgMode_Object = MibTableColumn
ciscoEsPortCfgMode = _CiscoEsPortCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 36),
    _CiscoEsPortCfgMode_Type()
)
ciscoEsPortCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortCfgMode.setStatus("mandatory")


class _CiscoEsPortActiveMode_Type(Integer32):
    """Custom type ciscoEsPortActiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cutthru", 2),
          ("ieee8021d", 1),
          ("unknown", 3))
    )


_CiscoEsPortActiveMode_Type.__name__ = "Integer32"
_CiscoEsPortActiveMode_Object = MibTableColumn
ciscoEsPortActiveMode = _CiscoEsPortActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 37),
    _CiscoEsPortActiveMode_Type()
)
ciscoEsPortActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortActiveMode.setStatus("mandatory")


class _CiscoEsPortErrThreshold_Type(Integer32):
    """Custom type ciscoEsPortErrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CiscoEsPortErrThreshold_Type.__name__ = "Integer32"
_CiscoEsPortErrThreshold_Object = MibTableColumn
ciscoEsPortErrThreshold = _CiscoEsPortErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 38),
    _CiscoEsPortErrThreshold_Type()
)
ciscoEsPortErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortErrThreshold.setStatus("mandatory")


class _CiscoEsPortLearningState_Type(Integer32):
    """Custom type ciscoEsPortLearningState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disableDstnLearning", 3),
          ("disableLearning", 4),
          ("disableSrcLearning", 2),
          ("normal", 1))
    )


_CiscoEsPortLearningState_Type.__name__ = "Integer32"
_CiscoEsPortLearningState_Object = MibTableColumn
ciscoEsPortLearningState = _CiscoEsPortLearningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 39),
    _CiscoEsPortLearningState_Type()
)
ciscoEsPortLearningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortLearningState.setStatus("mandatory")


class _CiscoEsPortRuntlessMode_Type(Integer32):
    """Custom type ciscoEsPortRuntlessMode based on Integer32"""
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


_CiscoEsPortRuntlessMode_Type.__name__ = "Integer32"
_CiscoEsPortRuntlessMode_Object = MibTableColumn
ciscoEsPortRuntlessMode = _CiscoEsPortRuntlessMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 40),
    _CiscoEsPortRuntlessMode_Type()
)
ciscoEsPortRuntlessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortRuntlessMode.setStatus("mandatory")


class _CiscoEsPortType_Type(Integer32):
    """Custom type ciscoEsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("type-100BaseFx", 4),
          ("type-100BaseT", 3),
          ("type-100VG-Fx", 10),
          ("type-100VG-Tx", 11),
          ("type-10Base2", 6),
          ("type-10BaseFL", 7),
          ("type-10BaseT", 1),
          ("type-10BaseT-4", 5),
          ("type-ATM155", 8),
          ("type-ISL-FX", 12),
          ("type-ISL-TX", 13),
          ("type-R2503", 14),
          ("type-StkPort", 2),
          ("unknown", 9))
    )


_CiscoEsPortType_Type.__name__ = "Integer32"
_CiscoEsPortType_Object = MibTableColumn
ciscoEsPortType = _CiscoEsPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 41),
    _CiscoEsPortType_Type()
)
ciscoEsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortType.setStatus("mandatory")


class _CiscoEsPortCDPTimeToLive_Type(Integer32):
    """Custom type ciscoEsPortCDPTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoEsPortCDPTimeToLive_Type.__name__ = "Integer32"
_CiscoEsPortCDPTimeToLive_Object = MibTableColumn
ciscoEsPortCDPTimeToLive = _CiscoEsPortCDPTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 42),
    _CiscoEsPortCDPTimeToLive_Type()
)
ciscoEsPortCDPTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortCDPTimeToLive.setStatus("mandatory")


class _CiscoEsPortFastPort_Type(Integer32):
    """Custom type ciscoEsPortFastPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CiscoEsPortFastPort_Type.__name__ = "Integer32"
_CiscoEsPortFastPort_Object = MibTableColumn
ciscoEsPortFastPort = _CiscoEsPortFastPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 43),
    _CiscoEsPortFastPort_Type()
)
ciscoEsPortFastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortFastPort.setStatus("mandatory")


class _CiscoEsPortISLOperStatus_Type(Integer32):
    """Custom type ciscoEsPortISLOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-trunking", 2),
          ("trunking", 1))
    )


_CiscoEsPortISLOperStatus_Type.__name__ = "Integer32"
_CiscoEsPortISLOperStatus_Object = MibTableColumn
ciscoEsPortISLOperStatus = _CiscoEsPortISLOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 44),
    _CiscoEsPortISLOperStatus_Type()
)
ciscoEsPortISLOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortISLOperStatus.setStatus("mandatory")


class _CiscoEsPortISLAdminStatus_Type(Integer32):
    """Custom type ciscoEsPortISLAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("desirable", 3),
          ("off", 2),
          ("on", 1))
    )


_CiscoEsPortISLAdminStatus_Type.__name__ = "Integer32"
_CiscoEsPortISLAdminStatus_Object = MibTableColumn
ciscoEsPortISLAdminStatus = _CiscoEsPortISLAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 1, 1, 45),
    _CiscoEsPortISLAdminStatus_Type()
)
ciscoEsPortISLAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsPortISLAdminStatus.setStatus("mandatory")
_CiscoEsOptPortStaTable_Object = MibTable
ciscoEsOptPortStaTable = _CiscoEsOptPortStaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 2)
)
if mibBuilder.loadTexts:
    ciscoEsOptPortStaTable.setStatus("mandatory")
_CiscoEsOptPortStaEntry_Object = MibTableRow
ciscoEsOptPortStaEntry = _CiscoEsOptPortStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 2, 1)
)
ciscoEsOptPortStaEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsPortSwitchNumber"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsPortNumber"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsOptPortStaPos"),
)
if mibBuilder.loadTexts:
    ciscoEsOptPortStaEntry.setStatus("mandatory")


class _CiscoEsOptPortStaPos_Type(Integer32):
    """Custom type ciscoEsOptPortStaPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoEsOptPortStaPos_Type.__name__ = "Integer32"
_CiscoEsOptPortStaPos_Object = MibTableColumn
ciscoEsOptPortStaPos = _CiscoEsOptPortStaPos_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 2, 1, 1),
    _CiscoEsOptPortStaPos_Type()
)
ciscoEsOptPortStaPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsOptPortStaPos.setStatus("mandatory")
_CiscoEsOptPortStaVal_Type = OctetString
_CiscoEsOptPortStaVal_Object = MibTableColumn
ciscoEsOptPortStaVal = _CiscoEsOptPortStaVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 2, 1, 2),
    _CiscoEsOptPortStaVal_Type()
)
ciscoEsOptPortStaVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsOptPortStaVal.setStatus("mandatory")
_CiscoEsPortStnTable_Object = MibTable
ciscoEsPortStnTable = _CiscoEsPortStnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3)
)
if mibBuilder.loadTexts:
    ciscoEsPortStnTable.setStatus("mandatory")
_CiscoEsPortStnEntry_Object = MibTableRow
ciscoEsPortStnEntry = _CiscoEsPortStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3, 1)
)
ciscoEsPortStnEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsPortStnSwitchNumber"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsPortStnPortNum"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsPortStnAddress"),
)
if mibBuilder.loadTexts:
    ciscoEsPortStnEntry.setStatus("mandatory")


class _CiscoEsPortStnSwitchNumber_Type(Integer32):
    """Custom type ciscoEsPortStnSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsPortStnSwitchNumber_Type.__name__ = "Integer32"
_CiscoEsPortStnSwitchNumber_Object = MibTableColumn
ciscoEsPortStnSwitchNumber = _CiscoEsPortStnSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3, 1, 1),
    _CiscoEsPortStnSwitchNumber_Type()
)
ciscoEsPortStnSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortStnSwitchNumber.setStatus("mandatory")
_CiscoEsPortStnPortNum_Type = Integer32
_CiscoEsPortStnPortNum_Object = MibTableColumn
ciscoEsPortStnPortNum = _CiscoEsPortStnPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3, 1, 2),
    _CiscoEsPortStnPortNum_Type()
)
ciscoEsPortStnPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortStnPortNum.setStatus("mandatory")
_CiscoEsPortStnAddress_Type = MacAddr
_CiscoEsPortStnAddress_Object = MibTableColumn
ciscoEsPortStnAddress = _CiscoEsPortStnAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3, 1, 3),
    _CiscoEsPortStnAddress_Type()
)
ciscoEsPortStnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortStnAddress.setStatus("mandatory")


class _CiscoEsPortStnLocation_Type(Integer32):
    """Custom type ciscoEsPortStnLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_CiscoEsPortStnLocation_Type.__name__ = "Integer32"
_CiscoEsPortStnLocation_Object = MibTableColumn
ciscoEsPortStnLocation = _CiscoEsPortStnLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3, 1, 4),
    _CiscoEsPortStnLocation_Type()
)
ciscoEsPortStnLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortStnLocation.setStatus("mandatory")
_CiscoEsPortStnSrcFrames_Type = Counter32
_CiscoEsPortStnSrcFrames_Object = MibTableColumn
ciscoEsPortStnSrcFrames = _CiscoEsPortStnSrcFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3, 1, 5),
    _CiscoEsPortStnSrcFrames_Type()
)
ciscoEsPortStnSrcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortStnSrcFrames.setStatus("mandatory")
_CiscoEsPortStnSrcBytes_Type = Counter32
_CiscoEsPortStnSrcBytes_Object = MibTableColumn
ciscoEsPortStnSrcBytes = _CiscoEsPortStnSrcBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3, 1, 6),
    _CiscoEsPortStnSrcBytes_Type()
)
ciscoEsPortStnSrcBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortStnSrcBytes.setStatus("mandatory")
_CiscoEsPortStnDestnFrames_Type = Counter32
_CiscoEsPortStnDestnFrames_Object = MibTableColumn
ciscoEsPortStnDestnFrames = _CiscoEsPortStnDestnFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3, 1, 7),
    _CiscoEsPortStnDestnFrames_Type()
)
ciscoEsPortStnDestnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortStnDestnFrames.setStatus("mandatory")
_CiscoEsPortStnDestnBytes_Type = Counter32
_CiscoEsPortStnDestnBytes_Object = MibTableColumn
ciscoEsPortStnDestnBytes = _CiscoEsPortStnDestnBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3, 1, 8),
    _CiscoEsPortStnDestnBytes_Type()
)
ciscoEsPortStnDestnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortStnDestnBytes.setStatus("mandatory")


class _CiscoEsPortStnPortOfExit_Type(OctetString):
    """Custom type ciscoEsPortStnPortOfExit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoEsPortStnPortOfExit_Type.__name__ = "OctetString"
_CiscoEsPortStnPortOfExit_Object = MibTableColumn
ciscoEsPortStnPortOfExit = _CiscoEsPortStnPortOfExit_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 3, 1, 9),
    _CiscoEsPortStnPortOfExit_Type()
)
ciscoEsPortStnPortOfExit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsPortStnPortOfExit.setStatus("mandatory")
_CiscoEsDmns_ObjectIdentity = ObjectIdentity
ciscoEsDmns = _CiscoEsDmns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5)
)
_CiscoEsEChannel_ObjectIdentity = ObjectIdentity
ciscoEsEChannel = _CiscoEsEChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 6)
)
_CiscoEsECTable_Object = MibTable
ciscoEsECTable = _CiscoEsECTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 6, 1)
)
if mibBuilder.loadTexts:
    ciscoEsECTable.setStatus("mandatory")
_CiscoEsECEntry_Object = MibTableRow
ciscoEsECEntry = _CiscoEsECEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 6, 1, 1)
)
ciscoEsECEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsECSwitchNumber"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsECNumber"),
)
if mibBuilder.loadTexts:
    ciscoEsECEntry.setStatus("mandatory")


class _CiscoEsECSwitchNumber_Type(Integer32):
    """Custom type ciscoEsECSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsECSwitchNumber_Type.__name__ = "Integer32"
_CiscoEsECSwitchNumber_Object = MibTableColumn
ciscoEsECSwitchNumber = _CiscoEsECSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 6, 1, 1, 1),
    _CiscoEsECSwitchNumber_Type()
)
ciscoEsECSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsECSwitchNumber.setStatus("mandatory")


class _CiscoEsECNumber_Type(Integer32):
    """Custom type ciscoEsECNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsECNumber_Type.__name__ = "Integer32"
_CiscoEsECNumber_Object = MibTableColumn
ciscoEsECNumber = _CiscoEsECNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 6, 1, 1, 2),
    _CiscoEsECNumber_Type()
)
ciscoEsECNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsECNumber.setStatus("mandatory")


class _CiscoEsECPorts_Type(OctetString):
    """Custom type ciscoEsECPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoEsECPorts_Type.__name__ = "OctetString"
_CiscoEsECPorts_Object = MibTableColumn
ciscoEsECPorts = _CiscoEsECPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 6, 1, 1, 3),
    _CiscoEsECPorts_Type()
)
ciscoEsECPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsECPorts.setStatus("mandatory")
_CiscoEsFilter_ObjectIdentity = ObjectIdentity
ciscoEsFilter = _CiscoEsFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7)
)
_CiscoEsFilterTable_Object = MibTable
ciscoEsFilterTable = _CiscoEsFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7, 1)
)
if mibBuilder.loadTexts:
    ciscoEsFilterTable.setStatus("mandatory")
_CiscoEsFilterEntry_Object = MibTableRow
ciscoEsFilterEntry = _CiscoEsFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7, 1, 1)
)
ciscoEsFilterEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsFilterSwitchNumber"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsFilterStationAddress"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsFilterType"),
)
if mibBuilder.loadTexts:
    ciscoEsFilterEntry.setStatus("mandatory")


class _CiscoEsFilterSwitchNumber_Type(Integer32):
    """Custom type ciscoEsFilterSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsFilterSwitchNumber_Type.__name__ = "Integer32"
_CiscoEsFilterSwitchNumber_Object = MibTableColumn
ciscoEsFilterSwitchNumber = _CiscoEsFilterSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7, 1, 1, 1),
    _CiscoEsFilterSwitchNumber_Type()
)
ciscoEsFilterSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsFilterSwitchNumber.setStatus("mandatory")
_CiscoEsFilterStationAddress_Type = MacAddr
_CiscoEsFilterStationAddress_Object = MibTableColumn
ciscoEsFilterStationAddress = _CiscoEsFilterStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7, 1, 1, 2),
    _CiscoEsFilterStationAddress_Type()
)
ciscoEsFilterStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsFilterStationAddress.setStatus("mandatory")


class _CiscoEsFilterType_Type(Integer32):
    """Custom type ciscoEsFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination-filter", 2),
          ("source-filter", 1))
    )


_CiscoEsFilterType_Type.__name__ = "Integer32"
_CiscoEsFilterType_Object = MibTableColumn
ciscoEsFilterType = _CiscoEsFilterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7, 1, 1, 3),
    _CiscoEsFilterType_Type()
)
ciscoEsFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsFilterType.setStatus("mandatory")


class _CiscoEsFilterPorts_Type(OctetString):
    """Custom type ciscoEsFilterPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoEsFilterPorts_Type.__name__ = "OctetString"
_CiscoEsFilterPorts_Object = MibTableColumn
ciscoEsFilterPorts = _CiscoEsFilterPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7, 1, 1, 4),
    _CiscoEsFilterPorts_Type()
)
ciscoEsFilterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsFilterPorts.setStatus("mandatory")


class _CiscoEsFilterMask_Type(OctetString):
    """Custom type ciscoEsFilterMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoEsFilterMask_Type.__name__ = "OctetString"
_CiscoEsFilterMask_Object = MibTableColumn
ciscoEsFilterMask = _CiscoEsFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7, 1, 1, 5),
    _CiscoEsFilterMask_Type()
)
ciscoEsFilterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsFilterMask.setStatus("mandatory")


class _CiscoEsFilterRemoteSwitch_Type(Integer32):
    """Custom type ciscoEsFilterRemoteSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CiscoEsFilterRemoteSwitch_Type.__name__ = "Integer32"
_CiscoEsFilterRemoteSwitch_Object = MibTableColumn
ciscoEsFilterRemoteSwitch = _CiscoEsFilterRemoteSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7, 1, 1, 6),
    _CiscoEsFilterRemoteSwitch_Type()
)
ciscoEsFilterRemoteSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsFilterRemoteSwitch.setStatus("mandatory")


class _CiscoEsFilterRemotePort_Type(Integer32):
    """Custom type ciscoEsFilterRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_CiscoEsFilterRemotePort_Type.__name__ = "Integer32"
_CiscoEsFilterRemotePort_Object = MibTableColumn
ciscoEsFilterRemotePort = _CiscoEsFilterRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7, 1, 1, 7),
    _CiscoEsFilterRemotePort_Type()
)
ciscoEsFilterRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsFilterRemotePort.setStatus("mandatory")


class _CiscoEsFilterStatus_Type(Integer32):
    """Custom type ciscoEsFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_CiscoEsFilterStatus_Type.__name__ = "Integer32"
_CiscoEsFilterStatus_Object = MibTableColumn
ciscoEsFilterStatus = _CiscoEsFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 7, 1, 1, 8),
    _CiscoEsFilterStatus_Type()
)
ciscoEsFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsFilterStatus.setStatus("mandatory")
_CiscoEsVLANs_ObjectIdentity = ObjectIdentity
ciscoEsVLANs = _CiscoEsVLANs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8)
)
_CiscoEsVLANPortTable_Object = MibTable
ciscoEsVLANPortTable = _CiscoEsVLANPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 1)
)
if mibBuilder.loadTexts:
    ciscoEsVLANPortTable.setStatus("mandatory")
_CiscoEsVLANPortEntry_Object = MibTableRow
ciscoEsVLANPortEntry = _CiscoEsVLANPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 1, 1)
)
ciscoEsVLANPortEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsVLANPortVLANNumber"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsVLANPortSwitchNumber"),
)
if mibBuilder.loadTexts:
    ciscoEsVLANPortEntry.setStatus("mandatory")


class _CiscoEsVLANPortVLANNumber_Type(Integer32):
    """Custom type ciscoEsVLANPortVLANNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CiscoEsVLANPortVLANNumber_Type.__name__ = "Integer32"
_CiscoEsVLANPortVLANNumber_Object = MibTableColumn
ciscoEsVLANPortVLANNumber = _CiscoEsVLANPortVLANNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 1, 1, 1),
    _CiscoEsVLANPortVLANNumber_Type()
)
ciscoEsVLANPortVLANNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANPortVLANNumber.setStatus("mandatory")


class _CiscoEsVLANPortSwitchNumber_Type(Integer32):
    """Custom type ciscoEsVLANPortSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsVLANPortSwitchNumber_Type.__name__ = "Integer32"
_CiscoEsVLANPortSwitchNumber_Object = MibTableColumn
ciscoEsVLANPortSwitchNumber = _CiscoEsVLANPortSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 1, 1, 2),
    _CiscoEsVLANPortSwitchNumber_Type()
)
ciscoEsVLANPortSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANPortSwitchNumber.setStatus("mandatory")


class _CiscoEsVLANPortPorts_Type(OctetString):
    """Custom type ciscoEsVLANPortPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoEsVLANPortPorts_Type.__name__ = "OctetString"
_CiscoEsVLANPortPorts_Object = MibTableColumn
ciscoEsVLANPortPorts = _CiscoEsVLANPortPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 1, 1, 3),
    _CiscoEsVLANPortPorts_Type()
)
ciscoEsVLANPortPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANPortPorts.setStatus("mandatory")
_CiscoEsVLANInfoTable_Object = MibTable
ciscoEsVLANInfoTable = _CiscoEsVLANInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2)
)
if mibBuilder.loadTexts:
    ciscoEsVLANInfoTable.setStatus("mandatory")
_CiscoEsVLANInfoEntry_Object = MibTableRow
ciscoEsVLANInfoEntry = _CiscoEsVLANInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1)
)
ciscoEsVLANInfoEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsVLANInfoVLANNumber"),
)
if mibBuilder.loadTexts:
    ciscoEsVLANInfoEntry.setStatus("mandatory")


class _CiscoEsVLANInfoVLANNumber_Type(Integer32):
    """Custom type ciscoEsVLANInfoVLANNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CiscoEsVLANInfoVLANNumber_Type.__name__ = "Integer32"
_CiscoEsVLANInfoVLANNumber_Object = MibTableColumn
ciscoEsVLANInfoVLANNumber = _CiscoEsVLANInfoVLANNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 1),
    _CiscoEsVLANInfoVLANNumber_Type()
)
ciscoEsVLANInfoVLANNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoVLANNumber.setStatus("mandatory")


class _CiscoEsVLANInfoState_Type(Integer32):
    """Custom type ciscoEsVLANInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CiscoEsVLANInfoState_Type.__name__ = "Integer32"
_CiscoEsVLANInfoState_Object = MibTableColumn
ciscoEsVLANInfoState = _CiscoEsVLANInfoState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 2),
    _CiscoEsVLANInfoState_Type()
)
ciscoEsVLANInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoState.setStatus("mandatory")


class _CiscoEsVLANInfoName_Type(DisplayString):
    """Custom type ciscoEsVLANInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CiscoEsVLANInfoName_Type.__name__ = "DisplayString"
_CiscoEsVLANInfoName_Object = MibTableColumn
ciscoEsVLANInfoName = _CiscoEsVLANInfoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 3),
    _CiscoEsVLANInfoName_Type()
)
ciscoEsVLANInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoName.setStatus("mandatory")
_CiscoEsVLANInfoBaseAddr_Type = MacAddr
_CiscoEsVLANInfoBaseAddr_Object = MibTableColumn
ciscoEsVLANInfoBaseAddr = _CiscoEsVLANInfoBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 4),
    _CiscoEsVLANInfoBaseAddr_Type()
)
ciscoEsVLANInfoBaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoBaseAddr.setStatus("mandatory")
_CiscoEsVLANInfoIfIndex_Type = Integer32
_CiscoEsVLANInfoIfIndex_Object = MibTableColumn
ciscoEsVLANInfoIfIndex = _CiscoEsVLANInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 5),
    _CiscoEsVLANInfoIfIndex_Type()
)
ciscoEsVLANInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoIfIndex.setStatus("mandatory")


class _CiscoEsVLANInfoIpState_Type(Integer32):
    """Custom type ciscoEsVLANInfoIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always-bootp", 3),
          ("auto-bootp", 2),
          ("disabled", 1))
    )


_CiscoEsVLANInfoIpState_Type.__name__ = "Integer32"
_CiscoEsVLANInfoIpState_Object = MibTableColumn
ciscoEsVLANInfoIpState = _CiscoEsVLANInfoIpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 6),
    _CiscoEsVLANInfoIpState_Type()
)
ciscoEsVLANInfoIpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoIpState.setStatus("mandatory")
_CiscoEsVLANInfoIpAddress_Type = IpAddress
_CiscoEsVLANInfoIpAddress_Object = MibTableColumn
ciscoEsVLANInfoIpAddress = _CiscoEsVLANInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 7),
    _CiscoEsVLANInfoIpAddress_Type()
)
ciscoEsVLANInfoIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoIpAddress.setStatus("mandatory")
_CiscoEsVLANInfoIpSubnetMask_Type = IpAddress
_CiscoEsVLANInfoIpSubnetMask_Object = MibTableColumn
ciscoEsVLANInfoIpSubnetMask = _CiscoEsVLANInfoIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 8),
    _CiscoEsVLANInfoIpSubnetMask_Type()
)
ciscoEsVLANInfoIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoIpSubnetMask.setStatus("mandatory")
_CiscoEsVLANInfoIpDefaultGateway_Type = IpAddress
_CiscoEsVLANInfoIpDefaultGateway_Object = MibTableColumn
ciscoEsVLANInfoIpDefaultGateway = _CiscoEsVLANInfoIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 9),
    _CiscoEsVLANInfoIpDefaultGateway_Type()
)
ciscoEsVLANInfoIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoIpDefaultGateway.setStatus("mandatory")


class _CiscoEsVLANInfoStp_Type(Integer32):
    """Custom type ciscoEsVLANInfoStp based on Integer32"""
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


_CiscoEsVLANInfoStp_Type.__name__ = "Integer32"
_CiscoEsVLANInfoStp_Object = MibTableColumn
ciscoEsVLANInfoStp = _CiscoEsVLANInfoStp_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 10),
    _CiscoEsVLANInfoStp_Type()
)
ciscoEsVLANInfoStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoStp.setStatus("mandatory")
_CiscoEsVLANInfoNumStations_Type = Gauge32
_CiscoEsVLANInfoNumStations_Object = MibTableColumn
ciscoEsVLANInfoNumStations = _CiscoEsVLANInfoNumStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 11),
    _CiscoEsVLANInfoNumStations_Type()
)
ciscoEsVLANInfoNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoNumStations.setStatus("mandatory")
_CiscoEsVLANInfoMaxStations_Type = Integer32
_CiscoEsVLANInfoMaxStations_Object = MibTableColumn
ciscoEsVLANInfoMaxStations = _CiscoEsVLANInfoMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 2, 1, 12),
    _CiscoEsVLANInfoMaxStations_Type()
)
ciscoEsVLANInfoMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANInfoMaxStations.setStatus("mandatory")
_CiscoEsVLANStpTable_Object = MibTable
ciscoEsVLANStpTable = _CiscoEsVLANStpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3)
)
if mibBuilder.loadTexts:
    ciscoEsVLANStpTable.setStatus("mandatory")
_CiscoEsVLANStpEntry_Object = MibTableRow
ciscoEsVLANStpEntry = _CiscoEsVLANStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1)
)
ciscoEsVLANStpEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsVLANStpVLANIndex"),
)
if mibBuilder.loadTexts:
    ciscoEsVLANStpEntry.setStatus("mandatory")


class _CiscoEsVLANStpVLANIndex_Type(Integer32):
    """Custom type ciscoEsVLANStpVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CiscoEsVLANStpVLANIndex_Type.__name__ = "Integer32"
_CiscoEsVLANStpVLANIndex_Object = MibTableColumn
ciscoEsVLANStpVLANIndex = _CiscoEsVLANStpVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 1),
    _CiscoEsVLANStpVLANIndex_Type()
)
ciscoEsVLANStpVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStpVLANIndex.setStatus("mandatory")


class _CiscoEsVLANStpPriority_Type(Integer32):
    """Custom type ciscoEsVLANStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoEsVLANStpPriority_Type.__name__ = "Integer32"
_CiscoEsVLANStpPriority_Object = MibTableColumn
ciscoEsVLANStpPriority = _CiscoEsVLANStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 2),
    _CiscoEsVLANStpPriority_Type()
)
ciscoEsVLANStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANStpPriority.setStatus("mandatory")
_CiscoEsVLANStpTimeSinceTopologyChange_Type = TimeTicks
_CiscoEsVLANStpTimeSinceTopologyChange_Object = MibTableColumn
ciscoEsVLANStpTimeSinceTopologyChange = _CiscoEsVLANStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 3),
    _CiscoEsVLANStpTimeSinceTopologyChange_Type()
)
ciscoEsVLANStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStpTimeSinceTopologyChange.setStatus("mandatory")
_CiscoEsVLANStpTopChanges_Type = Counter32
_CiscoEsVLANStpTopChanges_Object = MibTableColumn
ciscoEsVLANStpTopChanges = _CiscoEsVLANStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 4),
    _CiscoEsVLANStpTopChanges_Type()
)
ciscoEsVLANStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStpTopChanges.setStatus("mandatory")
_CiscoEsVLANStpDesignatedRoot_Type = BridgeId
_CiscoEsVLANStpDesignatedRoot_Object = MibTableColumn
ciscoEsVLANStpDesignatedRoot = _CiscoEsVLANStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 5),
    _CiscoEsVLANStpDesignatedRoot_Type()
)
ciscoEsVLANStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStpDesignatedRoot.setStatus("mandatory")
_CiscoEsVLANStpRootCost_Type = Integer32
_CiscoEsVLANStpRootCost_Object = MibTableColumn
ciscoEsVLANStpRootCost = _CiscoEsVLANStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 6),
    _CiscoEsVLANStpRootCost_Type()
)
ciscoEsVLANStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStpRootCost.setStatus("mandatory")
_CiscoEsVLANStpRootPort_Type = Integer32
_CiscoEsVLANStpRootPort_Object = MibTableColumn
ciscoEsVLANStpRootPort = _CiscoEsVLANStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 7),
    _CiscoEsVLANStpRootPort_Type()
)
ciscoEsVLANStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStpRootPort.setStatus("mandatory")
_CiscoEsVLANStpMaxAge_Type = Integer32
_CiscoEsVLANStpMaxAge_Object = MibTableColumn
ciscoEsVLANStpMaxAge = _CiscoEsVLANStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 8),
    _CiscoEsVLANStpMaxAge_Type()
)
ciscoEsVLANStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStpMaxAge.setStatus("mandatory")
_CiscoEsVLANStpHelloTime_Type = Integer32
_CiscoEsVLANStpHelloTime_Object = MibTableColumn
ciscoEsVLANStpHelloTime = _CiscoEsVLANStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 9),
    _CiscoEsVLANStpHelloTime_Type()
)
ciscoEsVLANStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStpHelloTime.setStatus("mandatory")
_CiscoEsVLANStpHoldTime_Type = Integer32
_CiscoEsVLANStpHoldTime_Object = MibTableColumn
ciscoEsVLANStpHoldTime = _CiscoEsVLANStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 10),
    _CiscoEsVLANStpHoldTime_Type()
)
ciscoEsVLANStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStpHoldTime.setStatus("mandatory")
_CiscoEsVLANStpForwardDelay_Type = Integer32
_CiscoEsVLANStpForwardDelay_Object = MibTableColumn
ciscoEsVLANStpForwardDelay = _CiscoEsVLANStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 11),
    _CiscoEsVLANStpForwardDelay_Type()
)
ciscoEsVLANStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStpForwardDelay.setStatus("mandatory")


class _CiscoEsVLANStpBridgeMaxAge_Type(Integer32):
    """Custom type ciscoEsVLANStpBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_CiscoEsVLANStpBridgeMaxAge_Type.__name__ = "Integer32"
_CiscoEsVLANStpBridgeMaxAge_Object = MibTableColumn
ciscoEsVLANStpBridgeMaxAge = _CiscoEsVLANStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 12),
    _CiscoEsVLANStpBridgeMaxAge_Type()
)
ciscoEsVLANStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANStpBridgeMaxAge.setStatus("mandatory")


class _CiscoEsVLANStpBridgeHelloTime_Type(Integer32):
    """Custom type ciscoEsVLANStpBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CiscoEsVLANStpBridgeHelloTime_Type.__name__ = "Integer32"
_CiscoEsVLANStpBridgeHelloTime_Object = MibTableColumn
ciscoEsVLANStpBridgeHelloTime = _CiscoEsVLANStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 13),
    _CiscoEsVLANStpBridgeHelloTime_Type()
)
ciscoEsVLANStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANStpBridgeHelloTime.setStatus("mandatory")


class _CiscoEsVLANStpBridgeForwardDelay_Type(Integer32):
    """Custom type ciscoEsVLANStpBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_CiscoEsVLANStpBridgeForwardDelay_Type.__name__ = "Integer32"
_CiscoEsVLANStpBridgeForwardDelay_Object = MibTableColumn
ciscoEsVLANStpBridgeForwardDelay = _CiscoEsVLANStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 3, 1, 14),
    _CiscoEsVLANStpBridgeForwardDelay_Type()
)
ciscoEsVLANStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsVLANStpBridgeForwardDelay.setStatus("mandatory")
_CiscoEsVLANStationTable_Object = MibTable
ciscoEsVLANStationTable = _CiscoEsVLANStationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 4)
)
if mibBuilder.loadTexts:
    ciscoEsVLANStationTable.setStatus("mandatory")
_CiscoEsVLANStationEntry_Object = MibTableRow
ciscoEsVLANStationEntry = _CiscoEsVLANStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 4, 1)
)
ciscoEsVLANStationEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsVLANStationVLANIndex"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsVLANStationBoxNum"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsVLANStationAddress"),
)
if mibBuilder.loadTexts:
    ciscoEsVLANStationEntry.setStatus("mandatory")


class _CiscoEsVLANStationVLANIndex_Type(Integer32):
    """Custom type ciscoEsVLANStationVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CiscoEsVLANStationVLANIndex_Type.__name__ = "Integer32"
_CiscoEsVLANStationVLANIndex_Object = MibTableColumn
ciscoEsVLANStationVLANIndex = _CiscoEsVLANStationVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 4, 1, 1),
    _CiscoEsVLANStationVLANIndex_Type()
)
ciscoEsVLANStationVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStationVLANIndex.setStatus("mandatory")


class _CiscoEsVLANStationBoxNum_Type(Integer32):
    """Custom type ciscoEsVLANStationBoxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsVLANStationBoxNum_Type.__name__ = "Integer32"
_CiscoEsVLANStationBoxNum_Object = MibTableColumn
ciscoEsVLANStationBoxNum = _CiscoEsVLANStationBoxNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 4, 1, 2),
    _CiscoEsVLANStationBoxNum_Type()
)
ciscoEsVLANStationBoxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStationBoxNum.setStatus("mandatory")


class _CiscoEsVLANStationAddress_Type(OctetString):
    """Custom type ciscoEsVLANStationAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CiscoEsVLANStationAddress_Type.__name__ = "OctetString"
_CiscoEsVLANStationAddress_Object = MibTableColumn
ciscoEsVLANStationAddress = _CiscoEsVLANStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 4, 1, 3),
    _CiscoEsVLANStationAddress_Type()
)
ciscoEsVLANStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStationAddress.setStatus("mandatory")
_CiscoEsVLANStationPort_Type = Integer32
_CiscoEsVLANStationPort_Object = MibTableColumn
ciscoEsVLANStationPort = _CiscoEsVLANStationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 4, 1, 4),
    _CiscoEsVLANStationPort_Type()
)
ciscoEsVLANStationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStationPort.setStatus("mandatory")


class _CiscoEsVLANStationTraffic_Type(OctetString):
    """Custom type ciscoEsVLANStationTraffic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoEsVLANStationTraffic_Type.__name__ = "OctetString"
_CiscoEsVLANStationTraffic_Object = MibTableColumn
ciscoEsVLANStationTraffic = _CiscoEsVLANStationTraffic_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 4, 1, 5),
    _CiscoEsVLANStationTraffic_Type()
)
ciscoEsVLANStationTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsVLANStationTraffic.setStatus("mandatory")
_CiscoEsOptVLANStaTable_Object = MibTable
ciscoEsOptVLANStaTable = _CiscoEsOptVLANStaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 5)
)
if mibBuilder.loadTexts:
    ciscoEsOptVLANStaTable.setStatus("mandatory")
_CiscoEsOptVLANStaEntry_Object = MibTableRow
ciscoEsOptVLANStaEntry = _CiscoEsOptVLANStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 5, 1)
)
ciscoEsOptVLANStaEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsVLANStationVLANIndex"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsVLANStationBoxNum"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsOptVLANStaPos"),
)
if mibBuilder.loadTexts:
    ciscoEsOptVLANStaEntry.setStatus("mandatory")


class _CiscoEsOptVLANStaPos_Type(Integer32):
    """Custom type ciscoEsOptVLANStaPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoEsOptVLANStaPos_Type.__name__ = "Integer32"
_CiscoEsOptVLANStaPos_Object = MibTableColumn
ciscoEsOptVLANStaPos = _CiscoEsOptVLANStaPos_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 5, 1, 1),
    _CiscoEsOptVLANStaPos_Type()
)
ciscoEsOptVLANStaPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsOptVLANStaPos.setStatus("mandatory")
_CiscoEsOptVLANStaVal_Type = OctetString
_CiscoEsOptVLANStaVal_Object = MibTableColumn
ciscoEsOptVLANStaVal = _CiscoEsOptVLANStaVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 5, 1, 2),
    _CiscoEsOptVLANStaVal_Type()
)
ciscoEsOptVLANStaVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsOptVLANStaVal.setStatus("mandatory")


class _CiscoEsTransitedConfiguredVLANs_Type(OctetString):
    """Custom type ciscoEsTransitedConfiguredVLANs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CiscoEsTransitedConfiguredVLANs_Type.__name__ = "OctetString"
_CiscoEsTransitedConfiguredVLANs_Object = MibScalar
ciscoEsTransitedConfiguredVLANs = _CiscoEsTransitedConfiguredVLANs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 6),
    _CiscoEsTransitedConfiguredVLANs_Type()
)
ciscoEsTransitedConfiguredVLANs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsTransitedConfiguredVLANs.setStatus("mandatory")


class _CiscoEsTransitedVLANs_Type(OctetString):
    """Custom type ciscoEsTransitedVLANs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CiscoEsTransitedVLANs_Type.__name__ = "OctetString"
_CiscoEsTransitedVLANs_Object = MibScalar
ciscoEsTransitedVLANs = _CiscoEsTransitedVLANs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 7),
    _CiscoEsTransitedVLANs_Type()
)
ciscoEsTransitedVLANs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsTransitedVLANs.setStatus("mandatory")
_CiscoEsRouter_ObjectIdentity = ObjectIdentity
ciscoEsRouter = _CiscoEsRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 9)
)
_CiscoEsRouterTable_Object = MibTable
ciscoEsRouterTable = _CiscoEsRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 9, 1)
)
if mibBuilder.loadTexts:
    ciscoEsRouterTable.setStatus("mandatory")
_CiscoEsRouterEntry_Object = MibTableRow
ciscoEsRouterEntry = _CiscoEsRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 9, 1, 1)
)
ciscoEsRouterEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB", "ciscoEsRouterBox"),
    (0, "CISCO-ES-STACK-MIB", "ciscoEsRouterPort"),
)
if mibBuilder.loadTexts:
    ciscoEsRouterEntry.setStatus("mandatory")


class _CiscoEsRouterBox_Type(Integer32):
    """Custom type ciscoEsRouterBox based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsRouterBox_Type.__name__ = "Integer32"
_CiscoEsRouterBox_Object = MibTableColumn
ciscoEsRouterBox = _CiscoEsRouterBox_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 9, 1, 1, 1),
    _CiscoEsRouterBox_Type()
)
ciscoEsRouterBox.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsRouterBox.setStatus("mandatory")
_CiscoEsRouterPort_Type = Integer32
_CiscoEsRouterPort_Object = MibTableColumn
ciscoEsRouterPort = _CiscoEsRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 9, 1, 1, 2),
    _CiscoEsRouterPort_Type()
)
ciscoEsRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsRouterPort.setStatus("mandatory")


class _CiscoEsRouterOpState_Type(Integer32):
    """Custom type ciscoEsRouterOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("empty", 3),
          ("unknown", 4),
          ("up", 1))
    )


_CiscoEsRouterOpState_Type.__name__ = "Integer32"
_CiscoEsRouterOpState_Object = MibTableColumn
ciscoEsRouterOpState = _CiscoEsRouterOpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 9, 1, 1, 3),
    _CiscoEsRouterOpState_Type()
)
ciscoEsRouterOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsRouterOpState.setStatus("mandatory")
_CiscoEsRouterNetAddr_Type = IpAddress
_CiscoEsRouterNetAddr_Object = MibTableColumn
ciscoEsRouterNetAddr = _CiscoEsRouterNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 9, 1, 1, 4),
    _CiscoEsRouterNetAddr_Type()
)
ciscoEsRouterNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsRouterNetAddr.setStatus("mandatory")
_CiscoEsRouterBoardId_Type = Integer32
_CiscoEsRouterBoardId_Object = MibTableColumn
ciscoEsRouterBoardId = _CiscoEsRouterBoardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 9, 1, 1, 5),
    _CiscoEsRouterBoardId_Type()
)
ciscoEsRouterBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsRouterBoardId.setStatus("mandatory")
_CiscoEsRouterRev_Type = Integer32
_CiscoEsRouterRev_Object = MibTableColumn
ciscoEsRouterRev = _CiscoEsRouterRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 9, 1, 1, 6),
    _CiscoEsRouterRev_Type()
)
ciscoEsRouterRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsRouterRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ciscoEsStackCfgChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 0, 1)
)
ciscoEsStackCfgChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-ES-STACK-MIB", "ciscoEsNumSwitches"))
)
if mibBuilder.loadTexts:
    ciscoEsStackCfgChange.setStatus(
        ""
    )

ciscoEsStackProStackMatrixChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 1, 1, 0, 2)
)
ciscoEsStackProStackMatrixChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-ES-STACK-MIB", "ciscoEsProStackMatrixStatus"))
)
if mibBuilder.loadTexts:
    ciscoEsStackProStackMatrixChange.setStatus(
        ""
    )

ciscoEsStackTempChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 2, 0, 1)
)
ciscoEsStackTempChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-ES-STACK-MIB", "ciscoEsStackSwitchTemperature"))
)
if mibBuilder.loadTexts:
    ciscoEsStackTempChange.setStatus(
        ""
    )

ciscoEsPortStrNFwdEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 4, 0, 1)
)
ciscoEsPortStrNFwdEntry.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-ES-STACK-MIB", "ciscoEsPortActiveMode"))
)
if mibBuilder.loadTexts:
    ciscoEsPortStrNFwdEntry.setStatus(
        ""
    )

ciscoEsEtherChannelFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 6, 0, 1)
)
ciscoEsEtherChannelFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-ES-STACK-MIB", "ciscoEsECPorts"))
)
if mibBuilder.loadTexts:
    ciscoEsEtherChannelFailed.setStatus(
        ""
    )

ciscoEsVLANNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 0, 1)
)
ciscoEsVLANNewRoot.setObjects(
    ("CISCO-ES-STACK-MIB", "ciscoEsVLANInfoVLANNumber")
)
if mibBuilder.loadTexts:
    ciscoEsVLANNewRoot.setStatus(
        ""
    )

ciscoEsVLANTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 8, 0, 2)
)
ciscoEsVLANTopologyChange.setObjects(
    ("CISCO-ES-STACK-MIB", "ciscoEsVLANInfoVLANNumber")
)
if mibBuilder.loadTexts:
    ciscoEsVLANTopologyChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ES-STACK-MIB",
    **{"MacAddr": MacAddr,
       "BridgeId": BridgeId,
       "cisco": cisco,
       "workgroup": workgroup,
       "esStack": esStack,
       "ciscoEsMain": ciscoEsMain,
       "ciscoEsConfig": ciscoEsConfig,
       "ciscoEsStackCfgChange": ciscoEsStackCfgChange,
       "ciscoEsStackProStackMatrixChange": ciscoEsStackProStackMatrixChange,
       "ciscoEsIpAddr": ciscoEsIpAddr,
       "ciscoEsNetMask": ciscoEsNetMask,
       "ciscoEsDefaultGateway": ciscoEsDefaultGateway,
       "ciscoEsSysCurTime": ciscoEsSysCurTime,
       "ciscoEsConfiguration": ciscoEsConfiguration,
       "ciscoEsNumSwitches": ciscoEsNumSwitches,
       "ciscoEsStackStatus": ciscoEsStackStatus,
       "ciscoEsTftpServer": ciscoEsTftpServer,
       "ciscoEsTftpServerDomain": ciscoEsTftpServerDomain,
       "ciscoEsTftpFileLoc": ciscoEsTftpFileLoc,
       "ciscoEsSetLock": ciscoEsSetLock,
       "ciscoEsProStackMatrixStatus": ciscoEsProStackMatrixStatus,
       "ciscoEsNumMatrixModules": ciscoEsNumMatrixModules,
       "ciscoEsLLPortDsbld": ciscoEsLLPortDsbld,
       "ciscoEsTrapRcvrTable": ciscoEsTrapRcvrTable,
       "ciscoEsTrapRcvrEntry": ciscoEsTrapRcvrEntry,
       "ciscoEsTrapRcvrIndex": ciscoEsTrapRcvrIndex,
       "ciscoEsTrapRcvrStatus": ciscoEsTrapRcvrStatus,
       "ciscoEsTrapRcvrIpAddress": ciscoEsTrapRcvrIpAddress,
       "ciscoEsTrapRcvrComm": ciscoEsTrapRcvrComm,
       "ciscoEsTrapRcvrVLANs": ciscoEsTrapRcvrVLANs,
       "ciscoEsStack": ciscoEsStack,
       "ciscoEsStackTempChange": ciscoEsStackTempChange,
       "ciscoEsStackTable": ciscoEsStackTable,
       "ciscoEsStackEntry": ciscoEsStackEntry,
       "ciscoEsStackSwitchNumber": ciscoEsStackSwitchNumber,
       "ciscoEsStackSwitchAddr": ciscoEsStackSwitchAddr,
       "ciscoEsStackSwitchFwVersion": ciscoEsStackSwitchFwVersion,
       "ciscoEsStackSwitchHwVersion": ciscoEsStackSwitchHwVersion,
       "ciscoEsStackSwitchUptime": ciscoEsStackSwitchUptime,
       "ciscoEsStackSwitchStatus": ciscoEsStackSwitchStatus,
       "ciscoEsStackSwitchTemperature": ciscoEsStackSwitchTemperature,
       "ciscoEsStackSwitchMemory": ciscoEsStackSwitchMemory,
       "ciscoEsStackSwitchProbe": ciscoEsStackSwitchProbe,
       "ciscoEsStackSwitchProbeDirection": ciscoEsStackSwitchProbeDirection,
       "ciscoEsStackSwitchFeatureStatus": ciscoEsStackSwitchFeatureStatus,
       "ciscoEsStackSwitchFeatureKey": ciscoEsStackSwitchFeatureKey,
       "ciscoEsStackSwitchPorts": ciscoEsStackSwitchPorts,
       "ciscoEsStackSwitchAgingTime": ciscoEsStackSwitchAgingTime,
       "ciscoEsStackSwitchAgingLevel": ciscoEsStackSwitchAgingLevel,
       "ciscoEsStackSwitchBufferOverruns": ciscoEsStackSwitchBufferOverruns,
       "ciscoEsStackSwitchSoftwareFrames": ciscoEsStackSwitchSoftwareFrames,
       "ciscoEsStackSwitchInErrFrames": ciscoEsStackSwitchInErrFrames,
       "ciscoEsStackSwitchInShortFrames": ciscoEsStackSwitchInShortFrames,
       "ciscoEsStackSwitchInLongFrames": ciscoEsStackSwitchInLongFrames,
       "ciscoEsStackSwitchOutDroppedFrames": ciscoEsStackSwitchOutDroppedFrames,
       "ciscoEsStackSwitchInNoSpaceFrames": ciscoEsStackSwitchInNoSpaceFrames,
       "ciscoEsStackSwitchOutTotalReqs": ciscoEsStackSwitchOutTotalReqs,
       "ciscoEsStackSwitchOutTotalFrames": ciscoEsStackSwitchOutTotalFrames,
       "ciscoEsStackSwitchLongestHashChain": ciscoEsStackSwitchLongestHashChain,
       "ciscoEsStackSwitchHashTableFulls": ciscoEsStackSwitchHashTableFulls,
       "ciscoEsStackSwitchId": ciscoEsStackSwitchId,
       "ciscoEsStackSwitchDplxCtrl": ciscoEsStackSwitchDplxCtrl,
       "ciscoEsModule": ciscoEsModule,
       "ciscoEsModTable": ciscoEsModTable,
       "ciscoEsModEntry": ciscoEsModEntry,
       "ciscoEsModSwitchNumber": ciscoEsModSwitchNumber,
       "ciscoEsModNumber": ciscoEsModNumber,
       "ciscoEsModState": ciscoEsModState,
       "ciscoEsModType": ciscoEsModType,
       "ciscoEsModRevision": ciscoEsModRevision,
       "ciscoEsModNumPorts": ciscoEsModNumPorts,
       "ciscoEsModUptime": ciscoEsModUptime,
       "ciscoEsPort": ciscoEsPort,
       "ciscoEsPortStrNFwdEntry": ciscoEsPortStrNFwdEntry,
       "ciscoEsPortTable": ciscoEsPortTable,
       "ciscoEsPortEntry": ciscoEsPortEntry,
       "ciscoEsPortSwitchNumber": ciscoEsPortSwitchNumber,
       "ciscoEsPortNumber": ciscoEsPortNumber,
       "ciscoEsPortModNumber": ciscoEsPortModNumber,
       "ciscoEsPortIfIndex": ciscoEsPortIfIndex,
       "ciscoEsPortDuplex": ciscoEsPortDuplex,
       "ciscoEsPortRcvLocalFrames": ciscoEsPortRcvLocalFrames,
       "ciscoEsPortForwardedFrames": ciscoEsPortForwardedFrames,
       "ciscoEsPortMostStations": ciscoEsPortMostStations,
       "ciscoEsPortMaxStations": ciscoEsPortMaxStations,
       "ciscoEsPortSWHandledFrames": ciscoEsPortSWHandledFrames,
       "ciscoEsPortLocalStations": ciscoEsPortLocalStations,
       "ciscoEsPortRemoteStations": ciscoEsPortRemoteStations,
       "ciscoEsPortUnknownStaFrames": ciscoEsPortUnknownStaFrames,
       "ciscoEsPortResetStats": ciscoEsPortResetStats,
       "ciscoEsPortResetTimer": ciscoEsPortResetTimer,
       "ciscoEsPortResetAddrs": ciscoEsPortResetAddrs,
       "ciscoEsPortInFrames": ciscoEsPortInFrames,
       "ciscoEsPortOutFrames": ciscoEsPortOutFrames,
       "ciscoEsPortLongFrames": ciscoEsPortLongFrames,
       "ciscoEsPortShortFrames": ciscoEsPortShortFrames,
       "ciscoEsPortInBufOverflows": ciscoEsPortInBufOverflows,
       "ciscoEsPortOutBufOverflows": ciscoEsPortOutBufOverflows,
       "ciscoEsPortRcvBcasts": ciscoEsPortRcvBcasts,
       "ciscoEsPortRcvMcasts": ciscoEsPortRcvMcasts,
       "ciscoEsPortSwitchedFrames": ciscoEsPortSwitchedFrames,
       "ciscoEsPortInOctets": ciscoEsPortInOctets,
       "ciscoEsPortOutOctets": ciscoEsPortOutOctets,
       "ciscoEsPortPktsInErrors": ciscoEsPortPktsInErrors,
       "ciscoEsPortLinkState": ciscoEsPortLinkState,
       "ciscoEsPortOprStatus": ciscoEsPortOprStatus,
       "ciscoEsPortMdiMdix": ciscoEsPortMdiMdix,
       "ciscoEsPortHashOverflows": ciscoEsPortHashOverflows,
       "ciscoEsPortTableOverflows": ciscoEsPortTableOverflows,
       "ciscoEsPortAddrAgingTime": ciscoEsPortAddrAgingTime,
       "ciscoEsPortDemandAgingLevel": ciscoEsPortDemandAgingLevel,
       "ciscoEsPortCfgMode": ciscoEsPortCfgMode,
       "ciscoEsPortActiveMode": ciscoEsPortActiveMode,
       "ciscoEsPortErrThreshold": ciscoEsPortErrThreshold,
       "ciscoEsPortLearningState": ciscoEsPortLearningState,
       "ciscoEsPortRuntlessMode": ciscoEsPortRuntlessMode,
       "ciscoEsPortType": ciscoEsPortType,
       "ciscoEsPortCDPTimeToLive": ciscoEsPortCDPTimeToLive,
       "ciscoEsPortFastPort": ciscoEsPortFastPort,
       "ciscoEsPortISLOperStatus": ciscoEsPortISLOperStatus,
       "ciscoEsPortISLAdminStatus": ciscoEsPortISLAdminStatus,
       "ciscoEsOptPortStaTable": ciscoEsOptPortStaTable,
       "ciscoEsOptPortStaEntry": ciscoEsOptPortStaEntry,
       "ciscoEsOptPortStaPos": ciscoEsOptPortStaPos,
       "ciscoEsOptPortStaVal": ciscoEsOptPortStaVal,
       "ciscoEsPortStnTable": ciscoEsPortStnTable,
       "ciscoEsPortStnEntry": ciscoEsPortStnEntry,
       "ciscoEsPortStnSwitchNumber": ciscoEsPortStnSwitchNumber,
       "ciscoEsPortStnPortNum": ciscoEsPortStnPortNum,
       "ciscoEsPortStnAddress": ciscoEsPortStnAddress,
       "ciscoEsPortStnLocation": ciscoEsPortStnLocation,
       "ciscoEsPortStnSrcFrames": ciscoEsPortStnSrcFrames,
       "ciscoEsPortStnSrcBytes": ciscoEsPortStnSrcBytes,
       "ciscoEsPortStnDestnFrames": ciscoEsPortStnDestnFrames,
       "ciscoEsPortStnDestnBytes": ciscoEsPortStnDestnBytes,
       "ciscoEsPortStnPortOfExit": ciscoEsPortStnPortOfExit,
       "ciscoEsDmns": ciscoEsDmns,
       "ciscoEsEChannel": ciscoEsEChannel,
       "ciscoEsEtherChannelFailed": ciscoEsEtherChannelFailed,
       "ciscoEsECTable": ciscoEsECTable,
       "ciscoEsECEntry": ciscoEsECEntry,
       "ciscoEsECSwitchNumber": ciscoEsECSwitchNumber,
       "ciscoEsECNumber": ciscoEsECNumber,
       "ciscoEsECPorts": ciscoEsECPorts,
       "ciscoEsFilter": ciscoEsFilter,
       "ciscoEsFilterTable": ciscoEsFilterTable,
       "ciscoEsFilterEntry": ciscoEsFilterEntry,
       "ciscoEsFilterSwitchNumber": ciscoEsFilterSwitchNumber,
       "ciscoEsFilterStationAddress": ciscoEsFilterStationAddress,
       "ciscoEsFilterType": ciscoEsFilterType,
       "ciscoEsFilterPorts": ciscoEsFilterPorts,
       "ciscoEsFilterMask": ciscoEsFilterMask,
       "ciscoEsFilterRemoteSwitch": ciscoEsFilterRemoteSwitch,
       "ciscoEsFilterRemotePort": ciscoEsFilterRemotePort,
       "ciscoEsFilterStatus": ciscoEsFilterStatus,
       "ciscoEsVLANs": ciscoEsVLANs,
       "ciscoEsVLANNewRoot": ciscoEsVLANNewRoot,
       "ciscoEsVLANTopologyChange": ciscoEsVLANTopologyChange,
       "ciscoEsVLANPortTable": ciscoEsVLANPortTable,
       "ciscoEsVLANPortEntry": ciscoEsVLANPortEntry,
       "ciscoEsVLANPortVLANNumber": ciscoEsVLANPortVLANNumber,
       "ciscoEsVLANPortSwitchNumber": ciscoEsVLANPortSwitchNumber,
       "ciscoEsVLANPortPorts": ciscoEsVLANPortPorts,
       "ciscoEsVLANInfoTable": ciscoEsVLANInfoTable,
       "ciscoEsVLANInfoEntry": ciscoEsVLANInfoEntry,
       "ciscoEsVLANInfoVLANNumber": ciscoEsVLANInfoVLANNumber,
       "ciscoEsVLANInfoState": ciscoEsVLANInfoState,
       "ciscoEsVLANInfoName": ciscoEsVLANInfoName,
       "ciscoEsVLANInfoBaseAddr": ciscoEsVLANInfoBaseAddr,
       "ciscoEsVLANInfoIfIndex": ciscoEsVLANInfoIfIndex,
       "ciscoEsVLANInfoIpState": ciscoEsVLANInfoIpState,
       "ciscoEsVLANInfoIpAddress": ciscoEsVLANInfoIpAddress,
       "ciscoEsVLANInfoIpSubnetMask": ciscoEsVLANInfoIpSubnetMask,
       "ciscoEsVLANInfoIpDefaultGateway": ciscoEsVLANInfoIpDefaultGateway,
       "ciscoEsVLANInfoStp": ciscoEsVLANInfoStp,
       "ciscoEsVLANInfoNumStations": ciscoEsVLANInfoNumStations,
       "ciscoEsVLANInfoMaxStations": ciscoEsVLANInfoMaxStations,
       "ciscoEsVLANStpTable": ciscoEsVLANStpTable,
       "ciscoEsVLANStpEntry": ciscoEsVLANStpEntry,
       "ciscoEsVLANStpVLANIndex": ciscoEsVLANStpVLANIndex,
       "ciscoEsVLANStpPriority": ciscoEsVLANStpPriority,
       "ciscoEsVLANStpTimeSinceTopologyChange": ciscoEsVLANStpTimeSinceTopologyChange,
       "ciscoEsVLANStpTopChanges": ciscoEsVLANStpTopChanges,
       "ciscoEsVLANStpDesignatedRoot": ciscoEsVLANStpDesignatedRoot,
       "ciscoEsVLANStpRootCost": ciscoEsVLANStpRootCost,
       "ciscoEsVLANStpRootPort": ciscoEsVLANStpRootPort,
       "ciscoEsVLANStpMaxAge": ciscoEsVLANStpMaxAge,
       "ciscoEsVLANStpHelloTime": ciscoEsVLANStpHelloTime,
       "ciscoEsVLANStpHoldTime": ciscoEsVLANStpHoldTime,
       "ciscoEsVLANStpForwardDelay": ciscoEsVLANStpForwardDelay,
       "ciscoEsVLANStpBridgeMaxAge": ciscoEsVLANStpBridgeMaxAge,
       "ciscoEsVLANStpBridgeHelloTime": ciscoEsVLANStpBridgeHelloTime,
       "ciscoEsVLANStpBridgeForwardDelay": ciscoEsVLANStpBridgeForwardDelay,
       "ciscoEsVLANStationTable": ciscoEsVLANStationTable,
       "ciscoEsVLANStationEntry": ciscoEsVLANStationEntry,
       "ciscoEsVLANStationVLANIndex": ciscoEsVLANStationVLANIndex,
       "ciscoEsVLANStationBoxNum": ciscoEsVLANStationBoxNum,
       "ciscoEsVLANStationAddress": ciscoEsVLANStationAddress,
       "ciscoEsVLANStationPort": ciscoEsVLANStationPort,
       "ciscoEsVLANStationTraffic": ciscoEsVLANStationTraffic,
       "ciscoEsOptVLANStaTable": ciscoEsOptVLANStaTable,
       "ciscoEsOptVLANStaEntry": ciscoEsOptVLANStaEntry,
       "ciscoEsOptVLANStaPos": ciscoEsOptVLANStaPos,
       "ciscoEsOptVLANStaVal": ciscoEsOptVLANStaVal,
       "ciscoEsTransitedConfiguredVLANs": ciscoEsTransitedConfiguredVLANs,
       "ciscoEsTransitedVLANs": ciscoEsTransitedVLANs,
       "ciscoEsRouter": ciscoEsRouter,
       "ciscoEsRouterTable": ciscoEsRouterTable,
       "ciscoEsRouterEntry": ciscoEsRouterEntry,
       "ciscoEsRouterBox": ciscoEsRouterBox,
       "ciscoEsRouterPort": ciscoEsRouterPort,
       "ciscoEsRouterOpState": ciscoEsRouterOpState,
       "ciscoEsRouterNetAddr": ciscoEsRouterNetAddr,
       "ciscoEsRouterBoardId": ciscoEsRouterBoardId,
       "ciscoEsRouterRev": ciscoEsRouterRev}
)
