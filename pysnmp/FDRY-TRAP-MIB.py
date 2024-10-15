# SNMP MIB module (FDRY-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FDRY-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:47 2024
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

(fdryTrap,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "fdryTrap")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

fdryTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1)
)
fdryTrapMIB.setRevisions(
        ("2010-06-02 00:00",
         "2008-02-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SecurityModel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("usm", 3),
          ("v1", 1),
          ("v2c", 2))
    )



class SecurityLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auth", 2),
          ("authPriv", 3),
          ("noAuth", 1))
    )



# MIB Managed Objects in the order of their OIDs

_FdryTrapReceiver_ObjectIdentity = ObjectIdentity
fdryTrapReceiver = _FdryTrapReceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1)
)
_FdryTrapReceiverTable_Object = MibTable
fdryTrapReceiverTable = _FdryTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fdryTrapReceiverTable.setStatus("current")
_FdryTrapReceiverEntry_Object = MibTableRow
fdryTrapReceiverEntry = _FdryTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1)
)
fdryTrapReceiverEntry.setIndexNames(
    (0, "FDRY-TRAP-MIB", "fdryTrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    fdryTrapReceiverEntry.setStatus("current")
_FdryTrapReceiverIndex_Type = Unsigned32
_FdryTrapReceiverIndex_Object = MibTableColumn
fdryTrapReceiverIndex = _FdryTrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 1),
    _FdryTrapReceiverIndex_Type()
)
fdryTrapReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryTrapReceiverIndex.setStatus("current")


class _FdryTrapReceiverAddrType_Type(InetAddressType):
    """Custom type fdryTrapReceiverAddrType based on InetAddressType"""


_FdryTrapReceiverAddrType_Object = MibTableColumn
fdryTrapReceiverAddrType = _FdryTrapReceiverAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 2),
    _FdryTrapReceiverAddrType_Type()
)
fdryTrapReceiverAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverAddrType.setStatus("current")
_FdryTrapReceiverAddr_Type = InetAddress
_FdryTrapReceiverAddr_Object = MibTableColumn
fdryTrapReceiverAddr = _FdryTrapReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 3),
    _FdryTrapReceiverAddr_Type()
)
fdryTrapReceiverAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverAddr.setStatus("current")


class _FdryTrapReceiverCommunityOrSecurityName_Type(OctetString):
    """Custom type fdryTrapReceiverCommunityOrSecurityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FdryTrapReceiverCommunityOrSecurityName_Type.__name__ = "OctetString"
_FdryTrapReceiverCommunityOrSecurityName_Object = MibTableColumn
fdryTrapReceiverCommunityOrSecurityName = _FdryTrapReceiverCommunityOrSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 4),
    _FdryTrapReceiverCommunityOrSecurityName_Type()
)
fdryTrapReceiverCommunityOrSecurityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverCommunityOrSecurityName.setStatus("current")


class _FdryTrapReceiverUDPPort_Type(Integer32):
    """Custom type fdryTrapReceiverUDPPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryTrapReceiverUDPPort_Type.__name__ = "Integer32"
_FdryTrapReceiverUDPPort_Object = MibTableColumn
fdryTrapReceiverUDPPort = _FdryTrapReceiverUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 5),
    _FdryTrapReceiverUDPPort_Type()
)
fdryTrapReceiverUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverUDPPort.setStatus("current")


class _FdryTrapReceiverSecurityModel_Type(SecurityModel):
    """Custom type fdryTrapReceiverSecurityModel based on SecurityModel"""


_FdryTrapReceiverSecurityModel_Object = MibTableColumn
fdryTrapReceiverSecurityModel = _FdryTrapReceiverSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 6),
    _FdryTrapReceiverSecurityModel_Type()
)
fdryTrapReceiverSecurityModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverSecurityModel.setStatus("current")


class _FdryTrapReceiverSecurityLevel_Type(SecurityLevel):
    """Custom type fdryTrapReceiverSecurityLevel based on SecurityLevel"""


_FdryTrapReceiverSecurityLevel_Object = MibTableColumn
fdryTrapReceiverSecurityLevel = _FdryTrapReceiverSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 7),
    _FdryTrapReceiverSecurityLevel_Type()
)
fdryTrapReceiverSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverSecurityLevel.setStatus("current")
_FdryTrapReceiverRowStatus_Type = RowStatus
_FdryTrapReceiverRowStatus_Object = MibTableColumn
fdryTrapReceiverRowStatus = _FdryTrapReceiverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 8),
    _FdryTrapReceiverRowStatus_Type()
)
fdryTrapReceiverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-TRAP-MIB",
    **{"SecurityModel": SecurityModel,
       "SecurityLevel": SecurityLevel,
       "fdryTrapMIB": fdryTrapMIB,
       "fdryTrapReceiver": fdryTrapReceiver,
       "fdryTrapReceiverTable": fdryTrapReceiverTable,
       "fdryTrapReceiverEntry": fdryTrapReceiverEntry,
       "fdryTrapReceiverIndex": fdryTrapReceiverIndex,
       "fdryTrapReceiverAddrType": fdryTrapReceiverAddrType,
       "fdryTrapReceiverAddr": fdryTrapReceiverAddr,
       "fdryTrapReceiverCommunityOrSecurityName": fdryTrapReceiverCommunityOrSecurityName,
       "fdryTrapReceiverUDPPort": fdryTrapReceiverUDPPort,
       "fdryTrapReceiverSecurityModel": fdryTrapReceiverSecurityModel,
       "fdryTrapReceiverSecurityLevel": fdryTrapReceiverSecurityLevel,
       "fdryTrapReceiverRowStatus": fdryTrapReceiverRowStatus}
)
