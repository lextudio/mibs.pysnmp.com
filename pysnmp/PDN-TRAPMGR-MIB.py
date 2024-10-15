# SNMP MIB module (PDN-TRAPMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-TRAPMGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:12 2024
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

(pdn_traps,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-traps")

(SwitchState,) = mibBuilder.importSymbols(
    "PDN-TC",
    "SwitchState")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DevTrapMgrMaxNumber_Type = Integer32
_DevTrapMgrMaxNumber_Object = MibScalar
devTrapMgrMaxNumber = _DevTrapMgrMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 1),
    _DevTrapMgrMaxNumber_Type()
)
devTrapMgrMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTrapMgrMaxNumber.setStatus("mandatory")
_DevTrapMgrCurrentNumber_Type = Integer32
_DevTrapMgrCurrentNumber_Object = MibScalar
devTrapMgrCurrentNumber = _DevTrapMgrCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 2),
    _DevTrapMgrCurrentNumber_Type()
)
devTrapMgrCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTrapMgrCurrentNumber.setStatus("mandatory")
_DevTrapMgrTable_Object = MibTable
devTrapMgrTable = _DevTrapMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 3)
)
if mibBuilder.loadTexts:
    devTrapMgrTable.setStatus("mandatory")
_DevTrapMgrEntry_Object = MibTableRow
devTrapMgrEntry = _DevTrapMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 3, 1)
)
devTrapMgrEntry.setIndexNames(
    (0, "PDN-TRAPMGR-MIB", "devTrapMgrIpAddress"),
)
if mibBuilder.loadTexts:
    devTrapMgrEntry.setStatus("mandatory")
_DevTrapMgrIpAddress_Type = IpAddress
_DevTrapMgrIpAddress_Object = MibTableColumn
devTrapMgrIpAddress = _DevTrapMgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 3, 1, 1),
    _DevTrapMgrIpAddress_Type()
)
devTrapMgrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTrapMgrIpAddress.setStatus("mandatory")
_DevTrapMgrDestination_Type = Integer32
_DevTrapMgrDestination_Object = MibTableColumn
devTrapMgrDestination = _DevTrapMgrDestination_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 3, 1, 2),
    _DevTrapMgrDestination_Type()
)
devTrapMgrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTrapMgrDestination.setStatus("mandatory")
_DevTrapMgrCircuit_Type = Integer32
_DevTrapMgrCircuit_Object = MibTableColumn
devTrapMgrCircuit = _DevTrapMgrCircuit_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 3, 1, 3),
    _DevTrapMgrCircuit_Type()
)
devTrapMgrCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTrapMgrCircuit.setStatus("mandatory")
_DevTrapMgrSubCircuit_Type = Integer32
_DevTrapMgrSubCircuit_Object = MibTableColumn
devTrapMgrSubCircuit = _DevTrapMgrSubCircuit_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 3, 1, 4),
    _DevTrapMgrSubCircuit_Type()
)
devTrapMgrSubCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTrapMgrSubCircuit.setStatus("mandatory")
_PdnDevTrapMgrTable_Object = MibTable
pdnDevTrapMgrTable = _PdnDevTrapMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 4)
)
if mibBuilder.loadTexts:
    pdnDevTrapMgrTable.setStatus("mandatory")
_PdnDevTrapMgrEntry_Object = MibTableRow
pdnDevTrapMgrEntry = _PdnDevTrapMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 4, 1)
)
pdnDevTrapMgrEntry.setIndexNames(
    (0, "PDN-TRAPMGR-MIB", "pdnDevTrapMgrDestAddress"),
    (0, "PDN-TRAPMGR-MIB", "pdnDevTrapMgrSubnetMask"),
)
if mibBuilder.loadTexts:
    pdnDevTrapMgrEntry.setStatus("mandatory")
_PdnDevTrapMgrDestAddress_Type = IpAddress
_PdnDevTrapMgrDestAddress_Object = MibTableColumn
pdnDevTrapMgrDestAddress = _PdnDevTrapMgrDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 4, 1, 1),
    _PdnDevTrapMgrDestAddress_Type()
)
pdnDevTrapMgrDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDevTrapMgrDestAddress.setStatus("mandatory")
_PdnDevTrapMgrSubnetMask_Type = IpAddress
_PdnDevTrapMgrSubnetMask_Object = MibTableColumn
pdnDevTrapMgrSubnetMask = _PdnDevTrapMgrSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 4, 1, 2),
    _PdnDevTrapMgrSubnetMask_Type()
)
pdnDevTrapMgrSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDevTrapMgrSubnetMask.setStatus("mandatory")


class _PdnDevTrapMgrDestPort_Type(Integer32):
    """Custom type pdnDevTrapMgrDestPort based on Integer32"""
    defaultValue = 162


_PdnDevTrapMgrDestPort_Object = MibTableColumn
pdnDevTrapMgrDestPort = _PdnDevTrapMgrDestPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 4, 1, 3),
    _PdnDevTrapMgrDestPort_Type()
)
pdnDevTrapMgrDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDevTrapMgrDestPort.setStatus("mandatory")


class _PdnDevTrapMgrCommunityName_Type(DisplayString):
    """Custom type pdnDevTrapMgrCommunityName based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PdnDevTrapMgrCommunityName_Type.__name__ = "DisplayString"
_PdnDevTrapMgrCommunityName_Object = MibTableColumn
pdnDevTrapMgrCommunityName = _PdnDevTrapMgrCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 4, 1, 4),
    _PdnDevTrapMgrCommunityName_Type()
)
pdnDevTrapMgrCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDevTrapMgrCommunityName.setStatus("mandatory")


class _PdnDevTrapMgrEnable_Type(Integer32):
    """Custom type pdnDevTrapMgrEnable based on Integer32"""
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


_PdnDevTrapMgrEnable_Type.__name__ = "Integer32"
_PdnDevTrapMgrEnable_Object = MibTableColumn
pdnDevTrapMgrEnable = _PdnDevTrapMgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 4, 1, 5),
    _PdnDevTrapMgrEnable_Type()
)
pdnDevTrapMgrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDevTrapMgrEnable.setStatus("mandatory")
_PdnDevTrapMgrRowStatus_Type = RowStatus
_PdnDevTrapMgrRowStatus_Object = MibTableColumn
pdnDevTrapMgrRowStatus = _PdnDevTrapMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 4, 1, 6),
    _PdnDevTrapMgrRowStatus_Type()
)
pdnDevTrapMgrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDevTrapMgrRowStatus.setStatus("mandatory")
_PdnDevConfigTrapsEnable_Type = SwitchState
_PdnDevConfigTrapsEnable_Object = MibScalar
pdnDevConfigTrapsEnable = _PdnDevConfigTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9, 5),
    _PdnDevConfigTrapsEnable_Type()
)
pdnDevConfigTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDevConfigTrapsEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-TRAPMGR-MIB",
    **{"devTrapMgrMaxNumber": devTrapMgrMaxNumber,
       "devTrapMgrCurrentNumber": devTrapMgrCurrentNumber,
       "devTrapMgrTable": devTrapMgrTable,
       "devTrapMgrEntry": devTrapMgrEntry,
       "devTrapMgrIpAddress": devTrapMgrIpAddress,
       "devTrapMgrDestination": devTrapMgrDestination,
       "devTrapMgrCircuit": devTrapMgrCircuit,
       "devTrapMgrSubCircuit": devTrapMgrSubCircuit,
       "pdnDevTrapMgrTable": pdnDevTrapMgrTable,
       "pdnDevTrapMgrEntry": pdnDevTrapMgrEntry,
       "pdnDevTrapMgrDestAddress": pdnDevTrapMgrDestAddress,
       "pdnDevTrapMgrSubnetMask": pdnDevTrapMgrSubnetMask,
       "pdnDevTrapMgrDestPort": pdnDevTrapMgrDestPort,
       "pdnDevTrapMgrCommunityName": pdnDevTrapMgrCommunityName,
       "pdnDevTrapMgrEnable": pdnDevTrapMgrEnable,
       "pdnDevTrapMgrRowStatus": pdnDevTrapMgrRowStatus,
       "pdnDevConfigTrapsEnable": pdnDevConfigTrapsEnable}
)
