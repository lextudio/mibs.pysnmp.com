# SNMP MIB module (APERTUS-TNSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APERTUS-TNSERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:17 2024
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



class Tn3270AidKey(Integer32):
    """Custom type Tn3270AidKey based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pa1", 2),
          ("pa2", 3),
          ("pa3", 4),
          ("pf1", 5),
          ("pf10", 14),
          ("pf11", 15),
          ("pf12", 16),
          ("pf13", 17),
          ("pf14", 18),
          ("pf15", 19),
          ("pf16", 20),
          ("pf17", 21),
          ("pf18", 22),
          ("pf19", 23),
          ("pf2", 6),
          ("pf20", 24),
          ("pf21", 25),
          ("pf22", 26),
          ("pf23", 27),
          ("pf24", 28),
          ("pf3", 7),
          ("pf4", 8),
          ("pf5", 9),
          ("pf6", 10),
          ("pf7", 11),
          ("pf8", 12),
          ("pf9", 13))
    )





class Tn5250AidKey(Integer32):
    """Custom type Tn5250AidKey based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("attn", 30),
          ("none", 1),
          ("pa1", 2),
          ("pa2", 3),
          ("pa3", 4),
          ("pf1", 5),
          ("pf10", 14),
          ("pf11", 15),
          ("pf12", 16),
          ("pf13", 17),
          ("pf14", 18),
          ("pf15", 19),
          ("pf16", 20),
          ("pf17", 21),
          ("pf18", 22),
          ("pf19", 23),
          ("pf2", 6),
          ("pf20", 24),
          ("pf21", 25),
          ("pf22", 26),
          ("pf23", 27),
          ("pf24", 28),
          ("pf3", 7),
          ("pf4", 8),
          ("pf5", 9),
          ("pf6", 10),
          ("pf7", 11),
          ("pf8", 12),
          ("pf9", 13),
          ("sysreq", 29),
          ("test", 31))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Apertus_ObjectIdentity = ObjectIdentity
apertus = _Apertus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543)
)
_Express_ObjectIdentity = ObjectIdentity
express = _Express_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3)
)
_AperTnServMIB_ObjectIdentity = ObjectIdentity
aperTnServMIB = _AperTnServMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1)
)
_AperTnServMibVersionNumber_Type = Integer32
_AperTnServMibVersionNumber_Object = MibScalar
aperTnServMibVersionNumber = _AperTnServMibVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 1),
    _AperTnServMibVersionNumber_Type()
)
aperTnServMibVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServMibVersionNumber.setStatus("mandatory")
_AperTnServAdm_ObjectIdentity = ObjectIdentity
aperTnServAdm = _AperTnServAdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2)
)
_AperTnServAdmGen_ObjectIdentity = ObjectIdentity
aperTnServAdmGen = _AperTnServAdmGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1)
)
_AperTnServAdmRelease_Type = DisplayString
_AperTnServAdmRelease_Object = MibScalar
aperTnServAdmRelease = _AperTnServAdmRelease_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 1),
    _AperTnServAdmRelease_Type()
)
aperTnServAdmRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmRelease.setStatus("mandatory")
_AperTnServAdmSCN_Type = Integer32
_AperTnServAdmSCN_Object = MibScalar
aperTnServAdmSCN = _AperTnServAdmSCN_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 2),
    _AperTnServAdmSCN_Type()
)
aperTnServAdmSCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmSCN.setStatus("mandatory")
_AperTnServAdmServerInstanceName_Type = DisplayString
_AperTnServAdmServerInstanceName_Object = MibScalar
aperTnServAdmServerInstanceName = _AperTnServAdmServerInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 3),
    _AperTnServAdmServerInstanceName_Type()
)
aperTnServAdmServerInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmServerInstanceName.setStatus("mandatory")
_AperTnServAdmMaxSessions_Type = Integer32
_AperTnServAdmMaxSessions_Object = MibScalar
aperTnServAdmMaxSessions = _AperTnServAdmMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 4),
    _AperTnServAdmMaxSessions_Type()
)
aperTnServAdmMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmMaxSessions.setStatus("mandatory")
_AperTnServAdmKeepAliveTimer_Type = Integer32
_AperTnServAdmKeepAliveTimer_Object = MibScalar
aperTnServAdmKeepAliveTimer = _AperTnServAdmKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 5),
    _AperTnServAdmKeepAliveTimer_Type()
)
aperTnServAdmKeepAliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmKeepAliveTimer.setStatus("mandatory")
_AperTnServAdmKeepAliveResponseTimeout_Type = Integer32
_AperTnServAdmKeepAliveResponseTimeout_Object = MibScalar
aperTnServAdmKeepAliveResponseTimeout = _AperTnServAdmKeepAliveResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 6),
    _AperTnServAdmKeepAliveResponseTimeout_Type()
)
aperTnServAdmKeepAliveResponseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmKeepAliveResponseTimeout.setStatus("mandatory")
_AperTnServAdmKeepAliveRetryCount_Type = Integer32
_AperTnServAdmKeepAliveRetryCount_Object = MibScalar
aperTnServAdmKeepAliveRetryCount = _AperTnServAdmKeepAliveRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 7),
    _AperTnServAdmKeepAliveRetryCount_Type()
)
aperTnServAdmKeepAliveRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmKeepAliveRetryCount.setStatus("mandatory")
_AperTnServAdmDefaultInactivityLimit_Type = Integer32
_AperTnServAdmDefaultInactivityLimit_Object = MibScalar
aperTnServAdmDefaultInactivityLimit = _AperTnServAdmDefaultInactivityLimit_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 8),
    _AperTnServAdmDefaultInactivityLimit_Type()
)
aperTnServAdmDefaultInactivityLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmDefaultInactivityLimit.setStatus("mandatory")


class _AperTnServAdmUndefinedClients_Type(Integer32):
    """Custom type aperTnServAdmUndefinedClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prompt", 1),
          ("reject", 2))
    )


_AperTnServAdmUndefinedClients_Type.__name__ = "Integer32"
_AperTnServAdmUndefinedClients_Object = MibScalar
aperTnServAdmUndefinedClients = _AperTnServAdmUndefinedClients_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 9),
    _AperTnServAdmUndefinedClients_Type()
)
aperTnServAdmUndefinedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUndefinedClients.setStatus("mandatory")


class _AperTnServAdmAllowableNameTypes_Type(Integer32):
    """Custom type aperTnServAdmAllowableNameTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("user", 2))
    )


_AperTnServAdmAllowableNameTypes_Type.__name__ = "Integer32"
_AperTnServAdmAllowableNameTypes_Object = MibScalar
aperTnServAdmAllowableNameTypes = _AperTnServAdmAllowableNameTypes_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 10),
    _AperTnServAdmAllowableNameTypes_Type()
)
aperTnServAdmAllowableNameTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmAllowableNameTypes.setStatus("mandatory")
_AperTnServAdmNumPorts_Type = Integer32
_AperTnServAdmNumPorts_Object = MibScalar
aperTnServAdmNumPorts = _AperTnServAdmNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 11),
    _AperTnServAdmNumPorts_Type()
)
aperTnServAdmNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmNumPorts.setStatus("mandatory")
_AperTnServAdmPortTable_Object = MibTable
aperTnServAdmPortTable = _AperTnServAdmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 12)
)
if mibBuilder.loadTexts:
    aperTnServAdmPortTable.setStatus("mandatory")
_AperTnServAdmPortEntry_Object = MibTableRow
aperTnServAdmPortEntry = _AperTnServAdmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 12, 1)
)
aperTnServAdmPortEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdmPort"),
)
if mibBuilder.loadTexts:
    aperTnServAdmPortEntry.setStatus("mandatory")
_AperTnServAdmPort_Type = Integer32
_AperTnServAdmPort_Object = MibTableColumn
aperTnServAdmPort = _AperTnServAdmPort_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 12, 1, 1),
    _AperTnServAdmPort_Type()
)
aperTnServAdmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmPort.setStatus("mandatory")


class _AperTnServAdmMenuMode_Type(Integer32):
    """Custom type aperTnServAdmMenuMode based on Integer32"""
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


_AperTnServAdmMenuMode_Type.__name__ = "Integer32"
_AperTnServAdmMenuMode_Object = MibScalar
aperTnServAdmMenuMode = _AperTnServAdmMenuMode_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 13),
    _AperTnServAdmMenuMode_Type()
)
aperTnServAdmMenuMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmMenuMode.setStatus("mandatory")
_AperTnServAdmPasswordLimit_Type = Integer32
_AperTnServAdmPasswordLimit_Object = MibScalar
aperTnServAdmPasswordLimit = _AperTnServAdmPasswordLimit_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 14),
    _AperTnServAdmPasswordLimit_Type()
)
aperTnServAdmPasswordLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmPasswordLimit.setStatus("mandatory")
_AperTnServAdmNumGroups_Type = Integer32
_AperTnServAdmNumGroups_Object = MibScalar
aperTnServAdmNumGroups = _AperTnServAdmNumGroups_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 15),
    _AperTnServAdmNumGroups_Type()
)
aperTnServAdmNumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmNumGroups.setStatus("mandatory")
_AperTnServAdmGroupTableLastChange_Type = TimeTicks
_AperTnServAdmGroupTableLastChange_Object = MibScalar
aperTnServAdmGroupTableLastChange = _AperTnServAdmGroupTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 16),
    _AperTnServAdmGroupTableLastChange_Type()
)
aperTnServAdmGroupTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroupTableLastChange.setStatus("mandatory")
_AperTnServAdmGroupTable_Object = MibTable
aperTnServAdmGroupTable = _AperTnServAdmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17)
)
if mibBuilder.loadTexts:
    aperTnServAdmGroupTable.setStatus("mandatory")
_AperTnServAdmGroupEntry_Object = MibTableRow
aperTnServAdmGroupEntry = _AperTnServAdmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1)
)
aperTnServAdmGroupEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdmGroupName"),
)
if mibBuilder.loadTexts:
    aperTnServAdmGroupEntry.setStatus("mandatory")
_AperTnServAdmGroupName_Type = DisplayString
_AperTnServAdmGroupName_Object = MibTableColumn
aperTnServAdmGroupName = _AperTnServAdmGroupName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1, 1),
    _AperTnServAdmGroupName_Type()
)
aperTnServAdmGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroupName.setStatus("mandatory")
_AperTnServAdmGroupDescription_Type = DisplayString
_AperTnServAdmGroupDescription_Object = MibTableColumn
aperTnServAdmGroupDescription = _AperTnServAdmGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1, 2),
    _AperTnServAdmGroupDescription_Type()
)
aperTnServAdmGroupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroupDescription.setStatus("mandatory")


class _AperTnServAdmGroupMenuMode_Type(Integer32):
    """Custom type aperTnServAdmGroupMenuMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("off", 2),
          ("on", 1))
    )


_AperTnServAdmGroupMenuMode_Type.__name__ = "Integer32"
_AperTnServAdmGroupMenuMode_Object = MibTableColumn
aperTnServAdmGroupMenuMode = _AperTnServAdmGroupMenuMode_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1, 3),
    _AperTnServAdmGroupMenuMode_Type()
)
aperTnServAdmGroupMenuMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroupMenuMode.setStatus("mandatory")
_AperTnServAdmGroupInactivityLimit_Type = Integer32
_AperTnServAdmGroupInactivityLimit_Object = MibTableColumn
aperTnServAdmGroupInactivityLimit = _AperTnServAdmGroupInactivityLimit_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1, 4),
    _AperTnServAdmGroupInactivityLimit_Type()
)
aperTnServAdmGroupInactivityLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroupInactivityLimit.setStatus("mandatory")
_AperTnServAdmGroup3270StatusKey_Type = Tn3270AidKey
_AperTnServAdmGroup3270StatusKey_Object = MibTableColumn
aperTnServAdmGroup3270StatusKey = _AperTnServAdmGroup3270StatusKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1, 5),
    _AperTnServAdmGroup3270StatusKey_Type()
)
aperTnServAdmGroup3270StatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroup3270StatusKey.setStatus("mandatory")
_AperTnServAdmGroup3270PasswordKey_Type = Tn3270AidKey
_AperTnServAdmGroup3270PasswordKey_Object = MibTableColumn
aperTnServAdmGroup3270PasswordKey = _AperTnServAdmGroup3270PasswordKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1, 6),
    _AperTnServAdmGroup3270PasswordKey_Type()
)
aperTnServAdmGroup3270PasswordKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroup3270PasswordKey.setStatus("mandatory")
_AperTnServAdmGroup3270SysReqKey_Type = Tn3270AidKey
_AperTnServAdmGroup3270SysReqKey_Object = MibTableColumn
aperTnServAdmGroup3270SysReqKey = _AperTnServAdmGroup3270SysReqKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1, 7),
    _AperTnServAdmGroup3270SysReqKey_Type()
)
aperTnServAdmGroup3270SysReqKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroup3270SysReqKey.setStatus("mandatory")
_AperTnServAdmGroup3270AttnKey_Type = Tn3270AidKey
_AperTnServAdmGroup3270AttnKey_Object = MibTableColumn
aperTnServAdmGroup3270AttnKey = _AperTnServAdmGroup3270AttnKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1, 8),
    _AperTnServAdmGroup3270AttnKey_Type()
)
aperTnServAdmGroup3270AttnKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroup3270AttnKey.setStatus("mandatory")
_AperTnServAdmGroup5250StatusKey_Type = Tn5250AidKey
_AperTnServAdmGroup5250StatusKey_Object = MibTableColumn
aperTnServAdmGroup5250StatusKey = _AperTnServAdmGroup5250StatusKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1, 9),
    _AperTnServAdmGroup5250StatusKey_Type()
)
aperTnServAdmGroup5250StatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroup5250StatusKey.setStatus("mandatory")
_AperTnServAdmGroup5250PasswordKey_Type = Tn5250AidKey
_AperTnServAdmGroup5250PasswordKey_Object = MibTableColumn
aperTnServAdmGroup5250PasswordKey = _AperTnServAdmGroup5250PasswordKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 17, 1, 10),
    _AperTnServAdmGroup5250PasswordKey_Type()
)
aperTnServAdmGroup5250PasswordKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmGroup5250PasswordKey.setStatus("mandatory")
_AperTnServAdmNumUsers_Type = Integer32
_AperTnServAdmNumUsers_Object = MibScalar
aperTnServAdmNumUsers = _AperTnServAdmNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 18),
    _AperTnServAdmNumUsers_Type()
)
aperTnServAdmNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmNumUsers.setStatus("mandatory")
_AperTnServAdmUserTableLastChange_Type = TimeTicks
_AperTnServAdmUserTableLastChange_Object = MibScalar
aperTnServAdmUserTableLastChange = _AperTnServAdmUserTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 19),
    _AperTnServAdmUserTableLastChange_Type()
)
aperTnServAdmUserTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUserTableLastChange.setStatus("mandatory")
_AperTnServAdmUserTable_Object = MibTable
aperTnServAdmUserTable = _AperTnServAdmUserTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20)
)
if mibBuilder.loadTexts:
    aperTnServAdmUserTable.setStatus("mandatory")
_AperTnServAdmUserEntry_Object = MibTableRow
aperTnServAdmUserEntry = _AperTnServAdmUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1)
)
aperTnServAdmUserEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdmUserName"),
)
if mibBuilder.loadTexts:
    aperTnServAdmUserEntry.setStatus("mandatory")
_AperTnServAdmUserName_Type = DisplayString
_AperTnServAdmUserName_Object = MibTableColumn
aperTnServAdmUserName = _AperTnServAdmUserName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 1),
    _AperTnServAdmUserName_Type()
)
aperTnServAdmUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUserName.setStatus("mandatory")
_AperTnServAdmUserDescription_Type = DisplayString
_AperTnServAdmUserDescription_Object = MibTableColumn
aperTnServAdmUserDescription = _AperTnServAdmUserDescription_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 2),
    _AperTnServAdmUserDescription_Type()
)
aperTnServAdmUserDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUserDescription.setStatus("mandatory")


class _AperTnServAdmUserPasswordRequired_Type(Integer32):
    """Custom type aperTnServAdmUserPasswordRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServAdmUserPasswordRequired_Type.__name__ = "Integer32"
_AperTnServAdmUserPasswordRequired_Object = MibTableColumn
aperTnServAdmUserPasswordRequired = _AperTnServAdmUserPasswordRequired_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 3),
    _AperTnServAdmUserPasswordRequired_Type()
)
aperTnServAdmUserPasswordRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUserPasswordRequired.setStatus("mandatory")
_AperTnServAdmUserEncryptedPassword_Type = Integer32
_AperTnServAdmUserEncryptedPassword_Object = MibTableColumn
aperTnServAdmUserEncryptedPassword = _AperTnServAdmUserEncryptedPassword_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 4),
    _AperTnServAdmUserEncryptedPassword_Type()
)
aperTnServAdmUserEncryptedPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUserEncryptedPassword.setStatus("mandatory")
_AperTnServAdmUserBadPasswordCounter_Type = Integer32
_AperTnServAdmUserBadPasswordCounter_Object = MibTableColumn
aperTnServAdmUserBadPasswordCounter = _AperTnServAdmUserBadPasswordCounter_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 5),
    _AperTnServAdmUserBadPasswordCounter_Type()
)
aperTnServAdmUserBadPasswordCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUserBadPasswordCounter.setStatus("mandatory")


class _AperTnServAdmUserMenuMode_Type(Integer32):
    """Custom type aperTnServAdmUserMenuMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("off", 2),
          ("on", 1))
    )


_AperTnServAdmUserMenuMode_Type.__name__ = "Integer32"
_AperTnServAdmUserMenuMode_Object = MibTableColumn
aperTnServAdmUserMenuMode = _AperTnServAdmUserMenuMode_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 6),
    _AperTnServAdmUserMenuMode_Type()
)
aperTnServAdmUserMenuMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUserMenuMode.setStatus("mandatory")
_AperTnServAdmUserInactivityLimit_Type = Integer32
_AperTnServAdmUserInactivityLimit_Object = MibTableColumn
aperTnServAdmUserInactivityLimit = _AperTnServAdmUserInactivityLimit_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 7),
    _AperTnServAdmUserInactivityLimit_Type()
)
aperTnServAdmUserInactivityLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUserInactivityLimit.setStatus("mandatory")
_AperTnServAdmUser3270StatusKey_Type = Tn3270AidKey
_AperTnServAdmUser3270StatusKey_Object = MibTableColumn
aperTnServAdmUser3270StatusKey = _AperTnServAdmUser3270StatusKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 8),
    _AperTnServAdmUser3270StatusKey_Type()
)
aperTnServAdmUser3270StatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUser3270StatusKey.setStatus("mandatory")
_AperTnServAdmUser3270PasswordKey_Type = Tn3270AidKey
_AperTnServAdmUser3270PasswordKey_Object = MibTableColumn
aperTnServAdmUser3270PasswordKey = _AperTnServAdmUser3270PasswordKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 9),
    _AperTnServAdmUser3270PasswordKey_Type()
)
aperTnServAdmUser3270PasswordKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUser3270PasswordKey.setStatus("mandatory")
_AperTnServAdmUser3270SysReqKey_Type = Tn3270AidKey
_AperTnServAdmUser3270SysReqKey_Object = MibTableColumn
aperTnServAdmUser3270SysReqKey = _AperTnServAdmUser3270SysReqKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 10),
    _AperTnServAdmUser3270SysReqKey_Type()
)
aperTnServAdmUser3270SysReqKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUser3270SysReqKey.setStatus("mandatory")
_AperTnServAdmUser3270AttnKey_Type = Tn3270AidKey
_AperTnServAdmUser3270AttnKey_Object = MibTableColumn
aperTnServAdmUser3270AttnKey = _AperTnServAdmUser3270AttnKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 11),
    _AperTnServAdmUser3270AttnKey_Type()
)
aperTnServAdmUser3270AttnKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUser3270AttnKey.setStatus("mandatory")
_AperTnServAdmUser5250StatusKey_Type = Tn5250AidKey
_AperTnServAdmUser5250StatusKey_Object = MibTableColumn
aperTnServAdmUser5250StatusKey = _AperTnServAdmUser5250StatusKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 12),
    _AperTnServAdmUser5250StatusKey_Type()
)
aperTnServAdmUser5250StatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUser5250StatusKey.setStatus("mandatory")
_AperTnServAdmUser5250PasswordKey_Type = Tn5250AidKey
_AperTnServAdmUser5250PasswordKey_Object = MibTableColumn
aperTnServAdmUser5250PasswordKey = _AperTnServAdmUser5250PasswordKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 20, 1, 13),
    _AperTnServAdmUser5250PasswordKey_Type()
)
aperTnServAdmUser5250PasswordKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmUser5250PasswordKey.setStatus("mandatory")
_AperTnServAdmNumRoutingEntries_Type = Integer32
_AperTnServAdmNumRoutingEntries_Object = MibScalar
aperTnServAdmNumRoutingEntries = _AperTnServAdmNumRoutingEntries_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 21),
    _AperTnServAdmNumRoutingEntries_Type()
)
aperTnServAdmNumRoutingEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmNumRoutingEntries.setStatus("mandatory")
_AperTnServAdmRoutingTableLastChange_Type = TimeTicks
_AperTnServAdmRoutingTableLastChange_Object = MibScalar
aperTnServAdmRoutingTableLastChange = _AperTnServAdmRoutingTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 22),
    _AperTnServAdmRoutingTableLastChange_Type()
)
aperTnServAdmRoutingTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmRoutingTableLastChange.setStatus("mandatory")
_AperTnServAdmRoutingTable_Object = MibTable
aperTnServAdmRoutingTable = _AperTnServAdmRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 23)
)
if mibBuilder.loadTexts:
    aperTnServAdmRoutingTable.setStatus("mandatory")
_AperTnServAdmRoutingEntry_Object = MibTableRow
aperTnServAdmRoutingEntry = _AperTnServAdmRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 23, 1)
)
aperTnServAdmRoutingEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdmRoutingSourceIp"),
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdmRoutingPort"),
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdmRoutingDeviceType"),
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdmRoutingModelType"),
)
if mibBuilder.loadTexts:
    aperTnServAdmRoutingEntry.setStatus("mandatory")
_AperTnServAdmRoutingSourceIp_Type = DisplayString
_AperTnServAdmRoutingSourceIp_Object = MibTableColumn
aperTnServAdmRoutingSourceIp = _AperTnServAdmRoutingSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 23, 1, 1),
    _AperTnServAdmRoutingSourceIp_Type()
)
aperTnServAdmRoutingSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmRoutingSourceIp.setStatus("mandatory")
_AperTnServAdmRoutingPort_Type = Integer32
_AperTnServAdmRoutingPort_Object = MibTableColumn
aperTnServAdmRoutingPort = _AperTnServAdmRoutingPort_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 23, 1, 2),
    _AperTnServAdmRoutingPort_Type()
)
aperTnServAdmRoutingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmRoutingPort.setStatus("mandatory")


class _AperTnServAdmRoutingDeviceType_Type(Integer32):
    """Custom type aperTnServAdmRoutingDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("display3270", 1),
          ("display5250", 3),
          ("printer3270", 2))
    )


_AperTnServAdmRoutingDeviceType_Type.__name__ = "Integer32"
_AperTnServAdmRoutingDeviceType_Object = MibTableColumn
aperTnServAdmRoutingDeviceType = _AperTnServAdmRoutingDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 23, 1, 3),
    _AperTnServAdmRoutingDeviceType_Type()
)
aperTnServAdmRoutingDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmRoutingDeviceType.setStatus("mandatory")


class _AperTnServAdmRoutingModelType_Type(Integer32):
    """Custom type aperTnServAdmRoutingModelType based on Integer32"""
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
        *(("any", 6),
          ("dynamic", 5),
          ("model2", 1),
          ("model3", 2),
          ("model4", 3),
          ("model5", 4))
    )


_AperTnServAdmRoutingModelType_Type.__name__ = "Integer32"
_AperTnServAdmRoutingModelType_Object = MibTableColumn
aperTnServAdmRoutingModelType = _AperTnServAdmRoutingModelType_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 23, 1, 4),
    _AperTnServAdmRoutingModelType_Type()
)
aperTnServAdmRoutingModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmRoutingModelType.setStatus("mandatory")
_AperTnServAdmRoutingDescription_Type = DisplayString
_AperTnServAdmRoutingDescription_Object = MibTableColumn
aperTnServAdmRoutingDescription = _AperTnServAdmRoutingDescription_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 23, 1, 5),
    _AperTnServAdmRoutingDescription_Type()
)
aperTnServAdmRoutingDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmRoutingDescription.setStatus("mandatory")


class _AperTnServAdmRoutingDestinationType_Type(Integer32):
    """Custom type aperTnServAdmRoutingDestinationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lu", 2),
          ("symbolicdestination", 3),
          ("user", 1))
    )


_AperTnServAdmRoutingDestinationType_Type.__name__ = "Integer32"
_AperTnServAdmRoutingDestinationType_Object = MibTableColumn
aperTnServAdmRoutingDestinationType = _AperTnServAdmRoutingDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 23, 1, 6),
    _AperTnServAdmRoutingDestinationType_Type()
)
aperTnServAdmRoutingDestinationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmRoutingDestinationType.setStatus("mandatory")
_AperTnServAdmRoutingDestination_Type = DisplayString
_AperTnServAdmRoutingDestination_Object = MibTableColumn
aperTnServAdmRoutingDestination = _AperTnServAdmRoutingDestination_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 23, 1, 7),
    _AperTnServAdmRoutingDestination_Type()
)
aperTnServAdmRoutingDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmRoutingDestination.setStatus("mandatory")
_AperTnServAdmNumSecurAccEntries_Type = Integer32
_AperTnServAdmNumSecurAccEntries_Object = MibScalar
aperTnServAdmNumSecurAccEntries = _AperTnServAdmNumSecurAccEntries_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 24),
    _AperTnServAdmNumSecurAccEntries_Type()
)
aperTnServAdmNumSecurAccEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmNumSecurAccEntries.setStatus("mandatory")
_AperTnServAdmSecurAccTableLastChange_Type = TimeTicks
_AperTnServAdmSecurAccTableLastChange_Object = MibScalar
aperTnServAdmSecurAccTableLastChange = _AperTnServAdmSecurAccTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 25),
    _AperTnServAdmSecurAccTableLastChange_Type()
)
aperTnServAdmSecurAccTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmSecurAccTableLastChange.setStatus("mandatory")
_AperTnServAdmSecurAccTable_Object = MibTable
aperTnServAdmSecurAccTable = _AperTnServAdmSecurAccTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 26)
)
if mibBuilder.loadTexts:
    aperTnServAdmSecurAccTable.setStatus("mandatory")
_AperTnServAdmSecurAccEntry_Object = MibTableRow
aperTnServAdmSecurAccEntry = _AperTnServAdmSecurAccEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 26, 1)
)
aperTnServAdmSecurAccEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdmSecurAccSourceIp"),
)
if mibBuilder.loadTexts:
    aperTnServAdmSecurAccEntry.setStatus("mandatory")
_AperTnServAdmSecurAccSourceIp_Type = DisplayString
_AperTnServAdmSecurAccSourceIp_Object = MibTableColumn
aperTnServAdmSecurAccSourceIp = _AperTnServAdmSecurAccSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 26, 1, 1),
    _AperTnServAdmSecurAccSourceIp_Type()
)
aperTnServAdmSecurAccSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmSecurAccSourceIp.setStatus("mandatory")
_AperTnServAdmSecurAccDescription_Type = DisplayString
_AperTnServAdmSecurAccDescription_Object = MibTableColumn
aperTnServAdmSecurAccDescription = _AperTnServAdmSecurAccDescription_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 26, 1, 2),
    _AperTnServAdmSecurAccDescription_Type()
)
aperTnServAdmSecurAccDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmSecurAccDescription.setStatus("mandatory")
_AperTnServAdmSecurAccDestination_Type = DisplayString
_AperTnServAdmSecurAccDestination_Object = MibTableColumn
aperTnServAdmSecurAccDestination = _AperTnServAdmSecurAccDestination_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 1, 26, 1, 3),
    _AperTnServAdmSecurAccDestination_Type()
)
aperTnServAdmSecurAccDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdmSecurAccDestination.setStatus("mandatory")
_AperTnServAdm3270_ObjectIdentity = ObjectIdentity
aperTnServAdm3270 = _AperTnServAdm3270_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2)
)
_AperTnServAdm3270DefaultStatusKey_Type = Tn3270AidKey
_AperTnServAdm3270DefaultStatusKey_Object = MibScalar
aperTnServAdm3270DefaultStatusKey = _AperTnServAdm3270DefaultStatusKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 1),
    _AperTnServAdm3270DefaultStatusKey_Type()
)
aperTnServAdm3270DefaultStatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270DefaultStatusKey.setStatus("mandatory")
_AperTnServAdm3270DefaultSysReqKey_Type = Tn3270AidKey
_AperTnServAdm3270DefaultSysReqKey_Object = MibScalar
aperTnServAdm3270DefaultSysReqKey = _AperTnServAdm3270DefaultSysReqKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 2),
    _AperTnServAdm3270DefaultSysReqKey_Type()
)
aperTnServAdm3270DefaultSysReqKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270DefaultSysReqKey.setStatus("mandatory")
_AperTnServAdm3270DefaultAttnKey_Type = Tn3270AidKey
_AperTnServAdm3270DefaultAttnKey_Object = MibScalar
aperTnServAdm3270DefaultAttnKey = _AperTnServAdm3270DefaultAttnKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 3),
    _AperTnServAdm3270DefaultAttnKey_Type()
)
aperTnServAdm3270DefaultAttnKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270DefaultAttnKey.setStatus("mandatory")
_AperTnServAdm3270DefaultPasswordKey_Type = Tn3270AidKey
_AperTnServAdm3270DefaultPasswordKey_Object = MibScalar
aperTnServAdm3270DefaultPasswordKey = _AperTnServAdm3270DefaultPasswordKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 4),
    _AperTnServAdm3270DefaultPasswordKey_Type()
)
aperTnServAdm3270DefaultPasswordKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270DefaultPasswordKey.setStatus("mandatory")


class _AperTnServAdm3270LoadBalanceMode_Type(Integer32):
    """Custom type aperTnServAdm3270LoadBalanceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firstavaillu", 2),
          ("links", 1))
    )


_AperTnServAdm3270LoadBalanceMode_Type.__name__ = "Integer32"
_AperTnServAdm3270LoadBalanceMode_Object = MibScalar
aperTnServAdm3270LoadBalanceMode = _AperTnServAdm3270LoadBalanceMode_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 5),
    _AperTnServAdm3270LoadBalanceMode_Type()
)
aperTnServAdm3270LoadBalanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270LoadBalanceMode.setStatus("mandatory")
_AperTnServAdm3270NumSessions_Type = Integer32
_AperTnServAdm3270NumSessions_Object = MibScalar
aperTnServAdm3270NumSessions = _AperTnServAdm3270NumSessions_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 6),
    _AperTnServAdm3270NumSessions_Type()
)
aperTnServAdm3270NumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270NumSessions.setStatus("mandatory")
_AperTnServAdm3270SessionTableLastChange_Type = TimeTicks
_AperTnServAdm3270SessionTableLastChange_Object = MibScalar
aperTnServAdm3270SessionTableLastChange = _AperTnServAdm3270SessionTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 7),
    _AperTnServAdm3270SessionTableLastChange_Type()
)
aperTnServAdm3270SessionTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270SessionTableLastChange.setStatus("mandatory")
_AperTnServAdm3270SessionTable_Object = MibTable
aperTnServAdm3270SessionTable = _AperTnServAdm3270SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    aperTnServAdm3270SessionTable.setStatus("mandatory")
_AperTnServAdm3270SessionEntry_Object = MibTableRow
aperTnServAdm3270SessionEntry = _AperTnServAdm3270SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 8, 1)
)
aperTnServAdm3270SessionEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdm3270SessionGroupOrUserName"),
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdm3270SessionName"),
)
if mibBuilder.loadTexts:
    aperTnServAdm3270SessionEntry.setStatus("mandatory")
_AperTnServAdm3270SessionGroupOrUserName_Type = DisplayString
_AperTnServAdm3270SessionGroupOrUserName_Object = MibTableColumn
aperTnServAdm3270SessionGroupOrUserName = _AperTnServAdm3270SessionGroupOrUserName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 8, 1, 1),
    _AperTnServAdm3270SessionGroupOrUserName_Type()
)
aperTnServAdm3270SessionGroupOrUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270SessionGroupOrUserName.setStatus("mandatory")
_AperTnServAdm3270SessionName_Type = DisplayString
_AperTnServAdm3270SessionName_Object = MibTableColumn
aperTnServAdm3270SessionName = _AperTnServAdm3270SessionName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 8, 1, 2),
    _AperTnServAdm3270SessionName_Type()
)
aperTnServAdm3270SessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270SessionName.setStatus("mandatory")
_AperTnServAdm3270SessionDescription_Type = DisplayString
_AperTnServAdm3270SessionDescription_Object = MibTableColumn
aperTnServAdm3270SessionDescription = _AperTnServAdm3270SessionDescription_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 8, 1, 3),
    _AperTnServAdm3270SessionDescription_Type()
)
aperTnServAdm3270SessionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270SessionDescription.setStatus("mandatory")


class _AperTnServAdm3270SessionGroupOrUser_Type(Integer32):
    """Custom type aperTnServAdm3270SessionGroupOrUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 1),
          ("user", 2))
    )


_AperTnServAdm3270SessionGroupOrUser_Type.__name__ = "Integer32"
_AperTnServAdm3270SessionGroupOrUser_Object = MibTableColumn
aperTnServAdm3270SessionGroupOrUser = _AperTnServAdm3270SessionGroupOrUser_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 8, 1, 4),
    _AperTnServAdm3270SessionGroupOrUser_Type()
)
aperTnServAdm3270SessionGroupOrUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270SessionGroupOrUser.setStatus("mandatory")


class _AperTnServAdm3270SessionType_Type(Integer32):
    """Custom type aperTnServAdm3270SessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("display", 1),
          ("printer", 2))
    )


_AperTnServAdm3270SessionType_Type.__name__ = "Integer32"
_AperTnServAdm3270SessionType_Object = MibTableColumn
aperTnServAdm3270SessionType = _AperTnServAdm3270SessionType_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 8, 1, 5),
    _AperTnServAdm3270SessionType_Type()
)
aperTnServAdm3270SessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270SessionType.setStatus("mandatory")


class _AperTnServAdm3270SessionModel_Type(Integer32):
    """Custom type aperTnServAdm3270SessionModel based on Integer32"""
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
        *(("dynamic", 5),
          ("model2", 1),
          ("model3", 2),
          ("model4", 3),
          ("model5", 4))
    )


_AperTnServAdm3270SessionModel_Type.__name__ = "Integer32"
_AperTnServAdm3270SessionModel_Object = MibTableColumn
aperTnServAdm3270SessionModel = _AperTnServAdm3270SessionModel_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 8, 1, 6),
    _AperTnServAdm3270SessionModel_Type()
)
aperTnServAdm3270SessionModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270SessionModel.setStatus("mandatory")
_AperTnServAdm3270SessionDestination_Type = DisplayString
_AperTnServAdm3270SessionDestination_Object = MibTableColumn
aperTnServAdm3270SessionDestination = _AperTnServAdm3270SessionDestination_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 2, 8, 1, 7),
    _AperTnServAdm3270SessionDestination_Type()
)
aperTnServAdm3270SessionDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm3270SessionDestination.setStatus("mandatory")
_AperTnServAdm5250_ObjectIdentity = ObjectIdentity
aperTnServAdm5250 = _AperTnServAdm5250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3)
)
_AperTnServAdm5250DefaultStatusKey_Type = Tn5250AidKey
_AperTnServAdm5250DefaultStatusKey_Object = MibScalar
aperTnServAdm5250DefaultStatusKey = _AperTnServAdm5250DefaultStatusKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 1),
    _AperTnServAdm5250DefaultStatusKey_Type()
)
aperTnServAdm5250DefaultStatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250DefaultStatusKey.setStatus("mandatory")
_AperTnServAdm5250DefaultPasswordKey_Type = Tn5250AidKey
_AperTnServAdm5250DefaultPasswordKey_Object = MibScalar
aperTnServAdm5250DefaultPasswordKey = _AperTnServAdm5250DefaultPasswordKey_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 2),
    _AperTnServAdm5250DefaultPasswordKey_Type()
)
aperTnServAdm5250DefaultPasswordKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250DefaultPasswordKey.setStatus("mandatory")
_AperTnServAdm5250NumSessions_Type = Integer32
_AperTnServAdm5250NumSessions_Object = MibScalar
aperTnServAdm5250NumSessions = _AperTnServAdm5250NumSessions_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 3),
    _AperTnServAdm5250NumSessions_Type()
)
aperTnServAdm5250NumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250NumSessions.setStatus("mandatory")
_AperTnServAdm5250SessionTableLastChange_Type = TimeTicks
_AperTnServAdm5250SessionTableLastChange_Object = MibScalar
aperTnServAdm5250SessionTableLastChange = _AperTnServAdm5250SessionTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 4),
    _AperTnServAdm5250SessionTableLastChange_Type()
)
aperTnServAdm5250SessionTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionTableLastChange.setStatus("mandatory")
_AperTnServAdm5250SessionTable_Object = MibTable
aperTnServAdm5250SessionTable = _AperTnServAdm5250SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionTable.setStatus("mandatory")
_AperTnServAdm5250SessionEntry_Object = MibTableRow
aperTnServAdm5250SessionEntry = _AperTnServAdm5250SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1)
)
aperTnServAdm5250SessionEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdm5250SessionGroupOrUserName"),
    (0, "APERTUS-TNSERVER-MIB", "aperTnServAdm5250SessionName"),
)
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionEntry.setStatus("mandatory")
_AperTnServAdm5250SessionGroupOrUserName_Type = DisplayString
_AperTnServAdm5250SessionGroupOrUserName_Object = MibTableColumn
aperTnServAdm5250SessionGroupOrUserName = _AperTnServAdm5250SessionGroupOrUserName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 1),
    _AperTnServAdm5250SessionGroupOrUserName_Type()
)
aperTnServAdm5250SessionGroupOrUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionGroupOrUserName.setStatus("mandatory")
_AperTnServAdm5250SessionName_Type = DisplayString
_AperTnServAdm5250SessionName_Object = MibTableColumn
aperTnServAdm5250SessionName = _AperTnServAdm5250SessionName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 2),
    _AperTnServAdm5250SessionName_Type()
)
aperTnServAdm5250SessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionName.setStatus("mandatory")
_AperTnServAdm5250SessionDescription_Type = DisplayString
_AperTnServAdm5250SessionDescription_Object = MibTableColumn
aperTnServAdm5250SessionDescription = _AperTnServAdm5250SessionDescription_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 3),
    _AperTnServAdm5250SessionDescription_Type()
)
aperTnServAdm5250SessionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionDescription.setStatus("mandatory")


class _AperTnServAdm5250SessionGroupOrUser_Type(Integer32):
    """Custom type aperTnServAdm5250SessionGroupOrUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 1),
          ("user", 2))
    )


_AperTnServAdm5250SessionGroupOrUser_Type.__name__ = "Integer32"
_AperTnServAdm5250SessionGroupOrUser_Object = MibTableColumn
aperTnServAdm5250SessionGroupOrUser = _AperTnServAdm5250SessionGroupOrUser_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 4),
    _AperTnServAdm5250SessionGroupOrUser_Type()
)
aperTnServAdm5250SessionGroupOrUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionGroupOrUser.setStatus("mandatory")


class _AperTnServAdm5250SessionAutoSignon_Type(Integer32):
    """Custom type aperTnServAdm5250SessionAutoSignon based on Integer32"""
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


_AperTnServAdm5250SessionAutoSignon_Type.__name__ = "Integer32"
_AperTnServAdm5250SessionAutoSignon_Object = MibTableColumn
aperTnServAdm5250SessionAutoSignon = _AperTnServAdm5250SessionAutoSignon_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 5),
    _AperTnServAdm5250SessionAutoSignon_Type()
)
aperTnServAdm5250SessionAutoSignon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionAutoSignon.setStatus("mandatory")
_AperTnServAdm5250SessionRemoteUser_Type = DisplayString
_AperTnServAdm5250SessionRemoteUser_Object = MibTableColumn
aperTnServAdm5250SessionRemoteUser = _AperTnServAdm5250SessionRemoteUser_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 6),
    _AperTnServAdm5250SessionRemoteUser_Type()
)
aperTnServAdm5250SessionRemoteUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionRemoteUser.setStatus("mandatory")
_AperTnServAdm5250SessionInitialMenu_Type = DisplayString
_AperTnServAdm5250SessionInitialMenu_Object = MibTableColumn
aperTnServAdm5250SessionInitialMenu = _AperTnServAdm5250SessionInitialMenu_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 7),
    _AperTnServAdm5250SessionInitialMenu_Type()
)
aperTnServAdm5250SessionInitialMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionInitialMenu.setStatus("mandatory")
_AperTnServAdm5250SessionInitialProgram_Type = DisplayString
_AperTnServAdm5250SessionInitialProgram_Object = MibTableColumn
aperTnServAdm5250SessionInitialProgram = _AperTnServAdm5250SessionInitialProgram_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 8),
    _AperTnServAdm5250SessionInitialProgram_Type()
)
aperTnServAdm5250SessionInitialProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionInitialProgram.setStatus("mandatory")
_AperTnServAdm5250SessionInitialLibrary_Type = DisplayString
_AperTnServAdm5250SessionInitialLibrary_Object = MibTableColumn
aperTnServAdm5250SessionInitialLibrary = _AperTnServAdm5250SessionInitialLibrary_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 9),
    _AperTnServAdm5250SessionInitialLibrary_Type()
)
aperTnServAdm5250SessionInitialLibrary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionInitialLibrary.setStatus("mandatory")


class _AperTnServAdm5250SessionAutoDeviceConfiguration_Type(Integer32):
    """Custom type aperTnServAdm5250SessionAutoDeviceConfiguration based on Integer32"""
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


_AperTnServAdm5250SessionAutoDeviceConfiguration_Type.__name__ = "Integer32"
_AperTnServAdm5250SessionAutoDeviceConfiguration_Object = MibTableColumn
aperTnServAdm5250SessionAutoDeviceConfiguration = _AperTnServAdm5250SessionAutoDeviceConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 10),
    _AperTnServAdm5250SessionAutoDeviceConfiguration_Type()
)
aperTnServAdm5250SessionAutoDeviceConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionAutoDeviceConfiguration.setStatus("mandatory")


class _AperTnServAdm5250SessionVirtualDeviceOrController_Type(Integer32):
    """Custom type aperTnServAdm5250SessionVirtualDeviceOrController based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controller", 2),
          ("device", 1))
    )


_AperTnServAdm5250SessionVirtualDeviceOrController_Type.__name__ = "Integer32"
_AperTnServAdm5250SessionVirtualDeviceOrController_Object = MibTableColumn
aperTnServAdm5250SessionVirtualDeviceOrController = _AperTnServAdm5250SessionVirtualDeviceOrController_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 11),
    _AperTnServAdm5250SessionVirtualDeviceOrController_Type()
)
aperTnServAdm5250SessionVirtualDeviceOrController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionVirtualDeviceOrController.setStatus("mandatory")
_AperTnServAdm5250SessionVirtualDeviceOrControllerName_Type = DisplayString
_AperTnServAdm5250SessionVirtualDeviceOrControllerName_Object = MibTableColumn
aperTnServAdm5250SessionVirtualDeviceOrControllerName = _AperTnServAdm5250SessionVirtualDeviceOrControllerName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 12),
    _AperTnServAdm5250SessionVirtualDeviceOrControllerName_Type()
)
aperTnServAdm5250SessionVirtualDeviceOrControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionVirtualDeviceOrControllerName.setStatus("mandatory")
_AperTnServAdm5250SessionDestination_Type = DisplayString
_AperTnServAdm5250SessionDestination_Object = MibTableColumn
aperTnServAdm5250SessionDestination = _AperTnServAdm5250SessionDestination_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 2, 3, 5, 1, 13),
    _AperTnServAdm5250SessionDestination_Type()
)
aperTnServAdm5250SessionDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServAdm5250SessionDestination.setStatus("mandatory")
_AperTnServOper_ObjectIdentity = ObjectIdentity
aperTnServOper = _AperTnServOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3)
)
_AperTnServOperGen_ObjectIdentity = ObjectIdentity
aperTnServOperGen = _AperTnServOperGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 1)
)


class _AperTnServOperStatus_Type(Integer32):
    """Custom type aperTnServOperStatus based on Integer32"""
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
        *(("down", 4),
          ("draining", 3),
          ("loading", 2),
          ("ready", 1))
    )


_AperTnServOperStatus_Type.__name__ = "Integer32"
_AperTnServOperStatus_Object = MibScalar
aperTnServOperStatus = _AperTnServOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 1, 1),
    _AperTnServOperStatus_Type()
)
aperTnServOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperStatus.setStatus("mandatory")
_AperTnServOperActiveSessions_Type = Integer32
_AperTnServOperActiveSessions_Object = MibScalar
aperTnServOperActiveSessions = _AperTnServOperActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 1, 2),
    _AperTnServOperActiveSessions_Type()
)
aperTnServOperActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperActiveSessions.setStatus("mandatory")
_AperTnServOperUpTime_Type = TimeTicks
_AperTnServOperUpTime_Object = MibScalar
aperTnServOperUpTime = _AperTnServOperUpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 1, 3),
    _AperTnServOperUpTime_Type()
)
aperTnServOperUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperUpTime.setStatus("mandatory")
_AperTnServOperConns_ObjectIdentity = ObjectIdentity
aperTnServOperConns = _AperTnServOperConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2)
)
_AperTnServOperConnsNumActive_Type = Integer32
_AperTnServOperConnsNumActive_Object = MibScalar
aperTnServOperConnsNumActive = _AperTnServOperConnsNumActive_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 1),
    _AperTnServOperConnsNumActive_Type()
)
aperTnServOperConnsNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsNumActive.setStatus("mandatory")
_AperTnServOperConnsTableLastChange_Type = TimeTicks
_AperTnServOperConnsTableLastChange_Object = MibScalar
aperTnServOperConnsTableLastChange = _AperTnServOperConnsTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 2),
    _AperTnServOperConnsTableLastChange_Type()
)
aperTnServOperConnsTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsTableLastChange.setStatus("mandatory")
_AperTnServOperConnsTable_Object = MibTable
aperTnServOperConnsTable = _AperTnServOperConnsTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    aperTnServOperConnsTable.setStatus("mandatory")
_AperTnServOperConnsEntry_Object = MibTableRow
aperTnServOperConnsEntry = _AperTnServOperConnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1)
)
aperTnServOperConnsEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServOperConnsClientIP"),
    (0, "APERTUS-TNSERVER-MIB", "aperTnServOperConnsClientPort"),
)
if mibBuilder.loadTexts:
    aperTnServOperConnsEntry.setStatus("mandatory")
_AperTnServOperConnsClientIP_Type = IpAddress
_AperTnServOperConnsClientIP_Object = MibTableColumn
aperTnServOperConnsClientIP = _AperTnServOperConnsClientIP_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 1),
    _AperTnServOperConnsClientIP_Type()
)
aperTnServOperConnsClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsClientIP.setStatus("mandatory")
_AperTnServOperConnsClientPort_Type = Integer32
_AperTnServOperConnsClientPort_Object = MibTableColumn
aperTnServOperConnsClientPort = _AperTnServOperConnsClientPort_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 2),
    _AperTnServOperConnsClientPort_Type()
)
aperTnServOperConnsClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsClientPort.setStatus("mandatory")
_AperTnServOperConnsServerPort_Type = Integer32
_AperTnServOperConnsServerPort_Object = MibTableColumn
aperTnServOperConnsServerPort = _AperTnServOperConnsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 3),
    _AperTnServOperConnsServerPort_Type()
)
aperTnServOperConnsServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsServerPort.setStatus("mandatory")


class _AperTnServOperConnsType_Type(Integer32):
    """Custom type aperTnServOperConnsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tn3270", 1),
          ("tn5250", 2))
    )


_AperTnServOperConnsType_Type.__name__ = "Integer32"
_AperTnServOperConnsType_Object = MibTableColumn
aperTnServOperConnsType = _AperTnServOperConnsType_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 4),
    _AperTnServOperConnsType_Type()
)
aperTnServOperConnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsType.setStatus("mandatory")
_AperTnServOperConnsAppcSessId_Type = Integer32
_AperTnServOperConnsAppcSessId_Object = MibTableColumn
aperTnServOperConnsAppcSessId = _AperTnServOperConnsAppcSessId_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 5),
    _AperTnServOperConnsAppcSessId_Type()
)
aperTnServOperConnsAppcSessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsAppcSessId.setStatus("mandatory")
_AperTnServOperConnsAlsName_Type = DisplayString
_AperTnServOperConnsAlsName_Object = MibTableColumn
aperTnServOperConnsAlsName = _AperTnServOperConnsAlsName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 6),
    _AperTnServOperConnsAlsName_Type()
)
aperTnServOperConnsAlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsAlsName.setStatus("mandatory")


class _AperTnServOperConnsLuNumber_Type(Integer32):
    """Custom type aperTnServOperConnsLuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AperTnServOperConnsLuNumber_Type.__name__ = "Integer32"
_AperTnServOperConnsLuNumber_Object = MibTableColumn
aperTnServOperConnsLuNumber = _AperTnServOperConnsLuNumber_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 7),
    _AperTnServOperConnsLuNumber_Type()
)
aperTnServOperConnsLuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsLuNumber.setStatus("mandatory")


class _AperTnServOperConnsState_Type(Integer32):
    """Custom type aperTnServOperConnsState based on Integer32"""
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
        *(("active", 6),
          ("connecting", 1),
          ("disconnecting", 7),
          ("menu", 3),
          ("negotiating", 2),
          ("other", 8),
          ("reserving", 4),
          ("sessionpending", 5))
    )


_AperTnServOperConnsState_Type.__name__ = "Integer32"
_AperTnServOperConnsState_Object = MibTableColumn
aperTnServOperConnsState = _AperTnServOperConnsState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 8),
    _AperTnServOperConnsState_Type()
)
aperTnServOperConnsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsState.setStatus("mandatory")
_AperTnServOperConnsUpTime_Type = TimeTicks
_AperTnServOperConnsUpTime_Object = MibTableColumn
aperTnServOperConnsUpTime = _AperTnServOperConnsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 9),
    _AperTnServOperConnsUpTime_Type()
)
aperTnServOperConnsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsUpTime.setStatus("mandatory")
_AperTnServOperConnsInactivityLimit_Type = Integer32
_AperTnServOperConnsInactivityLimit_Object = MibTableColumn
aperTnServOperConnsInactivityLimit = _AperTnServOperConnsInactivityLimit_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 10),
    _AperTnServOperConnsInactivityLimit_Type()
)
aperTnServOperConnsInactivityLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsInactivityLimit.setStatus("mandatory")
_AperTnServOperConnsTimeSinceLastEvent_Type = TimeTicks
_AperTnServOperConnsTimeSinceLastEvent_Object = MibTableColumn
aperTnServOperConnsTimeSinceLastEvent = _AperTnServOperConnsTimeSinceLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 11),
    _AperTnServOperConnsTimeSinceLastEvent_Type()
)
aperTnServOperConnsTimeSinceLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsTimeSinceLastEvent.setStatus("mandatory")
_AperTnServOperConnsDeviceName_Type = DisplayString
_AperTnServOperConnsDeviceName_Object = MibTableColumn
aperTnServOperConnsDeviceName = _AperTnServOperConnsDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 12),
    _AperTnServOperConnsDeviceName_Type()
)
aperTnServOperConnsDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsDeviceName.setStatus("mandatory")
_AperTnServOperConnsUserName_Type = DisplayString
_AperTnServOperConnsUserName_Object = MibTableColumn
aperTnServOperConnsUserName = _AperTnServOperConnsUserName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 13),
    _AperTnServOperConnsUserName_Type()
)
aperTnServOperConnsUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsUserName.setStatus("mandatory")
_AperTnServOperConnsSessionName_Type = DisplayString
_AperTnServOperConnsSessionName_Object = MibTableColumn
aperTnServOperConnsSessionName = _AperTnServOperConnsSessionName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 14),
    _AperTnServOperConnsSessionName_Type()
)
aperTnServOperConnsSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsSessionName.setStatus("mandatory")
_AperTnServOperConnsBytesOutbound_Type = Counter32
_AperTnServOperConnsBytesOutbound_Object = MibTableColumn
aperTnServOperConnsBytesOutbound = _AperTnServOperConnsBytesOutbound_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 15),
    _AperTnServOperConnsBytesOutbound_Type()
)
aperTnServOperConnsBytesOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsBytesOutbound.setStatus("mandatory")
_AperTnServOperConnsBytesInbound_Type = Counter32
_AperTnServOperConnsBytesInbound_Object = MibTableColumn
aperTnServOperConnsBytesInbound = _AperTnServOperConnsBytesInbound_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 2, 3, 1, 16),
    _AperTnServOperConnsBytesInbound_Type()
)
aperTnServOperConnsBytesInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOperConnsBytesInbound.setStatus("mandatory")
_AperTnServOper3270_ObjectIdentity = ObjectIdentity
aperTnServOper3270 = _AperTnServOper3270_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3)
)
_AperTnServOper3270NumActive_Type = Integer32
_AperTnServOper3270NumActive_Object = MibScalar
aperTnServOper3270NumActive = _AperTnServOper3270NumActive_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 1),
    _AperTnServOper3270NumActive_Type()
)
aperTnServOper3270NumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270NumActive.setStatus("mandatory")
_AperTnServOper3270Table_Object = MibTable
aperTnServOper3270Table = _AperTnServOper3270Table_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    aperTnServOper3270Table.setStatus("mandatory")
_AperTnServOper3270Entry_Object = MibTableRow
aperTnServOper3270Entry = _AperTnServOper3270Entry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1)
)
aperTnServOper3270Entry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServOper3270AlsName"),
    (0, "APERTUS-TNSERVER-MIB", "aperTnServOper3270LuNumber"),
)
if mibBuilder.loadTexts:
    aperTnServOper3270Entry.setStatus("mandatory")
_AperTnServOper3270AlsName_Type = DisplayString
_AperTnServOper3270AlsName_Object = MibTableColumn
aperTnServOper3270AlsName = _AperTnServOper3270AlsName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 1),
    _AperTnServOper3270AlsName_Type()
)
aperTnServOper3270AlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270AlsName.setStatus("mandatory")


class _AperTnServOper3270LuNumber_Type(Integer32):
    """Custom type aperTnServOper3270LuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AperTnServOper3270LuNumber_Type.__name__ = "Integer32"
_AperTnServOper3270LuNumber_Object = MibTableColumn
aperTnServOper3270LuNumber = _AperTnServOper3270LuNumber_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 2),
    _AperTnServOper3270LuNumber_Type()
)
aperTnServOper3270LuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270LuNumber.setStatus("mandatory")
_AperTnServOper3270ClientIP_Type = IpAddress
_AperTnServOper3270ClientIP_Object = MibTableColumn
aperTnServOper3270ClientIP = _AperTnServOper3270ClientIP_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 3),
    _AperTnServOper3270ClientIP_Type()
)
aperTnServOper3270ClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270ClientIP.setStatus("mandatory")
_AperTnServOper3270ClientPort_Type = Integer32
_AperTnServOper3270ClientPort_Object = MibTableColumn
aperTnServOper3270ClientPort = _AperTnServOper3270ClientPort_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 4),
    _AperTnServOper3270ClientPort_Type()
)
aperTnServOper3270ClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270ClientPort.setStatus("mandatory")


class _AperTnServOper3270LuType_Type(Integer32):
    """Custom type aperTnServOper3270LuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("display", 1),
          ("printer", 2))
    )


_AperTnServOper3270LuType_Type.__name__ = "Integer32"
_AperTnServOper3270LuType_Object = MibTableColumn
aperTnServOper3270LuType = _AperTnServOper3270LuType_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 5),
    _AperTnServOper3270LuType_Type()
)
aperTnServOper3270LuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270LuType.setStatus("mandatory")


class _AperTnServOper3270LuState_Type(Integer32):
    """Custom type aperTnServOper3270LuState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("enabled", 2),
          ("other", 1))
    )


_AperTnServOper3270LuState_Type.__name__ = "Integer32"
_AperTnServOper3270LuState_Object = MibTableColumn
aperTnServOper3270LuState = _AperTnServOper3270LuState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 6),
    _AperTnServOper3270LuState_Type()
)
aperTnServOper3270LuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270LuState.setStatus("mandatory")


class _AperTnServOper3270SscpLuState_Type(Integer32):
    """Custom type aperTnServOper3270SscpLuState based on Integer32"""
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


_AperTnServOper3270SscpLuState_Type.__name__ = "Integer32"
_AperTnServOper3270SscpLuState_Object = MibTableColumn
aperTnServOper3270SscpLuState = _AperTnServOper3270SscpLuState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 7),
    _AperTnServOper3270SscpLuState_Type()
)
aperTnServOper3270SscpLuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270SscpLuState.setStatus("mandatory")


class _AperTnServOper3270LuLuState_Type(Integer32):
    """Custom type aperTnServOper3270LuLuState based on Integer32"""
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


_AperTnServOper3270LuLuState_Type.__name__ = "Integer32"
_AperTnServOper3270LuLuState_Object = MibTableColumn
aperTnServOper3270LuLuState = _AperTnServOper3270LuLuState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 8),
    _AperTnServOper3270LuLuState_Type()
)
aperTnServOper3270LuLuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270LuLuState.setStatus("mandatory")


class _AperTnServOper3270KeyboardLock_Type(Integer32):
    """Custom type aperTnServOper3270KeyboardLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_AperTnServOper3270KeyboardLock_Type.__name__ = "Integer32"
_AperTnServOper3270KeyboardLock_Object = MibTableColumn
aperTnServOper3270KeyboardLock = _AperTnServOper3270KeyboardLock_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 9),
    _AperTnServOper3270KeyboardLock_Type()
)
aperTnServOper3270KeyboardLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270KeyboardLock.setStatus("mandatory")
_AperTnServOper3270NetworkQualifiedSluName_Type = DisplayString
_AperTnServOper3270NetworkQualifiedSluName_Object = MibTableColumn
aperTnServOper3270NetworkQualifiedSluName = _AperTnServOper3270NetworkQualifiedSluName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 10),
    _AperTnServOper3270NetworkQualifiedSluName_Type()
)
aperTnServOper3270NetworkQualifiedSluName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270NetworkQualifiedSluName.setStatus("mandatory")


class _AperTnServOper3270ModelNumber_Type(Integer32):
    """Custom type aperTnServOper3270ModelNumber based on Integer32"""
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
        *(("model2", 1),
          ("model3", 2),
          ("model4", 3),
          ("model5", 4))
    )


_AperTnServOper3270ModelNumber_Type.__name__ = "Integer32"
_AperTnServOper3270ModelNumber_Object = MibTableColumn
aperTnServOper3270ModelNumber = _AperTnServOper3270ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 11),
    _AperTnServOper3270ModelNumber_Type()
)
aperTnServOper3270ModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270ModelNumber.setStatus("mandatory")
_AperTnServOper3270AssociatedPrinter_Type = DisplayString
_AperTnServOper3270AssociatedPrinter_Object = MibTableColumn
aperTnServOper3270AssociatedPrinter = _AperTnServOper3270AssociatedPrinter_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 3, 2, 1, 12),
    _AperTnServOper3270AssociatedPrinter_Type()
)
aperTnServOper3270AssociatedPrinter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper3270AssociatedPrinter.setStatus("mandatory")
_AperTnServOper5250_ObjectIdentity = ObjectIdentity
aperTnServOper5250 = _AperTnServOper5250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4)
)
_AperTnServOper5250NumActive_Type = Integer32
_AperTnServOper5250NumActive_Object = MibScalar
aperTnServOper5250NumActive = _AperTnServOper5250NumActive_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 1),
    _AperTnServOper5250NumActive_Type()
)
aperTnServOper5250NumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250NumActive.setStatus("mandatory")
_AperTnServOper5250TableLastChange_Type = TimeTicks
_AperTnServOper5250TableLastChange_Object = MibScalar
aperTnServOper5250TableLastChange = _AperTnServOper5250TableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 2),
    _AperTnServOper5250TableLastChange_Type()
)
aperTnServOper5250TableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250TableLastChange.setStatus("mandatory")
_AperTnServOper5250Table_Object = MibTable
aperTnServOper5250Table = _AperTnServOper5250Table_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    aperTnServOper5250Table.setStatus("mandatory")
_AperTnServOper5250Entry_Object = MibTableRow
aperTnServOper5250Entry = _AperTnServOper5250Entry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3, 1)
)
aperTnServOper5250Entry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServOper5250AppcSessId"),
)
if mibBuilder.loadTexts:
    aperTnServOper5250Entry.setStatus("mandatory")
_AperTnServOper5250AppcSessId_Type = Integer32
_AperTnServOper5250AppcSessId_Object = MibTableColumn
aperTnServOper5250AppcSessId = _AperTnServOper5250AppcSessId_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3, 1, 1),
    _AperTnServOper5250AppcSessId_Type()
)
aperTnServOper5250AppcSessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250AppcSessId.setStatus("mandatory")
_AperTnServOper5250ClientIP_Type = IpAddress
_AperTnServOper5250ClientIP_Object = MibTableColumn
aperTnServOper5250ClientIP = _AperTnServOper5250ClientIP_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3, 1, 2),
    _AperTnServOper5250ClientIP_Type()
)
aperTnServOper5250ClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250ClientIP.setStatus("mandatory")
_AperTnServOper5250ClientPort_Type = Integer32
_AperTnServOper5250ClientPort_Object = MibTableColumn
aperTnServOper5250ClientPort = _AperTnServOper5250ClientPort_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3, 1, 3),
    _AperTnServOper5250ClientPort_Type()
)
aperTnServOper5250ClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250ClientPort.setStatus("mandatory")
_AperTnServOper5250AlsName_Type = DisplayString
_AperTnServOper5250AlsName_Object = MibTableColumn
aperTnServOper5250AlsName = _AperTnServOper5250AlsName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3, 1, 4),
    _AperTnServOper5250AlsName_Type()
)
aperTnServOper5250AlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250AlsName.setStatus("mandatory")
_AperTnServOper5250SymbolicDestination_Type = DisplayString
_AperTnServOper5250SymbolicDestination_Object = MibTableColumn
aperTnServOper5250SymbolicDestination = _AperTnServOper5250SymbolicDestination_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3, 1, 5),
    _AperTnServOper5250SymbolicDestination_Type()
)
aperTnServOper5250SymbolicDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250SymbolicDestination.setStatus("mandatory")
_AperTnServOper5250LocalLuName_Type = DisplayString
_AperTnServOper5250LocalLuName_Object = MibTableColumn
aperTnServOper5250LocalLuName = _AperTnServOper5250LocalLuName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3, 1, 6),
    _AperTnServOper5250LocalLuName_Type()
)
aperTnServOper5250LocalLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250LocalLuName.setStatus("mandatory")
_AperTnServOper5250RemoteLuName_Type = DisplayString
_AperTnServOper5250RemoteLuName_Object = MibTableColumn
aperTnServOper5250RemoteLuName = _AperTnServOper5250RemoteLuName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3, 1, 7),
    _AperTnServOper5250RemoteLuName_Type()
)
aperTnServOper5250RemoteLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250RemoteLuName.setStatus("mandatory")
_AperTnServOper5250ModeName_Type = DisplayString
_AperTnServOper5250ModeName_Object = MibTableColumn
aperTnServOper5250ModeName = _AperTnServOper5250ModeName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3, 1, 8),
    _AperTnServOper5250ModeName_Type()
)
aperTnServOper5250ModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250ModeName.setStatus("mandatory")


class _AperTnServOper5250KeyboardLock_Type(Integer32):
    """Custom type aperTnServOper5250KeyboardLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_AperTnServOper5250KeyboardLock_Type.__name__ = "Integer32"
_AperTnServOper5250KeyboardLock_Object = MibTableColumn
aperTnServOper5250KeyboardLock = _AperTnServOper5250KeyboardLock_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 3, 4, 3, 1, 9),
    _AperTnServOper5250KeyboardLock_Type()
)
aperTnServOper5250KeyboardLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServOper5250KeyboardLock.setStatus("mandatory")
_AperTnServStats_ObjectIdentity = ObjectIdentity
aperTnServStats = _AperTnServStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4)
)
_AperTnServRtm_ObjectIdentity = ObjectIdentity
aperTnServRtm = _AperTnServRtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1)
)


class _AperTnServRtmSupport_Type(Integer32):
    """Custom type aperTnServRtmSupport based on Integer32"""
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


_AperTnServRtmSupport_Type.__name__ = "Integer32"
_AperTnServRtmSupport_Object = MibScalar
aperTnServRtmSupport = _AperTnServRtmSupport_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 1),
    _AperTnServRtmSupport_Type()
)
aperTnServRtmSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmSupport.setStatus("mandatory")


class _AperTnServRtmDefaultState_Type(Integer32):
    """Custom type aperTnServRtmDefaultState based on Integer32"""
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


_AperTnServRtmDefaultState_Type.__name__ = "Integer32"
_AperTnServRtmDefaultState_Object = MibScalar
aperTnServRtmDefaultState = _AperTnServRtmDefaultState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 2),
    _AperTnServRtmDefaultState_Type()
)
aperTnServRtmDefaultState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultState.setStatus("mandatory")


class _AperTnServRtmDefaultControl_Type(Integer32):
    """Custom type aperTnServRtmDefaultControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("local", 2))
    )


_AperTnServRtmDefaultControl_Type.__name__ = "Integer32"
_AperTnServRtmDefaultControl_Object = MibScalar
aperTnServRtmDefaultControl = _AperTnServRtmDefaultControl_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 3),
    _AperTnServRtmDefaultControl_Type()
)
aperTnServRtmDefaultControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultControl.setStatus("mandatory")


class _AperTnServRtmDefaultLocalDisplay_Type(Integer32):
    """Custom type aperTnServRtmDefaultLocalDisplay based on Integer32"""
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


_AperTnServRtmDefaultLocalDisplay_Type.__name__ = "Integer32"
_AperTnServRtmDefaultLocalDisplay_Object = MibScalar
aperTnServRtmDefaultLocalDisplay = _AperTnServRtmDefaultLocalDisplay_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 4),
    _AperTnServRtmDefaultLocalDisplay_Type()
)
aperTnServRtmDefaultLocalDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultLocalDisplay.setStatus("mandatory")


class _AperTnServRtmDefaultDef_Type(Integer32):
    """Custom type aperTnServRtmDefaultDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cdeb", 3),
          ("firstChar", 1),
          ("kb", 2))
    )


_AperTnServRtmDefaultDef_Type.__name__ = "Integer32"
_AperTnServRtmDefaultDef_Object = MibScalar
aperTnServRtmDefaultDef = _AperTnServRtmDefaultDef_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 5),
    _AperTnServRtmDefaultDef_Type()
)
aperTnServRtmDefaultDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultDef.setStatus("mandatory")


class _AperTnServRtmDefaultMeasureTcpIpTime_Type(Integer32):
    """Custom type aperTnServRtmDefaultMeasureTcpIpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServRtmDefaultMeasureTcpIpTime_Type.__name__ = "Integer32"
_AperTnServRtmDefaultMeasureTcpIpTime_Object = MibScalar
aperTnServRtmDefaultMeasureTcpIpTime = _AperTnServRtmDefaultMeasureTcpIpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 6),
    _AperTnServRtmDefaultMeasureTcpIpTime_Type()
)
aperTnServRtmDefaultMeasureTcpIpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultMeasureTcpIpTime.setStatus("mandatory")


class _AperTnServRtmDefaultMeasureSnaTime_Type(Integer32):
    """Custom type aperTnServRtmDefaultMeasureSnaTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServRtmDefaultMeasureSnaTime_Type.__name__ = "Integer32"
_AperTnServRtmDefaultMeasureSnaTime_Object = MibScalar
aperTnServRtmDefaultMeasureSnaTime = _AperTnServRtmDefaultMeasureSnaTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 7),
    _AperTnServRtmDefaultMeasureSnaTime_Type()
)
aperTnServRtmDefaultMeasureSnaTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultMeasureSnaTime.setStatus("mandatory")
_AperTnServRtmDefaultSamplingFactor_Type = Integer32
_AperTnServRtmDefaultSamplingFactor_Object = MibScalar
aperTnServRtmDefaultSamplingFactor = _AperTnServRtmDefaultSamplingFactor_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 8),
    _AperTnServRtmDefaultSamplingFactor_Type()
)
aperTnServRtmDefaultSamplingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultSamplingFactor.setStatus("mandatory")
_AperTnServRtmDefaultNumberOfBoundaries_Type = Integer32
_AperTnServRtmDefaultNumberOfBoundaries_Object = MibScalar
aperTnServRtmDefaultNumberOfBoundaries = _AperTnServRtmDefaultNumberOfBoundaries_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 9),
    _AperTnServRtmDefaultNumberOfBoundaries_Type()
)
aperTnServRtmDefaultNumberOfBoundaries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultNumberOfBoundaries.setStatus("mandatory")
_AperTnServRtmDefaultBoundary1_Type = Integer32
_AperTnServRtmDefaultBoundary1_Object = MibScalar
aperTnServRtmDefaultBoundary1 = _AperTnServRtmDefaultBoundary1_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 10),
    _AperTnServRtmDefaultBoundary1_Type()
)
aperTnServRtmDefaultBoundary1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultBoundary1.setStatus("mandatory")
_AperTnServRtmDefaultBoundary2_Type = Integer32
_AperTnServRtmDefaultBoundary2_Object = MibScalar
aperTnServRtmDefaultBoundary2 = _AperTnServRtmDefaultBoundary2_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 11),
    _AperTnServRtmDefaultBoundary2_Type()
)
aperTnServRtmDefaultBoundary2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultBoundary2.setStatus("mandatory")
_AperTnServRtmDefaultBoundary3_Type = Integer32
_AperTnServRtmDefaultBoundary3_Object = MibScalar
aperTnServRtmDefaultBoundary3 = _AperTnServRtmDefaultBoundary3_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 12),
    _AperTnServRtmDefaultBoundary3_Type()
)
aperTnServRtmDefaultBoundary3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultBoundary3.setStatus("mandatory")
_AperTnServRtmDefaultBoundary4_Type = Integer32
_AperTnServRtmDefaultBoundary4_Object = MibScalar
aperTnServRtmDefaultBoundary4 = _AperTnServRtmDefaultBoundary4_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 13),
    _AperTnServRtmDefaultBoundary4_Type()
)
aperTnServRtmDefaultBoundary4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultBoundary4.setStatus("mandatory")
_AperTnServRtmDefaultThresholdTrigger_Type = Integer32
_AperTnServRtmDefaultThresholdTrigger_Object = MibScalar
aperTnServRtmDefaultThresholdTrigger = _AperTnServRtmDefaultThresholdTrigger_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 14),
    _AperTnServRtmDefaultThresholdTrigger_Type()
)
aperTnServRtmDefaultThresholdTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultThresholdTrigger.setStatus("mandatory")


class _AperTnServRtmDefaultThresholdTriggerState_Type(Integer32):
    """Custom type aperTnServRtmDefaultThresholdTriggerState based on Integer32"""
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


_AperTnServRtmDefaultThresholdTriggerState_Type.__name__ = "Integer32"
_AperTnServRtmDefaultThresholdTriggerState_Object = MibScalar
aperTnServRtmDefaultThresholdTriggerState = _AperTnServRtmDefaultThresholdTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 15),
    _AperTnServRtmDefaultThresholdTriggerState_Type()
)
aperTnServRtmDefaultThresholdTriggerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultThresholdTriggerState.setStatus("mandatory")


class _AperTnServRtmDefaultCounterOverflowTriggerState_Type(Integer32):
    """Custom type aperTnServRtmDefaultCounterOverflowTriggerState based on Integer32"""
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


_AperTnServRtmDefaultCounterOverflowTriggerState_Type.__name__ = "Integer32"
_AperTnServRtmDefaultCounterOverflowTriggerState_Object = MibScalar
aperTnServRtmDefaultCounterOverflowTriggerState = _AperTnServRtmDefaultCounterOverflowTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 16),
    _AperTnServRtmDefaultCounterOverflowTriggerState_Type()
)
aperTnServRtmDefaultCounterOverflowTriggerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultCounterOverflowTriggerState.setStatus("mandatory")


class _AperTnServRtmDefaultCounterOverflowHostAlert_Type(Integer32):
    """Custom type aperTnServRtmDefaultCounterOverflowHostAlert based on Integer32"""
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


_AperTnServRtmDefaultCounterOverflowHostAlert_Type.__name__ = "Integer32"
_AperTnServRtmDefaultCounterOverflowHostAlert_Object = MibScalar
aperTnServRtmDefaultCounterOverflowHostAlert = _AperTnServRtmDefaultCounterOverflowHostAlert_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 17),
    _AperTnServRtmDefaultCounterOverflowHostAlert_Type()
)
aperTnServRtmDefaultCounterOverflowHostAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultCounterOverflowHostAlert.setStatus("mandatory")


class _AperTnServRtmDefaultUnbindTriggerState_Type(Integer32):
    """Custom type aperTnServRtmDefaultUnbindTriggerState based on Integer32"""
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


_AperTnServRtmDefaultUnbindTriggerState_Type.__name__ = "Integer32"
_AperTnServRtmDefaultUnbindTriggerState_Object = MibScalar
aperTnServRtmDefaultUnbindTriggerState = _AperTnServRtmDefaultUnbindTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 18),
    _AperTnServRtmDefaultUnbindTriggerState_Type()
)
aperTnServRtmDefaultUnbindTriggerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultUnbindTriggerState.setStatus("mandatory")


class _AperTnServRtmDefaultUnbindHostAlert_Type(Integer32):
    """Custom type aperTnServRtmDefaultUnbindHostAlert based on Integer32"""
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


_AperTnServRtmDefaultUnbindHostAlert_Type.__name__ = "Integer32"
_AperTnServRtmDefaultUnbindHostAlert_Object = MibScalar
aperTnServRtmDefaultUnbindHostAlert = _AperTnServRtmDefaultUnbindHostAlert_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 19),
    _AperTnServRtmDefaultUnbindHostAlert_Type()
)
aperTnServRtmDefaultUnbindHostAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDefaultUnbindHostAlert.setStatus("mandatory")
_AperTnServRtmNumActive_Type = Integer32
_AperTnServRtmNumActive_Object = MibScalar
aperTnServRtmNumActive = _AperTnServRtmNumActive_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 20),
    _AperTnServRtmNumActive_Type()
)
aperTnServRtmNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmNumActive.setStatus("mandatory")
_AperTnServRtmTable_Object = MibTable
aperTnServRtmTable = _AperTnServRtmTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21)
)
if mibBuilder.loadTexts:
    aperTnServRtmTable.setStatus("mandatory")
_AperTnServRtmEntry_Object = MibTableRow
aperTnServRtmEntry = _AperTnServRtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1)
)
aperTnServRtmEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServRtmAlsName"),
    (0, "APERTUS-TNSERVER-MIB", "aperTnServRtmLuNumber"),
)
if mibBuilder.loadTexts:
    aperTnServRtmEntry.setStatus("mandatory")
_AperTnServRtmAlsName_Type = DisplayString
_AperTnServRtmAlsName_Object = MibTableColumn
aperTnServRtmAlsName = _AperTnServRtmAlsName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 1),
    _AperTnServRtmAlsName_Type()
)
aperTnServRtmAlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmAlsName.setStatus("mandatory")


class _AperTnServRtmLuNumber_Type(Integer32):
    """Custom type aperTnServRtmLuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AperTnServRtmLuNumber_Type.__name__ = "Integer32"
_AperTnServRtmLuNumber_Object = MibTableColumn
aperTnServRtmLuNumber = _AperTnServRtmLuNumber_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 2),
    _AperTnServRtmLuNumber_Type()
)
aperTnServRtmLuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmLuNumber.setStatus("mandatory")
_AperTnServRtmClientIP_Type = IpAddress
_AperTnServRtmClientIP_Object = MibTableColumn
aperTnServRtmClientIP = _AperTnServRtmClientIP_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 3),
    _AperTnServRtmClientIP_Type()
)
aperTnServRtmClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmClientIP.setStatus("mandatory")
_AperTnServRtmClientPort_Type = Integer32
_AperTnServRtmClientPort_Object = MibTableColumn
aperTnServRtmClientPort = _AperTnServRtmClientPort_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 4),
    _AperTnServRtmClientPort_Type()
)
aperTnServRtmClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmClientPort.setStatus("mandatory")


class _AperTnServRtmState_Type(Integer32):
    """Custom type aperTnServRtmState based on Integer32"""
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


_AperTnServRtmState_Type.__name__ = "Integer32"
_AperTnServRtmState_Object = MibTableColumn
aperTnServRtmState = _AperTnServRtmState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 5),
    _AperTnServRtmState_Type()
)
aperTnServRtmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmState.setStatus("mandatory")


class _AperTnServRtmLocalDisplay_Type(Integer32):
    """Custom type aperTnServRtmLocalDisplay based on Integer32"""
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


_AperTnServRtmLocalDisplay_Type.__name__ = "Integer32"
_AperTnServRtmLocalDisplay_Object = MibTableColumn
aperTnServRtmLocalDisplay = _AperTnServRtmLocalDisplay_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 6),
    _AperTnServRtmLocalDisplay_Type()
)
aperTnServRtmLocalDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmLocalDisplay.setStatus("mandatory")
_AperTnServRtmUpTime_Type = TimeTicks
_AperTnServRtmUpTime_Object = MibTableColumn
aperTnServRtmUpTime = _AperTnServRtmUpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 7),
    _AperTnServRtmUpTime_Type()
)
aperTnServRtmUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmUpTime.setStatus("mandatory")


class _AperTnServRtmDef_Type(Integer32):
    """Custom type aperTnServRtmDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cdeb", 3),
          ("firstChar", 1),
          ("kb", 2))
    )


_AperTnServRtmDef_Type.__name__ = "Integer32"
_AperTnServRtmDef_Object = MibTableColumn
aperTnServRtmDef = _AperTnServRtmDef_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 8),
    _AperTnServRtmDef_Type()
)
aperTnServRtmDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmDef.setStatus("mandatory")


class _AperTnServRtmMeasureTcpIpTime_Type(Integer32):
    """Custom type aperTnServRtmMeasureTcpIpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServRtmMeasureTcpIpTime_Type.__name__ = "Integer32"
_AperTnServRtmMeasureTcpIpTime_Object = MibTableColumn
aperTnServRtmMeasureTcpIpTime = _AperTnServRtmMeasureTcpIpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 9),
    _AperTnServRtmMeasureTcpIpTime_Type()
)
aperTnServRtmMeasureTcpIpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmMeasureTcpIpTime.setStatus("mandatory")


class _AperTnServRtmMeasureSnaTime_Type(Integer32):
    """Custom type aperTnServRtmMeasureSnaTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServRtmMeasureSnaTime_Type.__name__ = "Integer32"
_AperTnServRtmMeasureSnaTime_Object = MibTableColumn
aperTnServRtmMeasureSnaTime = _AperTnServRtmMeasureSnaTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 10),
    _AperTnServRtmMeasureSnaTime_Type()
)
aperTnServRtmMeasureSnaTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmMeasureSnaTime.setStatus("mandatory")
_AperTnServRtmSamplingFactor_Type = Integer32
_AperTnServRtmSamplingFactor_Object = MibTableColumn
aperTnServRtmSamplingFactor = _AperTnServRtmSamplingFactor_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 11),
    _AperTnServRtmSamplingFactor_Type()
)
aperTnServRtmSamplingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmSamplingFactor.setStatus("mandatory")
_AperTnServRtmNumberOfBoundaries_Type = Integer32
_AperTnServRtmNumberOfBoundaries_Object = MibTableColumn
aperTnServRtmNumberOfBoundaries = _AperTnServRtmNumberOfBoundaries_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 12),
    _AperTnServRtmNumberOfBoundaries_Type()
)
aperTnServRtmNumberOfBoundaries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmNumberOfBoundaries.setStatus("mandatory")
_AperTnServRtmBoundary1_Type = Integer32
_AperTnServRtmBoundary1_Object = MibTableColumn
aperTnServRtmBoundary1 = _AperTnServRtmBoundary1_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 13),
    _AperTnServRtmBoundary1_Type()
)
aperTnServRtmBoundary1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmBoundary1.setStatus("mandatory")
_AperTnServRtmBoundary2_Type = Integer32
_AperTnServRtmBoundary2_Object = MibTableColumn
aperTnServRtmBoundary2 = _AperTnServRtmBoundary2_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 14),
    _AperTnServRtmBoundary2_Type()
)
aperTnServRtmBoundary2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmBoundary2.setStatus("mandatory")
_AperTnServRtmBoundary3_Type = Integer32
_AperTnServRtmBoundary3_Object = MibTableColumn
aperTnServRtmBoundary3 = _AperTnServRtmBoundary3_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 15),
    _AperTnServRtmBoundary3_Type()
)
aperTnServRtmBoundary3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmBoundary3.setStatus("mandatory")
_AperTnServRtmBoundary4_Type = Integer32
_AperTnServRtmBoundary4_Object = MibTableColumn
aperTnServRtmBoundary4 = _AperTnServRtmBoundary4_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 16),
    _AperTnServRtmBoundary4_Type()
)
aperTnServRtmBoundary4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmBoundary4.setStatus("mandatory")
_AperTnServRtmCounter1_Type = Counter32
_AperTnServRtmCounter1_Object = MibTableColumn
aperTnServRtmCounter1 = _AperTnServRtmCounter1_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 17),
    _AperTnServRtmCounter1_Type()
)
aperTnServRtmCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmCounter1.setStatus("mandatory")
_AperTnServRtmCounter2_Type = Counter32
_AperTnServRtmCounter2_Object = MibTableColumn
aperTnServRtmCounter2 = _AperTnServRtmCounter2_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 18),
    _AperTnServRtmCounter2_Type()
)
aperTnServRtmCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmCounter2.setStatus("mandatory")
_AperTnServRtmCounter3_Type = Counter32
_AperTnServRtmCounter3_Object = MibTableColumn
aperTnServRtmCounter3 = _AperTnServRtmCounter3_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 19),
    _AperTnServRtmCounter3_Type()
)
aperTnServRtmCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmCounter3.setStatus("mandatory")
_AperTnServRtmCounter4_Type = Counter32
_AperTnServRtmCounter4_Object = MibTableColumn
aperTnServRtmCounter4 = _AperTnServRtmCounter4_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 20),
    _AperTnServRtmCounter4_Type()
)
aperTnServRtmCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmCounter4.setStatus("mandatory")
_AperTnServRtmOverFlows_Type = Counter32
_AperTnServRtmOverFlows_Object = MibTableColumn
aperTnServRtmOverFlows = _AperTnServRtmOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 21),
    _AperTnServRtmOverFlows_Type()
)
aperTnServRtmOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmOverFlows.setStatus("mandatory")
_AperTnServRtmThresholdTrigger_Type = Integer32
_AperTnServRtmThresholdTrigger_Object = MibTableColumn
aperTnServRtmThresholdTrigger = _AperTnServRtmThresholdTrigger_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 22),
    _AperTnServRtmThresholdTrigger_Type()
)
aperTnServRtmThresholdTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmThresholdTrigger.setStatus("mandatory")


class _AperTnServRtmThresholdTriggerState_Type(Integer32):
    """Custom type aperTnServRtmThresholdTriggerState based on Integer32"""
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


_AperTnServRtmThresholdTriggerState_Type.__name__ = "Integer32"
_AperTnServRtmThresholdTriggerState_Object = MibTableColumn
aperTnServRtmThresholdTriggerState = _AperTnServRtmThresholdTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 23),
    _AperTnServRtmThresholdTriggerState_Type()
)
aperTnServRtmThresholdTriggerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmThresholdTriggerState.setStatus("mandatory")


class _AperTnServRtmCounterOverflowed_Type(Integer32):
    """Custom type aperTnServRtmCounterOverflowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServRtmCounterOverflowed_Type.__name__ = "Integer32"
_AperTnServRtmCounterOverflowed_Object = MibTableColumn
aperTnServRtmCounterOverflowed = _AperTnServRtmCounterOverflowed_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 24),
    _AperTnServRtmCounterOverflowed_Type()
)
aperTnServRtmCounterOverflowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmCounterOverflowed.setStatus("mandatory")


class _AperTnServRtmCounterOverflowTriggerState_Type(Integer32):
    """Custom type aperTnServRtmCounterOverflowTriggerState based on Integer32"""
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


_AperTnServRtmCounterOverflowTriggerState_Type.__name__ = "Integer32"
_AperTnServRtmCounterOverflowTriggerState_Object = MibTableColumn
aperTnServRtmCounterOverflowTriggerState = _AperTnServRtmCounterOverflowTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 25),
    _AperTnServRtmCounterOverflowTriggerState_Type()
)
aperTnServRtmCounterOverflowTriggerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmCounterOverflowTriggerState.setStatus("mandatory")


class _AperTnServRtmCounterOverflowHostAlert_Type(Integer32):
    """Custom type aperTnServRtmCounterOverflowHostAlert based on Integer32"""
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


_AperTnServRtmCounterOverflowHostAlert_Type.__name__ = "Integer32"
_AperTnServRtmCounterOverflowHostAlert_Object = MibTableColumn
aperTnServRtmCounterOverflowHostAlert = _AperTnServRtmCounterOverflowHostAlert_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 26),
    _AperTnServRtmCounterOverflowHostAlert_Type()
)
aperTnServRtmCounterOverflowHostAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmCounterOverflowHostAlert.setStatus("mandatory")


class _AperTnServRtmUnbindTriggerState_Type(Integer32):
    """Custom type aperTnServRtmUnbindTriggerState based on Integer32"""
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


_AperTnServRtmUnbindTriggerState_Type.__name__ = "Integer32"
_AperTnServRtmUnbindTriggerState_Object = MibTableColumn
aperTnServRtmUnbindTriggerState = _AperTnServRtmUnbindTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 27),
    _AperTnServRtmUnbindTriggerState_Type()
)
aperTnServRtmUnbindTriggerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmUnbindTriggerState.setStatus("mandatory")


class _AperTnServRtmUnbindHostAlert_Type(Integer32):
    """Custom type aperTnServRtmUnbindHostAlert based on Integer32"""
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


_AperTnServRtmUnbindHostAlert_Type.__name__ = "Integer32"
_AperTnServRtmUnbindHostAlert_Object = MibTableColumn
aperTnServRtmUnbindHostAlert = _AperTnServRtmUnbindHostAlert_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 28),
    _AperTnServRtmUnbindHostAlert_Type()
)
aperTnServRtmUnbindHostAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmUnbindHostAlert.setStatus("mandatory")
_AperTnServRtmNumTrans_Type = Integer32
_AperTnServRtmNumTrans_Object = MibTableColumn
aperTnServRtmNumTrans = _AperTnServRtmNumTrans_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 29),
    _AperTnServRtmNumTrans_Type()
)
aperTnServRtmNumTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmNumTrans.setStatus("mandatory")
_AperTnServRtmTotalRspTime_Type = Integer32
_AperTnServRtmTotalRspTime_Object = MibTableColumn
aperTnServRtmTotalRspTime = _AperTnServRtmTotalRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 30),
    _AperTnServRtmTotalRspTime_Type()
)
aperTnServRtmTotalRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmTotalRspTime.setStatus("mandatory")
_AperTnServRtmLastRspTime_Type = Integer32
_AperTnServRtmLastRspTime_Object = MibTableColumn
aperTnServRtmLastRspTime = _AperTnServRtmLastRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 31),
    _AperTnServRtmLastRspTime_Type()
)
aperTnServRtmLastRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmLastRspTime.setStatus("mandatory")
_AperTnServRtmAvgRspTime_Type = Integer32
_AperTnServRtmAvgRspTime_Object = MibTableColumn
aperTnServRtmAvgRspTime = _AperTnServRtmAvgRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 32),
    _AperTnServRtmAvgRspTime_Type()
)
aperTnServRtmAvgRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmAvgRspTime.setStatus("mandatory")
_AperTnServRtmMinRspTime_Type = Integer32
_AperTnServRtmMinRspTime_Object = MibTableColumn
aperTnServRtmMinRspTime = _AperTnServRtmMinRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 33),
    _AperTnServRtmMinRspTime_Type()
)
aperTnServRtmMinRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmMinRspTime.setStatus("mandatory")
_AperTnServRtmMaxRspTime_Type = Integer32
_AperTnServRtmMaxRspTime_Object = MibTableColumn
aperTnServRtmMaxRspTime = _AperTnServRtmMaxRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 34),
    _AperTnServRtmMaxRspTime_Type()
)
aperTnServRtmMaxRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmMaxRspTime.setStatus("mandatory")
_AperTnServRtmTotalSnaRspTime_Type = Integer32
_AperTnServRtmTotalSnaRspTime_Object = MibTableColumn
aperTnServRtmTotalSnaRspTime = _AperTnServRtmTotalSnaRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 35),
    _AperTnServRtmTotalSnaRspTime_Type()
)
aperTnServRtmTotalSnaRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmTotalSnaRspTime.setStatus("mandatory")
_AperTnServRtmAvgSnaRspTime_Type = Integer32
_AperTnServRtmAvgSnaRspTime_Object = MibTableColumn
aperTnServRtmAvgSnaRspTime = _AperTnServRtmAvgSnaRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 36),
    _AperTnServRtmAvgSnaRspTime_Type()
)
aperTnServRtmAvgSnaRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmAvgSnaRspTime.setStatus("mandatory")
_AperTnServRtmNumTcpIpSamples_Type = Integer32
_AperTnServRtmNumTcpIpSamples_Object = MibTableColumn
aperTnServRtmNumTcpIpSamples = _AperTnServRtmNumTcpIpSamples_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 37),
    _AperTnServRtmNumTcpIpSamples_Type()
)
aperTnServRtmNumTcpIpSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmNumTcpIpSamples.setStatus("mandatory")
_AperTnServRtmTotalTcpIpRspTime_Type = Integer32
_AperTnServRtmTotalTcpIpRspTime_Object = MibTableColumn
aperTnServRtmTotalTcpIpRspTime = _AperTnServRtmTotalTcpIpRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 38),
    _AperTnServRtmTotalTcpIpRspTime_Type()
)
aperTnServRtmTotalTcpIpRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmTotalTcpIpRspTime.setStatus("mandatory")
_AperTnServRtmAvgTcpIpRspTime_Type = Integer32
_AperTnServRtmAvgTcpIpRspTime_Object = MibTableColumn
aperTnServRtmAvgTcpIpRspTime = _AperTnServRtmAvgTcpIpRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 39),
    _AperTnServRtmAvgTcpIpRspTime_Type()
)
aperTnServRtmAvgTcpIpRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmAvgTcpIpRspTime.setStatus("mandatory")
_AperTnServRtmLastThinkTime_Type = Integer32
_AperTnServRtmLastThinkTime_Object = MibTableColumn
aperTnServRtmLastThinkTime = _AperTnServRtmLastThinkTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 40),
    _AperTnServRtmLastThinkTime_Type()
)
aperTnServRtmLastThinkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmLastThinkTime.setStatus("mandatory")
_AperTnServRtmAvgThinkTime_Type = Integer32
_AperTnServRtmAvgThinkTime_Object = MibTableColumn
aperTnServRtmAvgThinkTime = _AperTnServRtmAvgThinkTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 21, 1, 41),
    _AperTnServRtmAvgThinkTime_Type()
)
aperTnServRtmAvgThinkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmAvgThinkTime.setStatus("mandatory")
_AperTnServRtmMaxHist_Type = Integer32
_AperTnServRtmMaxHist_Object = MibScalar
aperTnServRtmMaxHist = _AperTnServRtmMaxHist_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 22),
    _AperTnServRtmMaxHist_Type()
)
aperTnServRtmMaxHist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aperTnServRtmMaxHist.setStatus("mandatory")
_AperTnServRtmNumHist_Type = Integer32
_AperTnServRtmNumHist_Object = MibScalar
aperTnServRtmNumHist = _AperTnServRtmNumHist_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 23),
    _AperTnServRtmNumHist_Type()
)
aperTnServRtmNumHist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmNumHist.setStatus("mandatory")
_AperTnServRtmLastHist_Type = TimeTicks
_AperTnServRtmLastHist_Object = MibScalar
aperTnServRtmLastHist = _AperTnServRtmLastHist_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 24),
    _AperTnServRtmLastHist_Type()
)
aperTnServRtmLastHist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmLastHist.setStatus("mandatory")
_AperTnServRtmHistTable_Object = MibTable
aperTnServRtmHistTable = _AperTnServRtmHistTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25)
)
if mibBuilder.loadTexts:
    aperTnServRtmHistTable.setStatus("mandatory")
_AperTnServRtmHistEntry_Object = MibTableRow
aperTnServRtmHistEntry = _AperTnServRtmHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1)
)
aperTnServRtmHistEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServRtmHistIndex"),
)
if mibBuilder.loadTexts:
    aperTnServRtmHistEntry.setStatus("mandatory")
_AperTnServRtmHistIndex_Type = Integer32
_AperTnServRtmHistIndex_Object = MibTableColumn
aperTnServRtmHistIndex = _AperTnServRtmHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 1),
    _AperTnServRtmHistIndex_Type()
)
aperTnServRtmHistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistIndex.setStatus("mandatory")
_AperTnServRtmHistWhenDisconnected_Type = TimeTicks
_AperTnServRtmHistWhenDisconnected_Object = MibTableColumn
aperTnServRtmHistWhenDisconnected = _AperTnServRtmHistWhenDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 2),
    _AperTnServRtmHistWhenDisconnected_Type()
)
aperTnServRtmHistWhenDisconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistWhenDisconnected.setStatus("mandatory")
_AperTnServRtmHistAlsName_Type = DisplayString
_AperTnServRtmHistAlsName_Object = MibTableColumn
aperTnServRtmHistAlsName = _AperTnServRtmHistAlsName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 3),
    _AperTnServRtmHistAlsName_Type()
)
aperTnServRtmHistAlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistAlsName.setStatus("mandatory")
_AperTnServRtmHistLuNumber_Type = Integer32
_AperTnServRtmHistLuNumber_Object = MibTableColumn
aperTnServRtmHistLuNumber = _AperTnServRtmHistLuNumber_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 4),
    _AperTnServRtmHistLuNumber_Type()
)
aperTnServRtmHistLuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistLuNumber.setStatus("mandatory")
_AperTnServRtmHistClientIP_Type = IpAddress
_AperTnServRtmHistClientIP_Object = MibTableColumn
aperTnServRtmHistClientIP = _AperTnServRtmHistClientIP_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 5),
    _AperTnServRtmHistClientIP_Type()
)
aperTnServRtmHistClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistClientIP.setStatus("mandatory")
_AperTnServRtmHistClientPort_Type = Integer32
_AperTnServRtmHistClientPort_Object = MibTableColumn
aperTnServRtmHistClientPort = _AperTnServRtmHistClientPort_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 6),
    _AperTnServRtmHistClientPort_Type()
)
aperTnServRtmHistClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistClientPort.setStatus("mandatory")
_AperTnServRtmHistDeviceName_Type = DisplayString
_AperTnServRtmHistDeviceName_Object = MibTableColumn
aperTnServRtmHistDeviceName = _AperTnServRtmHistDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 7),
    _AperTnServRtmHistDeviceName_Type()
)
aperTnServRtmHistDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistDeviceName.setStatus("mandatory")
_AperTnServRtmHistUserName_Type = DisplayString
_AperTnServRtmHistUserName_Object = MibTableColumn
aperTnServRtmHistUserName = _AperTnServRtmHistUserName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 8),
    _AperTnServRtmHistUserName_Type()
)
aperTnServRtmHistUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistUserName.setStatus("mandatory")
_AperTnServRtmHistSessionName_Type = DisplayString
_AperTnServRtmHistSessionName_Object = MibTableColumn
aperTnServRtmHistSessionName = _AperTnServRtmHistSessionName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 9),
    _AperTnServRtmHistSessionName_Type()
)
aperTnServRtmHistSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistSessionName.setStatus("mandatory")


class _AperTnServRtmHistDef_Type(Integer32):
    """Custom type aperTnServRtmHistDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cdeb", 3),
          ("firstChar", 1),
          ("kb", 2))
    )


_AperTnServRtmHistDef_Type.__name__ = "Integer32"
_AperTnServRtmHistDef_Object = MibTableColumn
aperTnServRtmHistDef = _AperTnServRtmHistDef_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 10),
    _AperTnServRtmHistDef_Type()
)
aperTnServRtmHistDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistDef.setStatus("mandatory")


class _AperTnServRtmHistMeasureTcpIpTime_Type(Integer32):
    """Custom type aperTnServRtmHistMeasureTcpIpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServRtmHistMeasureTcpIpTime_Type.__name__ = "Integer32"
_AperTnServRtmHistMeasureTcpIpTime_Object = MibTableColumn
aperTnServRtmHistMeasureTcpIpTime = _AperTnServRtmHistMeasureTcpIpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 11),
    _AperTnServRtmHistMeasureTcpIpTime_Type()
)
aperTnServRtmHistMeasureTcpIpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistMeasureTcpIpTime.setStatus("mandatory")


class _AperTnServRtmHistMeasureSnaTime_Type(Integer32):
    """Custom type aperTnServRtmHistMeasureSnaTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServRtmHistMeasureSnaTime_Type.__name__ = "Integer32"
_AperTnServRtmHistMeasureSnaTime_Object = MibTableColumn
aperTnServRtmHistMeasureSnaTime = _AperTnServRtmHistMeasureSnaTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 12),
    _AperTnServRtmHistMeasureSnaTime_Type()
)
aperTnServRtmHistMeasureSnaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistMeasureSnaTime.setStatus("mandatory")
_AperTnServRtmHistSamplingFactor_Type = Integer32
_AperTnServRtmHistSamplingFactor_Object = MibTableColumn
aperTnServRtmHistSamplingFactor = _AperTnServRtmHistSamplingFactor_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 13),
    _AperTnServRtmHistSamplingFactor_Type()
)
aperTnServRtmHistSamplingFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistSamplingFactor.setStatus("mandatory")
_AperTnServRtmHistNumberOfBoundaries_Type = Integer32
_AperTnServRtmHistNumberOfBoundaries_Object = MibTableColumn
aperTnServRtmHistNumberOfBoundaries = _AperTnServRtmHistNumberOfBoundaries_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 14),
    _AperTnServRtmHistNumberOfBoundaries_Type()
)
aperTnServRtmHistNumberOfBoundaries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistNumberOfBoundaries.setStatus("mandatory")
_AperTnServRtmHistBoundary1_Type = Integer32
_AperTnServRtmHistBoundary1_Object = MibTableColumn
aperTnServRtmHistBoundary1 = _AperTnServRtmHistBoundary1_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 15),
    _AperTnServRtmHistBoundary1_Type()
)
aperTnServRtmHistBoundary1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistBoundary1.setStatus("mandatory")
_AperTnServRtmHistBoundary2_Type = Integer32
_AperTnServRtmHistBoundary2_Object = MibTableColumn
aperTnServRtmHistBoundary2 = _AperTnServRtmHistBoundary2_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 16),
    _AperTnServRtmHistBoundary2_Type()
)
aperTnServRtmHistBoundary2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistBoundary2.setStatus("mandatory")
_AperTnServRtmHistBoundary3_Type = Integer32
_AperTnServRtmHistBoundary3_Object = MibTableColumn
aperTnServRtmHistBoundary3 = _AperTnServRtmHistBoundary3_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 17),
    _AperTnServRtmHistBoundary3_Type()
)
aperTnServRtmHistBoundary3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistBoundary3.setStatus("mandatory")
_AperTnServRtmHistBoundary4_Type = Integer32
_AperTnServRtmHistBoundary4_Object = MibTableColumn
aperTnServRtmHistBoundary4 = _AperTnServRtmHistBoundary4_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 18),
    _AperTnServRtmHistBoundary4_Type()
)
aperTnServRtmHistBoundary4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistBoundary4.setStatus("mandatory")
_AperTnServRtmHistCounter1_Type = Counter32
_AperTnServRtmHistCounter1_Object = MibTableColumn
aperTnServRtmHistCounter1 = _AperTnServRtmHistCounter1_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 19),
    _AperTnServRtmHistCounter1_Type()
)
aperTnServRtmHistCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistCounter1.setStatus("mandatory")
_AperTnServRtmHistCounter2_Type = Counter32
_AperTnServRtmHistCounter2_Object = MibTableColumn
aperTnServRtmHistCounter2 = _AperTnServRtmHistCounter2_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 20),
    _AperTnServRtmHistCounter2_Type()
)
aperTnServRtmHistCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistCounter2.setStatus("mandatory")
_AperTnServRtmHistCounter3_Type = Counter32
_AperTnServRtmHistCounter3_Object = MibTableColumn
aperTnServRtmHistCounter3 = _AperTnServRtmHistCounter3_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 21),
    _AperTnServRtmHistCounter3_Type()
)
aperTnServRtmHistCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistCounter3.setStatus("mandatory")
_AperTnServRtmHistCounter4_Type = Counter32
_AperTnServRtmHistCounter4_Object = MibTableColumn
aperTnServRtmHistCounter4 = _AperTnServRtmHistCounter4_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 22),
    _AperTnServRtmHistCounter4_Type()
)
aperTnServRtmHistCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistCounter4.setStatus("mandatory")
_AperTnServRtmHistOverFlows_Type = Counter32
_AperTnServRtmHistOverFlows_Object = MibTableColumn
aperTnServRtmHistOverFlows = _AperTnServRtmHistOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 23),
    _AperTnServRtmHistOverFlows_Type()
)
aperTnServRtmHistOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistOverFlows.setStatus("mandatory")


class _AperTnServRtmHistCounterOverflowed_Type(Integer32):
    """Custom type aperTnServRtmHistCounterOverflowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServRtmHistCounterOverflowed_Type.__name__ = "Integer32"
_AperTnServRtmHistCounterOverflowed_Object = MibTableColumn
aperTnServRtmHistCounterOverflowed = _AperTnServRtmHistCounterOverflowed_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 24),
    _AperTnServRtmHistCounterOverflowed_Type()
)
aperTnServRtmHistCounterOverflowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistCounterOverflowed.setStatus("mandatory")
_AperTnServRtmHistNumTrans_Type = Integer32
_AperTnServRtmHistNumTrans_Object = MibTableColumn
aperTnServRtmHistNumTrans = _AperTnServRtmHistNumTrans_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 25),
    _AperTnServRtmHistNumTrans_Type()
)
aperTnServRtmHistNumTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistNumTrans.setStatus("mandatory")
_AperTnServRtmHistTotalRspTime_Type = Integer32
_AperTnServRtmHistTotalRspTime_Object = MibTableColumn
aperTnServRtmHistTotalRspTime = _AperTnServRtmHistTotalRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 26),
    _AperTnServRtmHistTotalRspTime_Type()
)
aperTnServRtmHistTotalRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistTotalRspTime.setStatus("mandatory")
_AperTnServRtmHistAvgRspTime_Type = Integer32
_AperTnServRtmHistAvgRspTime_Object = MibTableColumn
aperTnServRtmHistAvgRspTime = _AperTnServRtmHistAvgRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 27),
    _AperTnServRtmHistAvgRspTime_Type()
)
aperTnServRtmHistAvgRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistAvgRspTime.setStatus("mandatory")
_AperTnServRtmHistMinRspTime_Type = Integer32
_AperTnServRtmHistMinRspTime_Object = MibTableColumn
aperTnServRtmHistMinRspTime = _AperTnServRtmHistMinRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 28),
    _AperTnServRtmHistMinRspTime_Type()
)
aperTnServRtmHistMinRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistMinRspTime.setStatus("mandatory")
_AperTnServRtmHistMaxRspTime_Type = Integer32
_AperTnServRtmHistMaxRspTime_Object = MibTableColumn
aperTnServRtmHistMaxRspTime = _AperTnServRtmHistMaxRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 29),
    _AperTnServRtmHistMaxRspTime_Type()
)
aperTnServRtmHistMaxRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistMaxRspTime.setStatus("mandatory")
_AperTnServRtmHistTotalSnaRspTime_Type = Integer32
_AperTnServRtmHistTotalSnaRspTime_Object = MibTableColumn
aperTnServRtmHistTotalSnaRspTime = _AperTnServRtmHistTotalSnaRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 30),
    _AperTnServRtmHistTotalSnaRspTime_Type()
)
aperTnServRtmHistTotalSnaRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistTotalSnaRspTime.setStatus("mandatory")
_AperTnServRtmHistAvgSnaRspTime_Type = Integer32
_AperTnServRtmHistAvgSnaRspTime_Object = MibTableColumn
aperTnServRtmHistAvgSnaRspTime = _AperTnServRtmHistAvgSnaRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 31),
    _AperTnServRtmHistAvgSnaRspTime_Type()
)
aperTnServRtmHistAvgSnaRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistAvgSnaRspTime.setStatus("mandatory")
_AperTnServRtmHistNumTcpIpSamples_Type = Integer32
_AperTnServRtmHistNumTcpIpSamples_Object = MibTableColumn
aperTnServRtmHistNumTcpIpSamples = _AperTnServRtmHistNumTcpIpSamples_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 32),
    _AperTnServRtmHistNumTcpIpSamples_Type()
)
aperTnServRtmHistNumTcpIpSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistNumTcpIpSamples.setStatus("mandatory")
_AperTnServRtmHistTotalTcpIpRspTime_Type = Integer32
_AperTnServRtmHistTotalTcpIpRspTime_Object = MibTableColumn
aperTnServRtmHistTotalTcpIpRspTime = _AperTnServRtmHistTotalTcpIpRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 33),
    _AperTnServRtmHistTotalTcpIpRspTime_Type()
)
aperTnServRtmHistTotalTcpIpRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistTotalTcpIpRspTime.setStatus("mandatory")
_AperTnServRtmHistAvgTcpIpRspTime_Type = Integer32
_AperTnServRtmHistAvgTcpIpRspTime_Object = MibTableColumn
aperTnServRtmHistAvgTcpIpRspTime = _AperTnServRtmHistAvgTcpIpRspTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 34),
    _AperTnServRtmHistAvgTcpIpRspTime_Type()
)
aperTnServRtmHistAvgTcpIpRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistAvgTcpIpRspTime.setStatus("mandatory")
_AperTnServRtmHistAvgThinkTime_Type = Integer32
_AperTnServRtmHistAvgThinkTime_Object = MibTableColumn
aperTnServRtmHistAvgThinkTime = _AperTnServRtmHistAvgThinkTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 25, 1, 35),
    _AperTnServRtmHistAvgThinkTime_Type()
)
aperTnServRtmHistAvgThinkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmHistAvgThinkTime.setStatus("mandatory")
_AperTnServRtmNumAls_Type = Integer32
_AperTnServRtmNumAls_Object = MibScalar
aperTnServRtmNumAls = _AperTnServRtmNumAls_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 26),
    _AperTnServRtmNumAls_Type()
)
aperTnServRtmNumAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmNumAls.setStatus("mandatory")
_AperTnServRtmPerAlsTable_Object = MibTable
aperTnServRtmPerAlsTable = _AperTnServRtmPerAlsTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27)
)
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsTable.setStatus("mandatory")
_AperTnServRtmPerAlsEntry_Object = MibTableRow
aperTnServRtmPerAlsEntry = _AperTnServRtmPerAlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1)
)
aperTnServRtmPerAlsEntry.setIndexNames(
    (0, "APERTUS-TNSERVER-MIB", "aperTnServRtmPerAlsName"),
)
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsEntry.setStatus("mandatory")
_AperTnServRtmPerAlsName_Type = DisplayString
_AperTnServRtmPerAlsName_Object = MibTableColumn
aperTnServRtmPerAlsName = _AperTnServRtmPerAlsName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 1),
    _AperTnServRtmPerAlsName_Type()
)
aperTnServRtmPerAlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsName.setStatus("mandatory")


class _AperTnServRtmPerAlsControl_Type(Integer32):
    """Custom type aperTnServRtmPerAlsControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("local", 2),
          ("unsupported", 3))
    )


_AperTnServRtmPerAlsControl_Type.__name__ = "Integer32"
_AperTnServRtmPerAlsControl_Object = MibTableColumn
aperTnServRtmPerAlsControl = _AperTnServRtmPerAlsControl_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 2),
    _AperTnServRtmPerAlsControl_Type()
)
aperTnServRtmPerAlsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsControl.setStatus("mandatory")


class _AperTnServRtmPerAlsState_Type(Integer32):
    """Custom type aperTnServRtmPerAlsState based on Integer32"""
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


_AperTnServRtmPerAlsState_Type.__name__ = "Integer32"
_AperTnServRtmPerAlsState_Object = MibTableColumn
aperTnServRtmPerAlsState = _AperTnServRtmPerAlsState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 3),
    _AperTnServRtmPerAlsState_Type()
)
aperTnServRtmPerAlsState.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsState.setStatus("mandatory")


class _AperTnServRtmPerAlsDef_Type(Integer32):
    """Custom type aperTnServRtmPerAlsDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cdeb", 3),
          ("firstChar", 1),
          ("kb", 2))
    )


_AperTnServRtmPerAlsDef_Type.__name__ = "Integer32"
_AperTnServRtmPerAlsDef_Object = MibTableColumn
aperTnServRtmPerAlsDef = _AperTnServRtmPerAlsDef_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 4),
    _AperTnServRtmPerAlsDef_Type()
)
aperTnServRtmPerAlsDef.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsDef.setStatus("mandatory")


class _AperTnServRtmPerAlsMeasureTcpIpTime_Type(Integer32):
    """Custom type aperTnServRtmPerAlsMeasureTcpIpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServRtmPerAlsMeasureTcpIpTime_Type.__name__ = "Integer32"
_AperTnServRtmPerAlsMeasureTcpIpTime_Object = MibTableColumn
aperTnServRtmPerAlsMeasureTcpIpTime = _AperTnServRtmPerAlsMeasureTcpIpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 5),
    _AperTnServRtmPerAlsMeasureTcpIpTime_Type()
)
aperTnServRtmPerAlsMeasureTcpIpTime.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsMeasureTcpIpTime.setStatus("mandatory")


class _AperTnServRtmPerAlsMeasureSnaTime_Type(Integer32):
    """Custom type aperTnServRtmPerAlsMeasureSnaTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AperTnServRtmPerAlsMeasureSnaTime_Type.__name__ = "Integer32"
_AperTnServRtmPerAlsMeasureSnaTime_Object = MibTableColumn
aperTnServRtmPerAlsMeasureSnaTime = _AperTnServRtmPerAlsMeasureSnaTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 6),
    _AperTnServRtmPerAlsMeasureSnaTime_Type()
)
aperTnServRtmPerAlsMeasureSnaTime.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsMeasureSnaTime.setStatus("mandatory")
_AperTnServRtmPerAlsSamplingFactor_Type = Integer32
_AperTnServRtmPerAlsSamplingFactor_Object = MibTableColumn
aperTnServRtmPerAlsSamplingFactor = _AperTnServRtmPerAlsSamplingFactor_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 7),
    _AperTnServRtmPerAlsSamplingFactor_Type()
)
aperTnServRtmPerAlsSamplingFactor.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsSamplingFactor.setStatus("mandatory")
_AperTnServRtmPerAlsNumberOfBoundaries_Type = Integer32
_AperTnServRtmPerAlsNumberOfBoundaries_Object = MibTableColumn
aperTnServRtmPerAlsNumberOfBoundaries = _AperTnServRtmPerAlsNumberOfBoundaries_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 8),
    _AperTnServRtmPerAlsNumberOfBoundaries_Type()
)
aperTnServRtmPerAlsNumberOfBoundaries.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsNumberOfBoundaries.setStatus("mandatory")
_AperTnServRtmPerAlsBoundary1_Type = Integer32
_AperTnServRtmPerAlsBoundary1_Object = MibTableColumn
aperTnServRtmPerAlsBoundary1 = _AperTnServRtmPerAlsBoundary1_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 9),
    _AperTnServRtmPerAlsBoundary1_Type()
)
aperTnServRtmPerAlsBoundary1.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsBoundary1.setStatus("mandatory")
_AperTnServRtmPerAlsBoundary2_Type = Integer32
_AperTnServRtmPerAlsBoundary2_Object = MibTableColumn
aperTnServRtmPerAlsBoundary2 = _AperTnServRtmPerAlsBoundary2_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 10),
    _AperTnServRtmPerAlsBoundary2_Type()
)
aperTnServRtmPerAlsBoundary2.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsBoundary2.setStatus("mandatory")
_AperTnServRtmPerAlsBoundary3_Type = Integer32
_AperTnServRtmPerAlsBoundary3_Object = MibTableColumn
aperTnServRtmPerAlsBoundary3 = _AperTnServRtmPerAlsBoundary3_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 11),
    _AperTnServRtmPerAlsBoundary3_Type()
)
aperTnServRtmPerAlsBoundary3.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsBoundary3.setStatus("mandatory")
_AperTnServRtmPerAlsBoundary4_Type = Integer32
_AperTnServRtmPerAlsBoundary4_Object = MibTableColumn
aperTnServRtmPerAlsBoundary4 = _AperTnServRtmPerAlsBoundary4_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 12),
    _AperTnServRtmPerAlsBoundary4_Type()
)
aperTnServRtmPerAlsBoundary4.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsBoundary4.setStatus("mandatory")


class _AperTnServRtmPerAlsResetCounters_Type(Integer32):
    """Custom type aperTnServRtmPerAlsResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_AperTnServRtmPerAlsResetCounters_Type.__name__ = "Integer32"
_AperTnServRtmPerAlsResetCounters_Object = MibTableColumn
aperTnServRtmPerAlsResetCounters = _AperTnServRtmPerAlsResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 13),
    _AperTnServRtmPerAlsResetCounters_Type()
)
aperTnServRtmPerAlsResetCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsResetCounters.setStatus("mandatory")
_AperTnServRtmPerAlsThresholdTrigger_Type = Integer32
_AperTnServRtmPerAlsThresholdTrigger_Object = MibTableColumn
aperTnServRtmPerAlsThresholdTrigger = _AperTnServRtmPerAlsThresholdTrigger_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 14),
    _AperTnServRtmPerAlsThresholdTrigger_Type()
)
aperTnServRtmPerAlsThresholdTrigger.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsThresholdTrigger.setStatus("mandatory")


class _AperTnServRtmPerAlsThresholdTriggerState_Type(Integer32):
    """Custom type aperTnServRtmPerAlsThresholdTriggerState based on Integer32"""
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


_AperTnServRtmPerAlsThresholdTriggerState_Type.__name__ = "Integer32"
_AperTnServRtmPerAlsThresholdTriggerState_Object = MibTableColumn
aperTnServRtmPerAlsThresholdTriggerState = _AperTnServRtmPerAlsThresholdTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 15),
    _AperTnServRtmPerAlsThresholdTriggerState_Type()
)
aperTnServRtmPerAlsThresholdTriggerState.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsThresholdTriggerState.setStatus("mandatory")


class _AperTnServRtmPerAlsCounterOverflowTriggerState_Type(Integer32):
    """Custom type aperTnServRtmPerAlsCounterOverflowTriggerState based on Integer32"""
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


_AperTnServRtmPerAlsCounterOverflowTriggerState_Type.__name__ = "Integer32"
_AperTnServRtmPerAlsCounterOverflowTriggerState_Object = MibTableColumn
aperTnServRtmPerAlsCounterOverflowTriggerState = _AperTnServRtmPerAlsCounterOverflowTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 16),
    _AperTnServRtmPerAlsCounterOverflowTriggerState_Type()
)
aperTnServRtmPerAlsCounterOverflowTriggerState.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsCounterOverflowTriggerState.setStatus("mandatory")


class _AperTnServRtmPerAlsUnbindTriggerState_Type(Integer32):
    """Custom type aperTnServRtmPerAlsUnbindTriggerState based on Integer32"""
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


_AperTnServRtmPerAlsUnbindTriggerState_Type.__name__ = "Integer32"
_AperTnServRtmPerAlsUnbindTriggerState_Object = MibTableColumn
aperTnServRtmPerAlsUnbindTriggerState = _AperTnServRtmPerAlsUnbindTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 4, 1, 27, 1, 17),
    _AperTnServRtmPerAlsUnbindTriggerState_Type()
)
aperTnServRtmPerAlsUnbindTriggerState.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    aperTnServRtmPerAlsUnbindTriggerState.setStatus("mandatory")
_AperTnServTraps_ObjectIdentity = ObjectIdentity
aperTnServTraps = _AperTnServTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 5)
)

# Managed Objects groups


# Notification objects

aperTnServTrapsRtmExcessiveTransaction = NotificationType(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 5, 0, 1)
)
aperTnServTrapsRtmExcessiveTransaction.setObjects(
      *(("APERTUS-TNSERVER-MIB", "aperTnServRtmAlsName"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmLuNumber"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmClientIP"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmClientPort"))
)
if mibBuilder.loadTexts:
    aperTnServTrapsRtmExcessiveTransaction.setStatus(
        ""
    )

aperTnServTrapsRtmCounterOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 5, 0, 2)
)
aperTnServTrapsRtmCounterOverflow.setObjects(
      *(("APERTUS-TNSERVER-MIB", "aperTnServRtmAlsName"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmLuNumber"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmClientIP"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmClientPort"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmPerAlsControl"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmCounterOverflowHostAlert"))
)
if mibBuilder.loadTexts:
    aperTnServTrapsRtmCounterOverflow.setStatus(
        ""
    )

aperTnServTrapsRtmSessionUnbound = NotificationType(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 5, 0, 3)
)
aperTnServTrapsRtmSessionUnbound.setObjects(
      *(("APERTUS-TNSERVER-MIB", "aperTnServRtmAlsName"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmLuNumber"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmClientIP"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmClientPort"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmPerAlsControl"),
        ("APERTUS-TNSERVER-MIB", "aperTnServRtmUnbindHostAlert"))
)
if mibBuilder.loadTexts:
    aperTnServTrapsRtmSessionUnbound.setStatus(
        ""
    )

aperTnServTrapsUserDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 543, 3, 1, 5, 0, 4)
)
aperTnServTrapsUserDisabled.setObjects(
      *(("APERTUS-TNSERVER-MIB", "aperTnServAdmUserName"),
        ("APERTUS-TNSERVER-MIB", "aperTnServOperConnsClientIP"),
        ("APERTUS-TNSERVER-MIB", "aperTnServOperConnsClientPort"))
)
if mibBuilder.loadTexts:
    aperTnServTrapsUserDisabled.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APERTUS-TNSERVER-MIB",
    **{"Tn3270AidKey": Tn3270AidKey,
       "Tn5250AidKey": Tn5250AidKey,
       "apertus": apertus,
       "express": express,
       "aperTnServMIB": aperTnServMIB,
       "aperTnServMibVersionNumber": aperTnServMibVersionNumber,
       "aperTnServAdm": aperTnServAdm,
       "aperTnServAdmGen": aperTnServAdmGen,
       "aperTnServAdmRelease": aperTnServAdmRelease,
       "aperTnServAdmSCN": aperTnServAdmSCN,
       "aperTnServAdmServerInstanceName": aperTnServAdmServerInstanceName,
       "aperTnServAdmMaxSessions": aperTnServAdmMaxSessions,
       "aperTnServAdmKeepAliveTimer": aperTnServAdmKeepAliveTimer,
       "aperTnServAdmKeepAliveResponseTimeout": aperTnServAdmKeepAliveResponseTimeout,
       "aperTnServAdmKeepAliveRetryCount": aperTnServAdmKeepAliveRetryCount,
       "aperTnServAdmDefaultInactivityLimit": aperTnServAdmDefaultInactivityLimit,
       "aperTnServAdmUndefinedClients": aperTnServAdmUndefinedClients,
       "aperTnServAdmAllowableNameTypes": aperTnServAdmAllowableNameTypes,
       "aperTnServAdmNumPorts": aperTnServAdmNumPorts,
       "aperTnServAdmPortTable": aperTnServAdmPortTable,
       "aperTnServAdmPortEntry": aperTnServAdmPortEntry,
       "aperTnServAdmPort": aperTnServAdmPort,
       "aperTnServAdmMenuMode": aperTnServAdmMenuMode,
       "aperTnServAdmPasswordLimit": aperTnServAdmPasswordLimit,
       "aperTnServAdmNumGroups": aperTnServAdmNumGroups,
       "aperTnServAdmGroupTableLastChange": aperTnServAdmGroupTableLastChange,
       "aperTnServAdmGroupTable": aperTnServAdmGroupTable,
       "aperTnServAdmGroupEntry": aperTnServAdmGroupEntry,
       "aperTnServAdmGroupName": aperTnServAdmGroupName,
       "aperTnServAdmGroupDescription": aperTnServAdmGroupDescription,
       "aperTnServAdmGroupMenuMode": aperTnServAdmGroupMenuMode,
       "aperTnServAdmGroupInactivityLimit": aperTnServAdmGroupInactivityLimit,
       "aperTnServAdmGroup3270StatusKey": aperTnServAdmGroup3270StatusKey,
       "aperTnServAdmGroup3270PasswordKey": aperTnServAdmGroup3270PasswordKey,
       "aperTnServAdmGroup3270SysReqKey": aperTnServAdmGroup3270SysReqKey,
       "aperTnServAdmGroup3270AttnKey": aperTnServAdmGroup3270AttnKey,
       "aperTnServAdmGroup5250StatusKey": aperTnServAdmGroup5250StatusKey,
       "aperTnServAdmGroup5250PasswordKey": aperTnServAdmGroup5250PasswordKey,
       "aperTnServAdmNumUsers": aperTnServAdmNumUsers,
       "aperTnServAdmUserTableLastChange": aperTnServAdmUserTableLastChange,
       "aperTnServAdmUserTable": aperTnServAdmUserTable,
       "aperTnServAdmUserEntry": aperTnServAdmUserEntry,
       "aperTnServAdmUserName": aperTnServAdmUserName,
       "aperTnServAdmUserDescription": aperTnServAdmUserDescription,
       "aperTnServAdmUserPasswordRequired": aperTnServAdmUserPasswordRequired,
       "aperTnServAdmUserEncryptedPassword": aperTnServAdmUserEncryptedPassword,
       "aperTnServAdmUserBadPasswordCounter": aperTnServAdmUserBadPasswordCounter,
       "aperTnServAdmUserMenuMode": aperTnServAdmUserMenuMode,
       "aperTnServAdmUserInactivityLimit": aperTnServAdmUserInactivityLimit,
       "aperTnServAdmUser3270StatusKey": aperTnServAdmUser3270StatusKey,
       "aperTnServAdmUser3270PasswordKey": aperTnServAdmUser3270PasswordKey,
       "aperTnServAdmUser3270SysReqKey": aperTnServAdmUser3270SysReqKey,
       "aperTnServAdmUser3270AttnKey": aperTnServAdmUser3270AttnKey,
       "aperTnServAdmUser5250StatusKey": aperTnServAdmUser5250StatusKey,
       "aperTnServAdmUser5250PasswordKey": aperTnServAdmUser5250PasswordKey,
       "aperTnServAdmNumRoutingEntries": aperTnServAdmNumRoutingEntries,
       "aperTnServAdmRoutingTableLastChange": aperTnServAdmRoutingTableLastChange,
       "aperTnServAdmRoutingTable": aperTnServAdmRoutingTable,
       "aperTnServAdmRoutingEntry": aperTnServAdmRoutingEntry,
       "aperTnServAdmRoutingSourceIp": aperTnServAdmRoutingSourceIp,
       "aperTnServAdmRoutingPort": aperTnServAdmRoutingPort,
       "aperTnServAdmRoutingDeviceType": aperTnServAdmRoutingDeviceType,
       "aperTnServAdmRoutingModelType": aperTnServAdmRoutingModelType,
       "aperTnServAdmRoutingDescription": aperTnServAdmRoutingDescription,
       "aperTnServAdmRoutingDestinationType": aperTnServAdmRoutingDestinationType,
       "aperTnServAdmRoutingDestination": aperTnServAdmRoutingDestination,
       "aperTnServAdmNumSecurAccEntries": aperTnServAdmNumSecurAccEntries,
       "aperTnServAdmSecurAccTableLastChange": aperTnServAdmSecurAccTableLastChange,
       "aperTnServAdmSecurAccTable": aperTnServAdmSecurAccTable,
       "aperTnServAdmSecurAccEntry": aperTnServAdmSecurAccEntry,
       "aperTnServAdmSecurAccSourceIp": aperTnServAdmSecurAccSourceIp,
       "aperTnServAdmSecurAccDescription": aperTnServAdmSecurAccDescription,
       "aperTnServAdmSecurAccDestination": aperTnServAdmSecurAccDestination,
       "aperTnServAdm3270": aperTnServAdm3270,
       "aperTnServAdm3270DefaultStatusKey": aperTnServAdm3270DefaultStatusKey,
       "aperTnServAdm3270DefaultSysReqKey": aperTnServAdm3270DefaultSysReqKey,
       "aperTnServAdm3270DefaultAttnKey": aperTnServAdm3270DefaultAttnKey,
       "aperTnServAdm3270DefaultPasswordKey": aperTnServAdm3270DefaultPasswordKey,
       "aperTnServAdm3270LoadBalanceMode": aperTnServAdm3270LoadBalanceMode,
       "aperTnServAdm3270NumSessions": aperTnServAdm3270NumSessions,
       "aperTnServAdm3270SessionTableLastChange": aperTnServAdm3270SessionTableLastChange,
       "aperTnServAdm3270SessionTable": aperTnServAdm3270SessionTable,
       "aperTnServAdm3270SessionEntry": aperTnServAdm3270SessionEntry,
       "aperTnServAdm3270SessionGroupOrUserName": aperTnServAdm3270SessionGroupOrUserName,
       "aperTnServAdm3270SessionName": aperTnServAdm3270SessionName,
       "aperTnServAdm3270SessionDescription": aperTnServAdm3270SessionDescription,
       "aperTnServAdm3270SessionGroupOrUser": aperTnServAdm3270SessionGroupOrUser,
       "aperTnServAdm3270SessionType": aperTnServAdm3270SessionType,
       "aperTnServAdm3270SessionModel": aperTnServAdm3270SessionModel,
       "aperTnServAdm3270SessionDestination": aperTnServAdm3270SessionDestination,
       "aperTnServAdm5250": aperTnServAdm5250,
       "aperTnServAdm5250DefaultStatusKey": aperTnServAdm5250DefaultStatusKey,
       "aperTnServAdm5250DefaultPasswordKey": aperTnServAdm5250DefaultPasswordKey,
       "aperTnServAdm5250NumSessions": aperTnServAdm5250NumSessions,
       "aperTnServAdm5250SessionTableLastChange": aperTnServAdm5250SessionTableLastChange,
       "aperTnServAdm5250SessionTable": aperTnServAdm5250SessionTable,
       "aperTnServAdm5250SessionEntry": aperTnServAdm5250SessionEntry,
       "aperTnServAdm5250SessionGroupOrUserName": aperTnServAdm5250SessionGroupOrUserName,
       "aperTnServAdm5250SessionName": aperTnServAdm5250SessionName,
       "aperTnServAdm5250SessionDescription": aperTnServAdm5250SessionDescription,
       "aperTnServAdm5250SessionGroupOrUser": aperTnServAdm5250SessionGroupOrUser,
       "aperTnServAdm5250SessionAutoSignon": aperTnServAdm5250SessionAutoSignon,
       "aperTnServAdm5250SessionRemoteUser": aperTnServAdm5250SessionRemoteUser,
       "aperTnServAdm5250SessionInitialMenu": aperTnServAdm5250SessionInitialMenu,
       "aperTnServAdm5250SessionInitialProgram": aperTnServAdm5250SessionInitialProgram,
       "aperTnServAdm5250SessionInitialLibrary": aperTnServAdm5250SessionInitialLibrary,
       "aperTnServAdm5250SessionAutoDeviceConfiguration": aperTnServAdm5250SessionAutoDeviceConfiguration,
       "aperTnServAdm5250SessionVirtualDeviceOrController": aperTnServAdm5250SessionVirtualDeviceOrController,
       "aperTnServAdm5250SessionVirtualDeviceOrControllerName": aperTnServAdm5250SessionVirtualDeviceOrControllerName,
       "aperTnServAdm5250SessionDestination": aperTnServAdm5250SessionDestination,
       "aperTnServOper": aperTnServOper,
       "aperTnServOperGen": aperTnServOperGen,
       "aperTnServOperStatus": aperTnServOperStatus,
       "aperTnServOperActiveSessions": aperTnServOperActiveSessions,
       "aperTnServOperUpTime": aperTnServOperUpTime,
       "aperTnServOperConns": aperTnServOperConns,
       "aperTnServOperConnsNumActive": aperTnServOperConnsNumActive,
       "aperTnServOperConnsTableLastChange": aperTnServOperConnsTableLastChange,
       "aperTnServOperConnsTable": aperTnServOperConnsTable,
       "aperTnServOperConnsEntry": aperTnServOperConnsEntry,
       "aperTnServOperConnsClientIP": aperTnServOperConnsClientIP,
       "aperTnServOperConnsClientPort": aperTnServOperConnsClientPort,
       "aperTnServOperConnsServerPort": aperTnServOperConnsServerPort,
       "aperTnServOperConnsType": aperTnServOperConnsType,
       "aperTnServOperConnsAppcSessId": aperTnServOperConnsAppcSessId,
       "aperTnServOperConnsAlsName": aperTnServOperConnsAlsName,
       "aperTnServOperConnsLuNumber": aperTnServOperConnsLuNumber,
       "aperTnServOperConnsState": aperTnServOperConnsState,
       "aperTnServOperConnsUpTime": aperTnServOperConnsUpTime,
       "aperTnServOperConnsInactivityLimit": aperTnServOperConnsInactivityLimit,
       "aperTnServOperConnsTimeSinceLastEvent": aperTnServOperConnsTimeSinceLastEvent,
       "aperTnServOperConnsDeviceName": aperTnServOperConnsDeviceName,
       "aperTnServOperConnsUserName": aperTnServOperConnsUserName,
       "aperTnServOperConnsSessionName": aperTnServOperConnsSessionName,
       "aperTnServOperConnsBytesOutbound": aperTnServOperConnsBytesOutbound,
       "aperTnServOperConnsBytesInbound": aperTnServOperConnsBytesInbound,
       "aperTnServOper3270": aperTnServOper3270,
       "aperTnServOper3270NumActive": aperTnServOper3270NumActive,
       "aperTnServOper3270Table": aperTnServOper3270Table,
       "aperTnServOper3270Entry": aperTnServOper3270Entry,
       "aperTnServOper3270AlsName": aperTnServOper3270AlsName,
       "aperTnServOper3270LuNumber": aperTnServOper3270LuNumber,
       "aperTnServOper3270ClientIP": aperTnServOper3270ClientIP,
       "aperTnServOper3270ClientPort": aperTnServOper3270ClientPort,
       "aperTnServOper3270LuType": aperTnServOper3270LuType,
       "aperTnServOper3270LuState": aperTnServOper3270LuState,
       "aperTnServOper3270SscpLuState": aperTnServOper3270SscpLuState,
       "aperTnServOper3270LuLuState": aperTnServOper3270LuLuState,
       "aperTnServOper3270KeyboardLock": aperTnServOper3270KeyboardLock,
       "aperTnServOper3270NetworkQualifiedSluName": aperTnServOper3270NetworkQualifiedSluName,
       "aperTnServOper3270ModelNumber": aperTnServOper3270ModelNumber,
       "aperTnServOper3270AssociatedPrinter": aperTnServOper3270AssociatedPrinter,
       "aperTnServOper5250": aperTnServOper5250,
       "aperTnServOper5250NumActive": aperTnServOper5250NumActive,
       "aperTnServOper5250TableLastChange": aperTnServOper5250TableLastChange,
       "aperTnServOper5250Table": aperTnServOper5250Table,
       "aperTnServOper5250Entry": aperTnServOper5250Entry,
       "aperTnServOper5250AppcSessId": aperTnServOper5250AppcSessId,
       "aperTnServOper5250ClientIP": aperTnServOper5250ClientIP,
       "aperTnServOper5250ClientPort": aperTnServOper5250ClientPort,
       "aperTnServOper5250AlsName": aperTnServOper5250AlsName,
       "aperTnServOper5250SymbolicDestination": aperTnServOper5250SymbolicDestination,
       "aperTnServOper5250LocalLuName": aperTnServOper5250LocalLuName,
       "aperTnServOper5250RemoteLuName": aperTnServOper5250RemoteLuName,
       "aperTnServOper5250ModeName": aperTnServOper5250ModeName,
       "aperTnServOper5250KeyboardLock": aperTnServOper5250KeyboardLock,
       "aperTnServStats": aperTnServStats,
       "aperTnServRtm": aperTnServRtm,
       "aperTnServRtmSupport": aperTnServRtmSupport,
       "aperTnServRtmDefaultState": aperTnServRtmDefaultState,
       "aperTnServRtmDefaultControl": aperTnServRtmDefaultControl,
       "aperTnServRtmDefaultLocalDisplay": aperTnServRtmDefaultLocalDisplay,
       "aperTnServRtmDefaultDef": aperTnServRtmDefaultDef,
       "aperTnServRtmDefaultMeasureTcpIpTime": aperTnServRtmDefaultMeasureTcpIpTime,
       "aperTnServRtmDefaultMeasureSnaTime": aperTnServRtmDefaultMeasureSnaTime,
       "aperTnServRtmDefaultSamplingFactor": aperTnServRtmDefaultSamplingFactor,
       "aperTnServRtmDefaultNumberOfBoundaries": aperTnServRtmDefaultNumberOfBoundaries,
       "aperTnServRtmDefaultBoundary1": aperTnServRtmDefaultBoundary1,
       "aperTnServRtmDefaultBoundary2": aperTnServRtmDefaultBoundary2,
       "aperTnServRtmDefaultBoundary3": aperTnServRtmDefaultBoundary3,
       "aperTnServRtmDefaultBoundary4": aperTnServRtmDefaultBoundary4,
       "aperTnServRtmDefaultThresholdTrigger": aperTnServRtmDefaultThresholdTrigger,
       "aperTnServRtmDefaultThresholdTriggerState": aperTnServRtmDefaultThresholdTriggerState,
       "aperTnServRtmDefaultCounterOverflowTriggerState": aperTnServRtmDefaultCounterOverflowTriggerState,
       "aperTnServRtmDefaultCounterOverflowHostAlert": aperTnServRtmDefaultCounterOverflowHostAlert,
       "aperTnServRtmDefaultUnbindTriggerState": aperTnServRtmDefaultUnbindTriggerState,
       "aperTnServRtmDefaultUnbindHostAlert": aperTnServRtmDefaultUnbindHostAlert,
       "aperTnServRtmNumActive": aperTnServRtmNumActive,
       "aperTnServRtmTable": aperTnServRtmTable,
       "aperTnServRtmEntry": aperTnServRtmEntry,
       "aperTnServRtmAlsName": aperTnServRtmAlsName,
       "aperTnServRtmLuNumber": aperTnServRtmLuNumber,
       "aperTnServRtmClientIP": aperTnServRtmClientIP,
       "aperTnServRtmClientPort": aperTnServRtmClientPort,
       "aperTnServRtmState": aperTnServRtmState,
       "aperTnServRtmLocalDisplay": aperTnServRtmLocalDisplay,
       "aperTnServRtmUpTime": aperTnServRtmUpTime,
       "aperTnServRtmDef": aperTnServRtmDef,
       "aperTnServRtmMeasureTcpIpTime": aperTnServRtmMeasureTcpIpTime,
       "aperTnServRtmMeasureSnaTime": aperTnServRtmMeasureSnaTime,
       "aperTnServRtmSamplingFactor": aperTnServRtmSamplingFactor,
       "aperTnServRtmNumberOfBoundaries": aperTnServRtmNumberOfBoundaries,
       "aperTnServRtmBoundary1": aperTnServRtmBoundary1,
       "aperTnServRtmBoundary2": aperTnServRtmBoundary2,
       "aperTnServRtmBoundary3": aperTnServRtmBoundary3,
       "aperTnServRtmBoundary4": aperTnServRtmBoundary4,
       "aperTnServRtmCounter1": aperTnServRtmCounter1,
       "aperTnServRtmCounter2": aperTnServRtmCounter2,
       "aperTnServRtmCounter3": aperTnServRtmCounter3,
       "aperTnServRtmCounter4": aperTnServRtmCounter4,
       "aperTnServRtmOverFlows": aperTnServRtmOverFlows,
       "aperTnServRtmThresholdTrigger": aperTnServRtmThresholdTrigger,
       "aperTnServRtmThresholdTriggerState": aperTnServRtmThresholdTriggerState,
       "aperTnServRtmCounterOverflowed": aperTnServRtmCounterOverflowed,
       "aperTnServRtmCounterOverflowTriggerState": aperTnServRtmCounterOverflowTriggerState,
       "aperTnServRtmCounterOverflowHostAlert": aperTnServRtmCounterOverflowHostAlert,
       "aperTnServRtmUnbindTriggerState": aperTnServRtmUnbindTriggerState,
       "aperTnServRtmUnbindHostAlert": aperTnServRtmUnbindHostAlert,
       "aperTnServRtmNumTrans": aperTnServRtmNumTrans,
       "aperTnServRtmTotalRspTime": aperTnServRtmTotalRspTime,
       "aperTnServRtmLastRspTime": aperTnServRtmLastRspTime,
       "aperTnServRtmAvgRspTime": aperTnServRtmAvgRspTime,
       "aperTnServRtmMinRspTime": aperTnServRtmMinRspTime,
       "aperTnServRtmMaxRspTime": aperTnServRtmMaxRspTime,
       "aperTnServRtmTotalSnaRspTime": aperTnServRtmTotalSnaRspTime,
       "aperTnServRtmAvgSnaRspTime": aperTnServRtmAvgSnaRspTime,
       "aperTnServRtmNumTcpIpSamples": aperTnServRtmNumTcpIpSamples,
       "aperTnServRtmTotalTcpIpRspTime": aperTnServRtmTotalTcpIpRspTime,
       "aperTnServRtmAvgTcpIpRspTime": aperTnServRtmAvgTcpIpRspTime,
       "aperTnServRtmLastThinkTime": aperTnServRtmLastThinkTime,
       "aperTnServRtmAvgThinkTime": aperTnServRtmAvgThinkTime,
       "aperTnServRtmMaxHist": aperTnServRtmMaxHist,
       "aperTnServRtmNumHist": aperTnServRtmNumHist,
       "aperTnServRtmLastHist": aperTnServRtmLastHist,
       "aperTnServRtmHistTable": aperTnServRtmHistTable,
       "aperTnServRtmHistEntry": aperTnServRtmHistEntry,
       "aperTnServRtmHistIndex": aperTnServRtmHistIndex,
       "aperTnServRtmHistWhenDisconnected": aperTnServRtmHistWhenDisconnected,
       "aperTnServRtmHistAlsName": aperTnServRtmHistAlsName,
       "aperTnServRtmHistLuNumber": aperTnServRtmHistLuNumber,
       "aperTnServRtmHistClientIP": aperTnServRtmHistClientIP,
       "aperTnServRtmHistClientPort": aperTnServRtmHistClientPort,
       "aperTnServRtmHistDeviceName": aperTnServRtmHistDeviceName,
       "aperTnServRtmHistUserName": aperTnServRtmHistUserName,
       "aperTnServRtmHistSessionName": aperTnServRtmHistSessionName,
       "aperTnServRtmHistDef": aperTnServRtmHistDef,
       "aperTnServRtmHistMeasureTcpIpTime": aperTnServRtmHistMeasureTcpIpTime,
       "aperTnServRtmHistMeasureSnaTime": aperTnServRtmHistMeasureSnaTime,
       "aperTnServRtmHistSamplingFactor": aperTnServRtmHistSamplingFactor,
       "aperTnServRtmHistNumberOfBoundaries": aperTnServRtmHistNumberOfBoundaries,
       "aperTnServRtmHistBoundary1": aperTnServRtmHistBoundary1,
       "aperTnServRtmHistBoundary2": aperTnServRtmHistBoundary2,
       "aperTnServRtmHistBoundary3": aperTnServRtmHistBoundary3,
       "aperTnServRtmHistBoundary4": aperTnServRtmHistBoundary4,
       "aperTnServRtmHistCounter1": aperTnServRtmHistCounter1,
       "aperTnServRtmHistCounter2": aperTnServRtmHistCounter2,
       "aperTnServRtmHistCounter3": aperTnServRtmHistCounter3,
       "aperTnServRtmHistCounter4": aperTnServRtmHistCounter4,
       "aperTnServRtmHistOverFlows": aperTnServRtmHistOverFlows,
       "aperTnServRtmHistCounterOverflowed": aperTnServRtmHistCounterOverflowed,
       "aperTnServRtmHistNumTrans": aperTnServRtmHistNumTrans,
       "aperTnServRtmHistTotalRspTime": aperTnServRtmHistTotalRspTime,
       "aperTnServRtmHistAvgRspTime": aperTnServRtmHistAvgRspTime,
       "aperTnServRtmHistMinRspTime": aperTnServRtmHistMinRspTime,
       "aperTnServRtmHistMaxRspTime": aperTnServRtmHistMaxRspTime,
       "aperTnServRtmHistTotalSnaRspTime": aperTnServRtmHistTotalSnaRspTime,
       "aperTnServRtmHistAvgSnaRspTime": aperTnServRtmHistAvgSnaRspTime,
       "aperTnServRtmHistNumTcpIpSamples": aperTnServRtmHistNumTcpIpSamples,
       "aperTnServRtmHistTotalTcpIpRspTime": aperTnServRtmHistTotalTcpIpRspTime,
       "aperTnServRtmHistAvgTcpIpRspTime": aperTnServRtmHistAvgTcpIpRspTime,
       "aperTnServRtmHistAvgThinkTime": aperTnServRtmHistAvgThinkTime,
       "aperTnServRtmNumAls": aperTnServRtmNumAls,
       "aperTnServRtmPerAlsTable": aperTnServRtmPerAlsTable,
       "aperTnServRtmPerAlsEntry": aperTnServRtmPerAlsEntry,
       "aperTnServRtmPerAlsName": aperTnServRtmPerAlsName,
       "aperTnServRtmPerAlsControl": aperTnServRtmPerAlsControl,
       "aperTnServRtmPerAlsState": aperTnServRtmPerAlsState,
       "aperTnServRtmPerAlsDef": aperTnServRtmPerAlsDef,
       "aperTnServRtmPerAlsMeasureTcpIpTime": aperTnServRtmPerAlsMeasureTcpIpTime,
       "aperTnServRtmPerAlsMeasureSnaTime": aperTnServRtmPerAlsMeasureSnaTime,
       "aperTnServRtmPerAlsSamplingFactor": aperTnServRtmPerAlsSamplingFactor,
       "aperTnServRtmPerAlsNumberOfBoundaries": aperTnServRtmPerAlsNumberOfBoundaries,
       "aperTnServRtmPerAlsBoundary1": aperTnServRtmPerAlsBoundary1,
       "aperTnServRtmPerAlsBoundary2": aperTnServRtmPerAlsBoundary2,
       "aperTnServRtmPerAlsBoundary3": aperTnServRtmPerAlsBoundary3,
       "aperTnServRtmPerAlsBoundary4": aperTnServRtmPerAlsBoundary4,
       "aperTnServRtmPerAlsResetCounters": aperTnServRtmPerAlsResetCounters,
       "aperTnServRtmPerAlsThresholdTrigger": aperTnServRtmPerAlsThresholdTrigger,
       "aperTnServRtmPerAlsThresholdTriggerState": aperTnServRtmPerAlsThresholdTriggerState,
       "aperTnServRtmPerAlsCounterOverflowTriggerState": aperTnServRtmPerAlsCounterOverflowTriggerState,
       "aperTnServRtmPerAlsUnbindTriggerState": aperTnServRtmPerAlsUnbindTriggerState,
       "aperTnServTraps": aperTnServTraps,
       "aperTnServTrapsRtmExcessiveTransaction": aperTnServTrapsRtmExcessiveTransaction,
       "aperTnServTrapsRtmCounterOverflow": aperTnServTrapsRtmCounterOverflow,
       "aperTnServTrapsRtmSessionUnbound": aperTnServTrapsRtmSessionUnbound,
       "aperTnServTrapsUserDisabled": aperTnServTrapsUserDisabled}
)
