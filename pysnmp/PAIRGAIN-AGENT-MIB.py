# SNMP MIB module (PAIRGAIN-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:14 2024
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

(pgainAgent,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainAgent")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgAgentSw_ObjectIdentity = ObjectIdentity
pgAgentSw = _PgAgentSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 1)
)


class _PgAgentType_Type(Integer32):
    """Custom type pgAgentType based on Integer32"""
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
        *(("other", 1),
          ("pgCMU", 2),
          ("pgDMU", 5),
          ("pgEMU", 4),
          ("pgHMU", 3),
          ("pgMBMTiger", 6))
    )


_PgAgentType_Type.__name__ = "Integer32"
_PgAgentType_Object = MibScalar
pgAgentType = _PgAgentType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 1),
    _PgAgentType_Type()
)
pgAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAgentType.setStatus("mandatory")
_PgAgentFwVer_Type = Integer32
_PgAgentFwVer_Object = MibScalar
pgAgentFwVer = _PgAgentFwVer_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 2),
    _PgAgentFwVer_Type()
)
pgAgentFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAgentFwVer.setStatus("mandatory")
_PgAgentSwVer_Type = DisplayString
_PgAgentSwVer_Object = MibScalar
pgAgentSwVer = _PgAgentSwVer_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 3),
    _PgAgentSwVer_Type()
)
pgAgentSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAgentSwVer.setStatus("mandatory")


class _PgAgentBootProtocol_Type(Integer32):
    """Custom type pgAgentBootProtocol based on Integer32"""
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
        *(("bootp-tftp", 2),
          ("ftp-only", 4),
          ("other", 1),
          ("proprietary", 5),
          ("tftp-only", 3))
    )


_PgAgentBootProtocol_Type.__name__ = "Integer32"
_PgAgentBootProtocol_Object = MibScalar
pgAgentBootProtocol = _PgAgentBootProtocol_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 4),
    _PgAgentBootProtocol_Type()
)
pgAgentBootProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAgentBootProtocol.setStatus("mandatory")


class _PgAgentBootFile_Type(DisplayString):
    """Custom type pgAgentBootFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PgAgentBootFile_Type.__name__ = "DisplayString"
_PgAgentBootFile_Object = MibScalar
pgAgentBootFile = _PgAgentBootFile_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 5),
    _PgAgentBootFile_Type()
)
pgAgentBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentBootFile.setStatus("mandatory")


class _PgAgentAuthTraps_Type(Integer32):
    """Custom type pgAgentAuthTraps based on Integer32"""
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


_PgAgentAuthTraps_Type.__name__ = "Integer32"
_PgAgentAuthTraps_Object = MibScalar
pgAgentAuthTraps = _PgAgentAuthTraps_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 6),
    _PgAgentAuthTraps_Type()
)
pgAgentAuthTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentAuthTraps.setStatus("mandatory")


class _PgAgentTraps_Type(Integer32):
    """Custom type pgAgentTraps based on Integer32"""
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


_PgAgentTraps_Type.__name__ = "Integer32"
_PgAgentTraps_Object = MibScalar
pgAgentTraps = _PgAgentTraps_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 7),
    _PgAgentTraps_Type()
)
pgAgentTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentTraps.setStatus("mandatory")
_PgAgentMibLevel_Type = Integer32
_PgAgentMibLevel_Object = MibScalar
pgAgentMibLevel = _PgAgentMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 8),
    _PgAgentMibLevel_Type()
)
pgAgentMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAgentMibLevel.setStatus("mandatory")
_PgAgentMySlotId_Type = Integer32
_PgAgentMySlotId_Object = MibScalar
pgAgentMySlotId = _PgAgentMySlotId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 9),
    _PgAgentMySlotId_Type()
)
pgAgentMySlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAgentMySlotId.setStatus("mandatory")
_PgAgentNetProtocol_ObjectIdentity = ObjectIdentity
pgAgentNetProtocol = _PgAgentNetProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 2)
)
_PgAgentIpAddr_Type = IpAddress
_PgAgentIpAddr_Object = MibScalar
pgAgentIpAddr = _PgAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 2, 1),
    _PgAgentIpAddr_Type()
)
pgAgentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentIpAddr.setStatus("mandatory")
_PgAgentNetMask_Type = IpAddress
_PgAgentNetMask_Object = MibScalar
pgAgentNetMask = _PgAgentNetMask_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 2, 2),
    _PgAgentNetMask_Type()
)
pgAgentNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentNetMask.setStatus("mandatory")
_PgAgentDefaultGateway_Type = IpAddress
_PgAgentDefaultGateway_Object = MibScalar
pgAgentDefaultGateway = _PgAgentDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 2, 3),
    _PgAgentDefaultGateway_Type()
)
pgAgentDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentDefaultGateway.setStatus("mandatory")
_PgAgentBootServerAddr_Type = IpAddress
_PgAgentBootServerAddr_Object = MibScalar
pgAgentBootServerAddr = _PgAgentBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 2, 4),
    _PgAgentBootServerAddr_Type()
)
pgAgentBootServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentBootServerAddr.setStatus("mandatory")
_PgSnmpAgent_ObjectIdentity = ObjectIdentity
pgSnmpAgent = _PgSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 3)
)
_PgAgentTrapReceiverTable_Object = MibTable
pgAgentTrapReceiverTable = _PgAgentTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pgAgentTrapReceiverTable.setStatus("optional")
_PgAgentTrapReceiverEntry_Object = MibTableRow
pgAgentTrapReceiverEntry = _PgAgentTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 3, 1, 1)
)
pgAgentTrapReceiverEntry.setIndexNames(
    (0, "PAIRGAIN-AGENT-MIB", "pgAgentTrapRcvrNetAddress"),
)
if mibBuilder.loadTexts:
    pgAgentTrapReceiverEntry.setStatus("optional")


class _PgAgentTrapRcvrStatus_Type(Integer32):
    """Custom type pgAgentTrapRcvrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("other", 1),
          ("valid", 2))
    )


_PgAgentTrapRcvrStatus_Type.__name__ = "Integer32"
_PgAgentTrapRcvrStatus_Object = MibTableColumn
pgAgentTrapRcvrStatus = _PgAgentTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 3, 1, 1, 1),
    _PgAgentTrapRcvrStatus_Type()
)
pgAgentTrapRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentTrapRcvrStatus.setStatus("optional")
_PgAgentTrapRcvrNetAddress_Type = IpAddress
_PgAgentTrapRcvrNetAddress_Object = MibTableColumn
pgAgentTrapRcvrNetAddress = _PgAgentTrapRcvrNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 3, 1, 1, 2),
    _PgAgentTrapRcvrNetAddress_Type()
)
pgAgentTrapRcvrNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentTrapRcvrNetAddress.setStatus("optional")


class _PgAgentTrapRcvrComm_Type(DisplayString):
    """Custom type pgAgentTrapRcvrComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PgAgentTrapRcvrComm_Type.__name__ = "DisplayString"
_PgAgentTrapRcvrComm_Object = MibTableColumn
pgAgentTrapRcvrComm = _PgAgentTrapRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 3, 1, 1, 3),
    _PgAgentTrapRcvrComm_Type()
)
pgAgentTrapRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentTrapRcvrComm.setStatus("optional")
_PgAgentHw_ObjectIdentity = ObjectIdentity
pgAgentHw = _PgAgentHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 4)
)


class _PgAgentReset_Type(Integer32):
    """Custom type pgAgentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_PgAgentReset_Type.__name__ = "Integer32"
_PgAgentReset_Object = MibScalar
pgAgentReset = _PgAgentReset_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 4, 1),
    _PgAgentReset_Type()
)
pgAgentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentReset.setStatus("mandatory")


class _PgAgentRestart_Type(Integer32):
    """Custom type pgAgentRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRestart", 1),
          ("restart", 2))
    )


_PgAgentRestart_Type.__name__ = "Integer32"
_PgAgentRestart_Object = MibScalar
pgAgentRestart = _PgAgentRestart_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 4, 2),
    _PgAgentRestart_Type()
)
pgAgentRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentRestart.setStatus("optional")


class _PgAgentBootMode_Type(Integer32):
    """Custom type pgAgentBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("nvram", 1))
    )


_PgAgentBootMode_Type.__name__ = "Integer32"
_PgAgentBootMode_Object = MibScalar
pgAgentBootMode = _PgAgentBootMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 4, 3),
    _PgAgentBootMode_Type()
)
pgAgentBootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentBootMode.setStatus("mandatory")


class _PgAgentWriteNvram_Type(Integer32):
    """Custom type pgAgentWriteNvram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWriteNvram", 1),
          ("writeNvram", 2))
    )


_PgAgentWriteNvram_Type.__name__ = "Integer32"
_PgAgentWriteNvram_Object = MibScalar
pgAgentWriteNvram = _PgAgentWriteNvram_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 4, 4),
    _PgAgentWriteNvram_Type()
)
pgAgentWriteNvram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAgentWriteNvram.setStatus("mandatory")
_PgAgentLocImage_ObjectIdentity = ObjectIdentity
pgAgentLocImage = _PgAgentLocImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 5)
)


class _PgLocImageValid_Type(Integer32):
    """Custom type pgLocImageValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localImageInvalid", 3),
          ("localImageValid", 2),
          ("other", 1))
    )


_PgLocImageValid_Type.__name__ = "Integer32"
_PgLocImageValid_Object = MibScalar
pgLocImageValid = _PgLocImageValid_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 5, 1),
    _PgLocImageValid_Type()
)
pgLocImageValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocImageValid.setStatus("optional")


class _PgLocImageVersion_Type(DisplayString):
    """Custom type pgLocImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PgLocImageVersion_Type.__name__ = "DisplayString"
_PgLocImageVersion_Object = MibScalar
pgLocImageVersion = _PgLocImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 5, 2),
    _PgLocImageVersion_Type()
)
pgLocImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocImageVersion.setStatus("optional")


class _PgLocImageLoadMode_Type(Integer32):
    """Custom type pgLocImageLoadMode based on Integer32"""
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
        *(("localAsBackup", 4),
          ("localBoot", 3),
          ("network", 2),
          ("other", 1))
    )


_PgLocImageLoadMode_Type.__name__ = "Integer32"
_PgLocImageLoadMode_Object = MibScalar
pgLocImageLoadMode = _PgLocImageLoadMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 5, 3),
    _PgLocImageLoadMode_Type()
)
pgLocImageLoadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocImageLoadMode.setStatus("optional")


class _PgLocImageActualSource_Type(Integer32):
    """Custom type pgLocImageActualSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localImage", 3),
          ("other", 1),
          ("remoteImage", 2))
    )


_PgLocImageActualSource_Type.__name__ = "Integer32"
_PgLocImageActualSource_Object = MibScalar
pgLocImageActualSource = _PgLocImageActualSource_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 2, 5, 4),
    _PgLocImageActualSource_Type()
)
pgLocImageActualSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocImageActualSource.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-AGENT-MIB",
    **{"DisplayString": DisplayString,
       "pgAgentSw": pgAgentSw,
       "pgAgentType": pgAgentType,
       "pgAgentFwVer": pgAgentFwVer,
       "pgAgentSwVer": pgAgentSwVer,
       "pgAgentBootProtocol": pgAgentBootProtocol,
       "pgAgentBootFile": pgAgentBootFile,
       "pgAgentAuthTraps": pgAgentAuthTraps,
       "pgAgentTraps": pgAgentTraps,
       "pgAgentMibLevel": pgAgentMibLevel,
       "pgAgentMySlotId": pgAgentMySlotId,
       "pgAgentNetProtocol": pgAgentNetProtocol,
       "pgAgentIpAddr": pgAgentIpAddr,
       "pgAgentNetMask": pgAgentNetMask,
       "pgAgentDefaultGateway": pgAgentDefaultGateway,
       "pgAgentBootServerAddr": pgAgentBootServerAddr,
       "pgSnmpAgent": pgSnmpAgent,
       "pgAgentTrapReceiverTable": pgAgentTrapReceiverTable,
       "pgAgentTrapReceiverEntry": pgAgentTrapReceiverEntry,
       "pgAgentTrapRcvrStatus": pgAgentTrapRcvrStatus,
       "pgAgentTrapRcvrNetAddress": pgAgentTrapRcvrNetAddress,
       "pgAgentTrapRcvrComm": pgAgentTrapRcvrComm,
       "pgAgentHw": pgAgentHw,
       "pgAgentReset": pgAgentReset,
       "pgAgentRestart": pgAgentRestart,
       "pgAgentBootMode": pgAgentBootMode,
       "pgAgentWriteNvram": pgAgentWriteNvram,
       "pgAgentLocImage": pgAgentLocImage,
       "pgLocImageValid": pgLocImageValid,
       "pgLocImageVersion": pgLocImageVersion,
       "pgLocImageLoadMode": pgLocImageLoadMode,
       "pgLocImageActualSource": pgLocImageActualSource}
)
