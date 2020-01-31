#
# PySNMP MIB module CISCO-RSCN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RSCN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:11:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
FcGs3RejectReasonCode, = mibBuilder.importSymbols("CISCO-NS-MIB", "FcGs3RejectReasonCode")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcAddressId, = mibBuilder.importSymbols("CISCO-ST-TC", "FcAddressId")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, IpAddress, NotificationType, Gauge32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, TimeTicks, MibIdentifier, Counter64, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "NotificationType", "Gauge32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "TimeTicks", "MibIdentifier", "Counter64", "ModuleIdentity", "Integer32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoRscnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 292))
ciscoRscnMIB.setRevisions(('2008-09-01 00:00', '2006-08-17 00:00', '2005-05-06 00:00', '2003-10-16 00:00', '2002-09-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRscnMIB.setRevisionsDescriptions(("modified rscnEventTov range from '1..2000' to '0.2000'.", 'Added following notifications -rscnIlsRxRejectReqNotify -rscnElsRxRejectReqNotify Added 2 new notification control objects: - rscnIlsRxRejectReqNotifyEnable - rscnElsRxRejectReqNotifyEnable Added rscnNotifyControlGroupSup1 OBJECT-GROUP Added rscnRejectNotifyGroup NOTIFICATION-GROUP Added rscnMIBComplianceRev3 MODULE-COMPLIANCE', 'Added rscnEventTovTable.', 'Added rscnMultiPidTable.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRscnMIB.setLastUpdated('200809010000Z')
if mibBuilder.loadTexts: ciscoRscnMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoRscnMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoRscnMIB.setDescription("The MIB module for the management of the Fibre Channel's Registered State Change Notification (RSCN) functionality, which is specified by FC-FLA and FC-FS. GLOSSARY : RSCN - Registered State Change Notification. RSCN Notifications are sent to Nx_ports and other switches to notify that an event has occured. SW_RSCN - Switch Registered State Change Notification. SW_RSCN Notifications are sent to neighbouring switches in a fabric to notify that an event has occured. ELS - Extended Link Service. RSCN Software module uses ELS frame formats to send RSCN messages. ILS - Inter Link Service. RSCN Software module uses ILS frame formats to send SW-RSCN messages.")
ciscoRscnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 292, 1))
rscnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 292, 2))
rscnConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1))
rscnStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2))
rscnInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 3))
rscnNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4))
rscnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4, 0))
rscnScrNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnScrNumber.setStatus('current')
if mibBuilder.loadTexts: rscnScrNumber.setDescription('The number of Nx_Ports currently registered to receive RSCNs.')
rscnScrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 2), )
if mibBuilder.loadTexts: rscnScrTable.setStatus('current')
if mibBuilder.loadTexts: rscnScrTable.setDescription('A table of Nx_Ports that have registered to receive RSCNs on all VSANs configured on the local switch.')
rscnScrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-RSCN-MIB", "rscnScrFcId"))
if mibBuilder.loadTexts: rscnScrEntry.setStatus('current')
if mibBuilder.loadTexts: rscnScrEntry.setDescription('An entry (conceptual row) containing information about one Nx_Port which has registered to receive RSCNs on the VSAN indicated by vsanIndex.')
rscnScrFcId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 2, 1, 1), FcAddressId())
if mibBuilder.loadTexts: rscnScrFcId.setStatus('current')
if mibBuilder.loadTexts: rscnScrFcId.setDescription('The Fibre Channel Identifier (FC-ID) of the subscribing Nx_Port.')
rscnScrRegType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fromFabricCtrlr", 1), ("fromNxPort", 2), ("fromBoth", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnScrRegType.setStatus('current')
if mibBuilder.loadTexts: rscnScrRegType.setDescription("This object indicates the type of registration desired by the subscriber. 'fromFabricCtrlr' indicates RSCNs generated by the Fabric Controller. 'fromNxPort' indicates RSCNs generated by Nx_Ports. 'fromBoth' indicates RSCNs generated by Fabric Controller and Nx_Ports.")
rscnScrTotalRejects = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnScrTotalRejects.setStatus('current')
if mibBuilder.loadTexts: rscnScrTotalRejects.setDescription('The total number of SCRs rejected across all VSANs by the local switch.')
rscnRscnReqTotalRejects = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnRscnReqTotalRejects.setStatus('current')
if mibBuilder.loadTexts: rscnRscnReqTotalRejects.setDescription('The total number of RSCN requests rejected across all VSANs by the local switch.')
rscnSwRscnReqTotalRejects = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnSwRscnReqTotalRejects.setStatus('current')
if mibBuilder.loadTexts: rscnSwRscnReqTotalRejects.setDescription('The total number of SW_RSCN requests rejected across all VSANs by the local switch.')
rscnStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4), )
if mibBuilder.loadTexts: rscnStatsTable.setStatus('current')
if mibBuilder.loadTexts: rscnStatsTable.setDescription('The statistics related to the RSCN module. The statistics are maintained per VSAN.')
rscnStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: rscnStatsEntry.setStatus('current')
if mibBuilder.loadTexts: rscnStatsEntry.setDescription('An entry (conceptual row) in this table.')
rscnRxScrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnRxScrs.setStatus('current')
if mibBuilder.loadTexts: rscnRxScrs.setDescription('The number of SCRs received from Nx_Ports on this VSAN.')
rscnRxRscns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnRxRscns.setStatus('current')
if mibBuilder.loadTexts: rscnRxRscns.setDescription('The number of RSCNs from Nx_Ports received on this VSAN.')
rscnTxRscns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnTxRscns.setStatus('current')
if mibBuilder.loadTexts: rscnTxRscns.setDescription('The total number of RSCNs transmitted on this VSAN.')
rscnRxSwRscns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnRxSwRscns.setStatus('current')
if mibBuilder.loadTexts: rscnRxSwRscns.setDescription('The number of Inter-Switch Registered State Change Notifications (SW_RSCN) received on this VSAN from other switches.')
rscnTxSwRscns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnTxSwRscns.setStatus('current')
if mibBuilder.loadTexts: rscnTxSwRscns.setDescription('The number of Inter-Switch Registered State Change Notifications (SW_RSCN) transmitted on this VSAN to other switches.')
rscnScrRej = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnScrRej.setStatus('current')
if mibBuilder.loadTexts: rscnScrRej.setDescription('The number of SCR rejected on this VSAN.')
rscnRscnReqRej = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnRscnReqRej.setStatus('current')
if mibBuilder.loadTexts: rscnRscnReqRej.setDescription('The number of RSCN requests rejected on this VSAN.')
rscnSwRscnReqRej = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnSwRscnReqRej.setStatus('current')
if mibBuilder.loadTexts: rscnSwRscnReqRej.setDescription('The number of SW_RSCN requests rejected on this VSAN.')
rscnIlsRejReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 3, 1), FcGs3RejectReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnIlsRejReasonCode.setStatus('current')
if mibBuilder.loadTexts: rscnIlsRejReasonCode.setDescription('The reason code corresponding to an ILS request rejection. This object contains the reason code corresponding to the most recent SCR or RSCN request rejection by the RSCN module.')
rscnElsRejReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 3, 2), FcGs3RejectReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscnElsRejReasonCode.setStatus('current')
if mibBuilder.loadTexts: rscnElsRejReasonCode.setDescription('The reason code corresponding to an ELS request rejection. This object contains the reason code corresponding the most recent SW_RSCN request rejection by the RSCN module.')
rscnIlsRejectReqNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rscnIlsRejectReqNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: rscnIlsRejectReqNotifyEnable.setDescription("This object specifies if the RSCN module should generate 'rscnIlsRejectReqNotify' notifications. If value of this object is 'true', then the notification is generated when a SW_RSCN request is rejected. If it is 'false', the notification is not generated.")
rscnElsRejectReqNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rscnElsRejectReqNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: rscnElsRejectReqNotifyEnable.setDescription("This object specifies if the RSCN module should generate 'rscnElsRejectReqNotify' notifications. If value of this object is 'true', then the notification is generated when a SCR or RSCN request is rejected. If it is 'false', the notification is not generated.")
rscnNotifyFcId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 5), FcAddressId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rscnNotifyFcId.setStatus('current')
if mibBuilder.loadTexts: rscnNotifyFcId.setDescription('The FC-ID of an Nx_Port. This object is to be used in the notifications: rscnElsRejectReqNotify, rscnIlsRejectReqNotify, rscnElsRxRejectReqNotify and rscnIlsRxRejectReqNotify. This object is defined since the rscnScrFcId object in the rscnScrTable is not-accessible.')
rscnMultiPidTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 6), )
if mibBuilder.loadTexts: rscnMultiPidTable.setStatus('current')
if mibBuilder.loadTexts: rscnMultiPidTable.setDescription('This table contains the configuration information for multi-pid option for all VSANs on the local device.')
rscnMultiPidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: rscnMultiPidEntry.setStatus('current')
if mibBuilder.loadTexts: rscnMultiPidEntry.setDescription('An entry (conceptual row) in this table.')
rscnMultiPidEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 6, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rscnMultiPidEnable.setStatus('current')
if mibBuilder.loadTexts: rscnMultiPidEnable.setDescription("This object specifies whether the multi-pid option is enabled on this VSAN. If this object is set to 'true', then the multi-pid option is enabled. If this object is set to 'false, then the multi-pid option is disabled. If the multi-pid option is enabled, then RSCNs generated to the registered Nx ports may contain more than one affected port ID. By enabling this option, the number of RSCNs generated can be reduced.")
rscnEventTovTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 7), )
if mibBuilder.loadTexts: rscnEventTovTable.setStatus('current')
if mibBuilder.loadTexts: rscnEventTovTable.setDescription('This table contains the configuration information for Event Time Out Value option for all VSANs on the local device. The Event TOV value is used to send the coalesced RSCNs to the registered user.')
rscnEventTovEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 7, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: rscnEventTovEntry.setStatus('current')
if mibBuilder.loadTexts: rscnEventTovEntry.setDescription('An entry (conceptual row) in this table represents the Event Time out value on a VSAN.')
rscnEventTov = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000)).clone(2000)).setUnits('milli-secs').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rscnEventTov.setStatus('current')
if mibBuilder.loadTexts: rscnEventTov.setDescription('This object specifies the event time-out value configured for the VSAN. This timeout value corresponds to the coalescing timeout. This object is used to merge a number of RSCNs into a single frame and send them out when timer expires. The value of zero indicates that frames will not be coalesced.')
rscnIlsRxRejectReqNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rscnIlsRxRejectReqNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: rscnIlsRxRejectReqNotifyEnable.setDescription("This object specifies if the RSCN module should generate 'rscnIlsRxRejectReqNotify' notifications. If value of this object is 'true', then the notification is generated when a SW_RSCN that is rejected by another device is received on the local device. If it is 'false', the notification is not generated.")
rscnElsRxRejectReqNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rscnElsRxRejectReqNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: rscnElsRxRejectReqNotifyEnable.setDescription("This object specifies if the RSCN module should generate 'rscnElsRxRejectReqNotify' notifications. If value of this object is 'true', then the notification is generated when a RSCN request that is rejected by another device is received on the local device. If it is 'false', the notification is not generated.")
rscnElsRejectReqNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4, 0, 1)).setObjects(("CISCO-RSCN-MIB", "rscnElsRejReasonCode"), ("CISCO-RSCN-MIB", "rscnNotifyFcId"))
if mibBuilder.loadTexts: rscnElsRejectReqNotify.setStatus('current')
if mibBuilder.loadTexts: rscnElsRejectReqNotify.setDescription('This notification is generated by the RSCN module on this switch whenever it rejects a SCR or RSCN request. The rscnScrFcId object indicates the FC-ID of the sender of the request that was rejected.')
rscnIlsRejectReqNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4, 0, 2)).setObjects(("CISCO-RSCN-MIB", "rscnIlsRejReasonCode"), ("CISCO-RSCN-MIB", "rscnNotifyFcId"))
if mibBuilder.loadTexts: rscnIlsRejectReqNotify.setStatus('current')
if mibBuilder.loadTexts: rscnIlsRejectReqNotify.setDescription('This notification is generated by the RSCN module on this switch whenever it rejects a SW_RSCN request. The rscnScrFcId object contains the FC-ID of the sender of the request that was rejected.')
rscnElsRxRejectReqNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4, 0, 3)).setObjects(("CISCO-RSCN-MIB", "rscnElsRejReasonCode"), ("CISCO-RSCN-MIB", "rscnNotifyFcId"))
if mibBuilder.loadTexts: rscnElsRxRejectReqNotify.setStatus('current')
if mibBuilder.loadTexts: rscnElsRxRejectReqNotify.setDescription('This notification is generated by the RSCN module on this switch whenever it receives a rejected RSCN request. The rscnScrFcId object indicates the FC-ID of the sender where the request was rejected.')
rscnIlsRxRejectReqNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 292, 1, 4, 0, 4)).setObjects(("CISCO-RSCN-MIB", "rscnIlsRejReasonCode"), ("CISCO-RSCN-MIB", "rscnNotifyFcId"))
if mibBuilder.loadTexts: rscnIlsRxRejectReqNotify.setStatus('current')
if mibBuilder.loadTexts: rscnIlsRxRejectReqNotify.setDescription('This notification is generated by the RSCN module on this switch whenever it receives a rejected SW_RSCN request. The rscnScrFcId object contains the FC-ID of the sender where the request was rejected.')
rscnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 1))
rscnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2))
rscnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 1, 1)).setObjects(("CISCO-RSCN-MIB", "rscnConfigGroup"), ("CISCO-RSCN-MIB", "rscnStatsGroup"), ("CISCO-RSCN-MIB", "rscnNotifyControlGroup"), ("CISCO-RSCN-MIB", "rscnNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnMIBCompliance = rscnMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: rscnMIBCompliance.setDescription('The compliance statement for entities which implement RSCN feature.')
rscnMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 1, 2)).setObjects(("CISCO-RSCN-MIB", "rscnConfigGroupRev1"), ("CISCO-RSCN-MIB", "rscnStatsGroup"), ("CISCO-RSCN-MIB", "rscnNotifyControlGroup"), ("CISCO-RSCN-MIB", "rscnNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnMIBComplianceRev1 = rscnMIBComplianceRev1.setStatus('deprecated')
if mibBuilder.loadTexts: rscnMIBComplianceRev1.setDescription('The compliance statement for entities which implement RSCN feature.')
rscnMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 1, 3)).setObjects(("CISCO-RSCN-MIB", "rscnConfigGroupRev1"), ("CISCO-RSCN-MIB", "rscnStatsGroup"), ("CISCO-RSCN-MIB", "rscnNotifyControlGroup"), ("CISCO-RSCN-MIB", "rscnNotifyGroup"), ("CISCO-RSCN-MIB", "rscnConfigGroupRev1Sup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnMIBComplianceRev2 = rscnMIBComplianceRev2.setStatus('deprecated')
if mibBuilder.loadTexts: rscnMIBComplianceRev2.setDescription('The compliance statement for entities which implement RSCN feature.')
rscnMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 1, 4)).setObjects(("CISCO-RSCN-MIB", "rscnConfigGroupRev1"), ("CISCO-RSCN-MIB", "rscnStatsGroup"), ("CISCO-RSCN-MIB", "rscnNotifyControlGroup"), ("CISCO-RSCN-MIB", "rscnNotifyGroup"), ("CISCO-RSCN-MIB", "rscnConfigGroupRev1Sup1"), ("CISCO-RSCN-MIB", "rscnRejectNotifyGroup"), ("CISCO-RSCN-MIB", "rscnNotifyControlGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnMIBComplianceRev3 = rscnMIBComplianceRev3.setStatus('current')
if mibBuilder.loadTexts: rscnMIBComplianceRev3.setDescription('The compliance statement for entities which implement RSCN feature.')
rscnConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 1)).setObjects(("CISCO-RSCN-MIB", "rscnScrNumber"), ("CISCO-RSCN-MIB", "rscnScrRegType"), ("CISCO-RSCN-MIB", "rscnNotifyFcId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnConfigGroup = rscnConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: rscnConfigGroup.setDescription('A collection of objects for configuring and displaying SCR entries.')
rscnStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 2)).setObjects(("CISCO-RSCN-MIB", "rscnScrTotalRejects"), ("CISCO-RSCN-MIB", "rscnRscnReqTotalRejects"), ("CISCO-RSCN-MIB", "rscnSwRscnReqTotalRejects"), ("CISCO-RSCN-MIB", "rscnRxScrs"), ("CISCO-RSCN-MIB", "rscnRxRscns"), ("CISCO-RSCN-MIB", "rscnTxRscns"), ("CISCO-RSCN-MIB", "rscnRxSwRscns"), ("CISCO-RSCN-MIB", "rscnTxSwRscns"), ("CISCO-RSCN-MIB", "rscnScrRej"), ("CISCO-RSCN-MIB", "rscnRscnReqRej"), ("CISCO-RSCN-MIB", "rscnSwRscnReqRej"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnStatsGroup = rscnStatsGroup.setStatus('current')
if mibBuilder.loadTexts: rscnStatsGroup.setDescription('A collection of objects for displaying RSCN statistics.')
rscnNotifyControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 3)).setObjects(("CISCO-RSCN-MIB", "rscnIlsRejReasonCode"), ("CISCO-RSCN-MIB", "rscnElsRejReasonCode"), ("CISCO-RSCN-MIB", "rscnIlsRejectReqNotifyEnable"), ("CISCO-RSCN-MIB", "rscnElsRejectReqNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnNotifyControlGroup = rscnNotifyControlGroup.setStatus('current')
if mibBuilder.loadTexts: rscnNotifyControlGroup.setDescription('A collection of notification control and notification information objects.')
rscnNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 4)).setObjects(("CISCO-RSCN-MIB", "rscnIlsRejectReqNotify"), ("CISCO-RSCN-MIB", "rscnElsRejectReqNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnNotifyGroup = rscnNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: rscnNotifyGroup.setDescription('A collection of notifications for monitoring ILS and ELS request rejection by the RSCN module.')
rscnConfigGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 5)).setObjects(("CISCO-RSCN-MIB", "rscnScrNumber"), ("CISCO-RSCN-MIB", "rscnScrRegType"), ("CISCO-RSCN-MIB", "rscnNotifyFcId"), ("CISCO-RSCN-MIB", "rscnMultiPidEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnConfigGroupRev1 = rscnConfigGroupRev1.setStatus('current')
if mibBuilder.loadTexts: rscnConfigGroupRev1.setDescription('A collection of objects for configuring and displaying SCR entries and multi-pid option.')
rscnConfigGroupRev1Sup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 6)).setObjects(("CISCO-RSCN-MIB", "rscnEventTov"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnConfigGroupRev1Sup1 = rscnConfigGroupRev1Sup1.setStatus('current')
if mibBuilder.loadTexts: rscnConfigGroupRev1Sup1.setDescription('A collection of object(s) for configuring the Event time out option.')
rscnRejectNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 7)).setObjects(("CISCO-RSCN-MIB", "rscnIlsRxRejectReqNotify"), ("CISCO-RSCN-MIB", "rscnElsRxRejectReqNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnRejectNotifyGroup = rscnRejectNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: rscnRejectNotifyGroup.setDescription('A collection of notifications for monitoring ILS and ELS request rejection by other switches/ devices.')
rscnNotifyControlGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 292, 2, 2, 8)).setObjects(("CISCO-RSCN-MIB", "rscnIlsRxRejectReqNotifyEnable"), ("CISCO-RSCN-MIB", "rscnElsRxRejectReqNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rscnNotifyControlGroupSup1 = rscnNotifyControlGroupSup1.setStatus('current')
if mibBuilder.loadTexts: rscnNotifyControlGroupSup1.setDescription('A collection of notification control objects.')
mibBuilder.exportSymbols("CISCO-RSCN-MIB", rscnScrTable=rscnScrTable, rscnNotifyFcId=rscnNotifyFcId, rscnIlsRxRejectReqNotifyEnable=rscnIlsRxRejectReqNotifyEnable, rscnMIBComplianceRev2=rscnMIBComplianceRev2, rscnMIBCompliance=rscnMIBCompliance, rscnRxRscns=rscnRxRscns, ciscoRscnMIB=ciscoRscnMIB, rscnIlsRejReasonCode=rscnIlsRejReasonCode, rscnScrTotalRejects=rscnScrTotalRejects, rscnConfigGroupRev1=rscnConfigGroupRev1, rscnStatsGroup=rscnStatsGroup, rscnNotifyControlGroup=rscnNotifyControlGroup, rscnScrEntry=rscnScrEntry, rscnMultiPidEntry=rscnMultiPidEntry, rscnRejectNotifyGroup=rscnRejectNotifyGroup, rscnSwRscnReqRej=rscnSwRscnReqRej, rscnElsRxRejectReqNotify=rscnElsRxRejectReqNotify, rscnNotifyControlGroupSup1=rscnNotifyControlGroupSup1, rscnElsRejectReqNotifyEnable=rscnElsRejectReqNotifyEnable, rscnMultiPidEnable=rscnMultiPidEnable, rscnEventTov=rscnEventTov, rscnNotifyGroup=rscnNotifyGroup, rscnEventTovEntry=rscnEventTovEntry, rscnSwRscnReqTotalRejects=rscnSwRscnReqTotalRejects, rscnMIBComplianceRev3=rscnMIBComplianceRev3, rscnStatsEntry=rscnStatsEntry, rscnNotifications=rscnNotifications, ciscoRscnMIBObjects=ciscoRscnMIBObjects, rscnInformation=rscnInformation, rscnIlsRxRejectReqNotify=rscnIlsRxRejectReqNotify, rscnScrFcId=rscnScrFcId, rscnElsRxRejectReqNotifyEnable=rscnElsRxRejectReqNotifyEnable, rscnElsRejReasonCode=rscnElsRejReasonCode, rscnScrRegType=rscnScrRegType, rscnTxSwRscns=rscnTxSwRscns, rscnNotification=rscnNotification, rscnMIBGroups=rscnMIBGroups, rscnConfigGroupRev1Sup1=rscnConfigGroupRev1Sup1, rscnMIBConformance=rscnMIBConformance, rscnRxScrs=rscnRxScrs, rscnRscnReqTotalRejects=rscnRscnReqTotalRejects, rscnRxSwRscns=rscnRxSwRscns, rscnMIBCompliances=rscnMIBCompliances, rscnStats=rscnStats, rscnScrRej=rscnScrRej, rscnIlsRejectReqNotify=rscnIlsRejectReqNotify, rscnEventTovTable=rscnEventTovTable, rscnTxRscns=rscnTxRscns, rscnConfigGroup=rscnConfigGroup, rscnRscnReqRej=rscnRscnReqRej, rscnScrNumber=rscnScrNumber, rscnIlsRejectReqNotifyEnable=rscnIlsRejectReqNotifyEnable, rscnElsRejectReqNotify=rscnElsRejectReqNotify, rscnMultiPidTable=rscnMultiPidTable, rscnConfiguration=rscnConfiguration, rscnMIBComplianceRev1=rscnMIBComplianceRev1, PYSNMP_MODULE_ID=ciscoRscnMIB, rscnStatsTable=rscnStatsTable)