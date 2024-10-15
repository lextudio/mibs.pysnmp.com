# SNMP MIB module (CISCO-TS-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TS-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:56 2024
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

(Timeout,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "Timeout")

(cisco,
 workgroup) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "cisco",
    "workgroup")

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

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

(ringStationIfIndex,
 ringStationMacAddress) = mibBuilder.importSymbols(
    "TOKEN-RING-RMON-MIB",
    "ringStationIfIndex",
    "ringStationMacAddress")


# MODULE-IDENTITY


# Types definitions



class MacAddr(OctetString):
    """Custom type MacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TsStack_ObjectIdentity = ObjectIdentity
tsStack = _TsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32)
)
_CiscoTsMain_ObjectIdentity = ObjectIdentity
ciscoTsMain = _CiscoTsMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1)
)
_CiscoTsConfig_ObjectIdentity = ObjectIdentity
ciscoTsConfig = _CiscoTsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1)
)
_CiscoTsIpAddr_Type = IpAddress
_CiscoTsIpAddr_Object = MibScalar
ciscoTsIpAddr = _CiscoTsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 1),
    _CiscoTsIpAddr_Type()
)
ciscoTsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsIpAddr.setStatus("mandatory")
_CiscoTsNetMask_Type = IpAddress
_CiscoTsNetMask_Object = MibScalar
ciscoTsNetMask = _CiscoTsNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 2),
    _CiscoTsNetMask_Type()
)
ciscoTsNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsNetMask.setStatus("mandatory")
_CiscoTsDefaultGateway_Type = IpAddress
_CiscoTsDefaultGateway_Object = MibScalar
ciscoTsDefaultGateway = _CiscoTsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 3),
    _CiscoTsDefaultGateway_Type()
)
ciscoTsDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsDefaultGateway.setStatus("mandatory")


class _CiscoTsSysCurTime_Type(DisplayString):
    """Custom type ciscoTsSysCurTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CiscoTsSysCurTime_Type.__name__ = "DisplayString"
_CiscoTsSysCurTime_Object = MibScalar
ciscoTsSysCurTime = _CiscoTsSysCurTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 4),
    _CiscoTsSysCurTime_Type()
)
ciscoTsSysCurTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsSysCurTime.setStatus("mandatory")


class _CiscoTsConfiguration_Type(Integer32):
    """Custom type ciscoTsConfiguration based on Integer32"""
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


_CiscoTsConfiguration_Type.__name__ = "Integer32"
_CiscoTsConfiguration_Object = MibScalar
ciscoTsConfiguration = _CiscoTsConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 5),
    _CiscoTsConfiguration_Type()
)
ciscoTsConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsConfiguration.setStatus("mandatory")
_CiscoTsNumSwitches_Type = Integer32
_CiscoTsNumSwitches_Object = MibScalar
ciscoTsNumSwitches = _CiscoTsNumSwitches_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 6),
    _CiscoTsNumSwitches_Type()
)
ciscoTsNumSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsNumSwitches.setStatus("mandatory")


class _CiscoTsStackStatus_Type(Integer32):
    """Custom type ciscoTsStackStatus based on Integer32"""
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


_CiscoTsStackStatus_Type.__name__ = "Integer32"
_CiscoTsStackStatus_Object = MibScalar
ciscoTsStackStatus = _CiscoTsStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 7),
    _CiscoTsStackStatus_Type()
)
ciscoTsStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackStatus.setStatus("mandatory")
_CiscoTsTftpServer_Type = IpAddress
_CiscoTsTftpServer_Object = MibScalar
ciscoTsTftpServer = _CiscoTsTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 8),
    _CiscoTsTftpServer_Type()
)
ciscoTsTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTftpServer.setStatus("mandatory")


class _CiscoTsTftpServerTrBRF_Type(Integer32):
    """Custom type ciscoTsTftpServerTrBRF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CiscoTsTftpServerTrBRF_Type.__name__ = "Integer32"
_CiscoTsTftpServerTrBRF_Object = MibScalar
ciscoTsTftpServerTrBRF = _CiscoTsTftpServerTrBRF_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 9),
    _CiscoTsTftpServerTrBRF_Type()
)
ciscoTsTftpServerTrBRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTftpServerTrBRF.setStatus("mandatory")


class _CiscoTsTftpFileLoc_Type(DisplayString):
    """Custom type ciscoTsTftpFileLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CiscoTsTftpFileLoc_Type.__name__ = "DisplayString"
_CiscoTsTftpFileLoc_Object = MibScalar
ciscoTsTftpFileLoc = _CiscoTsTftpFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 10),
    _CiscoTsTftpFileLoc_Type()
)
ciscoTsTftpFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTftpFileLoc.setStatus("mandatory")


class _CiscoTsTftpDownload_Type(Integer32):
    """Custom type ciscoTsTftpDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CiscoTsTftpDownload_Type.__name__ = "Integer32"
_CiscoTsTftpDownload_Object = MibScalar
ciscoTsTftpDownload = _CiscoTsTftpDownload_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 11),
    _CiscoTsTftpDownload_Type()
)
ciscoTsTftpDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTftpDownload.setStatus("mandatory")


class _CiscoTsTftpDownloadStatus_Type(Integer32):
    """Custom type ciscoTsTftpDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("other", 3),
          ("writing", 1))
    )


_CiscoTsTftpDownloadStatus_Type.__name__ = "Integer32"
_CiscoTsTftpDownloadStatus_Object = MibScalar
ciscoTsTftpDownloadStatus = _CiscoTsTftpDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 12),
    _CiscoTsTftpDownloadStatus_Type()
)
ciscoTsTftpDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTftpDownloadStatus.setStatus("mandatory")


class _CiscoTsProStackMatrixStatus_Type(Integer32):
    """Custom type ciscoTsProStackMatrixStatus based on Integer32"""
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


_CiscoTsProStackMatrixStatus_Type.__name__ = "Integer32"
_CiscoTsProStackMatrixStatus_Object = MibScalar
ciscoTsProStackMatrixStatus = _CiscoTsProStackMatrixStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 13),
    _CiscoTsProStackMatrixStatus_Type()
)
ciscoTsProStackMatrixStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsProStackMatrixStatus.setStatus("mandatory")
_CiscoTsNumMatrixModules_Type = Integer32
_CiscoTsNumMatrixModules_Object = MibScalar
ciscoTsNumMatrixModules = _CiscoTsNumMatrixModules_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 14),
    _CiscoTsNumMatrixModules_Type()
)
ciscoTsNumMatrixModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsNumMatrixModules.setStatus("mandatory")


class _CiscoTsStackReset_Type(Integer32):
    """Custom type ciscoTsStackReset based on Integer32"""
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


_CiscoTsStackReset_Type.__name__ = "Integer32"
_CiscoTsStackReset_Object = MibScalar
ciscoTsStackReset = _CiscoTsStackReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 15),
    _CiscoTsStackReset_Type()
)
ciscoTsStackReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsStackReset.setStatus("mandatory")


class _CiscoTsStackRMONStatistics_Type(Integer32):
    """Custom type ciscoTsStackRMONStatistics based on Integer32"""
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


_CiscoTsStackRMONStatistics_Type.__name__ = "Integer32"
_CiscoTsStackRMONStatistics_Object = MibScalar
ciscoTsStackRMONStatistics = _CiscoTsStackRMONStatistics_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 16),
    _CiscoTsStackRMONStatistics_Type()
)
ciscoTsStackRMONStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsStackRMONStatistics.setStatus("mandatory")
_CiscoTsTrapRcvrTable_Object = MibTable
ciscoTsTrapRcvrTable = _CiscoTsTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 25)
)
if mibBuilder.loadTexts:
    ciscoTsTrapRcvrTable.setStatus("mandatory")
_CiscoTsTrapRcvrEntry_Object = MibTableRow
ciscoTsTrapRcvrEntry = _CiscoTsTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 25, 1)
)
ciscoTsTrapRcvrEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsTrapRcvrIndex"),
)
if mibBuilder.loadTexts:
    ciscoTsTrapRcvrEntry.setStatus("mandatory")


class _CiscoTsTrapRcvrIndex_Type(Integer32):
    """Custom type ciscoTsTrapRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiscoTsTrapRcvrIndex_Type.__name__ = "Integer32"
_CiscoTsTrapRcvrIndex_Object = MibTableColumn
ciscoTsTrapRcvrIndex = _CiscoTsTrapRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 25, 1, 1),
    _CiscoTsTrapRcvrIndex_Type()
)
ciscoTsTrapRcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTrapRcvrIndex.setStatus("mandatory")


class _CiscoTsTrapRcvrStatus_Type(Integer32):
    """Custom type ciscoTsTrapRcvrStatus based on Integer32"""
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


_CiscoTsTrapRcvrStatus_Type.__name__ = "Integer32"
_CiscoTsTrapRcvrStatus_Object = MibTableColumn
ciscoTsTrapRcvrStatus = _CiscoTsTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 25, 1, 2),
    _CiscoTsTrapRcvrStatus_Type()
)
ciscoTsTrapRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrapRcvrStatus.setStatus("mandatory")
_CiscoTsTrapRcvrIpAddress_Type = IpAddress
_CiscoTsTrapRcvrIpAddress_Object = MibTableColumn
ciscoTsTrapRcvrIpAddress = _CiscoTsTrapRcvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 25, 1, 3),
    _CiscoTsTrapRcvrIpAddress_Type()
)
ciscoTsTrapRcvrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrapRcvrIpAddress.setStatus("mandatory")


class _CiscoTsTrapRcvrComm_Type(DisplayString):
    """Custom type ciscoTsTrapRcvrComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CiscoTsTrapRcvrComm_Type.__name__ = "DisplayString"
_CiscoTsTrapRcvrComm_Object = MibTableColumn
ciscoTsTrapRcvrComm = _CiscoTsTrapRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 25, 1, 4),
    _CiscoTsTrapRcvrComm_Type()
)
ciscoTsTrapRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrapRcvrComm.setStatus("mandatory")


class _CiscoTsTrapRcvrTrBRFs_Type(OctetString):
    """Custom type ciscoTsTrapRcvrTrBRFs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CiscoTsTrapRcvrTrBRFs_Type.__name__ = "OctetString"
_CiscoTsTrapRcvrTrBRFs_Object = MibTableColumn
ciscoTsTrapRcvrTrBRFs = _CiscoTsTrapRcvrTrBRFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 25, 1, 5),
    _CiscoTsTrapRcvrTrBRFs_Type()
)
ciscoTsTrapRcvrTrBRFs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrapRcvrTrBRFs.setStatus("mandatory")
_CiscoTsStack_ObjectIdentity = ObjectIdentity
ciscoTsStack = _CiscoTsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2)
)
_CiscoTsStackTable_Object = MibTable
ciscoTsStackTable = _CiscoTsStackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoTsStackTable.setStatus("mandatory")
_CiscoTsStackEntry_Object = MibTableRow
ciscoTsStackEntry = _CiscoTsStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1)
)
ciscoTsStackEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsStackSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsStackSwitchBIAddr"),
)
if mibBuilder.loadTexts:
    ciscoTsStackEntry.setStatus("mandatory")


class _CiscoTsStackSwitchNumber_Type(Integer32):
    """Custom type ciscoTsStackSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoTsStackSwitchNumber_Type.__name__ = "Integer32"
_CiscoTsStackSwitchNumber_Object = MibTableColumn
ciscoTsStackSwitchNumber = _CiscoTsStackSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 1),
    _CiscoTsStackSwitchNumber_Type()
)
ciscoTsStackSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchNumber.setStatus("mandatory")
_CiscoTsStackSwitchBIAddr_Type = MacAddr
_CiscoTsStackSwitchBIAddr_Object = MibTableColumn
ciscoTsStackSwitchBIAddr = _CiscoTsStackSwitchBIAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 2),
    _CiscoTsStackSwitchBIAddr_Type()
)
ciscoTsStackSwitchBIAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchBIAddr.setStatus("mandatory")
_CiscoTsStackSwitchLAAddr_Type = MacAddr
_CiscoTsStackSwitchLAAddr_Object = MibTableColumn
ciscoTsStackSwitchLAAddr = _CiscoTsStackSwitchLAAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 3),
    _CiscoTsStackSwitchLAAddr_Type()
)
ciscoTsStackSwitchLAAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchLAAddr.setStatus("mandatory")


class _CiscoTsStackSwitchFwVersion_Type(DisplayString):
    """Custom type ciscoTsStackSwitchFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CiscoTsStackSwitchFwVersion_Type.__name__ = "DisplayString"
_CiscoTsStackSwitchFwVersion_Object = MibTableColumn
ciscoTsStackSwitchFwVersion = _CiscoTsStackSwitchFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 4),
    _CiscoTsStackSwitchFwVersion_Type()
)
ciscoTsStackSwitchFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchFwVersion.setStatus("mandatory")


class _CiscoTsStackSwitchHwVersion_Type(DisplayString):
    """Custom type ciscoTsStackSwitchHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CiscoTsStackSwitchHwVersion_Type.__name__ = "DisplayString"
_CiscoTsStackSwitchHwVersion_Object = MibTableColumn
ciscoTsStackSwitchHwVersion = _CiscoTsStackSwitchHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 5),
    _CiscoTsStackSwitchHwVersion_Type()
)
ciscoTsStackSwitchHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchHwVersion.setStatus("mandatory")
_CiscoTsStackSwitchUptime_Type = TimeTicks
_CiscoTsStackSwitchUptime_Object = MibTableColumn
ciscoTsStackSwitchUptime = _CiscoTsStackSwitchUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 6),
    _CiscoTsStackSwitchUptime_Type()
)
ciscoTsStackSwitchUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchUptime.setStatus("mandatory")


class _CiscoTsStackSwitchStatus_Type(Integer32):
    """Custom type ciscoTsStackSwitchStatus based on Integer32"""
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


_CiscoTsStackSwitchStatus_Type.__name__ = "Integer32"
_CiscoTsStackSwitchStatus_Object = MibTableColumn
ciscoTsStackSwitchStatus = _CiscoTsStackSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 7),
    _CiscoTsStackSwitchStatus_Type()
)
ciscoTsStackSwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchStatus.setStatus("mandatory")
_CiscoTsStackSwitchTemperature_Type = Integer32
_CiscoTsStackSwitchTemperature_Object = MibTableColumn
ciscoTsStackSwitchTemperature = _CiscoTsStackSwitchTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 8),
    _CiscoTsStackSwitchTemperature_Type()
)
ciscoTsStackSwitchTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchTemperature.setStatus("mandatory")


class _CiscoTsStackSwitchMemory_Type(Integer32):
    """Custom type ciscoTsStackSwitchMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CiscoTsStackSwitchMemory_Type.__name__ = "Integer32"
_CiscoTsStackSwitchMemory_Object = MibTableColumn
ciscoTsStackSwitchMemory = _CiscoTsStackSwitchMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 9),
    _CiscoTsStackSwitchMemory_Type()
)
ciscoTsStackSwitchMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchMemory.setStatus("mandatory")


class _CiscoTsStackSwitchSPANPort_Type(Integer32):
    """Custom type ciscoTsStackSwitchSPANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CiscoTsStackSwitchSPANPort_Type.__name__ = "Integer32"
_CiscoTsStackSwitchSPANPort_Object = MibTableColumn
ciscoTsStackSwitchSPANPort = _CiscoTsStackSwitchSPANPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 10),
    _CiscoTsStackSwitchSPANPort_Type()
)
ciscoTsStackSwitchSPANPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchSPANPort.setStatus("mandatory")


class _CiscoTsStackSwitchSPANMonitoredPort_Type(Integer32):
    """Custom type ciscoTsStackSwitchSPANMonitoredPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CiscoTsStackSwitchSPANMonitoredPort_Type.__name__ = "Integer32"
_CiscoTsStackSwitchSPANMonitoredPort_Object = MibTableColumn
ciscoTsStackSwitchSPANMonitoredPort = _CiscoTsStackSwitchSPANMonitoredPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 11),
    _CiscoTsStackSwitchSPANMonitoredPort_Type()
)
ciscoTsStackSwitchSPANMonitoredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchSPANMonitoredPort.setStatus("mandatory")


class _CiscoTsStackSwitchFeatureStatus_Type(Integer32):
    """Custom type ciscoTsStackSwitchFeatureStatus based on Integer32"""
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


_CiscoTsStackSwitchFeatureStatus_Type.__name__ = "Integer32"
_CiscoTsStackSwitchFeatureStatus_Object = MibTableColumn
ciscoTsStackSwitchFeatureStatus = _CiscoTsStackSwitchFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 12),
    _CiscoTsStackSwitchFeatureStatus_Type()
)
ciscoTsStackSwitchFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchFeatureStatus.setStatus("mandatory")
_CiscoTsStackSwitchFeatureKey_Type = Integer32
_CiscoTsStackSwitchFeatureKey_Object = MibTableColumn
ciscoTsStackSwitchFeatureKey = _CiscoTsStackSwitchFeatureKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 13),
    _CiscoTsStackSwitchFeatureKey_Type()
)
ciscoTsStackSwitchFeatureKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchFeatureKey.setStatus("mandatory")


class _CiscoTsStackSwitchPorts_Type(OctetString):
    """Custom type ciscoTsStackSwitchPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoTsStackSwitchPorts_Type.__name__ = "OctetString"
_CiscoTsStackSwitchPorts_Object = MibTableColumn
ciscoTsStackSwitchPorts = _CiscoTsStackSwitchPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 14),
    _CiscoTsStackSwitchPorts_Type()
)
ciscoTsStackSwitchPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchPorts.setStatus("mandatory")


class _CiscoTsStackSwitchAgingTime_Type(Integer32):
    """Custom type ciscoTsStackSwitchAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CiscoTsStackSwitchAgingTime_Type.__name__ = "Integer32"
_CiscoTsStackSwitchAgingTime_Object = MibTableColumn
ciscoTsStackSwitchAgingTime = _CiscoTsStackSwitchAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 15),
    _CiscoTsStackSwitchAgingTime_Type()
)
ciscoTsStackSwitchAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchAgingTime.setStatus("mandatory")


class _CiscoTsStackSwitchAgingLevel_Type(Integer32):
    """Custom type ciscoTsStackSwitchAgingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_CiscoTsStackSwitchAgingLevel_Type.__name__ = "Integer32"
_CiscoTsStackSwitchAgingLevel_Object = MibTableColumn
ciscoTsStackSwitchAgingLevel = _CiscoTsStackSwitchAgingLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 16),
    _CiscoTsStackSwitchAgingLevel_Type()
)
ciscoTsStackSwitchAgingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchAgingLevel.setStatus("mandatory")
_CiscoTsStackSwitchXmitFrames_Type = Counter32
_CiscoTsStackSwitchXmitFrames_Object = MibTableColumn
ciscoTsStackSwitchXmitFrames = _CiscoTsStackSwitchXmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 18),
    _CiscoTsStackSwitchXmitFrames_Type()
)
ciscoTsStackSwitchXmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchXmitFrames.setStatus("mandatory")
_CiscoTsStackSwitchRcvdFrames_Type = Counter32
_CiscoTsStackSwitchRcvdFrames_Object = MibTableColumn
ciscoTsStackSwitchRcvdFrames = _CiscoTsStackSwitchRcvdFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 19),
    _CiscoTsStackSwitchRcvdFrames_Type()
)
ciscoTsStackSwitchRcvdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchRcvdFrames.setStatus("mandatory")
_CiscoTsStackSwitchRcvdErrFrames_Type = Counter32
_CiscoTsStackSwitchRcvdErrFrames_Object = MibTableColumn
ciscoTsStackSwitchRcvdErrFrames = _CiscoTsStackSwitchRcvdErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 20),
    _CiscoTsStackSwitchRcvdErrFrames_Type()
)
ciscoTsStackSwitchRcvdErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchRcvdErrFrames.setStatus("mandatory")
_CiscoTsStackSwitchLostFrames_Type = Counter32
_CiscoTsStackSwitchLostFrames_Object = MibTableColumn
ciscoTsStackSwitchLostFrames = _CiscoTsStackSwitchLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 21),
    _CiscoTsStackSwitchLostFrames_Type()
)
ciscoTsStackSwitchLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchLostFrames.setStatus("mandatory")
_CiscoTsStackSwitchPendingSendRqsts_Type = Counter32
_CiscoTsStackSwitchPendingSendRqsts_Object = MibTableColumn
ciscoTsStackSwitchPendingSendRqsts = _CiscoTsStackSwitchPendingSendRqsts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 22),
    _CiscoTsStackSwitchPendingSendRqsts_Type()
)
ciscoTsStackSwitchPendingSendRqsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchPendingSendRqsts.setStatus("mandatory")
_CiscoTsStackSwitchXmitErrFrames_Type = Counter32
_CiscoTsStackSwitchXmitErrFrames_Object = MibTableColumn
ciscoTsStackSwitchXmitErrFrames = _CiscoTsStackSwitchXmitErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 23),
    _CiscoTsStackSwitchXmitErrFrames_Type()
)
ciscoTsStackSwitchXmitErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchXmitErrFrames.setStatus("mandatory")
_CiscoTsStackSwitchCurrActStations_Type = Counter32
_CiscoTsStackSwitchCurrActStations_Object = MibTableColumn
ciscoTsStackSwitchCurrActStations = _CiscoTsStackSwitchCurrActStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 24),
    _CiscoTsStackSwitchCurrActStations_Type()
)
ciscoTsStackSwitchCurrActStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchCurrActStations.setStatus("mandatory")
_CiscoTsStackSwitchLargestNumStations_Type = Counter32
_CiscoTsStackSwitchLargestNumStations_Object = MibTableColumn
ciscoTsStackSwitchLargestNumStations = _CiscoTsStackSwitchLargestNumStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 25),
    _CiscoTsStackSwitchLargestNumStations_Type()
)
ciscoTsStackSwitchLargestNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchLargestNumStations.setStatus("mandatory")
_CiscoTsStackSwitchMaxAddressChain_Type = Gauge32
_CiscoTsStackSwitchMaxAddressChain_Object = MibTableColumn
ciscoTsStackSwitchMaxAddressChain = _CiscoTsStackSwitchMaxAddressChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 26),
    _CiscoTsStackSwitchMaxAddressChain_Type()
)
ciscoTsStackSwitchMaxAddressChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchMaxAddressChain.setStatus("mandatory")
_CiscoTsStackSwitchAddressTblFulls_Type = Counter32
_CiscoTsStackSwitchAddressTblFulls_Object = MibTableColumn
ciscoTsStackSwitchAddressTblFulls = _CiscoTsStackSwitchAddressTblFulls_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 27),
    _CiscoTsStackSwitchAddressTblFulls_Type()
)
ciscoTsStackSwitchAddressTblFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchAddressTblFulls.setStatus("mandatory")
_CiscoTsStackSwitchId_Type = ObjectIdentifier
_CiscoTsStackSwitchId_Object = MibTableColumn
ciscoTsStackSwitchId = _CiscoTsStackSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 28),
    _CiscoTsStackSwitchId_Type()
)
ciscoTsStackSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchId.setStatus("mandatory")


class _CiscoTsStackSwitchSPANMonitoredTrCRFs_Type(OctetString):
    """Custom type ciscoTsStackSwitchSPANMonitoredTrCRFs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CiscoTsStackSwitchSPANMonitoredTrCRFs_Type.__name__ = "OctetString"
_CiscoTsStackSwitchSPANMonitoredTrCRFs_Object = MibTableColumn
ciscoTsStackSwitchSPANMonitoredTrCRFs = _CiscoTsStackSwitchSPANMonitoredTrCRFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 29),
    _CiscoTsStackSwitchSPANMonitoredTrCRFs_Type()
)
ciscoTsStackSwitchSPANMonitoredTrCRFs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchSPANMonitoredTrCRFs.setStatus("mandatory")


class _CiscoTsStackSwitchPwrSupplyStatus_Type(Integer32):
    """Custom type ciscoTsStackSwitchPwrSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("external-backup-no-reset", 6),
          ("external-no-backup", 5),
          ("internal-backup-will-reset", 4),
          ("internal-no-backup", 3),
          ("internal-only", 2),
          ("unknown", 1))
    )


_CiscoTsStackSwitchPwrSupplyStatus_Type.__name__ = "Integer32"
_CiscoTsStackSwitchPwrSupplyStatus_Object = MibTableColumn
ciscoTsStackSwitchPwrSupplyStatus = _CiscoTsStackSwitchPwrSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 1, 1, 30),
    _CiscoTsStackSwitchPwrSupplyStatus_Type()
)
ciscoTsStackSwitchPwrSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsStackSwitchPwrSupplyStatus.setStatus("mandatory")
_CiscoTsModule_ObjectIdentity = ObjectIdentity
ciscoTsModule = _CiscoTsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3)
)
_CiscoTsModTable_Object = MibTable
ciscoTsModTable = _CiscoTsModTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoTsModTable.setStatus("mandatory")
_CiscoTsModEntry_Object = MibTableRow
ciscoTsModEntry = _CiscoTsModEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3, 1, 1)
)
ciscoTsModEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsModSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsModNumber"),
)
if mibBuilder.loadTexts:
    ciscoTsModEntry.setStatus("mandatory")


class _CiscoTsModSwitchNumber_Type(Integer32):
    """Custom type ciscoTsModSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoTsModSwitchNumber_Type.__name__ = "Integer32"
_CiscoTsModSwitchNumber_Object = MibTableColumn
ciscoTsModSwitchNumber = _CiscoTsModSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3, 1, 1, 1),
    _CiscoTsModSwitchNumber_Type()
)
ciscoTsModSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsModSwitchNumber.setStatus("mandatory")


class _CiscoTsModNumber_Type(Integer32):
    """Custom type ciscoTsModNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CiscoTsModNumber_Type.__name__ = "Integer32"
_CiscoTsModNumber_Object = MibTableColumn
ciscoTsModNumber = _CiscoTsModNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3, 1, 1, 2),
    _CiscoTsModNumber_Type()
)
ciscoTsModNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsModNumber.setStatus("mandatory")


class _CiscoTsModState_Type(Integer32):
    """Custom type ciscoTsModState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 3),
          ("nomodule", 1),
          ("running", 2))
    )


_CiscoTsModState_Type.__name__ = "Integer32"
_CiscoTsModState_Object = MibTableColumn
ciscoTsModState = _CiscoTsModState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3, 1, 1, 3),
    _CiscoTsModState_Type()
)
ciscoTsModState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsModState.setStatus("mandatory")


class _CiscoTsModType_Type(Integer32):
    """Custom type ciscoTsModType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 11),
          ("proPort4Fiber", 4),
          ("proPort4TR", 3),
          ("proPortATM155Fiber", 8),
          ("proPortATM155UTP", 9),
          ("proPortISL-FX", 5),
          ("proPortISL-TX", 6),
          ("proStack", 2),
          ("system", 1),
          ("unknown", 10))
    )


_CiscoTsModType_Type.__name__ = "Integer32"
_CiscoTsModType_Object = MibTableColumn
ciscoTsModType = _CiscoTsModType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3, 1, 1, 4),
    _CiscoTsModType_Type()
)
ciscoTsModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsModType.setStatus("mandatory")
_CiscoTsModRevision_Type = DisplayString
_CiscoTsModRevision_Object = MibTableColumn
ciscoTsModRevision = _CiscoTsModRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3, 1, 1, 5),
    _CiscoTsModRevision_Type()
)
ciscoTsModRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsModRevision.setStatus("mandatory")
_CiscoTsModFwVer_Type = DisplayString
_CiscoTsModFwVer_Object = MibTableColumn
ciscoTsModFwVer = _CiscoTsModFwVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3, 1, 1, 6),
    _CiscoTsModFwVer_Type()
)
ciscoTsModFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsModFwVer.setStatus("mandatory")
_CiscoTsModNumPorts_Type = Integer32
_CiscoTsModNumPorts_Object = MibTableColumn
ciscoTsModNumPorts = _CiscoTsModNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3, 1, 1, 7),
    _CiscoTsModNumPorts_Type()
)
ciscoTsModNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsModNumPorts.setStatus("mandatory")
_CiscoTsModUptime_Type = TimeTicks
_CiscoTsModUptime_Object = MibTableColumn
ciscoTsModUptime = _CiscoTsModUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 3, 1, 1, 8),
    _CiscoTsModUptime_Type()
)
ciscoTsModUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsModUptime.setStatus("mandatory")
_CiscoTsPort_ObjectIdentity = ObjectIdentity
ciscoTsPort = _CiscoTsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4)
)
_CiscoTsPortCfgTable_Object = MibTable
ciscoTsPortCfgTable = _CiscoTsPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1)
)
if mibBuilder.loadTexts:
    ciscoTsPortCfgTable.setStatus("mandatory")
_CiscoTsPortCfgEntry_Object = MibTableRow
ciscoTsPortCfgEntry = _CiscoTsPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1)
)
ciscoTsPortCfgEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsStackSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsPortCfgNumber"),
)
if mibBuilder.loadTexts:
    ciscoTsPortCfgEntry.setStatus("mandatory")


class _CiscoTsPortCfgNumber_Type(Integer32):
    """Custom type ciscoTsPortCfgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiscoTsPortCfgNumber_Type.__name__ = "Integer32"
_CiscoTsPortCfgNumber_Object = MibTableColumn
ciscoTsPortCfgNumber = _CiscoTsPortCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 1),
    _CiscoTsPortCfgNumber_Type()
)
ciscoTsPortCfgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortCfgNumber.setStatus("mandatory")


class _CiscoTsPortCfgModNumber_Type(Integer32):
    """Custom type ciscoTsPortCfgModNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CiscoTsPortCfgModNumber_Type.__name__ = "Integer32"
_CiscoTsPortCfgModNumber_Object = MibTableColumn
ciscoTsPortCfgModNumber = _CiscoTsPortCfgModNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 2),
    _CiscoTsPortCfgModNumber_Type()
)
ciscoTsPortCfgModNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortCfgModNumber.setStatus("mandatory")
_CiscoTsPortCfgIfIndex_Type = Integer32
_CiscoTsPortCfgIfIndex_Object = MibTableColumn
ciscoTsPortCfgIfIndex = _CiscoTsPortCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 3),
    _CiscoTsPortCfgIfIndex_Type()
)
ciscoTsPortCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortCfgIfIndex.setStatus("mandatory")


class _CiscoTsPortCfgResetStats_Type(Integer32):
    """Custom type ciscoTsPortCfgResetStats based on Integer32"""
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


_CiscoTsPortCfgResetStats_Type.__name__ = "Integer32"
_CiscoTsPortCfgResetStats_Object = MibTableColumn
ciscoTsPortCfgResetStats = _CiscoTsPortCfgResetStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 4),
    _CiscoTsPortCfgResetStats_Type()
)
ciscoTsPortCfgResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgResetStats.setStatus("mandatory")


class _CiscoTsPortCfgResetAddrs_Type(Integer32):
    """Custom type ciscoTsPortCfgResetAddrs based on Integer32"""
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


_CiscoTsPortCfgResetAddrs_Type.__name__ = "Integer32"
_CiscoTsPortCfgResetAddrs_Object = MibTableColumn
ciscoTsPortCfgResetAddrs = _CiscoTsPortCfgResetAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 5),
    _CiscoTsPortCfgResetAddrs_Type()
)
ciscoTsPortCfgResetAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgResetAddrs.setStatus("mandatory")


class _CiscoTsPortCfgAddrAgingTime_Type(Integer32):
    """Custom type ciscoTsPortCfgAddrAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CiscoTsPortCfgAddrAgingTime_Type.__name__ = "Integer32"
_CiscoTsPortCfgAddrAgingTime_Object = MibTableColumn
ciscoTsPortCfgAddrAgingTime = _CiscoTsPortCfgAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 6),
    _CiscoTsPortCfgAddrAgingTime_Type()
)
ciscoTsPortCfgAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgAddrAgingTime.setStatus("mandatory")


class _CiscoTsPortCfgDemandAgingLevel_Type(Integer32):
    """Custom type ciscoTsPortCfgDemandAgingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_CiscoTsPortCfgDemandAgingLevel_Type.__name__ = "Integer32"
_CiscoTsPortCfgDemandAgingLevel_Object = MibTableColumn
ciscoTsPortCfgDemandAgingLevel = _CiscoTsPortCfgDemandAgingLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 7),
    _CiscoTsPortCfgDemandAgingLevel_Type()
)
ciscoTsPortCfgDemandAgingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgDemandAgingLevel.setStatus("mandatory")


class _CiscoTsPortCfgErrLoThreshold_Type(Integer32):
    """Custom type ciscoTsPortCfgErrLoThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CiscoTsPortCfgErrLoThreshold_Type.__name__ = "Integer32"
_CiscoTsPortCfgErrLoThreshold_Object = MibTableColumn
ciscoTsPortCfgErrLoThreshold = _CiscoTsPortCfgErrLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 8),
    _CiscoTsPortCfgErrLoThreshold_Type()
)
ciscoTsPortCfgErrLoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgErrLoThreshold.setStatus("mandatory")


class _CiscoTsPortCfgErrHiThreshold_Type(Integer32):
    """Custom type ciscoTsPortCfgErrHiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CiscoTsPortCfgErrHiThreshold_Type.__name__ = "Integer32"
_CiscoTsPortCfgErrHiThreshold_Object = MibTableColumn
ciscoTsPortCfgErrHiThreshold = _CiscoTsPortCfgErrHiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 9),
    _CiscoTsPortCfgErrHiThreshold_Type()
)
ciscoTsPortCfgErrHiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgErrHiThreshold.setStatus("mandatory")


class _CiscoTsPortCfgErrSampling_Type(Integer32):
    """Custom type ciscoTsPortCfgErrSampling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CiscoTsPortCfgErrSampling_Type.__name__ = "Integer32"
_CiscoTsPortCfgErrSampling_Object = MibTableColumn
ciscoTsPortCfgErrSampling = _CiscoTsPortCfgErrSampling_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 10),
    _CiscoTsPortCfgErrSampling_Type()
)
ciscoTsPortCfgErrSampling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgErrSampling.setStatus("mandatory")
_CiscoTsPortCfgMaxTransmitUnit_Type = Integer32
_CiscoTsPortCfgMaxTransmitUnit_Object = MibTableColumn
ciscoTsPortCfgMaxTransmitUnit = _CiscoTsPortCfgMaxTransmitUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 11),
    _CiscoTsPortCfgMaxTransmitUnit_Type()
)
ciscoTsPortCfgMaxTransmitUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgMaxTransmitUnit.setStatus("mandatory")


class _CiscoTsPortCfgMaxExplorerRate_Type(Integer32):
    """Custom type ciscoTsPortCfgMaxExplorerRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5000),
    )


_CiscoTsPortCfgMaxExplorerRate_Type.__name__ = "Integer32"
_CiscoTsPortCfgMaxExplorerRate_Object = MibTableColumn
ciscoTsPortCfgMaxExplorerRate = _CiscoTsPortCfgMaxExplorerRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 12),
    _CiscoTsPortCfgMaxExplorerRate_Type()
)
ciscoTsPortCfgMaxExplorerRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgMaxExplorerRate.setStatus("mandatory")


class _CiscoTsPortCfgSetACbits_Type(Integer32):
    """Custom type ciscoTsPortCfgSetACbits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CiscoTsPortCfgSetACbits_Type.__name__ = "Integer32"
_CiscoTsPortCfgSetACbits_Object = MibTableColumn
ciscoTsPortCfgSetACbits = _CiscoTsPortCfgSetACbits_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 13),
    _CiscoTsPortCfgSetACbits_Type()
)
ciscoTsPortCfgSetACbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgSetACbits.setStatus("mandatory")


class _CiscoTsPortCfgEarlyTokenRlse_Type(Integer32):
    """Custom type ciscoTsPortCfgEarlyTokenRlse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CiscoTsPortCfgEarlyTokenRlse_Type.__name__ = "Integer32"
_CiscoTsPortCfgEarlyTokenRlse_Object = MibTableColumn
ciscoTsPortCfgEarlyTokenRlse = _CiscoTsPortCfgEarlyTokenRlse_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 14),
    _CiscoTsPortCfgEarlyTokenRlse_Type()
)
ciscoTsPortCfgEarlyTokenRlse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgEarlyTokenRlse.setStatus("mandatory")


class _CiscoTsPortCfgForwardingMode_Type(Integer32):
    """Custom type ciscoTsPortCfgForwardingMode based on Integer32"""
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
        *(("auto", 1),
          ("cutthru", 3),
          ("storeandforward", 2),
          ("unknown", 4))
    )


_CiscoTsPortCfgForwardingMode_Type.__name__ = "Integer32"
_CiscoTsPortCfgForwardingMode_Object = MibTableColumn
ciscoTsPortCfgForwardingMode = _CiscoTsPortCfgForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 15),
    _CiscoTsPortCfgForwardingMode_Type()
)
ciscoTsPortCfgForwardingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgForwardingMode.setStatus("mandatory")


class _CiscoTsPortCfgActualForwardingMode_Type(Integer32):
    """Custom type ciscoTsPortCfgActualForwardingMode based on Integer32"""
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
          ("storeandforward", 1),
          ("unknown", 3))
    )


_CiscoTsPortCfgActualForwardingMode_Type.__name__ = "Integer32"
_CiscoTsPortCfgActualForwardingMode_Object = MibTableColumn
ciscoTsPortCfgActualForwardingMode = _CiscoTsPortCfgActualForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 16),
    _CiscoTsPortCfgActualForwardingMode_Type()
)
ciscoTsPortCfgActualForwardingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortCfgActualForwardingMode.setStatus("mandatory")


class _CiscoTsPortCfgPortMode_Type(Integer32):
    """Custom type ciscoTsPortCfgPortMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fdx-Port", 4),
          ("fdx-Station", 5),
          ("hdx-Port", 2),
          ("hdx-Station", 3),
          ("passive-probe", 7),
          ("ri-ro", 6),
          ("unknown", 8))
    )


_CiscoTsPortCfgPortMode_Type.__name__ = "Integer32"
_CiscoTsPortCfgPortMode_Object = MibTableColumn
ciscoTsPortCfgPortMode = _CiscoTsPortCfgPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 17),
    _CiscoTsPortCfgPortMode_Type()
)
ciscoTsPortCfgPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgPortMode.setStatus("mandatory")


class _CiscoTsPortCfgActualPortMode_Type(Integer32):
    """Custom type ciscoTsPortCfgActualPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fdx-Port", 3),
          ("fdx-Station", 4),
          ("hdx-Port", 1),
          ("hdx-Station", 2),
          ("passive-probe", 6),
          ("ri-ro", 5),
          ("unknown", 7))
    )


_CiscoTsPortCfgActualPortMode_Type.__name__ = "Integer32"
_CiscoTsPortCfgActualPortMode_Object = MibTableColumn
ciscoTsPortCfgActualPortMode = _CiscoTsPortCfgActualPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 18),
    _CiscoTsPortCfgActualPortMode_Type()
)
ciscoTsPortCfgActualPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortCfgActualPortMode.setStatus("mandatory")


class _CiscoTsPortCfgPriorityThres_Type(Integer32):
    """Custom type ciscoTsPortCfgPriorityThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CiscoTsPortCfgPriorityThres_Type.__name__ = "Integer32"
_CiscoTsPortCfgPriorityThres_Object = MibTableColumn
ciscoTsPortCfgPriorityThres = _CiscoTsPortCfgPriorityThres_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 19),
    _CiscoTsPortCfgPriorityThres_Type()
)
ciscoTsPortCfgPriorityThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgPriorityThres.setStatus("mandatory")


class _CiscoTsPortCfgMinXmitPriority_Type(Integer32):
    """Custom type ciscoTsPortCfgMinXmitPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_CiscoTsPortCfgMinXmitPriority_Type.__name__ = "Integer32"
_CiscoTsPortCfgMinXmitPriority_Object = MibTableColumn
ciscoTsPortCfgMinXmitPriority = _CiscoTsPortCfgMinXmitPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 20),
    _CiscoTsPortCfgMinXmitPriority_Type()
)
ciscoTsPortCfgMinXmitPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgMinXmitPriority.setStatus("mandatory")


class _CiscoTsPortCfgCfgLossThres_Type(Integer32):
    """Custom type ciscoTsPortCfgCfgLossThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CiscoTsPortCfgCfgLossThres_Type.__name__ = "Integer32"
_CiscoTsPortCfgCfgLossThres_Object = MibTableColumn
ciscoTsPortCfgCfgLossThres = _CiscoTsPortCfgCfgLossThres_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 21),
    _CiscoTsPortCfgCfgLossThres_Type()
)
ciscoTsPortCfgCfgLossThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgCfgLossThres.setStatus("mandatory")


class _CiscoTsPortCfgCfgLossInterval_Type(Integer32):
    """Custom type ciscoTsPortCfgCfgLossInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CiscoTsPortCfgCfgLossInterval_Type.__name__ = "Integer32"
_CiscoTsPortCfgCfgLossInterval_Object = MibTableColumn
ciscoTsPortCfgCfgLossInterval = _CiscoTsPortCfgCfgLossInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 22),
    _CiscoTsPortCfgCfgLossInterval_Type()
)
ciscoTsPortCfgCfgLossInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgCfgLossInterval.setStatus("mandatory")


class _CiscoTsPortCfgBcastSuppresion_Type(Integer32):
    """Custom type ciscoTsPortCfgBcastSuppresion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CiscoTsPortCfgBcastSuppresion_Type.__name__ = "Integer32"
_CiscoTsPortCfgBcastSuppresion_Object = MibTableColumn
ciscoTsPortCfgBcastSuppresion = _CiscoTsPortCfgBcastSuppresion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 23),
    _CiscoTsPortCfgBcastSuppresion_Type()
)
ciscoTsPortCfgBcastSuppresion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgBcastSuppresion.setStatus("mandatory")


class _CiscoTsPortCfgCDPTimeToLive_Type(Integer32):
    """Custom type ciscoTsPortCfgCDPTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoTsPortCfgCDPTimeToLive_Type.__name__ = "Integer32"
_CiscoTsPortCfgCDPTimeToLive_Object = MibTableColumn
ciscoTsPortCfgCDPTimeToLive = _CiscoTsPortCfgCDPTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 24),
    _CiscoTsPortCfgCDPTimeToLive_Type()
)
ciscoTsPortCfgCDPTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgCDPTimeToLive.setStatus("mandatory")


class _CiscoTsPortCfgSpanningTreeMode_Type(Integer32):
    """Custom type ciscoTsPortCfgSpanningTreeMode based on Integer32"""
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
        *(("auto", 1),
          ("blocking", 3),
          ("forwarding", 2),
          ("unknown", 4))
    )


_CiscoTsPortCfgSpanningTreeMode_Type.__name__ = "Integer32"
_CiscoTsPortCfgSpanningTreeMode_Object = MibTableColumn
ciscoTsPortCfgSpanningTreeMode = _CiscoTsPortCfgSpanningTreeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 25),
    _CiscoTsPortCfgSpanningTreeMode_Type()
)
ciscoTsPortCfgSpanningTreeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgSpanningTreeMode.setStatus("mandatory")


class _CiscoTsPortCfgSecurityMode_Type(Integer32):
    """Custom type ciscoTsPortCfgSecurityMode based on Integer32"""
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
        *(("normal", 1),
          ("secure-dest-addrs", 3),
          ("secure-src-addrs", 2),
          ("secure-src-and-dest-addrs", 4))
    )


_CiscoTsPortCfgSecurityMode_Type.__name__ = "Integer32"
_CiscoTsPortCfgSecurityMode_Object = MibTableColumn
ciscoTsPortCfgSecurityMode = _CiscoTsPortCfgSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 26),
    _CiscoTsPortCfgSecurityMode_Type()
)
ciscoTsPortCfgSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgSecurityMode.setStatus("mandatory")


class _CiscoTsPortCfgSoftErrThreshold_Type(Integer32):
    """Custom type ciscoTsPortCfgSoftErrThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CiscoTsPortCfgSoftErrThreshold_Type.__name__ = "Integer32"
_CiscoTsPortCfgSoftErrThreshold_Object = MibTableColumn
ciscoTsPortCfgSoftErrThreshold = _CiscoTsPortCfgSoftErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 27),
    _CiscoTsPortCfgSoftErrThreshold_Type()
)
ciscoTsPortCfgSoftErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgSoftErrThreshold.setStatus("mandatory")


class _CiscoTsPortCfgSoftErrReportInterval_Type(Integer32):
    """Custom type ciscoTsPortCfgSoftErrReportInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoTsPortCfgSoftErrReportInterval_Type.__name__ = "Integer32"
_CiscoTsPortCfgSoftErrReportInterval_Object = MibTableColumn
ciscoTsPortCfgSoftErrReportInterval = _CiscoTsPortCfgSoftErrReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 28),
    _CiscoTsPortCfgSoftErrReportInterval_Type()
)
ciscoTsPortCfgSoftErrReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgSoftErrReportInterval.setStatus("mandatory")


class _CiscoTsPortCfgSoftErrorMonitoring_Type(Integer32):
    """Custom type ciscoTsPortCfgSoftErrorMonitoring based on Integer32"""
    defaultValue = 2

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


_CiscoTsPortCfgSoftErrorMonitoring_Type.__name__ = "Integer32"
_CiscoTsPortCfgSoftErrorMonitoring_Object = MibTableColumn
ciscoTsPortCfgSoftErrorMonitoring = _CiscoTsPortCfgSoftErrorMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 1, 1, 29),
    _CiscoTsPortCfgSoftErrorMonitoring_Type()
)
ciscoTsPortCfgSoftErrorMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPortCfgSoftErrorMonitoring.setStatus("mandatory")
_CiscoTsPortStatsTable_Object = MibTable
ciscoTsPortStatsTable = _CiscoTsPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2)
)
if mibBuilder.loadTexts:
    ciscoTsPortStatsTable.setStatus("mandatory")
_CiscoTsPortStatsEntry_Object = MibTableRow
ciscoTsPortStatsEntry = _CiscoTsPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1)
)
ciscoTsPortStatsEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsStackSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsPortStatsNumber"),
)
if mibBuilder.loadTexts:
    ciscoTsPortStatsEntry.setStatus("mandatory")


class _CiscoTsPortStatsNumber_Type(Integer32):
    """Custom type ciscoTsPortStatsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiscoTsPortStatsNumber_Type.__name__ = "Integer32"
_CiscoTsPortStatsNumber_Object = MibTableColumn
ciscoTsPortStatsNumber = _CiscoTsPortStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 1),
    _CiscoTsPortStatsNumber_Type()
)
ciscoTsPortStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsNumber.setStatus("mandatory")


class _CiscoTsPortStatsModNumber_Type(Integer32):
    """Custom type ciscoTsPortStatsModNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CiscoTsPortStatsModNumber_Type.__name__ = "Integer32"
_CiscoTsPortStatsModNumber_Object = MibTableColumn
ciscoTsPortStatsModNumber = _CiscoTsPortStatsModNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 2),
    _CiscoTsPortStatsModNumber_Type()
)
ciscoTsPortStatsModNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsModNumber.setStatus("mandatory")
_CiscoTsPortStatsIfIndex_Type = Integer32
_CiscoTsPortStatsIfIndex_Object = MibTableColumn
ciscoTsPortStatsIfIndex = _CiscoTsPortStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 3),
    _CiscoTsPortStatsIfIndex_Type()
)
ciscoTsPortStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsIfIndex.setStatus("mandatory")
_CiscoTsPortStatsRcvLocalFrames_Type = Counter32
_CiscoTsPortStatsRcvLocalFrames_Object = MibTableColumn
ciscoTsPortStatsRcvLocalFrames = _CiscoTsPortStatsRcvLocalFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 4),
    _CiscoTsPortStatsRcvLocalFrames_Type()
)
ciscoTsPortStatsRcvLocalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsRcvLocalFrames.setStatus("mandatory")
_CiscoTsPortStatsForwardedFrames_Type = Counter32
_CiscoTsPortStatsForwardedFrames_Object = MibTableColumn
ciscoTsPortStatsForwardedFrames = _CiscoTsPortStatsForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 5),
    _CiscoTsPortStatsForwardedFrames_Type()
)
ciscoTsPortStatsForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsForwardedFrames.setStatus("mandatory")
_CiscoTsPortStatsStations_Type = Counter32
_CiscoTsPortStatsStations_Object = MibTableColumn
ciscoTsPortStatsStations = _CiscoTsPortStatsStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 6),
    _CiscoTsPortStatsStations_Type()
)
ciscoTsPortStatsStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsStations.setStatus("mandatory")
_CiscoTsPortStatsSWHandledFrames_Type = Counter32
_CiscoTsPortStatsSWHandledFrames_Object = MibTableColumn
ciscoTsPortStatsSWHandledFrames = _CiscoTsPortStatsSWHandledFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 7),
    _CiscoTsPortStatsSWHandledFrames_Type()
)
ciscoTsPortStatsSWHandledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsSWHandledFrames.setStatus("mandatory")
_CiscoTsPortStatsLocalStations_Type = Counter32
_CiscoTsPortStatsLocalStations_Object = MibTableColumn
ciscoTsPortStatsLocalStations = _CiscoTsPortStatsLocalStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 8),
    _CiscoTsPortStatsLocalStations_Type()
)
ciscoTsPortStatsLocalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsLocalStations.setStatus("mandatory")
_CiscoTsPortStatsRemoteStations_Type = Counter32
_CiscoTsPortStatsRemoteStations_Object = MibTableColumn
ciscoTsPortStatsRemoteStations = _CiscoTsPortStatsRemoteStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 9),
    _CiscoTsPortStatsRemoteStations_Type()
)
ciscoTsPortStatsRemoteStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsRemoteStations.setStatus("mandatory")
_CiscoTsPortStatsUnknownStaFrames_Type = Counter32
_CiscoTsPortStatsUnknownStaFrames_Object = MibTableColumn
ciscoTsPortStatsUnknownStaFrames = _CiscoTsPortStatsUnknownStaFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 10),
    _CiscoTsPortStatsUnknownStaFrames_Type()
)
ciscoTsPortStatsUnknownStaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsUnknownStaFrames.setStatus("mandatory")
_CiscoTsPortStatsResetTimer_Type = TimeTicks
_CiscoTsPortStatsResetTimer_Object = MibTableColumn
ciscoTsPortStatsResetTimer = _CiscoTsPortStatsResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 11),
    _CiscoTsPortStatsResetTimer_Type()
)
ciscoTsPortStatsResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsResetTimer.setStatus("mandatory")
_CiscoTsPortStatsInFrames_Type = Counter32
_CiscoTsPortStatsInFrames_Object = MibTableColumn
ciscoTsPortStatsInFrames = _CiscoTsPortStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 12),
    _CiscoTsPortStatsInFrames_Type()
)
ciscoTsPortStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsInFrames.setStatus("mandatory")
_CiscoTsPortStatsOutFrames_Type = Counter32
_CiscoTsPortStatsOutFrames_Object = MibTableColumn
ciscoTsPortStatsOutFrames = _CiscoTsPortStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 13),
    _CiscoTsPortStatsOutFrames_Type()
)
ciscoTsPortStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsOutFrames.setStatus("mandatory")
_CiscoTsPortStatsLongFrames_Type = Counter32
_CiscoTsPortStatsLongFrames_Object = MibTableColumn
ciscoTsPortStatsLongFrames = _CiscoTsPortStatsLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 14),
    _CiscoTsPortStatsLongFrames_Type()
)
ciscoTsPortStatsLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsLongFrames.setStatus("mandatory")
_CiscoTsPortStatsShortFrames_Type = Counter32
_CiscoTsPortStatsShortFrames_Object = MibTableColumn
ciscoTsPortStatsShortFrames = _CiscoTsPortStatsShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 15),
    _CiscoTsPortStatsShortFrames_Type()
)
ciscoTsPortStatsShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsShortFrames.setStatus("mandatory")
_CiscoTsPortStatsInBufOverflows_Type = Counter32
_CiscoTsPortStatsInBufOverflows_Object = MibTableColumn
ciscoTsPortStatsInBufOverflows = _CiscoTsPortStatsInBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 16),
    _CiscoTsPortStatsInBufOverflows_Type()
)
ciscoTsPortStatsInBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsInBufOverflows.setStatus("mandatory")
_CiscoTsPortStatsOutBufOverflows_Type = Counter32
_CiscoTsPortStatsOutBufOverflows_Object = MibTableColumn
ciscoTsPortStatsOutBufOverflows = _CiscoTsPortStatsOutBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 17),
    _CiscoTsPortStatsOutBufOverflows_Type()
)
ciscoTsPortStatsOutBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsOutBufOverflows.setStatus("mandatory")
_CiscoTsPortStatsRcvBcasts_Type = Counter32
_CiscoTsPortStatsRcvBcasts_Object = MibTableColumn
ciscoTsPortStatsRcvBcasts = _CiscoTsPortStatsRcvBcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 18),
    _CiscoTsPortStatsRcvBcasts_Type()
)
ciscoTsPortStatsRcvBcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsRcvBcasts.setStatus("mandatory")
_CiscoTsPortStatsRcvMcasts_Type = Counter32
_CiscoTsPortStatsRcvMcasts_Object = MibTableColumn
ciscoTsPortStatsRcvMcasts = _CiscoTsPortStatsRcvMcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 19),
    _CiscoTsPortStatsRcvMcasts_Type()
)
ciscoTsPortStatsRcvMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsRcvMcasts.setStatus("mandatory")
_CiscoTsPortStatsSwitchedFrames_Type = Counter32
_CiscoTsPortStatsSwitchedFrames_Object = MibTableColumn
ciscoTsPortStatsSwitchedFrames = _CiscoTsPortStatsSwitchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 20),
    _CiscoTsPortStatsSwitchedFrames_Type()
)
ciscoTsPortStatsSwitchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsSwitchedFrames.setStatus("mandatory")
_CiscoTsPortStatsPktsInErrors_Type = Counter32
_CiscoTsPortStatsPktsInErrors_Object = MibTableColumn
ciscoTsPortStatsPktsInErrors = _CiscoTsPortStatsPktsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 21),
    _CiscoTsPortStatsPktsInErrors_Type()
)
ciscoTsPortStatsPktsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsPktsInErrors.setStatus("mandatory")
_CiscoTsPortStatsAddrChainOverflows_Type = Counter32
_CiscoTsPortStatsAddrChainOverflows_Object = MibTableColumn
ciscoTsPortStatsAddrChainOverflows = _CiscoTsPortStatsAddrChainOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 22),
    _CiscoTsPortStatsAddrChainOverflows_Type()
)
ciscoTsPortStatsAddrChainOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsAddrChainOverflows.setStatus("mandatory")
_CiscoTsPortStatsTableOverflows_Type = Counter32
_CiscoTsPortStatsTableOverflows_Object = MibTableColumn
ciscoTsPortStatsTableOverflows = _CiscoTsPortStatsTableOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 23),
    _CiscoTsPortStatsTableOverflows_Type()
)
ciscoTsPortStatsTableOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsTableOverflows.setStatus("mandatory")
_CiscoTsPortStatsCfgLoss_Type = Integer32
_CiscoTsPortStatsCfgLoss_Object = MibTableColumn
ciscoTsPortStatsCfgLoss = _CiscoTsPortStatsCfgLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 24),
    _CiscoTsPortStatsCfgLoss_Type()
)
ciscoTsPortStatsCfgLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsCfgLoss.setStatus("mandatory")


class _CiscoTsPortStatsCfgLossRC_Type(Integer32):
    """Custom type ciscoTsPortStatsCfgLossRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("heart-beat-fail", 4),
          ("lobe-test-fail", 2),
          ("no-cfg-loss", 7),
          ("tkp-mac-frame-rcv-in-txi-mode", 3),
          ("txi-new-station", 5),
          ("txi-protocol-error", 6),
          ("wire-fault", 1))
    )


_CiscoTsPortStatsCfgLossRC_Type.__name__ = "Integer32"
_CiscoTsPortStatsCfgLossRC_Object = MibTableColumn
ciscoTsPortStatsCfgLossRC = _CiscoTsPortStatsCfgLossRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 25),
    _CiscoTsPortStatsCfgLossRC_Type()
)
ciscoTsPortStatsCfgLossRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsCfgLossRC.setStatus("mandatory")


class _CiscoTsPortStatsTrCRF_Type(OctetString):
    """Custom type ciscoTsPortStatsTrCRF based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CiscoTsPortStatsTrCRF_Type.__name__ = "OctetString"
_CiscoTsPortStatsTrCRF_Object = MibTableColumn
ciscoTsPortStatsTrCRF = _CiscoTsPortStatsTrCRF_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 26),
    _CiscoTsPortStatsTrCRF_Type()
)
ciscoTsPortStatsTrCRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsTrCRF.setStatus("mandatory")


class _CiscoTsPortStatsAutoDisableRC_Type(Integer32):
    """Custom type ciscoTsPortStatsAutoDisableRC based on Integer32"""
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
        *(("disabled-by-DRiP", 5),
          ("not-disabled", 1),
          ("remove-received", 4),
          ("speed-error", 3),
          ("unknown", 2))
    )


_CiscoTsPortStatsAutoDisableRC_Type.__name__ = "Integer32"
_CiscoTsPortStatsAutoDisableRC_Object = MibTableColumn
ciscoTsPortStatsAutoDisableRC = _CiscoTsPortStatsAutoDisableRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 2, 1, 27),
    _CiscoTsPortStatsAutoDisableRC_Type()
)
ciscoTsPortStatsAutoDisableRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPortStatsAutoDisableRC.setStatus("mandatory")
_CiscoTsProbe_ObjectIdentity = ObjectIdentity
ciscoTsProbe = _CiscoTsProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 5)
)
_CiscoTsPassiveProbeTable_Object = MibTable
ciscoTsPassiveProbeTable = _CiscoTsPassiveProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 5, 1)
)
if mibBuilder.loadTexts:
    ciscoTsPassiveProbeTable.setStatus("mandatory")
_CiscoTsPassiveProbeEntry_Object = MibTableRow
ciscoTsPassiveProbeEntry = _CiscoTsPassiveProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 5, 1, 1)
)
ciscoTsPassiveProbeEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsStackSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsPassiveProbeIndex"),
)
if mibBuilder.loadTexts:
    ciscoTsPassiveProbeEntry.setStatus("mandatory")


class _CiscoTsPassiveProbeIndex_Type(Integer32):
    """Custom type ciscoTsPassiveProbeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CiscoTsPassiveProbeIndex_Type.__name__ = "Integer32"
_CiscoTsPassiveProbeIndex_Object = MibTableColumn
ciscoTsPassiveProbeIndex = _CiscoTsPassiveProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 5, 1, 1, 1),
    _CiscoTsPassiveProbeIndex_Type()
)
ciscoTsPassiveProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPassiveProbeIndex.setStatus("mandatory")


class _CiscoTsPassiveProbePort_Type(Integer32):
    """Custom type ciscoTsPassiveProbePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_CiscoTsPassiveProbePort_Type.__name__ = "Integer32"
_CiscoTsPassiveProbePort_Object = MibTableColumn
ciscoTsPassiveProbePort = _CiscoTsPassiveProbePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 5, 1, 1, 2),
    _CiscoTsPassiveProbePort_Type()
)
ciscoTsPassiveProbePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPassiveProbePort.setStatus("mandatory")


class _CiscoTsPassiveProbeMonitoredPort_Type(Integer32):
    """Custom type ciscoTsPassiveProbeMonitoredPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_CiscoTsPassiveProbeMonitoredPort_Type.__name__ = "Integer32"
_CiscoTsPassiveProbeMonitoredPort_Object = MibTableColumn
ciscoTsPassiveProbeMonitoredPort = _CiscoTsPassiveProbeMonitoredPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 5, 1, 1, 3),
    _CiscoTsPassiveProbeMonitoredPort_Type()
)
ciscoTsPassiveProbeMonitoredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsPassiveProbeMonitoredPort.setStatus("mandatory")


class _CiscoTsPassiveProbeDirection_Type(Integer32):
    """Custom type ciscoTsPassiveProbeDirection based on Integer32"""
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
          ("receive", 2),
          ("transmit", 1),
          ("unknown", 4))
    )


_CiscoTsPassiveProbeDirection_Type.__name__ = "Integer32"
_CiscoTsPassiveProbeDirection_Object = MibTableColumn
ciscoTsPassiveProbeDirection = _CiscoTsPassiveProbeDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 5, 1, 1, 4),
    _CiscoTsPassiveProbeDirection_Type()
)
ciscoTsPassiveProbeDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsPassiveProbeDirection.setStatus("mandatory")
_CiscoTsVLANS_ObjectIdentity = ObjectIdentity
ciscoTsVLANS = _CiscoTsVLANS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6)
)
_CiscoTsTrCRFInfoTable_Object = MibTable
ciscoTsTrCRFInfoTable = _CiscoTsTrCRFInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 1)
)
if mibBuilder.loadTexts:
    ciscoTsTrCRFInfoTable.setStatus("mandatory")
_CiscoTsTrCRFInfoEntry_Object = MibTableRow
ciscoTsTrCRFInfoEntry = _CiscoTsTrCRFInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 1, 1)
)
ciscoTsTrCRFInfoEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsTrCRFInfoTrCRFNumber"),
)
if mibBuilder.loadTexts:
    ciscoTsTrCRFInfoEntry.setStatus("mandatory")


class _CiscoTsTrCRFInfoTrCRFNumber_Type(Integer32):
    """Custom type ciscoTsTrCRFInfoTrCRFNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CiscoTsTrCRFInfoTrCRFNumber_Type.__name__ = "Integer32"
_CiscoTsTrCRFInfoTrCRFNumber_Object = MibTableColumn
ciscoTsTrCRFInfoTrCRFNumber = _CiscoTsTrCRFInfoTrCRFNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 1, 1, 1),
    _CiscoTsTrCRFInfoTrCRFNumber_Type()
)
ciscoTsTrCRFInfoTrCRFNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTrCRFInfoTrCRFNumber.setStatus("mandatory")


class _CiscoTsTrCRFInfoName_Type(DisplayString):
    """Custom type ciscoTsTrCRFInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CiscoTsTrCRFInfoName_Type.__name__ = "DisplayString"
_CiscoTsTrCRFInfoName_Object = MibTableColumn
ciscoTsTrCRFInfoName = _CiscoTsTrCRFInfoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 1, 1, 2),
    _CiscoTsTrCRFInfoName_Type()
)
ciscoTsTrCRFInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTrCRFInfoName.setStatus("mandatory")


class _CiscoTsTrCRFInfoSpanningTreeProtoSpecification_Type(Integer32):
    """Custom type ciscoTsTrCRFInfoSpanningTreeProtoSpecification based on Integer32"""
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
          ("cisco", 2),
          ("ieee", 3),
          ("none", 1))
    )


_CiscoTsTrCRFInfoSpanningTreeProtoSpecification_Type.__name__ = "Integer32"
_CiscoTsTrCRFInfoSpanningTreeProtoSpecification_Object = MibTableColumn
ciscoTsTrCRFInfoSpanningTreeProtoSpecification = _CiscoTsTrCRFInfoSpanningTreeProtoSpecification_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 1, 1, 3),
    _CiscoTsTrCRFInfoSpanningTreeProtoSpecification_Type()
)
ciscoTsTrCRFInfoSpanningTreeProtoSpecification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrCRFInfoSpanningTreeProtoSpecification.setStatus("mandatory")
_CiscoTsTrCRFInfoSpanningTreeBridgeForwardDelay_Type = Timeout
_CiscoTsTrCRFInfoSpanningTreeBridgeForwardDelay_Object = MibTableColumn
ciscoTsTrCRFInfoSpanningTreeBridgeForwardDelay = _CiscoTsTrCRFInfoSpanningTreeBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 1, 1, 4),
    _CiscoTsTrCRFInfoSpanningTreeBridgeForwardDelay_Type()
)
ciscoTsTrCRFInfoSpanningTreeBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrCRFInfoSpanningTreeBridgeForwardDelay.setStatus("mandatory")
_CiscoTsTrCRFInfoSpanningTreeBridgeHelloTime_Type = Timeout
_CiscoTsTrCRFInfoSpanningTreeBridgeHelloTime_Object = MibTableColumn
ciscoTsTrCRFInfoSpanningTreeBridgeHelloTime = _CiscoTsTrCRFInfoSpanningTreeBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 1, 1, 5),
    _CiscoTsTrCRFInfoSpanningTreeBridgeHelloTime_Type()
)
ciscoTsTrCRFInfoSpanningTreeBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrCRFInfoSpanningTreeBridgeHelloTime.setStatus("mandatory")
_CiscoTsTrCRFInfoSpanningTreeBridgeMaxAge_Type = Timeout
_CiscoTsTrCRFInfoSpanningTreeBridgeMaxAge_Object = MibTableColumn
ciscoTsTrCRFInfoSpanningTreeBridgeMaxAge = _CiscoTsTrCRFInfoSpanningTreeBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 1, 1, 6),
    _CiscoTsTrCRFInfoSpanningTreeBridgeMaxAge_Type()
)
ciscoTsTrCRFInfoSpanningTreeBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrCRFInfoSpanningTreeBridgeMaxAge.setStatus("mandatory")


class _CiscoTsTrCRFInfoSpanningTreeInternalPortMode_Type(Integer32):
    """Custom type ciscoTsTrCRFInfoSpanningTreeInternalPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("blocking", 3),
          ("forwarding", 2))
    )


_CiscoTsTrCRFInfoSpanningTreeInternalPortMode_Type.__name__ = "Integer32"
_CiscoTsTrCRFInfoSpanningTreeInternalPortMode_Object = MibTableColumn
ciscoTsTrCRFInfoSpanningTreeInternalPortMode = _CiscoTsTrCRFInfoSpanningTreeInternalPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 1, 1, 7),
    _CiscoTsTrCRFInfoSpanningTreeInternalPortMode_Type()
)
ciscoTsTrCRFInfoSpanningTreeInternalPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrCRFInfoSpanningTreeInternalPortMode.setStatus("mandatory")
_CiscoTsTrBRFInfoTable_Object = MibTable
ciscoTsTrBRFInfoTable = _CiscoTsTrBRFInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 2)
)
if mibBuilder.loadTexts:
    ciscoTsTrBRFInfoTable.setStatus("mandatory")
_CiscoTsTrBRFInfoEntry_Object = MibTableRow
ciscoTsTrBRFInfoEntry = _CiscoTsTrBRFInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 2, 1)
)
ciscoTsTrBRFInfoEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsTrBRFInfoTrBRFNumber"),
)
if mibBuilder.loadTexts:
    ciscoTsTrBRFInfoEntry.setStatus("mandatory")


class _CiscoTsTrBRFInfoTrBRFNumber_Type(Integer32):
    """Custom type ciscoTsTrBRFInfoTrBRFNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CiscoTsTrBRFInfoTrBRFNumber_Type.__name__ = "Integer32"
_CiscoTsTrBRFInfoTrBRFNumber_Object = MibTableColumn
ciscoTsTrBRFInfoTrBRFNumber = _CiscoTsTrBRFInfoTrBRFNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 2, 1, 1),
    _CiscoTsTrBRFInfoTrBRFNumber_Type()
)
ciscoTsTrBRFInfoTrBRFNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTrBRFInfoTrBRFNumber.setStatus("mandatory")


class _CiscoTsTrBRFInfoName_Type(DisplayString):
    """Custom type ciscoTsTrBRFInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CiscoTsTrBRFInfoName_Type.__name__ = "DisplayString"
_CiscoTsTrBRFInfoName_Object = MibTableColumn
ciscoTsTrBRFInfoName = _CiscoTsTrBRFInfoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 2, 1, 2),
    _CiscoTsTrBRFInfoName_Type()
)
ciscoTsTrBRFInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTrBRFInfoName.setStatus("mandatory")


class _CiscoTsTrBRFInfoIpState_Type(Integer32):
    """Custom type ciscoTsTrBRFInfoIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp-always", 3),
          ("bootp-when-needed", 2),
          ("ip-disabled", 1))
    )


_CiscoTsTrBRFInfoIpState_Type.__name__ = "Integer32"
_CiscoTsTrBRFInfoIpState_Object = MibTableColumn
ciscoTsTrBRFInfoIpState = _CiscoTsTrBRFInfoIpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 2, 1, 3),
    _CiscoTsTrBRFInfoIpState_Type()
)
ciscoTsTrBRFInfoIpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrBRFInfoIpState.setStatus("mandatory")
_CiscoTsTrBRFInfoIpAddress_Type = IpAddress
_CiscoTsTrBRFInfoIpAddress_Object = MibTableColumn
ciscoTsTrBRFInfoIpAddress = _CiscoTsTrBRFInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 2, 1, 4),
    _CiscoTsTrBRFInfoIpAddress_Type()
)
ciscoTsTrBRFInfoIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrBRFInfoIpAddress.setStatus("mandatory")
_CiscoTsTrBRFInfoIpSubnetMask_Type = IpAddress
_CiscoTsTrBRFInfoIpSubnetMask_Object = MibTableColumn
ciscoTsTrBRFInfoIpSubnetMask = _CiscoTsTrBRFInfoIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 2, 1, 5),
    _CiscoTsTrBRFInfoIpSubnetMask_Type()
)
ciscoTsTrBRFInfoIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrBRFInfoIpSubnetMask.setStatus("mandatory")
_CiscoTsTrBRFInfoIpDefaultGateway_Type = IpAddress
_CiscoTsTrBRFInfoIpDefaultGateway_Object = MibTableColumn
ciscoTsTrBRFInfoIpDefaultGateway = _CiscoTsTrBRFInfoIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 2, 1, 6),
    _CiscoTsTrBRFInfoIpDefaultGateway_Type()
)
ciscoTsTrBRFInfoIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrBRFInfoIpDefaultGateway.setStatus("mandatory")


class _CiscoTsTrBRFInfoStpMode_Type(Integer32):
    """Custom type ciscoTsTrBRFInfoStpMode based on Integer32"""
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


_CiscoTsTrBRFInfoStpMode_Type.__name__ = "Integer32"
_CiscoTsTrBRFInfoStpMode_Object = MibTableColumn
ciscoTsTrBRFInfoStpMode = _CiscoTsTrBRFInfoStpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 2, 1, 7),
    _CiscoTsTrBRFInfoStpMode_Type()
)
ciscoTsTrBRFInfoStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrBRFInfoStpMode.setStatus("mandatory")


class _CiscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr_Type(Integer32):
    """Custom type ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CiscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr_Type.__name__ = "Integer32"
_CiscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr_Object = MibTableColumn
ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr = _CiscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 2, 1, 8),
    _CiscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr_Type()
)
ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr.setStatus("mandatory")


class _CiscoTsTransitedConfiguredTrCRFs_Type(OctetString):
    """Custom type ciscoTsTransitedConfiguredTrCRFs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CiscoTsTransitedConfiguredTrCRFs_Type.__name__ = "OctetString"
_CiscoTsTransitedConfiguredTrCRFs_Object = MibScalar
ciscoTsTransitedConfiguredTrCRFs = _CiscoTsTransitedConfiguredTrCRFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 3),
    _CiscoTsTransitedConfiguredTrCRFs_Type()
)
ciscoTsTransitedConfiguredTrCRFs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTransitedConfiguredTrCRFs.setStatus("mandatory")


class _CiscoTsTransitedTrCRFs_Type(OctetString):
    """Custom type ciscoTsTransitedTrCRFs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CiscoTsTransitedTrCRFs_Type.__name__ = "OctetString"
_CiscoTsTransitedTrCRFs_Object = MibScalar
ciscoTsTransitedTrCRFs = _CiscoTsTransitedTrCRFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 4),
    _CiscoTsTransitedTrCRFs_Type()
)
ciscoTsTransitedTrCRFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTransitedTrCRFs.setStatus("mandatory")


class _CiscoTsTransitedConfiguredTrBRFs_Type(OctetString):
    """Custom type ciscoTsTransitedConfiguredTrBRFs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CiscoTsTransitedConfiguredTrBRFs_Type.__name__ = "OctetString"
_CiscoTsTransitedConfiguredTrBRFs_Object = MibScalar
ciscoTsTransitedConfiguredTrBRFs = _CiscoTsTransitedConfiguredTrBRFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 5),
    _CiscoTsTransitedConfiguredTrBRFs_Type()
)
ciscoTsTransitedConfiguredTrBRFs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTransitedConfiguredTrBRFs.setStatus("mandatory")


class _CiscoTsTransitedTrBRFs_Type(OctetString):
    """Custom type ciscoTsTransitedTrBRFs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CiscoTsTransitedTrBRFs_Type.__name__ = "OctetString"
_CiscoTsTransitedTrBRFs_Object = MibScalar
ciscoTsTransitedTrBRFs = _CiscoTsTransitedTrBRFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 6),
    _CiscoTsTransitedTrBRFs_Type()
)
ciscoTsTransitedTrBRFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTransitedTrBRFs.setStatus("mandatory")
_CiscoTsTChannel_ObjectIdentity = ObjectIdentity
ciscoTsTChannel = _CiscoTsTChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 7)
)
_CiscoTsTCTable_Object = MibTable
ciscoTsTCTable = _CiscoTsTCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 7, 1)
)
if mibBuilder.loadTexts:
    ciscoTsTCTable.setStatus("mandatory")
_CiscoTsTCEntry_Object = MibTableRow
ciscoTsTCEntry = _CiscoTsTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 7, 1, 1)
)
ciscoTsTCEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsTCSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsTCNumber"),
)
if mibBuilder.loadTexts:
    ciscoTsTCEntry.setStatus("mandatory")


class _CiscoTsTCSwitchNumber_Type(Integer32):
    """Custom type ciscoTsTCSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoTsTCSwitchNumber_Type.__name__ = "Integer32"
_CiscoTsTCSwitchNumber_Object = MibTableColumn
ciscoTsTCSwitchNumber = _CiscoTsTCSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 7, 1, 1, 1),
    _CiscoTsTCSwitchNumber_Type()
)
ciscoTsTCSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTCSwitchNumber.setStatus("mandatory")


class _CiscoTsTCNumber_Type(Integer32):
    """Custom type ciscoTsTCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoTsTCNumber_Type.__name__ = "Integer32"
_CiscoTsTCNumber_Object = MibTableColumn
ciscoTsTCNumber = _CiscoTsTCNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 7, 1, 1, 2),
    _CiscoTsTCNumber_Type()
)
ciscoTsTCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTCNumber.setStatus("mandatory")


class _CiscoTsTCPorts_Type(OctetString):
    """Custom type ciscoTsTCPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoTsTCPorts_Type.__name__ = "OctetString"
_CiscoTsTCPorts_Object = MibTableColumn
ciscoTsTCPorts = _CiscoTsTCPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 7, 1, 1, 3),
    _CiscoTsTCPorts_Type()
)
ciscoTsTCPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTCPorts.setStatus("mandatory")


class _CiscoTsTCStatus_Type(Integer32):
    """Custom type ciscoTsTCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("reduced", 3),
          ("up", 1))
    )


_CiscoTsTCStatus_Type.__name__ = "Integer32"
_CiscoTsTCStatus_Object = MibTableColumn
ciscoTsTCStatus = _CiscoTsTCStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 7, 1, 1, 4),
    _CiscoTsTCStatus_Type()
)
ciscoTsTCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTCStatus.setStatus("mandatory")


class _CiscoTsTCActivePorts_Type(OctetString):
    """Custom type ciscoTsTCActivePorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoTsTCActivePorts_Type.__name__ = "OctetString"
_CiscoTsTCActivePorts_Object = MibTableColumn
ciscoTsTCActivePorts = _CiscoTsTCActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 7, 1, 1, 5),
    _CiscoTsTCActivePorts_Type()
)
ciscoTsTCActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTCActivePorts.setStatus("mandatory")
_CiscoTsFilter_ObjectIdentity = ObjectIdentity
ciscoTsFilter = _CiscoTsFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8)
)
_CiscoTsProtocolClassFilterTable_Object = MibTable
ciscoTsProtocolClassFilterTable = _CiscoTsProtocolClassFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 1)
)
if mibBuilder.loadTexts:
    ciscoTsProtocolClassFilterTable.setStatus("mandatory")
_CiscoTsProtocolClassFilterEntry_Object = MibTableRow
ciscoTsProtocolClassFilterEntry = _CiscoTsProtocolClassFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 1, 1)
)
ciscoTsProtocolClassFilterEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsProtocolClassFilterIndex"),
)
if mibBuilder.loadTexts:
    ciscoTsProtocolClassFilterEntry.setStatus("mandatory")


class _CiscoTsProtocolClassFilterIndex_Type(Integer32):
    """Custom type ciscoTsProtocolClassFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CiscoTsProtocolClassFilterIndex_Type.__name__ = "Integer32"
_CiscoTsProtocolClassFilterIndex_Object = MibTableColumn
ciscoTsProtocolClassFilterIndex = _CiscoTsProtocolClassFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 1, 1, 1),
    _CiscoTsProtocolClassFilterIndex_Type()
)
ciscoTsProtocolClassFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsProtocolClassFilterIndex.setStatus("mandatory")
_CiscoTsProtocolClassFilterEtype_Type = OctetString
_CiscoTsProtocolClassFilterEtype_Object = MibTableColumn
ciscoTsProtocolClassFilterEtype = _CiscoTsProtocolClassFilterEtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 1, 1, 2),
    _CiscoTsProtocolClassFilterEtype_Type()
)
ciscoTsProtocolClassFilterEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsProtocolClassFilterEtype.setStatus("mandatory")
_CiscoTsProtocolClassFilterDSAPs_Type = OctetString
_CiscoTsProtocolClassFilterDSAPs_Object = MibTableColumn
ciscoTsProtocolClassFilterDSAPs = _CiscoTsProtocolClassFilterDSAPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 1, 1, 3),
    _CiscoTsProtocolClassFilterDSAPs_Type()
)
ciscoTsProtocolClassFilterDSAPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsProtocolClassFilterDSAPs.setStatus("mandatory")
_CiscoTsProtocolFilterTable_Object = MibTable
ciscoTsProtocolFilterTable = _CiscoTsProtocolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 2)
)
if mibBuilder.loadTexts:
    ciscoTsProtocolFilterTable.setStatus("mandatory")
_CiscoTsProtocolFilterEntry_Object = MibTableRow
ciscoTsProtocolFilterEntry = _CiscoTsProtocolFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 2, 1)
)
ciscoTsProtocolFilterEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsStackSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsProtocolFilterPort"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsProtocolClassFilterIndex"),
)
if mibBuilder.loadTexts:
    ciscoTsProtocolFilterEntry.setStatus("mandatory")


class _CiscoTsProtocolFilterPort_Type(Integer32):
    """Custom type ciscoTsProtocolFilterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiscoTsProtocolFilterPort_Type.__name__ = "Integer32"
_CiscoTsProtocolFilterPort_Object = MibTableColumn
ciscoTsProtocolFilterPort = _CiscoTsProtocolFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 2, 1, 1),
    _CiscoTsProtocolFilterPort_Type()
)
ciscoTsProtocolFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsProtocolFilterPort.setStatus("mandatory")


class _CiscoTsProtocolFilterBlockingMode_Type(Integer32):
    """Custom type ciscoTsProtocolFilterBlockingMode based on Integer32"""
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
        *(("all", 1),
          ("none", 4),
          ("nsr", 3),
          ("sr", 2))
    )


_CiscoTsProtocolFilterBlockingMode_Type.__name__ = "Integer32"
_CiscoTsProtocolFilterBlockingMode_Object = MibTableColumn
ciscoTsProtocolFilterBlockingMode = _CiscoTsProtocolFilterBlockingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 2, 1, 2),
    _CiscoTsProtocolFilterBlockingMode_Type()
)
ciscoTsProtocolFilterBlockingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsProtocolFilterBlockingMode.setStatus("mandatory")


class _CiscoTsProtocolFilterTranspMode_Type(Integer32):
    """Custom type ciscoTsProtocolFilterTranspMode based on Integer32"""
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


_CiscoTsProtocolFilterTranspMode_Type.__name__ = "Integer32"
_CiscoTsProtocolFilterTranspMode_Object = MibTableColumn
ciscoTsProtocolFilterTranspMode = _CiscoTsProtocolFilterTranspMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 2, 1, 3),
    _CiscoTsProtocolFilterTranspMode_Type()
)
ciscoTsProtocolFilterTranspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsProtocolFilterTranspMode.setStatus("mandatory")
_CiscoTsMACDestFilterTable_Object = MibTable
ciscoTsMACDestFilterTable = _CiscoTsMACDestFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 3)
)
if mibBuilder.loadTexts:
    ciscoTsMACDestFilterTable.setStatus("mandatory")
_CiscoTsMACDestFilterEntry_Object = MibTableRow
ciscoTsMACDestFilterEntry = _CiscoTsMACDestFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 3, 1)
)
ciscoTsMACDestFilterEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsMACDestFilterSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsMACDestFilterStationAddress"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsMACDestFilterType"),
)
if mibBuilder.loadTexts:
    ciscoTsMACDestFilterEntry.setStatus("mandatory")


class _CiscoTsMACDestFilterSwitchNumber_Type(Integer32):
    """Custom type ciscoTsMACDestFilterSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoTsMACDestFilterSwitchNumber_Type.__name__ = "Integer32"
_CiscoTsMACDestFilterSwitchNumber_Object = MibTableColumn
ciscoTsMACDestFilterSwitchNumber = _CiscoTsMACDestFilterSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 3, 1, 1),
    _CiscoTsMACDestFilterSwitchNumber_Type()
)
ciscoTsMACDestFilterSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsMACDestFilterSwitchNumber.setStatus("mandatory")
_CiscoTsMACDestFilterStationAddress_Type = MacAddr
_CiscoTsMACDestFilterStationAddress_Object = MibTableColumn
ciscoTsMACDestFilterStationAddress = _CiscoTsMACDestFilterStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 3, 1, 2),
    _CiscoTsMACDestFilterStationAddress_Type()
)
ciscoTsMACDestFilterStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsMACDestFilterStationAddress.setStatus("mandatory")


class _CiscoTsMACDestFilterType_Type(Integer32):
    """Custom type ciscoTsMACDestFilterType based on Integer32"""
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
        *(("allow-dest", 2),
          ("block-dest", 1),
          ("force-dest", 4),
          ("limited-multicast", 3))
    )


_CiscoTsMACDestFilterType_Type.__name__ = "Integer32"
_CiscoTsMACDestFilterType_Object = MibTableColumn
ciscoTsMACDestFilterType = _CiscoTsMACDestFilterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 3, 1, 3),
    _CiscoTsMACDestFilterType_Type()
)
ciscoTsMACDestFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsMACDestFilterType.setStatus("mandatory")


class _CiscoTsMACDestFilterPorts_Type(OctetString):
    """Custom type ciscoTsMACDestFilterPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoTsMACDestFilterPorts_Type.__name__ = "OctetString"
_CiscoTsMACDestFilterPorts_Object = MibTableColumn
ciscoTsMACDestFilterPorts = _CiscoTsMACDestFilterPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 3, 1, 4),
    _CiscoTsMACDestFilterPorts_Type()
)
ciscoTsMACDestFilterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsMACDestFilterPorts.setStatus("mandatory")


class _CiscoTsMACDestFilterExitMask_Type(OctetString):
    """Custom type ciscoTsMACDestFilterExitMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoTsMACDestFilterExitMask_Type.__name__ = "OctetString"
_CiscoTsMACDestFilterExitMask_Object = MibTableColumn
ciscoTsMACDestFilterExitMask = _CiscoTsMACDestFilterExitMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 3, 1, 5),
    _CiscoTsMACDestFilterExitMask_Type()
)
ciscoTsMACDestFilterExitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsMACDestFilterExitMask.setStatus("mandatory")


class _CiscoTsMACDestFilterRemoteBox_Type(Integer32):
    """Custom type ciscoTsMACDestFilterRemoteBox based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoTsMACDestFilterRemoteBox_Type.__name__ = "Integer32"
_CiscoTsMACDestFilterRemoteBox_Object = MibTableColumn
ciscoTsMACDestFilterRemoteBox = _CiscoTsMACDestFilterRemoteBox_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 3, 1, 6),
    _CiscoTsMACDestFilterRemoteBox_Type()
)
ciscoTsMACDestFilterRemoteBox.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsMACDestFilterRemoteBox.setStatus("mandatory")


class _CiscoTsMACDestFilterRemotePort_Type(Integer32):
    """Custom type ciscoTsMACDestFilterRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiscoTsMACDestFilterRemotePort_Type.__name__ = "Integer32"
_CiscoTsMACDestFilterRemotePort_Object = MibTableColumn
ciscoTsMACDestFilterRemotePort = _CiscoTsMACDestFilterRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 3, 1, 7),
    _CiscoTsMACDestFilterRemotePort_Type()
)
ciscoTsMACDestFilterRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsMACDestFilterRemotePort.setStatus("mandatory")


class _CiscoTsMACDestFilterStatus_Type(Integer32):
    """Custom type ciscoTsMACDestFilterStatus based on Integer32"""
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


_CiscoTsMACDestFilterStatus_Type.__name__ = "Integer32"
_CiscoTsMACDestFilterStatus_Object = MibTableColumn
ciscoTsMACDestFilterStatus = _CiscoTsMACDestFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 3, 1, 8),
    _CiscoTsMACDestFilterStatus_Type()
)
ciscoTsMACDestFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsMACDestFilterStatus.setStatus("mandatory")
_CiscoTsMACSourceFilterTable_Object = MibTable
ciscoTsMACSourceFilterTable = _CiscoTsMACSourceFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 4)
)
if mibBuilder.loadTexts:
    ciscoTsMACSourceFilterTable.setStatus("mandatory")
_CiscoTsMACSourceFilterEntry_Object = MibTableRow
ciscoTsMACSourceFilterEntry = _CiscoTsMACSourceFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 4, 1)
)
ciscoTsMACSourceFilterEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsMACSourceFilterSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsMACSourceFilterStationAddress"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsMACSourceFilterType"),
)
if mibBuilder.loadTexts:
    ciscoTsMACSourceFilterEntry.setStatus("mandatory")


class _CiscoTsMACSourceFilterSwitchNumber_Type(Integer32):
    """Custom type ciscoTsMACSourceFilterSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoTsMACSourceFilterSwitchNumber_Type.__name__ = "Integer32"
_CiscoTsMACSourceFilterSwitchNumber_Object = MibTableColumn
ciscoTsMACSourceFilterSwitchNumber = _CiscoTsMACSourceFilterSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 4, 1, 1),
    _CiscoTsMACSourceFilterSwitchNumber_Type()
)
ciscoTsMACSourceFilterSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsMACSourceFilterSwitchNumber.setStatus("mandatory")
_CiscoTsMACSourceFilterStationAddress_Type = MacAddr
_CiscoTsMACSourceFilterStationAddress_Object = MibTableColumn
ciscoTsMACSourceFilterStationAddress = _CiscoTsMACSourceFilterStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 4, 1, 2),
    _CiscoTsMACSourceFilterStationAddress_Type()
)
ciscoTsMACSourceFilterStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsMACSourceFilterStationAddress.setStatus("mandatory")


class _CiscoTsMACSourceFilterType_Type(Integer32):
    """Custom type ciscoTsMACSourceFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow-source", 2),
          ("block-source", 1))
    )


_CiscoTsMACSourceFilterType_Type.__name__ = "Integer32"
_CiscoTsMACSourceFilterType_Object = MibTableColumn
ciscoTsMACSourceFilterType = _CiscoTsMACSourceFilterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 4, 1, 3),
    _CiscoTsMACSourceFilterType_Type()
)
ciscoTsMACSourceFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsMACSourceFilterType.setStatus("mandatory")


class _CiscoTsMACSourceFilterPorts_Type(OctetString):
    """Custom type ciscoTsMACSourceFilterPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoTsMACSourceFilterPorts_Type.__name__ = "OctetString"
_CiscoTsMACSourceFilterPorts_Object = MibTableColumn
ciscoTsMACSourceFilterPorts = _CiscoTsMACSourceFilterPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 4, 1, 4),
    _CiscoTsMACSourceFilterPorts_Type()
)
ciscoTsMACSourceFilterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsMACSourceFilterPorts.setStatus("mandatory")


class _CiscoTsMACSourceFilterStatus_Type(Integer32):
    """Custom type ciscoTsMACSourceFilterStatus based on Integer32"""
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


_CiscoTsMACSourceFilterStatus_Type.__name__ = "Integer32"
_CiscoTsMACSourceFilterStatus_Object = MibTableColumn
ciscoTsMACSourceFilterStatus = _CiscoTsMACSourceFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 4, 1, 5),
    _CiscoTsMACSourceFilterStatus_Type()
)
ciscoTsMACSourceFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsMACSourceFilterStatus.setStatus("mandatory")
_CiscoTsDupAddrFilterTable_Object = MibTable
ciscoTsDupAddrFilterTable = _CiscoTsDupAddrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 5)
)
if mibBuilder.loadTexts:
    ciscoTsDupAddrFilterTable.setStatus("mandatory")
_CiscoTsDupAddrFilterEntry_Object = MibTableRow
ciscoTsDupAddrFilterEntry = _CiscoTsDupAddrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 5, 1)
)
ciscoTsDupAddrFilterEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsDupAddrFilterSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsDupAddrFilterStationAddress"),
)
if mibBuilder.loadTexts:
    ciscoTsDupAddrFilterEntry.setStatus("mandatory")


class _CiscoTsDupAddrFilterSwitchNumber_Type(Integer32):
    """Custom type ciscoTsDupAddrFilterSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoTsDupAddrFilterSwitchNumber_Type.__name__ = "Integer32"
_CiscoTsDupAddrFilterSwitchNumber_Object = MibTableColumn
ciscoTsDupAddrFilterSwitchNumber = _CiscoTsDupAddrFilterSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 5, 1, 1),
    _CiscoTsDupAddrFilterSwitchNumber_Type()
)
ciscoTsDupAddrFilterSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsDupAddrFilterSwitchNumber.setStatus("mandatory")
_CiscoTsDupAddrFilterStationAddress_Type = MacAddr
_CiscoTsDupAddrFilterStationAddress_Object = MibTableColumn
ciscoTsDupAddrFilterStationAddress = _CiscoTsDupAddrFilterStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 5, 1, 2),
    _CiscoTsDupAddrFilterStationAddress_Type()
)
ciscoTsDupAddrFilterStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsDupAddrFilterStationAddress.setStatus("mandatory")


class _CiscoTsDupAddrFilterPorts_Type(OctetString):
    """Custom type ciscoTsDupAddrFilterPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CiscoTsDupAddrFilterPorts_Type.__name__ = "OctetString"
_CiscoTsDupAddrFilterPorts_Object = MibTableColumn
ciscoTsDupAddrFilterPorts = _CiscoTsDupAddrFilterPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 5, 1, 3),
    _CiscoTsDupAddrFilterPorts_Type()
)
ciscoTsDupAddrFilterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsDupAddrFilterPorts.setStatus("mandatory")
_CiscoTsTrunkProtocolFilterTable_Object = MibTable
ciscoTsTrunkProtocolFilterTable = _CiscoTsTrunkProtocolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 6)
)
if mibBuilder.loadTexts:
    ciscoTsTrunkProtocolFilterTable.setStatus("mandatory")
_CiscoTsTrunkProtocolFilterEntry_Object = MibTableRow
ciscoTsTrunkProtocolFilterEntry = _CiscoTsTrunkProtocolFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 6, 1)
)
ciscoTsTrunkProtocolFilterEntry.setIndexNames(
    (0, "CISCO-TS-STACK-MIB", "ciscoTsStackSwitchNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsTrunkProtocolFilterPort"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsTrCRFInfoTrCRFNumber"),
    (0, "CISCO-TS-STACK-MIB", "ciscoTsProtocolClassFilterIndex"),
)
if mibBuilder.loadTexts:
    ciscoTsTrunkProtocolFilterEntry.setStatus("mandatory")


class _CiscoTsTrunkProtocolFilterPort_Type(Integer32):
    """Custom type ciscoTsTrunkProtocolFilterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiscoTsTrunkProtocolFilterPort_Type.__name__ = "Integer32"
_CiscoTsTrunkProtocolFilterPort_Object = MibTableColumn
ciscoTsTrunkProtocolFilterPort = _CiscoTsTrunkProtocolFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 6, 1, 1),
    _CiscoTsTrunkProtocolFilterPort_Type()
)
ciscoTsTrunkProtocolFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTsTrunkProtocolFilterPort.setStatus("mandatory")


class _CiscoTsTrunkProtocolFilterBlockingMode_Type(Integer32):
    """Custom type ciscoTsTrunkProtocolFilterBlockingMode based on Integer32"""
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
        *(("all", 1),
          ("none", 4),
          ("nsr", 3),
          ("sr", 2))
    )


_CiscoTsTrunkProtocolFilterBlockingMode_Type.__name__ = "Integer32"
_CiscoTsTrunkProtocolFilterBlockingMode_Object = MibTableColumn
ciscoTsTrunkProtocolFilterBlockingMode = _CiscoTsTrunkProtocolFilterBlockingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 6, 1, 2),
    _CiscoTsTrunkProtocolFilterBlockingMode_Type()
)
ciscoTsTrunkProtocolFilterBlockingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrunkProtocolFilterBlockingMode.setStatus("mandatory")


class _CiscoTsTrunkProtocolFilterTranspMode_Type(Integer32):
    """Custom type ciscoTsTrunkProtocolFilterTranspMode based on Integer32"""
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


_CiscoTsTrunkProtocolFilterTranspMode_Type.__name__ = "Integer32"
_CiscoTsTrunkProtocolFilterTranspMode_Object = MibTableColumn
ciscoTsTrunkProtocolFilterTranspMode = _CiscoTsTrunkProtocolFilterTranspMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 8, 6, 1, 3),
    _CiscoTsTrunkProtocolFilterTranspMode_Type()
)
ciscoTsTrunkProtocolFilterTranspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoTsTrunkProtocolFilterTranspMode.setStatus("mandatory")
_CiscoTsUplinkMIBs_ObjectIdentity = ObjectIdentity
ciscoTsUplinkMIBs = _CiscoTsUplinkMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 9)
)

# Managed Objects groups


# Notification objects

ciscoTsStackCfgChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 0, 1)
)
ciscoTsStackCfgChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsNumSwitches"))
)
if mibBuilder.loadTexts:
    ciscoTsStackCfgChange.setStatus(
        ""
    )

ciscoTsStackProStackMatrixChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 1, 1, 0, 2)
)
ciscoTsStackProStackMatrixChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsProStackMatrixStatus"))
)
if mibBuilder.loadTexts:
    ciscoTsStackProStackMatrixChange.setStatus(
        ""
    )

ciscoTsStackTempChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 0, 3)
)
ciscoTsStackTempChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsStackSwitchTemperature"))
)
if mibBuilder.loadTexts:
    ciscoTsStackTempChange.setStatus(
        ""
    )

ciscoTsStackPwrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 2, 0, 4)
)
ciscoTsStackPwrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsStackSwitchPwrSupplyStatus"))
)
if mibBuilder.loadTexts:
    ciscoTsStackPwrStatusChange.setStatus(
        ""
    )

ciscoTsPortStrNFwdEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 0, 1)
)
ciscoTsPortStrNFwdEntry.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsPortCfgActualForwardingMode"))
)
if mibBuilder.loadTexts:
    ciscoTsPortStrNFwdEntry.setStatus(
        ""
    )

ciscoTsPortCfgLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 0, 2)
)
ciscoTsPortCfgLossTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsPortStatsCfgLoss"))
)
if mibBuilder.loadTexts:
    ciscoTsPortCfgLossTrap.setStatus(
        ""
    )

ciscoTsBeaconStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 0, 3)
)
ciscoTsBeaconStart.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsPortCfgNumber"))
)
if mibBuilder.loadTexts:
    ciscoTsBeaconStart.setStatus(
        ""
    )

ciscoTsBeaconEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 0, 4)
)
ciscoTsBeaconEnd.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsPortCfgNumber"))
)
if mibBuilder.loadTexts:
    ciscoTsBeaconEnd.setStatus(
        ""
    )

ciscoTsDuplicateMACAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 0, 5)
)
ciscoTsDuplicateMACAddr.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsPortCfgNumber"))
)
if mibBuilder.loadTexts:
    ciscoTsDuplicateMACAddr.setStatus(
        ""
    )

ciscoTsPortSoftErrExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 4, 0, 6)
)
ciscoTsPortSoftErrExceededTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsStackSwitchNumber"),
        ("CISCO-TS-STACK-MIB", "ciscoTsPortCfgNumber"),
        ("TOKEN-RING-RMON-MIB", "ringStationIfIndex"),
        ("TOKEN-RING-RMON-MIB", "ringStationMacAddress"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    ciscoTsPortSoftErrExceededTrap.setStatus(
        ""
    )

ciscoTsTrCRFNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 0, 1)
)
ciscoTsTrCRFNewRoot.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsTrCRFInfoTrCRFNumber"))
)
if mibBuilder.loadTexts:
    ciscoTsTrCRFNewRoot.setStatus(
        ""
    )

ciscoTsTrCRFTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 0, 2)
)
ciscoTsTrCRFTopologyChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsTrCRFInfoTrCRFNumber"))
)
if mibBuilder.loadTexts:
    ciscoTsTrCRFTopologyChange.setStatus(
        ""
    )

ciscoTsTrBRFNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 0, 3)
)
ciscoTsTrBRFNewRoot.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsTrBRFInfoTrBRFNumber"))
)
if mibBuilder.loadTexts:
    ciscoTsTrBRFNewRoot.setStatus(
        ""
    )

ciscoTsTrBRFTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 6, 0, 4)
)
ciscoTsTrBRFTopologyChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsTrBRFInfoTrBRFNumber"))
)
if mibBuilder.loadTexts:
    ciscoTsTrBRFTopologyChange.setStatus(
        ""
    )

ciscoTsTokenChannelFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 7, 0, 1)
)
ciscoTsTokenChannelFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsTCPorts"))
)
if mibBuilder.loadTexts:
    ciscoTsTokenChannelFailed.setStatus(
        ""
    )

ciscoTsTokenChannelStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 32, 7, 0, 2)
)
ciscoTsTokenChannelStatus.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CISCO-TS-STACK-MIB", "ciscoTsTCStatus"),
        ("CISCO-TS-STACK-MIB", "ciscoTsTCPorts"),
        ("CISCO-TS-STACK-MIB", "ciscoTsTCActivePorts"))
)
if mibBuilder.loadTexts:
    ciscoTsTokenChannelStatus.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TS-STACK-MIB",
    **{"MacAddr": MacAddr,
       "tsStack": tsStack,
       "ciscoTsMain": ciscoTsMain,
       "ciscoTsConfig": ciscoTsConfig,
       "ciscoTsStackCfgChange": ciscoTsStackCfgChange,
       "ciscoTsStackProStackMatrixChange": ciscoTsStackProStackMatrixChange,
       "ciscoTsIpAddr": ciscoTsIpAddr,
       "ciscoTsNetMask": ciscoTsNetMask,
       "ciscoTsDefaultGateway": ciscoTsDefaultGateway,
       "ciscoTsSysCurTime": ciscoTsSysCurTime,
       "ciscoTsConfiguration": ciscoTsConfiguration,
       "ciscoTsNumSwitches": ciscoTsNumSwitches,
       "ciscoTsStackStatus": ciscoTsStackStatus,
       "ciscoTsTftpServer": ciscoTsTftpServer,
       "ciscoTsTftpServerTrBRF": ciscoTsTftpServerTrBRF,
       "ciscoTsTftpFileLoc": ciscoTsTftpFileLoc,
       "ciscoTsTftpDownload": ciscoTsTftpDownload,
       "ciscoTsTftpDownloadStatus": ciscoTsTftpDownloadStatus,
       "ciscoTsProStackMatrixStatus": ciscoTsProStackMatrixStatus,
       "ciscoTsNumMatrixModules": ciscoTsNumMatrixModules,
       "ciscoTsStackReset": ciscoTsStackReset,
       "ciscoTsStackRMONStatistics": ciscoTsStackRMONStatistics,
       "ciscoTsTrapRcvrTable": ciscoTsTrapRcvrTable,
       "ciscoTsTrapRcvrEntry": ciscoTsTrapRcvrEntry,
       "ciscoTsTrapRcvrIndex": ciscoTsTrapRcvrIndex,
       "ciscoTsTrapRcvrStatus": ciscoTsTrapRcvrStatus,
       "ciscoTsTrapRcvrIpAddress": ciscoTsTrapRcvrIpAddress,
       "ciscoTsTrapRcvrComm": ciscoTsTrapRcvrComm,
       "ciscoTsTrapRcvrTrBRFs": ciscoTsTrapRcvrTrBRFs,
       "ciscoTsStack": ciscoTsStack,
       "ciscoTsStackTempChange": ciscoTsStackTempChange,
       "ciscoTsStackPwrStatusChange": ciscoTsStackPwrStatusChange,
       "ciscoTsStackTable": ciscoTsStackTable,
       "ciscoTsStackEntry": ciscoTsStackEntry,
       "ciscoTsStackSwitchNumber": ciscoTsStackSwitchNumber,
       "ciscoTsStackSwitchBIAddr": ciscoTsStackSwitchBIAddr,
       "ciscoTsStackSwitchLAAddr": ciscoTsStackSwitchLAAddr,
       "ciscoTsStackSwitchFwVersion": ciscoTsStackSwitchFwVersion,
       "ciscoTsStackSwitchHwVersion": ciscoTsStackSwitchHwVersion,
       "ciscoTsStackSwitchUptime": ciscoTsStackSwitchUptime,
       "ciscoTsStackSwitchStatus": ciscoTsStackSwitchStatus,
       "ciscoTsStackSwitchTemperature": ciscoTsStackSwitchTemperature,
       "ciscoTsStackSwitchMemory": ciscoTsStackSwitchMemory,
       "ciscoTsStackSwitchSPANPort": ciscoTsStackSwitchSPANPort,
       "ciscoTsStackSwitchSPANMonitoredPort": ciscoTsStackSwitchSPANMonitoredPort,
       "ciscoTsStackSwitchFeatureStatus": ciscoTsStackSwitchFeatureStatus,
       "ciscoTsStackSwitchFeatureKey": ciscoTsStackSwitchFeatureKey,
       "ciscoTsStackSwitchPorts": ciscoTsStackSwitchPorts,
       "ciscoTsStackSwitchAgingTime": ciscoTsStackSwitchAgingTime,
       "ciscoTsStackSwitchAgingLevel": ciscoTsStackSwitchAgingLevel,
       "ciscoTsStackSwitchXmitFrames": ciscoTsStackSwitchXmitFrames,
       "ciscoTsStackSwitchRcvdFrames": ciscoTsStackSwitchRcvdFrames,
       "ciscoTsStackSwitchRcvdErrFrames": ciscoTsStackSwitchRcvdErrFrames,
       "ciscoTsStackSwitchLostFrames": ciscoTsStackSwitchLostFrames,
       "ciscoTsStackSwitchPendingSendRqsts": ciscoTsStackSwitchPendingSendRqsts,
       "ciscoTsStackSwitchXmitErrFrames": ciscoTsStackSwitchXmitErrFrames,
       "ciscoTsStackSwitchCurrActStations": ciscoTsStackSwitchCurrActStations,
       "ciscoTsStackSwitchLargestNumStations": ciscoTsStackSwitchLargestNumStations,
       "ciscoTsStackSwitchMaxAddressChain": ciscoTsStackSwitchMaxAddressChain,
       "ciscoTsStackSwitchAddressTblFulls": ciscoTsStackSwitchAddressTblFulls,
       "ciscoTsStackSwitchId": ciscoTsStackSwitchId,
       "ciscoTsStackSwitchSPANMonitoredTrCRFs": ciscoTsStackSwitchSPANMonitoredTrCRFs,
       "ciscoTsStackSwitchPwrSupplyStatus": ciscoTsStackSwitchPwrSupplyStatus,
       "ciscoTsModule": ciscoTsModule,
       "ciscoTsModTable": ciscoTsModTable,
       "ciscoTsModEntry": ciscoTsModEntry,
       "ciscoTsModSwitchNumber": ciscoTsModSwitchNumber,
       "ciscoTsModNumber": ciscoTsModNumber,
       "ciscoTsModState": ciscoTsModState,
       "ciscoTsModType": ciscoTsModType,
       "ciscoTsModRevision": ciscoTsModRevision,
       "ciscoTsModFwVer": ciscoTsModFwVer,
       "ciscoTsModNumPorts": ciscoTsModNumPorts,
       "ciscoTsModUptime": ciscoTsModUptime,
       "ciscoTsPort": ciscoTsPort,
       "ciscoTsPortStrNFwdEntry": ciscoTsPortStrNFwdEntry,
       "ciscoTsPortCfgLossTrap": ciscoTsPortCfgLossTrap,
       "ciscoTsBeaconStart": ciscoTsBeaconStart,
       "ciscoTsBeaconEnd": ciscoTsBeaconEnd,
       "ciscoTsDuplicateMACAddr": ciscoTsDuplicateMACAddr,
       "ciscoTsPortSoftErrExceededTrap": ciscoTsPortSoftErrExceededTrap,
       "ciscoTsPortCfgTable": ciscoTsPortCfgTable,
       "ciscoTsPortCfgEntry": ciscoTsPortCfgEntry,
       "ciscoTsPortCfgNumber": ciscoTsPortCfgNumber,
       "ciscoTsPortCfgModNumber": ciscoTsPortCfgModNumber,
       "ciscoTsPortCfgIfIndex": ciscoTsPortCfgIfIndex,
       "ciscoTsPortCfgResetStats": ciscoTsPortCfgResetStats,
       "ciscoTsPortCfgResetAddrs": ciscoTsPortCfgResetAddrs,
       "ciscoTsPortCfgAddrAgingTime": ciscoTsPortCfgAddrAgingTime,
       "ciscoTsPortCfgDemandAgingLevel": ciscoTsPortCfgDemandAgingLevel,
       "ciscoTsPortCfgErrLoThreshold": ciscoTsPortCfgErrLoThreshold,
       "ciscoTsPortCfgErrHiThreshold": ciscoTsPortCfgErrHiThreshold,
       "ciscoTsPortCfgErrSampling": ciscoTsPortCfgErrSampling,
       "ciscoTsPortCfgMaxTransmitUnit": ciscoTsPortCfgMaxTransmitUnit,
       "ciscoTsPortCfgMaxExplorerRate": ciscoTsPortCfgMaxExplorerRate,
       "ciscoTsPortCfgSetACbits": ciscoTsPortCfgSetACbits,
       "ciscoTsPortCfgEarlyTokenRlse": ciscoTsPortCfgEarlyTokenRlse,
       "ciscoTsPortCfgForwardingMode": ciscoTsPortCfgForwardingMode,
       "ciscoTsPortCfgActualForwardingMode": ciscoTsPortCfgActualForwardingMode,
       "ciscoTsPortCfgPortMode": ciscoTsPortCfgPortMode,
       "ciscoTsPortCfgActualPortMode": ciscoTsPortCfgActualPortMode,
       "ciscoTsPortCfgPriorityThres": ciscoTsPortCfgPriorityThres,
       "ciscoTsPortCfgMinXmitPriority": ciscoTsPortCfgMinXmitPriority,
       "ciscoTsPortCfgCfgLossThres": ciscoTsPortCfgCfgLossThres,
       "ciscoTsPortCfgCfgLossInterval": ciscoTsPortCfgCfgLossInterval,
       "ciscoTsPortCfgBcastSuppresion": ciscoTsPortCfgBcastSuppresion,
       "ciscoTsPortCfgCDPTimeToLive": ciscoTsPortCfgCDPTimeToLive,
       "ciscoTsPortCfgSpanningTreeMode": ciscoTsPortCfgSpanningTreeMode,
       "ciscoTsPortCfgSecurityMode": ciscoTsPortCfgSecurityMode,
       "ciscoTsPortCfgSoftErrThreshold": ciscoTsPortCfgSoftErrThreshold,
       "ciscoTsPortCfgSoftErrReportInterval": ciscoTsPortCfgSoftErrReportInterval,
       "ciscoTsPortCfgSoftErrorMonitoring": ciscoTsPortCfgSoftErrorMonitoring,
       "ciscoTsPortStatsTable": ciscoTsPortStatsTable,
       "ciscoTsPortStatsEntry": ciscoTsPortStatsEntry,
       "ciscoTsPortStatsNumber": ciscoTsPortStatsNumber,
       "ciscoTsPortStatsModNumber": ciscoTsPortStatsModNumber,
       "ciscoTsPortStatsIfIndex": ciscoTsPortStatsIfIndex,
       "ciscoTsPortStatsRcvLocalFrames": ciscoTsPortStatsRcvLocalFrames,
       "ciscoTsPortStatsForwardedFrames": ciscoTsPortStatsForwardedFrames,
       "ciscoTsPortStatsStations": ciscoTsPortStatsStations,
       "ciscoTsPortStatsSWHandledFrames": ciscoTsPortStatsSWHandledFrames,
       "ciscoTsPortStatsLocalStations": ciscoTsPortStatsLocalStations,
       "ciscoTsPortStatsRemoteStations": ciscoTsPortStatsRemoteStations,
       "ciscoTsPortStatsUnknownStaFrames": ciscoTsPortStatsUnknownStaFrames,
       "ciscoTsPortStatsResetTimer": ciscoTsPortStatsResetTimer,
       "ciscoTsPortStatsInFrames": ciscoTsPortStatsInFrames,
       "ciscoTsPortStatsOutFrames": ciscoTsPortStatsOutFrames,
       "ciscoTsPortStatsLongFrames": ciscoTsPortStatsLongFrames,
       "ciscoTsPortStatsShortFrames": ciscoTsPortStatsShortFrames,
       "ciscoTsPortStatsInBufOverflows": ciscoTsPortStatsInBufOverflows,
       "ciscoTsPortStatsOutBufOverflows": ciscoTsPortStatsOutBufOverflows,
       "ciscoTsPortStatsRcvBcasts": ciscoTsPortStatsRcvBcasts,
       "ciscoTsPortStatsRcvMcasts": ciscoTsPortStatsRcvMcasts,
       "ciscoTsPortStatsSwitchedFrames": ciscoTsPortStatsSwitchedFrames,
       "ciscoTsPortStatsPktsInErrors": ciscoTsPortStatsPktsInErrors,
       "ciscoTsPortStatsAddrChainOverflows": ciscoTsPortStatsAddrChainOverflows,
       "ciscoTsPortStatsTableOverflows": ciscoTsPortStatsTableOverflows,
       "ciscoTsPortStatsCfgLoss": ciscoTsPortStatsCfgLoss,
       "ciscoTsPortStatsCfgLossRC": ciscoTsPortStatsCfgLossRC,
       "ciscoTsPortStatsTrCRF": ciscoTsPortStatsTrCRF,
       "ciscoTsPortStatsAutoDisableRC": ciscoTsPortStatsAutoDisableRC,
       "ciscoTsProbe": ciscoTsProbe,
       "ciscoTsPassiveProbeTable": ciscoTsPassiveProbeTable,
       "ciscoTsPassiveProbeEntry": ciscoTsPassiveProbeEntry,
       "ciscoTsPassiveProbeIndex": ciscoTsPassiveProbeIndex,
       "ciscoTsPassiveProbePort": ciscoTsPassiveProbePort,
       "ciscoTsPassiveProbeMonitoredPort": ciscoTsPassiveProbeMonitoredPort,
       "ciscoTsPassiveProbeDirection": ciscoTsPassiveProbeDirection,
       "ciscoTsVLANS": ciscoTsVLANS,
       "ciscoTsTrCRFNewRoot": ciscoTsTrCRFNewRoot,
       "ciscoTsTrCRFTopologyChange": ciscoTsTrCRFTopologyChange,
       "ciscoTsTrBRFNewRoot": ciscoTsTrBRFNewRoot,
       "ciscoTsTrBRFTopologyChange": ciscoTsTrBRFTopologyChange,
       "ciscoTsTrCRFInfoTable": ciscoTsTrCRFInfoTable,
       "ciscoTsTrCRFInfoEntry": ciscoTsTrCRFInfoEntry,
       "ciscoTsTrCRFInfoTrCRFNumber": ciscoTsTrCRFInfoTrCRFNumber,
       "ciscoTsTrCRFInfoName": ciscoTsTrCRFInfoName,
       "ciscoTsTrCRFInfoSpanningTreeProtoSpecification": ciscoTsTrCRFInfoSpanningTreeProtoSpecification,
       "ciscoTsTrCRFInfoSpanningTreeBridgeForwardDelay": ciscoTsTrCRFInfoSpanningTreeBridgeForwardDelay,
       "ciscoTsTrCRFInfoSpanningTreeBridgeHelloTime": ciscoTsTrCRFInfoSpanningTreeBridgeHelloTime,
       "ciscoTsTrCRFInfoSpanningTreeBridgeMaxAge": ciscoTsTrCRFInfoSpanningTreeBridgeMaxAge,
       "ciscoTsTrCRFInfoSpanningTreeInternalPortMode": ciscoTsTrCRFInfoSpanningTreeInternalPortMode,
       "ciscoTsTrBRFInfoTable": ciscoTsTrBRFInfoTable,
       "ciscoTsTrBRFInfoEntry": ciscoTsTrBRFInfoEntry,
       "ciscoTsTrBRFInfoTrBRFNumber": ciscoTsTrBRFInfoTrBRFNumber,
       "ciscoTsTrBRFInfoName": ciscoTsTrBRFInfoName,
       "ciscoTsTrBRFInfoIpState": ciscoTsTrBRFInfoIpState,
       "ciscoTsTrBRFInfoIpAddress": ciscoTsTrBRFInfoIpAddress,
       "ciscoTsTrBRFInfoIpSubnetMask": ciscoTsTrBRFInfoIpSubnetMask,
       "ciscoTsTrBRFInfoIpDefaultGateway": ciscoTsTrBRFInfoIpDefaultGateway,
       "ciscoTsTrBRFInfoStpMode": ciscoTsTrBRFInfoStpMode,
       "ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr": ciscoTsTrBRFInfoIEEEStpUsesBridgeFuncAddr,
       "ciscoTsTransitedConfiguredTrCRFs": ciscoTsTransitedConfiguredTrCRFs,
       "ciscoTsTransitedTrCRFs": ciscoTsTransitedTrCRFs,
       "ciscoTsTransitedConfiguredTrBRFs": ciscoTsTransitedConfiguredTrBRFs,
       "ciscoTsTransitedTrBRFs": ciscoTsTransitedTrBRFs,
       "ciscoTsTChannel": ciscoTsTChannel,
       "ciscoTsTokenChannelFailed": ciscoTsTokenChannelFailed,
       "ciscoTsTokenChannelStatus": ciscoTsTokenChannelStatus,
       "ciscoTsTCTable": ciscoTsTCTable,
       "ciscoTsTCEntry": ciscoTsTCEntry,
       "ciscoTsTCSwitchNumber": ciscoTsTCSwitchNumber,
       "ciscoTsTCNumber": ciscoTsTCNumber,
       "ciscoTsTCPorts": ciscoTsTCPorts,
       "ciscoTsTCStatus": ciscoTsTCStatus,
       "ciscoTsTCActivePorts": ciscoTsTCActivePorts,
       "ciscoTsFilter": ciscoTsFilter,
       "ciscoTsProtocolClassFilterTable": ciscoTsProtocolClassFilterTable,
       "ciscoTsProtocolClassFilterEntry": ciscoTsProtocolClassFilterEntry,
       "ciscoTsProtocolClassFilterIndex": ciscoTsProtocolClassFilterIndex,
       "ciscoTsProtocolClassFilterEtype": ciscoTsProtocolClassFilterEtype,
       "ciscoTsProtocolClassFilterDSAPs": ciscoTsProtocolClassFilterDSAPs,
       "ciscoTsProtocolFilterTable": ciscoTsProtocolFilterTable,
       "ciscoTsProtocolFilterEntry": ciscoTsProtocolFilterEntry,
       "ciscoTsProtocolFilterPort": ciscoTsProtocolFilterPort,
       "ciscoTsProtocolFilterBlockingMode": ciscoTsProtocolFilterBlockingMode,
       "ciscoTsProtocolFilterTranspMode": ciscoTsProtocolFilterTranspMode,
       "ciscoTsMACDestFilterTable": ciscoTsMACDestFilterTable,
       "ciscoTsMACDestFilterEntry": ciscoTsMACDestFilterEntry,
       "ciscoTsMACDestFilterSwitchNumber": ciscoTsMACDestFilterSwitchNumber,
       "ciscoTsMACDestFilterStationAddress": ciscoTsMACDestFilterStationAddress,
       "ciscoTsMACDestFilterType": ciscoTsMACDestFilterType,
       "ciscoTsMACDestFilterPorts": ciscoTsMACDestFilterPorts,
       "ciscoTsMACDestFilterExitMask": ciscoTsMACDestFilterExitMask,
       "ciscoTsMACDestFilterRemoteBox": ciscoTsMACDestFilterRemoteBox,
       "ciscoTsMACDestFilterRemotePort": ciscoTsMACDestFilterRemotePort,
       "ciscoTsMACDestFilterStatus": ciscoTsMACDestFilterStatus,
       "ciscoTsMACSourceFilterTable": ciscoTsMACSourceFilterTable,
       "ciscoTsMACSourceFilterEntry": ciscoTsMACSourceFilterEntry,
       "ciscoTsMACSourceFilterSwitchNumber": ciscoTsMACSourceFilterSwitchNumber,
       "ciscoTsMACSourceFilterStationAddress": ciscoTsMACSourceFilterStationAddress,
       "ciscoTsMACSourceFilterType": ciscoTsMACSourceFilterType,
       "ciscoTsMACSourceFilterPorts": ciscoTsMACSourceFilterPorts,
       "ciscoTsMACSourceFilterStatus": ciscoTsMACSourceFilterStatus,
       "ciscoTsDupAddrFilterTable": ciscoTsDupAddrFilterTable,
       "ciscoTsDupAddrFilterEntry": ciscoTsDupAddrFilterEntry,
       "ciscoTsDupAddrFilterSwitchNumber": ciscoTsDupAddrFilterSwitchNumber,
       "ciscoTsDupAddrFilterStationAddress": ciscoTsDupAddrFilterStationAddress,
       "ciscoTsDupAddrFilterPorts": ciscoTsDupAddrFilterPorts,
       "ciscoTsTrunkProtocolFilterTable": ciscoTsTrunkProtocolFilterTable,
       "ciscoTsTrunkProtocolFilterEntry": ciscoTsTrunkProtocolFilterEntry,
       "ciscoTsTrunkProtocolFilterPort": ciscoTsTrunkProtocolFilterPort,
       "ciscoTsTrunkProtocolFilterBlockingMode": ciscoTsTrunkProtocolFilterBlockingMode,
       "ciscoTsTrunkProtocolFilterTranspMode": ciscoTsTrunkProtocolFilterTranspMode,
       "ciscoTsUplinkMIBs": ciscoTsUplinkMIBs}
)
