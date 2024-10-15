# SNMP MIB module (IBMIROCRLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBMIROCRLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:57 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class NBNames(OctetString):
    """Custom type NBNames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )





class IpxNetworkNumber(OctetString):
    """Custom type IpxNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class IpxNodeNumber(OctetString):
    """Custom type IpxNodeNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )





class CircuitState(Integer32):
    """Custom type CircuitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("ackRcvd", 4),
          ("ackSent", 5),
          ("closed", 1),
          ("dhcpWait", 8),
          ("listen", 2),
          ("open", 6),
          ("reqSent", 3),
          ("termSent", 7),
          ("unknown", 0))
    )





class ZeroOrigCounter32(Counter32):
    """Custom type ZeroOrigCounter32 based on Counter32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm2210_ObjectIdentity = ObjectIdentity
ibm2210 = _Ibm2210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 72)
)
_IbmIROC_ObjectIdentity = ObjectIdentity
ibmIROC = _IbmIROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119)
)
_IbmIROCrouting_ObjectIdentity = ObjectIdentity
ibmIROCrouting = _IbmIROCrouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4)
)
_IbmIROCroutingRlan_ObjectIdentity = ObjectIdentity
ibmIROCroutingRlan = _IbmIROCroutingRlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5)
)
_IbmRlanTraps_ObjectIdentity = ObjectIdentity
ibmRlanTraps = _IbmRlanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 0)
)
_IbmRlanMIB_ObjectIdentity = ObjectIdentity
ibmRlanMIB = _IbmRlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1)
)
_IbmRlanGeneral_ObjectIdentity = ObjectIdentity
ibmRlanGeneral = _IbmRlanGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 1)
)
_RlanActiveUserTable_Object = MibTable
rlanActiveUserTable = _RlanActiveUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2)
)
if mibBuilder.loadTexts:
    rlanActiveUserTable.setStatus("mandatory")
_RlanActiveUserEntry_Object = MibTableRow
rlanActiveUserEntry = _RlanActiveUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1)
)
rlanActiveUserEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlanActiveUserEntry.setStatus("mandatory")


class _RlanActiveUserName_Type(DisplayString):
    """Custom type rlanActiveUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_RlanActiveUserName_Type.__name__ = "DisplayString"
_RlanActiveUserName_Object = MibTableColumn
rlanActiveUserName = _RlanActiveUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 1),
    _RlanActiveUserName_Type()
)
rlanActiveUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveUserName.setStatus("mandatory")
_RlanActiveUserConnected_Type = TimeTicks
_RlanActiveUserConnected_Object = MibTableColumn
rlanActiveUserConnected = _RlanActiveUserConnected_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 2),
    _RlanActiveUserConnected_Type()
)
rlanActiveUserConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveUserConnected.setStatus("mandatory")


class _RlanActiveUserTimeRemaining_Type(Integer32):
    """Custom type rlanActiveUserTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlanActiveUserTimeRemaining_Type.__name__ = "Integer32"
_RlanActiveUserTimeRemaining_Object = MibTableColumn
rlanActiveUserTimeRemaining = _RlanActiveUserTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 3),
    _RlanActiveUserTimeRemaining_Type()
)
rlanActiveUserTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveUserTimeRemaining.setStatus("mandatory")
_RlanActiveUserInPkts_Type = ZeroOrigCounter32
_RlanActiveUserInPkts_Object = MibTableColumn
rlanActiveUserInPkts = _RlanActiveUserInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 4),
    _RlanActiveUserInPkts_Type()
)
rlanActiveUserInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveUserInPkts.setStatus("mandatory")
_RlanActiveUserOutPkts_Type = ZeroOrigCounter32
_RlanActiveUserOutPkts_Object = MibTableColumn
rlanActiveUserOutPkts = _RlanActiveUserOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 5),
    _RlanActiveUserOutPkts_Type()
)
rlanActiveUserOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveUserOutPkts.setStatus("mandatory")
_RlanActiveUserInOctets_Type = ZeroOrigCounter32
_RlanActiveUserInOctets_Object = MibTableColumn
rlanActiveUserInOctets = _RlanActiveUserInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 6),
    _RlanActiveUserInOctets_Type()
)
rlanActiveUserInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveUserInOctets.setStatus("mandatory")
_RlanActiveUserOutOctets_Type = ZeroOrigCounter32
_RlanActiveUserOutOctets_Object = MibTableColumn
rlanActiveUserOutOctets = _RlanActiveUserOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 7),
    _RlanActiveUserOutOctets_Type()
)
rlanActiveUserOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveUserOutOctets.setStatus("mandatory")
_RlanActiveUserActiveVC_Type = TruthValue
_RlanActiveUserActiveVC_Object = MibTableColumn
rlanActiveUserActiveVC = _RlanActiveUserActiveVC_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 8),
    _RlanActiveUserActiveVC_Type()
)
rlanActiveUserActiveVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveUserActiveVC.setStatus("mandatory")
_RlanActiveIpUserTable_Object = MibTable
rlanActiveIpUserTable = _RlanActiveIpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3)
)
if mibBuilder.loadTexts:
    rlanActiveIpUserTable.setStatus("mandatory")
_RlanActiveIpUserEntry_Object = MibTableRow
rlanActiveIpUserEntry = _RlanActiveIpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1)
)
rlanActiveIpUserEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlanActiveIpUserEntry.setStatus("mandatory")
_RlanActiveIpUserState_Type = CircuitState
_RlanActiveIpUserState_Object = MibTableColumn
rlanActiveIpUserState = _RlanActiveIpUserState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 1),
    _RlanActiveIpUserState_Type()
)
rlanActiveIpUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpUserState.setStatus("mandatory")
_RlanActiveIpUserPrevState_Type = CircuitState
_RlanActiveIpUserPrevState_Object = MibTableColumn
rlanActiveIpUserPrevState = _RlanActiveIpUserPrevState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 2),
    _RlanActiveIpUserPrevState_Type()
)
rlanActiveIpUserPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpUserPrevState.setStatus("mandatory")
_RlanActiveIpUserLocalAddr_Type = IpAddress
_RlanActiveIpUserLocalAddr_Object = MibTableColumn
rlanActiveIpUserLocalAddr = _RlanActiveIpUserLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 3),
    _RlanActiveIpUserLocalAddr_Type()
)
rlanActiveIpUserLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpUserLocalAddr.setStatus("mandatory")
_RlanActiveIpUserRemoteAddr_Type = IpAddress
_RlanActiveIpUserRemoteAddr_Object = MibTableColumn
rlanActiveIpUserRemoteAddr = _RlanActiveIpUserRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 4),
    _RlanActiveIpUserRemoteAddr_Type()
)
rlanActiveIpUserRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpUserRemoteAddr.setStatus("mandatory")
_RlanActiveIpUserRemoteMask_Type = IpAddress
_RlanActiveIpUserRemoteMask_Object = MibTableColumn
rlanActiveIpUserRemoteMask = _RlanActiveIpUserRemoteMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 5),
    _RlanActiveIpUserRemoteMask_Type()
)
rlanActiveIpUserRemoteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpUserRemoteMask.setStatus("mandatory")
_RlanActiveIpUserRemoteName_Type = DisplayString
_RlanActiveIpUserRemoteName_Object = MibTableColumn
rlanActiveIpUserRemoteName = _RlanActiveIpUserRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 6),
    _RlanActiveIpUserRemoteName_Type()
)
rlanActiveIpUserRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpUserRemoteName.setStatus("mandatory")
_RlanActiveNBUserTable_Object = MibTable
rlanActiveNBUserTable = _RlanActiveNBUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4)
)
if mibBuilder.loadTexts:
    rlanActiveNBUserTable.setStatus("mandatory")
_RlanActiveNBUserEntry_Object = MibTableRow
rlanActiveNBUserEntry = _RlanActiveNBUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1)
)
rlanActiveNBUserEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlanActiveNBUserEntry.setStatus("mandatory")
_RlanActiveNBUserState_Type = CircuitState
_RlanActiveNBUserState_Object = MibTableColumn
rlanActiveNBUserState = _RlanActiveNBUserState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 1),
    _RlanActiveNBUserState_Type()
)
rlanActiveNBUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveNBUserState.setStatus("mandatory")
_RlanActiveNBUserPrevState_Type = CircuitState
_RlanActiveNBUserPrevState_Object = MibTableColumn
rlanActiveNBUserPrevState = _RlanActiveNBUserPrevState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 2),
    _RlanActiveNBUserPrevState_Type()
)
rlanActiveNBUserPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveNBUserPrevState.setStatus("mandatory")


class _RlanActiveNBProtType_Type(Integer32):
    """Custom type rlanActiveNBProtType based on Integer32"""
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
        *(("bridgeProt", 5),
          ("nbContlProt", 3),
          ("nbFrameCntlProt", 4),
          ("negotiating", 2),
          ("notApplicable", 1))
    )


_RlanActiveNBProtType_Type.__name__ = "Integer32"
_RlanActiveNBProtType_Object = MibTableColumn
rlanActiveNBProtType = _RlanActiveNBProtType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 3),
    _RlanActiveNBProtType_Type()
)
rlanActiveNBProtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveNBProtType.setStatus("mandatory")
_RlanActiveNBUserLocalMac_Type = MacAddress
_RlanActiveNBUserLocalMac_Object = MibTableColumn
rlanActiveNBUserLocalMac = _RlanActiveNBUserLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 4),
    _RlanActiveNBUserLocalMac_Type()
)
rlanActiveNBUserLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveNBUserLocalMac.setStatus("mandatory")
_RlanActiveNBUserRemoteMac_Type = MacAddress
_RlanActiveNBUserRemoteMac_Object = MibTableColumn
rlanActiveNBUserRemoteMac = _RlanActiveNBUserRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 5),
    _RlanActiveNBUserRemoteMac_Type()
)
rlanActiveNBUserRemoteMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveNBUserRemoteMac.setStatus("mandatory")
_RlanActiveNBUserRemoteNames_Type = NBNames
_RlanActiveNBUserRemoteNames_Object = MibTableColumn
rlanActiveNBUserRemoteNames = _RlanActiveNBUserRemoteNames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 6),
    _RlanActiveNBUserRemoteNames_Type()
)
rlanActiveNBUserRemoteNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveNBUserRemoteNames.setStatus("mandatory")


class _RlanActiveNBUserRemoteClass_Type(Integer32):
    """Custom type rlanActiveNBUserRemoteClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlanActiveNBUserRemoteClass_Type.__name__ = "Integer32"
_RlanActiveNBUserRemoteClass_Object = MibTableColumn
rlanActiveNBUserRemoteClass = _RlanActiveNBUserRemoteClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 7),
    _RlanActiveNBUserRemoteClass_Type()
)
rlanActiveNBUserRemoteClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveNBUserRemoteClass.setStatus("mandatory")


class _RlanActiveNBUserRemoteVerMaj_Type(Integer32):
    """Custom type rlanActiveNBUserRemoteVerMaj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlanActiveNBUserRemoteVerMaj_Type.__name__ = "Integer32"
_RlanActiveNBUserRemoteVerMaj_Object = MibTableColumn
rlanActiveNBUserRemoteVerMaj = _RlanActiveNBUserRemoteVerMaj_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 8),
    _RlanActiveNBUserRemoteVerMaj_Type()
)
rlanActiveNBUserRemoteVerMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveNBUserRemoteVerMaj.setStatus("mandatory")


class _RlanActiveNBUserRemoteVerMin_Type(Integer32):
    """Custom type rlanActiveNBUserRemoteVerMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlanActiveNBUserRemoteVerMin_Type.__name__ = "Integer32"
_RlanActiveNBUserRemoteVerMin_Object = MibTableColumn
rlanActiveNBUserRemoteVerMin = _RlanActiveNBUserRemoteVerMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 9),
    _RlanActiveNBUserRemoteVerMin_Type()
)
rlanActiveNBUserRemoteVerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveNBUserRemoteVerMin.setStatus("mandatory")
_RlanActiveIpxUserTable_Object = MibTable
rlanActiveIpxUserTable = _RlanActiveIpxUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5)
)
if mibBuilder.loadTexts:
    rlanActiveIpxUserTable.setStatus("mandatory")
_RlanActiveIpxUserEntry_Object = MibTableRow
rlanActiveIpxUserEntry = _RlanActiveIpxUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1)
)
rlanActiveIpxUserEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlanActiveIpxUserEntry.setStatus("mandatory")
_RlanActiveIpxUserState_Type = CircuitState
_RlanActiveIpxUserState_Object = MibTableColumn
rlanActiveIpxUserState = _RlanActiveIpxUserState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1, 1),
    _RlanActiveIpxUserState_Type()
)
rlanActiveIpxUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpxUserState.setStatus("mandatory")
_RlanActiveIpxUserPrevState_Type = CircuitState
_RlanActiveIpxUserPrevState_Object = MibTableColumn
rlanActiveIpxUserPrevState = _RlanActiveIpxUserPrevState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1, 2),
    _RlanActiveIpxUserPrevState_Type()
)
rlanActiveIpxUserPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpxUserPrevState.setStatus("mandatory")
_RlanActiveIpxUserNetworkNum_Type = IpxNetworkNumber
_RlanActiveIpxUserNetworkNum_Object = MibTableColumn
rlanActiveIpxUserNetworkNum = _RlanActiveIpxUserNetworkNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1, 3),
    _RlanActiveIpxUserNetworkNum_Type()
)
rlanActiveIpxUserNetworkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpxUserNetworkNum.setStatus("mandatory")
_RlanActiveIpxUserLocalNodeNum_Type = IpxNodeNumber
_RlanActiveIpxUserLocalNodeNum_Object = MibTableColumn
rlanActiveIpxUserLocalNodeNum = _RlanActiveIpxUserLocalNodeNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1, 4),
    _RlanActiveIpxUserLocalNodeNum_Type()
)
rlanActiveIpxUserLocalNodeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpxUserLocalNodeNum.setStatus("mandatory")
_RlanActiveIpxUserRemoteNodeNum_Type = IpxNodeNumber
_RlanActiveIpxUserRemoteNodeNum_Object = MibTableColumn
rlanActiveIpxUserRemoteNodeNum = _RlanActiveIpxUserRemoteNodeNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1, 5),
    _RlanActiveIpxUserRemoteNodeNum_Type()
)
rlanActiveIpxUserRemoteNodeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlanActiveIpxUserRemoteNodeNum.setStatus("mandatory")
_IbmRlanDomains_ObjectIdentity = ObjectIdentity
ibmRlanDomains = _IbmRlanDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 2)
)
_IbmRlanConformance_ObjectIdentity = ObjectIdentity
ibmRlanConformance = _IbmRlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3)
)
_RlanCompliances_ObjectIdentity = ObjectIdentity
rlanCompliances = _RlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 1)
)
_RlanCoreCompliance_ObjectIdentity = ObjectIdentity
rlanCoreCompliance = _RlanCoreCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 1, 1)
)
_RlanIpCompliance_ObjectIdentity = ObjectIdentity
rlanIpCompliance = _RlanIpCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 1, 2)
)
_RlanNBCompliance_ObjectIdentity = ObjectIdentity
rlanNBCompliance = _RlanNBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 1, 3)
)
_RlanIpxCompliance_ObjectIdentity = ObjectIdentity
rlanIpxCompliance = _RlanIpxCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 1, 4)
)
_RlanGroups_ObjectIdentity = ObjectIdentity
rlanGroups = _RlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 2)
)
_RlanActiveUserGroup_ObjectIdentity = ObjectIdentity
rlanActiveUserGroup = _RlanActiveUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 2, 1)
)
_RlanActiveIpUserGroup_ObjectIdentity = ObjectIdentity
rlanActiveIpUserGroup = _RlanActiveIpUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 2, 2)
)
_RlanActiveNBUserGroup_ObjectIdentity = ObjectIdentity
rlanActiveNBUserGroup = _RlanActiveNBUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 2, 3)
)
_RlanActiveIpxUserGroup_ObjectIdentity = ObjectIdentity
rlanActiveIpxUserGroup = _RlanActiveIpxUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 2, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMIROCRLAN-MIB",
    **{"NBNames": NBNames,
       "IpxNetworkNumber": IpxNetworkNumber,
       "IpxNodeNumber": IpxNodeNumber,
       "MacAddress": MacAddress,
       "CircuitState": CircuitState,
       "ZeroOrigCounter32": ZeroOrigCounter32,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "ibm2210": ibm2210,
       "ibmIROC": ibmIROC,
       "ibmIROCrouting": ibmIROCrouting,
       "ibmIROCroutingRlan": ibmIROCroutingRlan,
       "ibmRlanTraps": ibmRlanTraps,
       "ibmRlanMIB": ibmRlanMIB,
       "ibmRlanGeneral": ibmRlanGeneral,
       "rlanActiveUserTable": rlanActiveUserTable,
       "rlanActiveUserEntry": rlanActiveUserEntry,
       "rlanActiveUserName": rlanActiveUserName,
       "rlanActiveUserConnected": rlanActiveUserConnected,
       "rlanActiveUserTimeRemaining": rlanActiveUserTimeRemaining,
       "rlanActiveUserInPkts": rlanActiveUserInPkts,
       "rlanActiveUserOutPkts": rlanActiveUserOutPkts,
       "rlanActiveUserInOctets": rlanActiveUserInOctets,
       "rlanActiveUserOutOctets": rlanActiveUserOutOctets,
       "rlanActiveUserActiveVC": rlanActiveUserActiveVC,
       "rlanActiveIpUserTable": rlanActiveIpUserTable,
       "rlanActiveIpUserEntry": rlanActiveIpUserEntry,
       "rlanActiveIpUserState": rlanActiveIpUserState,
       "rlanActiveIpUserPrevState": rlanActiveIpUserPrevState,
       "rlanActiveIpUserLocalAddr": rlanActiveIpUserLocalAddr,
       "rlanActiveIpUserRemoteAddr": rlanActiveIpUserRemoteAddr,
       "rlanActiveIpUserRemoteMask": rlanActiveIpUserRemoteMask,
       "rlanActiveIpUserRemoteName": rlanActiveIpUserRemoteName,
       "rlanActiveNBUserTable": rlanActiveNBUserTable,
       "rlanActiveNBUserEntry": rlanActiveNBUserEntry,
       "rlanActiveNBUserState": rlanActiveNBUserState,
       "rlanActiveNBUserPrevState": rlanActiveNBUserPrevState,
       "rlanActiveNBProtType": rlanActiveNBProtType,
       "rlanActiveNBUserLocalMac": rlanActiveNBUserLocalMac,
       "rlanActiveNBUserRemoteMac": rlanActiveNBUserRemoteMac,
       "rlanActiveNBUserRemoteNames": rlanActiveNBUserRemoteNames,
       "rlanActiveNBUserRemoteClass": rlanActiveNBUserRemoteClass,
       "rlanActiveNBUserRemoteVerMaj": rlanActiveNBUserRemoteVerMaj,
       "rlanActiveNBUserRemoteVerMin": rlanActiveNBUserRemoteVerMin,
       "rlanActiveIpxUserTable": rlanActiveIpxUserTable,
       "rlanActiveIpxUserEntry": rlanActiveIpxUserEntry,
       "rlanActiveIpxUserState": rlanActiveIpxUserState,
       "rlanActiveIpxUserPrevState": rlanActiveIpxUserPrevState,
       "rlanActiveIpxUserNetworkNum": rlanActiveIpxUserNetworkNum,
       "rlanActiveIpxUserLocalNodeNum": rlanActiveIpxUserLocalNodeNum,
       "rlanActiveIpxUserRemoteNodeNum": rlanActiveIpxUserRemoteNodeNum,
       "ibmRlanDomains": ibmRlanDomains,
       "ibmRlanConformance": ibmRlanConformance,
       "rlanCompliances": rlanCompliances,
       "rlanCoreCompliance": rlanCoreCompliance,
       "rlanIpCompliance": rlanIpCompliance,
       "rlanNBCompliance": rlanNBCompliance,
       "rlanIpxCompliance": rlanIpxCompliance,
       "rlanGroups": rlanGroups,
       "rlanActiveUserGroup": rlanActiveUserGroup,
       "rlanActiveIpUserGroup": rlanActiveIpUserGroup,
       "rlanActiveNBUserGroup": rlanActiveNBUserGroup,
       "rlanActiveIpxUserGroup": rlanActiveIpxUserGroup}
)
